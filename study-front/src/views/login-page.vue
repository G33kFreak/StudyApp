<template>
  <div class="container">
    <h1>Login page</h1>
    <div class="row">
      <form class="col s12" @submit.prevent="handleLogin">
        <div class="row">
          <div class="input-field col s12">
            <input v-model="user.username" type="text" class="form-control" name="username" />
            <label for="username">Username</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input
              id="password"
              type="password"
              class="form-control"
              v-model="user.password"
              name="password"
            />
            <label for="password">Password</label>
          </div>
        </div>
        <button class="waves-effect green btn" type="submit">Login</button>
        <a class="waves-effect red btn cancel">Cancel</a>
      </form>
    </div>
  </div>
</template>

<script>
import User from "../models/user";

export default {
  name: "Login",
  data() {
    return {
      user: new User("", ""),
      loading: false,
      message: ""
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/classes");
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;
      if (this.user.username && this.user.password) {
        this.$store.dispatch("auth/login", this.user).then(
          () => {
            this.$router.push("/classes");
          },
          error => {
            this.loading = false;
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString();
          }
        );
      }
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 7%;
}

.cancel {
  margin: 5%;
}
</style>