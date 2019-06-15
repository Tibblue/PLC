<template>
  <v-container>
    <v-layout my-3>
      <v-flex xs2/>
      <v-flex xs8>
        <login/>
      </v-flex>
      <v-flex xs2/>
    </v-layout>
    <v-layout my-3>
      <v-flex xs2/>
      <v-flex xs8>
        <signIn/>
      </v-flex>
      <v-flex xs2/>
    </v-layout>
  </v-container>
</template>

<script>
  import login from '@/components/login'
  import signIn from '@/components/signIn'

  export default {
    mounted: async function (){
      // redirect to root if already logged in
      if(this.$session.has('id'))
        this.$router.push('/')
    },
    components: {
      login,
      signIn
    }
  }
</script>
