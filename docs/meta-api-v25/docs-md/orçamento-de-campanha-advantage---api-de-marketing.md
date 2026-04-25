<!-- Fonte: Orçamento de campanha Advantage - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Orçamento de campanha Advantage


Um orçamento de campanha Advantage é uma forma de otimizar a distribuição de um orçamento de campanha nos conjuntos de anúncios da sua campanha. Isso significa que o Facebook encontra de modo automático e contínuo as melhores oportunidades de resultados disponíveis nos conjuntos de anúncios e distribui seu orçamento de campanha em tempo real para obter esses resultados.


Você pode habilitar ou desabilitar um orçamento de campanha Advantage para uma campanha de anúncios. Se ele for desabilitado, você deverá fornecer orçamentos para todos os conjuntos de anúncios da campanha.


## Campos em nível de campanha


| Nome | Descrição |
| --- | --- |
| daily_budget | O orçamento diário da campanha. |
| lifetime_budget | O orçamento total da campanha. |
| pacing_type | Tipo de regularidade compartilhado entre os conjuntos de anúncios nesta campanha. Opções: standard; no_pacing (também conhecido como veiculação acelerada); day_parting (também conhecido como programação de anúncios) |
| budget_rebalance_flag | Não use para orçamentos de campanha Advantage. Consulte Reequilíbrio do orçamento do conjunto de anúncios abaixo. |
| adset_budgets | O orçamento do conjunto de anúncios que será usado para cada conjunto de anúncios na campanha. Use isso para desabilitar um orçamento de campanha Advantage e utilizar orçamentos individuais de conjuntos de anúncios. |
| bid_strategy | Estratégia de lances da campanha. Opções: LOWEST_COST_WITHOUT_CAP; COST_CAP; LOWEST_COST_WITH_BID_CAP; LOWEST_COST_WITH_MIN_ROAS Se você escolher Value como uma optimization_goal para LOWEST_COST_WITHOUT_CAP no Gerenciador de Anúncios , exibiremos Highest Value como sua estratégia de lance. |
| adset_bid_amounts | Os valores de lances que serão usados para conjuntos de anúncios nesta campanha quando a estratégia de lance da campanha estiver definida para LOWEST_COST_WITH_BID_CAP ou COST_CAP . Você deve definir este campo juntamente com bid_strategy . |


Veja [exemplos](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#examples) abaixo para saber mais sobre como usar esses campos.
[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)

## Controles em nível de conjunto de anúncios


| Nome | Descrição |
| --- | --- |
| daily_min_spend_target | Objetivo diário de gastos mínimos para o conjunto de anúncios, na moeda da sua conta. Você deve especificar um orçamento diário no nível da campanha de anúncios. Esse objetivo não garante que você gaste esse valor, mas o Facebook faz o melhor esforço para alcançá-lo. Para remover daily_min_spend_target de um conjunto de anúncios, defina-o para 0 ou um valor vazio. Por exemplo, daily_min_spend_target=0 ou daily_min_spend_target= . |
| daily_spend_cap | Limite de gastos diário do conjunto de anúncios definido na moeda da sua conta. Você deve especificar o orçamento diário no nível da campanha de anúncios. |
| lifetime_min_spend_target | Objetivo de gasto mínimo total para um conjunto de anúncios definido na moeda da sua conta. Você deve especificar o orçamento total no nível da campanha de anúncios. Esse objetivo não garante que você o alcance, mas o Facebook faz o melhor esforço para atingi-lo. Para remover lifetime_min_spend_target de um conjunto de anúncios, defina-o para 0 ou um valor vazio. Por exemplo, lifetime_min_spend_target=0 ou lifetime_min_spend_target= . |
| lifetime_spend_cap | Limite de gastos total do conjunto de anúncios definido na moeda da sua conta. Você deve especificar o orçamento total na campanha. |
| bid_amount | Valor do lance para este conjunto de anúncios. Ele somente está disponível quando o nível da campanha is_autobid está definido para false . |
| bid_constraints | Semelhante a um orçamento de conjunto de anúncios, lances de retorno mínimo sobre os gastos com anúncios (ou seja, ROAS mínimo, pelas iniciais em inglês) , use-o para fornecer o limite do ROAS , mas não é possível utilizar bid_amount com bid_constraints . Veja Exemplos para usar o ROAS mínimo com um orçamento de campanha Advantage. |


### Exemplos


#### `LOWEST_COST_WITHOUT_CAP`


Crie uma campanha usando um orçamento de campanha Advantage com `bid_strategy` definido para `LOWEST_COST_WITHOUT_CAP`. A campanha tem um orçamento diário de US$ 1.000 com lances automáticos:

```
curl
  -F 'name=L3 With Daily Budget' \
  -F 'objective=OUTCOME_TRAFFIC' \
  -F 'daily_budget=100000' \
  -F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
  -F 'special_ad_categories=NONE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/campaigns
```


#### `LOWEST_COST_WITH_BID_CAP`


Crie uma campanha usando um orçamento de campanha Advantage com `bid_strategy` definido para `LOWEST_COST_WITH_BID_CAP`. A campanha tem um orçamento total de US$ 1.000:

```
curl
  -F 'name=L3 With Lifetime Budget' \
  -F 'objective=OUTCOME_TRAFFIC' \
  -F 'lifetime_budget=100000' \
  -F 'bid_strategy=LOWEST_COST_WITH_BID_CAP' \
  -F 'special_ad_categories=NONE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/campaigns
```


Depois, crie um conjunto de anúncios com o lance máximo limitado:

```
curl \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'name=Test Adset No Budget' \
  -F 'status=ACTIVE' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'targeting={"geo_locations":{"countries":["US"]},"publisher_platforms": ["facebook","audience_network"],"facebook_positions":["feed"],"device_platforms":["mobile","desktop"]}' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=100' \
  -F 'time_stop=1712888798'
  -F 'access_token=<ACCESS_TOKEN>' \
 https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/adsets
```


#### `LOWEST_COST_WITH_MIN_ROAS`


Crie uma campanha usando um orçamento de campanha Advantage com `bid_strategy` definido para `LOWEST_COST_WITH_MIN_ROAS`. Por exemplo, a campanha tem um orçamento total de US$ 1.000 com *ROAS mínimo* definido:

```
curl
  -F 'name=L3 With Lifetime Budget' \
  -F 'objective=OUTCOME_SALES' \
  -F 'lifetime_budget=100000' \
  -F 'bid_strategy=LOWEST_COST_WITH_MIN_ROAS' \
  -F 'special_ad_categories=NONE' \
  -F 'access_token=<ACCESS_TOKEN>' \
 https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/campaigns
```


Depois, crie um conjunto de anúncios com valores mínimos de retorno sobre os gastos com anúncios definidos:

```
curl
  -F 'name=minRoasBiddingDemo' \
  -F 'optimization_goal=VALUE' \
  -F 'promoted_object={"pixel_id": <PIXEL_ID>, "custom_event_type": PURCHASE}' \
  -F 'targeting={"geo_locations":{"countries":["US"]}}' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'status=PAUSED' \
  -F 'time_stop=1712888798' \
  -F 'bid_constraints={"roas_average_floor": 10000}' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)

## Atualize um orçamento de campanha Advantage ou opções de estratégia de lance


Você pode desabilitar um orçamento de campanha Advantage de uma campanha de anúncios e adicionar orçamento aos conjuntos de anúncios. Por exemplo, use o seguinte exemplo de código:


- Remove o orçamento da campanha
- Define o orçamento de `AD_SET_ID1` para `5000`
- Define o orçamento de `AD_SET_ID1` para `7000`

```
curl
 -F 'adset_budgets=[{"adset_id": <AD_SET_ID1>, "daily_budget": 5000}, {"adset_id": <AD_SET_ID2>, "daily_budget": 7000}]'
 -F 'access_token=<ACCESS_TOKEN>'
https://graph.facebook.com/v25.0/CAMPAIGN_ID
```


Ou você pode mudar sua bid_strategy entre `COST_CAP` e `LOWEST_COST_WITH_BID_CAP`. Por exemplo, os seguintes conjuntos de exemplos de código:


- Estratégia de lance para `LOWEST_COST_WITH_BID_CAP`
- O lance de `AD_SET_ID1` para `1500`
- O lance de `AD_SET_ID1` para `2000`

```
curl
 -F 'adset_bid_amounts={"<AD_SET_ID1>": 1500, "<AD_SET_ID2>": 2000}'
 -F 'bid_strategy="LOWEST_COST_WITH_BID_CAP"'
 -F 'access_token=<ACCESS_TOKEN>'
https://graph.facebook.com/v25.0/CAMPAIGN_ID
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)

## Limitações e boas práticas


### Estratégia de lance


Defina uma estratégia de lance no nível da campanha. Todos os conjuntos de anúncios compartilham a mesma estratégia de lance definida no nível da campanha de anúncios. Você ainda pode definir diferentes valores de lance ou valores mínimos de retorno sobre os gastos com anúncios no nível do conjunto de anúncios para campanhas de lances não automáticas. Você pode utilizar essa mesma abordagem para o orçamento do conjunto de anúncios. No momento, para `LOWEST_COST_WITH_MIN_ROAS`, não é possível mudar para outras estratégias de lance depois de criar sua campanha. Consulte [Estratégias de lance](https://developers.facebook.com/docs/marketing-api/bidding-and-optimization#bid-strategy).


### Regularidade


Defina o `pacing_type` no nível da campanha, não no nível do conjunto de anúncios. Consulte [Regularidade e programação](https://developers.facebook.com/docs/marketing-api/pacing).


### Metas de otimização


Todas as metas de otimização devem ser as mesmas nos conjuntos de anúncios que possuem lances automáticos. Depois de veicular anúncios em uma campanha, não é possível editar metas de otimização. Consulte [Metas de otimização](https://developers.facebook.com/docs/marketing-api/bidding-and-optimization#opt).


### Campanhas com mais de 70 conjuntos de anúncios


Se a sua campanha tiver mais de 70 conjuntos de anúncios e utilizar um orçamento de campanha Advantage, você não poderá editar a estratégia de lance atual nem desativar o orçamento da campanha Advantage. [Saiba mais na Central de Ajuda para Empresas](https://www.facebook.com/business/help/519856662172206).
[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)

## Saiba mais


- [Sobre a otimização do orçamento da campanha](https://www.facebook.com/business/help/153514848493595)
- [Entenda os relatórios de CBO ao usar a estratégia de lance de menor custo](https://www.facebook.com/business/help/258714594633281)
[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)[○](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#)Nesta Página[Orçamento de campanha Advantage](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#or-amento-de-campanha-advantage)[Campos em nível de campanha](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#campos-em-n-vel-de-campanha)[Controles em nível de conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#controles-em-n-vel-de-conjunto-de-an-ncios)[Exemplos](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#examples)[Atualize um orçamento de campanha Advantage ou opções de estratégia de lance](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#atualize-um-or-amento-de-campanha-advantage-ou-op--es-de-estrat-gia-de-lance)[Limitações e boas práticas](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#limita--es-e-boas-pr-ticas)[Estratégia de lance](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#estrat-gia-de-lance)[Regularidade](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#regularidade)[Metas de otimização](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#metas-de-otimiza--o)[Campanhas com mais de 70 conjuntos de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#campanhas-com-mais-de-70-conjuntos-de-an-ncios)[Saiba mais](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zMOznQhA2TbXX66ZyMn0aqB3CvawtpDu3HMPB2pnpTQJCTqjj_-BYzZk-5g_aem_6vuV2J9YaT_RBOUCOaVZXg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AXRiIRgDQPK324yTZ6MyFzOZKcgW6kDOOI4mbXVv3lzX6C9jqK6EXUf9ehA_aem_KuxnZeESx3o_EKZgcJSHXQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l1l5ToSCA73C8_Hd7eGc4lcU_lK8krR00sJ0zDqDQQonuYju8XDA3RLBoGA_aem_9QxyT1X3mWvcR-7Q4hoBfg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5s8iaWHEj2ZuAbzqHBdSh7-lH9JAoV8QEkQxeaoDuMinimvkOJTWijpCodFw_aem_yBRzZ5ZG8FxkwjmCM9khfA&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l1l5ToSCA73C8_Hd7eGc4lcU_lK8krR00sJ0zDqDQQonuYju8XDA3RLBoGA_aem_9QxyT1X3mWvcR-7Q4hoBfg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zMOznQhA2TbXX66ZyMn0aqB3CvawtpDu3HMPB2pnpTQJCTqjj_-BYzZk-5g_aem_6vuV2J9YaT_RBOUCOaVZXg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ge0cq9qM25pvHS_8PIW41m767QjEg60-YFNFQsOjpXD2YuSyOswXp9C_t2A_aem_Fd9ERNDM3RK82dB4zQmHMA&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7m7JYdo0Djlm8VqNQQcQZF56OSWPeXvmYxR_SIX_QnnpSMsXEYqWxiHh-Obw_aem_dIpZeg0gTbv33mZVFYwTrQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zMOznQhA2TbXX66ZyMn0aqB3CvawtpDu3HMPB2pnpTQJCTqjj_-BYzZk-5g_aem_6vuV2J9YaT_RBOUCOaVZXg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fiIe1WGkswyJcSO_SShOhTKKnJUMsMwtGYD2WryzjsDgP0HLd4BGWyJhk0A_aem_5gpXSyFhxITG1Adtfyb7gA&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l1l5ToSCA73C8_Hd7eGc4lcU_lK8krR00sJ0zDqDQQonuYju8XDA3RLBoGA_aem_9QxyT1X3mWvcR-7Q4hoBfg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fiIe1WGkswyJcSO_SShOhTKKnJUMsMwtGYD2WryzjsDgP0HLd4BGWyJhk0A_aem_5gpXSyFhxITG1Adtfyb7gA&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7m7JYdo0Djlm8VqNQQcQZF56OSWPeXvmYxR_SIX_QnnpSMsXEYqWxiHh-Obw_aem_dIpZeg0gTbv33mZVFYwTrQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7m7JYdo0Djlm8VqNQQcQZF56OSWPeXvmYxR_SIX_QnnpSMsXEYqWxiHh-Obw_aem_dIpZeg0gTbv33mZVFYwTrQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wnGMQQJSvt9TlkleOO8rlrO0k48J18NDsXKuMJ8BRsCAxfzRpoa5aVvC4-Q_aem_TJ2iLKJur2Ny-g2sViPAMw&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AXRiIRgDQPK324yTZ6MyFzOZKcgW6kDOOI4mbXVv3lzX6C9jqK6EXUf9ehA_aem_KuxnZeESx3o_EKZgcJSHXQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7m7JYdo0Djlm8VqNQQcQZF56OSWPeXvmYxR_SIX_QnnpSMsXEYqWxiHh-Obw_aem_dIpZeg0gTbv33mZVFYwTrQ&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zMOznQhA2TbXX66ZyMn0aqB3CvawtpDu3HMPB2pnpTQJCTqjj_-BYzZk-5g_aem_6vuV2J9YaT_RBOUCOaVZXg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6vVcfVPeSpUWFfuHN4hE7bijip40Ru3a7jlkce-hPrWRFuYapOtfN8QjNQWA_aem_HttpfRwQwooXPZaOdg3AQA&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zMOznQhA2TbXX66ZyMn0aqB3CvawtpDu3HMPB2pnpTQJCTqjj_-BYzZk-5g_aem_6vuV2J9YaT_RBOUCOaVZXg&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xqg1myhbtYoLMOdeVc18TqQJY4WeZd02EGh0j8CR69xXXVb9-Vef4MGUsgklGjUoN4lzK9Gz_E8ZY153YcxAx3u_rU1F1X8Pn2p852MoZhTFoaUZbH-KuXiGvZVmFHLYbACkIDtgZUzOeI8SD5lysi_Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão