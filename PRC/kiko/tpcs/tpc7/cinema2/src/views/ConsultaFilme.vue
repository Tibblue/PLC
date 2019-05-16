<template>
  <v-container>
      <Meta :idFilme="$route.params.id"/>
      <Generos :idFilme="$route.params.id"/>
      <Atores :idFilme="$route.params.id"/>
      <v-layout>
        <v-btn @click="goBack()" color="info">Voltar a pagina anterior</v-btn>
      </v-layout>
  </v-container>
</template>

<script>
import Meta from '@/components/Meta'
import Generos from '@/components/Generos'
import Atores from '@/components/Atores'

export default {
  components: {
    Meta,
    Generos,
    Atores
  },
  methods: {
    goBack: function () {
      this.$router.go(-1)
    }
  }
}
</script>
