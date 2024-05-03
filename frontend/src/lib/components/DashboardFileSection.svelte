<script>
    import {uploadFile} from "$lib/api/files.js";

    export let data;
    import { Button } from "$lib/components/ui/button" 
    import DashboardFileTable from "./DashboardFileTable.svelte";

    async function handleUploadFile() {
        const fileInput = document.getElementById("fileInput");
        const file = fileInput.files[0];

        if (!file) {
            alert("Please select a file to upload");
            return;
        }

        let response;
        try{
            response = await uploadFile(file, data.accessToken);
        } catch (error) {
            console.log(error);
        }

        if (response.status === 201) {
            fileInput.value = "";
            location.reload();
        }
        else {
            alert("Ocorreu um erro!"); // usar o Alert do shadcn eventualmente
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
    
    #fileInput, .uploadButton {
        margin: 20px;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>


