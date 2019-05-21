<template>
  <v-container>
    <v-layout>
    <v-flex xs6 mr-2>
      <cardTable
        name="Writers"
        :list="writers"
        route="persons"
      ></cardTable>
    </v-flex>

    <v-flex xs6 ml-2>
      <cardTable
        name="Directors"
        :list="directors"
        route="persons"
      ></cardTable>
    </v-flex>
    </v-layout>

    <v-flex xs10 >
      <cardTable
        name="Persons"
        :list="persons"
        route="persons"
      ></cardTable>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{writers}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{directors}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{persons}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

  </v-container>
</template>

<script>
  import cardTable from '@/components/cardTable'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardTable
    },
    data: () => ({
      persons: [],
      writers: [],
      directors: []
    }),
    mounted: async function (){
      try{
        var response
        response = await axios.get(lhost+'/query/person_id');
        this.persons = response.data.results.bindings
        response = await axios.get(lhost+'/query/writer_id');
        this.writers = response.data.results.bindings
        response = await axios.get(lhost+'/query/director_id');
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
    }
  }
</script>
