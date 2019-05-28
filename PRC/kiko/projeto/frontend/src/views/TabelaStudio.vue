<template>
  <v-container>
    <cardTable
      name="Studio"
      :list="studiosSimple"
      route="studios"
    ></cardTable>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <p>{{studios}}</p> -->
    <!-- <p>{{studiosSimple}}</p> -->
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
      studios: [],
      studiosSimple: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/studio_id_label');
        this.studios = response.data.results.bindings
        this.studiosSimple = this.studios.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        return {id:item.id.value, label:item.label.value}
      }
    },
  }
</script>
