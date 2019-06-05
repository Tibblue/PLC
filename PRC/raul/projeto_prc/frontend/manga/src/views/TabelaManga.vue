<template>
  <v-container>

    <!-- <p>{{manga_list[0]}}</p>
    <p>{{simple_manga_list[0]}}</p> -->
    <!-- <v-flex xs12>
      <cardList
        name="Mangas"
        :list="simple_manga_list"
        route="mangas"
        ></cardList>
    </v-flex> -->
    <v-card-title>
      <h1> Lista de Mangas </h1>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="simple_manga_list"
      :search="search"
      :rows-per-page-items = "rows"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar uma lista...
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading"> {{props.item.nome}} </td>
          <td class="subheading"> {{props.item.data_i}} </td>
          <td class="subheading"> {{props.item.data_f}} </td>
          <td class="subheading"> {{props.item.nvol}} </td>
        </tr>
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </template>
    </v-data-table>
    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
   </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    components: {
    },
    data: () => ({
      search:'',
      manga_list : [],
      simple_manga_list : [],
      rows: [10,20,30,50,100,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Manga', align:'left', sortable:true, value:'nome',class:'title'},
        { text: 'Data Início', sortable:true, value:'data_i',class:'title'},
        { text: 'Data Fim', sortable:true, value:'data_f',class:'title'},
        { text: 'Número Volumes', sortable:true, value:'nvol',class:'title'},
      ],
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
        var data_inicio
        var data_fim
        var num_volumes

        if(item.data_i != undefined)
          data_inicio = item.data_i.value
        else
          data_inicio = ""

        if(item.data_f != undefined)
          data_fim = item.data_f.value
        else
          data_fim = ""

        if(item.nvol != undefined)
          num_volumes = item.nvol.value
        else
          num_volumes = ""

        var id = item.id.value.split("#MANGA_")[1]
        var nome_fix = this.fixName(id)

        return {id:id,
                data_i:data_inicio,
                data_f:data_fim,
                nvol:num_volumes,
                nome:nome_fix
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
