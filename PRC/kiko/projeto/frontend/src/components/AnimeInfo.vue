<template>
  <v-flex>
    <v-flex>
      <h1> <mark> DEBUG </mark> </h1>
      <h1> ANIME: {{this.idAnime}} </h1>
      <!-- <p> {{animeResponse}} </p> -->
      <li v-for="item in animeResponse" :key="item">
        <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}}
      </li>
      <h1> <mark> DEBUG </mark> </h1>
    </v-flex>
    <br/>
    <br/>

    <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.animeInfo.label"> {{this.animeInfo.label}} </h1>
          <h1 v-else> {{this.idAnime}} </h1>
          <!-- <p> {{animeResponse}} </p> -->
        </v-card-text>

        <v-container fluid grid-list-lg>
          <v-layout row wrap>
            <v-flex xs6 lg4>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Directors </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.animeInfo.directors}} </v-subheader> -->
                  <template v-for="director in this.animeInfo.directors">
                    <v-list-tile @click="personClicked(director)" :key="director">
                      <v-list-tile-content>
                        <v-list-tile-title> {{director}} </v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </template>
                </v-list>
              </v-card>
            </v-flex>

            <v-flex xs6 lg4>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Writers </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.animeInfo.writers}} </v-subheader> -->
                  <template v-for="writer in this.animeInfo.writers">
                    <v-list-tile @click="personClicked(writer)" :key="writer">
                      <v-list-tile-content>
                        <v-list-tile-title> {{writer}} </v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </template>
                </v-list>
              </v-card>
            </v-flex>

            <v-flex xs12 lg4>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Networks </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.animeInfo.networks}} </v-subheader> -->
                  <template v-for="network in this.animeInfo.networks">
                    <v-list-tile @click="networkClicked(network)" :key="network">
                      <v-list-tile-content>
                        <v-list-tile-title> {{network}} </v-list-tile-title>
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
    props: ["idAnime"],
    data: () => ({
      animeResponse: {},
      animeInfo: {
        label: '',
        directors: [],
        writers: [],
        networks: [],
        dbpedia: ''
      }
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/anime_info_id/'+this.idAnime);
        this.animeResponse = response.data.results.bindings
        console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.animeResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            console.log("LABEL")
            this.animeInfo.label = item.o.value
            break;
          case "hasDirector":
            console.log("DIRECTOR")
            this.animeInfo.directors.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasWriter":
            console.log("DIRECTOR")
            this.animeInfo.writers.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasNetwork":
            console.log("NETWORK")
            this.animeInfo.networks.push(item.o.value.split('#NETWORK_')[1])
            break;
          case "dbpedia":
            console.log("DBPEDIA")
            this.animeInfo.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      });
    },
    methods: {
      personClicked: function (id) {
        this.$router.push('/persons/'+id)
      },
      networkClicked: function (id) {
        this.$router.push('/networks/'+id)
      }
    }
  }
</script>

<style>

</style>
