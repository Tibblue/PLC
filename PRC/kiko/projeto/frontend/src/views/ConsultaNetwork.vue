<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> {{this.label}} </h1>
          <h1 v-else> {{fixName(this.idNetwork)}} </h1>
        </v-card-text>

        <v-container>
          <v-flex xs12>
            <cardTable
              name="Animes"
              :list="animesSimple"
              route="animes"
            ></cardTable>
          </v-flex>
        </v-container>
        <!-- <span>{{this.animesSimple}}</span> -->

      </v-card>
    </v-flex>

    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <h1> NETWORK: {{this.idNetwork}} </h1> -->
    <!-- <li v-for="item in networkResponse" :key="item"> -->
      <!-- <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}} -->
    <!-- </li> -->
    <!-- <p> {{networkResponse}} </p> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

  </v-container>
</template>

<script>
  import cardTable from '@/components/cardTable'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardTable,
    },
    data: () => ({
      idNetwork: '',
      networkResponse: {},
      label: '',
      animes: [],
      animesSimple: [],
      dbpedia: '',
    }),
    mounted: async function (){
      this.idNetwork = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/network_info_id/'+this.idNetwork);
        this.networkResponse = response.data.results.bindings
        console.log(this.networkResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.networkResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            break;
          case "produced":
            this.animes.push(item.o.value.split('#ANIME_')[1])
            break;
          case "dbpedia":
            this.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      })
      this.animesSimple = this.animes.map(item => {return {id:item}})
    },
    methods: {
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
