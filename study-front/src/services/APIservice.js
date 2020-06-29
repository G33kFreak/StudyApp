import axios from 'axios'
import authHeader from './auth-header'

axios.defaults.baseURL = 'http://192.168.0.115:8000'

export default class APIservice {

    getClasses() {
        return axios.get('/classes', { headers: authHeader() })
    }

    getProfileInfo() {
        let userId = JSON.parse(localStorage.getItem('id_user'));
        return axios.get('/accounts/profile/' + userId, { headers: authHeader() })
    }
}