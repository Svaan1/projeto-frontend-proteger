const backendUrl = "http://127.0.0.1:8000"

export async function makeRequest(endpoint, options) {
    return await fetch(backendUrl + endpoint, options)
}

