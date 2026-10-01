# Controle de Visitantes

Sistema web para registrar e acompanhar visitas em condomínios. Permite autenticar porteiros, cadastrar visitantes, registrar a autorização de entrada e finalizar visitas com o horário de saída.

## Motivação e contexto

O projeto reúne tarefas comuns da rotina de uma portaria: identificar visitantes, registrar o morador responsável pela autorização e acompanhar quem está no condomínio.

A aplicação centraliza esses registros e apresenta o andamento das visitas em um dashboard, com informações de chegada, autorização e saída.

## Tecnologias utilizadas

- **Python e Django 5.2:** lógica da aplicação, autenticação e acesso ao banco.
- **SQLite:** armazenamento dos dados.
- **Django Templates, HTML e CSS:** construção das páginas.
- **Bootstrap e template SB Admin 2:** interface visual.
- **django-widget-tweaks:** personalização dos campos dos formulários.
- **python-dotenv:** carregamento das variáveis de ambiente.

## Funcionalidades principais

- Login com e-mail e senha e encerramento da sessão.
- Cadastro do perfil de porteiro no primeiro acesso.
- Registro de visitantes, incluindo identificação, casa visitada e placa do veículo.
- Associação do registro ao porteiro responsável.
- Autorização de entrada com identificação do morador responsável.
- Registro dos horários de chegada, autorização e saída.
- Acompanhamento dos estados da visita: aguardando autorização, em visita e finalizada.
- Dashboard com indicadores por status e quantidade de registros no mês.
- Consulta dos registros e dos detalhes de cada visita.

## Como rodar localmente

### Pré-requisitos

- Python 3.10 ou superior.
- pip.
- Git.

### 1. Clonar o repositório

```bash
git clone https://github.com/Marllonlp/controle_visitantes.git
cd controle_visitantes
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente no Linux ou macOS:

```bash
source .venv/bin/activate
```

No Windows, pelo PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Copie o arquivo de exemplo no Linux ou macOS:

```bash
cp .env.example .env
```

No Windows, pelo PowerShell:

```powershell
Copy-Item .env.example .env
```

Gere uma chave Django:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Abra o `.env` e substitua o valor de `SECRET_KEY` pela chave gerada:

```env
SECRET_KEY=COLE_A_CHAVE_GERADA
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Esses valores são para execução local. Mantenha o `.env` fora do versionamento.

### 5. Preparar o banco e criar uma conta

```bash
python manage.py migrate
python manage.py createsuperuser
```

O banco SQLite será criado no arquivo `db.sqlite3`. Para a conta administrativa, informe o e-mail e a senha solicitados pelo comando.

### 6. Iniciar a aplicação

```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000/login/ e entre com a conta criada.

No primeiro acesso, complete o perfil de porteiro. O sistema vincula esse perfil automaticamente à conta autenticada.

## Fluxo de uso

1. Faça login e complete o perfil de porteiro, caso necessário.
2. Selecione **Registrar visitante** e preencha os dados da visita.
3. Abra os detalhes do visitante e informe o morador responsável para autorizar a entrada.
4. Finalize a visita quando o visitante sair.
5. Acompanhe os registros e os indicadores pelo dashboard.

A autorização é permitida apenas para visitas aguardando entrada. A finalização é permitida apenas para visitas em andamento.