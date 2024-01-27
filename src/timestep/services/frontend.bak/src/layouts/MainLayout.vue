<template>
  <div class="q-pa-md">
    <!-- <q-layout view="hHh LpR fFf"> -->
    <q-layout view="hHh Lpr lff">
      <q-header
        elevated
        :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'"
      >
        <q-toolbar>
          <!-- <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" /> -->
          <q-btn flat @click="drawer = !drawer" round dense icon="menu" />

          <q-toolbar-title
            class="cursor-pointer q-hoverable"
            @click="toolbarOnclick"
          >
            Timestep AI
          </q-toolbar-title>

          <SignOutComponent v-if="isSignedIn" />
        </q-toolbar>
      </q-header>

      <!-- <q-drawer v-model="leftDrawerOpen" side="left" overlay> -->
      <!-- drawer content -->
      <!-- </q-drawer> -->

      <q-drawer
        v-model="drawer"
        show-if-above
        :mini="!drawer || miniState"
        @click.capture="drawerClick"
        :width="200"
        :breakpoint="500"
        bordered
        :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
      >
        <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: 0 }">
          <q-list padding>
            <q-item
              clickable
              v-ripple
              v-for="page in pages"
              :key="page.name"
              :to="page.path"
              :active="router.currentRoute.value.path === page.path"
            >
              <q-item-section avatar v-if="page.metadata && page.metadata.icon">
                <q-icon :name="page.metadata.icon" />
              </q-item-section>

              <q-item-section>
                {{ page.name }}
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>

        <!--
          in this case, we use a button (can be anything)
          so that user can switch back
          to mini-mode
        -->
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
        <q-page class="q-px-lg q-py-md">
          <router-view />
        </q-page>
      </q-page-container>

      <!-- <q-footer>
        <q-toolbar>
          <q-toolbar-title>
          </q-toolbar-title>
        </q-toolbar>
      </q-footer> -->
    </q-layout>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import { AuthChangeEvent, NhostSession } from '@nhost/nhost-js';
import { nhost } from 'src/boot/nhost';
import SignOutComponent from 'src/components/SignOutComponent.vue';

export default defineComponent({
  name: 'MainLayout',

  components: {
    SignOutComponent,
  },

  setup() {
    // const isAuthenticated = ref(false)
    const isSignedIn = ref(false);
    const miniState = ref(false);
    const pages = ref([
      // { name: 'Home', path: '/' },
      {
        name: 'Accounts',
        path: '/accounts',
        metadata: { enabled: true, icon: 'manage_accounts' },
      },
      {
        name: 'Agents',
        path: '/agents',
        metadata: { enabled: true, icon: 'support_agent' },
      },
      // { name: 'Calendars', path: '/calendars', metadata: { enabled: true, icon: 'event_repeat' } },
      // { name: 'Contacts', path: '/contacts', metadata: { enabled: true, icon: 'contacts' } },
      // { name: 'Documents', path: '/documents', metadata: { enabled: false, icon: 'document_scanner' } },
      // { name: 'Tasks', path: '/tasks', metadata: { enabled: true, icon: 'task' } },
      // { name: 'Tools', path: '/tools', metadata: { enabled: true, icon: 'build' } },
      {
        name: 'Environments',
        path: '/threads',
        metadata: { enabled: true, icon: 'workspaces' },
      },
    ]);
    const router = useRouter();

    const { isAuthenticated, isLoading } = nhost.auth.getAuthenticationStatus();

    isSignedIn.value = isAuthenticated;

    nhost.auth.onAuthStateChanged(
      (event: AuthChangeEvent, session: NhostSession | null) => {
        // console.log(
        //   `The auth state has changed. State is now ${event} with session: ${session}`
        // )

        if (event === 'SIGNED_IN') {
          isSignedIn.value = true;
        } else {
          isSignedIn.value = false;
        }
      }
    );

    const toolbarOnclick = () => {
      router.push('/');
    };

    return {
      drawer: ref(false),
      drawerClick(e: { stopPropagation: () => void }) {
        // if in "mini" state and user
        // click on drawer, we switch it to "normal" mode
        if (miniState.value) {
          miniState.value = false;

          // notice we have registered an event with capture flag;
          // we need to stop further propagation as this click is
          // intended for switching drawer to "normal" mode only
          e.stopPropagation();
        }
      },
      // isAuthenticated,
      isSignedIn,
      miniState,
      pages,
      router,
      toolbarOnclick,
    };
  },
});
</script>
