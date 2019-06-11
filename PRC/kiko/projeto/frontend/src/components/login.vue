<template>
  <v-flex>
    <v-card>
      <v-toolbar dark color="indigo darken-2" flat>
        <v-flex text-xs-center><h2>Login</h2></v-flex>
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
        <v-btn @click="submit()"><h2>Login</h2></v-btn>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      username: '',
      password: '',
      img: '',
      alert: '' // replace with snackbar for style points
    }),
    methods: {
      submit: function () {
        axios.get('http://localhost:5011/users/'+this.username)
          .then(info => {
            // this.alert = info.data // debug
            this.$session.set('id',info.data.id)
            this.$session.set('bio',info.data.bio)
            this.$session.set('fav',info.data.favoriteAnimes)
            if(info.data.img)
              this.$session.set('img',info.data.img)
            this.$router.go(-1)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "User não existe"
          })
      }
    }
  }
</script>

<style>

</style>
