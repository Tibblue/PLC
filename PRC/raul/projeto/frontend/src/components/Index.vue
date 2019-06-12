<template>
  <v-flex dark>

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
    <!-- <v-flex xs3> -->
    <v-layout align-center justify-center fill-height>
      <!-- </v-flex> -->
      <v-flex xs8>
        <!-- <v-flex mt-5> -->
          <v-img
            src="https://3.bp.blogspot.com/-FxftVuWop1Y/V38sX5qzsJI/AAAAAAAADj0/1hMhFXpLYjclaSrv0BSnMkGglgrSpsXvgCKgB/s1600/Hearthstone%2BLogo.png">
          </v-img>
        <!-- </v-flex> -->
      </v-flex>
    </v-layout>
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