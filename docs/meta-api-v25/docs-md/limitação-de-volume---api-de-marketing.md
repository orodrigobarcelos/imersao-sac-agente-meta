<!-- Fonte: Limitação de volume - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/overview/rate-limiting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Limitação de volume da API de Marketing


A API de Marketing tem a própria lógica de limitação de volume e está excluída de todos os limites de volume da Graph API. Assim, se você fizer uma chamada da API de Marketing, ela não será considerada na [limitação da Graph API](https://developers.facebook.com/docs/graph-api/advanced/rate-limiting).


O recurso que afeta a cota de limitação de volume da API de Marketing é o [Acesso Padrão ao Gerenciamento de Anúncios](https://developers.facebook.com/docs/features-reference/ads-management-standard-access/). Ao adicionar o produto da API de Marketing ao [Painel de Apps](https://developers.facebook.com/apps), você já receberá o **Acesso Padrão** ao Gerenciamento de Anúncios. Com isso, você terá acesso de desenvolvimento à API de Marketing. Se você precisar de mais cota de limitação de volume, atualize para o **acesso avançado** o Acesso Padrão ao Gerenciamento de Anúncios na [análise do app](https://developers.facebook.com/docs/marketing-api/overview/authorization/).


### Cotas


| Acesso à API de Marketing | Acesso Padrão ao Gerenciamento de Anúncios | Capacidade |
| --- | --- | --- |
| Acesso ao desenvolvimento | Acesso padrão | Cota básica de limitação de volume |
| Acesso padrão | Acesso avançado | Mais cota de limitação de volume |


A maior parte das solicitações da API de Marketing e da API de Páginas está sujeita aos limites de volume de casos de uso de empresas (BUC, pelas iniciais em inglês) e depende dos pontos de extremidade sendo consultados. Você poderá descobrir isso verificando se a sua solicitação `HTTP` contém um cabeçalho `X-Business-Use-Case`. Veja mais detalhes em [Limites de volume de casos de uso de empresas](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#buc-rate-limits).


## Limites no nível da API da conta de anúncios


- A limitação de volume está no nível da conta de anúncios.
- A limitação de volume acontece em tempo real em um determinado intervalo de tempo.
- Cada chamada da API de Marketing recebe uma pontuação. A pontuação representa a soma das chamadas da API.
- Aplicamos uma pontuação máxima. Em geral, uma chamada da API de leitura é igual a 1 ponto, e uma chamada da API de gravação é igual a 3 pontos, e quando a pontuação máxima for atingida, lançaremos um erro de limitação. - Se o app estiver no nível de desenvolvimento da API de Marketing: - A pontuação máxima é 60. - A taxa de decaimento é de 300 segundos. - Se atingir a pontuação máxima, você passará por 300 segundos de bloqueio. - Se o app estiver no nível padrão da API de Marketing: - A pontuação máxima é 9.000. - A taxa de decaimento é de 300 segundos. - Se atingir a pontuação máxima, você passará por 60 segundos de bloqueio.


**Código de erro relacionado:**`17, Error subcode: 2446079, Message: User request limit reached. 613, Error subcode: 1487742, Message: There have been too many calls from this ad-account. Please wait a bit and try again.`
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limitação de volume de QPS em nível de conta de anúncios


Para impedir que o tráfego de repente sobrecarregue nossos sistemas, aplicamos a limitação de volume em tempo real aos pontos de extremidade de mutação da API de Marketing (operações de criação e edição de campanhas, além de conjuntos de anúncios e anúncios).


- A limitação de volume ocorre no nível da conta de anúncios, por app.
- Limite: 100 solicitações por segundo (QPS) por combinação de app e conta de anúncios.
- Aplicada a: operações de criação e edição para campanhas, conjuntos de anúncios e anúncios.
- Esse limite funciona em tempo real e foi desenvolvido para identificar picos curtos de tráfego que a janela-padrão de limitação de volume pode não detectar.


Os seguintes pontos de extremidade serão afetados:


- [`POST /{ad-account-id}/ads`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/ads)
- [`POST /adgroup`](https://developers.facebook.com/docs/marketing-api/reference/adgroup)
- [`POST /{ad-account-id}/adsets`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adsets)
- [`POST /adcampaign`](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign)
- [`POST /{ad-account-id}/campaigns`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/campaigns/)
- [`POST /campaigngroup`](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group)


Quando você exceder esse limite, distribua as solicitações de maneira uniforme ao longo do tempo, em vez de enviá-las em intermitências.


**Código de erro relacionado:**`613, Error subcode: 5044001, Message: Your ad account {ad_account_id} has exceeded the maximum allowed rate of mutation requests. To resolve this, reduce the frequency of your create, update operations on campaigns, ad sets, and ads.`


Quando esse erro for encontrado, implemente a limitação de solicitações para permanecer abaixo de 100 QPS por conta de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limitação de volume da plataforma de insights sobre anúncios


- A limitação de volume está no nível do app.
- A limitação de volume é determinada pela capacidade dos serviços a jusante e de infraestrutura de back-end.
- Quando seu app tiver limitação de volume, todas as chamadas da API de Insights de Anúncios para o app serão limitadas.
- A limitação de volume no nível do app é aplicada.


**Código de erro relacionado:**`4, Error subcode: 1504022 or 1504039, Message: There have been too many calls from this app. Wait a bit and try again.`


Quando esse erro for encontrado, reduza suas chamadas novamente.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limites em nível de app


- A limitação de volume está no nível do app.
- A limitação de volume é determinada pelo total de usuários de um app.
- Quando seu app tiver limitação de volume, todas as chamadas para o app serão limitadas.
- A limitação de volume no nível do app é aplicada.


**Código de erro relacionado:**`4, Message: Application request limit reached`


Quando esse erro for encontrado, reduza suas chamadas novamente.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limitação de volume de casos de uso de negócios em nível de conta de anúncios


Calculamos a cota de limitação de volume com base no seu nível de acesso à API de Marketing e no seu app.


- A limitação de volume está no nível da conta de anúncios, e a cota é calculada com base no nível de acesso à API de Anúncios do app.
- `ads_management` – para cada conta de anúncios em um período de uma hora: (100.000 se o seu app estiver no nível Padrão da API de Marketing ou 300 se o seu app estiver no nível de Desenvolvimento) + 40 * Número de anúncios ativos.
- `custom_audience` – para cada conta de anúncios em um período de uma hora: não deve ser superior a 700.000. Não deve ser inferior a 190.000 se o seu app estiver no nível Padrão da API de Marketing ou 5.000 se o seu app estiver no nível de Desenvolvimento + 40 * Número de públicos personalizados ativos.
- ads_insights – para cada conta de anúncios em um período de uma hora: (190.000 se o seu app estiver no nível Padrão da API de Anúncios ou 600 se o seu app estiver no nível de Desenvolvimento) + 400 * Número de anúncios ativos - 0,001 * Erros do usuário.
- Gerenciamento de catálogos – para cada conta de anúncios em um período de uma hora: 20.000 + 20.000 * log2 (usuários únicos).
- Lote de catálogo – para cada conta de anúncios em um período de uma hora: 200 + 200 * log2 (usuários únicos).
- A limitação de volume da API de Marketing também pode ser determinada pelo tempo total de CPU e pelo tempo total de mural na conta de anúncios. Você terá mais cota se o seu app tiver acesso padrão à API de Marketing; para saber mais, verifique o cabeçalho HTTP `[X-Business-Use-Case](/docs/graph-api/overview/rate-limiting/#headers-2)` e [Limites de volume de casos de uso de empresas](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#buc-rate-limits).


**Código de erro relacionado:**`80000, 80003, 80004, 80014, Message: There have been too many calls from this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.`


Verifique o ponto de extremidade da API e o cabeçalho HTTP `X-Business-Use-Case` para confirmar o tipo de limitação. Veja mais detalhes em [Limites de volume de casos de uso de empresas](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#buc-rate-limits). Quando esse erro for encontrado, reduza novamente as alterações à conta de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limitação de volume de gastos com anúncios em nível de conta de anúncios


Estabelecemos uma limitação de 10 vezes por dia para fazer alterações nos limites de gastos da sua conta de modo a garantir o desempenho da veiculação de anúncios.


- O número de alterações nos gastos da conta de anúncios, como os campos spend_cap, spend_cap_action, é limitado


**Código de erro relacionado:**`17, Error subcode: 1885172, Message: You can only change your account spending limit 10 times per day. Please wait to make more changes.`
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limites em nível do conjunto de anúncios


O número de alterações nos campos `daily_budget` e `lifetime_budget` do conjunto de anúncios é limitado. Para cada conjunto de anúncios, o orçamento só pode ser alterado 4 vezes por hora; se exceder esse limite, a alteração no orçamento desse conjunto de anúncios será bloqueada por uma hora.


**Código de erro relacionado:**`613, Error subcode: 1487632, Message: You can only change your ad set budget 4 times per hour. Please wait to make more changes.`


Quando esse erro for encontrado, reduza as alterações no conjunto de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limites em nível de anúncio


A criação de anúncios é limitada para uma determinada conta de anúncios com base no limite de gastos diário.


**Código de erro relacionado:**`613, Error subcode: 1487225, Message: User request limit reached`.


Verifique o subcódigo de erro (`1487225`) e o ponto de extremidade da API para confirmar o tipo de limitação. Quando esse erro for encontrado, reduza as alterações. Para aumentar o limite, você também pode aumentar o limite de gastos diário.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Limites de taxa de prevenção contra abusos


Quando nosso sistema detectar que determinadas contas de anúncios geram uma grande quantidade de tráfego anormal, a fim de proteger a estabilidade do sistema e garantir a experiência de outros usuários, reduziremos temporariamente a cota de limitação de volume da API das contas anormais. Tente entrar em contato com o [Suporte da Meta](https://developers.facebook.com/support/) para receber ajuda.


**Código de erro relacionado:**`613, Error subcode: null, Message: (#613) Calls to this api have exceeded the rate limit.`


A diferença entre isso e o limite em nível da API de nível da conta de anúncios é que esse erro não contém subcódigos de erro. Quando encontrar esse erro, investigue se alguma ação está desencadeando solicitações excessivas da API e entre em contato com o [Suporte da Meta](https://developers.facebook.com/support/) para receber ajuda.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)

## Lidar com erros de limitação


### Avaliação inicial


Verifique o nível de acesso à API de Marketing:


Por padrão, os apps têm `development_access` à API de Marketing. Para descobrir em que nível você está, acesse o painel Análise do app. Se tiver Acesso Padrão ao Gerenciamento de Anúncios, isso significará que você está no nível de desenvolvimento do acesso à API de Marketing. Se tiver acesso avançado ao recurso de Acesso Padrão ao Gerenciamento de Anúncios, isso significará que você está no nível padrão de acesso à API de Marketing. Você também pode verificar o cabeçalho `HTTP` e procurar `ads_api_access_tier` no cabeçalho [`X-Ad-Account-Usage`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers), [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) ou [`X-FB-Ads-Insights-Throttle`](https://developers.facebook.com/docs/marketing-api/insights/best-practices/#insightscallload).


Se continuar recebendo erros de limitação de volume, considere atualizar para o `standard_access` do Acesso Padrão ao Gerenciamento de Anúncios. Para chegar ao nível padrão e receber uma cota de limitação de volume mais elevada, você pode se inscrever no **acesso avançado** ao recurso de Acesso Padrão ao Gerenciamento de Anúncios no painel Análise do app.


- **Verifique os códigos de erro:** determine os códigos de erro específicos relacionados com a limitação na resposta da API.
- **Verifique os cabeçalhos HTTP:** - [`X-Ad-Account-Usage`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers) contém `acc_id_util_pct`, `reset_time_duration` e `ads_api_access_tier`. - [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) contém as informações `call_count`, `total_cputime`, `total_time` e `estimated_time_to_regain_access`, etc. para o ponto de extremidade do caso de uso de negócios. - [`X-FB-Ads-Insights-Throttle`](https://developers.facebook.com/docs/marketing-api/insights/best-practices/#insightscallload) contém `app_id_util_pct`, `acc_id_util_pct` e `ads_api_access_tier` para os pontos de extremidade da API de Insights de Anúncios.
- **Verifique o Painel de Apps:** fornecemos consoles no Painel de Apps que fornecem aos desenvolvedores um insight aprofundado sobre o sistema de limitação de volume e ajuda-os a diagnosticar e prevenir problemas de limitação de volume.


### Identifique a causa


- **Limitação de volume:** entenda as limitações de volume da API de Marketing da Meta para os diferentes pontos de extremidade usados e verifique se o número de solicitações de API está dentro dos limites permitidos para o app.
- **Limites de rajada:** verifique se os limites de rajada estão causando problemas durante os tempos de pico de uso. Normalmente, o tráfego de rajada causará limites no nível da API de nível da conta de anúncios (**Códigos de erro relacionados:**`17`, `613`).
- **Operações incorretas:** investigue se alguma operação incorreta está desencadeando solicitações excessivas de API.


### Etapas de mitigação


- **Prevenir o tráfego de rajada:** distribua solicitações de API uniformemente para evitar limitações causadas por um grande número de acessos em curto período.
- **Otimize solicitações:** combine várias solicitações menores em solicitações em lote, solicitações assíncronas ou em lotes de ID para minimizar o número total de chamadas de API.
- **Estratégia de recuo:** implemente um recuo exponencial ao receber erros de limitação, aumentando gradualmente o tempo entre as tentativas. Você também pode examinar cabeçalhos HTTP para a estimativa de tempo de redefinição.


#### Outras dicas de mitigação


- Verifique se há necessidade de fazer essas chamadas e reduza-as se for desnecessário.
- Para pontos de extremidade que aceitam solicitações assíncronas, como a API de Insights de Anúncios, use [solicitações assíncronas](https://developers.facebook.com/docs/marketing-api/asyncrequests) para consultar uma enorme quantidade de dados.
- Você também pode tentar passar uma lista de identificações se precisar consultar vários do mesmo tipo de objetos de anúncio.
- Para a API de Insights, use [Level Parameters](https://developers.facebook.com/docs/marketing-api/insights/parameters/v2.7) ou filtre para reduzir o número de chamadas.
[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)[○](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#)Nesta Página[Limitação de volume da API de Marketing](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limita--o-de-volume-da-api-de-marketing)[Limites no nível da API da conta de anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limites-no-n-vel-da-api-da-conta-de-an-ncios)[Limitação de volume de QPS em nível de conta de anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limita--o-de-volume-de-qps-em-n-vel-de-conta-de-an-ncios)[Limitação de volume da plataforma de insights sobre anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limita--o-de-volume-da-plataforma-de-insights-sobre-an-ncios)[Limites em nível de app](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limites-em-n-vel-de-app)[Limitação de volume de casos de uso de negócios em nível de conta de anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limita--o-de-volume-de-casos-de-uso-de-neg-cios-em-n-vel-de-conta-de-an-ncios)[Limitação de volume de gastos com anúncios em nível de conta de anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limita--o-de-volume-de-gastos-com-an-ncios-em-n-vel-de-conta-de-an-ncios)[Limites em nível do conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limites-em-n-vel-do-conjunto-de-an-ncios)[Limites em nível de anúncio](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limites-em-n-vel-de-an-ncio)[Limites de taxa de prevenção contra abusos](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#limites-de-taxa-de-preven--o-contra-abusos)[Lidar com erros de limitação](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#lidar-com-erros-de-limita--o)[Avaliação inicial](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#avalia--o-inicial)[Identifique a causa](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#identifique-a-causa)[Etapas de mitigação](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting#etapas-de-mitiga--o) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4YmxANasZwygR0uTUYlS4BNptpbHUhpHTQTISXPbSSUhskJ6HALhDI7M6QjQ_aem_GW1bvX_939_88-kbJAZ2yg&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQzrUgqR-oBC12jQEkAIffufNP2X5ZMZ42mzuRlVWjTL67Jwx3_Ql_9CHYA_aem_6brTpYTAkabyHuceB2L7Cw&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4M482Z0NP2LnqPOhhkJC5RSJRygW4L03D5coWEaLbnODShVUP0h-Vjrkwzjg_aem_bPDQo83l78LxsWmtCw4tZg&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4M482Z0NP2LnqPOhhkJC5RSJRygW4L03D5coWEaLbnODShVUP0h-Vjrkwzjg_aem_bPDQo83l78LxsWmtCw4tZg&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Zm0q7g2JRKdpKB6efjy41khE2djM8VyXwrsSKBmqujle8d_xjG9PEcgHGCw_aem_UqD4QgB_L1dDiUvUxz4ktQ&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UPkBC367cRzr_Yc_pGKpCZ9OxrY2uPYKZ3kWvGJP6qjHLPDSG3wOyRIspVA_aem_47XbdNyajDHTrVi7wImz8g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7PtFaghrN9Ug2KKbUHToxfl53lePE3x32jhGg53JL2m59jTTBNNzYqxD4eIA_aem_1WZpRyh-4yI4oCy0jKKJ-g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UPkBC367cRzr_Yc_pGKpCZ9OxrY2uPYKZ3kWvGJP6qjHLPDSG3wOyRIspVA_aem_47XbdNyajDHTrVi7wImz8g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UTdIHFaa5-P-Ku27G6TwQzGawByNRxuyDleAjcgO2ammLCiBQGfgCQlW7oA_aem_TJ1Ss-PfPW2WJ6Oc_JRBXQ&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7PtFaghrN9Ug2KKbUHToxfl53lePE3x32jhGg53JL2m59jTTBNNzYqxD4eIA_aem_1WZpRyh-4yI4oCy0jKKJ-g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4M482Z0NP2LnqPOhhkJC5RSJRygW4L03D5coWEaLbnODShVUP0h-Vjrkwzjg_aem_bPDQo83l78LxsWmtCw4tZg&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UPkBC367cRzr_Yc_pGKpCZ9OxrY2uPYKZ3kWvGJP6qjHLPDSG3wOyRIspVA_aem_47XbdNyajDHTrVi7wImz8g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UTdIHFaa5-P-Ku27G6TwQzGawByNRxuyDleAjcgO2ammLCiBQGfgCQlW7oA_aem_TJ1Ss-PfPW2WJ6Oc_JRBXQ&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQzrUgqR-oBC12jQEkAIffufNP2X5ZMZ42mzuRlVWjTL67Jwx3_Ql_9CHYA_aem_6brTpYTAkabyHuceB2L7Cw&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQzrUgqR-oBC12jQEkAIffufNP2X5ZMZ42mzuRlVWjTL67Jwx3_Ql_9CHYA_aem_6brTpYTAkabyHuceB2L7Cw&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Zm0q7g2JRKdpKB6efjy41khE2djM8VyXwrsSKBmqujle8d_xjG9PEcgHGCw_aem_UqD4QgB_L1dDiUvUxz4ktQ&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72Apefla7ia-YwB2w2KFx0b4b3tnYNy3yM2-zPy4y2r4NSAvEI3mm7CGeFXg_aem_F_iFSnieb_KYuZyQbk0a6g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UPkBC367cRzr_Yc_pGKpCZ9OxrY2uPYKZ3kWvGJP6qjHLPDSG3wOyRIspVA_aem_47XbdNyajDHTrVi7wImz8g&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQzrUgqR-oBC12jQEkAIffufNP2X5ZMZ42mzuRlVWjTL67Jwx3_Ql_9CHYA_aem_6brTpYTAkabyHuceB2L7Cw&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Zm0q7g2JRKdpKB6efjy41khE2djM8VyXwrsSKBmqujle8d_xjG9PEcgHGCw_aem_UqD4QgB_L1dDiUvUxz4ktQ&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4BdoY5mrr0x5E_zmNs-gHJzQYOZfqHkap9KHbdOnwE_RR3Y1crRq0dJXfqzuaOQ_EkMQclgjSXMp9ISGxdBpGxrBkCjP5kyj1h9rSHASc0x79S6fGenHHwm0CkEoHIqMOro6T-U1vMLW2RDgKcDt-EJXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão