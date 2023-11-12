<template>
  <q-layout view="hHh LpR fFf">
    <q-header elevated>
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        /> -->

        <q-toolbar-title
          class="my-box cursor-pointer q-hoverable"
          @click="toolbarOnclick"
        >
          Timestep AI
        </q-toolbar-title>

        <!-- <div>Quasar v{{ $q.version }}</div> -->

        <!-- <q-btn
          flat
          dense
          round
          icon="more_vert"
          aria-label="More"
          @click="toggleRightDrawer"
        /> -->
      </q-toolbar>

      <!-- <q-linear-progress dark indeterminate color="secondary" class="q-mt-sm" /> -->
      <!-- <q-linear-progress dark query color="secondary" class="q-mt-sm" /> -->
      <!-- <q-tabs align="left">
        <q-route-tab to="/agents" label="Agents" />
        <q-route-tab to="/environments" label="Environments" />
      </q-tabs> -->

    </q-header>

    <!-- <q-drawer
      behavior="desktop"
      v-model="leftDrawerOpen"
      overlay
      side="left"
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Environments
        </q-item-label>

        <q-item v-for="env of envs" :key="env.id">
          <q-item-section class="my-box cursor-pointer q-hoverable">
            <q-item-label @click="fetchEnv(env)">
              {{ env.name }}
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer> -->

    <!-- <q-drawer
      behavior="desktop"
      v-model="rightDrawerOpen"
      overlay
      side="right"
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
         Agents
        </q-item-label>
      </q-list>
    </q-drawer> -->

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>
      <q-toolbar>
        <q-toolbar-title>
          <!-- <a href="https://www.digitalocean.com/?refcode=2184d1107783&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
            <img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg" alt="DigitalOcean Referral Badge" />
          </a> -->
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
// import EssentialLink from 'components/EssentialLink.vue';
import { useRouter } from 'vue-router';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

// const linksList = [
  // {
  //   title: 'Docs',
  //   caption: 'quasar.dev',
  //   icon: 'school',
  //   link: 'https://quasar.dev'
  // },
  // {
  //   title: 'Github',
  //   caption: 'github.com/quasarframework',
  //   icon: 'code',
  //   link: 'https://github.com/quasarframework'
  // },
  // {
  //   title: 'Discord Chat Channel',
  //   caption: 'chat.quasar.dev',
  //   icon: 'chat',
  //   link: 'https://chat.quasar.dev'
  // },
  // {
  //   title: 'Forum',
  //   caption: 'forum.quasar.dev',
  //   icon: 'record_voice_over',
  //   link: 'https://forum.quasar.dev'
  // },
  // {
  //   title: 'Twitter',
  //   caption: '@quasarframework',
  //   icon: 'rss_feed',
  //   link: 'https://twitter.quasar.dev'
  // },
  // {
  //   title: 'Facebook',
  //   caption: '@QuasarFramework',
  //   icon: 'public',
  //   link: 'https://facebook.quasar.dev'
  // },
  // {
  //   title: 'Quasar Awesome',
  //   caption: 'Community Quasar projects',
  //   icon: 'favorite',
  //   link: 'https://awesome.quasar.dev'
  // }
// ];

export default defineComponent({
  name: 'MainLayout',

  // components: {
  //   // EssentialLink
  // },

  setup () {
    const leftDrawerOpen = ref(false);
    // const rightDrawerOpen = ref(false)
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

    // watch(result, (newValue, oldValue) => {
    //   console.log(newValue)
    //   console.log(oldValue)
    //   console.log(result.value)
    // })

    // const environments = useResult(result, null, (data) => data.environment);

    const fetchEnv = (env) => {
      return router.push(`/envs/${env.id}`);
    };
  
    const toolbarOnclick = () => {
      console.log('toolbarOnclick')
      router.push('/')
    }
  
    const envs = computed(() => result.value?.envs ?? [])

    return {
      // "environments": result.value?.data?.envs,
      // environments: result.value?.data?.envs,
      // environments: result.value?.data?.envs,
      // result,
      envs,
      loading,
      error,
      // essentialLinks: linksList,
      leftDrawerOpen,
      fetchEnv,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      toolbarOnclick,

      // rightDrawerOpen,
      // toggleRightDrawer () {
      //   rightDrawerOpen.value = !rightDrawerOpen.value
      // }
    }
  }
});
</script>
