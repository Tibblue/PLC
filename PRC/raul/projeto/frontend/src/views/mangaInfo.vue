1<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1>
    <p>{{manga_info}}</p>
    <p>{{authors}}</p>
    <p>{{magazines}}</p>
    <p>{{publishers}}</p>
    <p>{{first_publication}}</p>
    <p>{{last_publication}}</p>
    <p>{{num_volumes}}</p> -->

    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> Anime: {{this.label}} </h1>
          <h1 v-else> {{fixName(this.idManga)}} </h1>
        </v-card-text>

        <v-container grid-list-sm>
          <h1>Informação:</h1>
          <v-flex>
            <h2> Data da primeira publicação: {{first_publication[0]}} </h2>
            <h2> Data da última publicação: {{last_publication[0]}} </h2>
            <h2> Número de volumas: {{num_volumes[0]}} </h2>
          <!-- <v-spacer></v-spacer> -->
          </v-flex>
          <v-layout row wrap>
            <v-flex xs3 mt-2 mr-2>
              <cardList
                name="Authors"
                :list="authorsSimple"
                route="authors"
              ></cardList>
            </v-flex>
            <v-flex xs3 mt-2 mr-2>
              <cardList
                name="Magazines"
                :list="magazinesSimple"
                route="magazines"
              ></cardList>
            </v-flex>
            <v-flex xs3 mt-2>
              <cardList
                name="Publisher"
                :list="publishersSimple"
                route="publisher"
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
    <!-- <h1> ANIME: {{this.idManga}} </h1> -->
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
      idManga: '',
      manga_info: {},
      label: '',
      authors: [],
      authorsSimple: [],
      magazines: [],
      magazinesSimple:[],
      publishers: [],
      publishersSimple:[],
      first_publication: [],
      last_publication: [],
      num_volumes: [],

      // last_publicationSimple:[],

    }),
    mounted: async function (){
      this.idManga = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/manga_info_id/'+this.idManga);
        this.manga_info = response.data.results.bindings
        // console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.manga_info.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            break;
          case "hasAuthor":
            this.authors.push(item.o.value.split('#AUTHOR_')[1])
            break;
          case "hasMagazine":
            this.magazines.push(item.o.value.split('#MAGAZINE_')[1])
            break;
          case "hasPublisher":
            this.publishers.push(item.o.value.split('#PUBLISHER_')[1])
            break;
          case "last_publication":
            this.last_publication.push(item.o.value)
            break;
          case "first_publication":
            this.first_publication.push(item.o.value)
            break;
          case "num_volumes":
            this.num_volumes.push(item.o.value)
            break;
          default:
            console.log("FDS")
            break;
        }
      })
      this.authorsSimple = this.authors.map(this.simplify)
      this.magazinesSimple = this.magazines.map(this.simplify)
      this.publishersSimple = this.publishers.map(this.simplify)
      // this.last_publicationSimple = this.last_publication.map(this.simplify)

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
