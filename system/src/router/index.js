import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import test from '@/components/test'
// import rate from '@/components/rate'
import ElementUI from 'element-ui'

Vue.use(Router)

export default new Router({
  /*routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]*/
  routes: [
        {
            path: '/',
            redirect: '/home'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/article/:concept/:id',
                    name: 'readpage',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/searchPage'),
                    meta: { title: '文章页面' }
                },
                {
                    path: '/concept/:map/:concept',
                    name:'conceptpage',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '概念页面' }
                },
            ]
        },
        {
            path: '/home',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Login.vue'),
            meta: { title: '主页' }
        },
        {
            path: '/hello',
            component: () => import(/* webpackChunkName: "login" */ '../components/HelloWorld.vue'),
            meta: { title: '测试' }
        }
        
    ]
})