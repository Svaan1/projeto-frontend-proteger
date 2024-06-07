import { getFile } from '$lib/api/files.js'

export async function GET ({ cookies, params }) {
  const fileId = params.slug
  const accessToken = cookies.get('accessToken')

  return await getFile(fileId, accessToken)
}
