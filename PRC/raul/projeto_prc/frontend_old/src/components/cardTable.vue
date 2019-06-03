<template>
  <v-flex>
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <span>{{this.name}}</span> -->
    <!-- <span>{{this.list}}</span> -->
    <!-- <span>{{this.route}}</span> -->
    <!-- <span>{{filteredList}}</span> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex xs12>
        <v-text-field
          single-line
          v-model="searchText"
          prepend-icon="search"
          :label="'Search '+name"
        ></v-text-field>
      </v-flex>
    </v-toolbar>
    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex xs1/>
      <v-flex xs6>
        <v-layout>
          <v-btn icon @click="currentPage=1">
            <v-icon>{{'fas fa-angle-double-left'}}</v-icon>
          </v-btn>
          <v-btn icon @click="previousPage()">
            <v-icon>{{'fas fa-caret-left'}}</v-icon>
          </v-btn>
          <v-text-field
            solo flat readonly
            single-line
            class="centered-input"
            background-color="indigo darken-2"
            v-model="currentPage"
          ></v-text-field>
          <v-btn icon @click="nextPage()">
            <v-icon>{{'fas fa-caret-right'}}</v-icon>
          </v-btn>
          <v-btn icon @click="currentPage=Math.ceil(filteredList.length/pageSize)">
            <v-icon>{{'fas fa-angle-double-right'}}</v-icon>
          </v-btn>
        </v-layout>
      </v-flex>
      <v-flex xs1/>
      <v-flex xs3>
        <v-combobox
          v-model="pageSize"
          :items="items"
          label="Elements per Page"
        ></v-combobox>
      </v-flex>
      <v-flex xs1/>
    </v-toolbar>
    <v-card>
      <v-container fluid grid-list-md>
        <v-layout row wrap>
          <v-flex
            v-for="card in pagedList"
            :key="card.id"
          >
            <v-card
              flat hover
              dark color="grey darken-2"
              @click="itemClicked(card)"
            >
              <v-container fill-height fluid pa-2>
                <v-layout fill-height>
                  <v-flex align-end flexbox>
                    <span class="title">{{fixName(card.id)}}</span>
                    <v-spacer v-if="card.label"/>
                    <span v-if="card.label" class="subtitle">{{card.label}}</span>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<script>
  export default {
    props: ["name","list","route"],
    data: () => ({
      pageSize: 30,
      items: [20,30,60,100],
      searchText: '',
      currentPage: 1,
    }),
    methods: {
      itemClicked: function (item) {
        this.$router.push('/'+this.route+'/'+item.id)
      },
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
      nextPage: function () {
        if(this.currentPage<this.filteredList.length/this.pageSize)
          this.currentPage++
      },
      previousPage: function () {
        if(this.currentPage>1)
          this.currentPage--
      }
    },
    computed: {
      filteredList() {
        return this.list.filter(item => {
          var name = item.id
          return name.toLowerCase().includes(this.searchText.toLowerCase())
        })
      },
      pagedList() {
        var filtered = this.list.filter((item) => {
          var name = item.id
          // var label = item.label
          return name.toLowerCase().includes(this.searchText.toLowerCase())
        })
        var paged = filtered.filter((item,index) => {
          return index>=(this.currentPage-1)*this.pageSize
                  && index<this.currentPage*this.pageSize
        })
        return paged
      }
    }
  }
</script>

<style>
.centered-input input {
  text-align: center
}
</style>
