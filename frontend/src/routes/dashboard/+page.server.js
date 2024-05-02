import {getUser} from "$lib/api/auth.js";
import {redirect} from "@sveltejs/kit";
import {getFiles} from "$lib/api/files.js";

/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
    const accessToken = cookies.get("accessToken");
    if (accessToken) {
        let user;
        let files;
        try {
            user = await getUser(accessToken);
            files = await getFiles(accessToken);
        } catch {
            cookies.delete("accessToken", { path: "/" });
            return
        }

        if (user.ok) {
            const userData = await user.json();
            const filesData = await files.json();
            return { user: userData, files: filesData, accessToken: accessToken}
        }
    }

    cookies.delete("/accessToken", { path: "/" });
    redirect(302, '/login')
}

/** @type {import('./$types').Actions} */
export const actions = {
    logout: async ({ cookies }) => {
        cookies.delete("accessToken", { path: "/" });
    }
};