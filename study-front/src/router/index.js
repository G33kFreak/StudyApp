import Vue from 'vue'
import VueRouter from 'vue-router'
import Classes from '@/components/classes'
import MainPage from '@/components/main-page'
import SignUp from '@/components/sign-up'

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
        component: SignUp
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router