<script>
  export let data;

  import * as Table from "$lib/components/ui/table";

  import { Download, Trash2 } from 'lucide-svelte'
  import { goto } from "$app/navigation";
  import {deleteFile} from "$lib/api/files.js";
  import {writable} from "svelte/store";

  const files = writable(data.files);

  const formatter = new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'America/Sao_Paulo'
});

  function formatDate(dateString) {
      const date = new Date(dateString);

      // por algum motivo (prob por causa do docker) ele ta salvando com datetime de UTC
      // mas com formatação de pt-BR, então eu to subtraindo 3 horas pra ficar o tempo pt-BR de verdade
      date.setHours(date.getHours() - 3);

      return formatter.format(date);
  }

  async function handleGetFile(fileId) {
      await goto("/dashboard/files/" + fileId);
  }

  async function handleDeleteFile(fileId) {
      const response = await deleteFile(fileId, data.accessToken)

      if (response.status === 204) {
          data.files = data.files.filter(file => file.id !== fileId)
          files.update(files => files.filter(file => file.id !== fileId));
      }
  }
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
      {#each $files as file (file.id)}
        <Table.Row>
          <Table.Cell>{file.filename}</Table.Cell>
            <Table.Cell>{formatDate(file.datetime)}</Table.Cell>
            <Table.Cell>
                <button
                        on:click={() => {handleGetFile(file.id)}}
                        class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                >
                    <Download size="18"/>
                </button>
            </Table.Cell>
            <Table.Cell>
                <button
                        on:click={() => {handleDeleteFile(file.id)}}
                        class="flex h-9 w-9 items-center justify-center rounded-lg text-red-500 transition-colors hover:text-red-700 md:h-8 md:w-8"
                >
                    <Trash2 size="18"/>
                </button>
            </Table.Cell>
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>