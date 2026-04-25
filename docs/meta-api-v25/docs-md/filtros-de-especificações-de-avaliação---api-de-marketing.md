<!-- Fonte: Filtros de especificações de avaliação - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Filtros de especificações de avaliação


É possível usar tipos mais avançados de campos de filtro nas regras baseadas em horários.


## Campos de insights prefixados


Você pode definir tipos específicos de prefixos para filtros de insights. Isso é semelhante aos prefixos definidos em filtros de metadados usados para realizar uma filtragem multinível.


Você pode definir um prefixo de nível de objeto em um filtro para aproveitar a filtragem multinível de insights. Por exemplo, uma regra de anúncios pode ser filtrada por conjunto de anúncios ou desempenho da campanha. Você também pode especificar os prefixos de janela de atribuição e predefinição de tempo em um filtro. Isso é usado para substituir a janela de atribuição e a predefinição de tempo da regra nesse filtro específico.


### Uso


Os prefixos são opcionais. Um campo pode ter:


- um prefixo de nível de objeto
- um prefixo de janela de atribuição
- um prefixo de predefinição de tempo


Você pode ter todas as opções acima, nenhuma ou qualquer combinação, desde que as mantenha nessa ordem. O campo deve ter o seguinte formato:


{ `object_level_prefix?` } {`attribution_window_prefix?`} { `time_preset_prefix?` } { `field_name` }


Abaixo, veja exemplos corretos e incorretos de campos de insights prefixados. Também mostramos exemplos corretos e incorretos de campos de metadados prefixados para você saber quais filtros são aceitos.


##### Exemplos para o campo de insights `spent`


###### Bons exemplos

✓

`adset.yesterday_spent`: valor total gasto no nível do conjunto de anúncios referente ao dia anterior.
✓

`adset.spent`: valor total gasto no nível do conjunto de anúncios.
✓

`yesterday_spent`: valor total gasto referente ao dia anterior.
✓

`campaign.28d_view_1d_click:lifetime_results`: resultados totais no nível do conjunto de anúncios durante a respectiva vida útil, com janela de atribuição de 28 dias após a visualização e 1 dia após o clique.
✓

`campaign.lifetime_spent`: valor total gasto no nível da campanha de anúncios durante a respectiva vida útil.


###### Maus exemplos

✗

`lifetime_campaign.spent`: os prefixos de predefinição de tempo não podem aparecer antes dos prefixos de nível de objeto.
✗

`lifetime_today_spent`: não pode haver dois prefixos de predefinição de tempo.
✗

`ad.adset.spent`: não pode haver dois prefixos de nível de objeto.
✗

`yesterday.adset_spent`: delimitador incorreto.


##### Exemplos para o campo de metadados `daily_budget`


###### Bons exemplos

✓

`adset.daily_budget`: orçamento diário do conjunto de anúncios.
✓

`daily_budget`: orçamento diário.


###### Maus exemplos

✗

`yesterday_daily_budget`: não é possível usar prefixos de predefinição de tempo nos campos de metadados.
✗

`ad.daily_budget`: os anúncios não têm um orçamento diário.


### Prefixos de nível de objeto


| Prefixo | Tipo de objeto | Válido para tipos de objetos |
| --- | --- | --- |
| ad. | Anúncio | Anúncio |
| adset. | Conjunto de anúncios | Anúncio, conjunto de anúncios |
| campaign. | Campanha | Anúncio, conjunto de anúncios, campanha |


### Prefixos de janela de atribuição


| Prefixo de janela de atribuição | Descrição |
| --- | --- |
| account_default: | Use a configuração da janela de atribuição do nível da conta. |
| default: | A janela de atribuição padrão do Facebook é visualizações de 1 dia, cliques de 28 dias. |
| inline: | Apenas atribuição inline (visualizações de 0 dia, cliques de 0 dia) |
| 1d_view: | Visualizações de 1 dia, cliques de 0 dia |
| 7d_view: | Visualizações de 7 dias, cliques de 0 dia |
| 28d_view: | Visualizações de 28 dias, cliques de 0 dia |
| 1d_click: | Visualizações de 0 dia, cliques de 1 dia |
| 7d_click: | Visualizações de 0 dia, cliques de 7 dias |
| 28d_click: | Visualizações de 0 dia, cliques de 28 dias |
| 1d_view_1d_click: | Visualizações de 1 dia, cliques de 1 dia |
| 7d_view_1d_click: | Visualizações de 7 dias, cliques de 1 dia |
| 28d_view_1d_click: | Visualizações de 28 dias, cliques de 1 dia |
| 1d_view_7d_click: | Visualizações de 1 dia, cliques de 7 dias |
| 7d_view_7d_click: | Visualizações de 7 dias, cliques de 7 dias |
| 28d_view_7d_click: | Visualizações de 28 dias, cliques de 7 dias |
| 7d_view_28d_click: | Visualizações de 7 dias, cliques de 28 dias |
| 28d_view_28d_click: | Visualizações de 28 dias, cliques de 28 dias |


### Prefixos de predefinição de tempo


Esta é a mesma lista de valores válidos de predefinição de tempo, mas em minúsculas e com um delimitador anexado.


| Prefixo | Descrição |
| --- | --- |
| lifetime_ | Vida útil do objeto |
| today_ | O dia atual começa a partir da meia-noite no fuso horário da conta de anúncios |
| last_2_days_ | YESTERDAY e TODAY |
| last_3_days_ | Últimos 2 dias inteiros e TODAY |
| last_7_days_ | Últimos 6 dias inteiros e TODAY |
| last_14_days_ | Últimos 13 dias inteiros e TODAY |
| last_28_days_ | Últimos 27 dias inteiros e TODAY |
| last_30_days_ | Últimos 29 dias inteiros e TODAY |
| this_month_ | Este mês, incluindo TODAY |
| this_week_mon_today_ | Esta semana usando a segunda-feira como primeiro dia da semana, incluindo TODAY |
| this_week_sun_today | Esta semana usando o domingo como primeiro dia da semana, incluindo TODAY |
| yesterday_ | O dia inteiro anterior, excluindo TODAY |
| last_2d_ | Últimos 2 dias inteiros, excluindo TODAY |
| last_3d_ | Últimos 3 dias inteiros, excluindo TODAY |
| last_7d_ | Últimos 7 dias inteiros, excluindo TODAY |
| last_14d_ | Últimos 14 dias inteiros, excluindo TODAY |
| last_28d_ | Últimos 28 dias inteiros, excluindo TODAY |
| last_30d_ | Últimos 30 dias inteiros, excluindo TODAY |
| last_nd_14_8_ | Últimos 14 dias até os últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_30_8_ | Últimos 30 dias até os últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_60_8_ | Últimos 60 dias até os últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_120_8_ | Últimos 120 dias até aos últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_180_8_ | Últimos 180 dias até os últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_lifetime_8_ | Vida útil até os últimos 7 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_60_29_ | Últimos 60 dias até os últimos 28 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_120_20_ | Últimos 120 dias até os últimos 28 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_180_29_ | Últimos 180 dias até os últimos 28 dias para retorno sobre o investimento em publicidade (ROAS) |
| last_nd_lifetime_29_ | Vida útil até os últimos 28 dias para retorno sobre o investimento em publicidade (ROAS) |

[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#)

## Agregação


Você pode agregar alguns campos de insights em vários objetos de anúncio. Isso permite criar filtros nas métricas de um subconjunto específico de objetos de anúncio. Por exemplo, o alcance total de vários anúncios ou o número total de cliques em diferentes conjuntos de anúncios.


Enquanto algumas métricas (como `clicks`) são calculadas com uma soma simples, outras (como `reach`) são calculadas de forma diferente. Uma vez que `reach` é baseado em impressões únicas, os usuários duplicados são removidos da agregação em vários objetos de anúncio.


### Uso


Um campo agregado tem este formato: `aggregate(`{ `field` }`)`. O `field` pode conter os prefixos de janela de atribuição e de predefinição de tempo. O conjunto de objetos de anúncio a serem agregados é determinado por outro campo de filtro obrigatório `aggregation_id`.


#### Exemplo de campos agregados


##### Bons exemplos

✓

`aggregate(reach)`
✓

`aggregate(lifetime_reach)`


##### Maus exemplos

✗

`aggregate(daily_budget)`
✗

`aggregate(adset.reach)`


### Filtro de identificação de agregação


O filtro `aggregation_id` especifica quais objetos de anúncio devem ser agregados. Ele só aceita o operador `IN` e uma lista de identificações como valor. As identificações podem ser de anúncios, conjuntos de anúncios ou campanhas, mas todas devem ser do mesmo nível de objeto.


#### Exemplo de filtro `aggregation_id`


```
{
  "field": "aggregation_id",
  "operator": "IN",
  "value": [1234, 5678]
},
{
  "field": "aggregate(reach)",
  "operator": "GREATER_THAN",
  "value": 100
}
```


### Campos aceitos


- `clicks`
- `cpc`
- `cpm`
- `cpp`
- `ctr`
- `frequency`
- `impressions`
- `mobile_app_purchase_roas`
- `reach`
- `result_rate`
- `spent`
- `unique_clicks`
- `unique_impressions`
- `website_purchase_roas`
- `cost_per_unique_click`
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#)

## Campos de fórmula


Você pode definir expressões aritméticas simples como um campo. Por exemplo, é possível usar essa opção para encontrar a razão entre dois campos numéricos.


Isso funciona em campos de insights e em um subconjunto de campos numéricos de metadados. Confira a lista completa de valores aceitos abaixo.


### Uso


Um campo de fórmula consiste em campos ou constantes e operadores sintaticamente corretos separados por espaços. Ele é compatível com os operadores `+``-``*` e `/`. Você pode adicionar constantes, por exemplo, para pesar campos específicos ou fazer compensações.


Neste caso, os campos podem ser totalmente prefixados para que você possa adicionar prefixos válidos de nível de objeto e predefinição de tempo.


No momento, permitimos o uso de até `6` campos não constantes em uma fórmula. Você pode ter quantas constantes quiser.


`today_spent / adset.today_spent`


`0.8 * cpc + 0.2 * cpm`


{ `field_or_constant_1` } { `+` | `-` | `*` | `/` } { `field_or_constant_2` }


#### Exemplos de fórmulas


###### Bons exemplos

✓

`today_spent / adset.daily_budget`: porcentagem de gastos diários.
✓

`clicks / adset.clicks`: razão entre cliques e cliques do conjunto de anúncios.
✓

`today_impressions / yesterday_impressions`: razão entre o número de impressões do dia atual e o número de impressões do dia anterior.
✓

`today_impressions / aggregate(today_impressions)`: razão entre o número de impressões do dia atual e o número agregado de impressões.
✓

`(adset.spent - spent)`: é permitido usar parênteses; as fórmulas recebidas nas respostas da API serão colocadas entre parênteses.


###### Maus exemplos

✗

`(clicks + cpc + cpm + ctr + cpa + cpp) / cost_per`: não é possível usar mais do que `6` campos.
✗

`today_impressions/yesterday_impressions`: os termos devem ser separados por espaço.


### Campos numéricos válidos de metadados


| Campo | Válido para tipos de objetos |
| --- | --- |
| bid_amount | Anúncio, conjunto de anúncios |
| daily_budget | Conjunto de anúncios |
| lifetime_budget | Conjunto de anúncios |
| spend_cap | Campanha |

[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#)Nesta Página[Filtros de especificações de avaliação](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#filtros-de-especifica--es-de-avalia--o)[Campos de insights prefixados](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#campos-de-insights-prefixados)[Uso](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#uso)[Prefixos de nível de objeto](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#prefixos-de-n-vel-de-objeto)[Prefixos de janela de atribuição](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#prefixos-de-janela-de-atribui--o)[Prefixos de predefinição de tempo](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#prefixos-de-predefini--o-de-tempo)[Agregação](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#agrega--o)[Uso](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#uso-2)[Filtro de identificação de agregação](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#filtro-de-identifica--o-de-agrega--o)[Campos aceitos](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#campos-aceitos)[Campos de fórmula](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#campos-de-f-rmula)[Uso](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#uso-3)[Campos numéricos válidos de metadados](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/evaluation-spec-filters#campos-num-ricos-v-lidos-de-metadados) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ylpy2hfot3pq2Ftz8_IBPMbo9-XyVmWH8jGu4IuOzJJEFS7QqFtZRERAffg_aem_nVuUxkR4YOpeDCp3NicVGg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5EdhO2Q25dtRR_9m_v5GTzcUbjElRBFPO6oUsOEwvt78UBRlCAJxpMOiqCbQ_aem_UxsG-hGDnesGVDHAQzA3MA&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Z-G9E_3BofGJ0vl-2MDuESmj917r5b8P1lheX_ij4BOmmoIkPvWKgY7Wjyw_aem_b9cixAfLuFqwPzUuIpM3xg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6cHsJpgTKmzdrh_MVuQl-mBQBOUImqnrJ-6oTX1C6xGz7pGZMDQJ7r5X5unA_aem_5IDpXgTiW3483nL-wtCgoQ&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Z-G9E_3BofGJ0vl-2MDuESmj917r5b8P1lheX_ij4BOmmoIkPvWKgY7Wjyw_aem_b9cixAfLuFqwPzUuIpM3xg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4x_cAFnXK3OC-Mf0Q72P2SnAzyE02dbQs7B0Ijo0a7JmkyQksqzNLX_AZang_aem_g0c-09h7WMk0XH4-jwMpbw&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BptLHu6-C8Sv1mF1ob2Amr2oEbyNK90pInZulfX-L-2gAgrPfkTPwyzxP_w_aem_EJgINZvLnvi6bYXwLcLQ1g&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4x_cAFnXK3OC-Mf0Q72P2SnAzyE02dbQs7B0Ijo0a7JmkyQksqzNLX_AZang_aem_g0c-09h7WMk0XH4-jwMpbw&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BptLHu6-C8Sv1mF1ob2Amr2oEbyNK90pInZulfX-L-2gAgrPfkTPwyzxP_w_aem_EJgINZvLnvi6bYXwLcLQ1g&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mq_h3qsQv1rmvRNBnBnOwtS7rlqkc5Z18UBUiEloMKDjiH_DipTMf1YoPxg_aem_kCo_UvI0tCsyyNub75wXlw&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5EdhO2Q25dtRR_9m_v5GTzcUbjElRBFPO6oUsOEwvt78UBRlCAJxpMOiqCbQ_aem_UxsG-hGDnesGVDHAQzA3MA&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BptLHu6-C8Sv1mF1ob2Amr2oEbyNK90pInZulfX-L-2gAgrPfkTPwyzxP_w_aem_EJgINZvLnvi6bYXwLcLQ1g&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BptLHu6-C8Sv1mF1ob2Amr2oEbyNK90pInZulfX-L-2gAgrPfkTPwyzxP_w_aem_EJgINZvLnvi6bYXwLcLQ1g&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7odyAnH7pU0cAmIRIZtBBzI4A-LPWXiW5P3uEt21sbp8gPFXleYlGkV6x63g_aem_gDIiHk244haj0xAb1HpfMA&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ylpy2hfot3pq2Ftz8_IBPMbo9-XyVmWH8jGu4IuOzJJEFS7QqFtZRERAffg_aem_nVuUxkR4YOpeDCp3NicVGg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mq_h3qsQv1rmvRNBnBnOwtS7rlqkc5Z18UBUiEloMKDjiH_DipTMf1YoPxg_aem_kCo_UvI0tCsyyNub75wXlw&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4x_cAFnXK3OC-Mf0Q72P2SnAzyE02dbQs7B0Ijo0a7JmkyQksqzNLX_AZang_aem_g0c-09h7WMk0XH4-jwMpbw&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7-Yq7X4m2tqxAJ7Cff0bq5Q-Db_u2o-HazKdq-IdqhtV-TCTel12Y-KUAq9A_aem_Sja6Sjp8yLN3Nb9tk49mtg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ClMq36h1k7Cy9HoOMy5hnlA57QtDFYuslAf6cvfpRFdVmtABawcmRFDHDzA_aem_X3_BMISSkLiZai8j3njiNg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7-Yq7X4m2tqxAJ7Cff0bq5Q-Db_u2o-HazKdq-IdqhtV-TCTel12Y-KUAq9A_aem_Sja6Sjp8yLN3Nb9tk49mtg&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT77uHsoHSmTzejwtr2jgYcbbPWwcJLe2EG3RU2Iz-N2TmE4CfvoqDxjoMg2b7Ef6FduJgvYB_uNNMUNxlvzvw1MC5TTlXAk6ObFIGbAlG2yIwJDU50JSlVDZSEwlFMRbJH8BmvK3a5EXEXgvaD0sb6diIY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão