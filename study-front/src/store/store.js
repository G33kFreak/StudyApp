import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
axios.defaults.baseURL = 'http://127.0.0.1:8000/auth/'

export const store = new Vuex.Store({
    state: {
        token: localStorage.getItem('access_token') || null,
        filter: 'all',
    },
    getters: {
        loggedIn(state){
            return state.token !== null
        },
    },
    actions: {
        register(context, data){
            return new Promise((resolve, reject) => {
                axios.post('users/', {
                    username: data.username,
                    email: data.email,
                    password: data.password,
                })
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
            })
        },

        retrieveToken(сontext, credentials) {

            axios.post('jwt/create/', {
                username: credentials.username,
                password: credentials.password,
            })
            .then(response => {
                console.log(response);
            })
            .catch(error =>{
                console.log(error);
            })
           
          },
    }
})