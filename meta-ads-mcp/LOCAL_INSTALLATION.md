# Meta Ads MCP — Instalação local

Guia de instalação do servidor MCP no seu computador. **Para o fluxo completo
do template (incluindo deploy Railway)**, veja `INSTALACAO.md` na raiz do
projeto.

> Este projeto usa **`uv`** como gerenciador Python — funciona idêntico em
> Mac, Linux e Windows.

---

## Pré-requisitos

- **[uv](https://docs.astral.sh/uv/)** (gerencia Python e dependências)
- **Conta Meta Ads** com acesso à conta de anúncios
- **Cliente MCP** (Claude Code, Claude Desktop, Cursor, etc.)

> Você **não** precisa instalar Python manualmente — o `uv` baixa a versão
> certa automaticamente.

### Instalar o uv (uma vez)

- **Mac/Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Reabra o terminal depois da instalação.

---

## Instalação do projeto

A partir da raiz do template:

```bash
cd meta-ads-mcp
uv sync
```

`uv sync` cria o `.venv` automaticamente e instala todas as dependências
do `pyproject.toml`.

> Alternativa via `requirements.txt`:
> ```bash
> uv venv
> uv pip install -r requirements.txt
> ```

---

## Autenticação

Este template usa **token Meta direto**. Você precisa de 3 variáveis no `.env`:

```
META_ACCESS_TOKEN=...
META_APP_ID=...
META_APP_SECRET=...
```

Para gerar essas credenciais (criar app Meta + token com 9 permissões), siga
**`META_APP_SETUP.md`** na raiz do projeto.

Copie o `.env.example` e preencha:

- **Mac/Linux:**
  ```bash
  cp .env.example .env
  ```
- **Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```
- **Windows (CMD):**
  ```cmd
  copy .env.example .env
  ```

Edite o `.env` no seu editor preferido (ou peça ao Claude Code para preencher).

---

## Rodar o servidor

A partir da raiz do template (não da pasta `meta-ads-mcp/`):

### Modo stdio (uso com Claude Code / Claude Desktop)

```bash
uv run --directory meta-ads-mcp python -m meta_ads_mcp --transport stdio
```

### Modo streamable HTTP (uso via API ou Railway)

```bash
uv run --directory meta-ads-mcp python start.py
```

A porta padrão é `8080`. Configurável via `PORT` no `.env`.

---

## Configurar clientes MCP

### Claude Code

O arquivo `.mcp.json` na raiz do template já está configurado e usa `uv run`.
Basta abrir o Claude Code na pasta do projeto:

```bash
claude
```

### Claude Desktop

Adicione ao `claude_desktop_config.json`:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/CAMINHO/ABSOLUTO/seu-projeto/meta-ads-mcp",
        "python",
        "-m",
        "meta_ads_mcp",
        "--transport",
        "stdio"
      ],
      "env": {
        "META_ACCESS_TOKEN": "seu_token_aqui",
        "META_APP_ID": "seu_app_id",
        "META_APP_SECRET": "seu_app_secret"
      }
    }
  }
}
```

> Substitua `/CAMINHO/ABSOLUTO/seu-projeto/` pelo caminho real da pasta. No
> Windows o caminho usa barras invertidas duplas no JSON
> (`C:\\Users\\seu-nome\\seu-projeto\\meta-ads-mcp`).

---

## Privacidade e segurança

### Cache de token

Após a primeira autenticação OAuth (caso use o fluxo `get_login_link`), o
servidor pode armazenar o token nestes locais:

- **macOS**: `~/Library/Application Support/meta-ads-mcp/token_cache.json`
- **Linux**: `~/.config/meta-ads-mcp/token_cache.json`
- **Windows**: `%APPDATA%\meta-ads-mcp\token_cache.json`

### Boas práticas

- Nunca comite o `.env` (o `.gitignore` já bloqueia)
- Tokens Meta de curta duração expiram em 1–2 horas — gere um token de **60
  dias** no Graph API Explorer (veja `META_APP_SETUP.md`)
- Em produção (Railway), defina as variáveis no painel de Variables, não no
  arquivo `.env`

---

## Verificação

```bash
# Verifica que importa sem erro
uv run --directory meta-ads-mcp python -c "import meta_ads_mcp; print('OK')"

# Testa o entry-point
uv run --directory meta-ads-mcp python -m meta_ads_mcp --help
```

---

## Logs e debug

Logs ficam em:

- **macOS**: `~/Library/Application Support/meta-ads-mcp/meta_ads_debug.log`
- **Linux**: `~/.config/meta-ads-mcp/meta_ads_debug.log`
- **Windows**: `%APPDATA%\meta-ads-mcp\meta_ads_debug.log`

Para modo verboso:

- **Mac/Linux:**
  ```bash
  META_ADS_DEBUG=true uv run --directory meta-ads-mcp python start.py
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:META_ADS_DEBUG="true"; uv run --directory meta-ads-mcp python start.py
  ```

---

## Problemas comuns

| Problema | Solução |
|---|---|
| `command not found: uv` | Instale o `uv` (veja "Pré-requisitos" no topo). Reabra o terminal depois. |
| `ModuleNotFoundError: No module named 'mcp'` | Rode `uv sync` na pasta `meta-ads-mcp`. |
| `"Insufficient permissions"` em chamadas Meta | Verifique se seu token tem as 9 permissões em `TOKEN_PERMISSIONS.md`. |
| `act_XXXX not found` | Confirme o ID com `get_ad_accounts` e formato `act_<id>`. |
| Rate limit | Espere antes de tentar de novo, evite rodar múltiplas instâncias. |
| Token expirou | Gere token de longa duração no Access Token Tool (passo 5 do `META_APP_SETUP.md`). |

---

## Configuração avançada

### Variáveis de ambiente extras

Defina no `.env` ou exporte na sessão:

```
META_API_VERSION=v25.0
META_API_TIMEOUT=30
META_ADS_DEBUG=true

META_ADS_DISABLE_LOGIN_LINK=1
META_ADS_DISABLE_CALLBACK_SERVER=1
META_ADS_DISABLE_ADS_LIBRARY=1
```

### Transporte HTTP

Veja `STREAMABLE_HTTP_SETUP.md` para detalhes do transporte HTTP streamable
(usado no deploy Railway).

### App Meta customizado

Se quiser usar variáveis de OAuth (em vez de token direto), veja
`CUSTOM_META_APP.md`.
