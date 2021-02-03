export const API_ROOT = 'http://127.0.0.1:8000'

export function register (login: string, password: string) {
  fetch(API_ROOT + '/auth/register', {
    method: 'post',
    body: JSON.stringify({ login, password }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
}
