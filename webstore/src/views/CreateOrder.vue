<template>
    <h1>ОФОРМЛЕНИЕ ЗАКАЗА</h1>
    <div>
      <p> Введите номер телефона:</p>
      <FormInput name="phone" form="phoneForm" placeholder="Введите номер телефона" />
    </div>
    <div>
      <p>Введите имя:</p>
      <FormInput name="name" form="nameForm" placeholder="Введите имя" />
    </div>
    <p> Итого: {{ totalPrice }} руб.</p>
    <button class="btn btn-primary" @click="DoOrder">ОФОРМИТЬ ЗАКАЗ</button>
  </template>
  
  
<script>
import FormInput from '@/components/FormInput.vue';
import axios from 'axios';

export default {
  name: 'Cart',
  data() {
    return {
      cartItems: [] // Список товаров в корзине
    };
  },
  components: {
    FormInput,
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
    DoOrder() {
        // Оформление заказа
        this.$router.push('/order/done'); // Перейти на страницу домой
        // Здесь можно выполнить дополнительные действия, такие как отправка данных на сервер и т.д.
    }
  }
};
</script>