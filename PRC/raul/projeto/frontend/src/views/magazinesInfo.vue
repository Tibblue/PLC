1<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->
    <!-- <p>{{mangazine_info}}</p> -->
    <!-- <p>{{mangas}}</p> -->
    <!-- <p>{{magazines}}</p>
    <p>{{publishers}}</p> -->

    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> Revista: {{this.label}} </h1>
          <h1 v-else> {{fixName(this.id)}} </h1>
        </v-card-text>

        <v-container grid-list-sm>
          <v-layout row wrap>
            <v-flex xs6>
              <cardList
                name="Lista de Mangas"
                :list="mangasSimple"
                route="mangas"
              ></cardList>
            </v-flex>

          </v-layout>

          <!-- <span>{{this.directorsSimple}}</span> -->

        </v-container>
      </v-card>
    </v-flex>

    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <h1> ANIME: {{this.id}} </h1> -->
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
      id: '',
      mangazine_info: {},
      label: '',
      mangas: [],
      mangasSimple: [],

    }),
    mounted: async function (){
      this.id = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/magazine_info_id/'+this.id);
        this.mangazine_info = response.data.results.bindings
        // console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.mangazine_info.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            break;
          case "released":
            this.mangas.push(item.o.value.split('#MANGA_')[1])
          default:
            console.log("FDS")
            break;
        }
      })
      this.mangasSimple = this.mangas.map(this.simplify)

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
