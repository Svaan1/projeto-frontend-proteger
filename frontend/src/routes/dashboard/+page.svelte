<script>
    import {currentView} from "../../stores.js";

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
