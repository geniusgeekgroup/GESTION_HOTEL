import Vue from 'vue'
import VeeValidate from 'vee-validate'
import AppEntry from './AppEntry'
import store from './store'
import router from './router'

new Vue({
  el: '#app-entry',
  router,
  store,
  template: '<AppEntry/>',
  components: { AppEntry }
})
