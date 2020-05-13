import Vue from 'vue'
import VueRouter from 'vue-router'
import Classes from '@/components/classes'
import MainPage from '@/components/main-page'
import SignUp from '@/components/sign-up'
import Login from '@/components/login'
import Logout from '@/components/logout'


Vue.use(VueRouter)

const routes = [
    {
        path: '/classes',
        name: 'classes',
        component: Classes
    },
    {
        path: '',
        name: 'main',
        component: MainPage
    },
    {
        path: '/sign-up',
        name: 'sign-up',
        component: SignUp,
        meta: {
            requiresVisitor: true,
        }
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/logout',
        name: 'logout',
        component: Logout
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


export default router