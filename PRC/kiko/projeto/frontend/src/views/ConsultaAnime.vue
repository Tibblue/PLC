<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

    <v-flex>
      <v-card>
        <v-layout>
          <v-flex xs4 ma-3>
            <v-img
              class="white--text"
              contains
              :src="this.img"
            />
          </v-flex>
          <v-flex xs4>
            <v-card-text class="text-xs-center">
              <v-flex xs12 my-4>
                <h1> {{this.title}} </h1>
              </v-flex>
              <v-flex my-2 v-if="this.title_english">
                <h2> English Title </h2>
                <h3> {{this.title_english}} </h3>
              </v-flex>
              <v-flex my-2>
                <h2> Japonese Title </h2>
                <h3> {{this.title_japanese}} </h3>
              </v-flex>
            </v-card-text>
          </v-flex>
          <v-flex xs4>
            <v-card-text class="text-xs-center">
              <v-flex xs12 my-4 v-if="this.$session.has('id')">
                <v-btn v-if="!isFav()" @click="addFav()" color="green">
                  Adicionar aos Favoritos
                </v-btn>
                <v-btn v-else @click="remFav()" color="red">
                  Remover dos Favoritos
                </v-btn>
              </v-flex>
              <v-flex xs12 my-4>
                <h1> Type: {{this.type}} </h1>
                <h2> Score: {{this.score}} </h2>
              </v-flex>
            </v-card-text>
          </v-flex>
        </v-layout>

        <v-container grid-list-sm>
          <v-layout row wrap>
            <v-flex xs6 lg4>
              <cardListAnime
                name="Genres"
                :list="genresSimple"
                route="animes?genre="
              ></cardListAnime>
            </v-flex>
            <v-flex xs6 lg4>
              <cardListAnime
                name="Producers"
                :list="producersSimple"
                route="animes?producer="
              ></cardListAnime>
            </v-flex>
            <v-flex xs12 lg4>
              <cardListAnime
                name="Studio"
                :list="studiosSimple"
                route="animes?studio="
              ></cardListAnime>
            </v-flex>
          </v-layout>

        </v-container>
      </v-card>
    </v-flex>

    <v-layout justify-center>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-layout>

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
  import cardListAnime from '@/components/cardListAnime'
  import axios from 'axios'

  export default {
    components: {
      cardListAnime
    },
    data: () => ({
      idAnime: '',
      title: '',
      title_english: '',
      title_japanese: '',
      img: '',
      type: '',
      score: '',
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
        var response = await axios.get('http://localhost:4005/query/infoBy_id/'+this.idAnime);
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
          case "score":
            this.score = item.o.value
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
          id:item.replace(/(GENRE_|PRODUCER_|STUDIO_)/g, ""),
          label:this.fixName(item)
        }
      },
      addFav: function() {
        var newFavs = this.$session.get('fav')
        newFavs.push(this.idAnime)
        var newInfo = {
          id: this.$session.get('id'),
          bio: this.$session.get('bio'),
          img: this.$session.get('img'),
          favoriteAnimes: newFavs
        }
        var headers = { headers: { 'Content-Type': 'application/json' }}
        axios.put('http://localhost:5011/users/'+this.$session.get('id')
                  ,newInfo,headers)
          .then(() => {
            // this.alert = info.data // debug
            this.$session.set('fav',newFavs)
            this.$router.go(0)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "Error adding Anime to Favorite list"
          })
      },
      remFav: function() {
        var newFavs = this.$session.get('fav')
        var index = newFavs.indexOf(this.idAnime);
        newFavs.splice(index, 1)
        var newInfo = {
          id: this.$session.get('id'),
          bio: this.$session.get('bio'),
          img: this.$session.get('img'),
          favoriteAnimes: newFavs
        }
        var headers = { headers: { 'Content-Type': 'application/json' }}
        axios.put('http://localhost:5011/users/'+this.$session.get('id')
                  ,newInfo,headers)
          .then(() => {
            // this.alert = info.data // debug
            this.$session.set('fav',newFavs)
            this.$router.go(0)
          })
          .catch(() => {
            // this.alert = error // debug
            this.alert = "Error removing Anime from Favorite list"
          })
      },
      isFav: function() {
        var newFavs = this.$session.get('fav')
        var index = newFavs.indexOf(this.idAnime);
        if( index>-1)
          return true
        return false
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
