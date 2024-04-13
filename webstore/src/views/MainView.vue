<template>
<div>
  <span class="text_main">
  Главная страница
  </span>
</div>
<div class="mainpage-link-container">
          <RouterLinkButton link="/TestPage" title="Test"></RouterLinkButton>
          <RouterLinkButton link="/Store" title="Store"></RouterLinkButton>
      </div>
</template>
<script>
  import RouterLinkButton from '@/components/RouterLinkButton.vue'

  export default {
    name: 'IndexView',
    components: {
      RouterLinkButton
    }
  }
</script>
<style scoped>
.text_main {
  font-family:'Times New Roman', Times, serif;
  font-size: 32px;
  font-weight: 900;
  color:black;
}
.mainpage-section {
    display: flex;
    flex-direction: column;
    column-gap: 50px;
    align-items: center;
    justify-content: space-between;
  }

  .mainpage-text {
    margin-right: 140px;
  }

  .text-section-head{
    font-family: Neucha;
    font-size: 100px;
    font-weight: 400;
    line-height: 110px;
    letter-spacing: 0em;
    text-align: left;
    color:#000000;
  }
  .text-section {
    max-height: 354px;
    max-width: 961px;
    font-family: Neucha;
    font-size: 50px;
    font-weight: 400;
    line-height: 55px;
    letter-spacing: 0em;
    text-align: left;
    color:#000000;

  }

  .mainpage-link-container {
    display:flex;
    margin-top: 100px;
    flex-direction: column;
    justify-content: space-between;
    grid-gap: 40px;
    a {
      text-decoration: none;
    }
  }

</style>