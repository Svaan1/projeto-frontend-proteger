# Proteger Teresópolis

## Uso

1. Crie um arquivo .env na raiz do projeto.
   Defina as variáveis de ambiente necessárias, seguindo o exemplo:

```yaml
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_NAME=name
```

2. Certifique-se de ter o Docker e o Docker Compose instalados.
   No terminal, navegue até o diretório raiz do projeto.
   Execute o seguinte comando para construir e iniciar os contêineres:

```bash
docker-compose up
```

Isso iniciará as seguintes aplicações

- Aplicação Web - Porta 8080
- Grafana - Porta 3000
- PostgreSQL - Porta 5432
