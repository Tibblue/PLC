<template>
  <v-flex>
    <h1> <mark> DEBUG </mark> </h1>
    <!-- <span>{{this.name}}</span> -->
    <!-- <span>{{this.genre}}</span> -->
    <!-- <span>{{this.genres}}</span> -->
    <!-- <span>{{this.animes}}</span> -->
    <!-- <span>{{this.animesSimple}}</span> -->
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
      <v-flex xs6 pb-2>
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
      <v-flex xs4 px-2>
        <v-combobox
          v-model="pageSize"
          :items="nItems"
          label="Elements per Page"
          @change="checkPage()"
        ></v-combobox>
      </v-flex>
    </v-toolbar>
    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex xs4 px-2>
        <v-combobox
          v-model="genreSelected"
          :items="genres"
          label="Genre"
          @change="refreshList()"
        ></v-combobox>
      </v-flex>
      <v-flex xs4 px-2>
        <v-combobox
          v-model="producerSelected"
          :items="producers"
          label="Producer"
          @change="refreshList()"
        ></v-combobox>
      </v-flex>
      <v-flex xs4 px-2>
        <v-combobox
          v-model="studioSelected"
          :items="studios"
          label="Studio"
          @change="refreshList()"
        ></v-combobox>
      </v-flex>
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
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    props: ["name","route"],
    data: () => ({
      pageSize: 8,
      genreSelected: 'Any',
      producerSelected: 'Any',
      studioSelected: 'Any',
      nItems: [20,30,60],
      genres: [],
      producers: [],
      studios: [],
      searchText: '',
      currentPage: 1,
      animes: [],
      animesSimple: [],
    }),
    mounted: async function (){
      try{
        var response
        response = await axios.get(lhost+'/query/variable/anime_much_info');
        this.animes = response.data.results.bindings
        this.animesSimple = this.animes.map(this.simplify)

        // genre list
        response = await axios.get(lhost+'/query/genre_list');
        this.genre = response.data.results.bindings
        this.genres = this.genre.map(item => {return item.genre.value.split("#GENRE_")[1]})
        this.genres.sort()
        this.genres.unshift('Any')
        // // producer list
        // response = await axios.get(lhost+'/query/genre_list');
        // this.genre = response.data.results.bindings
        // this.genres = this.genre.map(item => {return item.genre.value.split("#GENRE_")[1]})
        // this.genres.sort()
        // this.genres.unshift('Any')
        // // studio list
        // response = await axios.get(lhost+'/query/genre_list');
        // this.genre = response.data.results.bindings
        // this.genres = this.genre.map(item => {return item.genre.value.split("#GENRE_")[1]})
        // this.genres.sort()
        // this.genres.unshift('Any')
      }
      catch(e){
        return(e);
      }
    },
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
      },
      refreshList: async function () {
        this.nameNew = this.name
        var query = '?'
        if(this.genreSelected!='Any')
          query+= 'genre='+this.genreSelected+'&'
        console.log(query)
        try{
          var response = await axios.get(lhost+'/query/variable/anime_much_info'+query);
          this.animes = response.data.results.bindings
          this.animesSimple = this.animes.map(this.simplify)
        }
        catch(e){
          return(e);
        }
        // this.$router.push('/'+this.route+query)
      },
      simplify: function (item) {
        var title_aux
        if(item.title_english)
          title_aux = item.title_english.value
        else
          title_aux = undefined
        return {
          id: item.id.value,
          title: item.title.value,
          title_english: title_aux,
          img: item.img.value,
        }
      }
    },
    computed: {
      maxPage() {
        return Math.ceil(this.filteredList.length/this.pageSize)
      },
      filteredList() {
        return this.animesSimple.filter(item => {
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
