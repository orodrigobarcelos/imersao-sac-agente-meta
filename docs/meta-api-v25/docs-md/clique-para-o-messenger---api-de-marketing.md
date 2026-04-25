<!-- Fonte: Clique para o Messenger - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de clique para o Messenger


Este guia explica como criar e publicar anúncios de clique para o Messenger usando a API de Marketing.


Se você tem interesse em usar o Gerenciador de Anúncios para criar uma campanha de anúncios de lead, acesse a [Central de Ajuda da Meta para Empresas](https://www.facebook.com/business/help/2398917563501477).


Os anúncios de clique para o Messenger direcionam as pessoas que clicam neles diretamente para conversas com sua empresa no Messenger. Esses anúncios podem ser usados para alcançar pessoas em grande escala, bem como fornecer serviço individualizado e com destaque.


Os anúncios de clique para o Messenger são compatíveis com anúncios de imagem, vídeo, carrossel ou apresentação multimídia. Também é possível incluir um comando para ligação telefônica nesses anúncios.


Se tiver interesse em criar anúncios que direcionem as pessoas para conversas no Instagram ou WhatsApp, consulte [Anúncios de clique para o Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-instagram) e [Anúncios de clique para o WhatsApp](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp). Também é possível criar anúncios para o destino no qual o usuário tem mais probabilidade de responder. Para mais informações, acesse [Anúncios de clique com vários destinos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-multidestination).


### Visão geral da criação de anúncio


Para criar e publicar um anúncio:


- [Crie uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#campaign).
- [Crie um conjunto de anúncios vinculando os anúncios à campanha](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adset)
- [Forneça um criativo para o tipo de anúncio do Messenger a ser exibido](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad-creative)
- [Crie um anúncio vinculando o criativo ao conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad)
- [Publique o anúncio no Facebook, Instagram e Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#publish-ad)


## Antes de começar


Este guia considera que você já tem o seguinte:


- [Uma conta de anúncios da Meta](https://adsmanager.facebook.com/adsmanager/)
- [A plataforma do Messenger integrada ao seu app ou site](https://developers.facebook.com/docs/messenger-platform)
- [Ativos carregados (como imagens ou vídeos) nos servidores da Meta para usar nos anúncios](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)


Para fazer chamadas aos pontos de extremidade deste guia, você precisará do seguinte:


- Um token de acesso à Página solicitado por uma pessoa que pode executar a tarefa `ADVERTIZE` na Página.
- Estas permissões devem ser concedidas pelo usuário do seu app: - `ads_management` - `pages_manage_ads` - `pages_read_engagement` - `pages_show_list`
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Etapa 1. criar uma campanha


Para criar uma campanha de anúncios, envie uma solicitação `POST` ao ponto de extremidade `act_ad_account_id/campaigns`, sendo ***ad_account_id*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


| access_token; buying_type; name | objective definido como OUTCOME_TRAFFIC ou OUTCOME_LEADS para anúncios de lead; special_ad_categories; status |
| --- | --- |


#### Referência rápida sobre campanha de anúncios


| Parâmetro | Valor |
| --- | --- |
| access_token | O token de acesso à Página. |
| buying_type | Definido como AUCTION (padrão) em anúncios do Messenger para leads |
| name string | O nome da campanha de anúncios. |
| objective enumeração | Objetivos da campanha. OUTCOME_TRAFFIC para CTS. OUTCOME_LEADS para anúncios do Messenger para leads. OUTCOME_ENGAGEMENT , OUTCOME_SALES e OUTCOME_TRAFFIC para anúncios gerais de CTM. |
| special_ad_categories matriz[enumeração] | NONE ou uma lista separada por vírgula de categorias de anúncios da Meta |
| status matriz[enumeração] | PAUSED : a campanha ainda não está pronta |


- Consulte a [referência sobre o ponto de extremidade da campanha da conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-account/campaigns/#Creating) para ver a lista de parâmetros disponíveis.


#### Exemplo de solicitação

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/campaigns" \
     -H "Content-Type: application/json" \
     -d '{
           "access_token":"Your_page_access_token",
           "buying_type":"AUCTION",
           "name":"Messenger_ad_campaign_name",
           "objective":"OUTCOME_TRAFFIC",
           "status":"PAUSED",
           "special_ad_categories":["NONE"],
         }'
```


Caso ela seja bem-sucedida, o app receberá uma resposta JSON com a identificação da campanha.

```
{
  "id": "campaign_id"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Etapa 2. criar um conjunto de anúncios


Para criar um conjunto de anúncios, envie uma solicitação `POST` ao ponto de extremidade `act_ad_account_id/adsets`, sendo ***ad_account_id*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `access_token`
- `bid_amount`
- `billing_event` definido como `IMPRESSIONS`
- `campaign_id`
- `daily_budget`
- `destination_type` definido como `MESSENGER`
- `name`
- `optimization_goal` definida como `CONVERSATIONS`, `IMPRESSIONS`, `LEAD_GENERATION` ou `QUALITY_LEAD` para anúncios de lead
- `promoted_object` definido como a identificação da Página do Facebook da sua empresa.
- `status` definido como `PAUSED`
- `targeting`


#### Referência rápida sobre conjunto de anúncios


| Parâmetro | Valor |
| --- | --- |
| access_token | O token de acesso à Página. |
| bid_amount número inteiro | O valor máximo que você quer pagar por um resultado com base na optimization_goal. |
| billing_event enumeração | Definido como IMPRESSIONS . A Meta cobra quando seu anúncio é mostrado para as pessoas. |
| campaign_id número inteiro | A identificação da campanha conforme a Etapa 1 . |
| daily_budget número inteiro | O valor que você quer gastar por dia. |
| destination_type string | Deve ser MESSENGER em anúncios do Messenger para leads Obrigatório em anúncios do Messenger para leads |
| name string | O nome do conjunto de anúncios. |
| optimization_goal enumeração | Pode ser CONVERSATIONS ou CONVERSIONS para CTM ou CTS. Pode ser LEAD_GENERATION ou QUALITY_LEAD em anúncios do Messenger para leads. |
| promoted_object enumeração | Definido como a identificação da Página do Facebook da sua empresa. Obrigatório em anúncios de lead para o Messenger Se você configurar uma fonte de dados CRM e escolher QUALITY_LEAD como uma meta de otimização, será possível adicionar a pixel_id ao promoted_object para aprimorar a otimização de qualidade. Não é necessário fornecer uma pixel_rule com o pixel_id . |
| status enumeração | PAUSED |
| targeting objeto | Um objeto que define o público a quem você quer mostrar os anúncios. |


Consulte a [referência sobre o ponto de extremidade do conjunto de anúncios da conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adsets/#Creating) para ver a lista de parâmetros disponíveis.


#### Exemplo de solicitação

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/adsets"
     -H "Content-Type: application/json"
     -d '{
           "access_token":"Your_page_access_token",
           "bid_amount":"Your_bid_amount",
           "billing_event":"IMPRESSIONS",
           "campaign_id":"Your_campaign_id",
           "daily_budget":"Your_daily_budget",
           "destination_type":"MESSENGER",
           "name:"Your_messenger_adset_name",
           "optimization_goal:IMPRESSIONS",
           "status:PAUSED",
           "targeting":{
             "geo_locations": { "countries":["US","CA"] },
             "device_platforms": ["mobile", "desktop"],
             "publisher_platforms": ["messenger"]
           }
         }'
```


Caso ela seja bem-sucedida, o app receberá a resposta JSON a seguir com a identificação do conjunto de anúncios.

```
{
  "id": "adset_id"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Etapa 3. fornecer um criativo do anúncio


Com o criativo, é possível adicionar ativos aos seus anúncios.


| Limitações Anúncios criados com object_story_id não são compatíveis.; A pessoa precisa ter o Messenger instalado no dispositivo para ver seu anúncio.; Não há compatibilidade com o posicionamento no lado direito. |  |
| --- | --- |


Para fornecer um criativo de anúncio, envie uma solicitação `POST` ao ponto de extremidade `/act_ad_account_id/adcreatives`, sendo ***ad_account_id*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `access_token`
- `name`
- `object_story_spec` (obrigatório)
- `privacy_url` (obrigatório para anúncios de lead)
- `standard_enhancements.enroll_status` (obrigatório para criativos do anúncio qualificados para [aprimoramentos padrão](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#api-support))


#### Referência rápida sobre criativo do anúncio


| Parâmetro | Valor |
| --- | --- |
| access_token | O token de acesso à Página. Obrigatório |
| name | O nome do criativo do anúncio. Por exemplo, "Clique para o Messenger de setembro", entre outros. Obrigatório |
| [object_story_spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/) | Um objeto com informações sobre a mensagem. Obrigatório para anúncios de clique para o Messenger ou de clique para assinar link_data : um objeto que define a mensagem com um modelo ou carrossel; page_id : obrigatório. A identificação da Página do Facebook enviando a mensagem; photo_data : um objeto que define a mensagem com uma imagem; text_data : um objeto que define a mensagem somente com texto; video_data : um objeto que define a mensagem com um vídeo |
| privacy_url | Definido como o URL da sua Política de Privacidade. Obrigatório em anúncios do Messenger para leads |


### Anúncios de clique para o Messenger


Para fornecer o criativo do anúncio de clique para o Messenger, envie uma solicitação `POST` ao ponto de extremidade `/act_ad_account_id/adcreatives`, sendo ***ad_account_id*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `access_token`
- `name`
- `object_story_spec` com um objeto `*_data` que define o tipo de mídia


#### Referência rápida sobre anúncio com imagem


| Parâmetros de `link_data` | Valores |
| --- | --- |
| call_to_action | Objeto que define o botão de chamada para ação no anúncio. type : o texto do botão (por exemplo, LEARN_MORE ) value : o destino do clique no botão {app_destination : MESSENGER} ( obrigatório ) |
| image_hash | O hash da imagem. |
| link | O URL da imagem. |
| message | O texto de boas-vindas a ser enviado depois de a pessoa clicar no botão de chamada para ação. Também é possível enviar um modelo padrão ou até 5 modelos de mensagem. Saiba mais. |


#### Exemplo de solicitação de anúncio com imagem

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/adcreatives"
     -H "Content-Type: application/json"
     -d '{
           "access_token":"page_access_token",
           "name":"Your_CTM_image_ad_name",
           "object_story_spec":{
             "page_id": "your_page_id",
             "link_data": {
               "page_welcome_message": "Your_welcome_message",
               "image_hash": "Your_image_hash",
               "link": "Your_image_URL",
               "call_to_action": {
                 "type":"LEARN_MORE",
                 "value":{ "app_destination":"MESSENGER" }
               }
             }
           }
         }'
```


#### Referência rápida sobre anúncio em vídeo de clique para o Messenger


| Parâmetros de `video_data` | Valores |
| --- | --- |
| call_to_action | Objeto que define o botão de chamada para ação no anúncio. type : o texto do botão (por exemplo, LEARN_MORE ) value : o destino do clique no botão {app_destination : MESSENGER} ( obrigatório ) |
| link_description | O texto do vídeo. |
| image_url | O URL da miniatura do vídeo. |
| `page_welcome_message` | O texto de boas-vindas a ser enviado depois de a pessoa clicar no botão de chamada para ação. Também é possível enviar um modelo padrão ou até 5 modelos de mensagem. Saiba mais. |
| `video_id` | O ID da Meta do vídeo. Saiba como carregar ativos nos servidores da Meta. |


#### Exemplo de solicitação de anúncio em vídeo

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/adcreatives"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "page_access_token",
           "name": "Your_CTM_image_ad_name",
           "object_story_spec": {
             "page_id": "your_page_id",
             "video_data": {
               "call_to_action": {
                 "type": "LEARN_MORE",
                 "value": { "app_destination": "MESSENGER" }
               },
               "link_description": "Your_link_description",
               "image_url": "Your_thumbnail_URL",
               "page_welcome_message": "Your_welcome_text",
               "video_id": "video_id"
             }
           }
         }'
```


#### Anúncio que usa um fluxo de mensagens configurado em um app parceiro.

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/adcreatives"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "page_access_token",
           "name": "Your_CTM_image_ad_name",
           "object_story_spec": {
             "page_id": "your_page_id",
             "link_data": {
               "image_hash": "your_image_hash",
               "link": "your_image_URL",
               "call_to_action": {
                 "type": "MESSAGE_PAGE",
                 "value": { "app_destination":"MESSENGER" }
               }
             }
           },
           "asset_feed_spec": {
             "additional_data": {
               "partner_app_welcome_message_flow_id": "FLOW-ID"
             }
           }
         }'
```


Para saber mais sobre fluxos de mensagens em apps, consulte [Welcome message flows](https://developers.facebook.com/docs/messenger-platform/ads/ads-welcome-message-flows) na documentação da plataforma do Messenger.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

### Como preencher a mensagem de boas-vindas da Página


A mensagem padrão exibida ao cliente é "Olá! Posso acessar mais informações sobre isso?". Você pode criar experiências do usuário mais personalizadas em anúncios de clique no Messenger ajustando a mensagem de saudação, os quebra-gelos e as mensagens de preenchimento automático dos seus anúncios no campo `page_welcome_message` em `object_story_spec`.


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


### Clique para assinar


Os anúncios de clique para assinar (CTS, pelas iniciais em inglês) são anúncio de clique para o Messenger que incluem uma matriz de objetos `object_story_spec.page_welcome_message` com um modelo de mensagem de notificação. Ao clicar no botão **Receber mensagens** no anúncio, a pessoa concorda em receber mensagens de marketing da sua empresa.


Para fornecer um criativo do anúncio com clique para assinar, envie uma solicitação `POST` ao ponto de extremidade `/act_ad_account_id/adcreatives`, sendo ***ad_account_id*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `access_token`
- `name`
- `object_story_spec` com - um objeto `*_data` que define o tipo de mídia - a matriz `page_welcome_message` que define a solicitação de aceitação de mensagens de marketing. Precisa incluir `landing_screen_type` definido como `marketing_messages` e o anexo da mensagem `payload.template_type` definido como `nofitication_messages`


#### Exemplo de solicitação de anúncio com imagem

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/adcreatives"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "page_access_token",
           "name": "Your_CTS_image_ad_name",
           "object_story_spec": {
             "page_id": "your_page_id",
             "link_data": {
               "image_hash": "Your_image_hash",
               "link": "Your_image_URL",
               "call_to_action": {
                 "type": "LEARN_MORE",
                 "value":{ "app_destination": "MESSENGER" }
               }
               "page_welcome_message": "{
                 "landing_screen_type": "marketing_messages",
                 "media_type": "image",
                 "image_format": {
                   "customer_action_type": "buttons",
                   "message": {
                     "text": "Your_welcome_message",
                     "attachment": {
                       "type": "template",
                       "payload":{
                         "template_type":"notification_messages",
                         "elements": [{
                             "title": "Your_CTS_title",
                             "subtitle": "Your_CTS_subtitle",
                             "image_url": "Your_image_URL",
                             "app_id": "Your_Meta_app_ID",
                             "buttons": [{
                               "type": "postback",
                               "payload": "Data_to_include_in_webhook_notification",
                               "title": "Get messages"
                             }]
                         }]
                       }
                     }
                   }
                 }
               }"
             }
           }
         }'
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

### Anúncios de lead em conversas


A partir da versão 24.0, a capacidade de criar anúncios de lead que geram leads no Messenger com a API está sendo descontinuada. Ainda será possível criar anúncios do Messenger para leads usando o Gerenciador de Anúncios. Para saber mais, veja [Como criar anúncios de lead com clique para o Messenger e o Instagram Direct no Gerenciador de Anúncios da Meta](https://www.facebook.com/business/help/2398917563501477).


Com os anúncios do Messenger para leads, você pode gerar leads no Messenger usando um modelo de conversa automatizada. É possível fazer perguntas específicas às pessoas que estão interessadas na sua empresa diretamente da sua plataforma de mensagens favorita, além de coletar as preferências dos clientes e fazer perguntas personalizadas para priorizar os leads mais qualificados.


Antes de fornecer criativos do anúncio, você precisa aceitar [os termos e condições dos anúncios do Messenger para leads.](https://www.facebook.com/ads/leadgen/tos)


#### Requisitos do modelo de mensagem


- Uma **mensagem de boas-vindas** que exibe uma saudação às pessoas após elas tocarem no seu anúncio e informa o que sua empresa tem a oferecer.
- **Perguntas** que coletam as informações necessárias para saber se a pessoa pode ser convertida em um lead. Podem ser perguntas sobre interesses, localização e informações de contato, como email e número de telefone.
- Uma **mensagem de confirmação** em que você agradece às pessoas pelas respostas e informa quais são os próximos passos. Você encontrará os novos leads no seu Gerenciador de Anúncios, na ferramenta de publicação da sua Página ou no CRM.
- Uma **Política de Privacidade**, já que você coletará informações dos clientes.


#### Limitações


- Os modelos de mensagem não podem ser editados nem excluídos depois de criados.


#### Criar um modelo de mensagem


Para criar um modelo de mensagem, envie uma solicitação `POST` ao ponto de extremidade `/page_id/messenger_lead_forms`, sendo ***page_id*** a identificação da Página do Facebook da sua empresa. A solicitação precisa incluir:


- `access_token`
- `privacy_url`
- A matriz `step_list` com `message`, `reply_type`, `step_id` e `step_type`
- `template_name`
- `reminder_text`


O modelo de mensagem a seguir inclui o `template_name`, o `privacy_url`, a `step_list` com uma mensagem de boas-vindas em `step_id: 0`, perguntas em `step_id: 1` a `4`, uma mensagem de confirmação em `step_id: 5` e uma mensagem de desqualificação em `step_id: 6`.


#### Referência rápida para modelos de mensagem


| Parâmetros `step_list` | Descrição |
| --- | --- |
| allow_to_skip booliano | Definido como true ou false . Definido como false quando a pessoa precisa fornecer uma resposta ou true se isso não for necessário. |
| answer_validation_enabled booliano | Definido como true ou false . Definido como true quando a resposta precisa ser validada. Compatível somente com validação de cidade, país, email, identificação nacional, número de telefone e código postal. |
| answers matriz de strings | Uma lista de respostas para uma pergunta. Obrigatório para reply_type: QUICK_REPLIES . |
| message string | O texto para uma etapa específica. Por exemplo, uma mensagem de boas-vindas, pergunta, orientação, confirmação ou uma mensagem de desqualificação. Obrigatório |
| next_step_ids matriz de step_id s | A próxima etapa, ou etapas possíveis, na lista de perguntas. Não pode referenciar uma pergunta anterior na lista. Pode depender da resposta fornecida. Por exemplo: se uma pessoa responder a uma pergunta com um desqualificador, a próxima etapa será a etapa desqualificadora. Porém, se a resposta for qualificadora, a etapa seguinte será a próxima pergunta da lista. |
| prefill_type enumeração{ CITY , EMAIL , PHONE } | Se uma resposta for preenchida automaticamente com as informações da pessoa. Isso ocorrerá caso ela já tenha compartilhado o email e o número de telefone com sua empresa. |
| reminder_text string | Texto para a pessoa que responde às perguntas, com um lembrete para preencher o formulário. |
| reply_type enumeração{ NONE , PREFILL , QUICK_REPLIES } | Se reply_type estiver definido como "PREFILL", os tamanhos de step_list[x].next_step_ids e step_list[x].answers devem corresponder |
| step_id string | A identificação da etapa que permite que você ordene as perguntas e mensagens. Por exemplo, se você tiver uma lista de 6 etapas, 0 é a mensagem de boas-vindas, 1 a 3 são as perguntas, 4 é a confirmação e 5 é a mensagem de desqualificação. |
| step_type enumeração{ CONFIRMATION , DISQUALIFY , INTRO , QUESTION } | O tipo da etapa, como pergunta ou mensagem introdutória. As etapas de INTRO e CONFIRMATION são obrigatórias |


#### Exemplo de modelo de mensagem para leads

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/your_page_ID/messenger_lead_forms"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "privacy_url": "Your_privacy_policy_URL",
           "reminder_text": "Your_reminder_text",
           "template_name": "Your_template_name",
           "step_list": [
             {
               "step_id": "0",
               "message": "Your_welcome_message",
               "step_type": "INTRO",
               "reply_type": "NONE",
               "next_step_ids": "1"
             },
             {
               "step_id": "1"
               "message": "Are_you_interested_in_our_products_or_services?",
               "step_type": "QUESTION",
               "reply_type": "QUICK_REPLIES",
               "answers": ["Yes", "Not now", "Maybe"],
               "next_step_ids": [2,6,2],
               "allow_to_skip": false,
               "answer_validation_enabled": true
             },
             {
               "step_id": "2",
               "message": "What city do you live in?",
               "step_type": "QUESTION",
               "reply_type": "PREFILL",
               "prefill_type": "CITY",
               "next_step_ids": "3",
               "allow_to_skip": true
             },
             {
               "step_id": "3",
               "message": "What is your phone number?",
               "step_type": "QUESTION",
               "reply_type": "PREFILL",
               "prefill_type": "PHONE",
               "next_step_ids": "4",
               "allow_to_skip": false,
               "answer_validation_enabled": true
             },
             {
               "step_id": "4",
               "message": "What is your email address?",
               "step_type": "QUESTION",
               "reply_type": "PREFILL",
               "prefill_type": "EMAIL",
               "next_step_ids": "5",
               "allow_to_skip": false,
               "answer_validation_enabled": true
             },
             {
               "step_id": "5",
               "message": "Your_confirmation_message",
               "step_type": "CONFIRMATION",
               "reply_type": "NONE"
             },
             {
               "step_id": "6",
               "message": "Your_disqualification_message",
               "step_type": "DISQUALIFY",
               "reply_type": "NONE"
             }
           ]
        }'
```


Caso ela seja bem-sucedida, o app receberá um objeto JSON com a identificação do modelo.

```
{
  "id": "your_messenger_lead_gen_template_id"
}
```


Um `fblead_form` também é criado e associado ao modelo de mensagem como parte deste processo.


#### Consultar lista de formulários


Para consultar a lista dos modelos de formulários para geração de leads do Messenger, envie uma solicitação `GET` ao ponto de extremidade `/page_id/messenger_lead_forms`. Também é possível consultar informações sobre um modelo específico enviando uma solicitação `GET` ao ponto de extremidade `/`***`Your_messenger_lead_gen_template_id`***.


#### Exemplos de criativo do anúncio


Para fornecer o criativo do anúncio de clique para o Messenger, envie uma solicitação `POST` ao ponto de extremidade `/act_`***`ad_account_id`***`/adcreatives`, sendo ***`ad_account_id`*** a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `access_token`
- `name`
- `object_story_spec` com um objeto `*_data` que define o tipo de mídia (imagem ou vídeo) e inclui: - o parâmetro `*_data.page_welcome_message` definido como o par chave-valor - `ctm_lead_gen_template_id:`***`Your_messenger_lead_gen_template_id`***


#### Exemplo de criativo com imagem em anúncios do Messenger para leads

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/adcreatives"
    -H "Content-Type: application/json"
    -d '{
          "access_token": "Your_page_access_token",
          "degrees_of_freedom_spec": {
            "creative_features_spec": {
              "standard_enhancements": { "enroll_status": "OPT_IN" }
            }
          },
          "name": "Your_lead_ad_image_ad_name",
          "object_story_spec": {
            "page_id": "Your_page_id",
            "link_data": {
              "call_to_action": {
                "type": "MESSAGE_PAGE",
                "value": { "app_destination": "MESSENGER" }
              },
              "description": "Sample_description",
              "image_hash": "Your_image_hash",
              "message": "Sample_message_for_Creative",
              "page_welcome_message": "{ "ctm_lead_gen_template_id": "Your_messenger_lead_gen_template_id" }"
            }
          }
       }'
```


#### Exemplo de criativo com vídeo em anúncios do Messenger para leads

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_AD_ACCOUNT_ID/adcreatives"
    -H "Content-Type: application/json"
    -d '{
          "access_token": "Your_page_access_token",
          "degrees_of_freedom_spec": {
            "creative_features_spec": {
              "standard_enhancements": { "enroll_status": "OPT_IN" }
            }
          },
          "name": "Your_lead_ad_video_ad_name",
          "object_story_spec": {
            "page_id": "your_page_id",
            "video_data": {
              "call_to_action": {
                "type": "MESSAGE_PAGE",
                "value":{ "app_destination": "MESSENGER" }
              },
              "image_url": "Your_thumbnail_url",
              "link_description": "Your_link_description ",
              "message": "Sample message for Creative ",
              "page_welcome_message": "{ "ctm_lead_gen_template_id": "Your_messenger_lead_gen_template_id" }",
              "video_id": "Your_video_id"
            }
          }
       }'
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

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


`object_story_id` é a identificação do post no formato `postOwnerID_postID`, e `instagram_user_id` é uma identificação da conta do Instagram conectada à Página ou a identificação da conta do Instagram associada à Página. Veja mais detalhes em [Configurar contas do Instagram com Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account).


### Adicionar extensões de produto ao clique para o Messenger


#### O que é o clique para o Messenger com extensões de produto?


As extensões de produto (recurso "Mostrar produto" no Gerenciador de Anúncios da Meta) é uma otimização do criativo Advantage+ que exibe produtos do seu catálogo abaixo de uma mídia única estática quando há probabilidade de melhorar o desempenho. Este documento mostra como usar os recursos de extensões de produto em anúncios de clique para o Messenger. Para saber como adicionar extensões de produto a anúncios que não sejam do tipo clique para o Messenger, consulte esta página.


#### Referência

[Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger)
[Extensões de produto para criativo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions)

#### Critérios de qualificação


- Ter um catálogo conectado a uma loja no Facebook
- Ter um catálogo com pelo menos um item de produto
- Criar uma campanha com o objetivo `OUTCOME_ENGAGMENET, OUTCOME_LEAD,OUTCOME_SALES` ou `LINK_CLICK`
- Usar o formato do anúncio com uma opção única de imagem ou vídeo ou o conteúdo de um post existente no Facebook


#### Criar usando uma imagem única

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/ads"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "creative_sourcing_spec": {
              "associated_product_set_id": "Your_associated_product_set_id"
            },
            "degrees_of_freedom_spec": {
              "creative_features_spec": {
                "product_extensions": {
                   "enroll_status": "OPT_IN"
                }
              }
            },
            "object_story_spec": {
              "page_id": Your_facebook_page_id",
              "link_data": {
                "call_to_action": {
                  "type": "MESSAGE_PAGE",
                  "value": {
                    "app_destination": "MESSENGER"
                  }
                },
                "image_hash":"Your_image_hash", (or “picture”: "Your_picture_url")"
                "link": "https://fb.com/messenger_doc/",
                "name": "Chat in Messenger"
              },
              "product_data": [
                {
                  "product_id": Your_product_id_1",
                  "product_source": "MANUAL",
		"product_decision": "ACCEPT"
                },
                {
                  "product_id":Your_product_id_2",
                  "product_source": "MANUAL",
		"product_decision": "ACCEPT"
                }
              ]
            }
```


#### Criar usando um vídeo único

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/ads"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "creative_sourcing_spec": {
              "associated_product_set_id": "Your_associated_product_set_id"
            },
            "degrees_of_freedom_spec": {
              "creative_features_spec": {
                "product_extensions": {
                   "enroll_status": "OPT_IN"
                }
              }
            },
            "object_story_spec": {
              "page_id": "Your_facebook_page_id",
              "video_data": {
                "video_id":"Your_video_id"",
                "video_thumbnail_id": "0",
                "call_to_action": {
                  "type": "MESSAGE_PAGE",
                  "value": {
                    "app_destination": "MESSENGER",
                    "link": "https://fb.com/messenger_doc/"
                  }
                },
                "image_url": "Your_image_url",
                "title": "Chat in Messenger",
                "video_thumbnail_source": "generated_default"
              },

              "product_data": [
                {
                  "product_id": Your_product_id_1",
                  "product_source": "MANUAL",
		"product_decision": "ACCEPT"
                },
                {
                  "product_id":Your_product_id_2",
                  "product_source": "MANUAL",
		"product_decision": "ACCEPT"
                }
              ]
            }
```


#### Criar usando um post existente do Facebook com o tipo de mídia "foto/vídeo"

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/ads"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "object_story_id": "Your_object_story_id(pageID_postID)",
           "creative_sourcing_spec": {
              "associated_product_set_id": "Your_associated_product_set_id"
            },
            "degrees_of_freedom_spec": {
              "creative_features_spec": {
                "product_extensions": {
                  "enroll_status": "OPT_IN"
                },
                "multi_photo_to_video": {
                  "enroll_status": "OPT_IN"
                }
              }
            },
            "product_data": [
              {
                "product_id": Your_product_id_1",
                "product_source": "MANUAL",
		"product_decision": "ACCEPT"
              },
              {
                "product_id":Your_product_id_2",
                "product_source": "MANUAL",
		"product_decision": "ACCEPT"
              }
            ]
          }
```


#### Criar usando um post existente do Facebook com o tipo de mídia "álbum"

***Para posts com várias fotos, as extensões de produto serão adicionadas após a conversão das fotos em vídeo.** Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/ads"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "object_story_id": "Your_object_story_id(pageID_postID)",
           "creative_sourcing_spec": {
              "associated_product_set_id": "Your_associated_product_set_id"
            },
            "degrees_of_freedom_spec": {
              "creative_features_spec": {
                "product_extensions": {
                   "enroll_status": "OPT_IN"
                }
              }
            },
            "product_data": [
              {
                "product_id": Your_product_id_1",
                "product_source": "MANUAL"
		"product_decision": "ACCEPT"
              },
              {
                "product_id":Your_product_id_2",
                "product_source": "MANUAL"
		"product_decision": "ACCEPT"
              }
            ]
          }
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Etapa 4. criar o anúncio


Para criar o anúncio, você precisa associar o criativo ao conjunto de anúncios. Envie uma solicitação `POST` ao ponto de extremidade `/act_ad_account_id/ads`, sendo ***ad_account_id*** a identificação da conta de anúncio da Meta. A solicitação precisa incluir:


- `access_token`
- `adset_id` (da [Etapa 2](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adset))
- `creative_id` (da [Etapa 3](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad-creative))
- `name`
- `status`


#### Referência rápida sobre anúncios de contas de anúncios


| Parâmetro | Valor |
| --- | --- |
| access_token | O token de acesso à Página. |
| adset_id | O AD-SET-ID da Etapa 2. |
| creative_id | {"creative_id": "AD-CREATIVE-ID"} , sendo AD-CREATIVE-ID o ID da Etapa 3. |
| name | O nome do anúncio. |
| status | Definido como PAUSED . Quando a campanha estiver pronta para o lançamento, defina como ACTIVE |


#### Exemplo de solicitação de anúncio com criativo

*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **ad_account_id**) pelos seus valores.*
```
curl -X POST "https://graph.facebook.com/v25.0/act_ad_account_id/ads"
     -H "Content-Type: application/json"
     -d '{
           "access_token": "Your_page_access_token",
           "adset_id": "Your_ad_set_id",
           "creative": { "creative_id": "Your_ad_creative_id" },
           "status": "PAUSED"
         }'
```


Caso ela seja bem-sucedida, o app receberá a resposta JSON a seguir com a identificação do anúncio.

```
{
  "id": "ad_id"
}
```


### Chamada para ação


Também é possível definir uma chamada para ação ao criar um anúncio.

```
"call_to_action": {
  "value": {"app_destination":"MESSENGER"},
  "type": "MESSAGE_PAGE"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Etapa 5. Publicar o anúncio


Verifique se o anúncio existe no [Gerenciador de Anúncios](https://adsmanager.facebook.com/). Clique no botão **Conferir e publicar** no canto superior direito. Selecione a campanha, o conjunto de anúncios e o anúncio.


É possível publicar o anúncio pelo Gerenciador de Anúncios ou pela API. Para publicar pela API, repita a [Etapa 4](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad) com o parâmetro `status` definido como `ACTIVE`.


O anúncio ficará com o status `PENDING_REVIEW` e será analisado pela Meta. Depois da aprovação, ele terá o status `ACTIVE` e será veiculado.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Elementos avançados de clique para o Messenger


É possível criar mensagens que incluam mais do que um elemento de mensagem, como um comando para ligação telefônica ou vários modelos. Você pode adicionar esses elementos ao definir uma matriz de objetos como `*_data.page_welcome_message` em vez de um valor de string.


#### Referência rápida sobre matriz da mensagem de boas-vindas da Página


| Parâmetros de `page_welcome_message` | Valores |
| --- | --- |
| landing_screen_type enumeração | Definido como call_prompt ( obrigatório ). |
| media_type enumeração | Definido como text em anúncios com comando para ligação telefônica |
| message objeto | Use para incluir um ou mais modelos de mensagem no anúncio de clique para o Messenger. |
| text_format.message | Objeto para definir as ações do botão de comando para ligação telefônica text : o texto da mensagem de boas-vindas; call_prompt_data : o par chave-valor do texto da mensagem de comando para ligação telefônica ( obrigatório ) Defina call_prompt_message como o texto do comando para a pessoa ligar para sua empresa. } Por exemplo, Ligue e agende uma visita ( obrigatório ) |


### Adicionar um comando para ligação telefônica


É possível adicionar um comando para ligação telefônica ao anúncio com clique para o Messenger definindo o valor de `*_data.page_welcome_message` como uma matriz de objetos representando os elementos desse comando. Defina o parâmetro `landing_screen_type` como `call_prompt`, `media_type` como `text`, além do objeto `text_format.message` com `text` de boas-vindas e `call_prompt_data.call_prompt_message` definido como um comando de ligar para sua empresa.
*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
...
      "page_welcome_message": "[
        {
          "landing_screen_type": "call_prompt",
          "media_type": "text",
          "text_format": {
            "message": {
              "text": "Your_welcome_message",
              "call_prompt_data": {
                "call_prompt_message": "Your_call_prompt_message"
              }
            }
          },
        }
      ]"
...
```


### Adicionar um ou mais modelos


Para criar um anúncio com vários modelos, defina o parâmetro `*_data.page_welcome_message` como uma matriz com um [modelo de mensagem](https://developers.facebook.com/docs/messenger-platform/send-messages/templates). O exemplo a seguir adiciona um modelo de resposta rápida.
*Texto formatado para facilitar a leitura. Substitua os **valores em negrito e itálico** (como **page_access_token**) pelos seus valores.*
```
...
      "page_welcome_message": "[{
        'message': {
          'text':'  Your_question_or_directive  ',
          'quick_replies':[
            {
              'content_type':'text',
              'title':'  Option_1  ',
              'payload':'  Option_1_information_for_webhook  '
            },
            {
              'content_type':'text',
              'title':'  Option_2  ',
              'payload':'  Option_2_information_for_webhook  '
            },
            {
              'content_type':'text',
              'title':'  Option_3  ',
              'payload':'  Option_3_information_for_webhook  '
            }
          ]
        }
      }]",
...
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Próximas etapas


Se ainda não tiver feito isso, [configure webhooks](https://developers.facebook.com/docs/messenger-platform/webhooks) para receber notificações quando uma pessoa clicar no seu anúncio.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)

## Saiba mais


Saiba mais sobre a API de Marketing e outras opções de anúncios de clique para o Messenger.


#### API de Marketing


- [Referência sobre campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group)
- [Referência sobre criativos do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)
- [Referência sobre anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup)
- [Referência sobre conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign)
- [Referência sobre direcionamento de público](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting)
- [Como criar formulários para anúncios de lead](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create/)
- [Primeiros passos: API de Marketing](https://developers.facebook.com/docs/marketing-apis/get-started)
- [Como recuperar leads gerados por anúncios](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving)
- [Visão geral das metas de otimização e dos eventos de lances](https://developers.facebook.com/docs/marketing-api/bidding/overview/billing-events#opt_bids)


#### Plataforma do Messenger


- [Referência de modelos de mensagem](https://developers.facebook.com/docs/messenger-platform/reference/templates)
- [Referência de formulários de lead de mensagem](https://developers.facebook.com/docs/graph-api/reference/page/messenger_lead_forms/)
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#)Nesta Página[Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#an-ncios-de-clique-para-o-messenger)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#antes-de-come-ar)[Etapa 1. criar uma campanha](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#campaign)[Etapa 2. criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adset)[Etapa 3. fornecer um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad-creative)[Anúncios de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#an-ncios-de-clique-para-o-messenger-2)[Como preencher a mensagem de boas-vindas da Página](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#como-preencher-a-mensagem-de-boas-vindas-da-p-gina)[Clique para assinar](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#cts)[Anúncios de lead em conversas](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#leads)[Como gerar criativos de anúncio usando conteúdo do Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#como-gerar-criativos-de-an-ncio-usando-conte-do-do-instagram)[Como gerar criativos do anúncio usando conteúdo do Facebook](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#como-gerar-criativos-do-an-ncio-usando-conte-do-do-facebook)[Adicionar extensões de produto ao clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adicionar-extens-es-de-produto-ao-clique-para-o-messenger)[Etapa 4. criar o anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#ad)[Chamada para ação](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#chamada-para-a--o)[Etapa 5. Publicar o anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#publish-ad)[Elementos avançados de clique para o Messenger](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#elementos-avan-ados-de-clique-para-o-messenger)[Adicionar um comando para ligação telefônica](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adicionar-um-comando-para-liga--o-telef-nica)[Adicionar um ou mais modelos](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#adicionar-um-ou-mais-modelos)[Próximas etapas](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#pr-ximas-etapas)[Saiba mais](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-messenger#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Bi32Z5l90QBpvFxePSP48ZX8K3CsHddIf7v-1VPKfzwvBR8qY--u4lbIQvA_aem_mHLwR-l6r9OzGDI0LwpcnQ&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Bi32Z5l90QBpvFxePSP48ZX8K3CsHddIf7v-1VPKfzwvBR8qY--u4lbIQvA_aem_mHLwR-l6r9OzGDI0LwpcnQ&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7BmHaDBJDjC9ECK7C8vC80SRdGSggc_jxL7sqcFpK7OWCI9upA-UrRCLwVXQ_aem_8nLb5RRWjGrCjXPxAzkskg&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Bi32Z5l90QBpvFxePSP48ZX8K3CsHddIf7v-1VPKfzwvBR8qY--u4lbIQvA_aem_mHLwR-l6r9OzGDI0LwpcnQ&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6YXDntIqFQxLi9QLzv_0VdzH4-zOoZh31x6b2dYKIW48Gvs0swzVMNAqebHw_aem_lsNogoEfoWXtnFb6ntEisA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RD8zCmeU1rKnOlz3cNBYuo3WLvd30elmCBn1znBL42NUmVaRMjWjnxTl7fQ_aem_SDM5nzzyMkcNQt8f8JhVBQ&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6aU9a3aY7S7AC4PlhRMpubdNLsjXKYhmZw2yKL1Ghar1IFmSHJ_lQxZ5-ggQ_aem_Ae2pM9k0kyAqhunHRzqhTw&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59hWd7yDA1FUU8FhbMkNMXX_G_fpaL7Dx5CfEuX2lsnQAJB5sNm7weSOQO7A_aem_MX1asp383kZOKV7W9MLANA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59hWd7yDA1FUU8FhbMkNMXX_G_fpaL7Dx5CfEuX2lsnQAJB5sNm7weSOQO7A_aem_MX1asp383kZOKV7W9MLANA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RD8zCmeU1rKnOlz3cNBYuo3WLvd30elmCBn1znBL42NUmVaRMjWjnxTl7fQ_aem_SDM5nzzyMkcNQt8f8JhVBQ&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59hWd7yDA1FUU8FhbMkNMXX_G_fpaL7Dx5CfEuX2lsnQAJB5sNm7weSOQO7A_aem_MX1asp383kZOKV7W9MLANA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR46ywNQDtGt7PYNWQcx__QOTrqB5iTpKWu0JozrAWseIVtzFF9IapfgWz6VFA_aem_g0BN9Vn0uU0JDa5lUJW45w&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7BmHaDBJDjC9ECK7C8vC80SRdGSggc_jxL7sqcFpK7OWCI9upA-UrRCLwVXQ_aem_8nLb5RRWjGrCjXPxAzkskg&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5rRxDVwNk0dq4tPRbRtz5FkTYBkud9qnQ9T6fOOklmldL23o_FhODVbPmgyw_aem_xrQAuils7ivPJFIQy5fiMA&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT48IFr2J7jOq9MztzftPZMVfWyOEu_oWYn1A6sP1MozX16-aPxgfIu_Mvnbr_Op0k2u8cJE5razs8mx0QljemGX7iclXyM6smLncramArDm6ou6yRHcn6E44pzlXmyzlglFULpPd8iAn0qC6fS_J1PvjDM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão