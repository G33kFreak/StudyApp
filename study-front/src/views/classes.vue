<template>
  <div>
    <div class="progress" v-if="loading">
      <div class="indeterminate"></div>
    </div>
    <div class="container" v-else>
      <div class="row">
        <div class="col s6" v-for="lecture in classes" v-bind:key="lecture.id">
          <div class="card">
            <div class="card-content">
              <p class="card-title">{{lecture.name}}</p>
              <p class="timestamp">Prowadzący: {{lecture.instructor_name}}</p>
              <hr />
              <li v-for="homework in lecture.homework" v-bind:key="homework.id">{{homework}}</li>
              <a
                :id="'showFormBtn_' + lecture.id"
                v-on:click="ShowHomeworkForm(lecture.id)"
                class="waves-effect btn"
              >Add homework</a>
              <form :id="'form_' + lecture.id" class="homeworkForm">
                <b>Description of homework:</b>
                <input type="text" name="homeworkDescription" ref="homework_desc" />
                <a
                  class="waves-effect green btn-small addBtn"
                  @click.prevent="PostHomework(lecture.id)"
                >Add</a>
                <a
                  class="waves-effect red btn-small cancelBtn"
                  v-on:click="ShowHomeworkForm(lecture.id)"
                >Cancel</a>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import APIservice from "../services/APIservice";
const myAPIservice = new APIservice();
export default {
  name: "classes",
  data() {
    return {
      profileInfo: [],
      classes: [],
      loading: false
    };
  },

  methods: {
    ShowHomeworkForm: function(lectureId) {
      let formId = "form_" + lectureId;
      let btnId = "showFormBtn_" + lectureId;
      if (document.getElementById(formId).style.display == "none") {
        document.getElementById(formId).style.display = "inherit";
        document.getElementById(btnId).style.display = "none";
      } else {
        document.getElementById(formId).style.display = "none";
        document.getElementById(btnId).style.display = "";
      }
    },

    PostHomework: function(id) {
      let description = this.$refs.homework_desc.value;
      myAPIservice.CreateHomework(description, id);
    }
  },

  created() {
    this.loading = true;
    myAPIservice
      .getClasses()
      .then(response => {
        this.classes = response.data;
        console.log(this.classes);
      })
      .catch(error => {
        console.log(error);
      });
    myAPIservice
      .getProfileInfo()
      .then(response => {
        this.profileInfo = response.data;
        console.log(this.profileInfo);
      })
      .catch(error => {
        console.log(error);
      })
      .finally(() => (this.loading = false));
  }
};
</script>

<style  scoped>
.btn {
  background-color: #ee6e73;
  margin-top: 25px;
}

.btn-small {
  margin-top: 20px !important;
}

.cancelBtn {
  margin-left: 25px;
}

.homeworkForm {
  display: none;
  margin-top: 25px;
}
</style>>
