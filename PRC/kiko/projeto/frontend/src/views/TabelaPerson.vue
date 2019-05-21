<template>
  <v-container>
  <!-- <v-flex ma-4 px-4> -->
    <!-- <v-flex px-4><v-flex px-4> -->
      <PersonsTable/>
    <!-- </v-flex></v-flex> -->
  <!-- </v-flex> -->
  </v-container>
</template>

<script>
  import PersonsTable from '@/components/PersonsTable'

  export default {
    components: {
      PersonsTable
    }
  }
</script>
