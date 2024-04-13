<template>
    <div class="modal-backd rop">
      <div class="modal">
        <header class="modal-header">
          <slot name="header">
            <button
              type="button"
              class="btn-close"
              @click="closeMenu"
            >
              x
            </button>
          </slot>
        </header>
        <section class="modal-body">
          <div v-if="cartItems.length === 0">
            Корзина пуста
          </div>
          <ul v-else>
            <li v-for="(item, index) in cartItems" :key="index">
              {{ item.name }} - {{ item.price }} руб. ({{ item.quantity }} шт.)
              <button @click="removeFromCart(index)">Удалить</button>
            </li>
          </ul>
          <div class="total" v-if="cartItems.length > 0">
            Итого: {{ getTotalPrice() }} руб.
          </div>
        </section>
        <footer class="modal-footer">
          <button v-if="cartItems.length > 0" @click="checkout">Оформить заказ</button>
        </footer>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CartModal",
    data() {
      return {
        cartItems: [
          { name: "Рыбка кардинал", price: 100, quantity: 1 },
          { name: "Рыбка гуппи", price: 80, quantity: 2 }
          // Добавьте другие товары по аналогии
        ]
      };
    },
    methods: {
      closeMenu() {
        this.$emit("closeMenu");
      },
      removeFromCart(index) {
        this.cartItems.splice(index, 1);
      },
      getTotalPrice() {
        return this.cartItems.reduce((total, item) => {
          return total + item.price * item.quantity;
        }, 0);
      },
      checkout() {
        // Ваш код для оформления заказа
      }
    }
  };
  </script>
  
  <style>
   .modal-backdrop {
  
    margin-top: 18px;
    margin-left: auto;
    display: flex;
    justify-content: center;
    align-items: center;}
  /* Ваши стили */
   .btn-close{
    font-size: 24px;
    color:brown
   }
  </style>