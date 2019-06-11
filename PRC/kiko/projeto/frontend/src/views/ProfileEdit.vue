<template>
  <v-container>
    <v-layout>
      <v-flex xs2/>
      <v-flex xs8>
        <profileEdit/>
      </v-flex>
      <v-flex xs2/>
    </v-layout>
  </v-container>
</template>

<script>
  import profileEdit from '@/components/profileEdit'

  export default {
    mounted: async function (){
      // redirect to root if not already logged in
      if(!this.$session.has('id'))
        this.$router.push('/')
    },
    components: {
      profileEdit
    }
  }
</script>
