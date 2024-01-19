<template>
  <q-page padding>
    <!-- content -->
  </q-page>
</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

import { Env } from 'components/models';

export default defineComponent({
  name: 'EnvPage',

  setup () {
    const route = useRoute();

    const { result, loading, error, refetch } = useQuery(
      gql`
        query getEnv($envId: ID!) {
          env(id: $envId) {
            id
            name
            namespace
            description
          }
        }
      `,
      { envId: route.params.envId }
    );
  
    const env: Env = computed(() => result.value?.env ?? [])

    watch(
      () => route.params.envId,
      async (newId) => {
        console.log('newId', newId)
        if (newId) {
          refetch({ envId: newId });
        } else {
          console.log('no newId')
        }
      }
    );

    return {
      env,
      error,
      loading,
    }
  }
})
</script>
