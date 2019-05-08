<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="animes"
      class="elevation-1"
    >
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="warning">
          Não foi possivel apresentar a lista de animes...
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading"> {{props.item.anime.value.split('#ANIME_')[1]}} </td>
          <td class="subheading"> {{props.item.label.value}} </td>
          <td class="subheading"> {{props.item.writer.value.split('#WRITER_')[1]}} </td>
          <td class="subheading"> {{props.item.director.value.split('#DIRECTOR_')[1]}} </td>
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
      headers: [
        { text: 'Anime', value:'anime', align:'left', sortable:true, class:'title'},
        { text: 'Label', value:'label', sortable:true, class:'title'},
        { text: 'Writer', value:'writer', sortable:true, class:'title'},
        { text: 'Director', value:'director', sortable:true, class:'title'}
      ],
      animes: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/PRC_Proj-anime_info');
        this.animes = response.data.results.bindings
        console.log(this.animes)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      rowClicked: function (item) {
        // this.$emit('filmeSelected', item)
        alert("click! \n"+item.anime.value)
        // this.$router.push('/filmes/'+item.id.split('#')[1])
      }
    }
  }
</script>

<style>

</style>
