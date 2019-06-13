<template>
  <v-flex>
    <v-toolbar dark color="grey darken-4" flat>
      <v-text-field
        single-line
        clearable
        v-model="searchText"
        prepend-icon="search"
        label="Search"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_set"
        :items="simple_sets_list"
        label="Select a set to filter..."
        @change="refreshList()"
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_playerclass"
        :items="simple_playerclass_list"
        label="Select a type to filter..."
        @change="refreshList()"
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_type"
        :items="simple_types_list"
        label="Select a type to filter..."
        @change="refreshList()"
      ></v-combobox>
      <v-spacer></v-spacer>
      <v-combobox
        v-model="select_rarity"
        :items="simple_rarity_list"
        label="Select a type to filter..."
        @change="refreshList()"
      ></v-combobox>
    </v-toolbar>
    <v-card>
      <v-container fluid grid-list-md>
        <v-layout row wrap>
          <v-flex
            v-for="card in filteredList"
            :key="card.id"
            xs2
          >
            <v-card
              flat hover
              dark color="grey darken-2"
              @click="itemClicked(card.id)"
            >
              <v-layout fill-height >
                <v-flex xs12 flexbox class="text-xs-center" mt-2>
                  <span class="title">{{card.nome}}</span>
                </v-flex>
              </v-layout >
                <v-flex >
                  <v-img
                    lazy-src = "https://scontent.flis7-1.fna.fbcdn.net/v/t1.15752-9/64226172_2524130620939642_2425744520294432768_n.png?_nc_cat=111&_nc_ht=scontent.flis7-1.fna&oh=2c72b9a7338179e06630a6fd07b97943&oe=5D825607"
                    class="white--text"
                    height="400"
                    :src="card.img"
                    contain
                  >
                  </v-img>
                </v-flex>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    components: {
      },
    data: () => ({
      searchText:'',
      cartas_list:[],
      simple_cartas_list:[],
      sets_list:[],
      simple_sets_list:[],
      playerclass_list:[],
      simple_playerclass_list:[],
      types_list:[],
      simple_types_list:[],
      rarity_list:[],
      simple_rarity_list:[],
      select_set:'Nothing',
      select_playerclass:'Nothing',
      select_type:'Nothing',
      select_rarity:'Nothing'
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/lista_cartas_info_limit')
        this.cartas_list = response.data.results.bindings
        this.simple_cartas_list = this.cartas_list.map(this.simplify)

        var response_sets = await axios.get('http://localhost:4005/query/listar_sets')
        this.sets_list = response_sets.data.results.bindings
        this.simple_sets_list = this.sets_list.map(this.simplify_set)
        this.simple_sets_list.sort()
        this.simple_sets_list.unshift("Nothing")

        var response_playerclass = await axios.get('http://localhost:4005/query/listar_playerclass')
        this.playerclass_list = response_playerclass.data.results.bindings
        this.simple_playerclass_list = this.playerclass_list.map(this.simplify_class)
        this.simple_playerclass_list.sort()
        this.simple_playerclass_list.unshift("Nothing")

        var response_type = await axios.get('http://localhost:4005/query/listar_types')
        this.types_list = response_type.data.results.bindings
        this.simple_types_list = this.types_list.map(this.simplify_atri)
        this.simple_types_list.sort()
        this.simple_types_list.unshift("Nothing")

        var response_rarity = await axios.get('http://localhost:4005/query/listar_rarities')
        this.rarity_list = response_rarity.data.results.bindings
        this.simple_rarity_list = this.rarity_list.map(this.simplify_atri)
        this.simple_rarity_list.sort()
        this.simple_rarity_list.unshift("Nothing")
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
        var img = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/" + id + ".png"
        return {id:id,
                nome:nome,
                set:set,
                classe:playerclass,
                rarity:rarity,
                type:type,
                img:img
        }
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
      itemClicked: function (id) {
        this.$router.push('/cartas'+'/'+id)
      },
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
        rowClicked: function (item) {
        this.$router.push('/cartas/'+item.id)
      },
      goBack: function() {
        this.$router.go(-1)
      },
      refreshList: async function () {
        var query = '?'
        if(this.select_set!='Nothing')
          query+= 'set='+this.select_set+'&'
        if(this.select_playerclass!='Nothing')
          query+= 'player_class='+this.select_playerclass+'&'
        if(this.select_type!='Nothing')
          query+= 'type='+this.select_type+'&'
        if(this.select_rarity!='Nothing')
          query+= 'rarity='+this.select_rarity+'&'
        try{
          var response = await axios.get('http://localhost:4005/query/filtros/tabela_filtros_limit'+query);
          this.cartas_list = response.data.results.bindings
          this.simple_cartas_list = this.cartas_list.map(this.simplify)
        }
        catch(e){
          return(e);
        }
      },
    },
    computed:{
      filteredList() {
        return this.simple_cartas_list.filter(item => {
          var search_ok = undefined
          var search_text = this.searchText.toLowerCase()
          var nome = item.nome.toLowerCase()
          search_ok = nome.includes(search_text)
          return search_ok
        })
      },
    }

}
</script>
