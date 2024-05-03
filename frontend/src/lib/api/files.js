import {makeRequest} from "$lib/api/base.js";

export async function getFiles(accessToken) {
    return await makeRequest("/files", {
        headers: {
            'Authorization': `Bearer ` + accessToken,
        }
    })
}

export async function getFile(fileId, accessToken) {
    return await makeRequest("/files/" + fileId, {
        headers: {
            'Authorization': `Bearer ` + accessToken,
        }
    })
}

export async function uploadFile(file, accessToken) {
    const formData = new FormData();
    formData.append("file", file);

    return await fetch("http://localhost:8080/files", {
        method: "POST",
        body: formData,
        headers: {
            'Authorization': 'Bearer ' + accessToken
        }
    });
}

export async function deleteFile(fileId, accessToken) {
    return await fetch("http://localhost:8080/files/" + fileId, {
        method: "DELETE",
        headers: {
            'Authorization': `Bearer ` + accessToken,
        }
    })
}