<template>
  <v-container>
    <v-card-title>
      <h1> Lista de {{this.name}}</h1>
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
      :items="this.list"
      :search="search"
      :rows-per-page-items = "rows"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar uma lista...
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="itemClicked(props.item.id)">
          <td class="subheading"> {{props.item.nome}} </td>
        </tr>
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </template>
    </v-data-table>

   </v-container>
</template>

<script>
  export default {
    props: ["name","list","route"],
    data: () => ({
      search:'',
      searchText: '',
      rows: [10,15,30,50,100,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text:"", align:'left', sortable:true, value:'nome',class:'title'},
      ],
    }),
    methods: {
      itemClicked: function (item) {
        this.$router.push('/'+this.route+'/'+item)
      },
    },
  }
</script>

<style>
</style>
