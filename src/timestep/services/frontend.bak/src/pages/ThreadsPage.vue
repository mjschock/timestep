<template>
  <q-table
    :title="title"
    :rows="rows"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />

  <q-card-actions vertical v-if="selected.length > 0">
    <q-card-actions vertical>
      <!-- <div class="q-mt-md">
        Selected: {{ JSON.stringify(selected) }}
      </div> -->
      <q-btn
        color="primary"
        label="View environment"
        no-caps
        type="button"
        @click="viewThread"
      />
    </q-card-actions>
  </q-card-actions>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue';
import { api } from 'boot/axios';
import { nhost } from 'src/boot/nhost';
import { useRouter } from 'vue-router';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

const pageType = 'Environment';

export default defineComponent({
  name: `${pageType}sPage`,
  setup() {
    const columns = [
      {
        align: 'left',
        field: (row) => row.id,
        label: 'ID',
        name: 'id',
        sortable: true,
      },
    ];
    const rows = ref([]);
    const selected = ref([]);
    const title = `${pageType}s`;
    const router = useRouter();

    // const { result, loading, error, refetch } = useQuery(
    //   gql`
    //     query GetThreads {
    //       threads {
    //         id
    //         messageIds
    //       }
    //     }
    //   `,
    //   { }
    // );

    // const rows = computed(() => result.value?.threads ?? [])
    const selectedThread = computed(() => selected.value[0] ?? {});

    const getThreads = async () => {
      api
        .get(`/threads`, {
          headers: {
            Authorization: `Bearer ${nhost.auth.getAccessToken()}`,
          },
        })
        .then((response) => {
          // agents.value = response.data
          // console.log(response.data)
          rows.value = response.data.threads;
        })
        .catch((error) => {
          // notif({
          //   color: 'negative',
          //   message: error.message,
          //   position: 'top',
          //   icon: 'report_problem',
          //   spinner: false,
          //   timeout: 5000,
          // })
          console.log(error);
        });
    };

    onMounted(() => {
      getThreads();
    });

    const viewThread = () => {
      router.push(`/threads/${selectedThread.value.id}`);
    };

    return {
      columns,
      rows,
      selected,
      title,
      getSelectedString() {
        return selected.value.length === 0
          ? ''
          : `${selected.value.length} ${pageType.toLowerCase()}${
              selected.value.length > 1 ? 's' : ''
            } selected of ${rows.value.length}`;
      },
      selectedThread,
      viewThread,
    };
  },
});
</script>
