
<template>
<footer class ="footer-line"></footer>
<footer class="footer-group">
<div class="footer-names">
  <span class="footer-text1">
  <span> © MAX_FIRSOV CO. 2023</span>
</span>
</div>

<a href="mailto:fishshopsupport2024@gmail.com" 
class="footer-contacts">fishshopsupport2024@gmail.com</a>
</footer>
</template>
<style scoped>
.footer-group {
    width: 100%;
    height: 45px;
    flex: 0 0 auto;
    display: flex;
    position: relative;
    align-items: flex-start;
    justify-content: space-between;
    background-color: rgb(165, 176, 159)
  }

  .footer-names{
  position: relative;
  align-items: flex-start;
  display: flex;
  min-width:400px;
  bottom:5px;
  }
  .footer-line {
    width: 100%;
    height: 1px;
    color: rgba(0, 0, 0, 1);
    position: relative;
    background-color: black;
  }
  .footer-logo{
    position: relative;
  }
  .footer-text1 {
    margin-top: 10px;
    color: rgba(0, 0, 0, 1);
    height: auto;
    position: relative;
    margin-left: 10px;
    font-size: 16px;
    font-style: Bold;
    font-family: 'Times New Roman', Times, serif;
    font-weight: 700;
    line-height: normal;
    font-stretch: normal;
    text-decoration:none;
    margin-bottom: 5px;
  }
  .footer-contacts {
    color: rgba(0, 0, 0, 1);
    height: auto;
    position: relative;
    /* margin-top: 10px; */
    font-size: 20px;
    font-style: Bold;
    text-align: right;
    font-family:'Times New Roman', Times, serif;
    font-weight: 500;
    line-height: normal;
    font-stretch: normal;
    text-decoration: none;
  }
  
  
  .footer-name-logo {
    margin-top: 5px;
    width: 227px;
    height: 40px;
    display: flex;
    position: relative;
    align-items: flex-start;
    flex-shrink: 1;
  }
  
</style>