<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> {{this.label}} </h1>
          <h1 v-else> {{fixName(this.idAnime)}} </h1>
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

    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <h1> ANIME: {{this.idAnime}} </h1> -->
    <!-- <li v-for="item in animeResponse" :key="item"> -->
      <!-- <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}} -->
    <!-- </li> -->
    <!-- <p> {{animeResponse}} </p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

  </v-container>
</template>

<script>
  import cardList from '@/components/cardList'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardList
    },
    data: () => ({
      idAnime: '',
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
      this.idAnime = this.$route.params.id
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
      })
      if(this.$session.has('directorsSimple'))
        this.directorsSimple = this.$session.get('directorsSimple')
      else
        this.$session.set('directorsSimple',this.directors.map(this.simplify))
      this.writersSimple = this.writers.map(this.simplify)
      this.networksSimple = this.networks.map(this.simplify)
    },
    methods: {
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
      simplify: function (item) {
        return {id:item}
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
