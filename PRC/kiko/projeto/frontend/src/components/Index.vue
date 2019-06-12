<template>
  <v-container>
    <!-- <h2>{{this.top5}}</h2> -->
    <!-- <h2>{{this.top5[0]}}</h2> -->

    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex text-xs-center><h1>Top 5 Anime</h1></v-flex>
    </v-toolbar>
    <v-layout ma-3>
      <v-flex xs6 pa-1>
        <v-toolbar dark color="indigo" flat>
          <v-flex text-xs-center><h1>Nº 1</h1></v-flex>
        </v-toolbar>
        <v-img :src="this.top5[0].img.value" @click="cardClicked(top5[0].id.value)">
          <v-card color="rgb(0, 0, 0, 0.7)">
            <v-flex xs12 pa-1>
              <h2>{{this.top5[0].title.value}}</h2>
            </v-flex>
          </v-card>
        </v-img>
      </v-flex>
      <v-flex xs6>
        <v-layout>
          <v-flex xs6 pa-1>
            <v-toolbar dark color="indigo" flat>
              <v-flex text-xs-center><h1>Nº 2</h1></v-flex>
            </v-toolbar>
            <v-img :src="this.top5[1].img.value" @click="cardClicked(top5[1].id.value)">
              <v-card color="rgb(0, 0, 0, 0.7)">
                <v-flex xs12 pa-1>
                  <h2>{{this.top5[1].title.value}}</h2>
                </v-flex>
              </v-card>
            </v-img>
          </v-flex>
          <v-flex xs6 pa-1>
            <v-toolbar dark color="indigo" flat>
              <v-flex text-xs-center><h1>Nº 3</h1></v-flex>
            </v-toolbar>
            <v-img :src="this.top5[2].img.value" @click="cardClicked(top5[2].id.value)">
              <v-card color="rgb(0, 0, 0, 0.7)">
                <v-flex xs12 pa-1>
                  <h2>{{this.top5[2].title.value}}</h2>
                </v-flex>
              </v-card>
            </v-img>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex xs6 pa-1>
            <v-toolbar dark color="indigo" flat>
              <v-flex text-xs-center><h1>Nº 4</h1></v-flex>
            </v-toolbar>
            <v-img :src="this.top5[3].img.value" @click="cardClicked(top5[3].id.value)">
              <v-card color="rgb(0, 0, 0, 0.7)">
                <v-flex xs12 pa-1>
                  <h2>{{this.top5[3].title.value}}</h2>
                </v-flex>
              </v-card>
            </v-img>
          </v-flex>
          <v-flex xs6 pa-1>
            <v-toolbar dark color="indigo" flat>
              <v-flex text-xs-center><h1>Nº 5</h1></v-flex>
            </v-toolbar>
            <v-img :src="this.top5[4].img.value" @click="cardClicked(top5[4].id.value)">
              <v-card color="rgb(0, 0, 0, 0.7)">
                <v-flex xs12 pa-1>
                  <h2>{{this.top5[4].title.value}}</h2>
                </v-flex>
              </v-card>
            </v-img>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    data: () => ({
      top5: []
    }),
    mounted: async function (){
      try{
        // // top5 list
        var response = await axios.get(lhost+'/query/top5animeByScore');
        this.top5 = response.data.results.bindings
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      cardClicked: function (id) {
        this.$router.push('/animes/'+id)
      }
    }
  }
</script>

<style>

</style>
