<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 350px">
      <q-list bordered padding>
        <q-item>
          <q-item-section>
            <q-item-label overline>Environment</q-item-label>
            <q-item-label>{{ env.name }}</q-item-label>
            <q-item-label caption>{{ env.description }}</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label caption>{{ env.namespace }}</q-item-label>
          </q-item-section>
        </q-item>

        <q-separator spaced />
        <q-item-label header>Agents</q-item-label>

        <q-item>
          <q-item-section avatar>
            <q-icon name="person_add" />
          </q-item-section>
          <q-item-section>Human</q-item-section>
          <!-- <q-item-section side>
            <q-item-label caption>meta</q-item-label>
          </q-item-section> -->
        </q-item>

        <q-item>
          <q-item-section avatar>
            <q-icon name="person" />
          </q-item-section>
          <q-item-section>Player 0</q-item-section>
          <!-- <q-item-section side>
            <q-item-label caption>meta</q-item-label>
          </q-item-section> -->
        </q-item>

        <!-- <q-separator spaced inset="item" /> -->

        <!-- <q-item>
          <q-item-section avatar>
            <q-avatar color="primary" icon="person" />
          </q-item-section>

          <q-item-section>
            <q-item-label>Human</q-item-label>
            <q-item-label caption lines="2">Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label caption>5 min ago</q-item-label>
            <q-icon name="star" color="yellow" />
          </q-item-section>
        </q-item> -->

        <!-- <q-separator spaced inset="item" />

        <q-item>
          <q-item-section top avatar>
            <q-avatar color="primary" text-color="white" square icon="bluetooth" />
          </q-item-section>

          <q-item-section>
            <q-item-label>Single line item</q-item-label>
            <q-item-label caption>Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label caption>meta</q-item-label>
          </q-item-section>
        </q-item>

        <q-separator spaced inset="item" /> -->

        <!-- <q-item>
          <q-item-section top avatar>
            <q-avatar>
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
          </q-item-section>

          <q-item-section>
            <q-item-label>Single line item</q-item-label>
            <q-item-label caption>Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-badge label="10k" />
          </q-item-section>
        </q-item> -->

        <!-- <q-separator spaced inset="item" />

        <q-item>
          <q-item-section top avatar>
            <q-avatar rounded>
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
          </q-item-section>

          <q-item-section>
            <q-item-label>Single line item</q-item-label>
            <q-item-label caption>Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label caption>meta</q-item-label>
          </q-item-section>
        </q-item> -->

        <!-- <q-separator spaced /> -->

        <!-- <q-item>
          <q-item-section top thumbnail class="q-ml-none">
            <img src="https://cdn.quasar.dev/img/mountains.jpg">
          </q-item-section>

          <q-item-section>
            <q-item-label>Single line item</q-item-label>
            <q-item-label caption>Secondary line text. Lorem ipsum dolor sit amet, consectetur adipiscit elit.</q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label caption>meta</q-item-label>
          </q-item-section>
        </q-item> -->
      </q-list>
    </div>
  </q-page>
</template>

<script lang="ts">
import { computed, defineComponent, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

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

    // watch(result, (newValue, oldValue) => {
    //   console.log(newValue)
    //   console.log(oldValue)
    //   console.log(result.value)
    // })

    // const environments = useResult(result, null, (data) => data.environment);

    // const fetchEnv = (env) => {
    //   return router.push(`/envs/${env.id}`);
    // };
  
    // const toolbarOnclick = () => {
    //   console.log('toolbarOnclick')
    //   router.push(`/`)
    // }
  
    const env = computed(() => result.value?.env ?? [])

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
      // "environments": result.value?.data?.envs,
      // environments: result.value?.data?.envs,
      // environments: result.value?.data?.envs,
      // result,
      env,
      loading,
      error,
      // essentialLinks: linksList,
      // leftDrawerOpen,
      // fetchEnv,
      // toggleLeftDrawer () {
      //   leftDrawerOpen.value = !leftDrawerOpen.value
      // },
      // toolbarOnclick,

      // rightDrawerOpen,
      // toggleRightDrawer () {
      //   rightDrawerOpen.value = !rightDrawerOpen.value
      // }
    }
  }
})
</script>
