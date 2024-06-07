<script>
    export let data;
    import { toast } from "svelte-sonner";
    import { Button } from "$lib/components/ui/button" 
    import {uploadFile} from "$lib/api/files.js";
    import DashboardFileTable from "./DashboardFileTable.svelte";

    async function handleUploadFile() {
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
            response = await uploadFile(file, data.accessToken);
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
        <Button class="uploadButton" on:click={handleUploadFile}>Enviar</Button>
    </div>
    <div id="fileTable">
        <DashboardFileTable data={data} />
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