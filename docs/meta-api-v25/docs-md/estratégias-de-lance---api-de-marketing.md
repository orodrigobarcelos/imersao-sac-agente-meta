<!-- Fonte: Estratégias de lance - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Estratégia de lance


Devido ao lançamento do iOS 14.5, as seguintes mudanças foram feitas:


- A estratégia de lance `target_cost` ficou obsoleta a partir da [versão 9.0 da API de Marketing](https://developers.facebook.com/docs/graph-api/changelog/version9.0). Não haverá mais compatibilidade com as campanhas que usarem essa estratégia de lance. Nesse caso, a veiculação será pausada. Em vez de `target_cost`, recomendamos usar [lances com limite de custo](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#cap).
- As campanhas do iOS 14.5 que usarem `COST_CAP` ou `LOWEST_COST_WITH_MIN_ROAS` deverão ter uma duração mínima de 3 dias.


Consulte nosso [registro de alterações](https://developers.facebook.com/docs/graph-api/changelog/non-versioned-changes/jan-19-2021) para saber mais sobre as mudanças do iOS 14.5.


Esta página explica como as estratégias de lance afetam seu lance e os controles de custo sobre os anúncios da Meta e descreve como configurá-las.


### Tipos de estratégia de lance


- `LOWEST_COST_WITHOUT_CAP`: o Facebook dá um lance automático em seu nome e obtém os resultados de menor custo para você. É possível aumentar automaticamente seu lance efetivo conforme necessário para obter os resultados desejados com base na sua `optimization_goal`. Se você definir `Value` como uma `optimization_goal`, no [Gerenciador de Anúncios](https://www.facebook.com/ads/manager/accounts), exibiremos `Highest Value` como sua estratégia de lance.
- [`COST_CAP`](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#cap): obtenha o melhor resultado possível enquanto nos esforçamos para manter o custo por ação definido por você. **Observação**: a adesão ao limite de custo não é garantida. Consulte [Limite de custo](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#cap).
- [`LOWEST_COST_WITH_MIN_ROAS`](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#min-roas-bidding): opção de lances específica para otimização de valor. Você precisa especificar um `roas_average_floor`, que representa o retorno mínimo desejado sobre o investimento em publicidade. Consulte [Lances de retorno mínimo sobre o investimento em anúncios](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#min-roas-bidding).
- `LOWEST_COST_WITH_BID_CAP`: damos lances automáticos por você e obtemos os menores custos. Aumentamos automaticamente seu lance conforme necessário para obter os resultados desejados. Porém, não ultrapassamos o limite especificado por você.


Consulte a tabela abaixo para saber mais sobre cada estratégia:


| Estratégia de lance | Objetivos compatíveis | Quando usar | Considerações |
| --- | --- | --- | --- |
| LOWEST_COST_WITHOUT_CAP | APP_INSTALLS CONVERSIONS EVENT_RESPONSES LEAD_GENERATION Consulte a tabela abaixo para saber mais sobre cada estratégia: LINK_CLICKS MESSAGES PAGE_LIKES POST_ENGAGEMENT PRODUCT_CATALOG_SALES REACH STORE_VISITS VIDEO_VIEWS | Você quer gastar todo o seu orçamento. Você precisa saber que lance e custo usar para outras opções de lance. Você precisa gastar seu orçamento com a maior eficiência possível. | Não há controle sobre o custo. Os custos podem aumentar à medida que você esgota as oportunidades mais baratas ou aumenta seu orçamento. |
| COST_CAP | APP_INSTALLS CONVERSIONS EVENT_RESPONSES LEAD_GENERATION LINK_CLICKS MESSAGES PAGE_LIKES POST_ENGAGEMENT PRODUCT_CATALOG_SALES VIDEO_VIEWS | Você quer maximizar os resultados controlando a relação custo-benefício do custo médio por conversão. As campanhas do iOS 14.5 precisam ter duração de 3 dias. | Os custos podem aumentar conforme você esgota as oportunidades mais baratas. O orçamento não pode ser gasto depois que o limite é atingido. |
| LOWEST_COST_WITH_MIN_ROAS | APP_INSTALLS CONVERSIONS PRODUCT_CATALOG_SALES | Se o retorno sobre o investimento em anúncios (ROAS) for a principal medida de sucesso e você puder repassar os valores de transação à nossa plataforma. | Específico para otimização de valor. Configurar a referência com um valor muito alto pode causar veiculação insuficiente. As campanhas do iOS 14.5 precisam ter duração de 3 dias. |
| LOWEST_COST_WITH_BID_CAP | APP_INSTALLS CONVERSIONS EVENT_RESPONSES LEAD_GENERATION LINK_CLICKS MESSAGES PAGE_LIKES POST_ENGAGEMENT PRODUCT_CATALOG_SALES REACH STORE_VISITS VIDEO_VIEWS | Você quer definir um lance máximo para vários leilões a fim de controlar custos e alcançar o máximo possível de usuários com o lance. | É necessário dedicar mais tempo com o gerenciamento de lances para controlar os custos. Os custos podem aumentar à medida que você esgota as oportunidades mais baratas ou aumenta seu orçamento. O orçamento não pode ser esgotado. O lance não é o custo exibido nos relatórios. |


`LOWEST_COST_WITH_MIN_ROAS`, `COST_CAP` e `LOWEST_COST_WITH_BID_CAP` também são chamados de *lances manuais* e permitem incluir controles de custo adicional. Para obter informações básicas, consulte [Sobre o volume mais alto](https://www.facebook.com/business/help/721453268045071).


Para ler `bid_strategy` de um conjunto de anúncios:

```
curl -G \
  -d 'fields=bid_strategy' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<AD_SET_ID>
```


Para atualizar a estratégia de lance de um conjunto de anúncios para `LOWEST_COST_WITH_BID_CAP` com um limite de lance de US$ 3:

```
curl
  -F 'bid_strategy=LOWEST_COST_WITH_BID_CAP' \
  -F 'bid_amount=300' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<AD_SET_ID>
```


Nas versões anteriores da API, você definia `is_autobid`, `is_average_price_pacing` e `bid_amount` para escolher a estratégia de lance.


Os sinalizadores boolianos `is_autobid` e `is_average_price_pacing` indicavam se você havia escolhido a opção de lance automático ou lances de custo médio. As duas estratégias ficaram obsoletas a partir do lançamento da [versão 3.0 da API de Marketing](https://developers.facebook.com/docs/graph-api/changelog/version3.0/#mapi-break).


## Limite de custo


O limite de custo é um recurso de lance baseado em custo que permite aos anunciantes expressar e otimizar em relação ao custo real (CPA/CPI) das conversões. Com essa ferramenta, os anunciantes podem obter os melhores resultados possíveis enquanto nos esforçamos para manter o custo desejado. Assim, é possível maximizar a eficiência dos custos, reduzir as complexidades do gerenciamento de lances e ajudar os anunciantes a expandir com confiança e de modo mais lucrativo. **Observação**: a adesão ao limite de custo não é garantida.


Para usar o limite de custo:


- `billing_event` deve ser `IMPRESSIONS`
- `pacing_type` deve ser padrão
- `optimization_goal` deve ser compatível com o limite de custo


Para usar uma estratégia de lances de limite de custo na otimização do orçamento da campanha, além dos requisitos listados acima, seu objetivo também precisa funcionar com limite de custo. Para mais informações sobre objetivos compatíveis, veja [Seu guia para estratégias de lance no Facebook, Limite de custo](https://www.facebook.com/business/m/one-sheeters/facebook-bid-strategy-guide).


Por exemplo, para usar um limite de custo no nível da campanha de anúncios:

```
curl
 -F "name"="L3 With Lifetime Budget" \
 -F "objective"="LINK_CLICKS" \
 -F "lifetime_budget=100000" \
 -F "bid_strategy"="COST_CAP" \
 -F "access_token"="ACCESS_TOKEN" \
https://graph.facebook.com/VERSION/AD_ACCOUNT_ID/campaigns
```


Para definir um limite de custo no nível do conjunto de anúncios:

```
curl \
  -F 'name=My Ad Set' \
  -F 'optimization_goal=CONVERSIONS' \
  -F 'billing_event=IMPRESSIONS'-F 'bid_strategy=COST_CAP'-F 'bid_amount=200' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={"geo_locations":{"countries":["US"]}}' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#)

## Lances de retorno mínimo sobre o investimento em anúncios (ROAS mínimo)


Esta é uma opção específica de lances para otimização de valor. Assim, você já deve estar qualificado para otimização de valor, que tem vários pré-requisitos:


- `optimization_goal` precisar ser `VALUE`.
- A conta deve ter acesso à otimização de valor, que pode ser consultada na sua conta de anúncios: - `CAN_USE_ROAS_VALUE_OPTIMIZATION` – a conta estará qualificada para otimização de valor quando o objetivo de campanha for = `“Website Conversion”` - `ADS_NEKO_MAI_ROAS` – a conta estará qualificada para otimização de valor quando o objetivo de campanha for = `“App Install”` - `CAN_USE_DYNAMIC_ADS_VALUE_OPTIMIZATION` – a conta estará qualificada para otimização de valor quando o objetivo de campanha for = `“Catalog Sales”`
- Os lances de ROAS mínimo usam `bid_constraints` para passar o `“ROAS floor”`, mas ele não pode ser usado com `bid_constraints`. Em vez disso, use `roas_average_floor`.


### Especificação da API em [Conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign)


Notas sobre `roas_average_floor`:


- `roas_average_floor` representa `“the mininum roas” = “total conversion purchase value” / “total spend”`. Por exemplo, `“return on ads spend”`
- **IMPORTANTE**: na API, `roas_average_floor` é um número inteiro e aumentado 10.000 vezes. Então, `roas_average_floor = 100` significa “o roas mínimo” = 0,01 (ou 1%), e `roas_average_floor = 23300` significa “o roas mínimo” = 2,33 (ou 233%). Por exemplo, para definir o ROAS mínimo como `1.5`, a especificação correspondente da API deve ser `bid_constraints = {"roas_average_floor": 15000}`.
- O intervalo válido de `roas_average_floor` é `[100, 10000000]`, incluso. Isso significa que o intervalo válido de “ROAS mínimo” é `[0.01, 1000.0]` ou `[1%, 100000.0%]`, incluso.
- Não defina `bid_info` nem `bid_amount` com o conjunto de anúncios de lances de ROAS mínimo. Você pode definir somente o `'bid'` do ROAS mínimo por meio de `roas_average_floor` em `bid_constraints`.

```
{
  "bid_strategy": "LOWEST_COST_WITH_MIN_ROAS",
  "bid_constraints": {
    "roas_average_floor": <roas_average_floor number>
  },
}
```


### Exemplos


#### Criar um novo conjunto de anúncios de lances mínimos


A chamada de API abaixo cria um conjunto de anúncios de lances de ROAS mínimo, com objetivo da campanha = "conversão no site" e limite mínimo de ROAS = `1.0` (ou 100%).

```
curl \
  -F 'name=minRoasBiddingDemo' \
  -F 'daily_budget=2000' \
  -F 'optimization_goal=VALUE' \
  -F 'promoted_object={"pixel_id": "<PIXEL_ID>", "custom_event_type": "PURCHASE"}' \
  -F 'targeting={"geo_locations":{"countries":["US"]}}' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'status=PAUSED' \
  -F 'start_time=2018-12-10T12:45:26-0700' \
  *-F 'bid_strategy=LOWEST_COST_WITH_MIN_ROAS' \
  -F 'bid_constraints={"roas_average_floor": 10000}' \*
  -F 'billing_event=IMPRESSIONS' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/adsets
```


#### Remover `roas_average_floor` do conjunto de anúncios de lances de ROAS mínimo


```
curl \
  -F bid_strategy=LOWEST_COST_WITHOUT_CAP \
  -F 'bid_constraints={}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/<ad set ID>
```


#### Adicionar `roas_average_floor` ao conjunto de anúncios de otimização de valor


Este exemplo define o ROAS mínimo como `1.23` (123%):

```
curl \
  -F 'bid_strategy=LOWEST_COST_WITH_MIN_ROAS' \
  -F 'bid_constraints={"roas_average_floor": 12300}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/<ad set ID>
```


#### Alterar `roas_average_floor` para o conjunto de anúncios de lances existente de ROAS mínimo


Esta chamada de API muda o `roas_average_floor` do conjunto de anúncios para `2.23` (223%).

```
curl \
  -F 'bid_constraints={"roas_average_floor": 22300}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/<ad set ID>
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#)

## Validação no nível do conjunto de anúncios


- `LOWEST_COST_WITH_BID_CAP` também é chamado de lance manual e permite incluir controles de custo adicionais no campo `bid_amount`.
- Para `COST_CAP`, é necessário fornecer um número de limite no campo `bid_amount`.
- Não será possível definir `bid_amount` se você usar a estratégia `LOWEST_COST_WITH_MIN_ROAS`.
[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#)[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#)Nesta Página[Estratégia de lance](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#estrat-gia-de-lance)[Limite de custo](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#cap)[Lances de retorno mínimo sobre o investimento em anúncios (ROAS mínimo)](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#min-roas-bidding)[Especificação da API em Conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#especifica--o-da-api-em-conjunto-de-an-ncios)[Exemplos](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#exemplos)[Validação no nível do conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy#bid-strategy-ad-sets) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6NNhNi1xvciSf71CUbALXbBvZnpdrcAA7RHrUHwjxCPSQb9wAY3AJp8amQ0g_aem_TsbgsSHnxP5j-scsH5FkPQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xgX3rTUNXK5PaSYMK-NxxtwAAKYeUqDzd_cyCAxao4dqmhfkKGa3yVBuKAQ_aem_cQ0r08fkfcXGmhNdwj_KLA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6cmjW4kZI24CqSFGk2-CA6C8lIYKpmHz9r69jW7kJkPnyLuiRPYlqVyRB3uQ_aem_-sYNzSpf252j1o0TwnmYcA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR73ZS6NbjyNHkns5aAAJg0RC1m92AJhIwPmn_35XKS6WLK8nQvq7XRDDlQrsA_aem_b_5UVah5vn6XVJlxweKlXA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xgX3rTUNXK5PaSYMK-NxxtwAAKYeUqDzd_cyCAxao4dqmhfkKGa3yVBuKAQ_aem_cQ0r08fkfcXGmhNdwj_KLA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wxKyqgcy4qT5yRcO5LHIZ8ZoMd8i1j3Qfbs7W2CxKKZf7MMoFXoGkrYszwQ_aem_bAHBlSpJB_AoU7QaJnoESw&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR73ZS6NbjyNHkns5aAAJg0RC1m92AJhIwPmn_35XKS6WLK8nQvq7XRDDlQrsA_aem_b_5UVah5vn6XVJlxweKlXA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xkBlHBTjLTTwJLP-DQ0Q6o9GldFWQOuft9WQzYh-W3Z7xkpltdWfq0nPRWQ_aem_oN9GbWjfZW-54p2YSdS-iQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59mn4wTxCTJRYq0JG9ylngcsiB64NcAoWDFy12ctEz9B31oKzuJ1ND0xn4wA_aem_Xn5EAq0OLIOTAOd2gvKgVA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59mn4wTxCTJRYq0JG9ylngcsiB64NcAoWDFy12ctEz9B31oKzuJ1ND0xn4wA_aem_Xn5EAq0OLIOTAOd2gvKgVA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xkBlHBTjLTTwJLP-DQ0Q6o9GldFWQOuft9WQzYh-W3Z7xkpltdWfq0nPRWQ_aem_oN9GbWjfZW-54p2YSdS-iQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xkBlHBTjLTTwJLP-DQ0Q6o9GldFWQOuft9WQzYh-W3Z7xkpltdWfq0nPRWQ_aem_oN9GbWjfZW-54p2YSdS-iQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xgX3rTUNXK5PaSYMK-NxxtwAAKYeUqDzd_cyCAxao4dqmhfkKGa3yVBuKAQ_aem_cQ0r08fkfcXGmhNdwj_KLA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wxKyqgcy4qT5yRcO5LHIZ8ZoMd8i1j3Qfbs7W2CxKKZf7MMoFXoGkrYszwQ_aem_bAHBlSpJB_AoU7QaJnoESw&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6NNhNi1xvciSf71CUbALXbBvZnpdrcAA7RHrUHwjxCPSQb9wAY3AJp8amQ0g_aem_TsbgsSHnxP5j-scsH5FkPQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wxKyqgcy4qT5yRcO5LHIZ8ZoMd8i1j3Qfbs7W2CxKKZf7MMoFXoGkrYszwQ_aem_bAHBlSpJB_AoU7QaJnoESw&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hgJVR6ec_yrn-JDzAbTfvwcDGL1NzoXvmRqsvBFtcn0FGzYqBLFbXwkSpdw_aem_iMxvia3eO7DJ2o-_AwWJzQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hgJVR6ec_yrn-JDzAbTfvwcDGL1NzoXvmRqsvBFtcn0FGzYqBLFbXwkSpdw_aem_iMxvia3eO7DJ2o-_AwWJzQ&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR73ZS6NbjyNHkns5aAAJg0RC1m92AJhIwPmn_35XKS6WLK8nQvq7XRDDlQrsA_aem_b_5UVah5vn6XVJlxweKlXA&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wxKyqgcy4qT5yRcO5LHIZ8ZoMd8i1j3Qfbs7W2CxKKZf7MMoFXoGkrYszwQ_aem_bAHBlSpJB_AoU7QaJnoESw&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4Dp_CQ_PpRDJlXYK6W0-NANIbWcS0LmC9pxTbTDnaIwHkWhiAZui1d3-x-E96iChvEnUBQA0Tnq2KFKtxdPFC4H1TRUOguxdw4dBIBqUZxJwCJr4Lhf8JAt24HoyvV7Ub8YwxZY65bq4JBgQv9CBHybj4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão