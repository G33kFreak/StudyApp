<template>
  <div class="card">
    <div class="card-content">
      <span class="card-title">Welcome to the Study app!</span>
      <p>
        Platform that makes your homework monitoring easier.
      </p>
      <p class="timestamp">You have to login to the platform if you want to use it. If you still don't have an account, sign up now!</p>
    </div>
    <div class="card-action">
      <a href="http://192.168.0.38:8080/login">Login</a>
      <a href="#">Sign up</a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
  .card{
    margin-top: 15%;
    min-height: 30%;
  }
</style>
