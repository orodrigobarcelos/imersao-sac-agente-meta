# Meta Ads MCP — Instalação local

Guia de instalação do servidor MCP no seu computador. **Para o fluxo completo
do template (incluindo deploy Railway)**, veja `INSTALACAO.md` na raiz do
projeto.

> Este arquivo cobre só a parte do servidor MCP em si.

---

## Pré-requisitos

- **Python 3.10+**
- **[uv](https://docs.astral.sh/uv/)** (recomendado) ou `pip` + `venv`
- **Conta Meta Ads** com acesso à conta de anúncios
- **Cliente MCP** (Claude Code, Claude Desktop, Cursor, etc.)

---

## Instalação

A partir da raiz do template:

```bash
cd meta-ads-mcp

# Criar venv
python3 -m venv .venv

# Instalar dependências
.venv/bin/pip install -r requirements.txt

# (Opcional) instalar em modo dev se for editar o código
.venv/bin/pip install -e .
```

---

## Autenticação

Este template usa **token Meta direto**. Você precisa de 3 variáveis no `.env`:

```bash
META_ACCESS_TOKEN=...
META_APP_ID=...
META_APP_SECRET=...
```

Para gerar essas credenciais (criar app Meta + token com 9 permissões), siga
**`META_APP_SETUP.md`** na raiz do projeto.

Copie o `.env.example` e preencha:

```bash
cp .env.example .env
# Edite .env com seu editor preferido
```

---

## Rodar o servidor

### Modo stdio (uso com Claude Code / Claude Desktop)

```bash
.venv/bin/python -m meta_ads_mcp --transport stdio
```

### Modo streamable HTTP (uso via API ou Railway)

```bash
.venv/bin/python start.py
```

A porta padrão é `8080`. Configurável via `PORT` no `.env`.

---

## Configurar clientes MCP

### Claude Code

O arquivo `.mcp.json` na raiz do template já está configurado. Apenas garanta
que o `.venv` foi criado e abra o Claude Code na pasta:

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
      "command": "/CAMINHO/ABSOLUTO/seu-projeto/meta-ads-mcp/.venv/bin/python",
      "args": ["-m", "meta_ads_mcp", "--transport", "stdio"],
      "env": {
        "META_ACCESS_TOKEN": "seu_token_aqui",
        "META_APP_ID": "seu_app_id",
        "META_APP_SECRET": "seu_app_secret"
      }
    }
  }
}
```

> Substitua `/CAMINHO/ABSOLUTO/` pelo caminho real da pasta no seu computador.

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
.venv/bin/python -c "import meta_ads_mcp; print('OK')"

# Testa o entry-point
.venv/bin/python -m meta_ads_mcp --help
```

---

## Logs e debug

Logs ficam em:

- **macOS**: `~/Library/Application Support/meta-ads-mcp/meta_ads_debug.log`
- **Linux**: `~/.config/meta-ads-mcp/meta_ads_debug.log`
- **Windows**: `%APPDATA%\meta-ads-mcp\meta_ads_debug.log`

Para modo verboso:

```bash
META_ADS_DEBUG=true .venv/bin/python start.py
```

---

## Problemas comuns

| Problema | Solução |
|---|---|
| `command not found: python3` | Instale Python 3.10+ |
| `ModuleNotFoundError: No module named 'mcp'` | Rode `.venv/bin/pip install -r requirements.txt` |
| `"Insufficient permissions"` em chamadas Meta | Verifique se seu token tem as 9 permissões em `TOKEN_PERMISSIONS.md` |
| `act_XXXX not found` | Confirme o ID com `get_ad_accounts` e formato `act_<id>` |
| Rate limit | Espere antes de tentar de novo, evite rodar múltiplas instâncias |
| Token expirou | Gere token de longa duração no Access Token Tool (passo 5 do `META_APP_SETUP.md`) |

---

## Configuração avançada

### Variáveis de ambiente extras

```bash
# Versão da API
export META_API_VERSION=v25.0

# Timeout em segundos
export META_API_TIMEOUT=30

# Modo debug
export META_ADS_DEBUG=true

# Desativar tools opcionais
export META_ADS_DISABLE_LOGIN_LINK=1
export META_ADS_DISABLE_CALLBACK_SERVER=1
export META_ADS_DISABLE_ADS_LIBRARY=1
```

### Transporte HTTP

Veja `STREAMABLE_HTTP_SETUP.md` para detalhes do transporte HTTP streamable
(usado no deploy Railway).

### App Meta customizado

Se quiser usar variáveis de OAuth (em vez de token direto), veja
`CUSTOM_META_APP.md`.
