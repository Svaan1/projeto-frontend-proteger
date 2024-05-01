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
    import DashboardMap from "$lib/components/DashboardMap.svelte";

    export let data;
</script>

<DashboardLayout>
    {#if $currentView === "graphs"}
        <DashboardMap/>
    {:else if $currentView === "files"}
        <DashboardFileSection data={data} />
    {:else if $currentView === "users"}
        users
    {:else if $currentView === "settings"}

        <div class="icon-leave">
            <LogOut class="h-5 w-5"/>
            <span class="icon-text">
                <p>Sair</p>
            </span>
        </div>

        <div class="icon-toggle">
            <button class="icons" on:click={toggleIcon}>
                {#if isSunVisible && visible}
                    <Sun class="h-5 w-5" />
                {:else}
                    <Moon class="h-5 w-5" />
                {/if}
            </button>
        </div>

        <div class="board">
            <input
                class="new-todo"
                placeholder="what needs to be done?"
                on:keydown={(event) => event.key === 'Enter' && add(event.target)}/>
            <div class="left">
                <h2>todo</h2>
                {#each todos.filter((t) => !t.done) as todo (todo.id)}
                    <label in:receive={{ key: todo.id }} out:send={{ key: todo.id }} animate:flip>
                        <input type="checkbox" bind:checked={todo.done} />
                        {todo.description}
                        <button on:click={() => remove(todo)}>x</button>
                    </label>
                {/each}
            </div>
            <div class="right">
                <h2>done</h2>
                {#each todos.filter((t) => t.done) as todo (todo.id)}
                    <label in:receive={{ key: todo.id }} out:send={{ key: todo.id }} animate:flip>
                        <input type="checkbox" bind:checked={todo.done} />
                        {todo.description}
                        <button on:click={() => remove(todo)}>x</button>
                    </label>
                {/each}
            </div>
        </div>
    {/if}
</DashboardLayout>
<!-- style -->
<style>

    .new-todo {
		font-size: 1.4em;
		width: 100%;
		margin: 2em 0 1em 0;
	}

	.board {
		max-width: 36em;
		margin: 0 auto;
	}

	.left,
	.right {
		float: left;
		width: 50%;
		padding: 0 1em 0 0;
		box-sizing: border-box;
	}

	h2 {
		font-size: 2em;
		font-weight: 200;
		user-select: none;
	}

	label {
		top: 0;
		left: 0;
		display: block;
		font-size: 1em;
		line-height: 1;
		padding: 0.5em;
		margin: 0 auto 0.5em auto;
		border-radius: 2px;
		background-color: #eee;
		user-select: none;
		color: black;
	}

	input {
		margin: 0;
	}

	.right label {
		background-color: rgb(180, 240, 100);
	}

	button {
		float: right;
		height: 1em;
		box-sizing: border-box;
		padding: 0 0.5em;
		line-height: 1;
		background-color: transparent;
		border: none;
		color: rgb(170, 30, 30);
		opacity: 0;
		transition: opacity 0.2s;
	}

	label:hover button {
		opacity: 1;
	}

    .icons{
        color: black;
        opacity: 1;
    }

    .icon-leave,
    .icon-toggle {
        display: flex;
        cursor: pointer;
        position: relative;
        align-items: center;
    }

    .icon-text {
        opacity: 0;
        left: 10px;
        padding: 20px;
        position: absolute;
        pointer-events: none;
    }

    .icon-leave:hover .icon-text {
        opacity: 1;
        cursor: pointer;
        pointer-events: all;
        animation: fadeInText 0.3s ease forwards;
    }

    .icon-leave:hover {
        animation: moveIcon 0.3s ease forwards;
    }

    .icon-leave:not(:hover) .icon-text {
        animation: fadeInText 0.3s ease reverse;
    }

    .icon-leave:not(:hover) {
        animation: moveIconBackward 0.3s ease forwards;
    }

    @keyframes moveIcon {
        from {
            transform: translateX(0);
        }
        to {
            transform: translateX(-10px);
        }
    }

    @keyframes moveIconBackward {
        from {
            transform: translateX(-10px);
        }
        to {
            transform: translateX(0);
        }
    }

    @keyframes fadeInText {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
