<template>
  <div class="q-pa-md">
    <q-card class="my-card" flat bordered v-if="isAuthenticated">
      <!-- <q-card-section>
        <div class="text-h6">Welcome to Timestep</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section>

      <q-separator /> -->

      <q-card-actions vertical>
        <q-form @submit="changePassword">
          <q-card-actions vertical>
            <q-input
              :type="isPwd ? 'password' : 'text'"
              label="Password"
              v-model="password"
              lazy-rules
            >
              <template v-slot:append>
                <q-icon
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  class="cursor-pointer"
                  @click="isPwd = !isPwd"
                />
              </template>
            </q-input>
            <q-btn
              color="primary"
              label="Change password"
              no-caps
              type="submit"
            />
          </q-card-actions>
        </q-form>
      </q-card-actions>
    </q-card>
    <q-card class="my-card" flat bordered v-if="!isAuthenticated">
      <!-- <q-card-section>
        <div class="text-h6">Our Changing Planet</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section> -->

      <q-tabs v-model="tab">
        <q-tab label="Sign in" name="sign-in" />
        <q-tab label="Sign up" name="sign-up" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="sign-in">
          <q-card-actions vertical>
            <q-form @submit="signIn">
              <q-card-actions vertical>
                <q-input
                  label="Email"
                  lazy-rules
                  type="email"
                  v-model="email"
                />
                <q-input
                  :type="isPwd ? 'password' : 'text'"
                  label="Password"
                  v-if="!resetPassword && !resendVerificationEmail"
                  v-model="password"
                  lazy-rules
                >
                  <template v-slot:append>
                    <q-icon
                      :name="isPwd ? 'visibility_off' : 'visibility'"
                      class="cursor-pointer"
                      @click="isPwd = !isPwd"
                    />
                  </template>
                </q-input>
                <q-toggle
                  v-model="resendVerificationEmail"
                  @update:model-value="toggleResendVerificationEmail"
                  label="Resend verification email?"
                />
                <q-toggle
                  v-model="resetPassword"
                  @update:model-value="toggleResetPassword"
                  label="Reset password?"
                />
                <q-btn
                  color="primary"
                  label="Sign in"
                  no-caps
                  type="submit"
                />
                <!-- <q-btn-toggle
                  color="primary"
                  no-caps
                  :options="[
                    {label: 'Sign in', value: 'sign-in'},
                    {label: 'Sign up', value: 'sign-up'}
                  ]"
                  type="submit"
                  v-model="submit"
                /> -->
              </q-card-actions>
            </q-form>
          </q-card-actions>
          <q-separator />
          <oauth-links />
        </q-tab-panel>

        <q-tab-panel name="sign-up">
          <q-card-actions vertical>
            <q-form @submit="signUp">
              <q-card-actions vertical>
                <q-input
                  v-model="email"
                  label="Email"
                  type="email"
                />
                <q-input
                  v-model="password"
                  label="Password"
                  type="password"
                />
                <q-btn
                  color="primary"
                  label="Sign up"
                  no-caps
                  type="submit"
                />
              </q-card-actions>
            </q-form>
          </q-card-actions>
          <q-separator />
          <oauth-links/>
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, reactive, ref, watch } from 'vue';
import { useQuasar } from 'quasar'
// import { useRouter } from 'vue-router';
// import { useQuery } from '@vue/apollo-composable';
// import gql from 'graphql-tag';

// import { Env } from 'components/models';
// import Agent, {
//   type Task
// } from 'agent-protocol'

import EssentialLink from 'components/EssentialLink.vue';
import LoginComponent from 'components/LoginComponent.vue';
import OauthLinks from 'src/components/OAuthLinks.vue'

import { AuthChangeEvent, AuthChangedFunction, AuthErrorPayload, ChangePasswordParams, ChangePasswordResponse, Mfa, NhostClient, NhostSession, NhostSessionResponse, RedirectOption, ResetPasswordParams, ResetPasswordResponse, SendVerificationEmailParams, SendVerificationEmailResponse, SignInParams, SignInResponse, SignUpParams } from '@nhost/nhost-js'

import { nhost } from 'src/boot/nhost';

export default defineComponent({
  name: 'IndexPage',
  components: {
    OauthLinks,
  },
  setup () {
    const $q = useQuasar()
    const email = ref('')
    const isAuthenticated = ref(false)
    const isLoading = ref(false)
    const isPwd = ref(true)
    const password = ref('')
    const resendVerificationEmail = ref(false)
    const resetPassword = ref(false)
    const submit = ref('sign-in')

    const toggleResendVerificationEmail = (val: boolean) => {
      resendVerificationEmail.value = val
      resetPassword.value = false
    }

    const toggleResetPassword = (val: boolean) => {
      resetPassword.value = val
      resendVerificationEmail.value = false
    }

    // const { isAuthenticated, isLoading } = nhost.auth.getAuthenticationStatus()

    nhost.auth.onAuthStateChanged((event: AuthChangeEvent, session: NhostSession | null) => {
      console.log(
        `The auth state has changed. State is now ${event} with session: ${session}`
      )

      if (event === 'SIGNED_IN') {
        isAuthenticated.value = true
      } else {
        isAuthenticated.value = false
      }
    })

    const changePassword = async (e: Event) => {
      e.preventDefault()

      const params: ChangePasswordParams = {
        newPassword: password.value,
      }
      const resp: ChangePasswordResponse = await nhost.auth.changePassword(params)
      const error: AuthErrorPayload | null = resp.error

      if (error) {
        console.log('error', error)
        $q.notify({
          color: 'negative',
          message: error.message,
          position: 'bottom',
          icon: 'report_problem',
        })
      }
    }

    const signIn = async (e: Event) => {
      e.preventDefault()

     if (resendVerificationEmail.value) {
        const hostname: string = window.location.hostname
        const redirectOptions: RedirectOption = {
          redirectTo: `https://${hostname}`,
        }
        const params: SendVerificationEmailParams = {
          email: email.value,
          options: redirectOptions,
        }
        const resp: SendVerificationEmailResponse = await nhost.auth.sendVerificationEmail(params)
        const error: AuthErrorPayload | null = resp.error

        if (error) {
          console.log('error', error)
          $q.notify({
            color: 'negative',
            message: error.message,
            position: 'bottom',
            icon: 'report_problem',
          })
        }

        return

      } else if (resetPassword.value) {
        const hostname: string = window.location.hostname
        const redirectOptions: RedirectOption = {
          redirectTo: `https://${hostname}`,
        }
        const params: ResetPasswordParams = {
          email: email.value,
          options: redirectOptions,
        }
        const resp: ResetPasswordResponse = await nhost.auth.resetPassword(params)
        const error: AuthErrorPayload | null = resp.error

        if (error) {
          console.log('error', error)
          $q.notify({
            color: 'negative',
            message: error.message,
            position: 'bottom',
            icon: 'report_problem',
          })
        }

        return

      } else {
        const params: SignInParams = {
          email: email.value,
          password: password.value,
        }
        const resp: SignInResponse = await nhost.auth.signIn(params)
        const error: AuthErrorPayload | null = resp.error
        const mfa: Mfa | null = resp.mfa
        const session: NhostSession | null = resp.session

        if (error) {
          console.log('error', error)
          // submitResult.value.error = error.error
          // submitResult.value.message = error.message
          // submitResult.value.status = error.status
          $q.notify({
            color: 'negative',
            message: error.message,
            position: 'bottom',
            icon: 'report_problem',
          })
        }

        if (mfa) {
          console.log('mfa', mfa)
        }

        if (session) {
          console.log('session', session)
        }
      }
    }

    const signUp = async (e: Event) => {
      e.preventDefault()

      const params: SignUpParams = {
        email: email.value,
        password: password.value,
      }
      const resp: NhostSessionResponse = await nhost.auth.signUp(params)
      const error: AuthErrorPayload | null = resp.error
      const session: NhostSession | null = resp.session

      if (error) {
        console.log('error', error)
        // submitResult.value.error = error.error
        // submitResult.value.message = error.message
        // submitResult.value.status = error.status
        $q.notify({
          color: 'negative',
          message: error.error,
          position: 'top',
          icon: 'report_problem',
        })
      }

      if (session) {
        console.log('session', session)
      }
    }

    return {
      changePassword,
      email,
      isAuthenticated,
      isLoading,
      isPwd,
      password,
      resendVerificationEmail,
      resetPassword,
      signIn,
      signUp,
      submit,
      tab: ref('sign-in'),
      toggleResendVerificationEmail,
      toggleResetPassword,
    };
  }
});
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 480px
</style>
