<template>
  <header-section />
  <div class="content-section">
    <div class="_container">
      <router-view />
    </div>
  </div>
  <footer-section />
</template>

<script>


  import header from "./views/HeaderView.vue"
  import footer from "./views/FooterView.vue"

  export default {
    name: "App",

    components: {
      'header-section': header,
      'footer-section': footer
    }
  }
</script>

<style>
  #app {
    width:100%;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #000000;
    background-color: #ffffff;
    height: 100%;
    
  }

  html {
    height: 100%;
  }

  body {
    min-height: 100%;
    margin: 0;
  }

  .content-section {
    width:100%;
    height:100%;
    display: flex;
    justify-content: center;
    min-height: calc(100vh - 145px);
    /* padding: 100px 50px 20px 50px; */ */
    /* box-sizing: border-box; */

    ._container {
      max-width: 1200px;
      width: 100%;
      text-align: center;
    }
  }
</style>