<template>
  <div>
      <h3>
          Gestion d'hotel très sérieuse !!!!
          <layout />
      </h3>
  </div>
</template>

<script type="coffee-script"  lang="coffee">
import Layout from 'components/layout/Layout'
export default 
    mounted: ->
        console.log "App Entry monté avec succès"

    components:{
        Layout
    }

    data: ->
        return {

        }

</script>

<style>

</style>
