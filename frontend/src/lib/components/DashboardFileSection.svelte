<script>
    export let data;

    async function uploadFile() {
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

        const responseData = await response.json();

        alert(JSON.stringify(responseData));

        // TODO: stylize error and success message (if 201 success message then remove file from input)
        // TODO: also update files list if successful
    }
</script>

<div id="fileUpload">
    <input type="file" name="file" id="fileInput">
    <button class="btn btn-blue" on:click={uploadFile}>inhtml</button>
</div>

<div class="fileList">
    {#each data.files as file (file.id)}
        <div class="file">
            {file.filename}
            {file.datetime}
        </div>
    {/each}
</div>
