<template>
  <v-container>
    <PersonInfo :idPerson="$route.params.id"/>
    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>
  </v-container>
</template>

<script>
  import PersonInfo from '@/components/PersonInfo'

  export default {
    components: {
      PersonInfo
    },
    methods: {
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
