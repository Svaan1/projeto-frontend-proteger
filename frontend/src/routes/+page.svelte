<!-- <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Rokkitt:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet"> -->

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Proteger Teresópolis</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
</head>

<body class="flex items-center justify-center min-h-screen bg-white">
    <main>
        <ol>
            <li>
                <button on:click={() => window.location.href = 'https://www.unifeso.edu.br/'} class="absolute top-5 inset-x-0 z-20 px-4 py-2 text-black text-4xl">Unifeso</button>
            </li>
            <li>
                <div>
                    <div class="flex justify-center items-center">
                        <h2 class="font-thin select-none z-99 text-4xl text-black subpixel-antialiased tracking-widest">T E R E S O P Ó L I S</h2>
                    </div>
                    <div>
                        <h1 class="font-mono z-99 select-none text-9xl text-black subpixel-antialiased animate-bounce text-center md:min-w-16">Projeto Proteger</h1>
                    </div>
                </div>
            </li>
            <li>
                <div class="flex justify-center items-center">
                    <button on:click={() => window.location.href = '/login'} id="btnTop" type="submit" class="mx-2 px-4 py-2 text-black outline outline-black outline-1 bg-transparent rounded-md shadow-lg transition-all duration-300 transform hover:scale-105 focus:outline-2 focus:ring-4">
                        Logar
                    </button>
                    <button on:click={() => window.location.href = '/register'} id="btnTop" type="submit" class="mx-2 px-4 py-2 text-white bg-black rounded-lg shadow-lg transition-all duration-300 transform hover:scale-105 focus:outline-2 focus:ring-4">
                        Registrar
                    </button>
                </div>
            </li>            
        </ol>
    </main>
</body>