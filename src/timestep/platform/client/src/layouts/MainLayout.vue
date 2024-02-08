<template>
  <q-layout view="hHh Lpr lff">
    <HeaderComponent
      title="Timestep AI"
      :is-signed-in="isSignedIn"
      :on-menu-button-click="() => { drawer = !drawer }"
      :on-title-click="() => $router.push('/')"
    />

    <q-drawer
      v-model="drawer"
      show-if-above
      :mini="!drawer || miniState"
      :width="200"
      :breakpoint="500"
      bordered
      :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
      @click.capture="drawerClick"
    >
      <q-scroll-area
        class="fit"
        :horizontal-thumb-style="{ opacity: '0' }"
      >
        <q-list padding>
          <q-item
            v-for="page in pages"
            :key="page.name"
            v-ripple
            clickable
            :to="page.path"
            :active="$router.currentRoute.value.path === page.path"
          >
            <q-item-section
              v-if="page.metadata && page.metadata.icon"
              avatar
            >
              <q-icon :name="page.metadata.icon" />
            </q-item-section>

            <q-item-section>
              {{ page.name }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <div
        class="q-mini-drawer-hide absolute"
        style="top: 15px; right: -17px"
      >
        <q-btn
          dense
          round
          unelevated
          color="accent"
          icon="chevron_left"
          @click="miniState = true"
        />
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import { AuthChangeEvent } from '@nhost/nhost-js'

import HeaderComponent from 'components/HeaderComponent.vue'
import { nhost } from 'src/boot/nhost'

export default defineComponent({
  name: 'MainLayout',

  components: {
    HeaderComponent
  },

  setup () {
    const isSignedIn = ref(false)
    const miniState = ref(false)
    const pages = ref([
      // { name: 'Home', path: '/' },
      {
        name: 'Accounts',
        path: '/accounts',
        metadata: { enabled: true, icon: 'manage_accounts' }
      },
      {
        name: 'Agents',
        path: '/agents',
        metadata: { enabled: true, icon: 'support_agent' }
      },
      // {
      //   name: 'Artifacts',
      //   path: '/artifacts',
      //   metadata: { enabled: true, icon: 'art_track' }
      // },
      // { name: 'Calendars', path: '/calendars', metadata: { enabled: true, icon: 'event_repeat' } },
      // { name: 'Contacts', path: '/contacts', metadata: { enabled: true, icon: 'contacts' } },
      // { name: 'Documents', path: '/documents', metadata: { enabled: false, icon: 'document_scanner' } },
      { name: 'Tasks', path: '/tasks', metadata: { enabled: true, icon: 'task' } }
      // { name: 'Tools', path: '/tools', metadata: { enabled: true, icon: 'build' } }
      // {
      //   name: 'Environments',
      //   path: '/threads',
      //   metadata: { enabled: true, icon: 'workspaces' }
      // }
    ])

    const { isAuthenticated } = nhost.auth.getAuthenticationStatus()

    isSignedIn.value = isAuthenticated

    nhost.auth.onAuthStateChanged((event: AuthChangeEvent) => {
      isSignedIn.value = event === 'SIGNED_IN'
    })

    return {
      drawer: ref(false),
      drawerClick (e: { stopPropagation: () => void }) {
        if (miniState.value) {
          miniState.value = false
          e.stopPropagation()
        }
      },
      isSignedIn,
      miniState,
      pages
    }
  }
})
</script>
