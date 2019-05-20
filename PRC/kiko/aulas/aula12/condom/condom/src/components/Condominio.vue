<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs2>
        <v-subheader>Receita: </v-subheader>
      </v-flex>
      <v-flex xs2>
          <v-subheader> {{ receita }}</v-subheader>
      </v-flex>
      <v-flex xs2>
        <v-subheader>Despesa: </v-subheader>
      </v-flex>
      <v-flex xs2>
          <v-subheader> {{ despesa }}</v-subheader>
      </v-flex>
      <v-flex xs2>
        <v-subheader>NºDespesas: </v-subheader>
      </v-flex>
      <v-flex xs2>
          <v-subheader> {{ lista.length }}</v-subheader>
      </v-flex>
    </v-layout>

    <hr />

    <v-layout>
        <v-flex xs2>
          <v-text-field
            label="Data"
            v-model="novo.data"
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs2>
            <v-select
                v-model="novo.tipo"
                :items="valoresTipo"
                :rules="[v => !!v || 'Tipo é obrigatório']"
                label="Tipo"
                required
            ></v-select>
        </v-flex>
        <v-flex xs2>
          <v-text-field
            label="Valor"
            v-model="novo.valor"
            mask="#####"
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs4>
          <v-text-field
            label="Descrição"
            v-model="novo.desc"
            solo
          ></v-text-field>
        </v-flex>

        <v-flex xs2 text-xs-center>
            <v-btn
                round
                color="green"
                dark
                @click="adicionaItem"
                >Adicionar</v-btn>
        </v-flex>
    </v-layout>

    <v-layout row wrap>
        <v-flex xs12>
        <v-data-table
            :headers="cabecalhos"
            :items="lista"
            class="elevation-1"
        >
            <template v-slot:items="props">
                <td>{{ props.item.data }}</td>
                <td>{{ props.item.tipo }}</td>
                <td class="text-xs-right">{{ props.item.valor }}</td>
                <td>{{ props.item.desc }}</td>
                <td><v-btn
                  dark round
                  color="red darken-4"
                  @click="removeItem(props.item)"
                  >Remover</v-btn></td>
            </template>
        </v-data-table>
        </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data: () => ({
      receita: 0,
      despesa: 0,
      lista: [],
      novo: {
          id: 0,
          data: "",
          tipo: "Receita",
          valor: 0,
          desc: ""
      },
      valoresTipo: ["Receita", "Despesa"],
      cabecalhos: [
          { text: 'Data', sortable: true, value: 'data' },
          { text: 'Tipo', sortable: false, value: 'tipo' },
          { text: 'Valor', value: 'valor' },
          { text: 'Descrição', value: 'desc' }
        ],
    }),

    methods: {
        adicionaItem: function(){
            if(this.lista.length>0)
              this.novo.id = this.lista[this.lista.length-1].id+1
            this.lista.push(JSON.parse(JSON.stringify(this.novo)))
            if(this.novo.tipo == "Despesa"){
                this.despesa += parseInt(this.novo.valor);
            }
            else{
                this.receita += parseInt(this.novo.valor);
            }
        },
        removeItem: function(item){
            var index = this.lista.findIndex(elem => elem.id == item.id)
            if(index != -1){
                this.lista.splice(index,1)
            }
            else{
                this.erro = true
            }
        }
    }
  }
</script>