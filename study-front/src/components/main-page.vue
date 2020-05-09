<template>
  <div id="app" class="container">
    <div class="header">
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#" class="header-label">StudyApp</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav></b-collapse>
      </b-navbar>
    </div>
    <div class="content">
      <b-jumbotron bg-variant="info" text-variant="white" border-variant="dark">
        <template v-slot:header>Study app</template>

        <template v-slot:lead>
          Platform that making homework monitoring easier 
        </template>

        <hr class="my-4" />

        <p>
          You have to login to the platform if you want to use it. If you still don't have an account, register now!
        </p>
        <b-button class="sign-up-button" size="lg" variant="light" href="http://192.168.0.7:8080/sign-up">Sign up</b-button>
        <b-button class="login-button" size="lg" variant="light" href="#">Login</b-button>
      </b-jumbotron>
    </div>
  </div>
</template>

<style scoped>
.content {
  margin-top: 5%;
}

.login-button {
  margin-left: 3%;
}
.header-label {
  float: left;
  text-align: center;
  width: 100%;
  font-size: 34px;
}
</style>
