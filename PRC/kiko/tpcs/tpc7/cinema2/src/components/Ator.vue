<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs2>
        <h3>Ator</h3>
      </v-flex>
      <v-flex xs10>
        <p>{{ ator.nome }}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
const lhost = 'http://cinema.di.uminho.pt'
export default {
  props: ['idAtor'],
  data: () => ({
    ator: {}
  }),
  mounted: async function () {
    try {
      var response = await axios.get(lhost + '/atores/' + this.idAtor)
      this.ator = response.data[0]
    } catch (e) {
      return e
    }
  }
}
</script>

<style>

</style>
