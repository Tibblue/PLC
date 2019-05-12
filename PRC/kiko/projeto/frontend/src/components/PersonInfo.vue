<template>
  <v-flex>
    <v-flex>
      <h1> <mark> DEBUG </mark> </h1>
      <h1> PERSON: {{this.idPerson}} </h1>
      <!-- <p> {{personResponse}} </p> -->
      <li v-for="item in personResponse" :key="item">
        <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}}
      </li>
      <h1> <mark> DEBUG </mark> </h1>
    </v-flex>
    <br/>
    <br/>

    <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.personInfo.label"> {{this.personInfo.label}} </h1>
          <h1 v-else> {{this.idPerson}} </h1>
          <!-- <p> {{personResponse}} </p> -->
        </v-card-text>

        <v-container fluid grid-list-lg>
          <v-layout row wrap>
            <v-flex xs12 md6>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Directed </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.personInfo.directed}} </v-subheader> -->
                  <template v-for="anime in this.personInfo.directed">
                    <v-list-tile @click="animeClicked(anime)" :key="anime">
                      <v-list-tile-content>
                        <v-list-tile-title> {{anime}} </v-list-tile-title>
                      </v-list-tile-content>
                    </v-list-tile>
                  </template>
                </v-list>
              </v-card>
            </v-flex>

            <v-flex xs12 md6>
              <v-card>
                <v-toolbar color="indigo" dark>
                  <v-toolbar-title> Wrote </v-toolbar-title>
                </v-toolbar>
                <v-list subheader>
                  <!-- <v-subheader> {{this.personInfo.wrote}} </v-subheader> -->
                  <template v-for="anime in this.personInfo.wrote">
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
    props: ["idPerson"],
    data: () => ({
      personResponse: {},
      personInfo: {
        label: '',
        directed: [],
        wrote: [],
        dbpedia: ''
      }
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/persons/'+this.idPerson);
        this.personResponse = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.personResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.personResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            console.log("LABEL")
            this.personInfo.label = item.o.value
            break;
          case "directed":
            console.log("DIRECTED")
            this.personInfo.directed.push(item.o.value.split('#ANIME_')[1])
            break;
          case "wrote":
            console.log("WROTE")
            this.personInfo.wrote.push(item.o.value.split('#ANIME_')[1])
            break;
          case "dbpedia":
            console.log("DBPEDIA")
            this.personInfo.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      });
    },
    methods: {
      animeClicked: function (id) {
        // this.$emit('filmeSelected', id)
        this.$router.push('/animes/'+id)
      }
    }
  }
</script>

<style>

</style>
