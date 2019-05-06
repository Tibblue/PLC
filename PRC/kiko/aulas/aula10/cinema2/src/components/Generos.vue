<template>
  <v-container>
    <v-layout row wrap v-if="generos.length>0">
      <v-flex xs2>
        <h3>Generos</h3>
      </v-flex>
      <v-flex xs10>
        <span v-for="(gen, index) in generos" :key="index">
          {{ gen.g.split('#gen_')[1] }},
        </span>
      </v-flex>
    </v-layout>
    <v-layout row wrap v-else>
      <v-flex xs12>
        <p>Sem generos associados</p>
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
      generos: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/filmes/'+this.idFilme+'/generos');
        this.generos = response.data
      }
      catch(e){
        return(e);
      }
    }
  }
</script>

<style>

</style>
