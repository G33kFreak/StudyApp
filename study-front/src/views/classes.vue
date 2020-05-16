<template>
  <div class="row">
    <div class="col s6" v-for="lecture in classes" v-bind:key="lecture">
      <div class="card" v-if="!isLoading">
        <div class="card-content">
          <p class="card-title">{{lecture.name}}</p>
          <p class="timestamp">Prowadzący: {{lecture.instructor}}</p>
          <p>{{lecture.toDo}}</p>
        </div>
      </div>
      <div class="progress" v-else>
        <div class="indeterminate"></div>
      </div>
    </div>
  </div>
</template>

<script>
import APIservice from "../services/APIservice";
const myAPIservice = new APIservice();
export default {
  name: "classes",
  isLoading: true,
  data() {
    return {
      classes: []
    };
  },
  created() {
    myAPIservice
      .getClasses()
      .then(response => {
        this.classes = response.data;
        console.log(this.classes);
        this.isLoading = false;
      })
      .catch(error => {
        console.log(error);
        this.isLoading = false;
      });
  }
};
</script>