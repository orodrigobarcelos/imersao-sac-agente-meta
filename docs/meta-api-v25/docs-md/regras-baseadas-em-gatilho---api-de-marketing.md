<!-- Fonte: Regras baseadas em gatilho - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Regras de anúncios baseadas em gatilho


Monitore o estado dos anúncios em tempo real. Uma regra baseada em gatilho é avaliada assim que os dados de insights ou metadados dos objetos do anúncio relevantes são alterados. A latência para alterações em metadados é geralmente de alguns segundos, e a latência para alterações em insights geralmente é dentro de alguns minutos (p99 atual é de cerca de 7,5 minutos).


Para regras baseadas em gatilho, `schedule_spec` não é compatível, uma vez que elas são sempre verificadas em tempo real.


As regras baseadas em gatilho só estão disponíveis na API neste local e não estão acessíveis por meio do Gerenciador de Anúncios.


## Objeto de gatilho


O objeto `trigger` define como é feita a avaliação de uma regra. Todos os tipos de gatilho exigem um `field` de gatilho, exceto `METADATA_CREATION`. Uma regra baseada em gatilho só verifica sua condição quando esse campo é alterado.


Uma regra baseada em gatilho pode ter somente um `trigger`. Se houver condições ou restrições em várias métricas, você poderá adicionar as restantes como `filters`.


O campo `filters` é usado da mesma forma que para [regras baseadas em programação](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/scheduled-based-rules). Uma regra baseada em gatilho passa sua avaliação somente quando o `trigger` e todos os `filters` atendem às condições. Então, um gatilho e um filtro serão intercambiáveis se a mudança em um campo levar à mudança de outro. Por exemplo, se você quiser que uma regra seja disparada quando `cost_per_mobile_app_install` > `X` AND `spent` > `Y`, poderá usar `cost_per_mobile_app_install` ou `spent` como o gatilho, e a outra como um dos filtros, porque esses campos dependem entre si.


O objeto `trigger` pertence a [`evaluation_spec`](https://developers.facebook.com/docs/marketing-api/ad-rules/evaluation-spec) e segue esta estrutura:


| Chaves do objeto de gatilho | Descrição |
| --- | --- |
| type | O tipo de regra baseada em gatilho. No momento, as opções aceitas são: METADATA_CREATION : é disparada quando um objeto de anúncio é criado METADATA_UPDATE : é disparada quando o field de metadados é atualizado STATS_CHANGE : é disparada quando o field de insights muda para cumprir com a comparação STATS_MILESTONE : é disparada quando o field de insights atingir um múltiplo do value |
| field | O campo subjacente. Não está em uso para METADATA_CREATION |
| value | O valor do filtro subjacente. Não está em uso para METADATA_CREATION . Opcional para METADATA_UPDATE . |
| operator | O operador do filtro subjacente. Não está em uso para METADATA_CREATION . Opcional para METADATA_UPDATE . |


Você pode criar regras de anúncio que são disparadas de quatro maneiras diferentes:


- Relacionadas a metadados: `METADATA_CREATION` ou `METADATA_UPDATE`
- Relacionadas a insights: `STATS_MILESTONE` ou `STATS_CHANGE`
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#)

## Regras de gatilho relacionadas a metadados


### Regra de criação de metadados


Esta regra é usada para monitorar quando um objeto de anúncio é criado. Somente `type` é obrigatório na especificação de `trigger`. Para os filtros, especifique o `entity_type` que deseja monitorar.


Veja a seguir um exemplo de uma regra de criação de metadados para monitorar a criação de todos os anúncios que se encaixem em um determinado objetivo. Sempre que um novo anúncio é criado sob uma campanha de anúncios com o objetivo `APP_INSTALLS`, um ping é enviado.

```
curl -i -X POST \
-F 'name=Metadata Creation Example 1' \
-F 'evaluation_spec={
      "evaluation_type" : "TRIGGER",
      "trigger" : {
        "type": "METADATA_CREATION",
      },
      "filters" : [
       {
         "field": "entity_type",
         "value": "AD",
         "operator": "EQUAL",
       },
       {
         "field": "campaign.objective",
         "value": ["APP_INSTALLS"],
         "operator": "IN",
       },
     ]
   }' \
-F 'execution_spec={
      "execution_type": "PING_ENDPOINT"
   }' \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library"
```


### Regra de atualização de metadados


Esta regra é usada para monitorar quando os metadados de um objeto de anúncio são alterados. Consulte a [lista](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/evaluation-spec#metadata-filters-supported-by-trigger-and-schedule-based-rules) de campos de metadados compatíveis. Na especificação de `trigger`, `field` é obrigatório, ao passo que `value` e `operator` são opcionais.


Se você tiver interesse na alteração de um campo, independentemente de qual seja seu valor, basta especificar a opção `field`. Veja a seguir um exemplo de envio de uma notificação do Facebook sempre que o orçamento diário de um conjunto de anúncios for alterado.

```
curl -i -X POST \
-F 'name=Metadata Update Example 1' \
-F 'evaluation_spec={
      "evaluation_type" : "TRIGGER",
      "trigger" : {
        "type": "METADATA_UPDATE",
        "field": "daily_budget",
      },
      "filters" : [
       {
         "field": "entity_type",
         "value": "ADSET",
         "operator": "EQUAL",
       },
     ]
   }' \
-F 'execution_spec={
      "execution_type": "NOTIFICATION"
   }' \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library"
```


Se você tiver interesse em somente um subconjunto dos eventos, poderá fornecer as opções `operator` e `value` para refinar a condição `trigger`. Veja a seguir um exemplo para ser notificado quando o orçamento diário de um conjunto de anúncios é alterado e exceder 1.000:

```
curl -i -X POST \
-F 'name=Metadata Update Example 2' \
-F 'evaluation_spec={
      "evaluation_type" : "TRIGGER",
      "trigger" : {
        "type": "METADATA_UPDATE",
        "field": "daily_budget",
        "value": 1000,
        "operator": "GREATER_THAN"
      },
      "filters" : [
       {
         "field": "entity_type",
         "value": "ADSET",
         "operator": "EQUAL",
       },
     ]
   }' \
-F 'execution_spec={
      "execution_type": "PING_ENDPOINT"
   }' \
-F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library"
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#)

## Regras de gatilho relacionadas a insights


### Regra de marco de estatísticas


Com `STATS_MILESTONE` como `type`, `evaluation_spec` será disparado quando `field` atingir um múltiplo de `value` para os objetos correspondentes às condições na matriz de `filters`.


Para esse tipo específico de regra, o `operator` de gatilho deve ser `EQUAL`, e o filtro `time_preset` deve ter um valor de `LIFETIME`.


Há um conjunto mais restritivo de campos compatíveis. Qualquer campo não listado abaixo não é compatível como um `field` de gatilho, mas **ainda pode ser usado como filtro** na lista de `filters`. Além disso, há valores mínimos obrigatórios para o `value` do gatilho, dependendo do `field`.


| Valores do campo de gatilho compatíveis | Valor mínimo |
| --- | --- |
| impressions | 1.000 |
| unique_impressions | 1.000 |
| reach | 1.000 |
| clicks | 10 |
| unique_clicks | 10 |
| spent | 1.000 (centavos) |
| results | 5 |
| app_custom_event | 1 |
| app_custom_event_fb_mobile_achievement_unlocked | 1 |
| app_custom_event_fb_mobile_activate_app | 1 |
| app_custom_event_fb_mobile_add_payment_info | 1 |
| app_custom_event_fb_mobile_add_to_cart | 1 |
| app_custom_event_fb_mobile_add_to_wishlist | 1 |
| app_custom_event_fb_mobile_complete_registration | 1 |
| app_custom_event_fb_mobile_content_view | 1 |
| app_custom_event_fb_mobile_initiated_checkout | 1 |
| app_custom_event_fb_mobile_level_achieved | 1 |
| app_custom_event_fb_mobile_purchase | 1 |
| app_custom_event_fb_mobile_rate | 1 |
| app_custom_event_fb_mobile_search | 1 |
| app_custom_event_fb_mobile_spent_credits | 1 |
| app_custom_event_fb_mobile_tutorial_completion | 1 |
| app_custom_event_other | 1 |
| leadgen | 1 |
| like | 1 |
| link_click | 1 |
| mobile_app_install | 1 |
| offsite_conversion | 1 |
| offsite_conversion_add_to_cart | 1 |
| offsite_conversion_checkout | 1 |
| offsite_conversion_fb_pixel_add_payment_info | 1 |
| offsite_conversion_fb_pixel_add_to_cart | 1 |
| offsite_conversion_fb_pixel_add_to_wishlist | 1 |
| offsite_conversion_fb_pixel_complete_registration | 1 |
| offsite_conversion_fb_pixel_initiate_checkout | 1 |
| offsite_conversion_fb_pixel_lead | 1 |
| offsite_conversion_fb_pixel_other | 1 |
| offsite_conversion_fb_pixel_purchase | 1 |
| offsite_conversion_fb_pixel_search | 1 |
| offsite_conversion_fb_pixel_view_content | 1 |
| offsite_engagement | 1 |
| post | 1 |
| post_comment | 1 |
| post_engagement | 1 |
| post_like | 1 |
| post_reaction | 1 |
| view_content | 1 |
| video_play | 1 |
| video_view | 1 |
| vote | 1 |


Veja a seguir um exemplo de uma regra de marco de estatísticas, que envia um ping sempre que alguém faz um comentário no seu post:

```
curl \
-F 'name=Rule 1' \
-F 'evaluation_spec={
      "evaluation_type" : "TRIGGER",
      "trigger" : {
        "type": "STATS_MILESTONE",
        "field": "post_comment",
        "value": 1,
        "operator": "EQUAL"
      },
      "filters" : [
       {
         "field": "entity_type",
         "value": "CAMPAIGN",
         "operator": "EQUAL",
       },
       {
         "field": "time_preset",
         "value": "LIFETIME",
         "operator": "EQUAL",
       },
     ]
   }' \
-F 'execution_spec={
      "execution_type": "PING_ENDPOINT"
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


### Regra de alteração de estatísticas


Ao usar `STATS_CHANGE` como `type` de gatilho, `execution_spec` é disparado quando o operador lógico `AND` do gatilho e todos os filtros são avaliados de `false` para `true` em um determinado `time_preset`.


Se avaliações posteriores do operador lógico `AND` também forem verdadeiras, `execution_spec`**não** é executado. Porém, se a avaliação do operador lógico `AND` mudar de `true` para `false`, `execution_spec` será executado quando for revertido para `true`.


Para esse tipo específico de regra, o `operator` de gatilho pode ser `GREATER_THAN`, `LESS_THAN`, `IN_RANGE` ou `NOT_IN_RANGE`.


Veja a seguir um exemplo de regra de alteração de estatísticas. Pause um anúncio sempre que ele tiver alcançado mais de 5.000 pessoas e for superior a US$ 10 por compra nos últimos 3 dias.

```
curl \
-F 'name=Rule 1' \
-F 'evaluation_spec={
      "evaluation_type" : "TRIGGER",
      "trigger" : {
        "type": "STATS_CHANGE",
        "field": "cost_per_purchase_fb",
        "value": 1000,
        "operator": "GREATER_THAN",
      },
      "filters" : [
       {
         "field": "entity_type",
         "value": "AD",
         "operator": "EQUAL"
       },
       {
         "field": "time_preset",
         "value": "LAST_3_DAYS",
         "operator": "EQUAL"
       },
       {
         "field": "reach",
         "value": 5000,
         "operator": "GREATER_THAN"
       }
     ]
   }' \
-F 'execution_spec={
      "execution_type": "PAUSE"
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


### Regras de alteração de insights de veiculação (Beta)


Ao usar `DELIVERY_INSIGHTS_CHANGE` como o `type` de gatilho, a regra será disparada quando todos os filtros definidos em `evaluation_spec` forem avaliados como `true`, **e** o gatilho definido em `evaluation_spec` mudar de `false` para `true`.


Em avaliações posteriores, se os filtros e o gatilho continuarem sendo avaliados como `true`, a regra não será disparada novamente.
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#)

## Configuração de Webhooks


Para usar o tipo de execução `PING_ENDPOINT`, você precisa configurar uma assinatura para seu app por meio do Webhooks. Configure um URL de retorno de chamada, um app do Facebook e Webhooks para receber notificações da API de Regras:


### Etapa 1: configurar um URL de retorno de chamada


Consulte [Webhooks da Meta](https://developers.facebook.com/docs/graph-api/webhooks#setup) e crie um URL de retorno de chamada que possa lidar com o desafio e a resposta durante a verificação. O URL de retorno de chamada lida com a estrutura de dados enviada quando uma regra é disparada:

```
{
  object: 'application',
  entry: [{
    id: '<APPLICATION_ID>',
    time: 1468938744,
    changes: [{
      field: 'ads_rules_engine',
      value: {
        'rule_id': 1234,
        'object_id': 5678,
        'object_type': 'ADSET',
        'trigger_type': 'STATS_CHANGE',
        'trigger_field': 'COST_PER_LINK_CLICK',
        'current_value': '15.8',
      }
    }],
  }],
}
```


O campo `current_value` é uma string codificada por JSON. Seu valor pode ser uma string em aspas duplas, um número, ou uma matriz que começa com `[` (colchete esquerdo) e termina com `]` (colchete direito).


### Etapa 2: adicionar o Webhook `ads_rules_engine` ao app


Assim que o URL de retorno de chamada lidar com o desafio e a resposta para verificação, registre-a no seu app quando uma regra é disparada:


- Crie um novo [app do Facebook](https://developers.facebook.com/apps/) ou use um existente.
- Adicione o produto do Webhooks.


- Crie uma nova assinatura para um app e selecione o `ad_rules_engine`.


Você também pode fazer isso por meio da Graph API, **usando um token de acesso do app e não um token de acesso do usuário**:

```
curl \
-F "object=application" \
-F "callback_url=<CALLBACK_URL>" \
-F "fields=ads_rules_engine" \
-F "verify_token=<VERIFY_TOKEN>" \
-F "access_token=<APP_ACCESS_TOKEN>" \
"https://graph.facebook.com/<VERSION>/<APP_ID>/subscriptions"
```


Consulte [Subscriptions Reference](https://developers.facebook.com/docs/graph-api/reference/app/subscriptions) para obter detalhes sobre `APP_ID/subscriptions`.
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#)Nesta Página[Regras de anúncios baseadas em gatilho](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#regras-de-an-ncios-baseadas-em-gatilho)[Objeto de gatilho](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#objeto-de-gatilho)[Regras de gatilho relacionadas a metadados](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#regras-de-gatilho-relacionadas-a-metadados)[Regra de criação de metadados](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#metadata-creation)[Regra de atualização de metadados](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#metadata-update)[Regras de gatilho relacionadas a insights](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#regras-de-gatilho-relacionadas-a-insights)[Regra de marco de estatísticas](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#stats-milestone)[Regra de alteração de estatísticas](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#stats-change)[Regras de alteração de insights de veiculação (Beta)](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#regras-de-altera--o-de-insights-de-veicula--o--beta-)[Configuração de Webhooks](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#webhooks)[Etapa 1: configurar um URL de retorno de chamada](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#etapa-1--configurar-um-url-de-retorno-de-chamada)[Etapa 2: adicionar o Webhook ads_rules_engine ao app](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/trigger-based-rules#etapa-2--adicionar-o-webhook-ads-rules-engine-ao-app) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tac08rjElNDZJXui4onUZye9UsApNasED3YRVJ7gNlQOf6sK-4pdUzlmXoA_aem_D2Rkjry9-zsYtFWWrQwYBQ&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6H6Dz5HNDqQXZT5Ye53mUrzuXglhsCL_y-TWUjEnmC_rGGAYkGRTUwgOTXjQ_aem_rwSb6nqBcCxug09eb4vkQw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tac08rjElNDZJXui4onUZye9UsApNasED3YRVJ7gNlQOf6sK-4pdUzlmXoA_aem_D2Rkjry9-zsYtFWWrQwYBQ&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4TEH9xl2YHdzH_jLDAwQ8ZXM9JIww_BiLL4T2tOs4BF9Q9CK_tGNAZjVlXfA_aem_vEckFwLnIaWrMeKDMd4cPg&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4vtCum1oYdrWzX9mNn83ka23jpkSsKoc5eox6S-SK5oovYp4QVjkKEDEdDzw_aem_2ykwctNA8tbTDIBKwGTD3A&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6H6Dz5HNDqQXZT5Ye53mUrzuXglhsCL_y-TWUjEnmC_rGGAYkGRTUwgOTXjQ_aem_rwSb6nqBcCxug09eb4vkQw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jowk9G05pLEsupx8HwkHvTWFb0jduwppNU_IpWm4dd_HByq4s0rrh6wDhow_aem_tbwTddLOkq2oQH5xAHHPHw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4TEH9xl2YHdzH_jLDAwQ8ZXM9JIww_BiLL4T2tOs4BF9Q9CK_tGNAZjVlXfA_aem_vEckFwLnIaWrMeKDMd4cPg&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7pTwnMOdIvf2LPNp3BrkWP12C1TsQp-JPHFmBf7uPE8Rem5wTWAEb4IR0MEw_aem_JEmyuWwItUUpUpaaqpjY-g&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6a8PdGvw-aHR0CTgntv1p2MxqvvTtS1VMNrNSIs9zh5JLQ3Geo2CVgHnVz0g_aem_55KunEbY4TtheusMinBVjw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5lMmlj0yLhS_Zaj9XIpUOgBXYs4mFhLxgBohZbG5bcopuVsFvvJY0nis1G5Q_aem_1geV-ulKgAI7-khAAT43fw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6a8PdGvw-aHR0CTgntv1p2MxqvvTtS1VMNrNSIs9zh5JLQ3Geo2CVgHnVz0g_aem_55KunEbY4TtheusMinBVjw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4TEH9xl2YHdzH_jLDAwQ8ZXM9JIww_BiLL4T2tOs4BF9Q9CK_tGNAZjVlXfA_aem_vEckFwLnIaWrMeKDMd4cPg&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jowk9G05pLEsupx8HwkHvTWFb0jduwppNU_IpWm4dd_HByq4s0rrh6wDhow_aem_tbwTddLOkq2oQH5xAHHPHw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tac08rjElNDZJXui4onUZye9UsApNasED3YRVJ7gNlQOf6sK-4pdUzlmXoA_aem_D2Rkjry9-zsYtFWWrQwYBQ&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6H6Dz5HNDqQXZT5Ye53mUrzuXglhsCL_y-TWUjEnmC_rGGAYkGRTUwgOTXjQ_aem_rwSb6nqBcCxug09eb4vkQw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BFzVG8FdytGxROysGdyZ1eqVKeQmwPxKoewMxxuX_Sqik6LaDGgDiRwpqng_aem_GJVm1lUWDc8vD_HjwL9wAg&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47Rzg3-QuGpOumeJGZeaLWv4GKcbeVpzvpDM73Cd4pFkn51Fmeb8wS4k6ccQ_aem_LT_U6izPqIoRtsPioYblbQ&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7pTwnMOdIvf2LPNp3BrkWP12C1TsQp-JPHFmBf7uPE8Rem5wTWAEb4IR0MEw_aem_JEmyuWwItUUpUpaaqpjY-g&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6a8PdGvw-aHR0CTgntv1p2MxqvvTtS1VMNrNSIs9zh5JLQ3Geo2CVgHnVz0g_aem_55KunEbY4TtheusMinBVjw&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5dTN0irRlaU1fA7J13y23LZvLDrRqufHoYgYSbzZx5PUfO9FXpGgIpXdz4DhQ_05TfWX7QKBv5TU7I85ighHUGXU71rkSwzB3Hj81VepgYucs_GqChinhMB_tkAz06Yk89zSbaHDHk8MEaWk5MzA2bqGM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão