<template>
  <nav>
    <div class="nav-wrapper">
      <div class="container">
        <a href="#" class="brand-logo">StudyApp</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li>
            <a href="#">Profile</a>
          </li>
          <li>
            <a class="nav-link" href @click.prevent="logOut">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/");
    }
  }
};
</script>