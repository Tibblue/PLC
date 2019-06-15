<template>
  <v-flex>
    <v-card>
      <v-toolbar dark color="indigo darken-2" flat>
        <v-flex text-xs-center><h2>Sign In</h2></v-flex>
      </v-toolbar>
      <v-card-text>
        <p>{{alert}}</p>
        <v-text-field
          clearable
          v-model="username"
          label="Username"
        ></v-text-field>
        <!-- <v-text-field
          clearable
          v-model="password"
          label="Password"
          type="password"
        ></v-text-field> -->
        <v-layout align-center justify-center fill-height>
          <v-btn @click="submit()"><h2>Sign In</h2></v-btn>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      username: '',
      // password: '',
      img: '',
      alert: '' // replace with snackbar for style points
    }),
    methods: {
      submit: function () {
        var newUserInfo = {
          id: this.username,
          bio: "New User",
          favoriteAnimes: []
        }
        var headers = { headers: { 'Content-Type': 'application/json' }}
        axios.post('http://localhost:5011/users'
                  ,newUserInfo,headers)
          .then(() => {
            // this.alert = info.data // debug
            this.alert = "Profile successfully created"
            // this.$router.go(0)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "New profile failed"
          })
      }
    }
  }
</script>

<style>

</style>
