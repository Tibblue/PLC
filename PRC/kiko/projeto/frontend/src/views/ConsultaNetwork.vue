<template>
  <v-container>
    <NetworkInfo :idNetwork="$route.params.id"/>
    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>
  </v-container>
</template>

<script>
  import NetworkInfo from '@/components/NetworkInfo'

  export default {
    components: {
      NetworkInfo
    },
    methods: {
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
