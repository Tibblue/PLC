<template>
  <v-container>

    <!-- <p>{{manga_list}}</p> -->
    <!-- <p>{{simple_manga_list}}</p> -->
    <v-flex xs12>
      <cardList
        name="Mangas"
        :list="simple_manga_list"
        route="/mangas"
        ></cardList>
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
      manga_list : [],
      simple_manga_list : []
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/lista_manga')
        this.manga_list = response.data.results.bindings
        this.simple_manga_list = this.manga_list.map(this.simplify)

      }
      catch(e){
        return(e);
      }
    },
     methods: {
      simplify: function (item) {
        return {id:item.id.value.split("#MANGA_")[1]}
      }
    },
}
</script>
