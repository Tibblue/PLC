<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

    <v-flex>
      <v-card>
        <v-layout>
          <v-flex xs4>
            <v-img
              class="white--text"
              width="266"
              ratio=1.6
              :src="this.img"
            />
          </v-flex>
          <v-flex xs4>
            <v-card-text class="text-xs-center">
              <h1> {{this.title}} </h1>
              <h2> {{this.title_english}} </h2>
              <h2> {{this.title_japanese}} </h2>
            </v-card-text>
          </v-flex>
          <v-flex xs4>
            <v-card-text class="text-xs-center">
              <h1> {{this.type}} </h1>
              <!-- <h2> {{this.score}} </h2> -->
            </v-card-text>
          </v-flex>
        </v-layout>

        <v-container grid-list-sm>
          <v-layout row wrap>
            <v-flex xs6 lg4>
              <cardList
                name="Genres"
                :list="genresSimple"
                route="genres"
              ></cardList>
            </v-flex>
            <v-flex xs6 lg4>
              <cardList
                name="Producers"
                :list="producersSimple"
                route="producers"
              ></cardList>
            </v-flex>
            <v-flex xs12 lg4>
              <cardList
                name="Studio"
                :list="studiosSimple"
                route="studios"
              ></cardList>
            </v-flex>
          </v-layout>

          <!-- <span>{{this.genresSimple}}</span> -->
          <!-- <span>{{this.producersSimple}}</span> -->
          <!-- <span>{{this.studiosSimple}}</span> -->

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
      title: '',
      title_english: '',
      title_japanese: '',
      img: '',
      type: '',
      animeResponse: {},
      genres: [],
      producers: [],
      studios: [],
      genresSimple: [],
      producersSimple: [],
      studiosSimple: []
    }),
    mounted: async function (){
      this.idAnime = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/infoBy_id/'+this.idAnime);
        this.animeResponse = response.data.results.bindings
        // console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.animeResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "title":
            this.title = item.o.value
            break;
          case "title_english":
            this.title_english = item.o.value
            break;
          case "title_japanese":
            this.title_japanese = item.o.value
            break;
          case "img":
            this.img = item.o.value
            break;
          case "type":
            this.type = item.o.value
            break;
          case "hasGenre":
            this.genres.push(item.o.value.split('#')[1])
            break;
          case "hasProducer":
            this.producers.push(item.o.value.split('#')[1])
            break;
          case "hasStudio":
            this.studios.push(item.o.value.split('#')[1])
            break;
          default:
            console.log("FDS")
            break;
        }
      })
      this.genresSimple = this.genres.map(this.simplify)
      this.producersSimple = this.producers.map(this.simplify)
      this.studiosSimple = this.studios.map(this.simplify)
    },
    methods: {
      fixName: function (name) {
        name = name.replace(/GENRE_/g, "")
        name = name.replace(/PRODUCER_/g, "")
        name = name.replace(/STUDIO_/g, "")
        name = name.replace(/_/g, " ")
        return name
      },
      simplify: function (item) {
        return {
          id:item,
          label:this.fixName(item)
        }
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
