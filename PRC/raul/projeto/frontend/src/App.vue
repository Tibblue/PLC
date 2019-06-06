<template>
  <v-app>
    <v-toolbar dark>
      <v-toolbar-items>
        <v-btn flat @click="goToHome()"><h2>Home</h2></v-btn>
        <v-btn flat @click="goToTable('cartas')"><h3>Cartas</h3></v-btn>
        <!-- <v-btn flat @click="goToTable('authors')"><h3>Autores</h3></v-btn>
        <v-btn flat @click="goToTable('magazines_publishers')"><h3>Revistas/Editores</h3></v-btn> -->
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
        <router-view/>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data: () => ({
      icons: [
        // ['home','http://localhost:8080'],
        ['fab fa-github','http://www.github.com/Tibblue'],
        ['fab fa-linkedin','https://www.linkedin.com/in/kiko-oliveira/'],
        ['fas fa-university','https://www.uminho.pt'],
      ]
    }),
    methods: {
      goTo: function (link) {
        // window.location = link; // opens in same tab
        window.open(link); // opens another tab
      },
      goToHome: function () {
        // this.$emit('filmeSelected', item)
        this.$router.push('/')
      },
      goToTable: function (table) {
        // this.$emit('filmeSelected', item)
        this.$router.push('/'+table)
      }
    }
  }
</script>
