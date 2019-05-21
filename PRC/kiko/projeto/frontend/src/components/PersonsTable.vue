<template>
  <v-flex>
    <v-layout>
    <v-flex xs6 mr-2>
      <cardTable
        name="Writers"
        :list="writers"
      ></cardTable>
    </v-flex>

    <v-flex xs6 ml-2>
      <cardTable
        name="Directors"
        :list="directors"
      ></cardTable>
    </v-flex>
    </v-layout>

<!--
    <v-layout justify-center>
      <v-flex xs12>
        <v-toolbar color="indigo darken-2" dark>
          <v-toolbar-title>Persons</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-flex xs6>
            <v-text-field
              v-model="searchTextPersons"
              append-icon="search"
              label="Search"
              single-line
            ></v-text-field>
          </v-flex>
        </v-toolbar>

        <v-card>
          <v-container fluid grid-list-md>
            <v-layout row wrap>
              <v-flex
                v-for="(card,index) in filteredPersons"
                :key="card.person.value"
              >
                <v-card v-if="index<100"
                  flat hover
                  dark color="grey darken-2"
                  @click="itemClicked(card)"
                >
                  <v-container fill-height fluid pa-2>
                    <v-layout fill-height>
                      <v-flex align-end flexbox>
                        <span class="title" v-text="card.label.value"></span>
                      </v-flex>
                    </v-layout>
                  </v-container>

                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout> -->

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{writers}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{directors}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{persons}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

  </v-flex>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"
  import cardTable from '@/components/cardTable'

  export default {
    components: {
      cardTable
    },
    data: () => ({
      searchTextPersons: '',
      persons: [],
      writers: [],
      directors: []
    }),
    mounted: async function (){
      try{
        var response
        // response = await axios.get(lhost+'/query/person_label');
        // this.persons = response.data.results.bindings
        response = await axios.get(lhost+'/query/writer_label');
        this.writers = response.data.results.bindings
        response = await axios.get(lhost+'/query/director_label');
        this.directors = response.data.results.bindings
        // console.log(this.persons) // debug
        // console.log(this.writers) // debug
        // console.log(this.directors) // debug
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      itemClicked: function (item) {
        this.$router.push('/persons/'+item.person.value.split('#PERSON_')[1])
      },
      fixName: function (name) {
        // TODO: remover _ e outras coisas assim que apareçam
        return name.split('#PERSON_')[1]
      },
      nextPage: function () {
        if(this.currentPageWriters<this.writers.length/this.pageSize)
          this.currentPageWriters++
      },
      previousPage: function () {
        if(this.currentPageWriters>1)
          this.currentPageWriters--
      }
    },
    computed: {
      filteredPersons() {
        return this.persons.filter(item => {
          var name = item.person.value.split('#PERSON_')[1]
          return name.toLowerCase().includes(this.searchTextPersons.toLowerCase())
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
