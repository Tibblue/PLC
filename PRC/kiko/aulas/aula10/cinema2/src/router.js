import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/ListaFilmes.vue')
    },
    {
      path: '/filmes/:id',
      name: 'filme',
      component: () => import('./views/ConsultaFilme.vue')
    }
  ]
})
