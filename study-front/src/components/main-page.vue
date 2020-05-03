<template>
  <div id="app" class="container">
    <tr v-for="lecture in classes" v-bind:key="lecture">
      <h1>{{lecture.name}}</h1>
    </tr>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'app',
  data(){
    return{
      loading: false, 
      classes: null,
    }
  },
  mounted(){
    this.loading = true;
    axios
      .get('http://127.0.0.1:8000/api/classes/')
      .then(response => (this.classes = response.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
  }
}
</script>


