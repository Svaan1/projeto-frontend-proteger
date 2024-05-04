<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Rokkitt:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

<script>
	import { Parallax, ParallaxLayer } from 'svelte-parallax'
    import { MoveDown } from 'lucide-svelte';
    import { redirect } from '@sveltejs/kit';
	
	let parallax;
	let disabled = false;
	let text = 'PROTEGER'.split('');
</script>

<button class="disable" on:click={() => disabled = !disabled}>Desabilitar</button>
<button class="login" on:click={() => window.location.href='/login'}>Login</button>

<Parallax sections={3} bind:this={parallax} disabled={disabled}>
	{#each text as char, index (index)}
	    <ParallaxLayer
			rate={(index + 1) / (text.length - 1)}
            offset={1}
		    style=
            "
                margin-left: {32 + (index * 5)}%; 
                display: flex; 
                align-items: center;
                justify-content: flex-start;
            "
		>
			<p class="text">
				{char}
			</p>
	  </ParallaxLayer>
	{/each}
	
	<ParallaxLayer offset={1} rate={-4.5} style="display: flex; justify-content: flex-start;">
		<div style="background-image: url(../src/lib/assets/proteger.jpg); width: 33%; height: 100%; background-repeat: no-repeat;"/>
	</ParallaxLayer>

    <ParallaxLayer offset={1} rate={1.5} style="display: flex; justify-content: center;">
		<div style="background-color: yellow; opacity: 0.5; width: 33%; height: 100%;"/>
	</ParallaxLayer>

    <ParallaxLayer offset={1} rate={4.5} style="display: flex; justify-content: flex-end;">
		<div style="background-image: url(../src/lib/assets/alface.jpg); width: 33%; height: 100%; background-repeat: no-repeat;"/>
	</ParallaxLayer>
	
  <ParallaxLayer 
	  rate=1 
		style="
            background-image: url(../src/lib/assets/ddd.jpg);
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            display: flex; 
            align-items: center;
            justify-content: center;
            flex-direction: column;
            height: 100vh;
		"
	>
    <h1>Proteger</h1>
    <div class="banner">
        <div class="clouds">
            <img src="../src/lib/assets/cloud1.png" alt="clouds" style="--i:1;"/>
            <img src="../src/lib/assets/cloud2.png" alt="clouds" style="--i:2;"/>
            <img src="../src/lib/assets/cloud3.png" alt="clouds" style="--i:3;"/>
            <img src="../src/lib/assets/cloud4.png" alt="clouds" style="--i:4;"/>
            <img src="../src/lib/assets/cloud5.png" alt="clouds" style="--i:5;"/>
        </div>
    </div>
    
    <button 
		  class="top-btn" 
			on:click={() => parallax.scrollTo(3, {selector: '.top-btn', duration: 9000})}
            style="position: relative; z-index: 9999;"
		>
		  Click me!
    </button>
  </ParallaxLayer>
	
	<ParallaxLayer 
	  offset=2
		rate=2 
		style="
            background-color: pink; 
			display: flex; 
			justify-content: center; 
			align-items: center;
		"
	>
    <h3>
        O projeto Proteger Teresópolis, uma iniciativa do Centro Universitário Serra dos Órgãos (Unifeso)
        e da Secretaria Municipal de Defesa Civil para reduzir a vulnerabilidade da cidade aos desastres naturais,
        especialmente os provocados pelas chuvas, concluiu o mapeamento das duas primeiras comunidades: Coreia e Vale da Revolta.
        A ideia do projeto é, até dezembro deste ano, mapear áreas de risco em 20 comunidades da cidade.
    </h3>
  </ParallaxLayer>
</Parallax>

<style>

    .banner .clouds{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    .banner .clouds img{
        position: absolute;
        bottom: 0;
        max-width: 80%;
        animation: animate calc(12s * var(--i)) linear infinite;
    }

    @keyframes animate{
        0%{
            transform: translateX(-100%);
        }
        100%{
            transform: translateX(100%);
        }
    }

	:global(body) {
    padding: 0;
    background-color: white;
    color: #313131;
    font-family: monospace;
  }

  p{
    font-size: 2em;
    overflow-wrap: break-word;
  }

  h1 {
    font-size: 3rem;
    color: black;
  }

  h3 {
    text-align: center;
    font-size: 3em; /* You can adjust the font size as needed */
    font-weight: bold; /* Optional: make the text bold */
    margin-top: 20px; /* Optional: add some top margin for spacing */
  }

  button {
    font-size: 1rem;
		cursor: pointer;
  }

  button:hover{
    outline: 4px solid crimson;
  }

  button:focus {
    outline: 4px dashed crimson;
  }

  .login{
    position: fixed;
    top: 1rem;
    right: 1rem;
    z-index: 9999;
  }

  .disable {
    position: fixed;
    top: 1rem;
    left: 1rem;
    z-index: 9999;
  }
	
    .text {
        font-size: 2.5rem;
    }
</style>