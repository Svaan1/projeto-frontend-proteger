<script>
  import logoImage from "$lib/assets/unifeso.png";

  export let form;
</script>

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
      <button type="submit" id="btnSubmit">Login</button>

      <button
        class="registerBtn"
        type="button"
        on:click={() => (window.location.href = "/register")}>Registrar</button
      >
    </form>
    {#if form?.success === false}
      <div class="message-box {form.success ? 'success' : 'error'}">
        {form.message}
      </div>
    {/if}
  </div>
</div>

<!-- styling -->
<style>
  .container {
    font-family: "Montserrat", sans-serif;

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

  form {
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .login {
    padding: 20px;
    max-width: 80vw;
    min-width: 250px;
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: whitesmoke;
  }

  .login form {
    cursor: default;
  }

  .login form h1 {
    font-weight: bold;
    font-size: 2em;
    margin-top: 70px;
  }

  .login form p {
    margin-bottom: 10px;
  }

  label {
    display: none;
  }

  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
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

  .message-box {
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    text-align: center;
    font-weight: bold;
  }

  .message-box.success {
    color: green;
    background-color: #e0ffe0;
    border: 1px solid green;
  }

  .message-box.error {
    color: red;
    background-color: #ffe0e0;
    border: 1px solid red;
  }
</style>
