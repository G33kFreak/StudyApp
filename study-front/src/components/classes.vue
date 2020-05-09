<template>
  <div id="app" class="container">
    <div class="header">
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">StudyApp</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav></b-navbar-nav>

          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-nav-item-dropdown right>
              <template v-slot:button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <div class="content">
      <div class="classes-containers" v-for="lecture in classes" v-bind:key="lecture">
        <b-card>
          <b-card-title>
            <h3>{{lecture.name}}</h3>
            <h5>Prowadzący: {{lecture.instructor}}</h5>
          </b-card-title>
          <b-card-text>{{lecture.toDo}}</b-card-text>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "app",
  data() {
    return {
      loading: false,
      classes: null
    };
  },
  mounted() {
    this.loading = true;
    axios
      .get("http://127.0.0.1:8000/classes")
      .then(response => (this.classes = response.data))
      .catch(error => console.log(error))
      .finally(() => (this.loading = false));
  }
};
</script>

<style scoped>
.content {
  display: flex;
  justify-content: space-around;
  width: 100%;
  flex-wrap: wrap;
}

.classes-containers {
  min-width: 50%;
  max-width: 50%;
  padding: 20px;
}
</style>


