<script>
    import logoUnifeso from "$lib/assets/unifeso.png"

    export let form;
</script>

{#if form?.success === false}
    {form?.message}
{/if}


<div class="container">
    <div class="signup">
        <form method="POST">
            <img src={logoUnifeso} alt="Logo da Unifeso">
            <h1>Registro</h1>
            <p>Já tem conta? Você pode <a href="/login">logar aqui</a>.</p>
            <input type="text" id="username" name="username" placeholder="Usuário" required="required" title="Coloque o seu nome de usuário">
            <input type="email" id="email" name="email" placeholder="Email" required="required" title="Coloque o seu email">
            <input type="password" id="password" name="password" placeholder="Senha" required="required" title="Coloque uma senha">
            <input type="password" id="passwordConfirm" name="passwordConfirm" placeholder="Confirmar Senha" required="required" title="Confirme a sua senha">
            <button type="submit" id="btnSubmit">Confirmar</button>
        </form>
    </div>
</div>

<style>
    .container {
        font-family: 'Roboto', sans-serif;

        margin: 0;
        padding: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        background-size: cover;
        justify-content: center;
    }

    img {
        width: 80px;
        position: absolute;
    }

    .signup {
        padding: 20px;
        margin: 0 auto;
        max-width: 80vw;
        overflow: hidden;
        min-width: 250px;
        border: 1px solid #ccc;
        background-color: whitesmoke;
    }


    form {
        display: flex;
        align-items: center;
        flex-direction: column;
    }

    .signup form h1 {
        cursor: default;
        margin-top: 80px;
        margin-bottom: 0;
    }

    .signup form p{
        cursor: default;
    }

    input[type="text"],
    input[type="email"],
    input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        box-sizing: border-box;
        border: 1px solid #ccc;
    }

    input[type="text"]:focus,
    input[type="email"]:focus,
    input[type="password"]:focus{
        outline: 1px solid black;
    }

    button {
        width: 100%;
        border: none;
        height: 40px;
        outline: none;
        font-size: 1em;
        display: block;
        cursor: pointer;
        font-weight: 700;
        color: #ffffff;
        margin: 10px auto;
        background: #000000;
        justify-content: center;
        transition: background 0.5s ease, box-shadow 0.5s ease;
    }

    button:hover {
        box-shadow: 0 0 10px rgb(56,56,56);
    }

    p{
        margin-top: 5px;
    }

    p a {
        color: rgb(128, 128, 128);
        text-align: center;
        margin-top: 10px;
        text-decoration: underline;
    }

    a:hover {
        color: rgb(56, 56, 56);
    }
</style>