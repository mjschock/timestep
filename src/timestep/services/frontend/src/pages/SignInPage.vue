<template>
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
        <q-dialog v-model="prompt" persistent>
          <q-card style="min-width: 350px">
            <!-- <q-card-section> -->
              <!-- <div class="text-h6">Your address</div> -->
              <!-- <q-img :src="totp.imageUrl" /> -->
              <!-- <div class="text-h6">Your secret</div> -->
              <!-- <div class="text-subtitle2">{{ totp.totpSecret }}</div> -->
            <!-- </q-card-section> -->

            <q-card-section class="q-pt-none">
              <!-- <q-input dense v-model="totp.code" autofocus @keyup.enter="prompt = false" /> -->
              <q-input dense v-model="totp.totpCode" autofocus />
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
              <q-btn flat label="Cancel" v-close-popup />
              <!-- <q-btn flat label="Verify" v-close-popup /> -->
              <q-btn flat label="Verify" @click="verifyMfa" />
            </q-card-actions>
          </q-card>
        </q-dialog>
      </q-card-actions>
    </q-form>
  </q-card-actions>
  <!-- <q-separator /> -->
  <!-- <oauth-links /> -->
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { 
  AuthErrorPayload,
  Mfa,
  NhostClient,
  NhostSession,
  NhostSessionResponse,
  RedirectOption,
  ResetPasswordParams,
  ResetPasswordResponse,
  SendVerificationEmailParams,
  SendVerificationEmailResponse,
  SignInParams,
  SignInResponse,
  SignUpParams
} from '@nhost/nhost-js'
import { api } from 'boot/axios'
import { nhost } from 'src/boot/nhost';
import OAuthLinks from 'src/components/OAuthLinks.vue'
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'SignInPage',

  components: {
    // OAuthLinks,
  },

  setup () {
    const email = ref('')
    const isPwd = ref(true)
    const password = ref('')
    const prompt = ref(false)
    const resendVerificationEmail = ref(false)
    const resetPassword = ref(false)
    const totp = ref({
      mfa: {
        ticket: '',
      },
      totpCode: '',
    })
    const $q = useQuasar()

    // const changePassword = async (e: Event) => {
    //   e.preventDefault()

    //   const params: ChangePasswordParams = {
    //     newPassword: password.value,
    //   }
    //   const resp: ChangePasswordResponse = await nhost.auth.changePassword(params)
    //   const error: AuthErrorPayload | null = resp.error

    //   if (error) {
    //     console.log('error', error)
    //     $q.notify({
    //       color: 'negative',
    //       message: error.message,
    //       position: 'bottom',
    //       icon: 'report_problem',
    //     })
    //   }
    // }

    const signIn = async (e: Event) => {
      e.preventDefault()

      const notif = $q.notify({
        group: false, // required to be updatable
        position: 'top',
        timeout: 0, // we want to be in control when it gets dismissed
        spinner: true,
        message: 'Signing in...',
        // caption: '0%'
      })

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
          // console.log('error', error)
          // $q.notify({
          //   color: 'negative',
          //   message: error.message,
          //   position: 'top',
          //   icon: 'report_problem',
          // })
          notif({
            color: 'negative',
            message: error.message,
            position: 'top',
            icon: 'report_problem',
            spinner: false,
            timeout: 5000,
          })
        } else {
          // $q.notify({
          //   color: 'positive',
          //   multiLine: true,
          //   message: 'Please click the link in the email we sent you to verify your account',
          //   position: 'top',
          //   icon: 'check_circle',
          // })
          notif({
            color: 'positive',
            multiLine: true,
            message: 'Please click the link in the email we sent you to verify your account',
            position: 'top',
            icon: 'check_circle',
            spinner: false,
            timeout: 5000,
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
          notif({
            color: 'negative',
            message: error.message,
            position: 'top',
            icon: 'report_problem',
            spinner: false,
            timeout: 5000,
          })
        } else {
          notif({
            color: 'positive',
            multiLine: true,
            message: 'Please click the link in the email we sent you to reset your password',
            position: 'top',
            icon: 'check_circle',
            spinner: false,
            timeout: 5000,
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

        // if (session) {
        //   console.log('session', session)
        // }

        if (error) {
          notif({
            color: 'negative',
            message: error.message,
            position: 'top',
            icon: 'report_problem',
            spinner: false,
            timeout: 5000,
          })
        } else {
          if (mfa && mfa.ticket) {
            notif({
              color: 'info',
              multiLine: true,
              message: 'Please enter the code from your authenticator app',
              position: 'top',
              icon: 'check_circle',
              spinner: false,
              timeout: 5000,
            })

            prompt.value = true
            // totp.mfa.ticket.value = mfa.ticket
            totp.value.mfa.ticket = mfa.ticket
          } else {
            notif({
              color: 'positive',
              multiLine: true,
              message: 'Signed in',
              position: 'top',
              icon: 'check_circle',
              spinner: false,
              timeout: 5000,
            })
          }
        }
      }
    }

    const toggleResendVerificationEmail = (val: boolean) => {
      resendVerificationEmail.value = val
      resetPassword.value = false
    }

    const toggleResetPassword = (val: boolean) => {
      resetPassword.value = val
      resendVerificationEmail.value = false
    }

    const verifyMfa = async (e: Event) => {
      e.preventDefault()

      const notif = $q.notify({
        group: false, // required to be updatable
        position: 'top',
        timeout: 0, // we want to be in control when it gets dismissed
        spinner: true,
        message: 'Verifying MFA...',
        // caption: '0%'
      })

      const params: SignInParams = {
        otp: totp.value.totpCode,
      }
      const resp: SignInResponse = await nhost.auth.signIn(params)
      const error: AuthErrorPayload | null = resp.error
      const mfa: Mfa | null = resp.mfa
      const session: NhostSession | null = resp.session

      // if (session) {
      //   console.log('session', session)
      // }

      if (error) {
        // console.log('error', error)
        notif({
          color: 'negative',
          message: error.message,
          position: 'top',
          icon: 'report_problem',
          spinner: false,
          timeout: 5000,
        })
      } else {
        // console.log('response', response)
        prompt.value = false
        notif({
          color: 'positive',
          message: 'MFA verified',
          position: 'top',
          icon: 'check_circle',
          spinner: false,
          timeout: 5000,
        })
      }

      // api.put(
      //   // `/users/${selected.value[0].id}`,
      //   `/users/me`,
      //   {
      //     mfa: {
      //       ticket: totp.value.mfa.ticket,
      //     },
      //     totpCode: totp.value.totpCode,
      //   },
      //   {
      //     headers: {
      //       'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
      //     },
      //   },
      // )
      //   .then((response) => {
      //     console.log('response', response)
      //     prompt.value = false
      //     notif({
      //       color: 'positive',
      //       message: 'MFA verified',
      //       position: 'top',
      //       icon: 'check_circle',
      //       spinner: false,
      //       timeout: 5000,
      //     })
      //   })
      //   .catch((error) => {
      //     console.log('error', error)
      //     notif({
      //       color: 'negative',
      //       message: error.message,
      //       position: 'top',
      //       icon: 'report_problem',
      //       spinner: false,
      //       timeout: 5000,
      //     })
      //   })
    }

    return {
      email,
      isPwd,
      password,
      prompt,
      resendVerificationEmail,
      resetPassword,
      toggleResendVerificationEmail,
      toggleResetPassword,
      signIn,
      totp,
      verifyMfa,
    }
  }
})
</script>
