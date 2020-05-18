// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/*引入静态资源*/
import './assets/global.css';
import './assets/iconfont/iconfont.css';
/*引入lazyload*/
import VueLazyLoad from 'vue-lazyload'
Vue.use(VueLazyLoad, {
  /*error: require('@/assets/imgError.png'),*/
  loading: require('@/assets/loading.gif')
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>'
})
