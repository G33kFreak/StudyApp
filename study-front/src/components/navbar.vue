<template>
  <nav>
    <div class="nav-wrapper">
      <div class="container">
        <a href="#" class="brand-logo">StudyApp</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li v-if="isLogged">
            <a href="/classes">Classes</a>
          </li>
          <li v-if="isLogged">
            <a href="/profile">Profile</a>
          </li>
          <li v-if="isLogged">
            <a class="nav-link" href @click.prevent="logOut">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data(){
    return{
      isLogged: false,
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.isLogged = true
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/");
      location.reload();
    }
  }
};
</script>