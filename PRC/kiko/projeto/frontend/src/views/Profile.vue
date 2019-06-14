<template>
  <v-container>
    <v-layout my-3>
      <v-flex xs8 offset-xs2>
        <profile/>
      </v-flex>
    </v-layout>
    <v-layout my-3>
      <v-flex xs8 offset-xs2>
        <profileEdit/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import profile from '@/components/profile'
  import profileEdit from '@/components/profileEdit'

  export default {
    mounted: async function (){
      // redirect to root if not already logged in
      if(!this.$session.has('id'))
        this.$router.push('/')
    },
    components: {
      profile,
      profileEdit
    }
  }
</script>
