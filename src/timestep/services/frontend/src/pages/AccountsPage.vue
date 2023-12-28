<template>
  <q-table
    title="Accounts"
    :rows="accounts"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />

  <q-card-actions vertical v-if="selectedAccountTypeIsPrimary">
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
    <q-form @submit="enableMfa">
      <q-card-actions vertical>
        <q-btn
          color="primary"
          label="Enable MFA TOTP"
          no-caps
          type="submit"
          disabled
        />
      </q-card-actions>
    </q-form>
    <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <!-- <div class="text-h6">Your address</div> -->
          <q-img :src="totp.imageUrl" />
          <!-- <div class="text-h6">Your secret</div> -->
          <div class="text-subtitle2">{{ totp.totpSecret }}</div>
        </q-card-section>

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
    <q-form @submit="deleteAccount">
      <q-card-actions vertical>
        <q-btn
          color="negative"
          label="Delete account"
          no-caps
          type="submit"
          disabled
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'
import { api } from 'boot/axios'
import { nhost } from 'src/boot/nhost';
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'AccountsPage',
  setup () {
    const accounts = ref([])
    const columns = [
      {
        align: 'left',
        field: account => account.displayName,
        label: 'Display Name',
        name: 'name',
        sortable: true
      },
      {
        align: 'left',
        field: account => account.type,
        label: 'Type',
        name: 'type',
        sortable: true
      }
    ]
    const isPwd = ref(true)
    const password = ref('')
    const prompt = ref(false)
    const selected = ref([])
    const selectedAccountTypeIsPrimary = computed(() => {
      return selected.value.length === 1 && selected.value[0].type === 'Primary'
    })
    const totp = ref({
      imageUrl: '',
      totpSecret: '',
      totpCode: '',
    })
    const $q = useQuasar()

    // const isAuthenticated = nhost.auth.isAuthenticated()

    // if (isAuthenticated) {
    //   console.log('User is authenticated')
    // }

    const changePassword = async (e: Event) => {
      e.preventDefault()

      const notif = $q.notify({
        group: false, // required to be updatable
        position: 'top',
        timeout: 0, // we want to be in control when it gets dismissed
        spinner: true,
        message: 'Changing password...',
        // caption: '0%'
      })

      const params: ChangePasswordParams = {
        newPassword: password.value,
      }
      const resp: ChangePasswordResponse = await nhost.auth.changePassword(params)
      const error: AuthErrorPayload | null = resp.error

      if (error) {
      //   $q.notify({
      //     color: 'negative',
      //     message: error.message,
      //     position: 'bottom',
      //     icon: 'report_problem',
      //   })
      // }
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
          message: 'Password changed',
          position: 'top',
          icon: 'check_circle',
          spinner: false,
          timeout: 5000,
        })
      }
    }

    const data = ref(null)

    const enableMfa = async (e: Event) => {
      e.preventDefault()

      // const notif = $q.notify({
      //   group: false, // required to be updatable
      //   position: 'top',
      //   timeout: 0, // we want to be in control when it gets dismissed
      //   spinner: true,
      //   message: 'Enabling MFA...',
      //   // caption: '0%'
      // })

      // const params: EnableMfaParams = {
      //   type: 'totp',
      // }
      // const resp: EnableMfaResponse = await nhost.auth.enableMfa(params)
      // const error: AuthErrorPayload | null = resp.error

      // type Data = {
      //   message: string
      // }

      // type Body = {
      //   email: string
      //   name: string
      // }

      // type ErrorMessage = {
      //   message: string
      // }

      // // The function will only accept a body of type `Body`
      // const { res, error } = await nhost.functions.call<Data, Body, ErrorMessage>(
      //   'accounts',
      //   { id: selected.value[0].id },
      // )

      // const params: DeleteAccountParams = {
      //   id: selected.value[0].id,
      // }
      // const resp: DeleteAccountResponse = await nhost.functions.call('delete-account', params)
      // const error: AuthErrorPayload | null = resp.error


      api.put(
        `/accounts/${selected.value[0].id}`,
        {
          mfa: {
            enabled: true,
            type: 'totp',
          }
        },
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
        },
      )
        .then((response) => {
          // console.log('response', response)
          // prompt.value = false
          // notif({
          //   color: 'positive',
          //   message: 'MFA enabled',
          //   position: 'top',
          //   icon: 'check_circle',
          //   spinner: false,
          //   timeout: 5000,
          // })
          const imageUrl = res?.data.imageUrl
          const totpSecret = res?.data.totpSecret

          if (imageUrl && totpSecret) {
            totp.value = {
              imageUrl,
              totpSecret,
              totpCode: '',
            }
            prompt.value = true
          }
        })
        .catch((error) => {
          console.log('error', error)
          // notif({
          //   color: 'negative',
          //   message: error.message,
          //   position: 'top',
          //   icon: 'report_problem',
          //   spinner: false,
          //   timeout: 5000,
          // })
        })

      // console.log('res', res)
      // console.log('error', error)

      // if (error) {
      // //   notif({
      // //     color: 'negative',
      // //     message: error.message,
      // //     position: 'top',
      // //     icon: 'report_problem',
      // //     spinner: false,
      // //     timeout: 5000,
      // //   })
      //   console.log('error', error)
      // } else {
      // //   notif({
      // //     color: 'positive',
      // //     message: 'MFA enabled',
      // //     position: 'top',
      // //     icon: 'check_circle',
      // //     spinner: false,
      // //     timeout: 5000,
      // //   })
      // // }
      //   console.log('res', res)
      //   const imageUrl = res?.data.imageUrl
      //   const totpSecret = res?.data.totpSecret

      //   if (imageUrl && totpSecret) {
      //     totp.value = {
      //       imageUrl,
      //       totpSecret,
      //       totpCode: '',
      //     }
      //     prompt.value = true
      //   }
      // }
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

      api.put(
        `/users/${selected.value[0].id}`,
        {
          activeMfaType: 'totp',
          totpCode: totp.value.totpCode,
        },
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
        },
      )
        .then((response) => {
          console.log('response', response)
          prompt.value = false
          notif({
            color: 'positive',
            message: 'MFA verified',
            position: 'top',
            icon: 'check_circle',
            spinner: false,
            timeout: 5000,
          })
        })
        .catch((error) => {
          console.log('error', error)
          notif({
            color: 'negative',
            message: error.message,
            position: 'top',
            icon: 'report_problem',
            spinner: false,
            timeout: 5000,
          })
        })
    }

    const deleteAccount = async (e: Event) => {
      e.preventDefault()

      // const notif = $q.notify({
      //   group: false, // required to be updatable
      //   position: 'top',
      //   timeout: 0, // we want to be in control when it gets dismissed
      //   spinner: true,
      //   message: 'Deleting account...',
      //   // caption: '0%'
      // })

      // api.delete(`/accounts/${selected.value[0].id}`)
      //   .then((response) => {
      //     notif({
      //       color: 'positive',
      //       message: 'Account deleted',
      //       position: 'top',
      //       icon: 'check_circle',
      //       spinner: false,
      //       timeout: 5000,
      //     })
      //   })
      //   .catch((error) => {
      //     notif({
      //       color: 'negative',
      //       message: error.message,
      //       position: 'top',
      //       icon: 'report_problem',
      //       spinner: false,
      //       timeout: 5000,
      //     })
      //   })

      type Data = {
        message: string
      }

      type Body = {
        email: string
        name: string
      }

      type ErrorMessage = {
        message: string
      }

      // The function will only accept a body of type `Body`
      const { res, error } = await nhost.functions.call<Data, Body, ErrorMessage>(
        'accounts',
        { id: selected.value[0].id },
      )

      // const params: DeleteAccountParams = {
      //   id: selected.value[0].id,
      // }
      // const resp: DeleteAccountResponse = await nhost.functions.call('delete-account', params)
      // const error: AuthErrorPayload | null = resp.error

      console.log('res', res)
      console.log('error', error)

      // Now the response data is typed as `Data`
      // console.log(res?.data.message)

      // Now the error message is typed as `ErrorMessage`
      // console.log(error?.message.error)

      // if (error) {
      //   notif({
      //     color: 'negative',
      //     message: error.message,
      //     position: 'top',
      //     icon: 'report_problem',
      //     spinner: false,
      //     timeout: 5000,
      //   })
      // } else {
      //   notif({
      //     color: 'positive',
      //     message: 'Account deleted',
      //     position: 'top',
      //     icon: 'check_circle',
      //     spinner: false,
      //     timeout: 5000,
      //   })
      // }
    }

    // async function getAccounts () {
    function getAccounts () {
      // const FILES = gql`
      //   query {
      //     files {
      //       id
      //       bucketId,
      //       name
      //     }
      //   }
      // `
      // const { data, error } = await nhost.graphql.request(FILES)

      // if (error) {
      //   console.error(error)
      //   return
      // }

      // accounts.value = data.files

      // const hasuraClaims = nhost.auth.getHasuraClaims()

      // if (hasuraClaims) {
      //   console.log('hasuraClaims', hasuraClaims)
      // }

      const user = nhost.auth.getUser()

      if (user) {
        console.log('user', user)
      }

      accounts.value = [{
        "activeMfaType": user?.activeMfaType,
        "avatarUrl": user?.avatarUrl,
        "createdAt": user?.createdAt,
        "defaultRole": user?.defaultRole,
        "displayName": user?.displayName,
        "email": user?.email,
        "emailVerified": user?.emailVerified,
        "id": user?.id,
        "isAnonymous": user?.isAnonymous,
        "locale": user?.locale,
        "metadata": user?.metadata,
        "phoneNumber": user?.phoneNumber,
        "phoneNumberVerified": user?.phoneNumberVerified,
        "roles": user?.roles,
        "type": "Primary",
      }]
    }

    getAccounts()

    return {
      accounts,
      changePassword,
      columns,
      deleteAccount,
      enableMfa,
      getSelectedString () {
        // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
        return selected.value.length === 0 ? '' : `${selected.value.length} account${selected.value.length > 1 ? 's' : ''} selected of ${accounts.value.length}`
      },
      isPwd,
      password,
      prompt,
      selected,
      selectedAccountTypeIsPrimary,
      totp,
      verifyMfa,
      // getSelectedString () {
      //   return `${this.selected.length} selected`
      // }
    }
  }
})
</script>
