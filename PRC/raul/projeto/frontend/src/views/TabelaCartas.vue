<template>
  <v-container>

    <!-- <p>{{cartas_list[0]}}</p>
    <p>{{simple_cartas_list[0]}}</p> -->

    <v-card-title>
      <h1> Lista de Cartas </h1>
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
      :items="simple_cartas_list"
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
          <td class="subheading"> {{props.item.set}} </td>
          <td class="subheading"> {{props.item.classe}} </td>
          <td class="subheading"> {{props.item.rarity}} </td>
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
      cartas_list : [],
      simple_cartas_list : [],
      rows: [10,20,30,50,100,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Nome', align:'left', sortable:true, value:'nome',class:'title'},
        { text: 'Set', sortable:true, value:'set',class:'title'},
        { text: 'Classe', sortable:true, value:'classe',class:'title'},
        { text: 'Raridade', sortable:true, value:'rarity',class:'title'},
      ],
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/lista_cartas_info')
        this.cartas_list = response.data.results.bindings
        this.simple_cartas_list = this.cartas_list.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        var nome
        var set
        var playerclass
        var rarity

        if(item.name != undefined)
          nome = item.name.value
        else
          nome = ""

        if(item.set != undefined)
          set = item.set.value.split("#SET_")[1]
        else
          set = ""

        if(item.playerclass != undefined)
          playerclass = item.playerclass.value.split("#PLAYERCLASS_")[1]
        else
          playerclass = ""

        if(item.rarity != undefined)
          rarity = item.rarity.value
        else
          rarity = ""

        var id = item.id.value.split("#CARD_")[1]
        // var nome_fix = this.fixName(id)

        return {id:id,
                nome:nome,
                set:set,
                classe:playerclass,
                rarity:rarity
        }
      },
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
        rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        // alert()
        this.$router.push('/cartas/'+item.id)
      },
      goBack: function() {
        this.$router.go(-1)
      }
    },
}
</script>
