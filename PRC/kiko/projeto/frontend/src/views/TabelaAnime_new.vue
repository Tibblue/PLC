<template>
  <v-container>
    <h1> <mark> DEBUG </mark> </h1>
    <!-- <p>{{animes}}</p> -->
    <!-- <p>{{animesSimple}}</p> -->
    <p>{{this.$route.query.genre}}</p>
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

    <v-flex xs12>
      <cardTableAnime
        name="Animes"
        route="animes"
      ></cardTableAnime>
    </v-flex>
  </v-container>
</template>

<script>
  import cardTableAnime from '@/components/cardTableAnime_new'

  export default {
    components: {
      cardTableAnime
    }
  }
</script>
