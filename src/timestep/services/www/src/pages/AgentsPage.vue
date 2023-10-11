<template>
  <q-page padding>
    <q-item v-for="agent in agents" :key="agent.id">
      <q-item-section class="my-box cursor-pointer q-hoverable">
        <q-item-label>
          {{ agent.title }}
        </q-item-label>
        <q-item-label caption>ID: {{ agent.id }}</q-item-label>
        <q-item-label>
          {{ agent.content }}
        </q-item-label>
      </q-item-section>
    </q-item>
  </q-page>
</template>

<script lang="ts">
// import { defineComponent } from 'vue'
// export default defineComponent({
//   // name: 'PageName'
// })

import { watch } from "vue";
import { useQuery, useResult } from "@vue/apollo-composable";
import { useRoute } from "vue-router";
import gql from "graphql-tag";

export default {
  name: "PageName",

  setup() {
    const route = useRoute();

    const { result, loading, error, refetch } = useQuery(
      gql`
        query agentsQuery($environmentId: Int!) {
          agents(where: { environment_id: { _eq: $environmentId } }) {
            id
            title
            content
          }
        }
      `,
      {
        environmentId: route.params.environmentId,
      }
    );

    const agents = useResult(result, null, (data) => data.agent);

    watch(
      () => route.params.environmentId,
      async (newId) => {
        refetch({ agentId: newId });
      }
    );

    return {
      agents,
    };
  },
};
</script>
