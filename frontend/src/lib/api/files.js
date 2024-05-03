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