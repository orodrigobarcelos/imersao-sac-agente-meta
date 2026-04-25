# Guia de Aprovacao do App na Meta (App Review)

## Visao Geral
O App Review e o processo onde a Meta verifica como seu app usa as APIs antes de dar permissoes avancadas.
Sem aprovacao, o app so funciona com usuarios que sao admins/devs do app.

## Timeline
- Aprovacao: 2-7 dias
- Rejeicao + nova tentativa: +3-5 dias por tentativa

## Permissoes que precisamos aprovar

| Permissao | Nivel | Pra que |
|-----------|-------|---------|
| ads_management | Advanced | Criar/editar campanhas, adsets, ads |
| ads_read | Advanced | Ler dados de campanhas e insights |
| business_management | Advanced | Gerenciar Business Manager |
| pages_read_engagement | Advanced | Ler engajamento das paginas (pre-requisito de ads_management) |
| pages_manage_metadata | Advanced | Lead Ads TOS |
| pages_manage_ads | Advanced | Gerenciar anuncios vinculados a pagina |
| leads_retrieval | Advanced | Ler leads de formularios |

## Requisitos obrigatorios
1. Business Verification — empresa verificada no Business Manager
2. Privacy Policy — URL publica com politica de privacidade
3. App em modo Live (nao Development)
4. Screencast (video) obrigatorio pra cada permissao

## Screencast — O mais importante
O revisor da Meta NAO explora o app sozinho — o screencast e a referencia principal.

O que incluir no video:
- Mostrar a tela de login/autenticacao
- Demonstrar CADA permissao em uso (criar campanha, ler insights, gerenciar ads)
- Explicar por que o app precisa daquela permissao
- Mostrar o fluxo completo do usuario
- O video deve ser como se o revisor nunca tivesse visto o app

## Erros comuns que causam rejeicao
1. Screencast ruim — nao mostra a funcionalidade claramente
2. Pedir permissoes desnecessarias — so peca o que realmente usa
3. App inacessivel — revisor nao consegue acessar (URL offline, senha errada)
4. Credenciais de teste — nao fornecer conta de teste funcional
5. Privacy Policy — URL inexistente ou generica
6. Sem fluxo visivel — listar permissao sem mostrar uso real no app
7. Fazer mudancas no app apos submeter — pode exigir re-review

## Dicas de quem ja passou
- Gravar screencasts separados por permissao
- Descrever claramente pra que serve cada permissao no formulario
- Ter dados reais no app (campanhas criadas, insights aparecendo)
- URL do app deve estar acessivel publicamente
- pages_read_engagement e pre-requisito de ads_management — aprovar primeiro

## Caso real: app de Ads (similar ao nosso)
Um app similar (Tmax - AI Ad Creation) foi rejeitado porque:
- Screencasts nao mostravam criacao de campanhas e ads funcionando
- Credenciais de teste nao permitiam publicar anuncios
- Permissoes listadas sem fluxo visivel

Solucao: refizeram os screencasts mostrando o fluxo completo e deu certo.

## Nosso plano de acao pra aprovacao
1. Verificar empresa no Business Manager (se ainda nao ta)
2. Criar Privacy Policy publica (pode ser uma pagina no site)
3. Gravar screencasts do chatbot:
   - Login e conexao do token
   - Criar campanha completa (CBO + ABO)
   - Criar adset com publico e posicionamento
   - Criar anuncio com imagem/video
   - Ver insights e relatorios
   - Listar e gerenciar campanhas
4. Submeter com descricoes claras por permissao
5. Ter conta de teste funcionando pro revisor testar

## Referencias
- https://www.saurabhdhar.com/blog/meta-app-approval-guide
- https://developers.facebook.com/docs/resp-plat-initiatives/individual-processes/app-review/submission-guide
- https://developers.facebook.com/docs/app-review/support/rejection-guides/app-verification/
- https://developers.facebook.com/docs/permissions/reference/ads_management/
- https://medium.com/@chriscouture/how-to-get-your-meta-facebook-app-approved-in-2023
