<template>
  <v-container>
    <AnimeInfo :idAnime="$route.params.id"/>
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
  import AnimeInfo from '@/components/AnimeInfo'

  export default {
    components: {
      AnimeInfo
    },
    methods: {
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
