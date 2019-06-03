<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> {{this.label}} </h1>
          <h1 v-else> {{fixName(this.idNetwork)}} </h1>
        </v-card-text>

        <v-container>
          <v-layout>
            <v-flex xs6 mr-2>
              <cardTable
                name="Directed"
                :list="directedSimple"
                route="animes"
              ></cardTable>
            </v-flex>
            <v-flex xs6 ml-2>
              <cardTable
                name="Wrote"
                :list="wroteSimple"
                route="animes"
              ></cardTable>
            </v-flex>
          </v-layout>
          <!-- <span>{{this.directedSimple}}</span> -->
          <!-- <span>{{this.wroteSimple}}</span> -->
        </v-container>
      </v-card>



    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <h1> PERSON: {{this.idPerson}} </h1> -->
    <!-- <p> {{personResponse}} </p> -->
    <!-- <li v-for="item in personResponse" :key="item"> -->
      <!-- <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}} -->
    <!-- </li> -->
    <!-- <h1> <mark> DEBUG </mark> </h1> -->

  </v-container>
</template>

<script>
  import cardTable from '@/components/cardTable'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardTable
    },
    data: () => ({
      idPerson: '',
      personResponse: {},
      label: '',
      directed: [],
      wrote: [],
      directedSimple: [],
      wroteSimples: [],
      dbpedia: ''
    }),
    mounted: async function (){
      this.idPerson = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/person_info_id/'+this.idPerson);
        this.personResponse = response.data.results.bindings
        // console.log(this.personResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.personResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            break;
          case "directed":
            this.directed.push(item.o.value.split('#ANIME_')[1])
            break;
          case "wrote":
            this.wrote.push(item.o.value.split('#ANIME_')[1])
            break;
          case "dbpedia":
            this.dbpedia = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      })
      this.directedSimple = this.directed.map(item => {return {id:item}})
      this.wroteSimple = this.wrote.map(item => {return {id:item}})
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
