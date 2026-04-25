<!-- Fonte: Regras de valor - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/bidding/value-rules -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Regras de valor


As regras de valor permitem que você expresse valor em critérios de público, posicionamento e local da conversão, além de consolidar campanhas para impulsionar o desempenho. Quando você usa regras de valor, suas campanhas podem ajustar a veiculação de acordo com os critérios e os resultados que você valoriza mais.


Critérios disponíveis: idade, gênero, localização, sistema operacional, plataforma do dispositivo e posicionamentos e locais da conversão selecionados.


O que é possível fazer com as regras de valor:


- Criar regras para definir quanto mais determinados públicos valem para seu negócio. Nosso sistema otimizará os resultados com base nessas regras.
- Maximizar o desempenho ao focar nos públicos mais importantes.
- Direcionar seus esforços para as metas da parte inferior do funil, priorizando lances em segmentos com alto valor total.
- Aplicar regras para diferentes públicos, posicionamentos e locais da conversão em um único conjunto de anúncios, permitindo que você consolide várias campanhas.


Por exemplo, se você souber que homens de 25 a 44 anos têm, em média, um valor total 60% maior e que mulheres da mesma faixa etária têm um valor total 20% menor em comparação com clientes fora dessas dimensões, será possível usar regras de valor para aumentar seu lance em 60% para o público masculino de 25 a 44 anos e reduzir em 20% para o público feminino da mesma faixa etária. As pessoas que não se enquadrarem nessas regras de valor receberão um lance sem ajuste.


Quando você cria um conjunto de regras de valor, a ordem dessas regras define quais ajustes serão aplicados com prioridade no leilão de anúncios. Se você criar regras com sobreposição de público, usaremos apenas a primeira regra aplicável para ajustar o lance. Por exemplo, a regra 1 determina que você quer aumentar seu lance em 20% para mulheres na Califórnia, e a regra 2 estabelece um lance 10% maior para mulheres que usam um sistema operacional móvel específico. Se uma mulher na Califórnia que usa esse sistema operacional estiver no seu público, apenas a regra 1 será aplicada, aumentando o lance em 20%, já que se trata da primeira regra na ordem de prioridade.


### Permissões


Você precisará destas permissões:


- `ads_management`
- `ads_read`


## Quando usar regras de valor e controles/sugestões de público


Use as regras de valor quando quiser identificar públicos de maior ou menor valor e tiver planos de pagar por isso.


**Observação:** ao usar as regras de valor, talvez você veja mais conversões do seu público preferencial, mas o custo geral por resultado poderá aumentar.


| Meta | Usar controles de público | Usar regras de valor | Usar sugestões de público |
| --- | --- | --- | --- |
| Deve seguir os regulamentos | SIM | NÃO | NÃO |
| Disponibilidade para pagar mais por públicos de valor mais alto | NÃO | SIM | NÃO |
| Orientar a Meta a alcançar públicos com maior probabilidade de conversão | NÃO | NÃO | SIM |


Para saber mais, consulte [Como usar sugestões de público, controles de público e regras de valor para alcançar seu público preferido](https://www.facebook.com/business/help/2016171032241412?locale=en_US). Assim como em outras campanhas, sugerimos que, ao usar as regras de valor, você mantenha o direcionamento o mais amplo possível, dentro do que for viável para seu negócio.
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como criar um conjunto de regras de valor


Para criar um conjunto de regras de valor, você precisa fazer uma solicitação `POST` para o ponto de extremidade `/act_{ad-account-id}/value_rule_set`. O corpo da solicitação para criar um conjunto de regras de valor deve incluir os seguintes parâmetros:


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. É uma string que representa o nome do conjunto de regras de valor. |
| rules lista\<object\> | Obrigatório. É uma matriz de regras, em que cada regra especifica um conjunto de critérios (como idade ou gênero) e os respectivos ajustes de lance. Cada conjunto de regras pode conter até 10 regras. |


**Observação:** você pode criar até 6 conjuntos de regras por conta de anúncios.


### O parâmetro `rules`


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. É uma string que representa o nome da regra. |
| adjust_sign string | Obrigatório. Indica se o ajuste tem como objetivo aumentar ou reduzir o lance. Valores: INCREASE , DECREASE |
| adjust_value número inteiro | Obrigatório. É um número que indica a porcentagem do ajuste de lance. Valores: Para INCREASE : entre 1 e 1000; Para DECREASE : entre 1 e 90 |
| criteria lista\<object\> | Obrigatório. É uma matriz de objetos que representam os critérios do público e o ajuste de lance associado. |


**Observação:** você pode criar até 10 regras por conjunto de regras.


### O parâmetro `criteria`


| Nome | Descrição |
| --- | --- |
| criteria_type string | Obrigatório. Dimensão destinada ao ajuste de lance. Valores: AGE , GENDER , OS_TYPE , DEVICE_PLATFORM , LOCATION , PLACEMENT |
| operator string | Obrigatório. Operador usado ao avaliar os critérios. No momento, o único operador compatível é CONTAINS . Valor: CONTAINS |
| criteria_values lista\<string\> | Obrigatório. É uma matriz de strings que especifica o valor do critério para o criteria_type fornecido. |
| criteria_value_types lista\<string\> | Obrigatório. É uma matriz de strings que especifica o nível de detalhe dos tipos de critérios utilizados. Isso permite uma segmentação mais precisa ao definir o escopo dos critérios. |


**Observação:** você pode criar até 4 critérios por regra. Conjuntos de regras com mais de dois critérios **não** serão editáveis (somente leitura) na interface do Gerenciador de Anúncios. A edição de conjuntos de regras será possível apenas via API.


### Os campos `criteria_values` e `criteria_value_types`


As matrizes `criteria_values` e `criteria_value_types` funcionam juntas para definir os valores de um `criteria_type` específico ou de uma dimensão utilizada no ajuste de lance. Cada valor na matriz `criteria_values` deve ter um tipo correspondente especificado na matriz `criteria_value_types`, com os tipos listados na mesma ordem dos respectivos valores.


| criteria_type | criteria_values | criteria_value_types |
| --- | --- | --- |
| AGE | 1. Faixa etária predefinida "18-24", "25-34", "35-44", "45-55", "55-64", "65+" 2. Faixa etária personalizada As faixas etárias podem ser arbitrárias (por exemplo, "18-26") ou abertas (por exemplo, "45+"). Por exemplo: ["18-26", "31-37", "48+"]. Importante: não é permitido usar "65" como limite máximo em uma faixa etária. Use "18+" em vez de "18-65". Observação: os conjuntos de regras que usam faixas etárias personalizadas não serão editáveis (somente leitura) na interface do Gerenciador de Anúncios. A edição de conjuntos de regras será possível apenas via API. | NONE |
| GENDER | MALE , FEMALE | NONE |
| OS_TYPE | ANDROID , IOS | NONE |
| DEVICE_PLATFORM | MOBILE , DESKTOP | NONE |
| LOCATION | Múltiplos, dependendo de criteria_value_types . LOCATION_COUNTRY; LOCATION_REGION; LOCATION_CITY; LOCATION_DMA | LOCATION_COUNTRY , LOCATION_REGION , LOCATION_CITY , LOCATION_DMA |
| PLACEMENT | FB_FEED , FB_STORIES , FB_REELS , FB_MARKETPLACE , FB_SEARCH , FB_VIDEO , IG_FEED , IG_STORIES , IG_REELS , IG_EXPLORE , AUDIENCE_NETWORK Observação: os conjuntos de regras que usarem os posicionamentos FB_MARKETPLACE , FB_SEARCH , FB_VIDEO e IG_EXPLORE não poderão ser editados (somente leitura) na interface do Gerenciador de Anúncios. A edição de conjuntos de regras será possível apenas via API. | NONE |
| OMNI_CHANNEL | APP , INSTANT_FORM , PHONE_CALL , WEBSITE | NONE |


Por exemplo, se você quiser aplicar um ajuste de lance às faixas etárias `45-55` e `55-64`, o objeto de critérios ficará assim:

```
{
  "criteria_type": "AGE",
  "operator": "CONTAINS",
  "criteria_values": [
    "45-55",
    "55-64"
  ],
  "criteria_value_types": [
    "NONE",
    "NONE"
  ]
}
```


Como alternativa, se você quiser aplicar um ajuste de lance ao país Brasil e à região de Alberta, no Canadá, o objeto de critérios ficará assim:

```
{
  "criteria_type": "LOCATION",
  "operator": "CONTAINS",
  "criteria_values": [
    "BR",
    "527"
  ],
  "criteria_value_types": [
    "LOCATION_COUNTRY",
    "LOCATION_REGION"
  ]
}
```


### Exemplo de solicitação


```
curl -X POST \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/value_rule_set \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "My Value Rule Set",
    "rules": [
      {
        "name": "High age and gender",
        "adjust_sign": "INCREASE",
        "adjust_value": 20,
        "criterias": [
          {
            "criteria_type": "AGE",
            "operator": "CONTAINS",
            "criteria_values": [
              "18-24"
            ],
            "criteria_value_types": [
              "NONE"
            ]
          },
          {
            "criteria_type": "GENDER",
            "operator": "CONTAINS",
            "criteria_values": [
              "MALE"
            ],
            "criteria_value_types": [
              "NONE"
            ]
          }
        ]
      },
      {
        "name": "High bid for OS",
        "adjust_sign": "INCREASE",
        "adjust_value": 20,
        "criterias": [
          {
            "criteria_type": "OS_TYPE",
            "operator": "CONTAINS",
            "criteria_values": [
              "ANDROID"
            ],
            "criteria_value_types": [
              "NONE"
            ]
          }
        ]
      },
      {
        "name": "High bid for location country",
        "adjust_sign": "INCREASE",
        "adjust_value": 20,
        "criterias": [
          {
            "criteria_type": "LOCATION",
            "operator": "CONTAINS",
            "criteria_values": [
              "GB"
            ],
            "criteria_value_types": [
              "LOCATION_COUNTRY"
            ]
          }
        ]
      },
      {
        "name": "High bid for location region",
        "adjust_sign": "INCREASE",
        "adjust_value": 20,
        "criterias": [
          {
            "criteria_type": "LOCATION",
            "operator": "CONTAINS",
            "criteria_values": [
              "3847"
            ],
            "criteria_value_types": [
              "LOCATION_REGION"
            ]
          }
        ]
      }
    ]
  }'
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como recuperar um conjunto de regras de valor


Para ler um conjunto de regras de valor referente a uma determinada conta de anúncios, faça uma solicitação `GET` para o ponto de extremidade `/act_{ad-account-id}/value_rule_set` e liste qualquer conjunto de regras de valor existente nessa conta. Outra opção é fazer uma solicitação `GET` para o ponto de extremidade `/{value-rule-set-id}`.


### Exemplo de solicitação


```
curl -X GET \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/value_rule_set?fields=name,rules{name,adjust_sign,adjust_value,status,criterias}&access_token=<ACCESS_TOKEN>
```


### Exemplo de resposta


```
{
  "data": [
    {
      "id": "1110000000003",
      "name": "My Value Rule Set",
      "rules": {
        "data": [
          {
            "name": "High age and gender",
            "adjust_sign": "INCREASE",
            "adjust_value": 20,
            "criterias": {
              "data": [
                {
                  "criteria_type": "AGE",
                  "operator": "CONTAINS",
                  "criteria_values": [
                    "18-24"
                  ],
                  "criteria_value_types": [
                    "NONE"
                  ],
                  "id": "1110000000000"
                },
                {
                  "criteria_type": "GENDER",
                  "operator": "CONTAINS",
                  "criteria_values": [
                    "male"
                  ],
                  "criteria_value_types": [
                    "NONE"
                  ],
                  "id": "1110000000001"
                }
              ]
            },
            "id": "1110000000002"
          },
        ]
      }
    }
  ]
}
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como atualizar um conjunto de regras de valor


Para atualizar um conjunto de regras de valor, faça uma solicitação `POST` para o ponto de extremidade `/{value-rule-set-id}`. O corpo da solicitação deve incluir a identificação de todos os objetos existentes que você pretende atualizar, além dos campos adicionados para o conjunto de regras de valor.


### Fluxo de trabalho para atualização do conjunto de regras de valor


O fluxo de trabalho recomendado para atualizar um conjunto de regras de valor é primeiro ler os campos e as identificações existentes por meio de uma solicitação `GET`, atualizar os campos conforme necessário e, depois, fazer uma solicitação `POST` com a carga atualizada.


#### Etapa 1: recuperar o conjunto de regras de valor


Faça uma solicitação `GET` para ver todos os campos e as identificações do conjunto de regras de valor.

```
curl -X GET \ https://graph.facebook.com/v25.0/<VALUE_RULE_SET_ID>?fields=name,rules{name,adjust_sign,adjust_value,status,criterias}&access_token=<ACCESS_TOKEN>
```


A resposta será semelhante a esta:

```
{
  "name": "Value Rule Set",
  "rules": {
    "data": [
      {
        "name": "High age",
        "adjust_sign": "INCREASE",
        "adjust_value": 20,
        "status": "ACTIVE",
        "criterias": {
          "data": [
            {
              "criteria_type": "AGE",
              "operator": "CONTAINS",
              "criteria_values": [
                "18-24"
              ],
              "criteria_value_types": [
                "NONE"
              ],
              "id": "1000000000000089"
            }
          ]
        },
        "id": "1000000000000099"
      }
    ]
  },
  "id": "1000000000000056",
}
```


#### Etapa 2: atualizar o conjunto de regras de valor


#### Exemplo A:


Se você quiser incluir a faixa etária `65+` nos critérios existentes e adicionar um critério de gênero para `FEMALE`, a solicitação `POST` para atualizar esse conjunto de regras de valor deverá ser assim:

```
curl -X POST \ https://graph.facebook.com/v25.0/<VALUE_RULE_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "name": "Value Rule Set", "rules": [ { "name": "High age", "adjust_sign": "INCREASE", "adjust_value": 20, "status": "ACTIVE", "criterias": [ { "criteria_type": "AGE", "operator": "CONTAINS", "criteria_values": [ "18-24", "65+" ], "criteria_value_types": [ "NONE", "NONE" ], "id": "1000000000000089" }, { "criteria_type": "GENDER", "operator": "CONTAINS", "criteria_values": [ "FEMALE" ], "criteria_value_types": [ "NONE" ] } ], "id": "1000000000000099" } ], "id": "1000000000000056" }'
```


#### Exemplo B:


Se você quiser remover o critério de idade, a solicitação `POST` para atualizar esse conjunto de regras de valor deverá ser assim:

```
curl -X POST \ https://graph.facebook.com/v25.0/<VALUE_RULE_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "name": "Value Rule Set", "rules": [ { "name": "High age", "adjust_sign": "INCREASE", "adjust_value": 20, "status": "ACTIVE", "criterias": [ { "criteria_type": "GENDER", "operator": "CONTAINS", "criteria_values": [ "FEMALE" ], "criteria_value_types": [ "NONE" ] } ], "id": "1000000000000099" } ], "id": "1000000000000056" }'
```


#### Exemplo C:


Se você quiser atualizar o nome do conjunto de regras de valor, a solicitação `POST` deverá ser assim:

```
curl -X POST \ https://graph.facebook.com/v25.0/<VALUE_RULE_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "name": "Value Rule Set Updated Name", "rules": [ { "name": "High age", "adjust_sign": "INCREASE", "adjust_value": 20, "status": "ACTIVE", "criterias": [ { "criteria_type": "GENDER", "operator": "CONTAINS", "criteria_values": [ "FEMALE" ], "criteria_value_types": [ "NONE" ] } ], "id": "1000000000000099" } ], "id": "1000000000000056" }'
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como excluir um conjunto de regras de valor


Para excluir um conjunto de regras de valor, faça uma solicitação `POST` para o ponto de extremidade `/{value-rule-set-id}/delete_rule_set` com um corpo de solicitação vazio.


### Exemplo de solicitação


Com a identificação do conjunto de regras que você quer excluir, faça uma solicitação como esta:

```
curl -X POST \ https://graph.facebook.com/v25.0/<VALUE_RULE_SET_ID>/delete_rule_set \ -H 'Authorization: Bearer <ACCESS_TOKEN>'
```


### Exemplo de resposta se `VALUE_RULE_SET_ID` for uma identificação válida


```
{
  "success": true
}
```


### Exemplo de resposta se `VALUE_RULE_SET_ID` for uma identificação inválida


```
{
  "error": {
    "message": "Unsupported post request. Object with ID 'redacted' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at https://developers.facebook.com/docs/graph-api",
    "type": "GraphMethodException",
    "code": 100,
    "error_subcode": 33,
    "fbtrace_id": "fbtrace_id"
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como criar um conjunto de anúncios com um conjunto de regras de valor


Para usar um conjunto de regras de valor em um conjunto de anúncios, adicione `value_rule_set_id` à solicitação de criação do conjunto de anúncios. Para saber mais sobre outros campos do conjunto de anúncios, consulte [Ad Set](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign).


### Exemplo de solicitação


```
curl -X POST \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "name": "My Ad Set", "campaign_id": "<CAMPAIGN_ID>", "value_rule_set_id": "<VALUE_RULE_SET_ID>", "value_rules_applied": true ... // other ad set fields }'
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como anexar um conjunto de regras de valor a um conjunto de anúncios existente


Para anexar um conjunto de regras de valor a um conjunto de anúncios existente, faça uma solicitação `POST` para o ponto de extremidade `/{ad_set_id}`. No corpo da solicitação, defina `value_rules_applied` como `true` e `value_rule_set_id` como a identificação de um conjunto de regras de valor existente.


### Exemplo de solicitação


```
curl -X POST \ https://graph.facebook.com/v25.0/<AD_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "value_rule_set_id": "<VALUE_RULE_SET_ID>", "value_rules_applied": true }'
```


**Observação:** incluir `value_rules_applied` definido como `true` é opcional quando você adiciona um conjunto de regras de valor a conjuntos de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como remover um conjunto de regras de valor de um conjunto de anúncios existente


Para remover o conjunto de regras de valor de um conjunto de anúncios existente, faça uma solicitação `POST` para o ponto de extremidade `/{ad_set_id}`, definindo o campo `value_rules_applied` como `false`, e omita o campo `value_rule_set_id` no corpo da solicitação.


### Exemplo de solicitação


```
curl -X POST \ https://graph.facebook.com/v25.0/<AD_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "value_rules_applied": false }'
```


**Observação:** se você incluir um campo `value_rule_set_id` válido na solicitação `POST`, mesmo com `value_rules_applied` definido como `false`, o conjunto de regras especificado será anexado à campanha. Para remover um conjunto de regras de valor, basta incluir o campo `value_rules_applied` definido como `false`.
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Como substituir o conjunto de regras de valor em um conjunto de anúncios existente


Para substituir o conjunto de regras de valor em um conjunto de anúncios existente, faça uma solicitação `POST` para o ponto de extremidade `/{ad_set_id}` e forneça a nova `value_rule_set_id` no corpo da solicitação. Isso substituirá o conjunto de regras de valor anterior associado ao conjunto de anúncios.


### Exemplo de solicitação


```
curl -X POST \ https://graph.facebook.com/v25.0/<AD_SET_ID> \ -H 'Authorization: Bearer <ACCESS_TOKEN>' \ -H 'Content-Type: application/json' \ -d '{ "value_rule_set_id": "<NEW_VALUE_RULE_SET_ID>", "value_rules_applied": true }'
```


**Observação**: incluir `value_rules_applied` definido como `true` é opcional quando você adiciona um conjunto de regras de valor ao conjunto de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)

## Configurações de conjuntos de anúncios qualificados para conjuntos de regras de valor


Um conjunto de regras de valor pode ser aplicado a todos os conjuntos de anúncios que usam a estratégia de lance `LOWEST_COST_WITHOUT_CAP` (também conhecida como lances automáticos) e que não tenham `VALUE` como meta de otimização, com exceção das seguintes configurações:


### 1. Objetivo da campanha: `OUTCOME_SALES` com local da conversão na web e na loja


```
{
  "optimization_goal": "OFFSITE_CONVERSIONS",
  "promoted_object": {
    "omnichannel_object": {
      "offline": [
        {
          "custom_event_type": "PURCHASE",
          "offline_conversion_data_set_id": "offline_conversion_data_set_id"
        }
      ],
      "pixel": [
        {
          "custom_event_type": "PURCHASE",
          "pixel_id": "pixel_id"
        }
      ]
    }
  }
}
```


### 2. Objetivo da campanha: `OUTCOME_LEADS` com local da conversão na web e em ligações


```
{
  "optimization_goal": "OFFSITE_CONVERSIONS",
  "optimization_sub_event": "NONE",
  "promoted_object": {
    "pixel_id": "pixel_id",
    "custom_event_type": "LEAD"
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)[○](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#)Nesta Página[Regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#regras-de-valor)[Quando usar regras de valor e controles/sugestões de público](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#quando-usar-regras-de-valor-e-controles-sugest-es-de-p-blico)[Como criar um conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-criar-um-conjunto-de-regras-de-valor)[O parâmetro rules](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#o-par-metro-rules)[O parâmetro criteria](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#o-par-metro-criteria)[Os campos criteria_values e criteria_value_types](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#os-campos-criteria-values-e-criteria-value-types)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o)[Como recuperar um conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-recuperar-um-conjunto-de-regras-de-valor)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-2)[Exemplo de resposta](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-resposta)[Como atualizar um conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-atualizar-um-conjunto-de-regras-de-valor)[Fluxo de trabalho para atualização do conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#fluxo-de-trabalho-para-atualiza--o-do-conjunto-de-regras-de-valor)[Como excluir um conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-excluir-um-conjunto-de-regras-de-valor)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-3)[Exemplo de resposta se VALUE_RULE_SET_ID for uma identificação válida](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-resposta-se-value-rule-set-id-for-uma-identifica--o-v-lida)[Exemplo de resposta se VALUE_RULE_SET_ID for uma identificação inválida](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-resposta-se-value-rule-set-id-for-uma-identifica--o-inv-lida)[Como criar um conjunto de anúncios com um conjunto de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-criar-um-conjunto-de-an-ncios-com-um-conjunto-de-regras-de-valor)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-4)[Como anexar um conjunto de regras de valor a um conjunto de anúncios existente](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-anexar-um-conjunto-de-regras-de-valor-a-um-conjunto-de-an-ncios-existente)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-5)[Como remover um conjunto de regras de valor de um conjunto de anúncios existente](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-remover-um-conjunto-de-regras-de-valor-de-um-conjunto-de-an-ncios-existente)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-6)[Como substituir o conjunto de regras de valor em um conjunto de anúncios existente](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#como-substituir-o-conjunto-de-regras-de-valor-em-um-conjunto-de-an-ncios-existente)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#exemplo-de-solicita--o-7)[Configurações de conjuntos de anúncios qualificados para conjuntos de regras de valor](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#configura--es-de-conjuntos-de-an-ncios-qualificados-para-conjuntos-de-regras-de-valor)[1. Objetivo da campanha: OUTCOME_SALES com local da conversão na web e na loja](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#1--objetivo-da-campanha--outcome-sales-com-local-da-convers-o-na-web-e-na-loja)[2. Objetivo da campanha: OUTCOME_LEADS com local da conversão na web e em ligações](https://developers.facebook.com/docs/marketing-api/bidding/value-rules#2--objetivo-da-campanha--outcome-leads-com-local-da-convers-o-na-web-e-em-liga--es) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7u-fQkdepOaOG5-_zRrw0hweS_ZL9Xt4_PueoftXql_oIskwsL3G1Lq4jeYw_aem_XgftOkN5Mr3L-eFCwZ45ew&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6iwPObEBjmTyRUrAEnJVGBwqva2r9-_LqRdrBKcEEPIZu5N2ThKDz4NBjsLQ_aem_Y2EcBCnt1hWtyoAhigqXlQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5luekEQ7ASEDnhgN5DXAgppNVQe_gFSTVXSIo_6UNc1nxY41-jLUejnNyPZQ_aem_b1FVSLXKRAa2rRsGsYFXYg&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ykli96u7oTiCXQUBGEc42pIVT41iMeqSFHzWLj6p8UOMDon6q72_hsS9QOg_aem__Dei7H8lpqjfxPl_RRSKWw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR788DaBZOrj7OGksEtTopbRWzO7oWUU8wo8EDPGLvVIbtW2AfjjxqhzJaO9yg_aem_buDWNqbaa9uN4A9Nc4m_Iw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ykli96u7oTiCXQUBGEc42pIVT41iMeqSFHzWLj6p8UOMDon6q72_hsS9QOg_aem__Dei7H8lpqjfxPl_RRSKWw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47pWEKG74gTMuBuVlMBYlpte6_1N5CD0Ke64vniB-Dnvz9-k89FG4HWzPOGQ_aem_25mK2GvNB56dlLaioZ73RQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZgGANmtQ2I0LzEEfqe7AJhA4qYBJJxe0eqwO99f6r9qti-rMHOTH5hiVKUA_aem_xZHvLV45pPv7fAfhTYWhPg&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR788DaBZOrj7OGksEtTopbRWzO7oWUU8wo8EDPGLvVIbtW2AfjjxqhzJaO9yg_aem_buDWNqbaa9uN4A9Nc4m_Iw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47pWEKG74gTMuBuVlMBYlpte6_1N5CD0Ke64vniB-Dnvz9-k89FG4HWzPOGQ_aem_25mK2GvNB56dlLaioZ73RQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6O7oxXcZhP15qlLqJ8t_c1_9WNBPPp5MI8Lr4wlqAX-MHm3GErst8v_bL1Ag_aem_L-nZZyaCvumn0hgD2oQSog&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR788DaBZOrj7OGksEtTopbRWzO7oWUU8wo8EDPGLvVIbtW2AfjjxqhzJaO9yg_aem_buDWNqbaa9uN4A9Nc4m_Iw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47pWEKG74gTMuBuVlMBYlpte6_1N5CD0Ke64vniB-Dnvz9-k89FG4HWzPOGQ_aem_25mK2GvNB56dlLaioZ73RQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZgGANmtQ2I0LzEEfqe7AJhA4qYBJJxe0eqwO99f6r9qti-rMHOTH5hiVKUA_aem_xZHvLV45pPv7fAfhTYWhPg&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GmHdZ0qjeK4Ln4RDhPq3l_TRdS1Eja0oM4rzLwGv6rZs2DBD46uFoazjuDw_aem_gNpBZqkXMrpKX4ygpH6rFQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6iwPObEBjmTyRUrAEnJVGBwqva2r9-_LqRdrBKcEEPIZu5N2ThKDz4NBjsLQ_aem_Y2EcBCnt1hWtyoAhigqXlQ&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR788DaBZOrj7OGksEtTopbRWzO7oWUU8wo8EDPGLvVIbtW2AfjjxqhzJaO9yg_aem_buDWNqbaa9uN4A9Nc4m_Iw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62m4Eb1ZDOw-hHt8u_qcVUOfQE_2eZXU1jRDd3a932HXP1QwXIOLXvWTb7RQ_aem_jQx-HeLy05sSu9VJhpns6A&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ykli96u7oTiCXQUBGEc42pIVT41iMeqSFHzWLj6p8UOMDon6q72_hsS9QOg_aem__Dei7H8lpqjfxPl_RRSKWw&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62m4Eb1ZDOw-hHt8u_qcVUOfQE_2eZXU1jRDd3a932HXP1QwXIOLXvWTb7RQ_aem_jQx-HeLy05sSu9VJhpns6A&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6PTESuZt5aI8_V9_Op9Eaue2055HM5INoqPde8psL3DrBe05M4J6ll5jh2BHuadqPFBFIPel-9ZGrCR85ySsojwt10gIh9amPD9cH-Z9hUCnrJhW73SFg9I9i1DS12AZdstBIcA58FIaIerYvMzJX1dfg)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão