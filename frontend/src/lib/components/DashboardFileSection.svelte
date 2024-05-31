<script>
    export let data;
    import { toast } from "svelte-sonner";
    import { Button } from "$lib/components/ui/button" 
    import DashboardFileTable from "./DashboardFileTable.svelte";

    let time = new Date();

	$: hours = time.getHours();
	$: minutes = time.getMinutes();
	$: seconds = time.getSeconds();
    
    $: period = hours >= 12 ? 'PM' : 'AM';
    
    // Convert 24-hour time to 12-hour time
    $: displayHours = hours > 12 ? hours - 12 : hours;

    async function uploadFile() {
        const fileInput = document.getElementById("fileInput");
        const file = fileInput.files[0];

        if (!file) {
            toast.warning("Por favor, selecione um arquivo para enviar.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        let response;
        try {
            response = await fetch("http://localhost:8080/files", {
                method: "POST",
                body: formData,
                headers: {
                    'Authorization': 'Bearer ' + data.accessToken
                }
            });
            toast.success("Arquivo enviado com sucesso.", {
                description: `${displayHours}:${minutes}:${seconds} ${period}`,
            });
        } catch (error) {
            toast.error("Ocorreu um erro na hora de enviar, tente novamente.");
        }

        if (response.status === 201) {
            fileInput.value = "";
            location.reload();
        }
        else {
            toast.error("Ocorreu um erro, por favor tente novamente.");
        }
    }
</script>

<div class="container">
    <div id="fileUpload">
        <input type="file" name="file" id="fileInput">
        <Button class="uploadButton" on:click={uploadFile}>Enviar</Button>
    </div>
    <div id="fileTable">
        <DashboardFileTable data={data.files} />
    </div>
</div>

<style>
    #fileUpload {
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 10px;
        border-bottom: 1px solid #ccc;
    }
    
    #fileTable {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        width: 75%;
        height: 75%;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>