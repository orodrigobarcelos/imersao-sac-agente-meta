# Agente de Tráfego Meta (template)

Template educacional de um **agente de IA para gestão de tráfego pago Meta Ads**
(Facebook/Instagram), operado integralmente pelo [Claude Code](https://claude.ai/code)
via servidor MCP.

Sem frontend. Sem login de usuário. Sem complicação. Você clona, configura suas
credenciais Meta, e pede ao Claude:

> "Crie uma campanha de captação de leads com R\$ 50/dia para o meu pixel X."

…e ele conduz toda a operação seguindo workflows pré-definidos.

---

## O que tem nesse template

- **Servidor MCP** com 50+ tools Meta Ads (campanhas, conjuntos, anúncios,
  públicos, insights, A/B test, duplicação, upload de mídia)
- **11 workflows em markdown** que ensinam o Claude a conduzir cada operação
  passo a passo (criar campanha, criar público, gerar relatório, etc.)
- **Documentação oficial Meta API v25** offline (329 arquivos `.md`) para
  consulta do Claude antes de qualquer integração
- **Guia de criação do app Meta** com as 9 permissões obrigatórias
- **Configuração de deploy** Railway (com `Dockerfile`, `Procfile`, `railway.json`)

---

## Começar agora

1. Clique em **"Use this template"** no GitHub para criar a sua cópia
2. Clone na sua máquina
3. Abra com `claude` e siga **`INSTALACAO.md`**

---

## Estrutura

```
.
├── CLAUDE.md                  ← instruções pro Claude do aluno
├── INSTALACAO.md              ← guia de instalação (local + Railway)
├── META_APP_SETUP.md          ← como criar app Meta + 9 permissões do token
├── META_APP_APPROVAL_GUIDE.md ← guia de aprovação App Review (uso comercial)
├── META_APP_REVIEW_SUBMISSION.md
├── prompts/workflows/         ← 11 workflows que o Claude lê e executa
├── docs/meta-api-v25/         ← documentação Meta API v25 offline
└── meta-ads-mcp/              ← servidor MCP (Python)
    ├── .env.example
    ├── start.py
    ├── requirements.txt
    └── meta_ads_mcp/core/     ← 50+ tools registradas
```

---

## Stack mínima

| Ferramenta | Para quê |
|---|---|
| Claude Code | Interface de uso (terminal) |
| Python 3.10+ | Roda o servidor MCP |
| Git | Clonar/versionar |
| Conta Meta Developer | Criar app + gerar token |
| (Opcional) Railway | Deploy online + cron jobs |

Você não precisa saber Python — o Claude executa tudo no terminal por você.

---

## Créditos

O servidor MCP deste template é baseado no projeto open-source
**[pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)**
de **Yves Junqueira / ARTELL Soluções Tecnológicas**, distribuído sob a
licença **Business Source License 1.1** (veja `meta-ads-mcp/LICENSE`).

A licença permite uso e modificação livre, **exceto** oferecer este software
como SaaS competidor das ofertas comerciais da Pipeboard.

---

## Suporte

Bugs e dúvidas: abra uma issue no repositório original do template.

Para a parte do servidor MCP em si, consulte também a documentação upstream
em `meta-ads-mcp/README.md` e `meta-ads-mcp/LOCAL_INSTALLATION.md`.
