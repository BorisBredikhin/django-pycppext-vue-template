<template>
<div>
  <h1>Вход</h1>
  <form>
    <label>Логин: <input id="login"></label>
    <br>
    <label>Пароль: <input type="password" id="password"></label>
  </form>
  <button @click="login">Войти</button>
</div>
</template>

<script lang="ts">
import { login as l } from '@/apiAdapters'
import { getById } from '@/utils'

export default {
  name: 'Register',
  methods: {
    login () {
      l(
        getById<HTMLInputElement>('login').value,
        getById<HTMLInputElement>('password').value
      )
    }
  }
}
</script>

<style scoped>

</style>
