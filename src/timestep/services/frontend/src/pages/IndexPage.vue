<template>
  <q-page padding>
    <!-- content -->
  </q-page>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
// import { useRouter } from 'vue-router';
// import { useQuery } from '@vue/apollo-composable';
// import gql from 'graphql-tag';

// import { Env } from 'components/models';
// import Agent, {
//   type Task
// } from 'agent-protocol'

export default defineComponent({
  name: 'IndexPage',
  setup () {
    // const router = useRouter();

    // const { result, loading, error } = useQuery(gql`
    //   query getEnvs {
    //     envs {
    //       id
    //       name
    //       namespace
    //     }
    //   }
    // `);

    // const fetchEnv = (env) => {
    //   return router.push(`/envs/${env.id}`);
    // };

    // const tasks = computed(() => result.value?.envs ?? [])
    // const columns = [
    //   {
    //     name: 'name',
    //     label: 'Name',
    //     field: 'name',
    //     align: 'left',
    //     sortable: true
    //   },
    //   {
    //     name: 'namespace',
    //     label: 'Namespace',
    //     field: 'namespace',
    //     align: 'left',
    //     sortable: true
    //   },
    // ]
    // const rows = tasks

    return {
      // columns,
      // error,
      // loading,
      // onRowClick: (row) => fetchEnv(row),
      // rows,
      // tasks,
    };
  }
});
</script>
