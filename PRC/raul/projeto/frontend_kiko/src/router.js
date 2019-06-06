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
      path: '/persons',
      name: 'personList',
      component: () => import('./views/TabelaPerson.vue')
    },
    {
      path: '/networks',
      name: 'networkList',
      component: () => import('./views/TabelaNetwork.vue')
    },
    {
      path: '/animes/:id',
      name: 'animeInfo',
      component: () => import('./views/ConsultaAnime.vue')
    },
    {
      path: '/persons/:id',
      name: 'personInfo',
      component: () => import('./views/ConsultaPerson.vue')
    },
    {
      path: '/networks/:id',
      name: 'networkInfo',
      component: () => import('./views/ConsultaNetwork.vue')
    }
  ]
})
