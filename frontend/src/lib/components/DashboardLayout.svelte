<script>
    import LineChart from "lucide-svelte/icons/line-chart";
    import Upload from "lucide-svelte/icons/upload";
    import { LogOut, Sun, Moon } from 'lucide-svelte';

    import logo from "$lib/assets/unifeso-black.ico"

    import * as Tooltip from "$lib/components/ui/tooltip";
    import { Separator } from "$lib/components/ui/separator"

    export let currentView;

    function setView(view) {
        currentView.set(view)
        localStorage.setItem("currentView", view);
    }

    let isSunVisible = true;
    function toggleIcon() {
        isSunVisible = !isSunVisible;
        visible = !visible;
    }
</script>

<div class="unselectable flex min-h-screen w-full flex-col bg-muted/40 caret-transparent">
    <aside class="fixed inset-y-0 left-0 z-10 hidden w-24 flex-col border-r bg-background sm:flex">
        <nav class="flex flex-col items-center gap-4 px-2 py-4">
            <a
                    href="/  "
                    class="group flex h-16 w-16 items-center justify-center gap-2 rounded-full text-lg font-semibold text-primary-foreground md:text-base"
            >
                <img src={logo} class="cursor-help" alt="Logo da Unifeso">
            </a>
            <Separator class="my-4" />
            <Tooltip.Root>
                <Tooltip.Trigger asChild let:builder>
                    <button 
                            on:click={() => setView("graphs")}
                            class:active={$currentView === 'graphs'}
                            class="flex items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            use:builder.action
                            {...builder}
                    >
                        <LineChart class="h-5 w-5" />
                        <span class="sr-only">Dashboard</span>
                    </button>
                </Tooltip.Trigger>
                <Tooltip.Content side="right">Dashboard</Tooltip.Content>
            </Tooltip.Root>
            <Tooltip.Root>
                <Tooltip.Trigger asChild let:builder>
                    <button
                            on:click={() => setView("files")}
                            class:active={$currentView === 'files'}
                            class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            use:builder.action
                            {...builder}
                    >
                        <Upload class="h-5 w-5" />
                        <span class="sr-only">Arquivos</span>
                    </button>
                </Tooltip.Trigger>
                <Tooltip.Content side="right">Arquivos</Tooltip.Content>
            </Tooltip.Root>
        </nav>
        <nav class="mt-auto flex flex-col items-center gap-4 px-2 py-4">
            <Tooltip.Root>
                <Tooltip.Trigger asChild let:builder>
                    <button
                        class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                        use:builder.action
                        {...builder}
                    >
                    <div class="icon-toggle">
                        <button class="icons" on:click={toggleIcon}>
                            {#if isSunVisible}
                                <Sun size={32} strokeWidth={1.5} />
                            {:else}
                                <Moon size={32} strokeWidth={1.5} />
                            {/if}
                        </button>
                    </div>
                        <span class="sr-only">togglelights</span>
                    </button>
                </Tooltip.Trigger>
                <Tooltip.Content side="right">Mudar tema</Tooltip.Content>
            </Tooltip.Root>
            <Tooltip.Root>
                <Tooltip.Trigger asChild let:builder>
                    <form method="POST" action="?/logout" class="icon-leave">
                        <button
                            class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            use:builder.action
                            {...builder}
                        >
                        <LogOut size={48} strokeWidth={1.5} />
                            <span class="sr-only">logout</span>
                        </button>
                    </form>
                </Tooltip.Trigger>
                <Tooltip.Content side="right">Sair</Tooltip.Content> 
            </Tooltip.Root>
        </nav>
    </aside>
    <main class="flex flex-col h-screen sm:gap-4 sm:py-4 sm:pl-14 justify-center items-center">
        <slot></slot>
    </main>
</div>

<style>
    .unselectable {
        user-select: none;
        -webkit-user-drag: none;
    }
    .active {
        --tw-text-opacity: 1;
        color: hsl(var(--foreground) / var(--tw-text-opacity));
        --tw-bg-opacity: 1;
        background-color: hsl(var(--accent) / var(--tw-bg-opacity));
    }
</style>