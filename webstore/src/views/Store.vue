
<template>
  <div class="ContentStore">
    <h1 >Аквариумные рыбки</h1>
    <div class="Store">
      <div class="row">
          <div class= "col-sm-2"v-for="fish in fishes" :key="fish.id">
            <div class="card">
              <img :src="'/src/assets/Fish/'+fish.image" class="card-img-top" :alt="fish.image">
              <div class="card-body">
                    <div class="card-body">
                      <h5 class="card-title">{{ fish.name }}</h5>
                      <p class="card-text">Стоимость: {{ fish.price }} руб.</p>
                      <button class="btn btn-primary" @click="addToCart(fish.id)">В корзину</button>
                      <button class="btn btn-primary" @click="viewFishDetails(fish.id)">Подробнее</button>
                    </div>
                <div class="row justify-content-end"></div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { mapActions } from 'vuex'; // Если вы используете Vuex

export default {
  name: 'FishStore',
  data() {
    return {
      fishes: []
    };
  },
  computed: {
    numberOfFishes() {
      return this.fishes.length;
    }
  },
  mounted() {
    this.fetchFishes();
  },
  methods: {
    ...mapActions({
    addNotification: 'addNotification'
  }),
    fetchFishes() {
      axios.get('http://127.0.0.1:8000/fish/all')
        .then(response => {
          this.fishes = response.data.map(fish => ({
            id: fish.id,
            name: fish.name,
            price: fish.price,
            image: fish.image_url
            
          }));
        })
        
        .catch(error => {
          console.error('Error fetching fishes:', error);
        });
    },
    addToCart(tmp_id) {
  axios.post(`http://127.0.0.1:8000/cart/${tmp_id}`)
    .then(response => {
      // Вызываем мутацию для добавления уведомления в хранилище Vuex
      this.addNotification({
        title: 'Success',
        message: 'Added to cart',
        type: 'success'
      });
    })
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
.ContentStore{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
 .store{
  margin-top: 40px;
  justify-content: space-between;
  }
 .card {
  /* margin-top: 10px; */
  margin-left: auto;
  margin:20px;
  display: flex;
  justify-content:space-between;
  align-items: center;
  background-color: rgb(255, 228, 196);
  border-color: rgb(126, 114, 100);
  border:5px;

  width: 150px;
  height: 300px;

}
.card-title{
  font-family:'Times New Roman', Times, serif;
  font-weight: 1000;
  font-size: 14px;
}
.card-text{
  font-family:'Times New Roman', Times, serif;
  font-weight: 500;
  font-size: 14px;
}
.card-img-top {
  border: 2px solid black; 
}

.btn-primary{
  margin-left: 5px;
  margin-right: 5px;
  font-family:'Times New Roman', Times, serif;
  font-weight: 400;
  font-size: 14px;
  text-decoration: none;
  color: rgb(0, 0, 0);
  background-color: rgb(67, 124, 37);
  border-radius: 7px;
  width:125px;
  height:20px;
  padding: 0px 0px 0px 0px;
  text-align: center;
}

</style> 