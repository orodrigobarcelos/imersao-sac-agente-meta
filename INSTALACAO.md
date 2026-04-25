# Instalação — Agente de Tráfego Meta

Este guia leva você do zero até o agente funcionando.

---

## Você vai precisar

- **Conta Meta Developer** (grátis) — `developers.facebook.com`
- **Conta de anúncios Meta Ads** ativa (com saldo ou meio de pagamento)
- **Claude Code** instalado — `claude.ai/code`
- **Conta GitHub** (grátis) — só para clonar/duplicar o template
- **Conta Railway** (opcional, ~U\$5/mês depois do trial) — para subir online com cron jobs

Tempo estimado: **15 minutos** na primeira vez.

---

## Parte A — Rodar localmente (Mac, Linux ou Windows)

> Este projeto usa **`uv`** como gerenciador Python. Os mesmos comandos
> funcionam idênticos em Mac, Linux e Windows.

### 1. Clonar o template

No GitHub, no repositório deste template, clique em **"Use this template"** →
**"Create a new repository"**. Dê um nome ao seu repo (ex: `meu-agente-trafego`)
e crie. Isso te dá uma cópia limpa que **é sua**.

Em seguida, no seu computador, abra o terminal e clone:

```bash
git clone https://github.com/SEU_USUARIO/meu-agente-trafego.git
cd meu-agente-trafego
```

### 2. Abrir no Claude Code

```bash
claude
```

O Claude vai ler automaticamente o `CLAUDE.md` e entender o projeto.

### 3. Pedir ao Claude para preparar o ambiente

Cole exatamente isso no Claude Code:

> Prepare o ambiente: instale o `uv` se eu não tiver (use o instalador oficial
> do meu sistema operacional), crie o venv em `meta-ads-mcp/.venv` e instale
> as dependências do `requirements.txt`.

O Claude detecta seu sistema e roda os comandos certos:

- **Mac/Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Você não precisa saber Python — o Claude faz tudo no terminal pra você.

### 4. Criar o app Meta

Veja **`META_APP_SETUP.md`** (na raiz do projeto) — passo a passo de criação
do app + as 9 permissões obrigatórias do token. Você pode até pedir:

> Me guie em criar o app Meta seguindo o `META_APP_SETUP.md`.

### 5. Configurar credenciais

Peça ao Claude:

> Copie `meta-ads-mcp/.env.example` para `meta-ads-mcp/.env` e me peça as
> credenciais para preencher.

Cole as 3 credenciais (`META_ACCESS_TOKEN`, `META_APP_ID`, `META_APP_SECRET`)
quando o Claude pedir. Ele preenche o `.env` pra você.

### 6. Iniciar o servidor MCP

```bash
uv run --directory meta-ads-mcp python start.py
```

Esse comando funciona idêntico em Mac, Linux e Windows. Ou simplesmente peça
ao Claude pra iniciar.

### 7. Testar

No Claude Code, peça:

> Liste minhas contas de anúncio.

Se aparecerem suas contas, está funcionando!

---

## Parte B — Subir online (produção, GitHub + Railway)

> Necessário se você quiser **agendamentos automáticos** (cron jobs) ou
> acessar o agente fora do seu computador.

### 1. Garanta que seu código está no GitHub

Se ainda não fez `git push`:

```bash
git add .
git commit -m "config inicial"
git push
```

> O `.gitignore` já está configurado para **nunca** subir o `.env` com suas
> credenciais. Confirme antes de cada push.

### 2. Criar projeto no Railway

1. Acesse [railway.app](https://railway.app) e faça login com GitHub
2. Clique **"New Project"** → **"Deploy from GitHub repo"**
3. Selecione o repo `meu-agente-trafego`
4. Railway detecta o `Dockerfile` em `meta-ads-mcp/` e começa o build
5. Aguarde o primeiro deploy (3–5 min)

### 3. Configurar variáveis de ambiente no Railway

No painel do projeto Railway → aba **Variables** → adicione:

| Variável | Valor |
|---|---|
| `META_ACCESS_TOKEN` | seu token (longa duração, 60 dias) |
| `META_APP_ID` | seu app id |
| `META_APP_SECRET` | seu app secret |

Railway define o `PORT` automaticamente — não configure manualmente.

### 4. Gerar URL pública

No painel Railway → aba **Settings** → seção **Networking** → clique
**"Generate Domain"**. Você recebe uma URL tipo
`https://meu-agente-trafego.up.railway.app`.

### 5. Apontar Claude Code para a URL pública

Edite o `.mcp.json` na raiz do projeto e troque o bloco `meta-ads` por:

```json
{
  "mcpServers": {
    "meta-ads": {
      "type": "http",
      "url": "https://SEU_PROJETO.up.railway.app/mcp",
      "headers": {
        "X-META-ACCESS-TOKEN": "SEU_TOKEN_AQUI"
      }
    }
  }
}
```

> Como o `.mcp.json` pode conter o token, ele **não vai pro GitHub** (o
> `.gitignore` já bloqueia variantes locais). Se preferir, crie
> `.mcp.local.json` com o conteúdo acima.

### 6. (Futuro) Cron jobs

Quando o agente tiver tarefas agendadas (ex: pausar campanhas com ROAS baixo
às 2h da manhã), use **Railway Cron**:

1. No Railway → **New Service** → **Cron Job**
2. Comando: a tarefa que o Claude programar
3. Agendamento: padrão cron (`0 2 * * *` = 2h todo dia)

Não precisa configurar agora — quando chegar a hora, o Claude orienta.

---

## Problemas comuns

| Erro | Solução |
|---|---|
| `uv: command not found` | Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh \| sh`. Windows (PowerShell): `irm https://astral.sh/uv/install.ps1 \| iex`. Reabra o terminal depois. |
| `python: command not found` | O `uv` baixa o Python automaticamente. Se persistir, peça ao Claude para instalar Python 3.10+. |
| `git: command not found` | Instale Git: `brew install git` (Mac) ou `winget install Git.Git` (Windows). |
| `claude: command not found` | Instale Claude Code: [claude.ai/code](https://claude.ai/code). |
| Token Meta "expired" | Gere um novo no Graph API Explorer (veja `META_APP_SETUP.md`). |
| `permissions error` em alguma tool Meta | Verifique se seu token tem as 9 permissões (`meta-ads-mcp/TOKEN_PERMISSIONS.md`). |
| Lead Ads erro 1815089 | Aceite o TOS como **perfil pessoal** em `facebook.com/ads/leadgen/tos/?page_id=ID`. |
