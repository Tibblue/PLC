<template>
  <v-flex>
    <!-- <span>{{this.name}}</span> -->
    <!-- <span>{{this.list}}</span> -->

    <v-toolbar dark color="indigo darken-2" flat>
      <v-flex xs12>
        <v-text-field
          v-model="searchText"
          prepend-icon="search"
          :label="'Search '+name"
          single-line
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
            v-for="(card,index) in filteredList"
            :key="card.person.value"
          >
            <v-card
              v-if="index>=currentPage*pageSize-pageSize && index<currentPage*pageSize"
              flat hover
              dark color="grey darken-2"
              @click="itemClicked(card)"
            >
              <v-container fill-height fluid pa-2>
                <v-layout fill-height>
                  <v-flex align-end flexbox>
                    <span class="subtitle">{{index}}</span>
                    <span class="title">{{card.label.value}}</span>
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
    props: ["name","list"],
    data: () => ({
      pageSize: 30,
      items: [20,30,60,100],
      searchText: '',
      currentPage: 1,
    }),
    methods: {
      itemClicked: function (item) {
        this.$router.push('/persons/'+item.person.value.split('#PERSON_')[1])
      },
      fixName: function (name) {
        // TODO: remover _ e outras coisas assim que apareçam
        return name.split('#PERSON_')[1]
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
          var name = item.person.value.split('#PERSON_')[1]
          return name.toLowerCase().includes(this.searchText.toLowerCase())
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
