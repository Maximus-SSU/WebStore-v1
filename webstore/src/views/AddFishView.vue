<template>
    <div>
      <h1>Administrate Fish</h1>
      <form @submit.prevent="addFish">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="newFish.name" required><br>
        <label for="price">Price:</label>
        <input type="number" id="price" v-model.number="newFish.price" required><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" v-model="newFish.image_url" required><br>
        <button type="submit">Add Fish</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newFish: {
          name: '',
          price: 0,
          image_url: ''
        }
      }
    },
    methods: {
      async addFish() {
        try {
          await axios.post('http://localhost:8000/fish', this.newFish);
          alert('Fish added successfully!');
          // Опционально: очищаем форму после добавления рыбы
          this.newFish = {
            name: '',
            price: 0,
            image_url: ''
          };
        } catch (error) {
          console.error('Error adding fish:', error);
          alert('Error adding fish. See console for details.');
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add some styles */
  </style>
  