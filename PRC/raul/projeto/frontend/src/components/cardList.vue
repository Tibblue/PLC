<template>
    <v-flex xs12>
      <v-card>
        <v-toolbar color="blue darken-3" dark>
          <v-toolbar-title> {{this.name}} </v-toolbar-title>
        </v-toolbar>
        <v-list subheader>
          <template v-for="item in this.list">
            <v-list-tile @click="itemClicked(item.id)" :key="item.id">
              <v-list-tile-content>
                <v-list-tile-title> {{fixName(item.id)}} </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
      </v-card>
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
      fixName: function (name) {
        return name.replace(/_/g, " ")
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
