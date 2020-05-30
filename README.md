### Objetivo

Criar uma api em Python usando [Flask](https://flask-ptbr.readthedocs.io/en/latest/), um micro-framework multiplataforma que provê um modelo simples para a criação de microsserviços, como APIs RESTful.

Instruções retiradas do vídeo [Tutorial Python e Flask](https://www.youtube.com/watch?v=N6cZ6aHvLYs)

### Resultados

Criado um arquivo com as seguintes informações para que fossem manipuladas e consultadas pelas rotas abaixo:

```
[
  {
    "id": 1,
    "name": "Ana",
    "lang": "python"
  }
]
```

#### Rotas

/devs [GET, POST]: obter e adicionar informações na lista de desenvolvedores;
/devs/<lang> [GET]: obter as informações filtradas por linguagem;
/devs/<id> [GET]: obter as informações filtradas por id;
/devs/<id> [PUT, DELETE]: alterar ou deletar as informações buscando por id, para enviar os dados a serem alterados, use o body com as alterações:

```
{
    "lang": "javascript"
}

```

#### Rodando localmente
