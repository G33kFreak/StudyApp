import Vue from 'vue'
import VueRouter from 'vue-router'
import StartPage from '../views/start-page'
import Classes from '../views/classes'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'startPage',
    component: StartPage
  },
  {
    path: '/classes',
    name: 'classes',
    component: Classes
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
