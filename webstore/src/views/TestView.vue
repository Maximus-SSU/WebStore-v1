<template>
    <div >
        <simplebutton title= "Show Fish Test" @click="displayText">
    <p v-if="showText">{{ "Hello" }}</p>></simplebutton>
    </div>
  </template>

<script>
  import simplebutton from '@/components/SimpleButton.vue'

  export default {
    name: 'IndexView',
    components: {
      simplebutton
    }
  }
</script>