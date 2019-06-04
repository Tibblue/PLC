import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'

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
      path: '/mangas',
      name: 'mangasList',
      component: () => import('./views/TabelaManga.vue')
    },
    {
      path: '/mangas/:id',
      name: 'mangaInfo',
      component: () => import('./views/mangaInfo.vue')
    },
    {
      path: '/authors/:id',
      name: 'authorInfo',
      component: () => import('./views/authorInfo.vue')
    },
    {
      path: '/magazines/:id',
      name: 'magazinesInfo',
      component: () => import('./views/magazinesInfo.vue')
    },
    {
      path: '/publisher/:id',
      name: 'publishersInfo',
      component: () => import('./views/publishersInfo.vue')
    },
  ]
})