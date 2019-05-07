<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="filmes"
      class="elevation-1"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar uma lista dos filmes...
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading"> {{props.item.ano}} </td>
          <td class="subheading"> {{props.item.tit}} </td>
          <td class="subheading"> {{props.item.id.split('#')[1]}} </td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
  import axios from 'axios'
  const lhost = "http://cinema.di.uminho.pt"

  export default {
    data: () => ({
      headers: [
        { text: 'Ano', align:'left', sortable:true, value:'ano', class:'title'},
        { text: 'Titulo', value:'tit', sortable:true, class:'title'},
        { text: 'Identificador', value:'id', sortable:true, class:'title'}
      ],
      filmes: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/filmes');
        this.filmes = response.data
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        // alert()
        this.$router.push('/filmes/'+item.id.split('#')[1])
      }
    }
  }
</script>

<style>

</style>
