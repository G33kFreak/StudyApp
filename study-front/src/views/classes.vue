<template>
  <div>
    <div class="progress" v-if="loading">
      <div class="indeterminate"></div>
    </div>
    <div class="container" v-else>
      <div class="row">
        <div class="col s6" v-for="lecture in classes" v-bind:key="lecture.id">
          <div class="card">
            <div class="card-content">
              <p class="card-title">{{lecture.name}}</p>
              <p class="timestamp">Prowadzący: {{lecture.instructor_name}}</p>
              <hr />
              <li v-for="homework in lecture.homework" v-bind:key="homework.id">{{homework}}</li>
              <a v-if="profileInfo.is_staff" class="waves-effect btn">Add homework</a>
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
  name: "classes",
  data() {
    return {
      profileInfo: [],
      classes: [],
      loading: false
    };
  },
  created() {
    this.loading = true;
    myAPIservice
      .getClasses()
      .then(response => {
        this.classes = response.data;
        console.log(this.classes);
      })
      .catch(error => {
        console.log(error);
      });
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

<style  scoped>
.btn {
  background-color: #ee6e73;
  margin-top: 25px;
}
</style>>
