<template>
  <v-container>
    <v-card-title>
      <v-text-field
        v-model="searchText"
        append-icon="search"
        label="Search"
        single-line
      ></v-text-field>
      <v-spacer/>
      <v-text-field
        v-model="pagination.page"
        label="Page number"
      ></v-text-field>
    </v-card-title>
    <!-- <p>{{networks}}</p> -->
    <v-data-table
      :headers="headers"
      :items="networks"
      :search="searchText"
      :rows-per-page-items="rowsPerPage"
      :pagination.sync="pagination"
      class="elevation-1"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar a lista de networks...
        </v-alert>
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          A pesquisa por "{{searchText}}" não teve resultados.
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading"> {{props.item.network.value.split('#NETWORK_')[1]}} </td>
          <td v-if="props.item.label" class="subheading"> {{props.item.label.value}} </td>
          <td v-else > <p><i>No Label</i></p> </td>
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
      pagination: {},
      rowsPerPage: [6,9,15,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Network', value:'network.value', align:'left', sortable:true, class:'title'},
        { text: 'Label', value:'label.value', sortable:true, class:'title'}
      ],
      networks: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/network_label');
        this.networks = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.networks) // debug
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      rowClicked: function (item) {
        this.$router.push('/networks/'+item.network.value.split('#NETWORK_')[1])
      }
    }
  }
</script>

<style>

</style>
