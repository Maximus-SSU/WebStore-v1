<template>
    <div class="FishDetails" v-if="fish"> <!-- Добавляем условие v-if -->
      <h1>{{ fish.name }}</h1>
      <img :src="'/src/assets/Fish/'+ fish.image" class="card-img-top" :alt="fish.image">
      <p>Цена:{{ fish.price }} руб.</p>
      <button class="btn btn-primary" @click="addToCart(fish)">В корзину</button>
      <p>Описание: {{ fish.desc }}</p>
    </div>
    <div v-else> <!-- Добавляем альтернативное содержимое, если fish равен null -->
      Loading...
    </div>
</template>
  <script>

import axios from 'axios';
export default {
  name: 'FishDetails',
  data() {
    return {
      tempID: null,
      fish: null // Изменение на fish, чтобы содержать информацию только о одной рыбе
    };
  },
  created() {
    this.tempID = this.$route.params.id;
  },
  mounted() {
    this.fetchFish(); // Изменение на fetchFish
  },
  methods: {
    fetchFish() { // Изменение названия метода на fetchFish
      axios.get(`http://127.0.0.1:8000/fish/${this.$route.params.id}`)
        .then(response => {
          const fishData = response.data;
          this.fish = {
            id: fishData.id,
            name: fishData.name,
            price: fishData.price,
            image: fishData.image_url,
            desc: fishData.desc // Добавляем описание
            // Другие свойства рыбы, если есть
          };
        })
        .catch(error => {
          console.error('Error fetching fish:', error);
        });
    },
    
  }
};


</script>

  
  <style scoped>
  
.card-img-top {
  border: 2px solid black; 
  max-width: 600px;
  max-height: 400px;
}

.btn-primary{
  height: 40px;
  width:200px;
  font-family:'Times New Roman', Times, serif;
  font-weight: 1000;
  font-size: 20px;
  text-decoration: none;
  text-align: center;
  color: rgb(0, 0, 0);
  background-color: rgb(67, 124, 37);
  border-radius: 7px;
  
}
  </style>
  