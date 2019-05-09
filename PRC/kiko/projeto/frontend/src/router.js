import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/animes/:id',
      name: 'anime',
      component: () => import('./views/Home.vue')
    }
  ]
})
