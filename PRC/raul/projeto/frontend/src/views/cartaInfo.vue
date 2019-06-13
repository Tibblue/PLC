1<template>
  <v-container>
    <v-flex>
      <v-card>
        <v-card-text class="text-xs-center">
          <h1 v-if="this.label">{{this.nome}} </h1>
          <h1 v-else> {{fixName(this.idCarta)}} </h1>
        </v-card-text>
        <v-layout>
          <v-flex xs6 ml-5 >
            <v-flex ml-5 mt-3>
              <h1>Informação:</h1>
              <p v-if="this.label">
                <font size="5"> <b>ID:</b></font>
                <font size="4"> {{this.label}} </font>
              </p>
              <p v-if="this.set">
                <font size="5"> <b>Set:</b></font>
                <font size="4"> {{this.set}} </font>
              </p>
              <p v-if="this.playerclass">
                <font size="5"> <b>Class:</b></font>
                <font size="4"> {{this.playerclass}} </font>
              </p>
              <p v-if="this.type">
                <font size="5"> <b>Type:</b></font>
                <font size="4"> {{this.type}} </font>
              </p>
              <p v-if="this.attack">
                <font size="5"> <b>Attack:</b></font>
                <font size="4"> {{this.attack}} </font>
              </p>
              <p v-if="this.health">
                <font size="5"> <b>Health:</b></font>
                <font size="4"> {{this.health}} </font>
              </p>
              <p v-if="this.cost">
                <font size="5"> <b>Cost:</b></font>
                <font size="4"> {{this.cost}} </font>
              </p>
              <p v-if="this.rarity">
                <font size="5"> <b>Rarity</b>:</font>
                <font size="4"> {{this.rarity}} </font>
              </p>
              <p v-if="this.text">
                <font size="5"> <b>Text:</b></font>
                <font size="4"> {{this.text}} </font>
              </p>
            </v-flex>
          </v-flex>
          <v-flex xs3>
            <v-card elevation=0>
              <v-img
                lazy-src = "https://media0.giphy.com/media/sSgvbe1m3n93G/giphy.gif?cid=790b76115cf931896d4c323655356431&rid=giphy.gif"
                :src="this.image"
                height="500"
                contain
              ></v-img>
            </v-card>
          </v-flex>
        </v-layout>
      </v-card>
    </v-flex>

    <v-flex>
      <v-btn @click="goBack()" color="black" dark>Voltar à página anterior</v-btn>
    </v-flex>
  </v-container>
</template>

<script>
  import cardList from '@/components/cardList'
  import axios from 'axios'
  const lhost = "http://localhost:4005"

  export default {
    components: {
      cardList
    },
    data: () => ({
      idCarta: '',
      carta_info: {},
      image: '',
      label: '',
      nome: '',
      set: '',
      attack:'',
      health:'',
      cost:'',
      rarity:'',
      text:'',
      playerclass: '',
      type:'',
      authors: [],
      authorsSimple: [],
    }),
    mounted: async function (){
      this.idCarta = this.$route.params.id
      try{
        var response = await axios.get(lhost+'/query/carta_info/'+this.idCarta);
        this.carta_info = response.data.results.bindings
      }
      catch(e){
        return(e);
      }
      this.carta_info.forEach(item => {
        switch (item.p.value.split('#')[1]) {
          case "label":
            this.label = item.o.value
            this.image = "https://art.hearthstonejson.com/v1/render/latest/enUS/256x/" + this.label + ".png"
            break;
          case "name":
            this.nome = item.o.value
            break;
          case "hasSet":
            switch(this.set = item.o.value.split('#SET_')[1]){
              case "EXPERT1":
                this.set = "Hall of Fame"
                break
              case "CORE":
                this.set = "Classic"
                break
              case "TGT":
                this.set = "The Grand Tournament"
                break
              case "OG":
                this.set = "Whispers of the Old Gods"
                break
              case "KARA":
                this.set = "One Night in Karazhan"
                break
              case "BRM":
                this.set = "Blackrock Mountain"
                break
              case "GANGS":
                this.set = "Mean Streets of Gadgetzan"
                break
              case "HERO_SKINS":
                this.set = "Hero Skin"
                break
              case "CREDITS":
                this.set = "Credit Card"
                break
              case "GVG":
                this.set = "Goblins vs Gnomes"
                break
              case "NAXX":
                this.set = "Naxxramas"
                break
              case "TB":
                this.set = "Tavern Brawl"
                break
              case "LOE":
                this.set = "The League of Explorers"
                break
              case "PROMO":
                this.set = "Promo"
                break
              case "MISSIONS":
                this.set = "Mission"
                break
              case "CHEAT":
                this.set = "Cheat"
                break
              case "REWARD":
                this.set = "Reward"
                break
            }
            break;
          case "hasPlayerClass":
            this.playerclass = item.o.value.split('#PLAYERCLASS_')[1]
            break;
          case "attack":
            this.attack = item.o.value
            break;
          case "health":
            this.health = item.o.value
            break;
          case "cost":
            this.cost = item.o.value
            break;
          case "rarity":
            this.rarity = item.o.value
            break;
          case "text":
            this.text =item.o.value
            break;
          case "type":
            this.type = item.o.value
            break;
          default:
            console.log("FDS")
            break;
        }
      })
    },
    methods: {
      fixName: function (name) {
        return name.replace(/_/g, " ")
      },
      simplify: function (item) {
        return {id:item}
      },
      goBack: function() {
        this.$router.go(-1)
      },
      capitalizeFirstLetter(string)
      {
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
      }
    }
  }
</script>
