import Vue from 'vue'
import VueRouter from 'vue-router'
import StartPage from '../views/start-page'
import Classes from '../views/classes'
import Login from '../views/login-page'
import Signup from '../views/signup-page'
import Profile from '../views/profile'


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
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: Signup
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
/*
router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next('/');
  }

  next();
})
*/
export default router
