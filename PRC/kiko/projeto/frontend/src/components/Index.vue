<template>
  <v-flex>
    <!-- <v-card-title>
      <v-text-field
        append-icon="search"
        label="Search"
        single-line
      />
    </v-card-title> -->
    <h1 @click="goToTable('animes')">Animes</h1>
    <h1 @click="goToTable('producers')">Producers</h1>
    <h1 @click="goToTable('studios')">Studios</h1>
  </v-flex>
</template>

<script>
  export default {
    data: () => ({
      // animes: []
    }),
    methods: {
      goToTable: function (table) {
        this.$router.push('/'+table)
      }
    }
  }
</script>

<style>

</style>
