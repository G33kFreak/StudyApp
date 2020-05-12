<template>
  <div id="app" class="container">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          type="email"
          required
          placeholder="Enter email"
          v-model="email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your user name: " label-for="input-2">
        <b-form-input id="input-2" v-model="username" required placeholder="Enter user name"></b-form-input>
      </b-form-group>

      <b-form @submit.stop.prevent>
        <label for="text-password">Password</label>
        <b-input type="password" id="text-password" v-model="password" aria-describedby="password-help-block"></b-input>
        <b-form-text id="password-help-block">
          Your password must be 8-20 characters long, contain letters and numbers, and must not
          contain spaces, special characters, or emoji.
        </b-form-text>
      </b-form>

      <b-button size="lg" type="submit" variant="primary">Submit</b-button>
      <b-button size="lg" type="reset" class="reset-btn" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          food: null,
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>


<style scoped>
  .reset-btn{
    margin-left: 3%;
  }
</style>