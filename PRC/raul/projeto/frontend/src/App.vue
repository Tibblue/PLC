<template>
  <v-app>
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
    <v-footer dark height="auto">
      <v-card-text class="text-xs-center">
        <!-- <v-btn icon v-for="icon in icons" :key="icon[0]">
          <v-icon size="24px" @click="goTo(icon[1])">{{icon[0]}}</v-icon>
        </v-btn> -->
        <!-- <v-divider></v-divider> -->
        <v-card-text>
          <strong>Raul Vilas Boas</strong> -
          Projeto de PRC
        </v-card-text>
        <v-btn flat @click="goTo('https://playhearthstone.com/en-us/')">
          <v-img
            src="https://images-na.ssl-images-amazon.com/images/I/919avEb7fmL.png"
          ></v-img>
        </v-btn>
        <v-btn flat @click="goTo('https://github.com/MrBoas/PRC')">
          <v-img
            src="https://image.flaticon.com/icons/svg/25/25231.svg"
          ></v-img>
        </v-btn>
        <v-btn flat @click="goTo('https://www.youtube.com/watch?v=dQw4w9WgXcQ')">
          <h3>MEMES</h3>
        </v-btn>
      </v-card-text>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data: () => ({
      icons: [
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
