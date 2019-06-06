<template>
  <v-flex>
    <!-- <v-card-title>
      <v-text-field
        append-icon="search"
        label="Search"
        single-line
      />
    </v-card-title> -->
    <!-- <h1 @click="goToTable('cartas')">cartas</h1> -->
    <!-- <h1 @click="goToTable('authors')">Autores</h1>
    <h1 @click="goToTable('magazines_publishers')">Revistas/Editoras</h1> -->
    <!-- <h1 @click="goToTable('publishers')">Editoras</h1> -->

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
