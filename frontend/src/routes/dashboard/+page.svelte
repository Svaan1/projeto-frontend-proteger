<script>
    import {currentView} from "../../stores.js";
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
    {:else if $currentView === "togglelights"}
    <!-- -->
    {:else if $currentView === "logout"}
    <!-- -->
    {/if}
</DashboardLayout>