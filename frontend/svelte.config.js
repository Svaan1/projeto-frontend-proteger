import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";
import adapter from "@sveltejs/adapter-node";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    csrf: {
      checkOrigin: false
    },
    env: {
      dir: "../"
    }
  },

  alias: {
    "@/*": "./src/lib/*",
    $images: "src/lib/assets/images",
  },

  preprocess: [vitePreprocess({})],
};

export default config;
