<script>
  import {goto} from "$app/navigation";
  import logoImage from "$lib/assets/unifeso.png";

  export let form;
</script>

{#if form?.success === false}
  {form?.message}
{/if}

<div class="container">
  <div class="login">
    <form method="POST" id="loginForm">
      <img src={logoImage} title="Unifeso" alt="Logo da Unifeso" />
      <h1>Login</h1>
      <p>Faça o login na sua conta.</p>
      <label for="chk" aria-hidden="true">Login</label>
      <input
        type="text"
        id="username"
        name="username"
        placeholder="Usuário"
        required
      />
      <input
        type="password"
        id="password"
        name="password"
        placeholder="Senha"
        required
      />
      <button type="submit" id="btnSubmit" onsubmit="return false;"
        >Login</button
      >
      <p class="resetPswd">
        Esqueceu a senha? <a href="#">Clique aqui para resetar</a>.
      </p>
      <button class="registerBtn" type="button" on:click={() => goto("/register")}>Registrar</button>
    </form>
  </div>
</div>

<style>
  .container {
    font-family: "Roboto", sans-serif;

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

  .login {
    padding: 20px;
    margin: 0 auto;
    max-width: 80vw;
    min-width: 250px;
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: whitesmoke;
  }

  form {
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .login form h1 {
    cursor: default;
    margin-top: 80px;
    margin-bottom: 0;
  }

  .login form p {
    cursor: default;
  }

  label {
    display: none;
  }

  input[type="text"],
  input[type="password"] {
    width: 100%;
    margin-bottom: 15px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }

  input[type="text"]:focus,
  input[type="password"]:focus {
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
    transition:
      background 0.5s ease,
      box-shadow 0.5s ease;
  }

  button:hover {
    box-shadow: 0 0 10px rgb(56, 56, 56);
  }

  p {
    margin-top: 5px;
  }

  p a {
    color: rgb(128, 128, 128);
    margin-top: 10px;
    text-align: center;
    text-decoration: none;
  }

  a:hover {
    color: rgb(56, 56, 56);
    text-decoration: underline;
  }

  .registerBtn {
    color: black;
    background: transparent;
    border: 1px solid rgba(0, 0, 0, 0.8);
  }

  .registerBtn:hover {
    background: transparent;
  }

  .resetPswd {
    font-size: 15px;
    margin-bottom: 0;
  }
</style>
