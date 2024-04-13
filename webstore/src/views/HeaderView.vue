
<template>
  <header class="header">
    <div class="logotype-section"> 
      <div class="logotype-image-section">
        <img src="../assets/mainlogo.png" @click="goHome" alt="logotype" class="logotype-image">
        <img src="../assets/goBack.png" @click="goBack" alt="goback" class="return-image">
       </div>
      <span class="header-text">FishShop64</span> 
    </div>
    <div class="navigation-section">
        <router-link to="/"><span class="navigation-text">Главная</span></router-link>
        <router-link to="/about"><span class="navigation-text">О нас</span></router-link>
        <img src="../assets/cart.png" @click="goCart" alt="cart" class="cart-image">
        <!-- <button type="button" class="btn" @click="showModal">Open Modal!</button>
        <modal v-show="isModalVisible" @close="closeModal"/> -->
    </div>
  </header>
</template>
<script>
  import modal from '@/components/ModalMenu.vue';

  export default {
    name: 'app',
    components: {
      modal,
    },
    data () {
      return {
        isModalVisible: false,
      };
    },
    methods: {
      goHome() {
      this.$router.push('/'); // Перейти на страницу корзины
      },
      goCart() {
      this.$router.push('/cart'); // Перейти на страницу домой
      },
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
      goBack() {
      this.$router.go(-1); // Перейти на предыдущую страницу
    }
    },
  };
</script>



<style>
.header {
  top: 0px;
  width: 100%;
  height: 100px;
  
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-shrink: 1;
  background-color: rgb(165, 176, 159);
}

.cart-button{
  cursor:pointer;
}

.header-text{
  position:relative;
  left:50px;
  top:50%;
  font-size: 48px;
  font-style: Bold;
  text-align: right;
  font-family: Cormorant Infant;
  font-weight: 1000;
}

.logotype-section {
            display: flex;
            flex-direction: row;
            align-items: center;
            .logotype-image-section {
              align-items: center;
              display:flex;
              flex-direction: column;
              .logotype-image {
                width: 100px;
                height: 70px;
                margin-right: 15px;
                margin-bottom:5px;
                margin-top: 5px;
                cursor:pointer;
            }
            .return-image{
              width: 60px;
              height: 20px;
              margin-right: 15px;
              margin-left:10px;
              cursor:pointer;
              background-color:rgb(135, 142, 131);
              border: 2px solid black; /* Рамка */
              border-radius: 10px; /* Скругленные углы */
            }
            }
            
            .logotype-title {
                font-family: "Handlee";
                font-weight: 400;
                font-size: 70px;
            }
        }
.navigation-section {
  position:relative;
  margin-right: 20px;
  margin-top:10px;
  display: flex;
  flex-direction: column;
  align-items:center;
  justify-content: space-between;
}
.cart-image{
 width: 50px;
 height:30px; 
 margin-top: 10px;
 cursor:pointer;
  background-color:rgb(135, 142, 131);
  border: 2px solid black; /* Рамка */
  border-radius: 10px; /* Скругленные углы */
}
.navigation-text{
  font-size: 16px;
  text-align: right;
  text-decoration-line: none;
  font-family: Cormorant Infant;
  font-weight: 700;
}



</style>