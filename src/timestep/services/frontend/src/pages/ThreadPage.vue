<template>
  <q-card-actions vertical>
    <div class="q-pa-md row justify-center">
      <div style="width: 100%; max-width: 400px">
        <q-chat-message
          v-for="message in messages"
          :bg-color="message.role === 'user' ? 'primary' : 'amber'"
          :key="message.id"
          :avatar="message.role === 'user' ? message.avatarUrl : 'https://robohash.org/4975920e-a4e3-11ee-a55c-17ba192d0095'"
          :sent="message.role === 'user'"
          :stamp="message.timestamp"
          :text="[message.content]"
          :text-color="message.role === 'user' ? 'white' : 'black'"
        />

        <q-chat-message v-if="loading"
          avatar="https://robohash.org/4975920e-a4e3-11ee-a55c-17ba192d0095"
          bg-color="amber"
        >
          <q-spinner-dots size="2rem" />
        </q-chat-message>
      </div>
    </div>
    <q-form>
      <q-card-actions vertical>
        <q-input
          label="Message"
          v-model="text"
          :disable="loading"
          @keyup.enter="sendMessage()"
        />
        <q-btn
          color="primary"
          label="Send message"
          no-caps
          type="button"
          @click="sendMessage()"
          :disable="loading || text.length === 0"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref, watch } from 'vue'
import { api } from 'boot/axios'
import { nhost } from 'src/boot/nhost';
import { useRoute } from 'vue-router';
import { useQuery, useQueryLoading, useMutation, useMutationLoading, useSubscription, useSubscriptionLoading } from '@vue/apollo-composable';
import gql from 'graphql-tag';
import { Console } from 'console';

const pageType = 'Thread'

export default defineComponent({
  name: `${pageType}Page`,
  setup () {
    const route = useRoute();
    const text = ref('')
    const loading = ref(false)

    // const columns = [
    //   {
    //     align: 'left',
    //     field: row => row.id,
    //     label: 'ID',
    //     name: 'id',
    //     sortable: true
    //   },
    // ]
    // // const rows = ref([])
    // const selected = ref([])
    // const title = `${pageType}`

    // const { result, loading, error, refetch } = useQuery(
    //   gql`
    //     query GetThread($threadId: ID!) {
    //       thread(id: $threadId) {
    //         id
    //         messageIds
    //       }

    //       messages(threadId: $threadId) {
    //         id
    //         text
    //         timestamp
    //         avatarUrl
    //       }
    //     }
    //   `,
    //   { threadId: route.params.threadId }
    // );

    // watch(
    //   () => route.params.threadId,
    //   async (newId) => {
    //     console.log('newId', newId)
    //     if (newId) {
    //       refetch({ threadId: newId });
    //     } else {
    //       console.log('no newId')
    //     }
    //   }
    // );

    // const rows = computed(() => result.value?.threads ?? [])
    // const selectedThread = computed(() => selected.value[0] ?? {})

    // const message = ref('')
    // const messages = computed(() => result.value?.messages ?? [])
    const messages = ref([])
    // const messagesLoading = computed(() => loading.value)
    // const messagesError = computed(() => error.value)

    // const sendMessage = async (e: Event) => {
    //   console.log('sendMessage', message.value)
    //   e.preventDefault()

    //   const params = {
    //     threadId: route.params.threadId,
    //     text: message.value,
    //   }

    //   console.log('params', params)

    //   const { mutate } = useMutation(
    //     gql`
    //       mutation PostMessage($threadId: ID!, $text: String!) {
    //         postMessage(threadId: $threadId, text: $text) {
    //           id
    //           text
    //           timestamp
    //           avatarUrl
    //         }
    //       }
    //     `,
    //     params
    //   );
    // }

    // const { mutate: sendMessage } = useMutation(gql`
    //   mutation sendMessage ($input: SendMessageInput!) {
    //     sendMessage (input: $input) {
    //       id
    //     }
    //   }
    // `, () => ({
    //   variables: {
    //     input: {
    //       messages: [
    //         {
    //           "content": text.value,
    //           "role": "USER",
    //         }
    //       ],
    //     },
    //   },
    // }))

    // sendMessage({
    //   messages: [
    //     {
    //       "content": text.value,
    //       "role": "USER",
    //     }
    //   ],
    // })

    const getMessages = async () => {
      loading.value = true

      api.get(
        `/threads/${route.params.threadId}/messages`,
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
        },
      )
        .then((response) => {
      //     // agents.value = response.data
          // console.log(response.data)
          messages.value = response.data.messages
          loading.value = false
        })
        .catch((error) => {
      //     // notif({
      //     //   color: 'negative',
      //     //   message: error.message,
      //     //   position: 'top',
      //     //   icon: 'report_problem',
      //     //   spinner: false,
      //     //   timeout: 5000,
      //     // })
          console.log(error)
          loading.value = false
        })
    }

    const sendMessage = async () => {
      loading.value = true
      const content = text.value
      text.value = ''

      messages.value.push(
        {
          // id: '1',
          content: content,
          role: 'user',
          // timestamp: new Date().toISOString(),
          // timestamp: new Date().toDateString(),
          // timestamp: new Date().toISOString().slice(0, 19).replace("T", " "),
          // avatarUrl: '
        }
      )

      api.post(
        `/threads/${route.params.threadId}/messages`,
        {
          content: content
          // messages: 
        },
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
          responseType: 'stream',
        },
      )
        .then((response) => {
          // console.log('response', response)
          // console.log(response.data)
          // console.log(response.data.data)
          const data = JSON.parse(response.data)
          // console.log(data.data.message)
          const message = data.data.message
          messages.value.push(data.data.message)
          // messages.value = response.data
          // console.log('json', response.json())
      //     // agents.value = response.data
          // console.log(response.data)
          // console.log('response.data', response.data)
          // messages.value = response.data.messages
          // messages.value.push(response.data.message)
          // response.data.on('data', (chunk) => {
          //   console.log('chunk', chunk)
          //   // messages.value.push(chunk)
          // })

          // response.data.on('end', () => {
          //   console.log('end')
          //   // getMessages()
          // })
          loading.value = false
        })
        .catch((error) => {
      //     // notif({
      //     //   color: 'negative',
      //     //   message: error.message,
      //     //   position: 'top',
      //     //   icon: 'report_problem',
      //     //   spinner: false,
      //     //   timeout: 5000,
      //     // })
          console.log(error)
          loading.value = false
        })
    }

    onMounted(() => {
      getMessages()
    })

    return {
      // columns,
      loading,
      // message,
      messages,
      // messagesLoading,
      // messagesError,
      sendMessage,
      text,
      // rows,
      // selected,
      // title,
      // getSelectedString () {
      //   return selected.value.length === 0 ? '' : `${selected.value.length} ${pageType.toLowerCase()}${selected.value.length > 1 ? 's' : ''} selected of ${rows.value.length}`
      // },
      // selectedThread,
    }
  }
})
</script>
