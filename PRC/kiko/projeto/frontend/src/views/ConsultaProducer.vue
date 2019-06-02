<template>
  <v-container>
    <!-- <h1>{{fixName(this.$route.params.id)}}</h1> -->

      <v-card>
        <v-card-text class="text-xs-center">
          <h1> {{this.label}} </h1>
        </v-card-text>

        <v-container>
          <cardTable
            name="Anime"
            :list="animesSimple"
            route="animes"
          ></cardTable>
          <!-- <span>{{this.animesSimple}}</span> -->
        </v-container>
      </v-card>

    <v-flex>
      <v-btn @click="goBack()" color="info">Voltar à página anterior</v-btn>
    </v-flex>

    <!-- <h1> <mark> DEBUG </mark> </h1> -->
    <!-- <h1> PRODUCER: {{this.idProducer}} </h1> -->
    <!-- <p> {{animeResponse}} </p> -->
    <!-- <li v-for="item in animeResponse" :key="item"> -->
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
      idProducer: '',
      id: '',
      label: '',
      animeResponse: {},
      animes: [],
      animesSimple: [],
      dbpedia: ''
    }),
    mounted: async function (){
      this.idProducer = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/infoBy_id/'+this.idProducer);
        this.animeResponse = response.data.results.bindings
        // console.log(this.animeResponse) // debug
      }
      catch(e){
        return(e);
      }
      this.animeResponse.forEach(item => {
        // console.log(item)
        switch (item.p.value.split('#')[1]) {
          case "id":
            this.id = item.o.value
            break;
          case "label":
            this.label = item.o.value
            break;
          case "produced":
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
        name = name.replace(/ANIME_\d+/g, " ")
        name = name.replace(/_/g, " ")
        return name
      },
      goBack: function() {
        this.$router.go(-1)
      }
    }
  }
</script>
