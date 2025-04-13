## O que é necessário

- Poetry
- Python 3.12.*

## Links

https://fastapidozero.dunossauro.com/
https://python-poetry.org/docs/managing-environments/#powershell


## Intalação no windows

Execute o terminal como administrador e execute:

```bash
pip install poetry
```

Verifique a instalação

```bash
poetry
```

## Criação do projeto

Entre na pasta que deseja por seu projeto e crie com:

```bash
poetry new nome_projeto
```

Entre na pasta

```bash
cd nome_projeto
```

Entre com seu editor, no meu caso é VS Code

```bash
code .
```

## Configuração do ambiente

crie o ambiente virtual, no mesmo nível do seu pyproject.toml execute:

```bash
poetry install
```

Mude algumas informações do pyproject

```bash
requires-python = ">=3.12,<4.0"
```

Instalando dependencias no Poetry

```bash
poetry add nome_dep
```
exemplo:

```bash
poetry add fastapi
```

## Ativando seu ambiente virtual poetry
Documentação

https://python-poetry.org/docs/managing-environments/#powershell

Obtendo informações

```bash
poetry env info
```

Informações do ambiente virtual

```bash
poetry env info --path
```
Como ativar o ambiente (retorna a expressão a ser utilizada)

```bash
poetry env activate
```

## Rodando seu Hello Word

No terminal faça:

```bash
fastapi dev src/teste_poetry/app.py
```
Se alegar erro instale (dentro do seu ambiente virtual):

```bash
poetry add "fastapi[standard]"
```

e rode o comando novamente

```bash
fastapi dev src/teste_poetry/app.py
```

### (pule) Rodando seu Helo Word - sem fastapi

No terminal faça:

```bash
python -i src/teste_poetry/app.py
```

dentro da interação rode sua função

```bash
read_root()
```

## Instalando ferramentas auxiliares
Lista

- Ruff: análise do código

Instalando

```bash
poetry add --group dev ruff
```
Utilizando

```bash
ruff check .
```

- Pytest e Pytest-cov: testes da aplicação

Instalando

```bash
poetry add --group dev pytest pytest-cov
```
Utilizando

```bash
pytest
```

- Taskipy

Instalando

```bash
poetry add --group dev taskipy
```
Utilizando para executar o fastapi

```bash
task nome_tesk
```

Exemplo

```bash
task run
```