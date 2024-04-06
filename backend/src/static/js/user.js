// Helper functions
async function safeFetch(endpoint, options) {
    const response = await fetch(endpoint, options);

    if (response.status == 401) {
        removeToken();
        return
    }

    return response;
}

function removeToken() {
    localStorage.removeItem('accessToken')
    window.location.href = '/login'
}

// Api Calls

async function fetchUser() {
    const accessToken = localStorage.getItem('accessToken');
    
    const response = await safeFetch('/user', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json'
        }
    })

    await response.json()
}

async function uploadFile(file) {
    const accessToken = localStorage.getItem('accessToken');

    const formData = new FormData();
    formData.append('file', file);

    const response = await safeFetch('/files',{
        method: 'POST',
        body: formData,
        headers: {
            'Authorization': `Bearer ${accessToken}`,
        }
    });

    return response
}