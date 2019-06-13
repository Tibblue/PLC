<template>
  <v-container>
    <v-card-title>
      <h1 style="color:White;">Lista de Cartas</h1>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_set"
        :items="simple_sets_list"
        label="Select a set to filter..."
        @change="refreshList()"
        dark
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_playerclass"
        :items="simple_playerclass_list"
        label="Select a class to filter..."
        @change="refreshList()"
        dark
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_type"
        :items="simple_types_list"
        label="Select a type to filter..."
        @change="refreshList()"
        dark
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_rarity"
        :items="simple_rarity_list"
        label="Select a rarity to filter..."
        @change="refreshList()"
        dark
      ></v-combobox>
      <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="search"
              label="Search"
              single-line
              dark
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
          <td class="subheading"> {{props.item.type}} </td>
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
      sets_list: [],
      simple_sets_list:[],
      playerclass_list:[],
      simple_playerclass_list:[],
      types_list:[],
      simple_types_list:[],
      rarity_list:[],
      simple_rarity_list:[],

      rows: [10,20,30,50,100,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Name', align:'left', sortable:true, value:'nome',class:'title'},
        { text: 'Set', sortable:true, value:'set',class:'title'},
        { text: 'Class', sortable:true, value:'classe',class:'title'},
        { text: 'Type', sortable:true, value:'type',class:'title'},
        { text: 'Rarity', sortable:true, value:'rarity',class:'title'},
      ],
      select_set:'All',
      select_playerclass:'All',
      select_type:'All',
      select_rarity:'All'
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/lista_cartas_info')
        this.cartas_list = response.data.results.bindings
        this.simple_cartas_list = this.cartas_list.map(this.simplify)

        var response_sets = await axios.get('http://localhost:4005/query/listar_sets')
        this.sets_list = response_sets.data.results.bindings
        this.simple_sets_list = this.sets_list.map(this.simplify_set)
        this.simple_sets_list.unshift("All")
        this.simple_sets_list.sort()

        var response_playerclass = await axios.get('http://localhost:4005/query/listar_playerclass')
        this.playerclass_list = response_playerclass.data.results.bindings
        this.simple_playerclass_list = this.playerclass_list.map(this.simplify_class)
        this.simple_playerclass_list.unshift("All")
        this.simple_playerclass_list.sort()

        var response_type = await axios.get('http://localhost:4005/query/listar_types')
        this.types_list = response_type.data.results.bindings
        this.simple_types_list = this.types_list.map(this.simplify_atri)
        this.simple_types_list.unshift("All")
        this.simple_types_list.sort()

        var response_rarity = await axios.get('http://localhost:4005/query/listar_rarities')
        this.rarity_list = response_rarity.data.results.bindings
        this.simple_rarity_list = this.rarity_list.map(this.simplify_atri)
        this.simple_rarity_list.unshift("All")
        this.simple_rarity_list.sort()
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
        var type

        if(item.name != undefined)
          nome = item.name.value
        else
          nome = ""

        if(item.set != undefined)
          set = item.set.value.split("#SET_")[1]
        else
          set = ""

        if(item.playerclass != undefined){
          playerclass = item.playerclass.value.split("#PLAYERCLASS_")[1]
        }
        else
          playerclass = ""

        if(item.rarity != undefined){
          rarity = item.rarity.value
        }
        else
          rarity = ""

        if(item.type != undefined){
          type = item.type.value
        }
        else
          type = ""

        var id = item.id.value.split("#CARD_")[1]

        return {id:id,
                nome:nome,
                set:set,
                classe:playerclass,
                rarity:rarity,
                type:type
        }
      },
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
        rowClicked: function (item) {
        this.$router.push('/cartas/'+item.id)
      },
      simplify_set: function (item) {
        item =  item.o.value.split("#SET_")[1]
        return item
      },
      simplify_class: function (item) {
        item =  item.o.value.split("#PLAYERCLASS_")[1]
        return item
      },
      simplify_atri: function (item) {
        item= item.o.value.toLowerCase()
        item= item.charAt(0).toUpperCase() + item.slice(1)
        return item
      },
      goBack: function() {
        this.$router.go(-1)
      },
      refreshList: async function () {
        var query = '?'
        if(this.select_set!='All')
          query+= 'set='+this.select_set+'&'
        if(this.select_playerclass!='All')
          query+= 'player_class='+this.select_playerclass+'&'
        if(this.select_type!='All')
          query+= 'type='+this.select_type+'&'
        if(this.select_rarity!='All')
          query+= 'rarity='+this.select_rarity+'&'
        try{
          var response = await axios.get('http://localhost:4005/query/filtros/tabela_filtros'+query);
          this.cartas_list = response.data.results.bindings
          this.simple_cartas_list = this.cartas_list.map(this.simplify)
        }
        catch(e){
          return(e);
        }
      },
    },
}
</script>
