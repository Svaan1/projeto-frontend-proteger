<script>
    import {currentView} from "../../stores.js";
    import { LogOut, Sun, Moon } from 'lucide-svelte';
    import DashboardLayout from "$lib/components/DashboardLayout.svelte";
    import DashboardFileSection from "$lib/components/DashboardFileSection.svelte";
    import DashboardMap from "$lib/components/DashboardMap.svelte";

    let isSunVisible = true;
    let visible = true;
    function toggleIcon() {
        isSunVisible = !isSunVisible;
        visible = !visible;
    }

    export let data;
</script>

<DashboardLayout>
    {#if $currentView === "graphs"}
        <DashboardMap/>
    {:else if $currentView === "files"}
        <DashboardFileSection data={data} />
    <!-- {:else if $currentView === "users"}
        users
    {:else if $currentView === "settings"} -->
    {/if}
    <!-- <form method="POST" action="?/logout" class="icon-leave">
        <button type="submit">
        <LogOut class="h-5 w-5"/>
        </button>
        <span class="icon-text">
            <p>Sair</p>
        </span>
    </form>

    <div class="icon-toggle">
        <button class="icons" on:click={toggleIcon}>
            {#if isSunVisible && visible}
                <Sun class="h-5 w-5" />
            {:else}
                <Moon class="h-5 w-5" />
            {/if}
        </button>
    </div> -->
    
</DashboardLayout>

<!-- style -->
<style>
    /* .icons {
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
    } */

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
