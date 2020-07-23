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
              <div
                class="homework-container"
                v-for="homework in lecture.homework"
                v-bind:key="homework.id"
              >
                <div class="desc-container">
                  <img
                    @click="DeleteHomework(homework.id)"
                    v-if="profileInfo.is_staff"
                    src="../assets/criss-cross.svg"
                    alt
                  />
                  <h6>{{homework.description}}</h6>
                </div>
                <div v-if="homework.isOverdue" class="deadline-container" style="color: #F44336;">
                  <div class="deadline-label-container" style="border: 2px solid #F44336;">
                    <p>Deadline</p>
                  </div>
                  <p>{{homework.deadlineDate}}</p>
                  <p>{{homework.deadlineTime}}</p>
                </div>
                <div v-else class="deadline-container" style="color: #4caf50;">
                  <div class="deadline-label-container" style="border: 2px solid #4caf50;">
                    <p>Deadline</p>
                  </div>
                  <p>{{homework.deadlineDate}}</p>
                  <p>{{homework.deadlineTime}}</p>
                </div>
              </div>
              <a
                v-if="profileInfo.is_staff"
                :id="'showFormBtn_' + lecture.id"
                v-on:click="ShowHomeworkForm(lecture.id)"
                class="waves-effect btn"
              >Add homework</a>
              <form :id="'form_' + lecture.id" class="homeworkForm">
                <b>Description of homework:</b>
                <input
                  type="text"
                  v-model="description"
                  name="homeworkDescription"
                  ref="homework_desc"
                />
                <b>Deadline:</b>
                <datetime format="DD-MM-YYYY H:i" width="20px" v-model="deadline"></datetime>
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
import datetime from "vuejs-datetimepicker";
const myAPIservice = new APIservice();
export default {
  name: "classes",
  components: { datetime },
  data() {
    return {
      description: "",
      deadline: "",
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
      myAPIservice.CreateHomework(this.description, id, this.deadline);
    },

    DeleteHomework: function(homeworkId) {
      myAPIservice.DeleteHomework(homeworkId);
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

.homework-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.deadline-container {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.deadline-label-container {
  margin-bottom: 5px;
}

.desc-container {
  max-width: 70%;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.desc-container h6 {
  margin-left: 10px;
}
</style>>
