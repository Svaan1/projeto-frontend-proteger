<script>
    import * as Table from "$lib/components/ui/table";

    import { Download, Trash2 } from 'lucide-svelte'
    import { goto } from "$app/navigation";

    async function handleGetFile(fileId) {
        await goto("/dashboard/files/" + fileId);
    }

    export let data;
</script>

<Table.Root>
    <Table.Caption>Arquivos cadastrados</Table.Caption>
    <Table.Header>
      <Table.Row>
        <Table.Head>Nome do Arquivo</Table.Head>
            <Table.Head>Data</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each data as data (data.id)}
        <Table.Row>
            <Table.Cell>{data.filename}</Table.Cell>
            <Table.Cell>{data.datetime}</Table.Cell>
            <Table.Cell>
                <button
                        on:click={() => {handleGetFile(data.id)}}
                        class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                >
                    <Download size="18"/>
                </button>
            </Table.Cell>
            <Table.Cell>
                <button
                        on:click={() => {}}
                        class="flex h-9 w-9 items-center justify-center rounded-lg text-red-500 transition-colors hover:text-red-700 md:h-8 md:w-8"
                >
                    <Trash2 size="18"/>
                </button>
            </Table.Cell>
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>