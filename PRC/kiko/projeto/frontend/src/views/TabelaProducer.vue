<template>
  <v-container>
    <v-flex xs12 mt-3>
      <cardTable
        name="Producers"
        :list="producersSimple"
        route="producers"
      ></cardTable>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{producers}}</p> -->
    <!-- <p>{{producersSimple}}</p> -->
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
      producers: [],
      producersSimple: [],
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/producer_id_label');
        this.producers = response.data.results.bindings
        this.producersSimple = this.producers.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        return {
          id:item.id.value,
          label:item.label.value
        }
      }
    }
  }
</script>
