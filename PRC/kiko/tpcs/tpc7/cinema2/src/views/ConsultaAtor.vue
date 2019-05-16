<template>
  <v-container>
      <Ator :idAtor="$route.params.id"/>
      <v-layout>
        <v-btn @click="goBack()" color="info">Voltar a pagina anterior</v-btn>
      </v-layout>
  </v-container>
</template>

<script>
import Ator from '@/components/Ator'

export default {
  components: {
    Ator
  },
  methods: {
    goBack: function () {
      this.$router.go(-1)
    }
  }
}
</script>
