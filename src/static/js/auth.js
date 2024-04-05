async function login(username, password) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    return await fetch('/auth/login', {
        method: 'POST',
        body: formData
    });
}

async function checkToken() {
    const storedAccessToken = localStorage.getItem('accessToken');
    
    if (storedAccessToken) {
        window.location.href = '/home';
        return;
    }
}
