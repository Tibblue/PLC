<template>
  <v-flex>
    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex text-xs-center><h2>{{this.$session.get('id')}}  Profile</h2></v-flex>
    </v-toolbar>
    <v-card>
      <v-layout>
        <v-flex xs6 v-if="this.$session.has('img')">
          <v-img :src="this.$session.get('img')"></v-img>
        </v-flex>
        <v-card-text>
          <h3>Bio</h3>
          <h4>{{this.$session.get('bio')}}</h4>

          <!-- <h4>Favorite Animes: {{this.$session.get('fav')}}</h4> -->
          <!-- <ol> -->
            <!-- <li v-for="fav in this.favsInfo" :key="fav.id">{{fav}}</li> -->
          <!-- </ol> -->
        </v-card-text>
      </v-layout>
    </v-card>

    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex text-xs-center><h2>Favorite Animes</h2></v-flex>
    </v-toolbar>
    <v-layout row wrap>
      <v-flex xs3 v-for="fav in this.favsInfo" :key="fav.id">
        <v-img :src="fav.img" @click="cardClicked(fav.id)">
          <v-card color="rgb(0, 0, 0, 0.7)">
            <v-flex xs12 pa-1>
              <h2>{{fixName(fav.id)}}</h2>
            </v-flex>
          </v-card>
        </v-img>
      </v-flex>
    </v-layout>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      alert: '', // replace with snackbar for style points
      favsInfo: [],
    }),
    mounted: async function () {
      this.favsInfo = await Promise.all(this.$session.get('fav').map(this.getInfoByID))
    },
    methods: {
      cardClicked: function (id) {
        this.$router.push('/animes/'+id)
      },
      fixName: function (name) {
        name = name.split('ANIME_')[1]
        name = name.replace(/\d+_/g, "")
        name = name.replace(/_/g, " ")
        return name
      },
      getInfoByID: async function (id) {
        var response = await axios.get("http://localhost:4005/query/infoBy_id/"+id)
        var info = response.data.results.bindings
        // console.log(info) // debug
        var title
        var img
        info.forEach(item => {
          // console.log(item) // debug
          switch (item.p.value.split('#')[1]) {
            case "title":
              title = item.o.value
              break;
            case "img":
              img = item.o.value
              break;
            default:
              // console.log("FDS") // debug
              break;
          }
        })
        return {id:id,title:title,img:img}
      }
    }
  }
</script>

<style>

</style>
