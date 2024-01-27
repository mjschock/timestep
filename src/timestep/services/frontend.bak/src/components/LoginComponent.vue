<template>
  <!-- <div class="q-pa-md q-gutter-sm"> -->
  <div class="q-pa-md" style="max-width: 400px">
    <q-form class="q-gutter-md">
      <q-input filled label="Email" lazy-rules type="email" v-model="email" />

      <q-input
        :type="isPwd ? 'password' : 'text'"
        filled
        label="Password"
        v-model="password"
        lazy-rules
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>

      <!-- <q-toggle v-model="accept" label="I accept the license and terms" /> -->

      <div>
        <!-- <q-btn label="Sign in" type="submit" color="primary" /> -->
        <q-btn
          label="Sign in"
          color="primary"
          type="button"
          @click="signIn()"
        />
        <q-btn
          label="Sign up"
          color="primary"
          type="button"
          @click="signUp()"
        />
        <!-- <q-btn label="Reset" type="reset" color="primary" /> -->
        <q-btn
          label="Resend verification email?"
          color="primary"
          type="button"
          @click="sendVerificationEmail()"
        />
      </div>
    </q-form>

    <div v-if="submitResult.message">
      <q-btn
        v-if="submitResult.error == 'invalid-email-password'"
        label="Reset password?"
        color="primary"
        type="button"
        @click="resetPassword()"
      />
      <div>{{ submitResult.error }}</div>
      <div>{{ submitResult.message }}</div>
      <div>{{ submitResult.status }}</div>
    </div>

    <!-- <q-btn label="Prompt" color="primary" @click="prompt = true" /> -->

    <!-- <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Your address</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="address" autofocus @keyup.enter="prompt = false" />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Add address" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog> -->

    <!-- <div class="loginBox" style="display: none;"> -->
    <!-- <div class="inner"> -->
    <!-- <div class="signIn" v-if="signIn"> -->
    <!-- <div class="top"> -->
    <!-- <img
              class="logo"
              src="https://res.cloudinary.com/dc3c8nrut/image/upload/v1685298768/logo-placeholder_l3yodl.png"
            /> -->
    <!-- <div class="title">Sign in</div> -->
    <!-- <div class="subtitle"> -->
    <!-- Don't have an account? -->
    <!-- <span class="subtitle-action" @click="signIn = !signIn">
                Sign up
              </span> -->
    <!-- </div> -->
    <!-- </div> -->
    <!-- <form> -->
    <!-- <div class="form"> -->
    <!-- <input
                required
                aria-required="true"
                aria-invalid="false"
                aria-label="E-mail"
                type="email"
                pattern="^[\w\.-]+@[\w\.-]+\.\w+$"
                class="w100"
                :class="{ invalid: email.error }"
                ref="email"
                placeholder="Email"
                autofocus
                @blur="validateEmail"
                @keydown="validateEmail"
                v-model="email.value"
              /> -->

    <!-- <q-input 
                filled
                hint="Email"
                type="email"
                v-model="email.value"
              /> -->

    <!-- <input
                required
                aria-required="true"
                type="password"
                class="w100"
                :class="{ invalid: password.error }"
                placeholder="Password"
                v-model="password.value"
                @blur="validatePassword"
                @keydown="validatePassword"
              /> -->

    <!-- <q-input 
                :type="isPwd ? 'password' : 'text'"
                filled
                hint="Password with toggle"
                v-model="password.value">
                <template v-slot:append>
                  <q-icon
                    :name="isPwd ? 'visibility_off' : 'visibility'"
                    class="cursor-pointer"
                    @click="isPwd = !isPwd"
                  />
                </template>
              </q-input>
            </div> -->

    <!-- <input
              type="submit"
              value="Sign in"
              class="action"
              :class="{ 'action-disabled': !loginValid }"
            /> -->
    <!-- </form> -->
    <!-- </div> -->

    <!-- <div class="register" v-else> -->
    <!-- <div class="top"> -->
    <!-- <img
              class="logo"
              src="https://res.cloudinary.com/dc3c8nrut/image/upload/v1685298768/logo-placeholder_l3yodl.png"
            /> -->
    <!-- <div class="title">Sign up</div> -->
    <!-- <div class="subtitle">
              Already have an account?
              <span class="subtitle-action" @click="signIn = !signIn">
                Sign in
              </span>
            </div> -->
    <!-- </div> -->

    <!-- <div class="form">
            <input
              type="text"
              class="w100"
              placeholder="Email"
              v-model="email.value"
            />
            <input
              type="password"
              class="w100"
              placeholder="Password"
              v-model="password.value"
            />
          </div> -->

    <!-- <button class="action" :class="{ 'action-disabled': !registerValid }">
            Sign up
          </button> -->
    <!-- </div> -->
    <!-- </div> -->
    <!-- </div> -->
  </div>
</template>

<script lang="ts">
// import { useQuasar } from 'quasar'
// import { defineComponent, ref } from 'vue'
import { computed, defineComponent, ref } from 'vue';
import { useMutation } from '@vue/apollo-composable';
import gql from 'graphql-tag';
import {
  AuthErrorPayload,
  Mfa,
  NhostClient,
  NhostSession,
  NhostSessionResponse,
  ResetPasswordParams,
  ResetPasswordResponse,
  SendVerificationEmailParams,
  SendVerificationEmailResponse,
  SignInParams,
  SignInResponse,
  SignUpParams,
} from '@nhost/nhost-js';
import { type } from 'os';

const nhost = new NhostClient({
  authUrl: 'https://www.timestep.local/v1/auth', // TODO: use env vars
  functionsUrl: 'https://www.timestep.local/v1/functions',
  graphqlUrl: 'https://www.timestep.local/v1/graphql',
  storageUrl: 'https://www.timestep.local/v1/storage',
});

// import { useQuery, useMutation } from '@vue/apollo-composable';
// import gql from 'graphql-tag';

export default defineComponent({
  name: 'LoginComponent',
  // props: {
  //   email: {
  //     type: String,
  //     default: '',
  //   },
  //   password: {
  //     type: String,
  //     default: '',
  //   },
  // },
  setup(props) {
    const email = ref('');
    const password = ref('');

    const submitResult = ref({
      error: '',
      message: '',
      status: 0,
    });

    const resetPassword = async () => {
      const params: ResetPasswordParams = {
        email: email.value,
      };
      const resp: ResetPasswordResponse = await nhost.auth.resetPassword(
        params
      );
      const error: AuthErrorPayload | null = resp.error;

      if (error) {
        console.log('error', error);
        submitResult.value.error = error.error;
        submitResult.value.message = error.message;
        submitResult.value.status = error.status;
      }
    };

    const sendVerificationEmail = async () => {
      const params: SendVerificationEmailParams = {
        email: email.value,
        options: {
          redirectTo: '/profile',
        },
      };
      const resp: SendVerificationEmailResponse =
        await nhost.auth.sendVerificationEmail(params);
      const error: AuthErrorPayload | null = resp.error;

      if (error) {
        console.log('error', error);
        submitResult.value.error = error.error;
        submitResult.value.message = error.message;
        submitResult.value.status = error.status;
      }
    };

    const signIn = async () => {
      const params: SignInParams = {
        email: email.value,
        password: password.value,
      };
      const resp: SignInResponse = await nhost.auth.signIn(params);
      const error: AuthErrorPayload | null = resp.error;
      const mfa: Mfa | null = resp.mfa;
      const session: NhostSession | null = resp.session;

      if (error) {
        console.log('error', error);
        submitResult.value.error = error.error;
        submitResult.value.message = error.message;
        submitResult.value.status = error.status;
      }

      if (mfa) {
        console.log('mfa', mfa);
      }

      if (session) {
        console.log('session', session);
      }
    };

    const signUp = async () => {
      const params: SignUpParams = {
        email: email.value,
        password: password.value,
      };
      const resp: NhostSessionResponse = await nhost.auth.signUp(params);
      const error: AuthErrorPayload | null = resp.error;
      const session: NhostSession | null = resp.session;

      if (error) {
        console.log('error', error);
        submitResult.value.error = error.error;
        submitResult.value.message = error.message;
        submitResult.value.status = error.status;
      }

      if (session) {
        console.log('session', session);
      }
    };

    return {
      email,
      isPwd: ref(true),
      password,
      resetPassword,
      sendVerificationEmail,
      signIn,
      signUp,
      submitResult,
    };
  },
  // data() {
  //   return {
  //     // address: ref(''),
  //     email: {
  //       error: false,
  //       value: '',
  //     },
  //     // emailRegex: /^[\w\.-]+@[\w\.-]+\.\w+$/,
  //     isPwd: ref(true),
  //     password: {
  //       error: false,
  //       value: '',
  //     },
  //     // passwordRegex: /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/,
  //     // prompt: ref(false),
  //     // signIn: true,
  //   }
  // },
  // methods: {
  //   signIn() {
  //     console.log('signIn')
  //   },
  //   signUp() {
  //     console.log('signUp')

  //     const { result, loading, error, refetch } = useQuery(
  //         gql`
  //           query getEnv($envId: ID!) {
  //             env(id: $envId) {
  //               id
  //               name
  //               namespace
  //               description
  //             }
  //           }
  //         `,
  //         { envId: this.email.value }
  //     );

  //     console.log('result', result)
  //   },
  // validateEmail(event) {
  //   if (this.email.value == '') this.email.error = true
  //   else this.email.error = false
  // },
  // validatePassword(event) {
  //   if (this.password.value == '') this.password.error = true
  //   else this.password.error = false
  // },
  // },
  // methods: {
  //   validateEmail(event) {
  //     if (this.email.value == "") this.email.error = true;
  //     else this.email.error = false;
  //   },

  //   validatePassword(event) {
  //     if (this.password.value == "") this.password.error = true;
  //     else this.password.error = false;
  //   }
  // },
  // mounted() {
  //   // this.$refs.email.focus();
  // },
  // computed: {
  //   emailValid() {
  //     return this.emailRegex.test(this.email.value);
  //   },

  //   passwordValid() {
  //     return this.password.value.length > 0;
  //   },

  //   loginValid() {
  //     return this.emailValid && this.passwordValid;
  //   },

  //   registerValid() {
  //     return (
  //       this.emailValid &&
  //       this.passwordValid
  //     );
  //   }
  // },
  // setup () {
  //   const $q = useQuasar()

  //   const email = ref(null)
  //   const password = ref(null)
  //   const accept = ref(false)

  //   return {
  //     email,
  //     password,
  //     accept,

  //     onSubmit () {
  //       if (accept.value !== true) {
  //         $q.notify({
  //           color: 'red-5',
  //           textColor: 'white',
  //           icon: 'warning',
  //           message: 'You need to accept the license and terms first'
  //         })
  //       }
  //       else {
  //         $q.notify({
  //           color: 'green-4',
  //           textColor: 'white',
  //           icon: 'cloud_done',
  //           message: 'Submitted'
  //         })
  //       }
  //     },

  //     onReset () {
  //       email.value = null
  //       password.value = null
  //       accept.value = false
  //     }
  //   }
  // }
});
</script>
