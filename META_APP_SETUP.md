# Como criar seu app Meta e gerar o token

> Este passo é **obrigatório** antes de usar o agente. Leva uns 10 minutos.

---

## 1. Criar o app no Meta Developers

1. Acesse [developers.facebook.com/apps](https://developers.facebook.com/apps)
2. Faça login com sua conta Facebook (a mesma que tem acesso à conta de anúncios)
3. Clique **"Criar app"**
4. Tipo: **"Empresa"** (Business) — clique avançar
5. Nome do app: algo simples (ex: `Meu Agente Tráfego`)
6. E-mail de contato: o seu
7. Clique **"Criar app"** e confirme com sua senha do Facebook

---

## 2. Adicionar o produto Marketing API

1. No painel do app recém-criado, role até a seção **"Adicionar produtos"**
2. Procure **"Marketing API"** → clique **"Configurar"**
3. Pronto. Não precisa configurar mais nada nessa tela.

---

## 3. Gerar o token de acesso

1. Acesse o [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. No canto superior direito, em **"Aplicativo Meta"**, selecione o app que você acabou de criar
3. Em **"Tipo de token de acesso ao usuário"**, deixe **"User Token"**
4. Clique no botão **"Adicionar permissões"** (lápis) e marque exatamente estas 9:

### Permissões obrigatórias (9)

| Permissão | Para quê |
|---|---|
| `ads_management` | Criar/editar/deletar campanhas, conjuntos, anúncios |
| `ads_read` | Ler dados de campanhas e métricas |
| `business_management` | Acessar Business Manager e contas vinculadas |
| `pages_show_list` | Listar suas páginas |
| `pages_read_engagement` | Ler engajamento das páginas (criativos) |
| `read_insights` | Ler relatórios e métricas |
| `pages_manage_metadata` | Aceitar TOS de Lead Ads |
| `pages_manage_ads` | Gerenciar anúncios vinculados a páginas |
| `leads_retrieval` | Ler leads gerados (Lead Ads) |

> **Importante:** sem `pages_manage_metadata`, formulários de Lead Ads vão
> dar erro 1815089 ("Termos de Serviço não aceitos") — mesmo que você já
> tenha aceitado na interface.

5. Clique **"Gerar token de acesso"**
6. Vai abrir uma popup do Facebook pedindo autorização → **"Continuar como [seu nome]"**
7. Na lista de permissões da popup, **mantenha todas marcadas** → confirme
8. Volte ao Graph API Explorer e **copie o token** que apareceu no campo

---

## 4. Pegar App ID e App Secret

1. Volte para [developers.facebook.com/apps](https://developers.facebook.com/apps) e abra seu app
2. Menu lateral → **Configurações → Básico**
3. **App ID:** copie o número que aparece no topo
4. **Chave secreta do app (App Secret):** clique **"Mostrar"**, confirme com sua senha, e copie

---

## 5. Colar no `.env` do projeto

Na pasta do projeto, abra `meta-ads-mcp/.env` (se não existir, copie de
`meta-ads-mcp/.env.example`) e preencha:

```bash
META_ACCESS_TOKEN=<token gerado no passo 3>
META_APP_ID=<app id do passo 4>
META_APP_SECRET=<app secret do passo 4>
```

Pronto. Pode pedir pro Claude iniciar o servidor MCP.

---

## Aceitar o TOS de Lead Ads (se for usar formulários)

1. Acesse `https://www.facebook.com/ads/leadgen/tos/?page_id=ID_DA_SUA_PAGINA`
   (substitua `ID_DA_SUA_PAGINA`)
2. Importante: aceite como **PERFIL PESSOAL**, não como página.
   Se aparecer "Não foi possível aceitar", troque para perfil pessoal e tente
   de novo.

---

## Token expirou? (depois de 1–2 horas)

O token gerado pelo Graph API Explorer é de curta duração. Para obter um token
de **60 dias**:

1. Volte ao [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Clique no ícone de **informações (i)** ao lado do token
3. Clique **"Abrir no Access Token Tool"**
4. Lá, role até **"Estender token de acesso"** → clique
5. Copie o novo token de longa duração e atualize o `.env`

> **Detalhes adicionais sobre permissões:** veja `meta-ads-mcp/TOKEN_PERMISSIONS.md`.
