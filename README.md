[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
![size-shield]
![commit-shield]

<p align="center">
  <h1 align="center">✍ Teste Técnico</h1>
</p>

## Tabela de Conteudos

* [Sobre o teste](#Sobre-o-teste)
* [Como instalar?](#Como-instalar)
* [Tecnologias Usadas](#Tecnologias-Usadas)

## Sobre o teste

### Objetivo
Desenvolver uma API utilizando Flask ou FastAPI que
implementa operações CRUD (Create, Read, Update, Delete) e integre com a API
da OpenAI para realizar transcrições de áudio.

<strong>Requisitos Funcionais</strong>

- Endpoints de Autenticação
- Upload e Transcrição de Áudio
- Gestão de Transcrições
- Filtragem de Transcrições por Assunto

<strong>Requisitos Técnicos</strong>

- Autenticação via JWT
- Status de Transcrição
- Armazenamento de Dados
- Criptografia de Senha
- Paginação
- Documentação com Swagger
- Versionamento de Código

### Objetivos atingidos

- Endpoints de Autenticação (implementado)
- Upload e Transcrição de Áudio (implementado)
- Gestão de Transcrições (implementado)
- Filtragem de Transcrições por Assunto (apenas o filtro por palavra-chave)
- Autenticação via JWT (implementado)
- Status de Transcrição (implementado)
- Armazenamento de Dados (implementado)
- Criptografia de Senha (implementado)
- Paginação (implementado)
- Documentação com Swagger (implementado)
- Versionamento de Código (implementado)

### Como o projeto foi feito?

O projeto foi construído de forma módular, permintindo mais flexibilidade e manutenibilidade, além de reutilização 
de código e divisão de tarefas. Aqui abaixo, está a estrutura de pastas:

```
│── /audios
│   ├── __init__.py
│   ├── controllers.py
│   ├── routes.py
│   ├── services.py
│── /authentication
│   ├── __init__.py
│   ├── controllers.py
│   ├── routes.py
│   ├── schemas.py
│── /config
│   ├── __init__.py
│   ├── db.py
│   ├── mongo.py
│── /migrations
│── /transcriptions
│   ├── __init__.py
│   ├── controllers.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│── /uploads
│── /users
│   ├── __init__.py
│   ├── controllers.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│── /utils
│── /venv
│── .dockerignore
│── .editorconfig
│── .env
│── .env-local
│── .gitignore
│── app.py
│── docker-compose.yml
│── Dockerfile.api
│── requirements.txt
```

Como de padrão, o `app.py` é o ponto de entrada da aplicação. Na pasta `/config` ficam as instâncias para manipulações dos bancos relacional e não-relacional. 
A aplicação é dividida em quatro módulos centrais: 

- audios
- authentication
- transcriptions
- users

E em cada arquivo, tem sua responsabilidade. O arquivo `models.py` é responsável por desenhar a tabela ou coleção do banco não relacional e fazer mapeamento, 
`routes.py` é responsavél por definir os endpoints de cada módulos, `schemas.py` é onde ficam as classes responsáveis pela serialização dos dados,
`services.py` são responsaveis integrações com OpenAI e salvar e recuperar arquivo de áudio, e por fim, o `controllers.py` são responsaveis pela requisição. 

Todas as dependências foram <i>Dockerizadas</i> para portabilidade da aplicação.
 
## Como instalar?

Inicialmente, é preciso as variáveis ​​de ambiente no arquivo .env da seguinte maneira:

```env
SQLALCHEMY_DATABASE_URI=
SQLALCHEMY_TRACK_MODIFICATIONS=
SQLALCHEMY_ECHO=

JWT_SECRET_KEY=

```

Depois disso, subir os containers

```bash
$ docker-compose up -d --build
```

E depois, é preciso rodar as migrações

```bash
$ docker exec -it baldussi-api /bin/bash

root@274c42373ef1:/app# flask db migrate

root@274c42373ef1:/app# flask db upgrade
```

## Tecnologias Usadas

* Framework Backend: [Flask](https://flask.palletsprojects.com/)
* Banco de Dados: [Postgres](https://www.postgresql.org/), [MongoDB](https://www.mongodb.com/)
* Tecnologia de processamento de banco de dados: [SQLALchemy](https://docs.sqlalchemy.org/)
* Tecnologia IA: [OpenAI](https://openai.com/)
* Ferramenta de Documentação de API: [SwaggerHUB](https://swagger.io/tools/swaggerhub/)

[contributors-shield]: https://img.shields.io/github/contributors/viniciusperrone/baldussi-admission-process?style=flat-square
[contributors-url]: https://github.com/viniciusperrone/baldussi-admission-processg/graphs/contributors

[issues-shield]: https://img.shields.io/github/issues/viniciusperrone/baldussi-admission-process?style=flat-square
[issues-url]: https://github.com/viniciusperrone/baldussi-admission-process/issues

[size-shield]: https://img.shields.io/github/repo-size/viniciusperrone/baldussi-admission-process?style=flat-square

[commit-shield]: https://img.shields.io/github/last-commit/viniciusperrone/baldussi-admission-process?style=flat-square
