import { makeRequest } from '$lib/api/base.js'

export async function getUser (accessToken) {
  return await makeRequest('/user', {
    method: 'GET',
    headers: {
      Authorization: `Bearer ` + accessToken
    }
  })
}

export async function login (formData) {
  return await makeRequest('/auth/login', {
    method: 'POST',
    body: formData
  })
}

export async function register (username, email, password) {
  const body = {
    username: username,
    email: email,
    password: password
  }

  return await makeRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify(body),
    headers: {
      'Content-Type': 'application/json'
    }
  })
}
