<template>
  <div>
    <Navbar />
    <router-view />
    <div class="footer">
      © 2020 Copyright:
      <a href="https://github.com/G33kFreak">Ruslan Zaripov</a>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/navbar";

import "../node_modules/materialize-css/dist/css/materialize.min.css";
import "../node_modules/materialize-css/dist/js/materialize.min.js";
export default {
  name: "app",
  components: {
    Navbar
  }
};
</script>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  margin: auto;
  width: 100%;
  text-align: center;
  color: #212121;
}

.footer a {
  color: #EE6E73;
  text-decoration: none;
}
</style>
