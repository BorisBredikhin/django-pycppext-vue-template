import { createStore } from 'vuex'

export const LOGIN = 'login'
export const LOGOUT = 'logout'

export default createStore({
  state: {
    loggedIn: false,
    token: null as (string | null)
  },
  mutations: {
    [LOGIN] (state, payload: string) {
      state.loggedIn = true
      state.token = payload
    },
    [LOGOUT] (state) {
      state.token = null
      state.loggedIn = false
    }
  },
  actions: {
  },
  modules: {
  }
})
