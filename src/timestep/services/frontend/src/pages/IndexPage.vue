<template>
  <div class="q-pa-md">
    <!-- <q-card class="my-card" flat bordered v-if="isAuthenticated"> -->
      <!-- <q-card-section>
        <div class="text-h6">Accounts</div>
        <div class="text-subtitle2">Primary</div>
      </q-card-section> -->

      <!-- <q-table
        title="Accounts"
        :rows="accounts"
        :columns="columns"
        row-key="id"
        :selected-rows-label="getSelectedString"
        selection="multiple"
        v-model:selected="selected"
      /> -->

      <!-- <q-separator /> -->

      <!-- <q-card-actions vertical v-if="selectedAccountTypeIsPrimary">
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
      </q-card-actions> -->

      <!-- <q-separator /> -->

      <!-- <agents-page v-if="isAuthenticated" /> -->
      <!-- <calendars-page v-if="isAuthenticated" /> -->
      <!-- <contacts-page v-if="isAuthenticated" /> -->
      <!-- <storage-page v-if="isAuthenticated" /> -->
    <!-- </q-card> -->
    <q-card class="my-card" flat bordered v-if="!isSignedIn">
      <!-- <q-card-section>
        <div class="text-h6">Our Changing Planet</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section> -->

      <q-tabs v-model="tab">
        <!-- <q-tab label="Accounts" name="accounts" />
        <q-tab label="Agents" name="agents" />
        <q-tab label="Calendars" name="calendars" />
        <q-tab label="Contacts" name="contacts" />
        <q-tab label="Documents" name="documents" /> -->
        <q-tab label="Sign in" name="sign-in" />
        <q-tab label="Sign up" name="sign-up" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab">
        <!-- <q-tab-panel name="accounts">
          <accounts-page />
        </q-tab-panel> -->

        <q-tab-panel name="sign-in">
          <sign-in-page />
        </q-tab-panel>

        <q-tab-panel name="sign-up">
          <sign-up-page />
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

import AgentsPage from 'src/pages/AgentsPage.vue';
import CalendarsPage from 'src/pages/CalendarsPage.vue';
import ContactsPage from 'src/pages/ContactsPage.vue';
import EssentialLink from 'components/EssentialLink.vue';
import LoginComponent from 'components/LoginComponent.vue';
import OauthLinks from 'src/components/OAuthLinks.vue'
import SignInPage from 'src/pages/SignInPage.vue'
import SignUpPage from'src/pages/SignUpPage.vue'
import StoragePage from 'src/pages/StoragePage.vue'

import { AuthChangeEvent, AuthChangedFunction, AuthErrorPayload, ChangePasswordParams, ChangePasswordResponse, Mfa, NhostClient, NhostSession, NhostSessionResponse, RedirectOption, ResetPasswordParams, ResetPasswordResponse, SendVerificationEmailParams, SendVerificationEmailResponse, SignInParams, SignInResponse, SignUpParams } from '@nhost/nhost-js'

import { nhost } from 'src/boot/nhost';
import gql from 'graphql-tag'

export default defineComponent({
  name: 'IndexPage',
  components: {
    // AgentsPage,
    // CalendarsPage,
    // ContactsPage,
    // OauthLinks,
    SignInPage,
    SignUpPage,
    // StoragePage,
  },
  setup () {
    const $q = useQuasar()
    // const columns = [
    //   {
    //     align: 'left',
    //     field: doc => doc.name,
    //     label: 'Name',
    //     name: 'name',
    //     sortable: true
    //   },
    //   {
    //     align: 'left',
    //     field: doc => doc.type,
    //     label: 'Type',
    //     name: 'type',
    //     sortable: true
    //   },
    //   // {
    //   //   align: 'left',
    //   //   field: doc => doc.id,
    //   //   label: 'ID',
    //   //   name: 'id',
    //   //   sortable: true
    //   // },
    // ]
    // const accounts = ref([])
    // const email = ref('')
    // const isAuthenticated = ref(false)
    const isSignedIn = ref(false)
    // const isLoading = ref(false)
    // const isPwd = ref(true)
    // const password = ref('')
    // const resendVerificationEmail = ref(false)
    // const resetPassword = ref(false)
    // const selected = ref([])
    // const submit = ref('sign-in')

    // async function getAccounts () {
    //   // const FILES = gql`
    //   //   query {
    //   //     files {
    //   //       id
    //   //       bucketId,
    //   //       name
    //   //     }
    //   //   }
    //   // `
    //   // const { data, error } = await nhost.graphql.request(FILES)

    //   // if (error) {
    //   //   console.error(error)
    //   //   return
    //   // }

    //   // accounts.value = data.files

    //   // const hasuraClaims = nhost.auth.getHasuraClaims()

    //   // if (hasuraClaims) {
    //   //   console.log('hasuraClaims', hasuraClaims)
    //   // }

    //   const user = nhost.auth.getUser()

    //   // if (user) {
    //   //   console.log('user', user)
    //   // }

    //   accounts.value = [{
    //     "name": user?.displayName,
    //     "id": user?.id,
    //     "type": "Primary"
    //   }]
    // }

    // getAccounts()

    // const toggleResendVerificationEmail = (val: boolean) => {
    //   resendVerificationEmail.value = val
    //   resetPassword.value = false
    // }

    // const toggleResetPassword = (val: boolean) => {
    //   resetPassword.value = val
    //   resendVerificationEmail.value = false
    // }

    const { isAuthenticated, isLoading } = nhost.auth.getAuthenticationStatus()

    isSignedIn.value = isAuthenticated

    nhost.auth.onAuthStateChanged((event: AuthChangeEvent, session: NhostSession | null) => {
      // console.log(
      //   `The auth state has changed. State is now ${event} with session: ${session}`
      // )

      if (event === 'SIGNED_IN') {
        isSignedIn.value = true
      } else {
        isSignedIn.value = false
      }
    })

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

    // const signUp = async (e: Event) => {
    //   e.preventDefault()

    //   const params: SignUpParams = {
    //     email: email.value,
    //     password: password.value,
    //   }
    //   const resp: NhostSessionResponse = await nhost.auth.signUp(params)
    //   const error: AuthErrorPayload | null = resp.error
    //   const session: NhostSession | null = resp.session

    //   if (error) {
    //     console.log('error', error)
    //     // submitResult.value.error = error.error
    //     // submitResult.value.message = error.message
    //     // submitResult.value.status = error.status
    //     $q.notify({
    //       color: 'negative',
    //       message: error.error,
    //       position: 'top',
    //       icon: 'report_problem',
    //     })
    //   }

    //   if (session) {
    //     console.log('session', session)
    //   }
    // }

    // const selectedAccountTypeIsPrimary = computed(() => {
    //   return selected.value.length === 1 && selected.value[0].type === 'Primary'
    // })

    return {
      // accounts,
      // columns,
      // changePassword,
      // email,
      // getSelectedString () {
      //   // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
      //   return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${accounts.value.length}`
      // },
      isSignedIn,
      // isLoading,
      // isPwd,
      // password,
      // resendVerificationEmail,
      // resetPassword,
      // selected,
      // selectedAccountTypeIsPrimary,
      // signIn,
      // signUp,
      // submit,
      tab: ref('sign-in'),
      // toggleResendVerificationEmail,
      // toggleResetPassword,
    };
  }
});
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
</style>
