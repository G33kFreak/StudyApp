<template>
  <div id="app" class="container">
    <b-form action="#" @submit.prevent="login">
      <b-form-group id="input-group-2" label="Your user name: " label-for="input-2">
        <b-form-input id="input-2" v-model="username" required placeholder="Enter user name"></b-form-input>
      </b-form-group>

      <b-form>
        <label for="text-password">Password</label>
        <b-input
          type="password"
          id="text-password"
          v-model="password"
          aria-describedby="password-help-block"
        ></b-input>
        <b-form-text id="password-help-block">
          Your password must be 8-20 characters long, contain letters and numbers, and must not
          contain spaces, special characters, or emoji.
        </b-form-text>
      </b-form>

      <b-button size="lg" type="submit" variant="primary">Login</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      username: '',
      password: ''
    };
  },

  methods: {
    login() {
      this.$store.dispatch('retrieveToken', {
        username: this.username,
        password: this.password
      });
    },
  }
};
</script>