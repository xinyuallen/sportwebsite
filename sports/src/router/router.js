const homeRouter = {
  path: '/',
  component: resolve => {
    require(['@/pages/index.vue'], resolve)
  },
  children: [{
    path: '/',
    name: 'home',
    component: resolve => require(['@/pages/home/home.vue'], resolve),
    meta: {
      title: 'sports',
    }
  }, {
    path: '/category/:categoryName',
    name: 'category',
    component: resolve => require(['@/pages/category/category.vue'], resolve),
    meta: {
      title: 'sports-category',
    }
  }]
};

const languageRouter = {
  path: '/language',
  name: 'language',
  meta: {
    title: 'language'
  },
  component: resolve => {
    require(['@/pages/language/language.vue'], resolve)
  }
};

/*路由未匹配*/
const notFoundRouter = {
  path: '*',
  component: resolve => require(['@/pages/notFound/notFound.vue'], resolve),
  name: 'notFound',
  meta: {
    title: '404-sorry！The page you visited does not exist. '
  }
};

/*所有上面定义的路由合并下面的routes里*/
const routes = [
  homeRouter,
  notFoundRouter,
  languageRouter
];

export default routes;
