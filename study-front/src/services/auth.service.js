import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://192.168.0.115:8000/auth';

class AuthService {
    login(user) {
        return axios
            .post(API_URL + '/jwt/create', {
                username: user.username,
                password: user.password
            })
            .then(response => {
                if (response.data.access) {
                    localStorage.setItem('user', JSON.stringify(response.data));
                }
                this.setUserId()
                return response.data;
            });
    }

    setUserId() {
        axios.get(API_URL + '/users/me', { headers: authHeader() })
            .then(response => {
                localStorage.setItem('id_user', JSON.stringify(response.data.id))
            })
            .catch(error => {
                console.log(error)
            })
    }

    logout() {
        localStorage.removeItem('user');
        localStorage.removeItem('id_user');
    }

    register(user) {
        return axios.post(API_URL + '/users/', {
            email: user.email,
            username: user.username,
            password: user.password
        });
    }
}

export default new AuthService();