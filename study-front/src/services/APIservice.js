import axios from 'axios'
import authHeader from './auth-header'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default class APIservice {
    getClasses() {
        return axios.get('/classes', {headers: authHeader()})
    }
}