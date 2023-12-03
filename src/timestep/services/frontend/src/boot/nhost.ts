import { boot } from 'quasar/wrappers'

import { NhostClient, NhostClientConstructorParams } from '@nhost/nhost-js';

const hostname: string = window.location.hostname

const nhostClientOptions: NhostClientConstructorParams = {
  authUrl: `https://${hostname}/v1/auth`,
  clientStorage: window.localStorage,
  clientStorageType: 'localStorage', // https://docs.nhost.io/reference/docgen/javascript/auth/types/client-storage-type
  functionsUrl: `https://${hostname}/v1/functions`,
  graphqlUrl: `https://${hostname}/v1/graphql`,
  refreshIntervalTime: 1000 * 60 * 60 * 24 * 3, // 3 days
  storageUrl: `https://${hostname}/v1/storage`,
};

const nhost = new NhostClient(nhostClientOptions);

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async ({ app, router, urlPath, publicPath, redirect }) => {
  router.beforeEach(async (to) => {
    const authenticated = await nhost.auth.isAuthenticatedAsync()
    if (!authenticated && to.meta.auth) {
      return '/signin'
    }
    return true
  })

  app.config.globalProperties.$nhost = nhost;
})

export { nhost }
