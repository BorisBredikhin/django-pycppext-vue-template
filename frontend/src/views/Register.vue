<template>
<div>
  <h1>Регистрация</h1>
  <form>
    <label>Логин: <input id="login"></label>
    <br>
    <label>Пароль: <input type="password" id="password"></label>
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
    register () {
      r(getById<HTMLInputElement>('login').value, getById<HTMLInputElement>('password').value)
    }
  }
}
</script>

<style scoped>

</style>
