<template>
  <v-app dark>
    <v-toolbar dark>
      <v-toolbar-items>
        <v-btn color="indigo darken-2" @click="goToHome()"><h2>Home</h2></v-btn>
        <v-btn flat @click="goToTable('animes')"><h3>Anime</h3></v-btn>
        <v-btn flat @click="goToTable('producers')"><h3>Producer</h3></v-btn>
        <v-btn flat @click="goToTable('studios')"><h3>Studio</h3></v-btn>
      </v-toolbar-items>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn color="indigo darken-2"
          v-if="!this.$session.has('id')"
          @click="login('kiko')"
        ><h2>Login</h2></v-btn>
        <v-btn flat
          v-if="this.$session.has('id')"
          @click="logout()"
        ><h2>Logout</h2></v-btn>
        <v-btn color="indigo darken-2"
          v-if="this.$session.has('id')"
          @click="goToProfile()"
        >
          <h2>{{this.$session.get('id')}} Profile</h2>
        </v-btn>
      </v-toolbar-items>
        <!-- <v-flex v-if="this.$session.has('id')"> -->
          <v-img
            :src="this.$session.get('img')"
            aspect-ratio=1
            max-width=64
            max-height=64
          ></v-img>
        <!-- </v-flex> -->
    </v-toolbar>

    <!-- <v-container> -->
    <!-- <v-flex ma-5> -->
      <router-view/>
    <!-- </v-flex> -->
    <!-- </v-container> -->

    <v-footer dark height="auto">
      <v-card-text class="text-xs-center">
        <v-btn icon v-for="icon in icons" :key="icon[0]">
          <v-icon size="24px" @click="goTo(icon[1])">{{icon[0]}}</v-icon>
        </v-btn>
        <v-divider></v-divider>
        <v-card-text>
          2019 — <strong>Francisco Oliveira</strong> —
          Projeto de PRC (Perfil PLC), Universidade do Minho
        </v-card-text>
      </v-card-text>
    </v-footer>
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
        this.$router.push('/'+table)
      },
      login: function () {
        this.$router.push('/login')
      },
      logout: function () {
        this.$session.clear()
        this.$router.go(0)
      },
      goToProfile: function () {
        this.$router.push('/profile')
      }
    }
  }
</script>
