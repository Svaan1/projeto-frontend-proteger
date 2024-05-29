<script>
    import * as Table from "$lib/components/ui/table";

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
          <Table.Cell>{data.datetime}</Table.Cell> <!-- new Intl.DateTimeFormat('pt-BR').format(data.datetime) -- formatar a data!!! -->
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>