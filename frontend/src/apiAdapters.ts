export const API_ROOT = 'http://127.0.0.1:8000'
export let token: string

export async function login (username: string, password: string) {
  const formData = new FormData()
  formData.append('username', username)
  formData.append('password', password)

  const r = await fetch(API_ROOT + '/rest-auth/login/', {
    method: 'POST',
    body: formData
  })
  const json = await r.json()

  document.cookie = `token=${json.key}`

  return (token = json.key)
}

export async function register (username: string, email: string, password1: string, password2: string) {
  const data = { username, email, password1, password2 }
  const formData = new FormData()

  for (const key in data) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-ignore
    // @ts-ignore
    formData.append(key, data[key])
  }

  const r = await fetch(API_ROOT + '/rest-auth/registration/', {
    method: 'POST',
    body: formData
  })

  if (r.status === 500) { // особенность rest-auth
    alert('Пользователь успешно зарегистрирован')
    document.location.href = '/'
  }
}
