// https://nuxt.com/docs/api/configuration/nuxt-config

const API_BASE_URL = 'http://localhost:5000/'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/icon', '@nuxt/eslint', '@nuxtjs/google-fonts', '@sidebase/nuxt-auth', /*'@nuxt-alt/markdown-it'*/],

  googleFonts: {
    families: {
      Rockwell: [400, 600],
      'Cherry Swash': [400, 700]
    },
    display: 'swap',
    download: true
  },

  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      baseURL: API_BASE_URL
    }
  },

  auth: {
    isEnabled: true,
    baseURL: API_BASE_URL,
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/auth/login', method: 'post' },
        signOut: { path: '/auth/logout', method: 'post' },
        getSession: { path: '/user/me', method: 'get' },
      },
      pages: {
        login: '/login',
      },
      token: {
        signInResponseTokenPointer: '/access_token',
        type: 'Bearer',
        headerName: 'Authorization',
        maxAgeInSeconds: 60 * 60 * 24,
      },
    },
  },

  markdownIt: {
    runtime: true,
    use: ['@vscode/markdown-it-katex']
  }
})
