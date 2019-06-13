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
      path: '/cartas',
      name: 'cartasList',
      component: () => import('./views/TabelaCartas.vue')
    },
    {
      path: '/cartas/:id',
      name: 'cartasInfo',
      component: () => import('./views/cartaInfo.vue')
    },
    {
      path: '/cartasview',
      name: 'cartasViewInfo',
      component: () => import('./views/cartasView.vue')
    },
  ]
})