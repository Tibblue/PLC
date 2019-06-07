<template>
  <v-flex>
    <!-- <p>{{cartas_list[0]}}</p>
    <p>{{simple_cartas_list[0]}}</p> -->
    <v-card>
      <v-container fluid grid-list-md>
        <v-layout row wrap>
          <v-flex
            v-for="card in simple_cartas_list"
            :key="card.id"
            xs3
          >
          <!-- <p>{{card.nome}}</p> -->
            <v-card
              flat hover
              dark color="grey darken-3"
              @click="itemClicked(card.id)"
            >
              <v-layout fill-height px-2 pt-1>
                <v-flex xs12 flexbox class="text-xs-center">
                  <span class="title">{{card.nome}}</span>
                  <v-spacer v-if="card.title_english"/>
                  <span v-if="card.title_english" class="subtitle">{{card.title_english}}</span>
                  </v-flex>
              </v-layout>
              <v-img
                class="white--text"
                width="266"
                ratio=1.6
                :src="card.img"
              >
              </v-img>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-flex>
</template>

<script>
  import axios from 'axios'

  export default {
    components: {
      },
    data: () => ({
      cartas_list:[],
      simple_cartas_list:[]
    }),
    mounted: async function () {
      try{
        var response = await axios.get('http://localhost:4005/query/listar_id_nome')
        this.cartas_list = response.data.results.bindings
        this.simple_cartas_list = this.cartas_list.map(this.simplify)
      }
      catch(e){
        return(e);
      }
    },
    methods: {
      simplify: function (item) {
        var nome
        var img
        if(item.name != undefined)
          nome = item.name.value
        else
          nome = ""

        var id = item.id.value.split("#CARD_")[1]
        img = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/" + id + ".png"

        return {id:id,
                nome:nome,
                img:img
        }
      },
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
        rowClicked: function (item) {
        this.$router.push('/cartas/'+item.id)
      },
      goBack: function() {
        this.$router.go(-1)
      },
    },
}
</script>
