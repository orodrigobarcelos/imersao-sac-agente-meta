<!-- Fonte: Vários destinos - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de clique com vários destinos


Este guia explica como criar e publicar anúncios de clique com vários destinos usando a API de Marketing.


Os anúncios de clique com vários destinos enviam as pessoas que clicam neles diretamente para conversas com sua empresa no app ou nos apps (Messenger, Instagram ou WhatsApp) que elas preferirem. Esses anúncios podem ser usados para alcançar pessoas em grande escala e fornecer serviço individualizado e com destaque.


Os anúncios com vários destinos podem levar uma pessoa a qualquer combinação destes destinos: bate-papo do Messenger, bate-papo do Instagram e bate-papo do WhatsApp.


Se você quiser criar um anúncio que direcione para um único destino, consulte os artigos a seguir:


- [Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger)
- [Anúncios de clique para o Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram)
- [Anúncios de clique para o WhatsApp](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp)


### Visão geral da criação de anúncio


Este documento descreve as etapas que você precisa seguir ao configurar sua integração de anúncios de clique com vários destinos. Você precisará:


- [Criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-1)
- [Criar um conjunto de anúncios que vincula os anúncios à campanha](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-2)
- [Fornecer um criativo para o tipo de anúncio com vários destinos que será exibido](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-3)
- [Criar um anúncio vinculando o criativo ao conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-4)


## Antes de começar


Este guia considera que você já tem o seguinte:


- [Uma conta de anúncios com a Meta](https://adsmanager.facebook.com/adsmanager/)
- [Ativos carregados nos servidores da Meta (como imagens ou vídeos) para usar nos anúncios](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)

## Etapa 1: criar uma campanha de anúncios


O primeiro passo é criar a campanha de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/campaigns`, em que `<AD_ACCOUNT_ID>` é a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| name string | Obrigatório. Nome da campanha de clique com vários destinos. |
| objective enumeração | Obrigatório. Objetivo da campanha. Objetivos compatíveis: OUTCOME_ENGAGEMENT , OUTCOME_SALES e OUTCOME_TRAFFIC . |
| special_ad_categories lista\<Object\> | Obrigatório. Categorias de anúncios especiais associadas à campanha de clique com vários destinos. No momento, os anúncios de clique com vários destinos não são compatíveis com categorias especiais. Por isso, é necessário definir este campo como NONE ou usar uma matriz vazia. Consulte a referência sobre campanha de anúncios para saber mais. |
| status enumeração | Opcional. Opções válidas: PAUSED e ACTIVE . Se o status for PAUSED , todos os respectivos conjuntos de anúncios e anúncios ativos serão pausados e terão status efetivo de CAMPAIGN_PAUSED . |


#### Solicitação


```
curl -X POST \
  -F 'name=Click to Multi Destination Campaign' \
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


Para verificar se você criou com sucesso uma campanha de clique com vários destinos, faça uma solicitação `GET` para `/<AD_CAMPAIGN_ID>`. Consulte a [referência sobre campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/#Reading) para ver uma lista completa dos parâmetros disponíveis.


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
  "name": "Click to Multi Destination Campaign",
  "status": "ACTIVE",
  "objective": "OUTCOME_ENGAGEMENT",
  "id": "<AD_CAMPAIGN_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)

## Etapa 2: criar um conjunto de anúncios


Quando você já tiver uma campanha, crie um conjunto de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adsets`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| bid_amount unsigned int32 | Obrigatório se bid_strategy for definido como LOWEST_COST_WITH_BID_CAP ou COST_CAP . O valor máximo que você deseja pagar por um resultado com base na sua optimization_goal . |
| bid_strategy enumeração | Opcional. A estratégia de lance da campanha para atender às suas metas de negócios. Consulte a referência sobre campanha de anúncios para saber mais. Valores: LOWEST_COST_WITHOUT_CAP , LOWEST_COST_WITH_BID_CAP , COST_CAP |
| billing_event enumeração | Obrigatório. Precisa ser definido como IMPRESSIONS em anúncios de clique com vários destinos. A Meta cobra quando seu anúncio é exibido para as pessoas. |
| campaign_id string numérica ou número inteiro | Obrigatório. Uma campanha de clique com vários destinos válida à qual você quer adicionar o conjunto de anúncios. |
| daily_budget int64 | Obrigatório se lifetime_budget não for definido. O orçamento diário definido na moeda da sua conta. Permitido apenas em conjuntos de anúncios com duração (diferença entre end_time e start_time ) superior a 24 horas. daily_budget ou lifetime_budget precisa ser maior que 0 . |
| destination_type string | Obrigatório. Defina como MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP se quiser usar os três destinos (Messenger, WhatsApp e Instagram).; Defina como MESSAGING_INSTAGRAM_DIRECT_MESSENGER se quiser usar o Messenger e o Instagram.; Defina como MESSAGING_MESSENGER_WHATSAPP se quiser usar o Messenger e o WhatsApp.; Defina como MESSAGING_INSTAGRAM_DIRECT_WHATSAPP se quiser usar o WhatsApp e o Instagram. Observação : se você incluir o WhatsApp como destino, verifique se há um número de telefone comercial do WhatsApp conectado à sua página. Caso inclua o Instagram como destino, será preciso ter uma conta comercial do Instagram conectada à sua página. |
| end_time datetime | Obrigatório quando lifetime_budget é especificado. Ao criar um conjunto de anúncios com um daily_budget , especifique end_time=0 ou deixe esse campo vazio para definir que o conjunto está em andamento e não tem data de término. Exemplo: 2015-03-12 23:59:59-07:00 ou 2015-03-12 23:59:59 PDT . Registro de data e hora UNIX (UTC). |
| lifetime_budget int64 | Obrigatório se daily_budget não for definido. O orçamento total do conjunto de anúncios definido na moeda da sua conta. Se for especificado, será preciso definir também um end_time . daily_budget ou lifetime_budget precisa ser maior que 0 . |
| name string | Obrigatório. O nome do conjunto de anúncios de clique com vários destinos. |
| optimization_goal enumeração | Obrigatório. A meta para qual o conjunto de anúncios está sendo otimizado. Precisa ser definido como CONVERSATIONS em anúncios de clique com vários destinos. Dependendo do objetivo da campanha, o conjunto de anúncios pode servir a diferentes metas de otimização. |
| promoted_object AdPromotedObject | Obrigatório. O objeto que o conjunto promove em todos os anúncios. Em anúncios de clique com vários destinos, promoted_object inclui as seguintes condições: page_id : Obrigatório. A identificação da Página do Facebook. Consulte Ad Set, Promoted Object para saber mais. |
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
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=<DAILY_BUDGET>' \
  -F 'destination_type=<DESTINATION_TYPE>' \
  -F 'name=<AD_SET_NAME>' \
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
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Resposta


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação do conjunto de anúncios recém-criado.

```
{
  "id": "<AD_SET_ID>"
}
```


### Atualização


É possível atualizar um conjunto de anúncios fazendo uma solicitação `POST` para `/<AD_SET_ID>`.


### Leitura


Para verificar se você criou com sucesso um conjunto de anúncios de clique com vários destinos, faça uma solicitação `GET` para `/<AD_SET_ID>`. Consulte a [referência sobre conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=name,destination_type,optimization_goal,bid_strategy' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_SET_ID>
```


#### Resposta


```
{
  "name": "<AD_SET_NAME>",
  "destination_type": "<DESTINATION_TYPE>",
  "optimization_goal": "CONVERSATIONS",
  "bid_strategy": "LOWEST_COST_WITHOUT_CAP'"
  "id": "<AD_SET_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)

## Etapa 3: gerar um criativo do anúncio


Com o criativo, é possível adicionar ativos aos seus anúncios. Para gerar um criativo do anúncio, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adcreatives`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


### Parâmetros


| Nome | Descrição |
| --- | --- |
| asset_feed_spec | Obrigatório. Especifique os destinos dos anúncios de clique com vários destinos. Obrigatório: optimization_type : precisa ser definido como DOF_MESSAGING_DESTINATION em anúncios de clique com vários destinos.; call_to_actions : matriz dos destinos selecionados em anúncios de clique com vários destinos. Precisa corresponder ao destination_type especificado no conjunto de anúncios. Messenger { "type" : "MESSAGE_PAGE" , "value" : { "app_destination" : "MESSENGER" , "link" : "https://fb.com/messenger_doc/" } } WhatsApp { "type" : "WHATSAPP_MESSAGE" , "value" : { "app_destination" : "WHATSAPP" , "link" : "https://api.whatsapp.com/send" } } Instagram { "type" : "INSTAGRAM_MESSAGE" , "value" : { "app_destination" : "INSTAGRAM_DIRECT" , "link" : "https://www.instagram.com" } } |
| name string | Obrigatório. O nome do criativo do anúncio. |
| object_story_spec AdCreativeObjectStorySpec | Obrigatório. Um objeto que contém informações sobre a mensagem. Consulte Ad Creative Object Story Spec para saber mais. Obrigatório: page_id : a identificação da Página do Facebook.; instagram_user_id : a identificação da conta do Instagram. Há três formas de obter a identificação de uma conta do Instagram : conta do Instagram de propriedade do Gerenciador de Negócios, conta do Instagram conectada à Página e conta do Instagram associada à Página. Opcional: link_data : a especificação para um post da Página com link ou um anúncio em carrossel .; photo_data : a especificação para um post da Página com foto.; text_data : a especificação para um post da Página com texto.; video_data : a especificação para um post da Página com vídeo. |
| degrees_of_freedom_spec | Opcional. Consulte Aprimoramentos padrão no criativo Advantage+ para saber mais. |


Acesse a [referência sobre criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


### Como preencher a mensagem de boas-vindas da Página


A mensagem padrão exibida ao cliente é "Olá! Posso obter mais informações sobre isso?". Você pode criar experiências do usuário mais personalizadas em anúncios de clique com vários destinos ajustando a mensagem de saudação, os quebra-gelos e as mensagens de preenchimento automático dos seus anúncios no campo `page_welcome_message` em `object_story_spec`.


Para mais informações sobre quebra-gelos, veja a [`ice_breakers`referência](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/ice-breakers).


#### Limitações


- Os títulos de quebra-gelos não devem ter mais de 80 caracteres.
- As respostas de quebra-gelos não devem ter mais de 300 caracteres.
- O texto da mensagem não pode ter mais de 300 caracteres.


#### Exemplo


Crie o objeto `page_welcome_message` para adicionar quebra-gelos com uma mensagem de saudação.

```
"page_welcome_message": {
  "type":"VISUAL_EDITOR",
  "version":2,
  "landing_screen_type":"welcome_message",
  "media_type":"text",
  "text_format":{
    "customer_action_type":"ice_breakers",
    "message":{
      "ice_breakers":[
        {"title":"Can I make a purchase?","response":"This is a response 1"},
        {"title":"Can I see a menu?", "response":"This is a response 2"},
        {"title":"Where are you located?", "response":"This is a response 3"}],
      "quick_replies":[],
      "text":"Hi {{user_first_name}}! Please let us know how we can help you."}
  },
  "user_edit":false,
  "surface":"visual_editor_new"
}
```


### Exemplos de como gerar um criativo do anúncio


Adicione o campo `page_welcome_message` ao criativo da seguinte forma.


#### Solicitação


```
curl -X POST \
-F 'name=<CREATIVE_NAME>' \
-F 'object_story_spec={
     "page_id": "438346666550309",
     "link_data": {
       "name": "<AD_HEADLINE>",
       "message": "<AD_PRIMARY_TEXT>",
       "image_hash": "<IMAGE_HASH>"
       "link": "https://fb.com/messenger_doc/",
       "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
       "call_to_action": {
         "type": "MESSAGE_PAGE",
         "value": {
           "app_destination": "MESSENGER"
         }
       }
     }
   }' \
-F 'asset_feed_spec={
     "optimization_type": "DOF_MESSAGING_DESTINATION",
     "call_to_actions": [
       {
         "type": "MESSAGE_PAGE",
         "value": {
           "app_destination": "MESSENGER",
           "link": "https://fb.com/messenger_doc/"
         }
       },
       {
         "type": "WHATSAPP_MESSAGE",
         "value": {
           "app_destination": "WHATSAPP",
           "link": "https://api.whatsapp.com/send"
         }
       },
       {
         "type": "INSTAGRAM_MESSAGE",
         "value": {
           "app_destination": "INSTAGRAM_DIRECT",
           "link": "https://www.instagram.com"
         }
       }
     ]
   }' \
-F 'degrees_of_freedom_spec={
     "creative_features_spec": {
       "standard_enhancements": {
         "enroll_status": "OPT_IN"
       }
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
  -F 'instagram_user_id=<IG_USER_ID>' \
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
       "instagram_user_id": "<IG_USER_ID>",
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


Consulte [Usar posts como anúncios do Instagram: posts do Facebook](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads/#facebook-posts) para saber mais.

```
curl -i -X POST \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives
  ?object_story_id=<postOwnerID_postID>
  &instagram_user_id=<IG_USER_ID>
  &call_to_action="{'type':MESSAGE_PAGE,'value':{'app_destination':'MESSENGER'}}"
  &access_token=<ACCESS_TOKEN>"
```


`object_story_id` é a identificação do post no formato `postOwnerID_postID`, e `instagram_user_id` é uma identificação da conta do Instagram conectada à Página ou a identificação da conta do Instagram associada à Página. Veja mais detalhes em [Set Up Instagram Accounts With Pages](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account).


### Atualização


É possível atualizar um [criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) fazendo uma solicitação `POST` para `/<AD_CREATIVE_ID>`.


### Leitura


Para verificar se você criou com sucesso um criativo do anúncio de clique com vários destinos, faça uma solicitação `GET` para `/<AD_CREATIVE_ID>`. Consulte [Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=name,object_story_spec{page_welcome_message},asset_feed_spec' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>
```


#### Resposta


```
{
  "name": "<CREATIVE_NAME>",
  "object_story_spec": {
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
              "title": "Sample icebreaker"
            },
            {
              "title": "Sample icebreaker"
            },
            {
              "title": "Sample icebreaker"
            }
          ]
        }
      }
    }
  },
  "asset_feed_spec": {
    "optimization_type": "DOF_MESSAGING_DESTINATION",
    "call_to_actions": [
      {
        "type": "MESSAGE_PAGE",
        "value": {
          "app_destination": "MESSENGER",
          "link": "https://fb.com/messenger_doc/"
        }
      },
      {
        "type": "WHATSAPP_MESSAGE",
        "value": {
          "app_destination": "WHATSAPP",
          "link": "https://api.whatsapp.com/send"
        }
      },
      {
        "type": "INSTAGRAM_MESSAGE",
        "value": {
          "app_destination": "INSTAGRAM_DIRECT",
          "link": "https://www.instagram.com"
        }
      }
    ]
  },
  "id": "<AD_CREATIVE_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)

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
  -F 'name=<AD_NAME>' \
  -F 'adset_id=<AD_SET_ID> \
  -F 'creative={
       "creative_id": "<AD_CREATIVE_ID>"
     }' \
  -F 'status=ACTIVE \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### Resposta


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação do anúncio recém-criado.

```
{
  "id": "<AD_ID>"
}
```


### Chamada para ação


Também é possível definir uma chamada para ação ao criar um anúncio.

```
"asset_feed_spec": {
  "optimization_type": "DOF_MESSAGING_DESTINATION",
  "call_to_actions": [
    {
      "type": "MESSAGE_PAGE",
      "value": {
        "app_destination": "MESSENGER",
        "link": "https://fb.com/messenger_doc/"
      }
    },
    {
      "type": "INSTAGRAM_MESSAGE",
      "value": {
        "app_destination": "INSTAGRAM_DIRECT",
        "link": "https://www.instagram.com"
      }
    }
  ]
}
```


Consulte [Especificação do feed de ativos](https://developers.facebook.com/docs/marketing-api/ad-creative/asset-feed-spec) para ver mais informações.


### Atualização


É possível atualizar um [anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) fazendo uma solicitação `POST` para `/<AD_ID>`.


### Leitura


Para verificar se você criou com sucesso um anúncio de clique com vários destinos, faça uma solicitação `GET` para `/<AD_ID>`. Consulte a [referência sobre anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) para ver uma lista completa dos parâmetros disponíveis.


#### Solicitação


```
curl -X GET -G \
  -d 'fields=status,adset_id \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


#### Resposta


```
{
  "status": "ACTIVE",
  "adset_id": "<AD_SET_ID>",
  "id": "<AD_ID>"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#)Nesta Página[Anúncios de clique com vários destinos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#an-ncios-de-clique-com-v-rios-destinos)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#antes-de-come-ar)[Etapa 1: criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-1)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#par-metros)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#atualiza--o)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#leitura)[Etapa 2: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-2)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#par-metros-2)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#atualiza--o-2)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#leitura-2)[Etapa 3: gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-3)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#par-metros-3)[Como preencher a mensagem de boas-vindas da Página](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#como-preencher-a-mensagem-de-boas-vindas-da-p-gina)[Exemplos de como gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#exemplos-de-como-gerar-um-criativo-do-an-ncio)[Como gerar criativos de anúncio usando conteúdo do Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#como-gerar-criativos-de-an-ncio-usando-conte-do-do-instagram)[Como gerar criativos do anúncio usando conteúdo do Facebook](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#como-gerar-criativos-do-an-ncio-usando-conte-do-do-facebook)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#atualiza--o-3)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#leitura-3)[Etapa 4: criar um anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-4)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#par-metros-4)[Chamada para ação](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#chamada-para-a--o)[Atualização](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#atualiza--o-4)[Leitura](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination#leitura-4) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7L6Y0N8vEiJKQYCmTHrxE_GOj0sVxAi-5_632zU-QvdmxynQ2cAboUuQItBA_aem_K09N6QmyUKp4EAFn_A9CFA&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7f35P2-DVftAM4Dws_xAgqr5m94a204kHGXueaA1pANIUGaX5FycfBvrInvw_aem_-zCDQ_Dp47ePdalRRFlZ1Q&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5J7Wx_L7zxzmRKIfa8J4BUbA-HCvgR9olMB08g5hQa9ugIzERUig__SVABsQ_aem_8Le3wQQUUvdH7iXGcmRABQ&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7tAMpWsuqBOVL6k7S9H9OGP3jRpPdafcI6lcH-6rRcCgeOQU7PbkJ0tgg6Ng_aem_72J_JwSiqAknokPDimwWYg&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wdbfEjp-1RkOlT4dA12GNeP5UTtXINjHWuirm6oc3buHruDq-JdXvW7-4YQ_aem_isshsAUy72vo404AcHa2Nw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7f35P2-DVftAM4Dws_xAgqr5m94a204kHGXueaA1pANIUGaX5FycfBvrInvw_aem_-zCDQ_Dp47ePdalRRFlZ1Q&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6qrIJfebu1JatmLOIKIIpc2IOAmBzBkDv2XGyoj-JkFCeCANCmNvB2H_hDSA_aem_xyMYgBf9ClVl53JyROb-sQ&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5J7Wx_L7zxzmRKIfa8J4BUbA-HCvgR9olMB08g5hQa9ugIzERUig__SVABsQ_aem_8Le3wQQUUvdH7iXGcmRABQ&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wdbfEjp-1RkOlT4dA12GNeP5UTtXINjHWuirm6oc3buHruDq-JdXvW7-4YQ_aem_isshsAUy72vo404AcHa2Nw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Wt3DOwVDRceYGMes10-jEErOA67qcS-LDwRHTNDDYCohguplt0e4hPC_2tw_aem_iQBBpesYMUBU3U-PpWwzfw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7tAMpWsuqBOVL6k7S9H9OGP3jRpPdafcI6lcH-6rRcCgeOQU7PbkJ0tgg6Ng_aem_72J_JwSiqAknokPDimwWYg&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5w_WmHxBg8iy7CyTvMqa_ubfVU7CTo50i8IjV14YkLpoCbwnR7i-UsMZtz7A_aem_YUrnqVWzrBps4a2TEW3l6g&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5w_WmHxBg8iy7CyTvMqa_ubfVU7CTo50i8IjV14YkLpoCbwnR7i-UsMZtz7A_aem_YUrnqVWzrBps4a2TEW3l6g&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Wt3DOwVDRceYGMes10-jEErOA67qcS-LDwRHTNDDYCohguplt0e4hPC_2tw_aem_iQBBpesYMUBU3U-PpWwzfw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wdbfEjp-1RkOlT4dA12GNeP5UTtXINjHWuirm6oc3buHruDq-JdXvW7-4YQ_aem_isshsAUy72vo404AcHa2Nw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wdbfEjp-1RkOlT4dA12GNeP5UTtXINjHWuirm6oc3buHruDq-JdXvW7-4YQ_aem_isshsAUy72vo404AcHa2Nw&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5J7Wx_L7zxzmRKIfa8J4BUbA-HCvgR9olMB08g5hQa9ugIzERUig__SVABsQ_aem_8Le3wQQUUvdH7iXGcmRABQ&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6wzcXq2ze6cyE8fy4HyP6CFsI2ERnBAw6wp2Xc9PFDPmdaM84yzGA-SmwI0g_aem_ybVazwfmsInJSn-enY-MWQ&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5h_FXQ9DFCnJbBpMi4niHgOotFj7oz29g4bqiilYN1jVePDdew4X8Chpjs3g_aem_AJ1ig_aUq9k4n3SRNrDFfA&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5h_FXQ9DFCnJbBpMi4niHgOotFj7oz29g4bqiilYN1jVePDdew4X8Chpjs3g_aem_AJ1ig_aUq9k4n3SRNrDFfA&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4eugwQPCnwlFbrpA935qpf8-O3EFEKCQU7JX3cmQvPhCJ4Bp-jEKrAhz5_dy5XqD5a41q5yyJx-JqTZRzF4OHCAHLh2lo6GaqECGQaP_MU23fLUCI5SOsJiGo7S5FSG3xvfBpbpS-gDWuw11lO_hxc2ps)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão