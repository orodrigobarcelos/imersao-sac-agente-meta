<!-- Fonte: Clique para o WhatsApp - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de clique para o WhatsApp


Este guia explica como criar e publicar anúncios de clique para o WhatsApp usando a API de Marketing.


Os anúncios de clique para o WhatsApp direcionam as pessoas diretamente para conversas com sua empresa no WhatsApp. Esses anúncios podem ser usados para alcançar pessoas em grande escala e fornecer serviço individualizado e com destaque.


Os anúncios de clique para o WhatsApp são compatíveis com anúncios de imagem, vídeo, carrossel ou apresentação multimídia. Também é possível incluir um comando interativo para ligação telefônica nesses anúncios.


Se tiver interesse em criar anúncios que direcionem pessoas para conversas no Messenger ou no Instagram, consulte [Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger) ou [Anúncios de clique para o Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram). Também é possível criar anúncios para o destino no qual o usuário tem mais probabilidade de responder. Para mais informações, acesse [Anúncios de clique com vários destinos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination).


### Visão geral da criação de anúncio


Este documento descreve as etapas que você precisa seguir ao configurar sua integração de anúncios de clique para o WhatsApp.


Você precisará:


- [Criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-1)
- [Criar um conjunto de anúncios que vincula os anúncios à campanha](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-2)
- [Fornecer um criativo para o tipo de anúncio do WhatsApp a ser exibido](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-3)
- [Criar um anúncio vinculando o criativo ao conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-4)
- [Publicar o anúncio no Facebook, Instagram e Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-5)


## Antes de começar


Este guia considera que você já tem o seguinte:


- [Uma conta de anúncios com a Meta](https://adsmanager.facebook.com/adsmanager/)
- [Ativos carregados nos servidores da Meta (como imagens ou vídeos) para usar nos anúncios](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)
- [Uma Página do Facebook com um número de telefone do WhatsApp vinculado](https://www.facebook.com/business/help/1583303048513172?id=2129163877102343) manualmente ou [via API](https://developers.facebook.com/docs/graph-api/reference/page/page_whatsapp_number_verification/)


Para fazer chamadas aos pontos de extremidade deste guia, você precisará do seguinte:


- Um token de acesso à Página solicitado por uma pessoa que pode executar a tarefa ADVERTISE na Página.
- Estas permissões devem ser concedidas a uma pessoa que usa seu app: - `ads_management` - `pages_manage_ads` - `pages_read_engagement` - `pages_show_list`
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)

## Etapa 1: criar uma campanha de anúncios


O primeiro passo é criar a campanha de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/campaigns`, em que `<AD_ACCOUNT_ID>` é a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. Nome da campanha de clique para o WhatsApp. |
| objective enumeração | Obrigatório. Objetivo da campanha. Os objetivos compatíveis são OUTCOME_ENGAGEMENT , OUTCOME_LEADS , OUTCOME_SALES e OUTCOME_TRAFFIC . Observação: em campanhas com comando para ligação, objective deve ser OUTCOME_ENGAGEMENT . |
| special_ad_categories lista\<Object\> | Obrigatório. Categorias de anúncios especiais associadas à campanha de clique para o WhatsApp. Consulte a referência sobre campanha de anúncios para saber mais. |
| status enumeração | Opcional. Opções válidas: PAUSED e ACTIVE . Se o status for PAUSED , todos os respectivos conjuntos de anúncios e anúncios ativos serão pausados e terão status efetivo de CAMPAIGN_PAUSED . |


#### Solicitação padrão


```
curl -X POST \
  -F 'name=Click to WhatsApp Campaign' \
  -F 'objective=OUTCOME_ENGAGEMENT' \
  -F 'status=ACTIVE' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Solicitação de campanha de chamada


```
curl -X POST \
  -F 'name=Click to WhatsApp Calling Campaign' \
  -F 'objective=OUTCOME_ENGAGEMENT' \
  -F 'status=PAUSED' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Resposta


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação da campanha recém-criada.

```
{
  "id": "<AD_CAMPAIGN_ID>"
}
```


### Atualização


É possível atualizar uma campanha fazendo uma solicitação `POST` para `/<AD_CAMPAIGN_ID>`.


### Leitura


Para verificar se você criou com sucesso uma campanha de clique para o WhatsApp, faça uma solicitação `GET` para `/<AD_CAMPAIGN_ID>`. Consulte a [referência sobre campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/#Reading) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=name,status,objective' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>
```


#### Resposta


```
{
  "name": "Click to WhatsApp Campaign",
  "status": "PAUSED",
  "objective": "OUTCOME_ENGAGEMENT",
  "id": "<AD_CAMPAIGN_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)

## Etapa 2: criar um conjunto de anúncios


Quando você já tiver uma campanha, crie um conjunto de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adsets`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição | Exemplo de valor |
| --- | --- | --- |
| bid_amount unsigned int32 | Obrigatório se bid_strategy for definido como LOWEST_COST_WITH_BID_CAP ou COST_CAP . O valor máximo que você deseja pagar por um resultado com base na sua optimization_goal . | 1000 |
| bid_strategy enumeração | Opcional. A estratégia de lance da campanha para atender às suas metas de negócios. Consulte a referência sobre campanha de anúncios para saber mais. Valores: LOWEST_COST_WITHOUT_CAP , LOWEST_COST_WITH_BID_CAP , COST_CAP | LOWEST_COST_WITHOUT_CAP |
| billing_event enumeração | Obrigatório. Precisa ser definido como IMPRESSIONS em anúncios de clique para o WhatsApp. A Meta cobra quando seu anúncio é exibido para as pessoas. | \ IMPRESSIONS |
| campaign_id string numérica ou número inteiro | Obrigatório. Uma campanha de clique para o WhatsApp válida à qual você quer adicionar o conjunto de anúncios. | 4523897324 |
| daily_budget int64 | Obrigatório se lifetime_budget não for definido. O orçamento diário definido na moeda da sua conta. Permitido apenas em conjuntos de anúncios com duração (diferença entre end_time e start_time ) superior a 24 horas. daily_budget ou lifetime_budget precisa ser maior que 0 . | 1 |
| destination_type string | Obrigatório. Defina como WHATSAPP em anúncios de clique para o WhatsApp com um único destino. | WHATSAPP |
| end_time datetime | Obrigatório quando lifetime_budget é especificado. Ao criar um conjunto de anúncios com um daily_budget , especifique end_time=0 ou deixe esse campo vazio para definir que o conjunto está em andamento e não tem data de término. Exemplo: 2015-03-12 23:59:59-07:00 ou 2015-03-12 23:59:59 PDT . Registro de data e hora UNIX (UTC). | 2026-05-12 23:59:59-07:00 |
| lifetime_budget int64 | Obrigatório se daily_budget não for definido. O orçamento total do conjunto de anúncios definido na moeda da sua conta. Se for especificado, será preciso definir também um end_time . daily_budget ou lifetime_budget precisa ser maior que 0 . | 1 |
| name string | Obrigatório. O nome do conjunto de anúncios de clique para o WhatsApp. | Jasper's Market |
| optimization_goal enumeração | Obrigatório. A meta para qual o conjunto de anúncios está sendo otimizado. Dependendo do objetivo da campanha, o conjunto de anúncios pode servir a diferentes metas de otimização. OUTCOME_ENGAGEMENT : o objetivo Engajamento pode otimizar CONVERSATIONS e LINK_CLICKS .; OUTCOME_SALES : o objetivo Vendas pode otimizar CONVERSATIONS , OFFSITE_CONVERSIONS , LINK_CLICKS , IMPRESSIONS e REACH .; OUTCOME_TRAFFIC : o objetivo Tráfego pode otimizar CONVERSATIONS , LANDING_PAGE_VIEWS , LINK_CLICKS , IMPRESSIONS , REACH e POST_ENGAGEMENT .; OUTCOME_LEADS : o objetivo Leads pode otimizar CONVERSATIONS . | OUTCOME_SALES |
| promoted_object AdPromotedObject | Obrigatório. O objeto que o conjunto promove em todos os anúncios. Para anúncios de clique para o WhatsApp, promoted_object inclui as seguintes condições: Obrigatório: page_id : Obrigatório. A identificação da Página do Facebook. Opcional: whatsapp_phone_number : o número de telefone do WhatsApp associado ao conjunto de anúncios de clique para o WhatsApp. Para ver mais detalhes, consulte Conjunto de anúncios, objeto promovido . | { "page_id": "452645324" } |
| start_time datetime | Opcional. A hora de início do conjunto de anúncios. Se nenhum valor for fornecido, este campo será padronizado como a hora atual. Exemplo: 2015-03-12 23:59:59-07:00 ou 2015-03-12 23:59:59 PDT . Registro de data e hora UNIX (UTC). | 2026-03-12 23:59:59-07:00 |
| status enumeração | Opcional. O status do conjunto de anúncios. Pode ser diferente do status efetivo devido à campanha principal. Se nenhum valor for fornecido, este campo será definido como ACTIVE por padrão. Valores: ACTIVE , PAUSED , DELETED , ARCHIVED | ACTIVE |
| targeting Objeto de direcionamento | Obrigatório. A estrutura de direcionamento de um anúncio de clique para o WhatsApp. Consulte Direcionamento para ver mais detalhes. Para habilitar o recurso de status do WhatsApp, consulte Direcionamento de posicionamento e veja mais detalhes. | { "device_platforms": ["mobile"], "geo_locations": { "countries": ["US"] } } |
| time_start datetime | Opcional. Intercambiável com start_time . | 2026-02-14 22:59:59-07:00 |
| time_stop datetime | Obrigatório quando lifetime_budget é especificado. Intercambiável com end_time . | 2026-05-12 23:59:59-07:00 |


Consulte o artigo [Conjuto de anúncios da conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adsets/) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "access_token":"<ACCESS_TOKEN>",
    "bid_amount":"<BID_AMOUNT>",
    "billing_event":"IMPRESSIONS",
    "campaign_id":"<CAMPAIGN_ID>",
    "daily_budget":"<DAILY_BUDGET>",
    "destination_type":"WHATSAPP",
    "name": "<AD_SET_NAME>",
    "optimization_goal": "IMPRESSIONS",
    "promoted_object": {
      "page_id": "<PAGE_ID>"
    },
    "status": "PAUSED",
    "start_time": "<START_TIME>",
    "targeting": {
      "geo_locations": { "countries":["US","CA"] },
      "device_platforms": ["mobile", "desktop"]
    }
  }' \
"https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets"
```


#### Resposta


```
{
  "id": "<AD_SET_ID>"
}
```


### Atualização


É possível atualizar um conjunto de anúncios fazendo uma solicitação `POST` para `/<AD_SET_ID>`.


### Leitura


Para verificar se você criou com sucesso um conjunto de anúncios de clique para o WhatsApp, faça uma solicitação `GET` para `/<AD_SET_ID>`. Consulte a [referência sobre conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=name,destination_type,optimization_goal,bid_strategy,status' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>
```


#### Resposta


```
{
  "name": "Click to WhatsApp Campaign",
  "status": "PAUSED",
  "objective": "OUTCOME_ENGAGEMENT",
  "id": "<AD_SET_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)

## Etapa 3: gerar um criativo do anúncio


Com o criativo, é possível adicionar ativos aos seus anúncios. Para gerar um criativo do anúncio, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adcreatives`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. O nome do criativo do anúncio. |
| object_story_spec AdCreativeObjectStorySpec | Obrigatório. Um objeto que contém informações sobre a mensagem. Consulte Ad Creative Object Story Spec para saber mais. Obrigatório: page_id : a identificação da Página do Facebook. Opcional: link_data : a especificação para um post da Página com link ou um anúncio em carrossel .; photo_data : a especificação para um post da Página com foto.; text_data : a especificação para um post da Página com texto.; video_data : a especificação para um post da Página com vídeo. |
| degrees_of_freedom_spec | Opcional. Consulte Aprimoramentos padrão no criativo Advantage+ para saber mais. |


Acesse a [referência sobre criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


### Como preencher a mensagem de boas-vindas da Página


A mensagem padrão exibida ao cliente é "Olá! Posso acessar mais informações sobre isso?". Você pode criar experiências do usuário mais personalizadas em anúncios de clique para o WhatsApp ajustando a mensagem de saudação no campo `page_welcome_message` em `object_story_spec`.


**Observação:** se você estiver usando a mensagem do WhatsApp para disparar WhatsApp Flows, trabalhe com seu provedor de soluções empresariais e as agências ao atualizá-la para garantir que os fluxos não sejam interrompidos.


### Exemplos


#### Adição de uma mensagem de preenchimento automático com uma mensagem de saudação


```
"page_welcome_message": {
  "type": "VISUAL_EDITOR",
  "version": 2,
  "landing_screen_type": "welcome_message",
  "media_type": "text",
  "text_format": {
    "customer_action_type": "autofill_message",
    "message": {
      "autofill_message": {
        "content": "<AUTOFILL_MESSAGE>"
      },
      "text": "<GREETING_MESSAGE>"
    }
  }
}
```


#### Adição de uma mensagem de saudação automática com uma chamada para ação "Ligar agora"


```
"page_welcome_message": {
     "type": "VISUAL_EDITOR",
     "version": 2,
     "landing_screen_type": "welcome_message",
     "media_type": "text",
     "text_format": {
       "customer_action_type": "autofill_message",
       "message": {
         "text": "<AUTOMATED_GREETING_MESSAGE_TEXT>",
         "automated_greeting_message_cta": {
           "type": "call"
         },
         "autofill_message": {
           "content": "<AUTOFILL_MESSAGE_CONTENT>"
         }
       }
     }
 }
```


#### Adição de uma mensagem de saudação automática com uma chamada para ação "Ver site"


```
"page_welcome_message": {
      "type": "VISUAL_EDITOR",
      "version": 2,
      "landing_screen_type": "welcome_message",
      "media_type": "text",
      "text_format": {
        "customer_action_type": "autofill_message",
        "message": {
          "text": "<AUTOMATED_GREETING_MESSAGE_TEXT>",
          "automated_greeting_message_cta": {
            "type": "url",
            "url": "<WEBSITE_URL>"
          },
          "autofill_message": {
           "content": "<AUTOFILL_MESSAGE_CONTENT>"
          }
        }
      }
    }
```


#### Adição de uma mensagem de saudação automática com uma chamada para ação "Ver catálogo"


```
"page_welcome_message": {
  "type": "VISUAL_EDITOR",
  "version": 2,
  "landing_screen_type": "welcome_message",
  "media_type": "text",
  "text_format": {
    "customer_action_type": "autofill_message",
    "message": {
      "text": "<AUTOMATED_GREETING_MESSAGE_TEXT>",
      "automated_greeting_message_cta": {
        "type": "catalog"
      },
      "autofill_message": {
        "content": "<AUTOFILL_MESSAGE_CONTENT>"
      }
    }
  }
}
```


#### Adição de uma mensagem de saudação automática com uma chamada para ação "Fluxos"


Somente fluxos que se encaixem nos seguintes critérios podem ser usados para criar um criativo do anúncio:


- WhatsApp Flows versão > 5.1
- Sem erros de validação
- Fluxo estático (ou seja, um fluxo sem troca de dados)
- Tela única
- Apenas componentes qualificados: - Título do texto - Subtítulo do texto - Corpo do texto - Legenda do texto - Entrada de texto - Área de texto - Seletor de data - Grupo de botões de opção - Rodapé - Grupo da caixa de seleção
- Não mais de oito componentes na tela
- Pelo menos um componente de entrada, como: - Entrada de texto - Área de texto - Seletor de data - Grupo de botões de opção - Grupo da caixa de seleção

```
"page_welcome_message": {
  "type": "VISUAL_EDITOR",
  "version": 2,
  "landing_screen_type": "ctwa_flows",
  "media_type": "text",
  "text_format": {
    "customer_action_type": "whatsapp_flow",
    "message": {
      "text": "<AUTOMATED_GREETING_MESSAGE_TEXT>",
      "automated_greeting_message_cta": {
        "type": "flow",
        "flow_data":{
          "call_to_action":"Apply now",
          "flow_id":"<FLOW_ID>"
        }
      },
      "autofill_message": {
        "content": "<AUTOFILL_MESSAGE_CONTENT>"
      }
    }
  }
}
```


**Observação:** o `flow_id` passado acima deve pertencer à mesma conta do WhatsApp Business que a do número de telefone promovido no conjunto de anúncios. Ver mais sobre o [WhatsApp Flows](https://developers.facebook.com/docs/whatsapp/flows/gettingstarted/).


#### Adição de quebra-gelos com uma mensagem de saudação


```
"page_welcome_message": {
  "type": "VISUAL_EDITOR",
  "version": 2,
  "landing_screen_type": "welcome_message",
    "media_type": "text",
    "text_format": {
      "customer_action_type": "ice_breakers",
      "message": {
        "text": "<GREETING_MESSAGE>",
        "ice_breakers": [
          {
            "title": "<ICEBREAKER>"
          },
          {
            "title": "<ICEBREAKER>"
          },
          {
            "title": "<ICEBREAKER>"
          }
        ]
      }
    }
  }
}
```


#### Como adicionar mensagem com um comando interativo de ligação


```
curl \
  -F 'object_story_spec={
      "page_id": "<PAGE_ID>"
      "link_data": {
     "image_hash":<IMAGE_HASH>
            "call_to_action": {
              	"type": "WHATSAPP_MESSAGE",
              	"value": {
                  	"app_destination": "WHATSAPP"
             	 }
          },
          "link": "https://api.whatsapp.com/send",
          "name": <AD_HEADLINE>",
          "page_welcome_message":
       "type": "VISUAL_EDITOR",
        "version": 2,
        "landing_screen_type": "ctwa_call_prompt",
        "media_type": "text",
        "text_format": {
          "message": {
            "text": "<MESSAGE>"",
            "call_prompt_data": {
              "call_prompt_message": "<CALL_PROMPT_MESSAGE>"
            }
          }
        },
        "user_edit": false
      },
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Resposta


```
{
  "id": "<AD_CREATIVE_ID>"
}
```


### Exemplos de como gerar um criativo do anúncio


#### Solicitação


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Sample ad creative",
        "object_story_spec": {
          "page_id": "<PAGE_ID>",
          "link_data": {
            "name": "<AD_HEADLINE>",
            "message": "<AD_PRIMARY_TEXT>",
            "description": "<AD_DESCRIPTION>",
            "image_hash": "<IMAGE_HASH>",
            "link": "https://api.whatsapp.com/send",
            "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
            "call_to_action": {
              "type": "WHATSAPP_MESSAGE",
              "value": {
                "app_destination": "WHATSAPP"
              }
            }
          }
        },
        "degrees_of_freedom_spec": {
          "creative_features_spec": {
            "standard_enhancements": {
              "enroll_status": "OPT_IN"
            }
          }
        }
      }' \
"https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives"
```


#### Resposta


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação do criativo do anúncio recém-gerado.

```
{
  "id": "<AD_CREATIVE_ID>"
}
```


### Anúncio que usa uma sequência de mensagens configurada em um app parceiro.


```
curl -X POST "https://graph.facebook.com/v25.0/act_<AD_ACCCOUNT_ID>/adcreatives"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "<PAGE_ACCESS_TOKEN>",
           "name": "<IMAGE_AD_NAME>",
           "object_story_spec": {
             "page_id": "<PAGE_ID>",
             "link_data": {
               "image_hash": "<IMAGE_HASH>",
               "link": "<IMAGE_URL>",
               "call_to_action": {
                 "type": "WHATSAPP_MESSAGE",
                 "value":{"app_destination":"WHATSAPP"}
               }
             }
           },
           "asset_feed_spec": {
             "additional_data": {
               "partner_app_welcome_message_flow_id": "SEQUENCE-ID"
             }
           }
         }'
```


Para saber mais sobre sequências de mensagens, consulte [Sequências de mensagem de boas-vindas](https://developers.facebook.com/docs/whatsapp/business-management-api/ads/welcome-message-sequences) na documentação da plataforma do WhatsApp Business.


### Como gerar criativos de anúncio usando conteúdo do Instagram


Você também pode usar o conteúdo existente do Instagram para gerar criativos.

```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "source_instagram_media_id": "<INSTAGRAM_MEDIA_ID>",
        "instagram_user_id": "<INSTAGRAM_USER_ID>",
        "object_id": "<PAGE_ID>",
        "call_to_action": {
          "type": "WHATSAPP_MESSAGE",
            "value": {
              "link": "https://api.whatsapp.com/send",
              "app_destination": "WHATSAPP"
            }
          }
        },
        "degrees_of_freedom_spec": {
          "creative_features_spec": {
            "standard_enhancements": {
              "enroll_status": "OPT_IN"
            }
          }
        }
      }' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Atualização


É possível atualizar um [criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) fazendo uma solicitação `POST` para `/<AD_CREATIVE_ID>`.


### Leitura


Para verificar se você criou com sucesso um criativo do anúncio de clique para o WhatsApp, faça uma solicitação `GET` para `/<AD_CREATIVE_ID>`. Consulte [Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=name,object_story_spec{link_data{call_to_action,page_welcome_message}}' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>
```


#### Resposta


```
{
  "name": "Sample ad creative",
  "object_story_spec" {
    "page_welcome_message": {
      "type": "VISUAL_EDITOR",
      "version": 2,
      "landing_screen_type": "welcome_message",
      "media_type": "text",
      "text_format": {
        "customer_action_type": "autofill_message",
        "message": {
          "autofill_message": {
            "content": "Sample autofill message"
          },
        "text": "Sample greeting message"
        }
      }
    }
  },
  "id": "<AD_CREATIVE_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)

## Etapa 4: criar um anúncio


Os anúncios permitem que você associe informações do criativo aos seus conjuntos de anúncios. Para criar um anúncio, envie uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/ads`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. O nome do anúncio. |
| adset_id string numérica ou número inteiro | Obrigatório. A identificação do conjunto de anúncios. |
| creative AdCreative | Obrigatório. O criativo que deve ser usado pelo anúncio. Você pode fornecer o creative_id de um criativo existente ou gerar um novo incluindo todos os campos obrigatórios. Consulte Ad Creative para saber mais. |
| status enumeração | Obrigatório. O status do anúncio. Valores: ACTIVE , PAUSED , DELETED , ARCHIVED |


#### Solicitação


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Sample ad",
        "adset_id": "<AD_SET_ID>",
        "creative": {
          "creative_id": "<AD_CREATIVE_ID>"
        },
        "status": "PAUSED"
     }' \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads"
```


#### Resposta


```
{
  "id": "<AD_ID>"
}
```


### Atualização


É possível atualizar um [anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) fazendo uma solicitação `POST` para `/<AD_ID>`.


### Leitura


Para verificar se você criou com sucesso um anúncio de clique para o WhatsApp, faça uma solicitação `GET` para `/<AD_ID>`. Consulte a [referência sobre anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=status,adset_id,campaign_id \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


#### Resposta


```
{
  "status": "PAUSED",
  "adset_id": "<AD_SET_ID>",
  "campaign_id": "<AD_CAMPAIGN_ID>",
  "id": "<AD_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)

## Etapa 5: publicar o anúncio


Confira se o anúncio aparece no Gerenciador de Anúncios. Quando estiver tudo pronto para publicar suas alterações, selecione a campanha, o conjunto de anúncios da campanha e o anúncio. Depois, clique no botão **Publicar**.


Também é possível publicar o anúncio via API. Para isso, basta enviar uma solicitação `POST` para `/<AD_ID>` com o parâmetro `status` definido como `ACTIVE`, sendo `<AD_ID>` o anúncio que você quer publicar.


O anúncio ficará com o status `PENDING_REVIEW` e será analisado pela Meta. Depois da aprovação, o status será automaticamente atualizado para `ACTIVE`, e o anúncio será veiculado.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#)Nesta Página[Anúncios de clique para o WhatsApp](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#an-ncios-de-clique-para-o-whatsapp)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#antes-de-come-ar)[Etapa 1: criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-1)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#par-metros)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#atualiza--o)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#leitura)[Etapa 2: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-2)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#par-metros-2)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#atualiza--o-2)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#leitura-2)[Etapa 3: gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-3)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#par-metros-3)[Como preencher a mensagem de boas-vindas da Página](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#como-preencher-a-mensagem-de-boas-vindas-da-p-gina)[Exemplos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#exemplos)[Exemplos de como gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#exemplos-de-como-gerar-um-criativo-do-an-ncio)[Anúncio que usa uma sequência de mensagens configurada em um app parceiro.](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#an-ncio-que-usa-uma-sequ-ncia-de-mensagens-configurada-em-um-app-parceiro-)[Como gerar criativos de anúncio usando conteúdo do Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#como-gerar-criativos-de-an-ncio-usando-conte-do-do-instagram)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#atualiza--o-3)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#leitura-3)[Etapa 4: criar um anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-4)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#par-metros-4)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#atualiza--o-4)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#leitura-4)[Etapa 5: publicar o anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp#step-5) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5eHrVoMGAlJv4WQerZNHuzaQPw174-XhmjIDNsL8G6xsQeXoA697IKx7vVeQ_aem_uJholL-EqBRLVLv1pC9Ofg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZVovhuJ-CL_9qnF6Yy5mjPsXbY8uZ69_9bVggUnON-UoDPal1mx2vkNP_ng_aem_nxZJBn1JFzulFkik1g2g4A&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR57AEX_63dOZ5rco91uglNZUsrERElPDa3bn1fi-ocibamjlaABTKq1F0H4jQ_aem_aEmqemuY6Qu6tZtZEt1XxA&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ExfANy4LcYymepBUFfwSe5DmYaAQiCD2jb-H--sOKS9ak3Kut25YQ65ztbw_aem_s2XZmJ4dBQLmOxGCMui-hA&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-EdP8s6OxGvaK5YjEFxsvshtiji9hYSM-mzKRv0omGim5CSHbE3t2MvuJJA_aem__NRXorBKfadHyADUc39czw&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZceUTlLOszifbccfiHthZDv-txPSf9VegF_z7Uv5mXtHHcz0vcMI1eV-lQ_aem_6sufL2rRgEbEhrpbSglZkg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZceUTlLOszifbccfiHthZDv-txPSf9VegF_z7Uv5mXtHHcz0vcMI1eV-lQ_aem_6sufL2rRgEbEhrpbSglZkg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5eHrVoMGAlJv4WQerZNHuzaQPw174-XhmjIDNsL8G6xsQeXoA697IKx7vVeQ_aem_uJholL-EqBRLVLv1pC9Ofg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vD3tmbdUkaeMbnulAJdQaxN3MNgCRRXmvQB1IHcQRiGNqO7M9Tee0coJCgQ_aem_nL6BR0NJH_gUkHDepdEYCw&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ExfANy4LcYymepBUFfwSe5DmYaAQiCD2jb-H--sOKS9ak3Kut25YQ65ztbw_aem_s2XZmJ4dBQLmOxGCMui-hA&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51CtXCbuw7-mMunuUabo-iV02ubWiIVcy_TYZYyvrQhoX0wD9t7Jgd6cWjCQ_aem_lgnjHlCDvtRax18mJAlRsQ&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZceUTlLOszifbccfiHthZDv-txPSf9VegF_z7Uv5mXtHHcz0vcMI1eV-lQ_aem_6sufL2rRgEbEhrpbSglZkg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51CtXCbuw7-mMunuUabo-iV02ubWiIVcy_TYZYyvrQhoX0wD9t7Jgd6cWjCQ_aem_lgnjHlCDvtRax18mJAlRsQ&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZceUTlLOszifbccfiHthZDv-txPSf9VegF_z7Uv5mXtHHcz0vcMI1eV-lQ_aem_6sufL2rRgEbEhrpbSglZkg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5eHrVoMGAlJv4WQerZNHuzaQPw174-XhmjIDNsL8G6xsQeXoA697IKx7vVeQ_aem_uJholL-EqBRLVLv1pC9Ofg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gZceUTlLOszifbccfiHthZDv-txPSf9VegF_z7Uv5mXtHHcz0vcMI1eV-lQ_aem_6sufL2rRgEbEhrpbSglZkg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5eHrVoMGAlJv4WQerZNHuzaQPw174-XhmjIDNsL8G6xsQeXoA697IKx7vVeQ_aem_uJholL-EqBRLVLv1pC9Ofg&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51CtXCbuw7-mMunuUabo-iV02ubWiIVcy_TYZYyvrQhoX0wD9t7Jgd6cWjCQ_aem_lgnjHlCDvtRax18mJAlRsQ&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-EdP8s6OxGvaK5YjEFxsvshtiji9hYSM-mzKRv0omGim5CSHbE3t2MvuJJA_aem__NRXorBKfadHyADUc39czw&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vD3tmbdUkaeMbnulAJdQaxN3MNgCRRXmvQB1IHcQRiGNqO7M9Tee0coJCgQ_aem_nL6BR0NJH_gUkHDepdEYCw&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6XSuNXRuP8dUgGQiMP2c4JPv_bz-YvqV1tLftMbxsD65AILh5DRBX_IlW6drEm2LEOdQIEPL17I9AKeazLEhfVTn79L3qfLH58T5ypIdwODbAu05jo_-NYuWriDDRS40Hj2mUqdwg22giqhMPRfBNAXJk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão