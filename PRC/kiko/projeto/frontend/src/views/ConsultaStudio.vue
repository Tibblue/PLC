<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label"> {{this.label}} </h1>
          <h1 v-else> {{fixName(this.idStudio)}} </h1>
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
    <!-- <h1> NETWORK: {{this.idStudio}} </h1> -->
    <!-- <li v-for="item in studioResponse" :key="item"> -->
      <!-- <b>{{item.p.value.split('#')[1]}} :</b> {{item.o.value}} -->
    <!-- </li> -->
    <!-- <p> {{studioResponse}} </p> -->
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
      idStudio: '',
      id: '',
      label: '',
      studioResponse: {},
      animes: [],
      animesSimple: [],
    }),
    mounted: async function (){
      this.idStudio = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/infoBy_id/'+this.idStudio);
        this.studioResponse = response.data.results.bindings
        // console.log(this.studioResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.studioResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "id":
            this.id = item.o.value
            break;
          case "label":
            this.label = item.o.value
            break;
          case "designedBy":
            this.animes.push(item.o.value.split('#')[1])
            break;
          default:
            console.log("FDS")
            break;
        }
      })
      this.animesSimple = this.animes.map(this.simplify)
    },
    methods: {
      simplify: function (item) {
        return {
          id:item,
          label:this.fixName(item)
        }
      },
      fixName: function (name) {
        name = name.replace(/ANIME_\d+/g, "") // removes id number at the start
        name = name.replace(/_/g, " ")
        return name
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
