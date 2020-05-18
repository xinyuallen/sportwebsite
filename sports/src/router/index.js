import Vue from 'vue';
import Router from 'vue-router';
import routes from './router.js';

Vue.use(Router);

const router = new Router({
  // mode: 'history',
  routes: routes,
  /*记录scroll，当前进/后退时会保存position，其他切换状态scroll为0*/
  scrollBehavior(to, from, savePosition) {
    if (savePosition) {
      return savePosition;
    } else {
      return {
        x: 0,
        y: 0
      };
    }
  }
})

/*全局前置守卫*/
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
})

/*路由错误处理*/
router.onError((callback) => {
  console.log('路由错误：', callback);
});

export default router;
