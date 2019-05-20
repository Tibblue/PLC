<template>
  <v-flex>
    <v-flex>
      <h1> <mark> DEBUG </mark> </h1>
      <h1> NETWORK: {{this.idNetwork}} </h1>
      <!-- <p> {{networkResponse}} </p> -->
      <li v-for="item in networkResponse" :key="item">
        <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}}
      </li>
      <h1> <mark> DEBUG </mark> </h1>
    </v-flex>
    <br/>
    <br/>

    <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.networkInfo.label"> {{this.networkInfo.label}} </h1>
          <h1 v-else> {{this.idNetwork}} </h1>
          <!-- <p> {{networkResponse}} </p> -->
        </v-card-text>

        <v-container fluid grid-list-lg>
          <v-layout row wrap>
            <v-flex xs6 lg4>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Animes </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.networkInfo.animes}} </v-subheader> -->
                  <template v-for="anime in this.networkInfo.animes">
                    <v-list-tile @click="animeClicked(anime)" :key="anime">
                      <v-list-tile-content>
                        <v-list-tile-title> {{anime}} </v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </template>
                </v-list>
              </v-card>
            </v-flex>

          </v-layout>
        </v-container>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    props: ["idNetwork"],
    data: () => ({
      networkResponse: {},
      networkInfo: {
        label: '',
        animes: [],
        dbpedia: ''
      }
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/network_info_id/'+this.idNetwork);
        this.networkResponse = response.data.results.bindings
        console.log(this.networkResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.networkResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            console.log("LABEL")
            this.networkInfo.label = item.o.value
            break;
          case "produced":
            console.log("ANIME")
            this.networkInfo.animes.push(item.o.value.split('#ANIME_')[1])
            break;
          case "dbpedia":
            console.log("DBPEDIA")
            this.networkInfo.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      });
    },
    methods: {
      animeClicked: function (id) {
        this.$router.push('/animes/'+id)
      }
    }
  }
</script>

<style>

</style>
