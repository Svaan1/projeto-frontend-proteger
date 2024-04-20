<script>
    import {currentView} from "../../stores.js";

    import DashboardLayout from "$lib/components/DashboardLayout.svelte";
</script>

<DashboardLayout>
    {#if $currentView === "graphs"}
        graphs
    {:else if $currentView === "files"}
        files
    {:else if $currentView === "users"}
        users
    {/if}
</DashboardLayout>
