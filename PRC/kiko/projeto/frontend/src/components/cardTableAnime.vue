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
          clearable
          @keyup="checkPage()"
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
          <v-flex pa-2 class="text-xs-center">
            <h1>{{currentPage}}/{{maxPage}}</h1>
          </v-flex>
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
          @click="checkPage()"
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
            xs3
          >
            <v-card
              flat hover
              dark color="grey darken-3"
              @click="itemClicked(card.id)"
            >
              <v-layout fill-height px-2 pt-1>
                <v-flex xs12 flexbox class="text-xs-center">
                  <span class="title">{{card.title}}</span>
                  <!-- <v-spacer v-if="card.title_english"/> -->
                  <!-- <span v-if="card.title_english" class="subtitle">{{card.title_english}}</span> -->
                  </v-flex>
              </v-layout>
              <v-img
                class="white--text"
                width="266"
                ratio=1.6
                :src="card.img"
              >
              </v-img>
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
      pageSize: 20,
      items: [20,30,60],
      searchText: '',
      currentPage: 1,
    }),
    methods: {
      itemClicked: function (id) {
        this.$router.push('/'+this.route+'/'+id)
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
      },
      checkPage: function() {
        var maxPage = Math.ceil(this.filteredList.length/this.pageSize)
        if(this.currentPage>maxPage)
          this.currentPage = maxPage||1
      }
    },
    computed: {
      maxPage() {
        return Math.ceil(this.filteredList.length/this.pageSize)
      },
      filteredList() {
        return this.list.filter(item => {
          var search_ok = undefined
          var search_text = this.searchText.toLowerCase()
          var title = item.title.toLowerCase()
          search_ok = title.includes(search_text)
          if(item.title_english){
            var title_english = item.title_english.toLowerCase()
            search_ok = search_ok | title_english.includes(search_text)
          }
          return search_ok
        })
      },
      pagedList() {
        return this.filteredList.filter((item,index) => {
          return index>=(this.currentPage-1)*this.pageSize
                  && index<this.currentPage*this.pageSize
        })
      }
    }
  }
</script>

<style>
.centered-input input {
  text-align: center
}
</style>
