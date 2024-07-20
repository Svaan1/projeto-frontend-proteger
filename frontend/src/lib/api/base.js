import { env } from '$env/dynamic/public'

const backendHost = env.BACKEND_HOST
const backendPort = env.BACKEND_PORT

const backendUrl = `${backendHost}:${backendPort}`

export async function makeRequest (endpoint, options) {
  options = {
    ...options,
    headers: {
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*',
      ...options.headers
    }
  }

  return await fetch(backendUrl + endpoint, options)
}
