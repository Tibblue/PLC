<template>
  <v-container>

    <!-- <p>{{publisher_list}}</p> -->
    <!-- <p>{{simple_publisher_list}}</p> -->
    <v-layout>
      <v-flex xs6 mr-2>
        <tableOne
          name="Revistas"
          :list="simple_magazine_list"
          route="magazines"
          ></tableOne>
      </v-flex>
      <v-flex xs6 ml-2>
        <tableOne
          name="Editoras"
          :list="simple_publisher_list"
          route="publisher"
          ></tableOne>
      </v-flex>
    </v-layout>
    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
   </v-container>
</template>

<script>
  import tableOne from '@/components/tableOne'
  import axios from 'axios'

  export default {
    components: {
      tableOne
    },
    data: () => ({
      magazine_list : [],
      simple_magazine_list : [],
      publisher_list : [],
      simple_publisher_list : [],
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/listar_magazine')
        this.magazine_list = response.data.results.bindings
        this.simple_magazine_list = this.magazine_list.map(this.simplify)

        var response2 = await axios.get('http://localhost:4005/query/listar_publisher')
        this.publisher_list = response2.data.results.bindings
        this.simple_publisher_list = this.publisher_list.map(this.simplify2)

      }
      catch(e){
        return(e);
      }
    },
     methods: {
      simplify: function (item) {

        var id = item.id.value.split("#MAGAZINE_")[1]
        var nomefix = this.fixName(id)

        return {id:id,
                nome:nomefix
        }
      },
      simplify2: function (item) {
        var id = item.id.value.split("#PUBLISHER_")[1]
        var nomefix = this.fixName(id)

        return {id:id,
                nome:nomefix
                }
      },

      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
        rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        // alert()
        this.$router.push('/mangas/'+item.id)
      },
      goBack: function() {
        this.$router.go(-1)
      }

    },
}
</script>
