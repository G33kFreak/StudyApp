<template>
  <div class="container">
    <h1>Sign up</h1>
    <div class="row">
      <form class="col s12" @submit.prevent="handleRegister">
        <div class="row">
          <div class="input-field col s12">
            <input id="email" type="email" v-model="user.email" class="form-control" name="email" />
            <label for="email">Email</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input
              id="username"
              type="text"
              v-model="user.username"
              class="form-control"
              name="username"
            />
            <label for="username">Username</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input v-model="user.password" type="password" class="form-control" name="password" />
            <label for="password">Password</label>
          </div>
        </div>
        <button class="waves-effect green btn" type="submit">Sign up</button>
        <a class="waves-effect red btn cancel">Cancel</a>
      </form>
    </div>
  </div>
</template>

<script>
import User from "../models/user";
export default {
  name: "sign-up",
  data() {
    return {
      user: new User("", "", ""),
      submitted: false,
      successful: false,
      message: ""
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/classes");
    }
  },
  methods: {
    handleRegister() {
      console.log(this.user);
      this.message = "";
      this.submitted = true;
      this.$store.dispatch("auth/register", this.user).then(
        data => {
          this.message = data.message;
          this.successful = true;
          this.$router.push("/login");
        },
        error => {
          this.message =
            (error.response && error.response.data) ||
            error.message ||
            error.toString();
          this.successful = false;
        }
      );
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 5%;
}
.cancel {
  margin: 5%;
}
</style>