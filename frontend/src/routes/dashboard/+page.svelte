<script>
    import {currentView} from "../../stores.js";

</script>

{#if $currentView === "graphs"}
    graphs
{:else if $currentView === "files"}
    files
{:else if $currentView === "users"}
    users
{/if}