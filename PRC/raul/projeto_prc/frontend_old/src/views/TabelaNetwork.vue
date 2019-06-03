<template>
  <v-container>
    <cardTable
      name="Networks"
      :list="networksSimple"
      route="networks"
    ></cardTable>
  </v-container>

  <!-- <h1> <mark> DEBUG </mark> </h1> -->
  <!-- <p>{{networks}}</p> -->
  <!-- <p>{{networksSimple}}</p> -->
  <!-- <h1> <mark> DEBUG </mark> </h1> -->

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
      networks: [],
      networksSimple: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/network_id');
        this.networks = response.data.results.bindings
        this.networksSimple = this.networks.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        return {id:item.network.value.split('#NETWORK_')[1]}
      }
    },
  }
</script>
