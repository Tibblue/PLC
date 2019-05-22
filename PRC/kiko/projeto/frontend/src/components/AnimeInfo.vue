<template>
  <v-flex>
    <v-card>
      <v-card-text class="text-xs-center">
        <h1 v-if="this.label"> {{this.label}} </h1>
        <h1 v-else> {{this.idAnime}} </h1>
      </v-card-text>

      <v-container grid-list-sm>
        <v-layout row wrap>
          <v-flex xs6 lg4>
            <cardList
              name="Directors"
              :list="directorsSimple"
              route="persons"
            ></cardList>
          </v-flex>
          <v-flex xs6 lg4>
            <cardList
              name="Writers"
              :list="writersSimple"
              route="persons"
            ></cardList>
          </v-flex>
          <v-flex xs12 lg4>
            <cardList
              name="Networks"
              :list="networksSimple"
              route="networks"
            ></cardList>
          </v-flex>
        </v-layout>

        <!-- <span>{{this.directorsSimple}}</span> -->
        <!-- <span>{{this.writersSimple}}</span> -->
        <!-- <span>{{this.networksSimple}}</span> -->

      </v-container>
    </v-card>
  </v-flex>
</template>

<script>
  import cardList from '@/components/cardList'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    props: ["idAnime"],
    components: {
      cardList
    },
    data: () => ({
      animeResponse: {},
      label: '',
      directors: [],
      writers: [],
      networks: [],
      directorsSimple: [],
      writersSimple: [],
      networksSimple: [],
      dbpedia: ''
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/anime_info_id/'+this.idAnime);
        this.animeResponse = response.data.results.bindings
        // console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.animeResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            break;
          case "hasDirector":
            this.directors.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasWriter":
            this.writers.push(item.o.value.split('#PERSON_')[1])
            break;
          case "hasNetwork":
            this.networks.push(item.o.value.split('#NETWORK_')[1])
            break;
          case "dbpedia":
            this.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      });
      this.directorsSimple = this.directors.map(this.simplify)
      this.writersSimple = this.writers.map(this.simplify)
      this.networksSimple = this.networks.map(this.simplify)
    },
    methods: {
      simplify: function (item) {
        return {id:item}
      }
    }
  }
</script>

<style>

</style>
