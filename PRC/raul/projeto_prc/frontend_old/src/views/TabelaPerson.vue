<template>
  <v-container>
    <v-layout>
      <v-flex xs6 mr-2>
        <cardTable
          name="Writers"
          :list="writersSimple"
          route="persons"
        ></cardTable>
      </v-flex>

      <v-flex xs6 ml-2>
        <cardTable
          name="Directors"
          :list="directorsSimple"
          route="persons"
        ></cardTable>
      </v-flex>
    </v-layout>

    <v-flex xs12 mt-3>
      <cardTable
        name="Persons"
        :list="personsSimple"
        route="persons"
      ></cardTable>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{writers}}</p> -->
    <!-- <p>{{writersSimple}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{directors}}</p> -->
    <!-- <p>{{directorsSimple}}</p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{persons}}</p> -->
    <!-- <p>{{personsSimple}}</p> -->
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
      directors: [],
      personsSimple: [],
      writersSimple: [],
      directorsSimple: [],
    }),
    mounted: async function (){
      try{
        var response
        response = await axios.get(lhost+'/query/person_id');
        this.persons = response.data.results.bindings
        this.personsSimple = this.persons.map(this.simplify)
        response = await axios.get(lhost+'/query/writer_id');
        this.writers = response.data.results.bindings
        this.writersSimple = this.writers.map(this.simplify)
        response = await axios.get(lhost+'/query/director_id');
        this.directors = response.data.results.bindings
        this.directorsSimple = this.directors.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        return {id:item.person.value.split('#PERSON_')[1]}
      }
    }
  }
</script>
