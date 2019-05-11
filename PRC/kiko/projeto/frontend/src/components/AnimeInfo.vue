<template>
  <v-container>
    <h2 xs2> ANIME: {{this.idAnime}} </h2>
    <p> {{anime}} </p>
  </v-container>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    props: ["idAnime"],
    data: () => ({
      anime: {}
    }),
    mounted: async function (){
      try{
        var query = `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :ANIME_`+this.idAnime+` ?p ?o .
}`
        var encoded = encodeURIComponent(query)
        var response = await axios.get(lhost+'/sparqlQuery?query='+encoded);
        // var response = await axios.get(lhost+'/query/PRC_Proj-anime_label');
        this.anime = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.anime) // debug
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        // alert("click! \n"+item.anime.value)
        this.$router.push('/animes/'+item.anime.value.split('#ANIME_')[1])
      }
    }
  }
</script>

<style>

</style>
