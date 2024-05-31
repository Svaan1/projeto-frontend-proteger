<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Rokkitt:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

<body class="flex items-center justify-center min-h-screen bg-sky-600">

    <div class="background"></div>
    <div class="overlay"></div>
    <h1 class="absolute inset-0 flex items-center justify-center select-none text-9xl opacity-50 z-10 text-yellow-300">Proteger</h1>
    <button on:click={() => window.location.href = '/login'} id="btnSubmit" type="submit" class="relative z-20 px-6 py-2 mr-4 text-white bg-black rounded-md shadow-lg transition-all duration-300 transform hover:outline-2 hover:scale-105 focus:outline-2 focus:ring-4 ">
        Login
    </button>
    <button on:click={() => window.location.href = '/register'} id="btnSubmit" type="submit" class="relative z-20 px-6 py-2 text-white bg-transparent outline outline-black outline-2 rounded-md shadow-lg transition-all duration-300 transform hover:outline-2 hover:scale-105 focus:outline-2 focus:ring-4 ">
        Registrar
    </button>
</body>
