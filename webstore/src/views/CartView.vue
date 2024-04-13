<template>
  <div>
    <h1>Корзина</h1>
    <div v-if="cartItems.length === 0">
      <p>Корзина пуста</p>
    </div>
    <div v-else>
      <div class="card-container">
        <div class="row" v-for="item in cartItems" :key="item.id">
          <div class="col-md-12">
            <div class="card">
              <p class="card-name" @click="viewFishDetails(item.fish.id)">{{ item.fish.name }}</p> 
              <p class="card-price">Цена: {{ item.fish.price }} руб.</p>
              <button @click="removeFromCart(item)" class="btn card-delete">Удалить</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-12">
          <p>Итого: {{ totalPrice }} руб.</p>
          <button @click="checkout" class="btn btn-primary">Оформить заказ</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Cart',
  data() {
    return {
      cartItems: [] // Список товаров в корзине
    };
  },
  computed: {
    totalPrice() {
      // Вычисляем общую стоимость товаров в корзине
      return this.cartItems.reduce((total, item) => total + item.fish.price, 0);
    }
  },
  mounted() {
    // Загрузка данных из таблицы cart
    this.fetchCartItems();
  },
  methods: {
    async fetchCartItems() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/cart/all');
        this.cartItems = response.data;
        // Загрузка данных о рыбе из таблицы Fish для каждого товара в корзине
        await this.fetchFishForCartItems();
      } catch (error) {
        console.error('Error fetching cart items:', error);
      }
    },
    async fetchFishForCartItems() {
      for (const item of this.cartItems) {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/fish/${item.fishid}`);
          item.fish = response.data;
        } catch (error) {
          console.error(`Error fetching fish with ID ${item.fishid} for cart item:`, error);
        }
      }
    },
    removeFromCart(item) {
      // Удаление товара из корзины
      const response = axios.delete(`http://127.0.0.1:8000/cart/${item.id}`);
      const index = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
      if (index !== -1) {
        this.cartItems.splice(index, 1);
      }
    },
    checkout() {
      // Оформление заказа
      this.$router.push('/order'); // Перейти на страницу домой
      // Здесь можно выполнить дополнительные действия, такие как отправка данных на сервер и т.д.
    },
    viewFishDetails(fishId) {
    // Проверяем, что fishId не пустой
    if (!fishId) {
      console.error('Missing required param "id"');
      return;
    }
    
    // Переход на страницу с деталями о рыбе
    this.$router.push({ name: 'FishDetails', params: { id: fishId } });
  }
  }
};
</script>

<style>
.card-container{
  width:100%;
  display:flex;
  flex-direction: column;
  justify-content: flex-start;
}
.card{
  height: 30px;
  width:500px;
  margin:10px;
  display:flex;
  flex-direction:row;
  justify-content: space-between;
  background-color: rgb(224, 224, 224);
}
.card-name{
  width:200px;
  margin-left: 5px;
  font-family:'Times New Roman', Times, serif;
  font-weight: 1000;
  font-size: 16px;
  text-align:left;
  cursor: pointer;
}
.card-price{
  width:200px;
  margin-left: 5px;
  font-family:'Times New Roman', Times, serif;
  font-weight: 800;
  font-size: 16px;
  text-align: left;
}
.btn-delete{
  width:100px;
  font-family:'Times New Roman', Times, serif;
  font-weight: 1000;
  font-size: 16px;
}
/* Ваши стили для корзины могут быть добавлены здесь */
</style>
