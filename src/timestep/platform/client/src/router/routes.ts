import { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') }
      // { path: 'accounts', component: () => import('pages/AccountsPage.vue') },
      // { path: 'agents', component: () => import('pages/AgentsPage.vue') },
      // { path: 'artifacts', component: () => import('pages/ArtifactsPage.vue') },
      // { path: 'tasks', component: () => import('pages/TasksPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
