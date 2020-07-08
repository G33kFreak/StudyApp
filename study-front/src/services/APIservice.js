import axios from 'axios'
import authHeader from './auth-header'

axios.defaults.baseURL = 'http://192.168.0.115:8000'

export default class APIservice {

    getClasses() {
        return axios.get('api/classes/', { headers: authHeader() })
    }

    getProfileInfo() {
        let userId = JSON.parse(localStorage.getItem('id_user'));
        return axios.get('/accounts/profile/' + userId, { headers: authHeader() })
    }

    CreateHomework(homeworkDesc, classId) {
        return axios.post('api/homework/', { description: homeworkDesc, Class: parseInt(classId), headers: authHeader() })
            .then((error) => {
                console.log(error);
            })
            .finally(() => {
                //location.reload();
            })
    }
}