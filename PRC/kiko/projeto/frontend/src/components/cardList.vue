<template>
  <v-flex>
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <span>{{this.name}}</span> -->
    <!-- <span>{{this.list}}</span> -->
    <!-- <span>{{this.route}}</span> -->
    <!-- <span>{{filteredList}}</span> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

    <v-flex xs12>
      <v-card>
        <v-toolbar color="indigo" dark>
          <v-toolbar-title> {{this.name}} </v-toolbar-title>
        </v-toolbar>
        <v-list subheader>
          <template v-for="item in this.list">
            <v-list-tile @click="itemClicked(item.id)" :key="item.id">
              <v-list-tile-content>
                <v-list-tile-title> {{item.label}} </v-list-tile-title>
                <!-- <v-list-tile-subtitle> {{item.id}} </v-list-tile-subtitle> -->
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
      </v-card>
    </v-flex>

  </v-flex>
</template>

<script>
  export default {
    props: ["name","list","route"],
    data: () => ({
      searchText: '',
    }),
    methods: {
      itemClicked: function (item) {
        this.$router.push('/'+this.route+'/'+item)
      },
    },
    computed: {
      filteredList() {
        return this.list.filter(item => {
          var name = item.id
          return name.toLowerCase().includes(this.searchText.toLowerCase())
        })
      }
    }
  }
</script>

<style>
</style>
