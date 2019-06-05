<template>
  <v-container>

    <!-- <p>{{publisher_list}}</p> -->
    <!-- <p>{{simple_publisher_list}}</p> -->
    <v-flex xs12>
      <cardList
        name="Magazines"
        :list="simple_publisher_list"
        route="magazines"
        ></cardList>
    </v-flex>
    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
   </v-container>
</template>

<script>
  import cardList from '@/components/cardList'
  import axios from 'axios'

  export default {
    components: {
      cardList
    },
    data: () => ({
      publisher_list : [],
      simple_publisher_list : []
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/listar_publisher')
        this.publisher_list = response.data.results.bindings
        this.simple_publisher_list = this.publisher_list.map(this.simplify)

      }
      catch(e){
        return(e);
      }
    },
     methods: {
      simplify: function (item) {
        return {id:item.id.value.split("#PUBLISHER_")[1]}
      }
    },
}
</script>
