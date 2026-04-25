<!-- Fonte: API de Insights - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/insights -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# API de Insights


Fornece uma interface única e consistente para recuperar estatísticas de anúncios.


- [Detalhamentos](https://developers.facebook.com/docs/marketing-api/insights/breakdowns): resultados de grupo.
- [Detalhamentos de ação](https://developers.facebook.com/docs/marketing-api/insights/action-breakdowns): entender a resposta dos detalhamentos de ação.
- [Trabalhos assíncronos](https://developers.facebook.com/docs/marketing-api/insights/async): para solicitações com grandes resultados, use trabalhos assíncronos.
- [Limites e melhores práticas](https://developers.facebook.com/docs/marketing-api/insights/best-practices/): limites de chamada, filtragem e boas práticas.


Para receber dados de desempenho, configure seus anúncios para rastrear as métricas que são importantes para você. Para isso, você pode usar as [tags de URL](https://developers.facebook.com/docs/reference/ads-api/adcreative), o [Pixel da Meta](https://developers.facebook.com/docs/marketing-api/audiences-api/pixel) e a [API de Conversões](https://developers.facebook.com/docs/marketing-api/conversions-api).


## Antes de começar


Você precisará do seguinte:


- A permissão `ads_read`.
- Um [app](https://developers.facebook.com/apps/). Consulte [Desenvolvimento de apps da Meta](https://developers.facebook.com/docs/development) para saber mais.
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Estatísticas de campanha


Para consultar as estatísticas de desempenho dos últimos 7 dias de uma campanha:

```
curl -G \
  -d "date_preset=last_7d" \
  -d "access_token=ACCESS_TOKEN" \
  "https://graph.facebook.com/API_VERSION/AD_CAMPAIGN_ID/insights"
```


Para saber mais, consulte a [referência de Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/insights).
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Chamadas


A API de Insights está disponível como uma borda em qualquer objeto de anúncios.


| Método de API |
| --- |
| act_\<AD_ACCOUNT_ID\>/insights |
| \<CAMPAIGN_ID\>/insights |
| \<ADSET_ID\>/insights |
| \<AD_ID\>/insights |


### Solicitação


Você pode solicitar campos específicos com uma lista separada por vírgulas nos parâmetros `fields`. Por exemplo:

```
curl -G \
-d "fields=impressions" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/<AD_ID>/insights"
```


### Resposta


```
{
  "data": [
    {
      "impressions": "2466376",
      "date_start": "2009-03-28",
      "date_stop": "2016-04-01"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MAZDZD"
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Níveis


Agregue os resultados em um nível de objeto definido. Isso elimina a duplicação dos dados automaticamente.


### Solicitação


Por exemplo, consulte os insights de uma campanha no nível do anúncio.

```
curl -G \
-d "level=ad" \
-d "fields=impressions,ad_id" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/CAMPAIGN_ID/insights"
```


### Resposta


```
{
  "data": [
    {
      "impressions": "9708",
      "ad_id": "6142546123068",
      "date_start": "2009-03-28",
      "date_stop": "2016-04-01"
    },
    {
      "impressions": "18841",
      "ad_id": "6142546117828",
      "date_start": "2009-03-28",
      "date_stop": "2016-04-01"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MQZDZD"
    }
  }
}
```


Se você não tiver acesso a todos os objetos do anúncio no nível solicitado, a chamada de insights não retornará dados. Por exemplo, ao solicitar insights com `level` definido como `ad`, se você não tiver acesso a um ou mais objetos desse tipo na conta de anúncios, a chamada de API retornará um erro de permissão.
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Janelas de atribuição


A **janela de atribuição de conversão** oferece períodos de tempo que definem quando atribuímos o evento a um anúncio em um app da Meta. Para saber mais, consulte [Sobre as janelas de atribuição no Gerenciador de Anúncios da Meta](https://www.facebook.com/business/help/2198119873776795). Mensuramos as ações que ocorrem quando acontece um evento de conversão e voltamos 1 e 7 dias no tempo. Para visualizar as ações designadas a janelas de atribuição diferentes, faça uma solicitação para `/{ad-account-id}/insights`. Se você não fornecer `action_attribution_windows`, usaremos `7d_click` e informaremos em `value`.


Por exemplo, especifique `action_attribution_windows`, e "value" será fixado na janela de atribuição `7d_click`. Faça uma solicitação para `act_10151816772662695/insights?action_attribution_windows=['1d_click','1d_view']` e receba este resultado:

```
"spend": 2352.45,
"actions": [
{
"action_type": "link_click",
"value": 6608,
"1d_view": 86,
"1d_click": 6510
},
"cost_per_action_type": [
{
"action_type": "link_click",
"value": 0.35600030266344,
"1d_view": 27.354069767442,
"1d_click": 0.36135944700461
},

// if attribution window is _not_ specified in query. And note that the number under 'value' key is the same even if attribution window is specified.
// act_10151816772662695/insights
"spend": 2352.45,
"actions": [
{
"action_type": "link_click",
"value": 6608
},
"cost_per_action_type": [
{
"action_type": "link_click",
"value": 0.35600030266344
},
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Expansão de campo


Solicite campos no nível do nó e por campos especificados na [expansão de campo](https://developers.facebook.com/docs/graph-api/using-graph-api/#field-expansion).


### Solicitação


```
curl -G \
-d "fields=insights{impressions}" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_ID"
```


### Resposta


```
{
  "id": "6042542123268",
  "name": "My Website Clicks Ad",
  "insights": {
    "data": [
      {
        "impressions": "9708",
        "date_start": "2016-03-06",
        "date_stop": "2016-04-01"
      }
    ],
    "paging": {
      "cursors": {
        "before": "MAZDZD",
        "after": "MAZDZD"
      }
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Classificação


Classifique os resultados informando o parâmetro `sort` com `{fieldname}_descending` ou `{fieldname}_ascending`:


### Solicitação


```
curl -G \
-d "sort=reach_descending" \
-d "level=ad" \
-d "fields=reach" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_SET_ID/insights"
```


### Resposta


```
{
  "data": [
    {
      "reach": 10742,
      "date_start": "2009-03-28",
      "date_stop": "2016-04-01"
    },
    {
      "reach": 5630,
      "date_start": "2009-03-28",
      "date_stop": "2016-04-03"
    },
    {
      "reach": 3231,
      "date_start": "2009-03-28",
      "date_stop": "2016-04-02"
    },
    {
      "reach": 936,
      "date_start": "2009-03-29",
      "date_stop": "2016-04-02"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MQZDZD"
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Rótulos de anúncios


Estatísticas de todos os rótulos cujos nomes são idênticos. Agregados em um único valor em um nível de objeto de anúncio. Consulte a [referência de rótulos de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-label) para saber mais.


### Solicitação


```
curl -G \
-d "fields=id,name,insights{unique_clicks,cpm,total_actions}" \
-d "level=ad" \
-d 'filtering=[{"field":"ad.adlabels","operator":"ANY", "value":["Label Name"]}]'  \
-d 'time_range={"since":"2015-03-01","until":"2015-03-31"}' \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_OBJECT_ID/insights"
```


### Resposta


```
{
  "data": [
    {
      "unique_clicks": 74,
      "cpm": 0.81081081081081,
      "total_actions": 49,
      "date_start": "2015-03-01",
      "date_stop": "2015-03-31",
    },
  ],
  "paging": {
    "cursors": {
      "before": "MA==",
      "after": "MA==",
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Definição de cliques


Para entender melhor as métricas de cliques oferecidas pela Meta atualmente, leia as definições e o uso de cada uma abaixo:


- **Cliques no link, `actions:link_click`** – o número de cliques em links do anúncio para selecionar destinos ou experiências dentro ou fora de propriedades da Meta. Consulte [Cliques no link na Central de Ajuda de Anúncios](https://www.facebook.com/business/help/659185130844708).
- **Cliques (todos), `clicks`** – a métrica contabiliza diversos tipos de cliques no anúncio, inclusive determinadas interações com o contêiner de anúncios, links para outros destinos e links para experiências de anúncios expandidas. Consulte [Cliques (todos) na Central de Ajuda de Anúncios](https://www.facebook.com/business/help/787506997938504).
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Objetos excluídos e arquivados


As unidades de anúncios podem ser `DELETED` ou `ARCHIVED`. As estatísticas de objetos excluídos ou arquivados aparecerão quando você consultar os respectivos objetos principais. Dessa forma, se você consultar `impressions` no nível do conjunto de anúncios, os resultados incluirão `impressions` de todos os anúncios do conjunto independentemente do estado de cada um deles (excluídos ou arquivados). Veja também [Gerenciar o status de seu objeto de anúncio](https://developers.facebook.com/docs/marketing-api/best-practices/storing_adobjects).


Porém, se você consultar usando filtros, a filtragem de status será aplicada por padrão para retornar apenas objetos ativos. Por isso, as estatísticas totais do nó principal poderão ser maiores que as estatísticas dos derivados.


No entanto, é possível obter as estatísticas de objetos `ARCHIVED` dos respectivos nós principais ao fornecer um parâmetro `filtering` adicional.


### Solicitação


Para consultar as estatísticas de todos os anúncios `ARCHIVED` em uma conta de anúncios listadas uma a uma:

```
curl -G \
  -d "level=ad" \
  -d "filtering=[{'field':'ad.effective_status','operator':'IN','value':['ARCHIVED']}]" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights/"
```


### Resposta


Observe que apenas os objetos arquivados são retornados nessa resposta.

```
{
  "data": [
    {
      "impressions": "1741",
      "date_start": "2016-03-11",
      "date_stop": "2016-03-12"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MAZDZD"
    }
  }
}
```


### Insights sobre objetos excluídos


Você poderá consultar insights sobre objetos excluídos usando as respectivas identificações ou o filtro `ad.effective_status`.


### Solicitação


Por exemplo, se você tiver a identificação do conjunto de anúncios:

```
curl -G \
-d "fields=id,name,status,insights{impressions}" \
-d "access_token=ACCESS_TOKEN" \
"https://graph.facebook.com/v25.0/AD_SET_ID"
```


Neste exemplo, consultamos com `ad.effective_status`:

```
POST https://graph.facebook.com/<VERSION>/act_ID/insights?access_token=token&appsecret_proof=proof&fields=ad_id,impressions&date_preset=lifetime&level=ad&filtering=[{"field":"ad.effective_status","operator":"IN","value":["DELETED"]}]
```


### Resposta


```
{
  "id": "6042147342661",
  "name": "My Like Campaign",
  "status": "DELETED",
  "insights": {
    "data": [
      {
        "impressions": "1741",
        "date_start": "2016-03-11",
        "date_stop": "2016-03-12"
      }
    ],
    "paging": {
      "cursors": {
        "before": "MAZDZD",
        "after": "MAZDZD"
      }
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Solução de problemas


### Tempos-limite


Os problemas mais comuns que causam falha nesse ponto de extremidade são o excesso de solicitações e a ocorrência de tempos-limite:


- Em solicitações `/GET` ou síncronas, é possível consultar erros de falta de memória ou de tempo-limite.
- Em solicitações `/POST` ou assíncronas, é possível consultar erros de tempo-limite. Para solicitações assíncronas, pode ser que demore até uma hora para concluir uma solicitação, incluindo tentativas de repetição. Por exemplo, se você fizer uma consulta que tentar extrair grandes volumes de dados para muitos objetos de nível de anúncio.


#### Recomendações


- Não há um limite explícito que indique quando ocorrerá uma falha na consulta. Quando o tempo limite for atingido, tente detalhar a consulta em consultas menores colocando filtros, como intervalo de datas.
- O cálculo de métricas únicas é demorado. Tente consultar métricas exclusivas em uma chamada separada para melhorar o desempenho de métricas não exclusivas.


### Limitação de volume


A API de Insights da Meta utiliza a limitação de volume para garantir uma experiência ideal de geração de relatórios a todos os nossos parceiros. Para mais informações e sugestões, consulte [Limites e boas práticas](https://developers.facebook.com/docs/marketing-api/insights/best-practices/) da API de Insights.


### Discrepância com o Gerenciador de Anúncios


A partir de 10 de junho de 2025, para reduzir discrepâncias com o Gerenciador de Anúncios da Meta, `use_unified_attribution_setting` e `action_report_time parameters` serão desconsiderados e as respostas da API imitarão as configurações do Gerenciador de Anúncios:


- Os valores atribuídos (`value`) serão baseados nas configurações de atribuição no nível do conjunto de anúncios (semelhante a `use_unified_attribution_setting=true`), e as ações inline/no anúncio serão incluídas nos dados da janela de atribuição de `1d_click` ou `1d_view`. Depois dessa alteração, os dados de janela de atribuição `inline` independentes não serão retornados.
- As ações serão registradas usando `action_report_time=mixed`: as ações na Meta (como cliques em links) usarão o tempo de relatórios baseado em impressões. Já as ações fora da Meta (como compras na web) aproveitarão o tempo de relatórios baseado em conversões.


Os comportamentos padrão da API e do Gerenciador de Anúncios são diferentes. Se você quiser observar o mesmo comportamento do Gerenciador de Anúncios, defina o campo `use_unified_attribution_setting` como verdadeiro.
[○](https://developers.facebook.com/docs/marketing-api/insights#)

## Saiba mais


- [Insights sobre a conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-account/insights)
- [Insights sobre a campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/insights)
- [Insights sobre o conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/insights)
- [Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/)


Essa API cobre apenas os pontos de extremidade da lista acima. Se você pretende incluir relatórios da Meta na sua solução, consulte os [Termos de Serviço](https://developers.facebook.com/terms) e as [Políticas do Desenvolvedor relacionadas à API de Marketing](https://developers.facebook.com/devpolicy/#marketingapi).
[○](https://developers.facebook.com/docs/marketing-api/insights#)[○](https://developers.facebook.com/docs/marketing-api/insights#)Nesta Página[API de Insights](https://developers.facebook.com/docs/marketing-api/insights#api-de-insights)[Antes de começar](https://developers.facebook.com/docs/marketing-api/insights#antes-de-come-ar)[Estatísticas de campanha](https://developers.facebook.com/docs/marketing-api/insights#estat-sticas-de-campanha)[Chamadas](https://developers.facebook.com/docs/marketing-api/insights#makingacall)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta)[Níveis](https://developers.facebook.com/docs/marketing-api/insights#n-veis)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o-2)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta-2)[Janelas de atribuição](https://developers.facebook.com/docs/marketing-api/insights#janelas-de-atribui--o)[Expansão de campo](https://developers.facebook.com/docs/marketing-api/insights#expans-o-de-campo)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o-3)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta-3)[Classificação](https://developers.facebook.com/docs/marketing-api/insights#classifica--o)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o-4)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta-4)[Rótulos de anúncios](https://developers.facebook.com/docs/marketing-api/insights#r-tulos-de-an-ncios)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o-5)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta-5)[Definição de cliques](https://developers.facebook.com/docs/marketing-api/insights#defini--o-de-cliques)[Objetos excluídos e arquivados](https://developers.facebook.com/docs/marketing-api/insights#objetos-exclu-dos-e-arquivados)[Solicitação](https://developers.facebook.com/docs/marketing-api/insights#solicita--o-6)[Resposta](https://developers.facebook.com/docs/marketing-api/insights#resposta-6)[Insights sobre objetos excluídos](https://developers.facebook.com/docs/marketing-api/insights#insights-sobre-objetos-exclu-dos)[Solução de problemas](https://developers.facebook.com/docs/marketing-api/insights#solu--o-de-problemas)[Tempos-limite](https://developers.facebook.com/docs/marketing-api/insights#tempos-limite)[Limitação de volume](https://developers.facebook.com/docs/marketing-api/insights#limita--o-de-volume)[Discrepância com o Gerenciador de Anúncios](https://developers.facebook.com/docs/marketing-api/insights#discrep-ncia-com-o-gerenciador-de-an-ncios)[Saiba mais](https://developers.facebook.com/docs/marketing-api/insights#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Wb295aqaKWWI3iO3YdrxSf-19pVojyHd8buX-mzrK8eEucIbdI_d9eZR0Mg_aem_3GKOSvOh4T6ccMNCuuBtvw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR79Qv9ywnqESsHPhNsw2_LTLLfZpyXYQnXZXqyKqiUuVJhmtQ4cEuWld8RUAw_aem_6BPMyDtACwjUef_JnYFjDg&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7eoTWYQuC6-PzgA7PYHahW2AIWm2xdID3QOOas-7NcaoBIdp18hohPtFQn2w_aem_JFCeMsEg_S0kGSyjw5WiYA&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Wb295aqaKWWI3iO3YdrxSf-19pVojyHd8buX-mzrK8eEucIbdI_d9eZR0Mg_aem_3GKOSvOh4T6ccMNCuuBtvw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4z6ZG65VfcfAN90ctyJQZAjSV5kFozLdI_WoQBdZDA2dpUN7vxDc1ef4lbIw_aem_btFCdDPbSwtk8J_fleE0ww&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QPIaocO6LNDS3M42j1lRiot8WPvMhMPovsNyzaxkyaKcz31-oQVofQ806BQ_aem_zieUCJN0sF1_J1r9dk_s9g&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Kxr-EZNT0FY3aIZeld4wRG9Ks6Remc0SRdwopUxK5G4b4BE8Lb5TWOECybA_aem__DrSeHMlWLti9xs6moq1-w&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR79Qv9ywnqESsHPhNsw2_LTLLfZpyXYQnXZXqyKqiUuVJhmtQ4cEuWld8RUAw_aem_6BPMyDtACwjUef_JnYFjDg&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Kxr-EZNT0FY3aIZeld4wRG9Ks6Remc0SRdwopUxK5G4b4BE8Lb5TWOECybA_aem__DrSeHMlWLti9xs6moq1-w&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56rkGFCktuIf8rIeXqWiwE1JYuBo8zSi6pS2tRc6cj26Ma_RY4SEkBaIQKSA_aem_N-6Hb4di5UuV5Cby2q8uFw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56rkGFCktuIf8rIeXqWiwE1JYuBo8zSi6pS2tRc6cj26Ma_RY4SEkBaIQKSA_aem_N-6Hb4di5UuV5Cby2q8uFw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56rkGFCktuIf8rIeXqWiwE1JYuBo8zSi6pS2tRc6cj26Ma_RY4SEkBaIQKSA_aem_N-6Hb4di5UuV5Cby2q8uFw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Y35ATmEPjzmetp6ORYI9guT_dy67UIkwcybfPciKxykJWB0lmYrvJJhXLSg_aem_lJtmoT0GKN_t9ksLBaI8AQ&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56rkGFCktuIf8rIeXqWiwE1JYuBo8zSi6pS2tRc6cj26Ma_RY4SEkBaIQKSA_aem_N-6Hb4di5UuV5Cby2q8uFw&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7eoTWYQuC6-PzgA7PYHahW2AIWm2xdID3QOOas-7NcaoBIdp18hohPtFQn2w_aem_JFCeMsEg_S0kGSyjw5WiYA&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7mu13aac5FXA9MY665b_NvPkXnm5GMPxByx36NUaUOsU0n5krCzAx-kXIkGttKcCEncLWoXwwxSiRRaGjcPyZJaCQca4mF8GjHbZww72QGuAEMird1OnWCeMvGKGMGJrgw6Jj_MM9mkm4zGRZ9Jg6s5FE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão