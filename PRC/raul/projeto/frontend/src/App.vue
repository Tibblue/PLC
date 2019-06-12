<template>
  <v-app dark>
    <v-toolbar dark>
      <v-toolbar-items>
        <v-btn flat @click="goToHome()"><h2>Home</h2></v-btn>
        <v-btn flat @click="goToTable('cartas')"><h3>Cards</h3></v-btn>
        <v-btn flat @click="goToTable('cartasview')"><h3>Cards View</h3></v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
        <router-view/>
    </v-content>
    <v-footer white height="auto">
      <v-card-text class="text-xs-center">
        <!-- <v-container grid-list-md text-xs-center  > -->
          <v-layout row wrap justify-center>
            <v-flex xs3>
              <v-toolbar white flat>
                <strong>Raul Vilas Boas - </strong>
                Projeto de PRC
                <v-img
                  flat
                  @click="goTo('https://playhearthstone.com/en-us/')"
                  src="https://images-na.ssl-images-amazon.com/images/I/919avEb7fmL.png"
                  height="50"
                  contain
                >
                </v-img>
                <v-img
                  flat
                  @click="goTo('https://github.com/MrBoas/PRC')"
                  src="https://scontent.flis7-1.fna.fbcdn.net/v/t1.15752-9/62343009_1508182902649833_850383011844194304_n.png?_nc_cat=109&_nc_ht=scontent.flis7-1.fna&oh=db3292325591fd617577a9fc87210415&oe=5D7E823C"
                  height="50"
                  contain
                  >
                </v-img>
                <!-- <v-img flat @click="goTo('https://www.youtube.com/watch?v=dQw4w9WgXcQ')">
                  <h3>MEMES</h3>
                </v-img> -->
              </v-toolbar>
            </v-flex>
          </v-layout>
        <!-- </v-container> -->
      </v-card-text>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data: () => ({
        icons: [
        ['fab fa-github','http://www.github.com/Tibblue'],
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