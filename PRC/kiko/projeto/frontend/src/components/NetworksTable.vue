<template>
  <v-container>

    <v-layout justify-center>
      <v-flex xs12>
        <v-toolbar color="indigo darken-2" dark>
          <v-toolbar-title>Networks</v-toolbar-title>
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
                :key="card.network.value"
              >
                <v-card
                  flat hover
                  dark color="grey darken-2"
                  @click="itemClicked(card)">
                    <v-container fill-height fluid pa-2>
                      <v-layout fill-height>
                        <v-flex align-end flexbox>
                          <span class="title" v-text="fixName(card.network.value)"></span>
                          <v-spacer/>
                          <span class="subtitle" v-text="fixName(card.network.value)"></span>
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

    <!-- <p>{{networks}}</p> -->

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
      itemClicked: function (item) {
        this.$router.push('/networks/'+item.network.value.split('#NETWORK_')[1])
      },
      fixName: function (name) {
        return name.split('#NETWORK_')[1]
      }
    },
    computed: {
      filteredList() {
        return this.networks.filter(item => {
          var name = item.network.value.split('#NETWORK_')[1]
          return name.toLowerCase().includes(this.searchText.toLowerCase())
        })
      }
    }
  }
</script>

<style>

</style>
