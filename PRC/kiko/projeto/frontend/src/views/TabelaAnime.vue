<template>
  <v-container>
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{this.$route.query.genre}}</p> -->
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
  import cardTableAnime from '@/components/cardTableAnime'

  export default {
    components: {
      cardTableAnime
    }
  }
</script>
