<template>
  <v-container>
    <v-flex>
      <tableOne
            name="Autores"
            :list="simple_author_list"
            route="authors"
            ></tableOne>
    </v-flex>
    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import tableOne from '@/components/tableOne'

  export default {
    components: {
      tableOne
    },
    data: () => ({
      search: '',
      author_list : [],
      simple_author_list : [],
      rows: [15,30,50,100,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Autor', align:'left', sortable:true, value:'nome',class:'title'},
      ],
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/listar_author')
        this.author_list = response.data.results.bindings
        this.simple_author_list = this.author_list.map(this.simplify)

      }
      catch(e){
        return(e);
      }
    },
     methods: {
      simplify: function (item) {
        var id = item.id.value.split("#AUTHOR_")[1]
        var nome_fix = this.fixName(id)
        return {id:id,
                nome:nome_fix
                }
      },
    fixName: function (name) {
        return name.replace(/_/g, " ")
      },
    rowClicked: function (item) {
        this.$router.push('/authors/'+item.id)
      },
      goBack: function() {
        this.$router.go(-1)
      }
    },

}
</script>
