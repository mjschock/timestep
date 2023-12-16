<template>
  <q-card-actions vertical>
    <div class="q-pa-md row justify-center">
      <div style="width: 100%; max-width: 400px">
        <!-- <q-chat-message
          v-for="message in messages"
          :key="message.id"
          :name="message.id"
          :avatar="message.avatarUrl"
          :stamp="message.timestamp"
          :text="[message.text]"
        /> -->
      </div>
    </div>
    <q-form>
      <q-card-actions vertical>
        <q-input
          label="Message"
          v-model="text"
        />
        <q-btn
          color="primary"
          label="Send message"
          no-caps
          type="button"
          @click="sendMessage()"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>
</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'
import { useRoute } from 'vue-router';
import { useQuery, useQueryLoading, useMutation, useMutationLoading, useSubscription, useSubscriptionLoading } from '@vue/apollo-composable';
import gql from 'graphql-tag';

const pageType = 'Thread'

export default defineComponent({
  name: `${pageType}Page`,
  setup () {
    // const route = useRoute();
    const text = ref('')

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

    const { mutate: sendMessage } = useMutation(gql`
      mutation sendMessage ($input: SendMessageInput!) {
        sendMessage (input: $input) {
          id
        }
      }
    `, () => ({
      variables: {
        input: {
          messages: [
            {
              "content": text.value,
              "role": "USER",
            }
          ],
        },
      },
    }))

    sendMessage({
      messages: [
        {
          "content": text.value,
          "role": "USER",
        }
      ],
    })

    return {
      // columns,
      // message,
      // messages,
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
