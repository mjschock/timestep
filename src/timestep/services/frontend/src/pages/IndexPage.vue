<template>
  <div class="q-pa-md">
    <!-- <q-toggle v-model="loading" label="Loading state" class="q-mb-md" /> -->
    <q-table
      flat bordered
      title="Environments"
      :rows="rows"
      :columns="columns"
      row-key="name"
      :loading="loading"
    >
      <template v-slot:loading>
        <q-inner-loading showing color="primary" />
      </template>
      <template v-slot:body="props">
        <q-tr :props="props">
          <!-- <q-td key="id" :props="props">
            {{ props.row.id }}
          </q-td> -->
          <q-td key="name" :props="props" @click="onRowClick(props.row)" style="cursor: pointer">
            {{ props.row.name }}
          </q-td>
          <q-td key="namespace" :props="props">
            {{ props.row.namespace }}
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
  <!-- <q-page class="row items-center justify-evenly">
    <div class="q-pa-md">
      <q-table
        title="Environments"
        :rows="rows"
        :columns="columns"
        row-key="name"
      />
    </div>
  </q-page> -->
</template>

<script lang="ts">
import { Task, Todo, Meta } from 'components/models';
// import ExampleComponent from 'components/ExampleComponent.vue';
// import SkeletonComponent from 'components/SkeletonComponent.vue';
import { computed, defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

export default defineComponent({
  name: 'IndexPage',
  // components: { ExampleComponent },
  // components: { SkeletonComponent },
  setup () {
    const router = useRouter();

    const { result, loading, error } = useQuery(gql`
      query getEnvs {
        envs {
          id
          name
          namespace
        }
      }
    `);

    const fetchEnv = (env) => {
      return router.push(`/envs/${env.id}`);
    };

    const tasks = computed(() => result.value?.envs ?? [])
    const columns = [
      // {
      //   name: 'id',
      //   label: 'ID',
      //   field: 'id',
      //   align: 'left',
      //   sortable: false
      // },
      {
        name: 'name',
        label: 'Name',
        field: 'name',
        align: 'left',
        sortable: true
      },
      {
        name: 'namespace',
        label: 'Namespace',
        field: 'namespace',
        align: 'left',
        sortable: true
      },
    ]
    const rows = tasks
    // const todos = ref<Todo[]>([
    //   {
    //     id: 1,
    //     content: 'ct1'
    //   },
    //   {
    //     id: 2,
    //     content: 'ct2'
    //   },
    //   {
    //     id: 3,
    //     content: 'ct3'
    //   },
    //   {
    //     id: 4,
    //     content: 'ct4'
    //   },
    //   {
    //     id: 5,
    //     content: 'ct5'
    //   }
    // ]);
    const meta = ref<Meta>({
      totalCount: 1200
    });
    return {
      columns,
      loading,
      rows,
      tasks,
      meta,
      // onRowClick: (row) => alert(`${row.name} clicked`),
      onRowClick: (row) => fetchEnv(row)
    };
  }
});
</script>
