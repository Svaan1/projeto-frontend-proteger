<script>
    import {onMount} from "svelte";
    import {writable} from "svelte/store";

    import DashboardLayout from "$lib/components/DashboardLayout.svelte";
    import DashboardFileSection from "$lib/components/DashboardFileSection.svelte";
    import DashboardMap from "$lib/components/DashboardMap.svelte";

    let storedView;
    let currentView;

    onMount(async () => {
        storedView = localStorage.getItem("currentView");

        if (storedView) {
            currentView = writable(storedView);
        } else {
            currentView = writable("files")
        }
    });

    export let data;
</script>

<DashboardLayout currentView={currentView}>
    {#if $currentView === "graphs"}
        <DashboardMap/>
    {:else if $currentView === "files"}
        <DashboardFileSection data={data} />
    {/if}
    
</DashboardLayout>

<style>
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
