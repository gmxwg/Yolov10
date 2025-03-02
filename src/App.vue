<template>
  <div id="app">
    <h1>Login</h1>
    <input v-model="username" placeholder="Username">
    <input v-model="password" type="password" placeholder="Password">
    <button @click="login">Login</button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const message = ref('');

const login = async () => {
  try {
    const response = await fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: username.value, password: password.value })
    });
    const data = await response.json();
    message.value = data.message;
  } catch (error) {
    console.error('Error logging in:', error);
  }
};
</script>

<style scoped>
/* 可添加样式 */
</style>