<template>
  <v-container>
    <v-card-title>
      <v-text-field
        v-model="searchText"
        append-icon="search"
        label="Search"
        single-line
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="animes"
      :search="searchText"
      item-key="anime"
      class="elevation-1"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar a lista de animes...
        </v-alert>
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          A pesquisa por "{{searchText}}" não teve resultados.
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading"> {{props.item.anime.value.split('#ANIME_')[1]}} </td>
          <td v-if="props.item.label" class="subheading"> {{props.item.label.value}} </td>
          <td v-else > <p><i>No Label</i></p> </td>
          <!-- <td class="subheading"> {{props.item.writer.value.split('#WRITER_')[1]}} </td> -->
          <!-- <td class="subheading"> {{props.item.director.value.split('#DIRECTOR_')[1]}} </td> -->
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    data: () => ({
      searchText: '',
      headers: [
        { text: 'Anime', value:'anime', align:'left', sortable:true, class:'title'},
        { text: 'Label', value:'label', sortable:true, class:'title'},
        // { text: 'Writer', value:'writer', sortable:true, class:'title'},
        // { text: 'Director', value:'director', sortable:true, class:'title'}
      ],
      animes: []
    }),
    mounted: async function (){
      try{
        var query = `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  ?anime a :Anime .
  OPTIONAL {?anime :label ?label .}
}`
        var encoded = encodeURIComponent(query)
        var response = await axios.get(lhost+'/sparqlQuery?query='+encoded);
        // var response = await axios.get(lhost+'/query/PRC_Proj-anime_label');
        this.animes = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.animes) // debug
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        // alert("click! \n"+item.anime.value)
        this.$router.push('/animes/'+item.anime.value.split('#ANIME_')[1])
      }
    }
  }
</script>

<style>

</style>
