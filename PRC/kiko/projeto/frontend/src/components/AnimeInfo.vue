<template>
  <v-container>
    <div>
      <h1> <mark> DEBUG </mark> </h1>
      <h1> ANIME: {{this.idAnime}} </h1>
      <!-- <p> {{anime}} </p> -->

      <li v-for="item in anime" :key="item">
        <b>{{item.p.value.split('#')[1]}} :</b>
        {{item.o.value}}
      </li>
      <h1> <mark> DEBUG </mark> </h1>
    </div>

    <br/>
    <br/>

    <h1 v-if="this.testing.label"> {{this.testing.label}} </h1>
    <h1 v-else> {{this.idAnime}} </h1>
    <br/>

    <h3> Directors </h3>
    <!-- <h3> {{this.testing.directors}} </h3> -->
    <p v-if="this.testing.directors.length==0"> Sem informação </p>
    <li v-else @click="personClicked(writer)"
        v-for="director in this.testing.directors" :key="director">
      {{director}}
    </li>
    <br/>

    <h3> Writers </h3>
    <!-- <h3> {{this.testing.writers}} </h3> -->
    <h4 v-if="this.testing.writers.length==0"> Sem informação </h4>
    <li v-else @click="personClicked(writer)"
        v-for="writer in this.testing.writers" :key="writer">
      {{writer}}
    </li>
    <br/>

    <h3> Networks </h3>
    <!-- <h3> {{this.testing.networks}} </h3> -->
    <p v-if="this.testing.networks.length==0"> Sem informação </p>
    <li v-else @click="networkClicked(network)"
        v-for="network in this.testing.networks" :key="network">
      {{network}}
    </li>
    <br/>


  </v-container>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    props: ["idAnime"],
    data: () => ({
      anime: {},
      testing: {
        label: '',
        directors: [],
        writers: [],
        networks: []
      }
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/animes/'+this.idAnime);
        this.anime = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.anime) // debug
      }
      catch(e){
        return(e);
      }
      this.anime.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            console.log("LABEL")
            this.testing.label = item.o.value
            break;
          case "hasDirector":
            console.log("DIRECTOR")
            this.testing.directors.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasWriter":
            console.log("DIRECTOR")
            this.testing.writers.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasNetwork":
            console.log("NETWORK")
            this.testing.networks.push(item.o.value.split('#NETWORK_')[1])
            break;
          default:
            console.log("FDS")
            console.log("FDS")
            console.log("FDS")
            break;
        }
      });
    },
    methods: {
      personClicked: function (id) {
        // this.$emit('filmeSelected', id)
        this.$router.push('/persons/'+id)
      },
      networkClicked: function (id) {
        // this.$emit('filmeSelected', id)
        this.$router.push('/networks/'+id)
      }
    }
  }
</script>

<style>

</style>
