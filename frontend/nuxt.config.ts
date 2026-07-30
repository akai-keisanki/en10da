// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/icon', '@nuxt/eslint', '@nuxtjs/google-fonts'],

  googleFonts: {
    families: {
      Rockwell: [400, 600],
      'Cherry Swash': [400, 700]
    },
    display: 'swap',
    download: true
  },

  css: ['~/assets/css/main.css']
})
