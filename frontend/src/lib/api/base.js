import { env } from '$env/dynamic/public'

const backendHost = env.BACKEND_HOST
const backendPort = env.BACKEND_PORT

const backendUrl = `${backendHost}:${backendPort}`

export async function makeRequest (endpoint, options) {
  return await fetch(backendUrl + endpoint, options)
}
