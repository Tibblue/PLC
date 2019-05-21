<template>
  <v-flex>
    <NetworksTable />
    <!-- <p>{{networks}}</p> -->
  </v-flex>
</template>

<script>
  import NetworksTable from '@/components/NetworksTable'

  export default {
    components: {
      NetworksTable
    }
  }
</script>
