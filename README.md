# Controle de Visitantes

Sistema web em Django para portaria de condomínio, com autenticação de porteiros, registro de visitantes e controle do ciclo completo da visita (aguardando, em visita e finalizada).

## Funcionalidades
- Login e logout de usuários.
- Dashboard com indicadores de visitantes.
- Registro de novos visitantes na portaria.
- Autorização de entrada com nome do morador responsável.
- Finalização de visita com registro de horário de saída.
- Listagem de visitantes recentes com detalhes.

## Tecnologias
- Python 3
- Django 5.2.x
- SQLite3
- `django-widget-tweaks`
- `python-dotenv`
- Bootstrap (template SB Admin 2)

## Estrutura do Projeto
```text
controle_visitantes/
├── apps/
│   ├── dashboard/
│   ├── porteiros/
│   ├── usuarios/
│   └── visitantes/
├── controle_visitantes/
│   ├── settings.py
│   └── urls.py
├── static/
├── templates/
├── manage.py
└── README.md
```

## Pré-requisitos
- Python 3.10+ (recomendado)
- `pip`

## Instalação
1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual.
3. Instale as dependências.

```bash
python -m venv .venv
source .venv/bin/activate
pip install "Django>=5.2,<5.3" django-widget-tweaks python-dotenv
```

## Variáveis de Ambiente
O projeto usa arquivo `.env` na raiz.

1. Gere uma chave segura (opcional):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

2. Crie o `.env`:
```bash
echo "SECRET_KEY=sua_chave_secreta" > .env
```

## Banco de Dados
Aplique as migrations:

```bash
python manage.py migrate
```

Crie um usuário administrador:

```bash
python manage.py createsuperuser
```

## Configuração Inicial Obrigatória
Para registrar visitantes, o usuário logado precisa ter um cadastro em `Porteiro` (relação 1:1 com `Usuario`).

Forma simples:
1. Acesse `/admin` com o superusuário.
2. Crie um registro em **Porteiros** vinculado ao usuário.

Sem esse vínculo, o registro de visitante falhará.

## Executando o Projeto
```bash
python manage.py runserver
```

Acesse no navegador:
- `http://127.0.0.1:8000/login/`

## Fluxo de Uso
1. Fazer login.
2. Clicar em **Registrar visitante**.
3. No detalhe do visitante, autorizar entrada informando o morador responsável.
4. Finalizar visita quando o visitante sair.

## Rotas Principais
- `GET /login/` -> tela de autenticação.
- `GET /logout/` -> logout do usuário.
- `GET /` -> dashboard inicial.
- `GET|POST /registrar-visitante/` -> cadastro de visitante.
- `GET|POST /visitante/<id>/` -> detalhes e autorização de entrada.
- `POST /visitante/<id>/finalizar-visita` -> finalização da visita.

## Observações
- Idioma padrão: `pt-br`.
- Fuso horário: `America/Sao_Paulo`.
- Banco padrão: `db.sqlite3` na raiz do projeto.
