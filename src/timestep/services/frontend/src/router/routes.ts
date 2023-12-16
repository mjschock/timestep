import { RouteRecordRaw } from 'vue-router';

import AccountsPage from 'pages/AccountsPage.vue'
import AboutPage from 'pages/AboutPage.vue'
import ApolloPage from 'pages/ApolloPage.vue'
import Index from 'pages/IndexPage.vue'
import Profile from 'pages/ProfilePage.vue'
import SignInMain from 'pages/sign-in/CommonActions.vue'
import SignInEmailPasword from 'pages/sign-in/EmailPassword.vue'
import SignInEmailPaswordless from 'pages/sign-in/EmailPasswordless.vue'
import SignIn from 'pages/sign-in/IndexPage.vue'
import SignUpMain from 'pages/sign-up/CommonActions.vue'
import SignUpEmailPasword from 'pages/sign-up/EmailPassword.vue'
import SignUpEmailPaswordless from 'pages/sign-up/EmailPasswordless.vue'
import SignUp from 'pages/sign-up/IndexPage.vue'
import Signout from 'pages/SignoutPage.vue'
import StoragePage from 'pages/StoragePage.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: Index, meta: { auth: false } },
      // {
      //   path: '/envs/:envId/agents/:agentId',
      //   component: () => import('pages/AgentPage.vue'),
      // },
      // {
      //   path: '/envs/:envId/agents',
      //   component: () => import('pages/AgentsPage.vue'),
      // },
      // {
      //   path: '/envs/:envId',
      //   component: () => import('pages/EnvPage.vue'),
      // },
      // {
      //   path: '/envs',
      //   component: () => import('pages/EnvsPage.vue'),
      // },
      // {
      //   path: '/settings',
      //   component: () => import('pages/SettingsPage.vue'),
      // },
      // { path: '/profile', component: Profile, meta: { auth: true } },
      { path: '/accounts', component: AccountsPage, meta: { auth: true } },
      { path: '/agents', component: () => import('pages/AgentsPage.vue'), meta: { auth: true } },
      { path: '/calendars', component: () => import('pages/CalendarsPage.vue'), meta: { auth: true } },
      { path: '/contacts', component: () => import('pages/ContactsPage.vue'), meta: { auth: true } },
      { path: '/documents', component: () => import('pages/DocumentsPage.vue'), meta: { auth: true } },
      { path: '/tasks', component: () => import('pages/TasksPage.vue'), meta: { auth: true } },
      { path: '/tools', component: () => import('pages/ToolsPage.vue'), meta: { auth: true } },
      { path: '/threads', component: () => import('pages/ThreadsPage.vue'), meta: { auth: true } },
      { path: '/threads/:threadId', component: () => import('pages/ThreadPage.vue'), meta: { auth: true } },
      // { path: '/signout', component: Signout },
      // {
      //   path: '/signin',
      //   component: SignIn,
      //   children: [
      //     { path: '', component: SignInMain },
      //     {
      //       path: 'passwordless',
      //       component: SignInEmailPaswordless
      //     },
      //     {
      //       path: 'email-password',
      //       component: SignInEmailPasword
      //     }
      //   ],
      //   meta: { auth: false },
      // },
      // {
      //   path: '/signup',
      //   component: SignUp,
      //   children: [
      //     { path: '', component: SignUpMain },
      //     {
      //       path: 'passwordless',
      //       component: SignUpEmailPaswordless
      //     },
      //     {
      //       path: 'email-password',
      //       component: SignUpEmailPasword
      //     }
      //   ],
      //   meta: { auth: false },
      // },
      // { path: '/apollo', component: ApolloPage, meta: { auth: true } },
      // { path: '/storage', component: StoragePage, meta: { auth: true } },
      // {
      //   path: '',
      //   redirect: '/envs/default/agents/default'
      // },
      // { path: '', component: () => import('pages/IndexPage.vue') }
    ],
    // meta: { auth: true },
  },
  // {
  //   path: '/signin',
  //   component: () => import('pages/SignInPage.vue'),
  //   meta: { auth: false },
  // },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
