<script>
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
        } catch (error) {
            alert("An error occurred during upload. Please try again.");
        }

        if (response.status === 201) {
            fileInput.value = "";
            location.reload();
            // não consegui trocar a currentView para files, mas deveria ser feito
        }
        else {
            alert("Ocorreu um erro!"); // usar o Alert do shadcn eventualmente
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
    
    #fileInput, .uploadButton {
        margin: 20px;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>


