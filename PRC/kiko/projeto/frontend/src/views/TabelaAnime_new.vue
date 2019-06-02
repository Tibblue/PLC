<template>
  <v-container>

    <v-flex xs12>
      <cardTableAnime
        name="Animes"
        :list="animesSimple"
        route="animes"
      ></cardTableAnime>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{animes}}</p> -->
    <!-- <p>{{animesSimple}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
  </v-container>
</template>

<script>
  import cardTableAnime from '@/components/cardTableAnime_new'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardTableAnime
    },
    data: () => ({
      animes: [],
      animesSimple: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/anime_titles_img_score');
        this.animes = response.data.results.bindings
        this.animesSimple = this.animes.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        var title_aux
        if(item.title_english)
          title_aux = item.title_english.value
        else
          title_aux = undefined
        return {
          id: item.id.value,
          title: item.title.value,
          title_english: title_aux,
          img: item.img.value,
        }
      }
    },
  }
</script>
