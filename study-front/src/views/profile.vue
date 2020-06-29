<template>
  <div>
    <div class="progress" v-if="loading">
      <div class="indeterminate"></div>
    </div>
    <div class="container">
      <div class="col s12 m7">
        <h2 class="header">Profile page</h2>
        <div class="card horizontal usercard">
          <div class="card-image">
            <p class="typeOfUser" v-if="profileInfo.is_staff">Prowadzący</p>
            <p class="typeOfUser" v-else>Student</p>
          </div>
          <div class="card-stacked profileInfoCard">
            <div class="card-content profileInfo">
              <li>Email: {{profileInfo.email}}</li>
              <li>Username: {{profileInfo.username}}</li>
              <li>First name: {{profileInfo.first_name}}</li>
              <li>Last name: {{profileInfo.last_name}}</li>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import APIservice from "../services/APIservice";
const myAPIservice = new APIservice();
export default {
  name: "profile",
  data() {
    return {
      profileInfo: [],
      loading: false
    };
  },
  created() {
    this.loading = true;
    myAPIservice
      .getProfileInfo()
      .then(response => {
        this.profileInfo = response.data;
        console.log(this.profileInfo);
      })
      .catch(error => {
        console.log(error);
      })
      .finally(() => (this.loading = false));
  }
};
</script>

<style scoped>
.typeOfUser {
  font-size: 56px;
  color: #ee6e73;
}
.profileInfo {
  font-size: 26px;
}
.profileInfoCard {
  margin-left: 5%;
}
.usercard {
  padding: 5%;
}
</style>