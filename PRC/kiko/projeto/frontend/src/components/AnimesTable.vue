<template>
  <v-container>

    <v-layout justify-center>
      <v-flex xs12>
        <v-toolbar color="indigo darken-2" dark>
          <v-toolbar-title>Animes</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-flex xs6>
            <v-text-field
              v-model="searchText"
              append-icon="search"
              label="Search"
              single-line
            ></v-text-field>
          </v-flex>
        </v-toolbar>

        <v-card>
          <v-container fluid grid-list-md>
            <v-layout row wrap>
              <v-flex
                v-for="card in filteredList"
                :key="card.anime.value"
              >
                <v-card
                  flat hover
                  dark color="grey darken-2"
                  @click="itemClicked(card)"
                >
                  <v-container fill-height fluid pa-2>
                    <v-layout fill-height>
                      <v-flex align-end flexbox>
                        <span v-if="card.label" class="title" v-text="card.label.value"></span>
                        <span v-else class="title" v-text="fixName(card.anime.value)"></span>
                      </v-flex>
                    </v-layout>
                  </v-container>

                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>

    <!-- <p>{{animes}}</p> -->
    <v-data-table
      :headers="headers"
      :items="animes"
      :search="searchText"
      :rows-per-page-items="rowsPerPage"
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
        <tr @click="itemClicked(props.item)">
          <td class="subheading"> {{props.item.anime.value.split('#ANIME_')[1]}} </td>
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
      rowsPerPage: [5,10,25,{"text":"$vuetify.dataIterator.rowsPerPageAll","value":-1}],
      headers: [
        { text: 'Anime', value:'anime.value', align:'left', sortable:true, class:'title'},
        { text: 'Label', value:'label.value', sortable:true, class:'title'},
      ],
      animes: []
    }),
    mounted: async function (){
      try{
        var response = await axios.get(lhost+'/query/anime_label');
        this.animes = response.data.results.bindings
        // console.log(encoded) // debug
        console.log(this.animes) // debug
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      itemClicked: function (item) {
        this.$router.push('/animes/'+item.anime.value.split('#ANIME_')[1])
      },
      fixName: function (name) {
        return name.split('#ANIME_')[1]
      }
    },
    computed: {
      filteredList() {
        return this.animes.filter(item => {
          var name = item.anime.value.split('#ANIME_')[1]
          return name.toLowerCase().includes(this.searchText.toLowerCase())
        })
      }
    }
  }
</script>

<style>

</style>
