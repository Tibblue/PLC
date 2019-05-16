<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs2>
        <h3>Titulo</h3>
      </v-flex>
      <v-flex xs10>
        <p>{{ filme.tit }}</p>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs2>
        <h3>Ano</h3>
      </v-flex>
      <v-flex xs10>
        <p>{{ filme.ano }}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
const lhost = "http://cinema.di.uminho.pt"

export default {
  props: ["idFilme"],
  data: () => ({
    filme: {}
  }),
  mounted: async function (){
    try{
      var response = await axios.get(lhost+'/filmes/'+this.idFilme)
      this.filme = response.data[0]
    }
    catch(e){
      return(e)
    }
  }
}
</script>

<style>

</style>
