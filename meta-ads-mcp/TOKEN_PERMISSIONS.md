# Permissoes do Token Meta - MCP v25.0

## Permissoes Minimas (funcionalidades basicas)
Necessarias para campanhas, adsets, ads, insights e publicos:

| Permissao | Pra que serve |
|-----------|---------------|
| `ads_management` | Criar/editar/deletar campanhas, adsets, ads, criativos |
| `ads_read` | Ler dados de campanhas, adsets, ads, insights |
| `business_management` | Gerenciar Business Manager e contas vinculadas |
| `pages_show_list` | Listar paginas do usuario |
| `pages_read_engagement` | Ler engajamento das paginas (necessario pra criativos) |
| `read_insights` | Ler metricas e relatorios |
| `public_profile` | Identificar o usuario |

## Permissoes para Lead Ads (formularios instantaneos)
Necessarias ALEM das minimas para criar adsets com `optimization_goal=LEAD_GENERATION`:

| Permissao | Pra que serve |
|-----------|---------------|
| `pages_manage_metadata` | Verificar/aceitar TOS de Lead Ads na pagina |
| `pages_manage_ads` | Gerenciar anuncios vinculados a pagina |
| `leads_retrieval` | Ler leads gerados pelos formularios |

**IMPORTANTE:** Sem `pages_manage_metadata`, a API retorna erro "Termos de Servico nao aceitos" (error 1815089) mesmo que o TOS ja tenha sido aceito na UI.

## Permissoes Opcionais (funcionalidades extras)

| Permissao | Pra que serve |
|-----------|---------------|
| `pages_manage_posts` | Publicar posts como pagina (usar posts como anuncios) |
| `instagram_basic` | Ler dados basicos do Instagram vinculado |
| `instagram_manage_comments` | Gerenciar comentarios nos anuncios do Instagram |

## Como aceitar TOS de Lead Ads
1. Acessar: `https://www.facebook.com/ads/leadgen/tos/?page_id=PAGE_ID`
2. **IMPORTANTE:** Aceitar como PERFIL PESSOAL, nao como pagina
3. Se aparecer "Nao foi possivel aceitar", trocar pra perfil pessoal primeiro

## Token no Graph API Explorer
Para gerar token com todas as permissoes:
1. Acessar: https://developers.facebook.com/tools/explorer/
2. Selecionar o app (ex: MCP - Trafego pago)
3. Adicionar permissoes: ads_management, ads_read, business_management, pages_show_list, pages_read_engagement, read_insights, pages_manage_metadata, pages_manage_ads, leads_retrieval
4. Gerar token e autorizar
