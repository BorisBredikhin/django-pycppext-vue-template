<template>
<div>
  <h1>Регистрация</h1>
  <form>
    <label>Логин: <input id="login"></label>
    <br>
    <label>E-mail: <input id="email" type="email"></label>
    <br>
    <label>Пароль: <input type="password" id="password"></label>
    <br>
    <label>Повторите пароль: <input type="password" id="password2"></label>
  </form>
  <button @click="register">Зарегистрироваться</button>
</div>
</template>

<script lang="ts">
import { register as r } from '@/apiAdapters'
import { getById } from '@/utils'

export default {
  name: 'Register',
  methods: {
    login () {
      r(
        getById<HTMLInputElement>('login').value,
        getById<HTMLInputElement>('email').value,
        getById<HTMLInputElement>('password').value,
        getById<HTMLInputElement>('password2').value
      )
    }
  }
}
</script>

<style scoped>

</style>
