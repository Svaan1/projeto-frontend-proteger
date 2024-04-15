# Proteger Teresópolis

## Uso

1. Crie um arquivo .env na raiz do projeto.
   Defina as variáveis de ambiente necessárias, seguindo o exemplo do arquivo `.env.default`.

2. Certifique-se de ter o Docker e o Docker Compose instalados.
   No terminal, navegue até o diretório raiz do projeto.
   Execute o seguinte comando para construir e iniciar os contêineres:

```bash
docker-compose up
```

Isso iniciará os seguintes serviços:

- Grafana - Porta 3000
- PostgreSQL - Porta 5432
- Backend - Porta 8080
- Frontend - Porta 80
