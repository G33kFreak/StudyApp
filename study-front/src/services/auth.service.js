import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/auth';

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
                return response.data;
            });
    }

    logout() {
        localStorage.removeItem('user');
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