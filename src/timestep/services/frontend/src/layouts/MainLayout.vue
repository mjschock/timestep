<template>
  <q-layout view="hHh LpR fFf">
    <q-header>
      <q-toolbar>
        <q-toolbar-title class="cursor-pointer q-hoverable" @click="toolbarOnclick">
          Timestep AI
        </q-toolbar-title>
        <!-- <q-breadcrumbs active-color="grey">
          <q-breadcrumbs-el label="envs" to="/envs" />
          <q-breadcrumbs-el :label="envId" :to="`/envs/${envId}`" :visible="false" />
          <q-breadcrumbs-el label="agents" :to="`/envs/${envId}/agents`"/>
          <q-breadcrumbs-el :label="agentId" />
        </q-breadcrumbs> -->
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>
      <q-toolbar>
        <q-toolbar-title>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'MainLayout',

  setup() {
    const router = useRouter();

    const envId = computed(() => (router.currentRoute.value.params.envId || '').toString())
    const agentId = computed(() => (router.currentRoute.value.params.agentId || '').toString())

    const toolbarOnclick = () => {
      router.push('/')
    }

    return {
      agentId,
      envId,
      toolbarOnclick,
    }
  }
});
</script>
