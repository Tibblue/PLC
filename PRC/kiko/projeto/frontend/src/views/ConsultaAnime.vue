<template>
  <v-container>
    <AnimeInfo :idAnime="$route.params.id"/>
    <v-layout>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-layout>
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
