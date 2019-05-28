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
      path: '/animes',
      name: 'animeList',
      component: () => import('./views/TabelaAnime.vue')
    },
    {
      path: '/genres',
      name: 'genreList',
      component: () => import('./views/TabelaAnime.vue')
    },
    {
      path: '/producers',
      name: 'producerList',
      component: () => import('./views/TabelaPerson.vue')
    },
    {
      path: '/studios',
      name: 'studioList',
      component: () => import('./views/TabelaNetwork.vue')
    },
    {
      path: '/animes/:id',
      name: 'animeInfo',
      component: () => import('./views/ConsultaAnime.vue')
    },
    {
      path: '/genres/:id',
      name: 'genreInfo',
      component: () => import('./views/ConsultaAnime.vue')
    },
    {
      path: '/producers/:id',
      name: 'producerInfo',
      component: () => import('./views/ConsultaPerson.vue')
    },
    {
      path: '/studios/:id',
      name: 'studioInfo',
      component: () => import('./views/ConsultaNetwork.vue')
    }
  ]
})
