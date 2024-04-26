import {redirect} from "@sveltejs/kit";

import {getUser, login} from "$lib/api/auth.js";

/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
    const accessToken = cookies.get("accessToken");

    if (accessToken) {
        let user;
        try {
            user = await getUser(accessToken);
        } catch {
            cookies.delete("/accessToken", { path: "/" });
            return
        }

        if (user.ok) {
            redirect(302, "/dashboard");
            return
        }

        cookies.delete("/accessToken", { path: "/" });
    }
}

/** @type {import('./$types').Actions} */
export const actions = {
    default: async ({ cookies, request }) => {
        const formData = await request.formData();

        let response;
        try {
            response = await login(formData);
        } catch {
            return { success: false, message: "Serviço Indisponível" }
        }

        const data = await response.json();

        if (response.ok) {
            cookies.set("accessToken", data.access_token, {
                httpOnly: true,
                sameSite: true,
                path: "/"
            })
            redirect(302, "/dashboard")
            return
        }

        return { success: false, message: data.detail, }

    }
};