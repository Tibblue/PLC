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
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('./views/Profile.vue')
    },
    {
      path: '/animes',
      name: 'animeList',
      component: () => import('./views/TabelaAnime.vue')
    },
    {
      path: '/producers',
      name: 'producerList',
      component: () => import('./views/TabelaProducer.vue')
    },
    {
      path: '/studios',
      name: 'studioList',
      component: () => import('./views/TabelaStudio.vue')
    },
    {
      path: '/animes/:id',
      name: 'animeInfo',
      component: () => import('./views/ConsultaAnime.vue')
    },
    {
      path: '/producers/:id',
      name: 'producerInfo',
      component: () => import('./views/ConsultaProducer.vue')
    },
    {
      path: '/studios/:id',
      name: 'studioInfo',
      component: () => import('./views/ConsultaStudio.vue')
    }
  ]
})
