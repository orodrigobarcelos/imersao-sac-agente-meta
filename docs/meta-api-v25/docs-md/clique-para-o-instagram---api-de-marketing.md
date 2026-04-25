<!-- Fonte: Clique para o Instagram - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de clique para o Instagram


Este guia explica como criar e publicar anúncios de clique para o Instagram usando a API de Marketing.


Os anúncios de clique para o Instagram Direct direcionam as pessoas diretamente para conversas com sua empresa no Instagram Direct. Esses anúncios podem ser usados para alcançar pessoas em grande escala e fornecer serviço individualizado e com destaque.


Os anúncios de clique para o Instagram são compatíveis com anúncios de imagem, vídeo, carrossel ou apresentação multimídia. Também é possível incluir um comando interativo para ligação telefônica nesses anúncios.


Se tiver interesse em criar anúncios que direcionem as pessoas para conversas no Messenger ou no WhatsApp, consulte [Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp) e [Anúncios de clique para o WhatsApp](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp). Também é possível criar anúncios para o destino no qual o usuário tem mais probabilidade de responder. Para mais informações, acesse [Anúncios de clique com vários destinos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination).


### Visão geral da criação de anúncio


Este documento descreve as etapas que você precisa seguir ao configurar sua integração de anúncios de clique para o Instagram. Você precisará fazer o seguinte:


- [Criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-1)
- [Criar um conjunto de anúncios que vincula os anúncios à campanha](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-2)
- [Fornecer um criativo para o tipo de anúncio do Instagram a ser exibido](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-3)
- [Criar um anúncio vinculando o criativo ao conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-4)
- [Publicar o anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-5)


## Antes de começar


Este guia considera que você já tem o seguinte:


- [Uma conta de anúncios com a Meta](https://adsmanager.facebook.com/adsmanager/)
- [Uma conta do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#account-id)
- [Ativos carregados nos servidores da Meta (como imagens ou vídeos) para usar nos anúncios](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)


Para fazer chamadas aos pontos de extremidade deste guia, você precisará do seguinte:


- Um token de acesso à Página solicitado por uma pessoa que pode executar a tarefa ADVERTISE na Página.
- Estas permissões devem ser concedidas a uma pessoa que usa seu app: - `ads_management` - `pages_manage_ads` - `pages_read_engagement` - `pages_show_list`
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)

## Etapa 1: criar uma campanha de anúncios


O primeiro passo é criar a campanha de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/campaigns`, em que `<AD_ACCOUNT_ID>` é a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. Nome da campanha de clique para o Instagram. |
| objective enumeração | Obrigatório. Objetivo da campanha. Objetivos compatíveis: OUTCOME_ENGAGEMENT , OUTCOME_SALES e OUTCOME_TRAFFIC . |
| special_ad_categories lista\<Object\> | Obrigatório. Categorias de anúncio especial associadas à campanha de clique para o Instagram. Consulte a referência sobre campanha de anúncios para saber mais. |
| status enumeração | Opcional. Opções válidas: PAUSED e ACTIVE . Se o status for PAUSED , todos os respectivos conjuntos de anúncios e anúncios ativos serão pausados e terão status efetivo de CAMPAIGN_PAUSED . |


#### Solicitação


```
curl -X POST \
  -F 'name=Click to Instagram Campaign' \
  -F 'objective=OUTCOME_ENGAGEMENT' \
  -F 'status=ACTIVE' \
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


Para verificar se você criou com sucesso uma campanha de clique para o Instagram, faça uma solicitação `GET` para `/<AD_CAMPAIGN_ID>`. Consulte a [referência sobre campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/#Reading) para ver uma lista completa dos parâmetros disponíveis.


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
  "name": "Click to Instagram Campaign",
  "status": "ACTIVE",
  "objective": "OUTCOME_ENGAGEMENT",
  "id": "<AD_CAMPAIGN_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)

## Etapa 2: criar um conjunto de anúncios


Quando você já tiver uma campanha, crie um conjunto de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adsets`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| bid_amount unsigned int32 | Obrigatório se bid_strategy for definido como LOWEST_COST_WITH_BID_CAP ou COST_CAP . O valor máximo que você deseja pagar por um resultado com base na sua optimization_goal . |
| bid_strategy enumeração | Opcional. A estratégia de lance da campanha para atender às suas metas de negócios. Consulte a referência sobre campanha de anúncios para saber mais. Valores: LOWEST_COST_WITHOUT_CAP , LOWEST_COST_WITH_BID_CAP , COST_CAP |
| billing_event enumeração | Obrigatório. Precisa ser definido como IMPRESSIONS em anúncios de clique para o Instagram. A Meta cobra quando seu anúncio é exibido para as pessoas. |
| campaign_id string numérica ou número inteiro | Obrigatório. Uma campanha de clique para o Instagram válida à qual você quer adicionar o conjunto de anúncios. |
| daily_budget int64 | Obrigatório se lifetime_budget não for definido. O orçamento diário definido na moeda da sua conta. Permitido apenas em conjuntos de anúncios com duração (diferença entre end_time e start_time ) superior a 24 horas. daily_budget ou lifetime_budget precisa ser maior que 0 . |
| destination_type string | Obrigatório. Defina como INSTAGRAM_DIRECT em anúncios de clique para o Instagram com um único destino. |
| end_time datetime | Obrigatório quando lifetime_budget é especificado. Ao criar um conjunto de anúncios com um daily_budget , especifique end_time=0 ou deixe esse campo vazio para definir que o conjunto está em andamento e não tem data de término. Exemplo: 2015-03-12 23:59:59-07:00 ou 2015-03-12 23:59:59 PDT . Registro de data e hora UNIX (UTC). |
| lifetime_budget int64 | Obrigatório se daily_budget não for definido. O orçamento total do conjunto de anúncios definido na moeda da sua conta. Se for especificado, será preciso definir também um end_time . daily_budget ou lifetime_budget precisa ser maior que 0 . |
| name string | Obrigatório. Nome do conjunto de anúncios de clique para o Instagram. |
| optimization_goal enumeração | Obrigatório. A meta para qual o conjunto de anúncios está sendo otimizado. Dependendo do objetivo da campanha, o conjunto de anúncios pode servir a diferentes metas de otimização. OUTCOME_ENGAGEMENT : o objetivo de engajamento pode otimizar para CONVERSATIONS e LINK_CLICKS . OUTCOME_SALES : o objetivo de vendas pode otimizar para CONVERSATIONS , OFFSITE_CONVERSIONS , LINK_CLICKS , IMPRESSIONS e REACH . OUTCOME_TRAFFIC : o objetivo de tráfego pode otimizar para CONVERSATIONS , LANDING_PAGE_VIEWS , LINK_CLICKS , IMPRESSIONS , REACH e POST_ENGAGEMENT . |
| promoted_object AdPromotedObject | Obrigatório. O objeto que o conjunto promove em todos os anúncios. Em anúncios de clique para o Instagram, promoted_object inclui as seguintes condições: page_id : Obrigatório. A identificação da Página do Facebook. Consulte Ad Set, Promoted Object para saber mais. |
| start_time datetime | Opcional. A hora de início do conjunto de anúncios. Se nenhum valor for fornecido, este campo será padronizado como a hora atual. Exemplo: 2015-03-12 23:59:59-07:00 ou 2015-03-12 23:59:59 PDT . Registro de data e hora UNIX (UTC). |
| status enumeração | Opcional. O status do conjunto de anúncios. Pode ser diferente do status efetivo devido à campanha principal. Se nenhum valor for fornecido, este campo será definido como ACTIVE por padrão. Valores: ACTIVE , PAUSED , DELETED , ARCHIVED |
| targeting Objeto de direcionamento | Obrigatório. A estrutura de direcionamento de um anúncio de clique para o Instagram. Consulte Direcionamento básico para saber mais. |
| time_start datetime | Opcional. Intercambiável com start_time . |
| time_stop datetime | Obrigatório quando lifetime_budget é especificado. Intercambiável com end_time . |


Consulte o artigo [Ad Account Adsets](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adsets/) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X POST \
  -F 'access_token=<ACCESS_TOKEN>' \
  -F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'campaign_id=<AD_CAMPAIGN_ID>' \
  -F 'daily_budget=<DAILY_BUDGET>' \
  -F 'destination_type=INSTAGRAM_DIRECT' \
  -F 'name=Click to Instagram Ad Set' \
  -F 'optimization_goal=CONVERSATIONS' \
  -F 'promoted_object={
    "page_id": "<PAGE_ID>"
  }' \
  -F 'status=ACTIVE' \
  -F 'start_time=<START_TIME>' \
  -F 'targeting={
    "geo_locations": { "countries":["US","CA"] },
    "device_platforms": ["mobile", "desktop"]
  }' \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/adsets
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


Para verificar se você criou com sucesso um conjunto de anúncios de clique para o Instagram, faça uma solicitação `GET` para `/<AD_SET_ID>`. Consulte a [referência sobre conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) para ver uma lista completa dos parâmetros disponíveis.


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
  "name": "Click to Instagram Ad Set",
  "destination_type": "INSTAGRAM_DIRECT",
  "optimization_goal": "CONVERSATIONS",
  "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
  "status": "ACTIVE",
  "id": "<AD_SET_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)

## Etapa 3: gerar um criativo do anúncio


Com o criativo, é possível adicionar ativos aos seus anúncios. Para gerar um criativo do anúncio, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adcreatives`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. O nome do criativo do anúncio. |
| object_story_spec AdCreativeObjectStorySpec | Obrigatório. Um objeto que contém informações sobre a mensagem. Consulte Ad Creative Object Story Spec para saber mais. Obrigatório: page_id : a identificação da Página do Facebook.; instagram_actor_id : a identificação da conta do Instagram. Há três formas de obter a identificação de uma conta do Instagram : conta do Instagram de propriedade do Gerenciador de Negócios, conta do Instagram conectada à Página e conta do Instagram associada à Página. Opcional: link_data : a especificação para um post da Página com link ou um anúncio em carrossel .; photo_data : a especificação para um post da Página com foto.; text_data : a especificação para um post da Página com texto.; video_data : a especificação para um post da Página com vídeo. |
| degrees_of_freedom_spec | Opcional. Consulte Aprimoramentos padrão no criativo Advantage+ para saber mais. |


Acesse a [referência sobre criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


Caso você veja o erro "O criativo deve fornecer enroll_status para aprimoramentos padrão" na versão 17.0 ou posterior, consulte [Aprimoramentos padrão no Criativo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements) e faça as correções necessárias.


### Como preencher a mensagem de boas-vindas da Página


A mensagem padrão exibida ao cliente é "Olá! Posso obter mais informações sobre isso?". Você pode criar experiências do usuário mais personalizadas em anúncios de clique para o Instagram ajustando a mensagem de saudação no campo `page_welcome_message` em `object_story_spec`.


#### Exemplo


Veja como adicionar quebra-gelos de texto com uma resposta automática opcional. A interpolação de strings `{{user_first_name}}`, `{{user_last_name}}`, `{{user_full_name}}` e `{{page_name}}` pode ser usada na mensagem de saudação e na resposta automática. Por exemplo, "Olá, {{user_first_name}}. Esta é a página {{page_name}}!".

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
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        },
        {
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        },
        {
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        }
      ]
    }
  }
}
```


### Exemplos de como gerar um criativo do anúncio


#### Criativo de imagem


Consulte [Ad, Image](https://developers.facebook.com/docs/marketing-api/reference/ad-image/) para saber mais.

```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "image_hash": "<IMAGE_HASH>"
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         }
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Criativo de vídeo


Consulte [Anúncios em vídeo e em carrossel](https://developers.facebook.com/docs/marketing-api/guides/videoads/) para saber mais.

```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "message": "<AD_PRIMARY_TEXT>",
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "video_data": {
         "video_id": "<VIDEO_ID>",
         "image_url": "<THUMBNAIL_URL>"
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         }
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Anúncio que usa um fluxo de mensagens configurado em um app parceiro


```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "image_hash": "<IMAGE_HASH>"
           "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         }
       }
     }' \
  -F 'asset_feed_spec={
       "additional_data": {
         "partner_app_welcome_message_flow_id": "<FLOW_ID>",
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v19.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Para saber mais sobre fluxos de mensagens em apps, consulte [Welcome message flows](https://developers.facebook.com/docs/messenger-platform/ads/ads-welcome-message-flows) na documentação da plataforma do Messenger.


#### Criativo de carrossel


Consulte [Anúncios em vídeo e em carrossel](https://developers.facebook.com/docs/marketing-api/guides/videoads/) para saber mais.

```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         },
         "child_attachments": [
              {
                "image_hash": "<IMAGE_HASH>",
                "call_to_action": {
                  "type": "INSTAGRAM_MESSAGE",
                  "value": {
                    "app_destination": "INSTAGRAM_DIRECT"
                  }
                },
                "name": "<AD_HEADLINE>"
              },
              {
                "video_id": "<VIDEO_ID>",
                "picture": "<THUMBNAIL_URL>",
                "call_to_action": {
                  "type": "INSTAGRAM_MESSAGE",
                  "value": {
                    "app_destination": "INSTAGRAM_DIRECT"
                  }
                },
                "name": "<AD_HEADLINE>"
              }
         ],
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Resposta


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação do criativo do anúncio recém-gerado.

```
{
  "id": "<AD_CREATIVE_ID>"
}
```


### Como gerar criativos de anúncio usando conteúdo do Instagram


#### Posts do Instagram


Consulte [Usar posts como anúncios do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads/) para saber mais.

```
curl -X POST \
  -F 'name=Sample ad creative from Instagram post' \
  -F 'object_id=<PAGE_ID>' \
  -F 'instagram_user_id=<INSTAGRAM_USER_ID>' \
  -F 'source_instagram_media_id=<INSTAGRAM_POST_ID>' \
  -F 'call_to_action={
       "type": "INSTAGRAM_MESSAGE",
       "value": {
         "link": "https://www.instagram.com"
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Imagens do Instagram


```
curl -X POST \
  -F 'name=Sample ad creative from Instagram image' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACTOR_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "picture": "<IMAGE_URL>"
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         }
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Como gerar criativos do anúncio usando conteúdo do Facebook


Consulte [Usar publicações como anúncios do Instagram: publicações do Facebook](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads/#facebook-posts) para saber mais.

```
curl -i -X POST \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives
  ?object_story_id=<postOwnerID_postID>
  &instagram_actor_id=<IG_USER_ID>
  &call_to_action="{'type':MESSAGE_PAGE,'value':{'app_destination':'MESSENGER'}}"
  &access_token=<ACCESS_TOKEN>"
```


Onde `object_story_id` é a identificação da publicação no formato `postOwnerID_postID` e `instagram_actor_id` é uma identificação da conta do Instagram conectada à Página ou a identificação da conta do Instagram associada à Página. Veja mais detalhes em [Set Up Instagram Accounts With Pages](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account).


### Atualização


É possível atualizar um [criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) fazendo uma solicitação `POST` para `/<AD_CREATIVE_ID>`.


### Leitura


Para verificar se você criou com sucesso um criativo do anúncio de clique para o Instagram, faça uma solicitação `GET` para `/<AD_CREATIVE_ID>`. Consulte [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


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
  "object_story_spec": {
    "link_data": {
      "call_to_action": {
        "type": "INSTAGRAM_MESSAGE",
        "value": {
          "app_destination": "INSTAGRAM_DIRECT"
        }
      },
      "page_welcome_message": {
        "type": "VISUAL_EDITOR",
        "version": 2,
        "landing_screen_type": "welcome_message",
        "media_type": "text",
        "text_format": {
          "customer_action_type": "ice_breakers",
          "message": {
            "text": "Sample greeting message",
            "ice_breakers": [
              {
                "title": "Sample icebreaker 1"
              },
              {
                "title": "Sample icebreaker 2"
              },
              {
                "title": "Sample icebreaker 3"
              }
            ]
          }
        }
      }
    }
  },
  "id": "<AD_CREATIVE_ID>"
}
```


### Identificação do objetivo alternativo na geração de um criativo do anúncio


Use esta API para conectar contas do Instagram com a identificação da Página associada à conta do Instagram (IABP ID, pelas iniciais em inglês).

```
curl -X GET \
  -F 'fields="iabp_id"' \
  -F 'business_id=<BUSINESS_ID>' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/connected_instagram_accounts_with_iabp
```


Depois, quando você [usar posts como anúncios](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads/), será possível aplicar a "IABP ID" como o valor da `object_id`.

```
curl -i -X POST \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives
  ?object_id=<IABP_ID> // iabp_id instead of page_id
  &instagram_user_id=<IG_USER_ID>
  &source_instagram_media_id=<IG_ORGANIC_MEDIA_ID>
  &access_token=<API_ACCESS_TOKEN>"
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)

## Etapa 4: criar um anúncio


Os anúncios permitem que você associe informações do criativo aos seus conjuntos de anúncios. Para criar um anúncio, envie uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/ads`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. O nome do criativo do anúncio. |
| adset_id string numérica ou número inteiro | Obrigatório. A identificação do conjunto de anúncios. |
| creative AdCreative | Obrigatório. O criativo que deve ser usado pelo anúncio. Você pode fornecer o creative_id de um criativo existente ou gerar um novo incluindo todos os campos obrigatórios. Consulte Ad Creative para saber mais. |
| status enumeração | Obrigatório. O status do anúncio. Valores: ACTIVE , PAUSED , DELETED , ARCHIVED |


#### Solicitação


```
curl -X POST \
  -F 'name=Click to Instagram Ad' \
  -F 'adset_id=<AD_SET_ID> \
  -F 'creative={
       "creative_id": "<AD_CREATIVE_ID>"
     }' \
  -F 'status=PAUSED \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### Resposta


```
{
  "id": "<AD_ID>"
}
```


### Chamada para ação


Também é possível definir uma chamada para ação ao criar um anúncio.

```
"call_to_action": {
  "value": {"app_destination":"INSTAGRAM_DIRECT"},
  "type": "MESSAGE_PAGE"
}
```


### Atualização


É possível atualizar um [anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) fazendo uma solicitação `POST` para `/<AD_ID>`.


### Leitura


Para verificar se você criou com sucesso um anúncio de clique para o Instagram, faça uma solicitação `GET` para `/<AD_ID>`. Consulte a [referência sobre anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) para ver uma lista completa dos parâmetros disponíveis.


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
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)

## Etapa 5: publicar o anúncio


Confira se o anúncio aparece no Gerenciador de Anúncios. Quando estiver tudo pronto para publicar suas alterações, selecione a campanha, o conjunto de anúncios da campanha e o anúncio. Depois, clique no botão **Publicar**.


Você também pode publicar seu anúncio via API enviando uma solicitação `POST` para `/<AD_ID>` com o parâmetro `status` definido como `ACTIVE`, sendo `<AD_ID>` o anúncio que você quer publicar.


### Solicitação


```
curl -X POST \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


### Resposta


```
{
  "success": true
}
```


O anúncio será analisado pela Meta e terá o `effective_status` de `PENDING_REVIEW`. Depois da aprovação, o status será automaticamente atualizado para `ACTIVE`, e o anúncio será veiculado.


### Solicitação


```
curl -X GET -G \
  -d 'fields=status,effective_status' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


### Resposta


```
{
  "status": "ACTIVE",
  "effective_status": "PENDING_REVIEW",
  "id": "<AD_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#)Nesta Página[Anúncios de clique para o Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#an-ncios-de-clique-para-o-instagram)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#antes-de-come-ar)[Etapa 1: criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-1)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#par-metros)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#atualiza--o)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#leitura)[Etapa 2: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-2)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#par-metros-2)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#atualiza--o-2)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#leitura-2)[Etapa 3: gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-3)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#par-metros-3)[Como preencher a mensagem de boas-vindas da Página](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#como-preencher-a-mensagem-de-boas-vindas-da-p-gina)[Exemplos de como gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#exemplos-de-como-gerar-um-criativo-do-an-ncio)[Como gerar criativos de anúncio usando conteúdo do Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#como-gerar-criativos-de-an-ncio-usando-conte-do-do-instagram)[Como gerar criativos do anúncio usando conteúdo do Facebook](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#como-gerar-criativos-do-an-ncio-usando-conte-do-do-facebook)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#atualiza--o-3)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#leitura-3)[Identificação do objetivo alternativo na geração de um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#identifica--o-do-objetivo-alternativo-na-gera--o-de-um-criativo-do-an-ncio)[Etapa 4: criar um anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-4)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#par-metros-4)[Chamada para ação](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#chamada-para-a--o)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#atualiza--o-4)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#leitura-4)[Etapa 5: publicar o anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-5)[Solicitação](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#solicita--o)[Resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram#resposta) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WtoNR1wOqTZOKcGPrauQrCCn3qxnzWPUIEFk2FJTarPFs4S71O35-G6g3Lw_aem_Tjqq7U981x5A6h3a0lGVpg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6pGB7U_PdrE5Mrynz6O_w3oQGNttz0q2Lso9k8JeDLdK0b4usnSeJ2yhGMYw_aem_QVMsDF7i62qsUfEMars4jg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6FvejkP6f4aSNtZJ4UtarLsuq0ReFAEVG33REGViEzKSX76qygPUm-TZOK0A_aem_6PgnSbvgYC0F2H1cMeJrkQ&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5z6c4IDrfW0X2_eCLsrXPfPbHOp4BKkLYcpKdqfaIKzIAHZ5R1sWH3AQsMog_aem_bUYgS6ANC3xSj-VUR3SJ7w&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5z6c4IDrfW0X2_eCLsrXPfPbHOp4BKkLYcpKdqfaIKzIAHZ5R1sWH3AQsMog_aem_bUYgS6ANC3xSj-VUR3SJ7w&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5zOlhDKwGhuX96kZp5CeM_3PlWZxCeOe0NSqrvUjH8RWBdngiQ6Mit-YUmug_aem_wYWhuMoNDoHd1AoQzw2yUw&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zHVPRMlTD8X30l5p9AxAjnpzoYp9SP7P0KM2puBFVn5x1yqtAVW-NTn-ZZQ_aem_H3BZ-h9FkDO7KOw8-3IpNA&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6pGB7U_PdrE5Mrynz6O_w3oQGNttz0q2Lso9k8JeDLdK0b4usnSeJ2yhGMYw_aem_QVMsDF7i62qsUfEMars4jg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7WFhyroOBYWhPTua14-EzdLa7YjJkLHWJ0OoJzrQU0EkwANhWfV23iR_Y_rQ_aem_dN_1r1SivINKAZ98pl1YQg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BgOyI6Y3ubBSQynL_KnK5I4-s4BGiREKln7GPxkedKzuj-NDOqh5sb7N7Og_aem_XmLBpuQ95n8jOJXd_wgfVg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5zOlhDKwGhuX96kZp5CeM_3PlWZxCeOe0NSqrvUjH8RWBdngiQ6Mit-YUmug_aem_wYWhuMoNDoHd1AoQzw2yUw&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BgOyI6Y3ubBSQynL_KnK5I4-s4BGiREKln7GPxkedKzuj-NDOqh5sb7N7Og_aem_XmLBpuQ95n8jOJXd_wgfVg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4T4ZXAbpqfaoTWiJD8O5Q3JVapgzjcszkXrL3zoy9Cuvyqyrfycp6OH65uAQ_aem_GXFY2OoY5T1dVZRiOW3wUg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GAwfYA66mU3fd0Is-serIgiqH30WcGtJPcI3wzZR6sYRHOd7Ei6H9Kg_Fgw_aem_siJZ-es0NM-2TsZjB7mXig&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5zOlhDKwGhuX96kZp5CeM_3PlWZxCeOe0NSqrvUjH8RWBdngiQ6Mit-YUmug_aem_wYWhuMoNDoHd1AoQzw2yUw&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4T4ZXAbpqfaoTWiJD8O5Q3JVapgzjcszkXrL3zoy9Cuvyqyrfycp6OH65uAQ_aem_GXFY2OoY5T1dVZRiOW3wUg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5z6c4IDrfW0X2_eCLsrXPfPbHOp4BKkLYcpKdqfaIKzIAHZ5R1sWH3AQsMog_aem_bUYgS6ANC3xSj-VUR3SJ7w&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WtoNR1wOqTZOKcGPrauQrCCn3qxnzWPUIEFk2FJTarPFs4S71O35-G6g3Lw_aem_Tjqq7U981x5A6h3a0lGVpg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7WFhyroOBYWhPTua14-EzdLa7YjJkLHWJ0OoJzrQU0EkwANhWfV23iR_Y_rQ_aem_dN_1r1SivINKAZ98pl1YQg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WtoNR1wOqTZOKcGPrauQrCCn3qxnzWPUIEFk2FJTarPFs4S71O35-G6g3Lw_aem_Tjqq7U981x5A6h3a0lGVpg&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7PkRX2xK56afVUG3fG_slT-RRaTi7J95_4hRBTDYBqMqIWS3TlkLrxDUjantQZQSoIMGJXVBbTnHXZ4EwfLawac06VTtiJTSrq0s4Wi5lLUwq43OGF6LPHEq2MXxKz51l1WFDGZBuR__fMbL2iJwjYVBA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão