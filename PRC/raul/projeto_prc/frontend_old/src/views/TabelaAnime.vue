<template>
  <v-container>

    <v-flex xs12>
      <cardTable
        name="Animes"
        :list="animesSimple"
        route="animes"
      ></cardTable>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{animes}}</p> -->
    <!-- <p>{{animesSimple}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
  </v-container>
</template>

<script>
  import cardTable from '@/components/cardTable'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardTable
    },
    data: () => ({
      animes: [],
      animesSimple: []
    }),
    mounted: async function (){
      try{
        if(this.$session.has('animesSimple'))
          this.animesSimple = this.$session.get('animesSimple')
        else
          var response = await axios.get(lhost+'/query/anime_label');
          this.animes = response.data.results.bindings
          this.animesSimple = this.animes.map(this.simplify)
          this.$session.set('animesSimple',this.animesSimple)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        return {id:item.anime.value.split('#ANIME_')[1]}
      }
    },
  }
</script>
