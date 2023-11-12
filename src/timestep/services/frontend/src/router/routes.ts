import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '/envs/:envId/agents/:agentId',
        component: () => import('pages/AgentPage.vue'),
      },
      {
        path: '/envs/:envId/agents',
        component: () => import('pages/AgentsPage.vue'),
      },
      {
        path: '/envs/:envId',
        component: () => import('pages/EnvPage.vue'),
      },
      {
        path: '/envs',
        component: () => import('pages/EnvsPage.vue'),
      },
      // {
      //   path: '',
      //   redirect: '/envs/default/agents/default'
      // },
      { path: '', component: () => import('pages/IndexPage.vue') }
    ],
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
