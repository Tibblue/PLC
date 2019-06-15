<template>
  <v-flex>
    <v-card>
      <v-toolbar dark color="indigo darken-2" flat>
        <v-flex text-xs-center><h2>Edit Profile</h2></v-flex>
      </v-toolbar>
      <v-card-text>
        <p>{{alert}}</p>

        <!-- <v-text-field
          clearable
          v-model="password"
          label="Password"
          type="password"
        ></v-text-field> -->

        <v-text-field
          clearable
          v-model="bio"
          label="New Bio"
        ></v-text-field>
        <v-layout align-center justify-center fill-height>
          <v-btn @click="submitBio()"><h2>Edit Bio</h2></v-btn>
        </v-layout>

        <v-text-field
          clearable
          v-model="image"
          label="New Image URL"
        ></v-text-field>
        <v-layout align-center justify-center fill-height>
          <v-btn @click="submitImage()"><h2>Change Profile Image</h2></v-btn>
        </v-layout>

        <v-layout align-center justify-center fill-height>
          <v-btn @click="deleteProfile()" color="red">
            <h2>Delete Profile !!!</h2>
          </v-btn>
        </v-layout>

      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      bio: '',
      image: '',
      alert: '' // replace with snackbar for style points
    }),
    methods: {
      deleteProfile: function () {
        axios.delete('http://localhost:5011/users/'+this.$session.get('id'))
          .then(() => {
            // this.alert = info.data // debug
            this.$session.clear()
            this.$router.push('/')
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "Profile delete failed!"
          })
      },
      submitBio: function () {
        var newInfo = {
          id: this.$session.get('id'),
          bio: this.bio,
          img: this.$session.get('img'),
          favoriteAnimes: this.$session.get('fav')
        }
        var headers = { headers: { 'Content-Type': 'application/json' }}
        axios.put('http://localhost:5011/users/'+this.$session.get('id')
                  ,newInfo,headers)
          .then(() => {
            // this.alert = info.data // debug
            this.$session.set('bio',this.bio)
            this.$router.go(0)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "Update da Bio falhou!"
          })
      },
      submitImage: function () {
        var newInfo = {
          id: this.$session.get('id'),
          bio: this.$session.get('bio'),
          img: this.image,
          favoriteAnimes: this.$session.get('fav')
        }
        var headers = { headers: { 'Content-Type': 'application/json' }}
        axios.put('http://localhost:5011/users/'+this.$session.get('id')
                  ,newInfo,headers)
          .then(() => {
            // this.alert = info.data // debug
            this.$session.set('img',this.image)
            this.$router.go(0)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "Update da Image falhou!"
          })
      }
    }
  }
</script>

<style>

</style>
