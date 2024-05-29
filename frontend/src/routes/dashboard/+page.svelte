<script>
    import {onMount} from "svelte";
    import {writable} from "svelte/store";

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

    let storedView;
    let currentView;
    onMount(async () => {
        storedView = localStorage.getItem("currentView");

        if (storedView) {
            currentView = writable(storedView);
        } else {
            currentView = writable("graphs")
        }
    })

    export let data;
</script>

<DashboardLayout>
    {#if $currentView === "graphs"}
        <DashboardMap/>
    {:else if $currentView === "files"}
        <DashboardFileSection data={data} />
    {:else if $currentView === "users"}
        users
    {:else if $currentView === "togglelights"}
    <!-- -->
    {:else if $currentView === "logout"}
    <!-- -->
    {/if}
</DashboardLayout>