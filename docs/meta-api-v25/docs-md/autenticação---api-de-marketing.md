<!-- Fonte: Autenticação - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/get-started/authentication -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Autenticação


Na API de Marketing, é preciso enviar um token de acesso como parâmetro em cada chamada de API.


Consulte [Tokens de acesso para tecnologias da Meta](https://developers.facebook.com/docs/facebook-login/guides/access-tokens) para obter mais informações sobre os vários tipos de tokens de acesso.


## Obter um token de acesso para seu app


### Tokens de acesso do usuário


#### Explorador da Graph API


Você pode obter um token de acesso do usuário usando o [Explorador da Graph API](https://developers.facebook.com/tools/explorer). Se quiser aprender a usar a ferramenta para fazer chamadas de API, consulte o [Guia do Explorador da Graph API](https://developers.facebook.com/docs/graph-api/explorer).


- No campo **App da Meta**, selecione um app para obter o token de acesso.
- No campo **Usuário ou Página**, selecione **Token do usuário**.
- No menu suspenso **Adicionar uma permissão** em **Permissões**, selecione as permissões necessárias (por exemplo, `ads_read` e/ou `ads_management`).
- Clique em **Gerar token de acesso**. A caixa na parte superior do botão será preenchida com o token de acesso. [Armazene o token](https://developers.facebook.com/docs/marketing-api/get-started/authentication#storing-the-token) para usar mais tarde.


#### Depurar


Para saber mais sobre o token que você acabou de gerar, clique no ícone de informações (**i**) em frente ao token para abrir a tabela **Informações sobre o token de acesso**, que exibe alguns detalhes básicos. Clique em **Abrir na Ferramenta Token de Acesso** para acessar o [Depurador de Token de Acesso](https://developers.facebook.com/tools/debug/accesstoken).


Durante a depuração, você poderá verificar o seguinte:


- **ID do app:** o ID do app mencionado na seção de pré-requisitos.
- **Expira:** um carimbo de data e hora. Um token de curta duração expira dentro de uma hora ou duas.
- **Escopos:** contém as permissões adicionadas no Explorador da Graph API.


#### Estender token de acesso


- Cole seu token na caixa de texto do [Depurador de Token de Acesso](https://developers.facebook.com/tools/debug/accesstoken) e clique em **Depurar**.
- Clique em **Estender token de acesso** na parte inferior da tabela **Informações sobre o token de acesso** para obter um token de longa duração e copiá-lo para uso posterior.


Verifique as propriedades do seu novo token usando o Depurador de Token de Acesso. Ele deve ter um tempo de validade mais longo, como 60 dias, ou exibir Nunca no campo **Expira**. Para mais informações, consulte [Tokens de longa duração de acesso](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing).


### Tokens de acesso de usuário do sistema


Um token de acesso de usuário do sistema é um tipo de token de acesso associado a uma conta de usuário do sistema, que é uma conta criada no Gerenciador de Negócios da Meta com o objetivo de gerenciar ativos e fazer chamadas à API de Marketing. Os tokens de acesso de usuário do sistema serão úteis para interações entre servidores onde não houver um usuário presente para autenticar. Eles podem ser usados para realizar ações em nome da empresa, como ler e escrever dados do negócio, além de gerenciar campanhas e outros objetos do anúncio.


Uma vantagem de usar um token de acesso de usuário do sistema é que ele não expira, o que significa que ele pode ser utilizado em scripts ou serviços de longa duração que precisam acessar a API de Marketing. Além disso, como as contas de usuário do sistema não estão vinculadas a um indivíduo específico, elas podem ser usadas para fornecer um nível de separação entre atividades pessoais e comerciais em tecnologias da Meta.


Os tokens de usuário do sistema também são menos propensos a serem invalidados por outros motivos, em comparação aos tokens de acesso de usuário de longa duração.


Consulte [Usuários do sistema](https://developers.facebook.com/docs/marketing-api/system-users) para saber mais.
[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)

## Obter um token de acesso para contas de anúncios que você gerencia


Quando o proprietário de uma conta de anúncios que será gerenciada por você clicar no botão **Permitir** após a solicitação das permissões, ele será redirecionado para um URL que contém o valor do parâmetro `redirect_uri` e um código de autorização.

```
http://SEU_URL?code=<AUTHORIZATION_CODE>
```


Você poderá então criar o URL para uma chamada de API que inclui o ponto de extremidade com o objetivo de obter um token, o ID do app, o URL do site, a chave secreta do app e o código de autorização que acabou de receber:

```
https://graph.facebook.com/v25.0/oauth/access_token? client_id=<YOUR_APP_ID> &redirect_uri=<YOUR_URL> &client_secret=<YOUR_APP_SECRET> &code=<AUTHORIZATION_CODE>
```


A resposta da API deve conter o token de acesso gerado:


- Ao seguir o fluxo de autenticação do servidor, você receberá um token persistente.
- Caso opte pelo fluxo de autenticação do lado do cliente, você receberá um token com um prazo de validade limitado, de uma a duas horas. Ele poderá ser substituído por um token persistente. Basta fazer uma chamada ao [ponto de extremidade da Graph API para tokens estendidos](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived).


Se a API for invocada por um [usuário do sistema](https://developers.facebook.com/docs/marketing-api/system-users) de uma empresa, você poderá usar um [token de acesso de usuário do sistema](https://developers.facebook.com/docs/marketing-api/system-users/install-apps-and-generate-tokens).


É possível depurar o token, verificar a data de expiração e validar as permissões concedidas no [Depurador de Token de Acesso](https://developers.facebook.com/tools/accesstoken) ou usando a [API de Validação Programática](https://developers.facebook.com/docs/facebook-login/access-tokens#debug).
[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)

## Como armazenar o token


O token deve ser armazenado com segurança no seu banco de dados para chamadas de API subsequentes. A movimentação de tokens entre seu cliente e o servidor deve ser feita de forma segura via HTTPS para garantir a segurança da conta. [Leia mais sobre as implicações de mover tokens entre os clientes e seu servidor.](https://developers.facebook.com/docs/facebook-login/access-tokens/portability)


Verifique regularmente a validade do token e, se necessário, solicite a renovação das permissões. Os tokens persistentes também podem se tornar inválidos em alguns casos, incluindo os seguintes:


- Há alterações na senha.
- As permissões são revogadas.


Como os tokens de acesso do usuário podem ser invalidados ou revogados a qualquer momento por razões diversas, é esperado que o app tenha um fluxo para poder solicitar novamente as permissões dos usuários. Verifique a validade do token do usuário quando seu app for iniciado. Se necessário, execute novamente o fluxo de autenticação para obter um token atualizado.


Caso isso não seja possível no seu app, talvez você precise solicitar permissões usando outro método. Isso pode ocorrer em casos em que as chamadas de API não são disparadas diretamente por uma interface do usuário ou são feitas periodicamente por meio da execução de scripts. Para solucionar essa questão, você pode enviar um email com instruções.
[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)

## Boas práticas para o gerenciamento seguro de credenciais


Para garantir a segurança das credenciais do usuário e dos tokens de acesso, siga estas boas práticas:


- **Use HTTPS:** sempre transmita tokens de acesso por conexões seguras (HTTPS) para evitar interceptação por agentes mal-intencionados.
- **Armazene tokens de forma segura:** utilize soluções de armazenamento seguras, como bancos de dados criptografados para armazenar acessos e atualizar tokens, minimizando o risco de acesso não autorizado.
- **Limite o escopo do token:** solicite apenas as permissões mínimas necessárias, reduzindo o risco de superexposição dos dados do usuário.
- **Implemente a expiração do token:** atualize os tokens regularmente e tenha um mecanismo sólido para lidar com a expiração, garantindo acesso contínuo sem expor tokens de longa duração.
[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)

## Saiba mais


- [Tokens de acesso](https://developers.facebook.com/docs/facebook-login/access-tokens)
- [Tokens de acesso de longa duração](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing)
- [Depuração e erros](https://developers.facebook.com/docs/facebook-login/access-tokens/debugging-and-error-handling)
- [Tokens de acesso à informação da sessão](https://developers.facebook.com/docs/facebook-login/access-tokens/session-info-access-token)
- [Portabilidade](https://developers.facebook.com/docs/facebook-login/access-tokens/portability)
[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)[○](https://developers.facebook.com/docs/marketing-api/get-started/authentication#)Nesta Página[Autenticação](https://developers.facebook.com/docs/marketing-api/get-started/authentication#autentica--o)[Obter um token de acesso para seu app](https://developers.facebook.com/docs/marketing-api/get-started/authentication#obter-um-token-de-acesso-para-seu-app)[Tokens de acesso do usuário](https://developers.facebook.com/docs/marketing-api/get-started/authentication#tokens-de-acesso-do-usu-rio)[Tokens de acesso de usuário do sistema](https://developers.facebook.com/docs/marketing-api/get-started/authentication#tokens-de-acesso-de-usu-rio-do-sistema)[Obter um token de acesso para contas de anúncios que você gerencia](https://developers.facebook.com/docs/marketing-api/get-started/authentication#obter-um-token-de-acesso-para-contas-de-an-ncios-que-voc--gerencia)[Como armazenar o token](https://developers.facebook.com/docs/marketing-api/get-started/authentication#como-armazenar-o-token)[Boas práticas para o gerenciamento seguro de credenciais](https://developers.facebook.com/docs/marketing-api/get-started/authentication#boas-pr-ticas-para-o-gerenciamento-seguro-de-credenciais)[Saiba mais](https://developers.facebook.com/docs/marketing-api/get-started/authentication#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZw3FgBP-lQ6fU9vzP0MxpvulyXomuISWRasl3dvGepO20hQJ1aTNl2YjrQ_aem_0ftIdwsJIiEqVFBidP6oaQ&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR472RZgOx4kaSBMF_ARKWNqyr-w9iqI98dpIYKQAtRRcgEOrswf3j4ASX_DHA_aem_-Q_iqdALmMy8zvq5QtOeQA&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69H3zRHQwAWZapqq5TOInp71Ag-drOhq2hQAZWjqhYo1pzkvrk4zgwmWKhYg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eoQgGkWWxGwH96germ7N_usI2ydp8FdX8YObYy_ZU2Wuwv1ZW-XZimUwzng_aem_ejJC2cDiQsA_XlSKxdBakw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5D1B2QYJfs6RDDucubo0O7c67p0aaOiB_BQx5AYvYhQx9HtSw7Jg1a0BR-dg_aem_aEKz6Qar57Ffqetv_AHT1A&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yGsmsVIXoWZI2FhWhKo-m0OAggPBqLOVW-3NW3bN3bdcvz7jfwR1xw_jhNg_aem_Se5pWkoys5mc7r0sDPKlZw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5jFuhaf8gDVarUZSdOvkt7zgXsMzLQCGP94Xpy0A2GCsErMnKH8MvElMwnHQ_aem_5Ad4h5G9L1BKRgCkX7yyGA&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eoQgGkWWxGwH96germ7N_usI2ydp8FdX8YObYy_ZU2Wuwv1ZW-XZimUwzng_aem_ejJC2cDiQsA_XlSKxdBakw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yGsmsVIXoWZI2FhWhKo-m0OAggPBqLOVW-3NW3bN3bdcvz7jfwR1xw_jhNg_aem_Se5pWkoys5mc7r0sDPKlZw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR472RZgOx4kaSBMF_ARKWNqyr-w9iqI98dpIYKQAtRRcgEOrswf3j4ASX_DHA_aem_-Q_iqdALmMy8zvq5QtOeQA&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZw3FgBP-lQ6fU9vzP0MxpvulyXomuISWRasl3dvGepO20hQJ1aTNl2YjrQ_aem_0ftIdwsJIiEqVFBidP6oaQ&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69H3zRHQwAWZapqq5TOInp71Ag-drOhq2hQAZWjqhYo1pzkvrk4zgwmWKhYg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yGsmsVIXoWZI2FhWhKo-m0OAggPBqLOVW-3NW3bN3bdcvz7jfwR1xw_jhNg_aem_Se5pWkoys5mc7r0sDPKlZw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eoQgGkWWxGwH96germ7N_usI2ydp8FdX8YObYy_ZU2Wuwv1ZW-XZimUwzng_aem_ejJC2cDiQsA_XlSKxdBakw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6B-CmiJki_tl8yW-7PjmIph4zfKo3ovbf0vuFW0PRWh23Xc1TFiBQ_0yYwxQ_aem_dbZNYq9DH_AWJDoXUOPpVw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69H3zRHQwAWZapqq5TOInp71Ag-drOhq2hQAZWjqhYo1pzkvrk4zgwmWKhYg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6B-CmiJki_tl8yW-7PjmIph4zfKo3ovbf0vuFW0PRWh23Xc1TFiBQ_0yYwxQ_aem_dbZNYq9DH_AWJDoXUOPpVw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6B-CmiJki_tl8yW-7PjmIph4zfKo3ovbf0vuFW0PRWh23Xc1TFiBQ_0yYwxQ_aem_dbZNYq9DH_AWJDoXUOPpVw&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR472RZgOx4kaSBMF_ARKWNqyr-w9iqI98dpIYKQAtRRcgEOrswf3j4ASX_DHA_aem_-Q_iqdALmMy8zvq5QtOeQA&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5jFuhaf8gDVarUZSdOvkt7zgXsMzLQCGP94Xpy0A2GCsErMnKH8MvElMwnHQ_aem_5Ad4h5G9L1BKRgCkX7yyGA&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yJFkHq-bt1EpPUUABg20Lb_6ivqQt1JwhFVQL3vpZJ9V-lAFGlc1FuP_xMc0oXd_oUYg3ub45Ulpvrx50YpDEqaL7ax-XbvRArFO6l1Rq_PNm2mrBF-wXPGt6VSgHHI-4VCayFB-nPjYBWL9uIbq1-eQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão