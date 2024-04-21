<script>
    import {currentView} from "../../stores.js";
    import { LogOut, Sun, Moon } from 'lucide-svelte';
    import { fade, crossfade } from 'svelte/transition';
    import { quintOut } from 'svelte/easing';
	import { flip } from 'svelte/animate';


    let isSunVisible = true;
    let visible = true;
    function toggleIcon() {
        isSunVisible = !isSunVisible;
        visible = !visible;
    }

	const [send, receive] = crossfade({
		fallback(node, params) {
			const style = getComputedStyle(node);
			const transform = style.transform === 'none' ? '' : style.transform;

			return {
				duration: 600,
				easing: quintOut,
				css: (t) => `
					transform: ${transform} scale(${t});
					opacity: ${t}
				`
			};
		}
	});

	let todos = [ // fill out the todo things
		// { id: 1, done: false, description: 'write some docs' },
		// { id: 2, done: true, description: 'buy some milk' },
	];

	let uid = todos.length + 1;

	function add(input) {
		const todo = {
			id: uid++,
			done: false,
			description: input.value
		};

		todos = [todo, ...todos];
		input.value = '';
	}

	function remove(todo) {
		todos = todos.filter((t) => t !== todo);
	}

    import DashboardLayout from "$lib/components/DashboardLayout.svelte";
    import DashboardFileSection from "$lib/components/DashboardFileSection.svelte";

    export let data;
</script>


<DashboardLayout>
    {#if $currentView === "graphs"}
        graphs
    {:else if $currentView === "files"}
        <DashboardFileSection data={data} />
    {:else if $currentView === "users"}
        users
    {/if}
</DashboardLayout>
