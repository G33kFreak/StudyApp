<template>
  <div class="row">
      <div class="col s6" v-for="lecture in classes" v-bind:key="lecture">
        <div class="card">
            <div class="card-content">
                <p class="card-title">{{lecture.name}}</p>
                <p class="timestamp">Prowadzący: {{lecture.instructor}}</p>
                <p>{{lecture.toDo}}</p>
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
      classes: []
    };
  },
  mounted() {
    myAPIservice
      .getClasses()
      .then(response => {
        this.classes = response.data;
        console.log(this.classes);
      })
      .catch(error => console.log(error));
  }
};
</script>