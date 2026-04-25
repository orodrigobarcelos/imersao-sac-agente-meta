<!-- Fonte: Anúncios em vídeo e em carrossel _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios em vídeo e em carrossel

Updated: Dec 11, 2025Você pode criar, mensurar e otimizar facilmente anúncios de vídeo e em carrossel no Facebook por meio da API. Consulte [Anúncios em carrossel no Facebook para Empresas⁠](https://www.facebook.com/business/a/online-sales/carousel-link-ads). Para ver os formatos de vídeo compatíveis com anúncios, acesse [Vídeos na Central de Ajuda para o Anunciante⁠](https://www.facebook.com/business/help/1640701476174343?__mref=message_bubble).

### Limitações


- O `video_id` precisa estar associado à conta de anúncios.


## Anúncios em vídeo

Siga estas etapas para criar um anúncio em vídeo em um objetivo `VIDEO_VIEWS` e otimizar o alcance do lance:

- Etapa 1: [fornecer criativos do anúncio](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#create-ad-creative)
- Etapa 2: [criar campanha de anúncios](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#create-ad-campaign)
- Etapa 3: [criar um conjunto de anúncios](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#create-ad-set)
- Etapa 4: [criar um anúncio](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#create-ad)


### Etapa 1: fornecer [criativos do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative)

Crie um anúncio usando um ID de vídeo existente e um vídeo carregado no Facebook.Você precisará do seguinte:

- As permissões `pages_read_engagement` e `ads_management`
- Um [vídeo carregado](https://developers.facebook.com/docs/graph-api/video-uploads) para o ponto de extremidade `act_{ad-account-id}/advideos`

```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
  "page_id": "<PAGE_ID>",
  "video_data": {"image_url":"<THUMBNAIL_URL>","video_id":"<VIDEO_ID>"}
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Etapa 2: criar [campanha de anúncios](https://developers.facebook.com/docs/reference/ads-api/adcampaign)

Defina o objetivo como `VIDEO_VIEWS`:
```
curl -X POST \
  -F 'name="Video Views campaign"' \
  -F 'objective="OUTCOME_ENGAGEMENT"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```
Consulte [Referência: Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group), [AdObjectives em PHP⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-php-ads-sdk%2Fblob%2Fmaster%2Fsrc%2FFacebookAds%2FObject%2FValues%2FAdObjectives.php%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I) e [AdObjectives em Python⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-python-ads-sdk%2Fblob%2F199daddec0174ac45d4ee985490b987739cb13af%2Ffacebookads%2Fmixins.py%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA%23L128&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I).

### Etapa 3: criar um [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset)

Se a meta for o menor custo por visualização possível, será necessário emparelhar o objetivo da campanha de visualização do vídeo com `optimization_goal=THRUPLAY` de um conjunto de anúncios. Você pode definir `bidding_event` como `IMPRESSIONS` ou `THRUPLAY` para pagar por impressão ou por visualização do vídeo. Consulte [Anúncios com custo por ação](https://developers.facebook.com/docs/marketing-api/cost-per-action-ads).
```
curl \
  -F 'name=A CPV Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=500' \
  -F 'start_time=2024-05-06T04:45:29+0000' \
  -F 'end_time=2024-06-06T04:45:29+0000' \
  -F 'billing_event=THRUPLAY' \
  -F 'optimization_goal=THRUPLAY' \
  -F 'bid_amount=100' \
  -F 'targeting={
  "device_platforms": ["mobile"],
  "geo_locations": {"countries":["US"]},
  "publisher_platforms": ["facebook"]
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
As taxas de custo por visualização são menores para conjuntos de anúncios com `optimization_goal=THRUPLAY` se comparadas a CPVs de compras por alcance e frequência otimizadas para visualizações de vídeo. A data final deve estar no futuro. Consulte a [referência sobre conjunto de anúncios](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign).

### Etapa 4: criar um [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup)

Use o conjunto de anúncios e o criativo do anúncio existentes:
```
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
  "creative_id": "<CREATIVE_ID>"
  }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```

Quando um objetivo da campanha for `VIDEO_VIEWS`, por padrão, o anúncio terá as [especificações de rastreamento](https://developers.facebook.com/docs/reference/ads-api/tracking-specs) adequadas que definem as ações rastreadas de um anúncio. Por exemplo, visualizações do vídeo:
```
{'action.type':'video_view','post':'POST_ID','post.wall':'PAGE_ID'}
```
Consulte [Minhas campanhas do Gerenciador de Anúncios⁠](https://www.facebook.com/ads/manager/account/campaigns/) e a [referência Anúncio](https://developers.facebook.com/docs/marketing-api/adgroup).

#### Exemplo de reconhecimento da marca

Consulte o [blog de reconhecimento da marca](https://developers.facebook.com/ads/blog/post/2015/12/09/brand-awareness/) para criar um anúncio em vídeo para essa finalidade.

#### Exemplo de alcance e frequência

Para disponibilizar um vídeo a mais pessoas, use o objetivo da campanha de visualização do vídeo com [alcance e frequência](https://developers.facebook.com/docs/reference/ads-api/reachandfrequency). Você precisará criar uma previsão, reservá-la e atribuí-la ao seu conjunto de anúncios.Siga a [criação da visualização do vídeo](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#video_create), mas aplique alcance e frequência ao seu conjunto de anúncios. Especifique estes parâmetros adicionais:
```
-F "rf_prediction_id=<RESERVATION_ID>" \
```


## Vídeo para resposta direta

Para incentivar as pessoas a mudar do reconhecimento à ação, consulte [Criativo do vídeo no formato de carrossel](https://developers.facebook.com/ads/blog/post/2015/10/21/video-creative-in-carousel/).

- **Alcance pessoas que assistiram a um vídeo**. Do reconhecimento a afinidade e consideração. Consulte [Remarketing](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#remarketing).
- **Tenha engajamento com marcas e produtos**. Adicione uma chamada para ação para visitar uma página específica no seu site. Consulte [Chamada para ação](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#call_to_action).


### Remarketing

O remarketing de anúncios em vídeo oferece suporte para os anunciantes direcionarem para determinados públicos personalizados de vídeos orgânicos ou pagos no Facebook e Instagram. Use este recurso para mover pessoas do reconhecimento para os objetivos da parte mais inferior do funil, como afinidade e consideração. Consulte a [pesquisa Combinações de criativos que funcionam⁠](https://www.facebook.com/business/news/creative-ad-sequencing).Você precisa de permissão de anunciante para a página que contém um vídeo para criar um público para esse vídeo.Para o público, defina `subtype=ENGAGEMENT`. Então, defina as regras para o público que você deseja criar. Cada regra tem um `object_id`, por exemplo, ID de vídeo e `event_name`. O `event_name` será uma das seguintes opções:

- `video_watched` – o número de vezes em que o vídeo foi visto por um agregado de no mínimo 3 segundos ou por quase toda sua duração (o que acontecer primeiro).
- `video_completed` – o número de vezes nas quais o vídeo foi visto até a marca que corresponde a 95% da duração, inclusive visualizações em que as pessoas pularam até esse ponto.
- `video_view_10s` – o número de vezes em que o vídeo foi visto por um agregado de no mínimo 10 segundos ou por quase toda sua duração (o que acontecer primeiro).
- `video_view_15s` – o número de vezes em que o vídeo foi visto por um agregado de no mínimo 15 segundos ou por quase toda sua duração (o que acontecer primeiro).
- `video_view_25_percent` – o número de vezes nas quais o vídeo foi visto até a marca que corresponde a 25% da duração, inclusive visualizações em que as pessoas pularam até esse ponto.
- `video_view_50_percent` – o número de vezes nas quais o vídeo foi visto até a marca que corresponde a 50% da duração, inclusive visualizações em que as pessoas pularam até esse ponto.
- `video_view_75_percent` – o número de vezes nas quais o vídeo foi visto até a marca que corresponde a 75% da duração, inclusive visualizações em que as pessoas pularam até esse ponto.
Você pode combinar vídeos para criar um público baseado em vários vídeos e ações. Por exemplo, um público pode conter visualizações de três segundos do vídeo A e visualizações completas do vídeo B e C.Isso cria um público dos últimos 14 dias de espectadores que visualizaram o vídeo 1 por mais de 3 segundos, e os espectadores que visualizaram o vídeo 2 completamente. O público também será preenchido automaticamente com espectadores antes que ele seja criado com `prefill=true`.
```
curl \
  -F 'name=Video Ads Engagement Audience' \
  -F 'subtype=ENGAGEMENT' \
  -F 'description=Users who watched my video' \
  -F 'prefill=1' \
  -F 'rule=[
  {"object_id":"%video_id_1","event_name":"video_watched"},
  {"object_id":"%video_id_2","event_name":"video_completed"}
  ]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
A veiculação secundária é compatível com visualizações do vídeo depois de 16 de outubro de 2015.

### Chamada para ação

Os vídeos com comandos interativos de chamada para ação (CTA) estimulam as pessoas a saber mais e a visitar uma página específica em um site. Melhore o desempenho quando seu objetivo principal for gerar visualizações do vídeo ou reconhecimento da marca e seu objetivo secundário for gerar cliques fora do site. Você deve usar um anúncio de link de vídeo para o último. Como as CTAs funcionam:

- Para dispositivos móveis e desktop, é mostrada como parte do post. Quando o vídeo é pausado, é exibida ao lado da opção Retomar.
- Para dispositivos móveis, quando alguém clica em um vídeo para assistir em tela cheia, uma CTA flutuante aparece como uma imagem sobreposta do vídeo.
- Os posts de link de vídeo externo não exibem CTAs.
Você pode usar o vídeo com CTAs apenas com os seguintes objetivos de campanha:

- `PAGE_LIKES`
- [`LEAD_GENERATION`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/create#video)
- [`LOCAL_AWARENESS`](https://developers.facebook.com/docs/marketing-api/guides/local-awareness)
- `LINK_CLICKS`
- `CONVERSIONS`
- [`APP_INSTALLS`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/mobile-app-ads#create_video)
- `VIDEO_VIEWS`
- `BRAND_AWARENESS`
- [Ad for Mobile App](https://developers.facebook.com/docs/app-ads/formats/ad-for-mobile-app)
Consulte [Expansão de vídeo para objetivos adicionais](https://developers.facebook.com/ads/blog/post/2015/04/09/expansion-video-objectives/). Isso cria um anúncio em vídeo com a chamada para ação `GET_DIRECTIONS`:
```
curl \
  -F 'object_story_spec={
  "page_id": "<PAGE_ID>",
  "video_data": {
  "call_to_action": {
  "type": "GET_DIRECTIONS",
  "value": {
  "link": "fbgeo:\/\/37.48327, -122.15033, \"1601 Willow Rd Menlo Park CA\""
  }
  },
  "image_url": "<THUMBNAIL_URL>",
  "link_description": "Come check out our new store in Menlo Park!",
  "video_id": "<VIDEO_ID>"
  }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
   https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


## Métricas de vídeo


### Insights de post de vídeo, Orgânico

Saiba mais sobre o desempenho dos seus vídeos no Facebook e tome decisões mais informadas sobre o conteúdo de vídeo. Atualmente, oferecemos métricas apenas quando alguém começa a assistir aos vídeos. Essas métricas incluem visualizações do vídeo, visualizações do vídeo únicas, a duração média da visualização do vídeo e a retenção do público. Veja em quais partes as pessoas desistem do vídeo e as partes que as pessoas acham mais interessantes.

### Insights do anúncio em vídeo, Pago

Use a [API de Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/insights-api). A [resposta](https://developers.facebook.com/docs/marketing-api/reference/ads-insights) contém diversas métricas de vídeo.

### Tipo de vídeo

Recupere as estatísticas do anúncio em vídeo agrupadas por tipo de vídeo, como reprodução automática e clique para reproduzir. Inclua `action_video_type` em `action_breakdowns`. Os valores esperados para `action_video_type` são `total`, `click_to_play` e `auto_play`.**Estamos fazendo testes limitados com a opção `action_video_type` no momento.** Para identificar clientes com o detalhamento, verifique `CAN_USE_VIDEO_METRICS_BREAKDOWN` da [conta de anúncios](https://developers.facebook.com/docs/reference/ads-api/adaccount).
```
curl -G \
  -d 'action_breakdowns=action_video_type' \
  -d 'date_preset=last_30_days' \
  -d 'fields=actions,video_avg_pct_watched_actions,video_complete_watched_actions' \
  -d 'access_token= <ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```
A resposta inclui objetos com `action_type` como `video_view` e contém um `action_video_type` importante:
```
{
  "data": [
    {
      "actions": [
        ...
        {
          "action_type": "video_play",
          "value": 9898
        },
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 921129
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 915971
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 5158
        }
      ],
      "video_avg_pct_watched_actions": [
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 60.59
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 60.47
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 80.63
        }
      ],
      "video_complete_watched_actions": [
        {
          "action_type": "video_view",
          "action_video_type": "total",
          "value": 156372
        },
        {
          "action_type": "video_view",
          "action_video_type": "auto_play",
          "value": 154015
        },
        {
          "action_type": "video_view",
          "action_video_type": "click_to_play",
          "value": 2357
        }
      ],
      "date_start": "2014-12-26",
      "date_stop": "2015-03-25"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MA==",
      "after": "MA=="
    }
  }
}
```
Consulte [API de Insights](https://developers.facebook.com/docs/marketing-api/insights-api/getting-started).

## Anúncios em carrossel

Obtenha mais espaço para o criativo no Feed e leve as pessoas para seu site ou app para celular a fim de converter. Crie um anúncio em carrossel de duas formas:

- Criar um anúncio e um post sem exibição na Página em uma chamada: [API do criativo do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative).
- Criar um [post sem exibição na Página](https://developers.facebook.com/docs/reference/ads-api/unpublished-page-posts) e um [criativo do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative) por meio do post (indisponível para carrossel de vídeo).
**Os anúncios em carrossel não são compatíveis com o Facebook Stories.**

### Criar em linha

Crie um post da Página de anúncio em carrossel enquanto elabora um criativo do anúncio. Especifique o conteúdo do post da Página em `object_story_spec`. Isso criará um post sem exibição na Página a partir de `adcreatives`. Consulte os [criativos do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative#object_story_spec). Por exemplo:
```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "link_data": {
      "child_attachments": [
        {
          "description": "$8.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product1",
          "name": "Product 1",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$9.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product2",
          "name": "Product 2",
          "video_id": "<VIDEO_ID>"
        },
        {
          "description": "$10.99",
          "image_hash": "<IMAGE_HASH>",
          "link": "https:\/\/www.link.com\/product3",
          "name": "Product 3"
        }
      ],
      "link": "<URL>"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
A resposta é um ID do criativo:
```
{"id":"<CREATIVE_ID>"}
```


### Criar o post e depois o anúncio

Crie um post sem exibição na Página. `child_attachments` é uma [matriz de objetos de link](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads#spec). Em cada objeto de link, `picture`, `name` e `description` são opcionais. Você pode publicá-los apenas pela Página com um token de acesso à Página.
```
curl -X GET \
  -d 'message="Browse our latest products"' \
  -d 'published=0' \
  -d 'child_attachments=[
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 1",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 2",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 3",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       },
       {
         "link": "<APP_STORE_URL>",
         "name": "Product 4",
         "description": "$4.99",
         "image_hash": "<IMAGE_HASH>"
       }
     ]' \
  -d 'caption="WWW.EXAMPLE.COM"' \
  -d 'link="http://www.example.com/products"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/posts
```
Em seguida, forneça um criativo do anúncio com o post sem exibição na Página. Use `id` para `object_story_id` no seu criativo do anúncio.
```
curl -X POST \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Criar anúncio em carrossel com vídeos

Os anúncios em carrossel com vídeo podem ter "legenda" no anexo secundário para personalizar o URL de exibição no final da tela:
```
"child_attachments": [
 {
   "link": "https://www.facebookmarketingdevelopers.com/",
   "name": "Facebook Marketing Developers",
   "description": "Facebook Marketing Developers",
   "call_to_action": {
     "type": "APPLY_NOW",
     "value": {
      "link_title": "Facebook Marketing Developers"
     }
   },
   "video_id": "123",
   "caption": "mycustomlinkcaption.com"
  },
]
```
Para ver detalhes sobre os anexos secundários, use o ID e faça uma chamada à [Graph API, Vídeo, Referência](https://developers.facebook.com/docs/graph-api/reference/video).

### Criar anúncio de app para celular

Limitações:

- Os anúncios de app para celular em carrossel oferecem suporte a apenas um app
- Um mínimo de três imagens, em comparação com as duas imagens nos anúncios em carrossel que não são de app
- Os anúncios de app para celular em carrossel devem ter uma chamada para ação
- O cartão final, que normalmente exibe a foto do perfil da Página, não será exibido em anúncios de app para celular em carrossel. É necessário especificar o mesmo link da loja de apps em cada `child_attachment`. Você não precisa especificar o link novamente em `call_to_action:{'value':{'link':... }}}`.
Por exemplo, para criar um anúncio em carrossel para instalação de app para celular:
```
curl -X POST \
  -F 'name="Carousel app ad"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "link_data": {
         "message": "My message",
         "link": "http://www.example.com/appstoreurl",
         "caption": "WWW.ITUNES.COM",
         "name": "The link name",
         "description": "The link description",
         "child_attachments": [
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           },
           {
             "link": "http://www.example.com/appstoreurl",
             "image_hash": "<IMAGE_HASH>",
             "call_to_action": {
               "type": "USE_MOBILE_APP",
               "value": {
                 "app_link": "<DEEP_LINK>"
               }
             }
           }
         ],
         "multi_share_optimized": true
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Você pode publicar apenas seu post como a Página do Facebook associada ao app para celular. Você precisa usar um token de acesso à Página.
```
curl \
  -F 'message=My description' \
  -F 'link=<APP_STORE_URL>' \
  -F 'caption=WWW.ITUNES.COM' \
  -F 'child_attachments=[
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    },
    {
      "link": "<APP_STORE_URL>",
      "image_hash": "<IMAGE_HASH_I>",
      "call_to_action": {
        "type": "USE_MOBILE_APP",
        "value": {"app_link":"<DEEP_LINK_I>","link_title":"<LINK_TITLE_I>"}
      }
    }
  ]' \
  -F 'multi_share_optimized=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```
Use o `id` da resposta para criar AdCreative:
```
curl -X POST \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


## Especificação de campo

Este é um anúncio em carrossel no iOS, mostrando como os campos descritos são usados.

| Nome | Descrição |
| --- | --- |
| child_attachments tipo: objeto | Uma matriz de objetos de link com 2 a 10 elementos exigidos para anúncios em carrossel. Use pelo menos 3 objetos para obter um desempenho otimizado. O uso de 2 objetos serve para permitir integrações leves e pode causar resultados abaixo do esperado para a campanha. |
| child_attachments.link tipo: cadeia de caracteres | URL do link ou URL da loja de apps anexado ao post. Obrigatório. |
| child_attachments.picture Tipo: URL | A imagem de prévia associada a esse link. Taxa de proporção 1:1 e um mínimo de 458 x 458 px para melhor exibição. É preciso especificar picture ou image_hash . |
| child_attachments.image_hash tipo: cadeia de caracteres | Hash de uma imagem de prévia associada ao link da sua biblioteca de imagens . Use a taxa de proporção 1:1 e um mínimo de 458 x 458 px para uma melhor exibição. É preciso especificar picture ou image_hash . |
| child_attachments.name tipo: cadeia de caracteres | Título da prévia do link. Se não especificado, o título da página vinculada será usado. Normalmente truncado depois de 35 caracteres. Defina um name único, já que as interfaces do Facebook mostram ações relatadas por name . |
| child_attachments.description tipo: string | Um preço, desconto ou domínio de site. Se não especificado, o conteúdo da página vinculada será extraído e usado. Normalmente truncado depois de 30 caracteres. |
| child_attachments.call_to_action tipo: objeto | Chamada para ação opcional. Consulte Chamada para ação . Você não precisa especificar o link novamente em call_to_action:{'value':{'link':... }}} . |
| child_attachments.video_id tipo: cadeia de caracteres | ID do vídeo do anúncio . Pode ser usado em qualquer elemento secundário. Se especificado, será necessário definir image_hash ou picture . |
| message tipo: string | Corpo principal do post, também chamado de mensagem de status. |
| link tipo: cadeia de caracteres | URL de um link para “Ver mais”. Obrigatório. |
| caption tipo: cadeia de caracteres | URL para exibir no link “Ver mais”. Não aplicável para anúncios de app móvel em carrossel |
| multi_share_optimized tipo: booliano | Se for definido como true , as imagens e links serão selecionadas e ordenadas de forma automática. Caso contrário, use a ordem original dos elementos secundários. O padrão é true . |
| multi_share_end_card tipo: booliano | Se for definido como false , o cartão final que exibe o ícone da página será removido. O padrão é true . |


## Estatísticas do anúncio por produto

Reúna ações para anúncios em carrossel por produto com `actions_breakdown=['action_carousel_card_id', 'action_carousel_card_name']`. Cada `child_attachment` tem um ID de cartão diferente. `action_carousel_card_id` e `action_carousel_card_name` só se aplicam a anúncios em carrossel.Obtenha as seguintes estatísticas por cartão:

- `website_ctr` – disponível ao especificar `fields=['website_ctr']`.
- `app_install`, `app_use`, `apps.uses`, `credit_spent`, `mobile_app_install`, `tab_view`, `link_click`, `mobile_app_install`, `app_custom_event.*` e `offsite_conversion.*` – disponíveis ao especificar `fields=['actions']`. Outras ações não estão disponíveis com um detalhamento do cartão.

```
curl -G \
  -d 'action_breakdowns=["action_type","action_carousel_card_id"]' \
  -d 'level=ad' \
  -d 'date_preset=last_30_days' \
  -d 'time_increment=all_days' \
  -d 'breakdowns=placement' \
  --data-urlencode 'filtering=[
    {
      "field": "action_type",
      "operator": "IN",
      "value": ["link_click"]
    }
  ]' \
  -d 'fields=impressions,inline_link_clicks,actions,website_ctr' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```
Resposta:
```
{
...
   "website_ctr": [
      {
         "action_carousel_card_id": "1",
         "action_type": "link_click",
         "value": 51.401869158878
      },
      {
         "action_carousel_card_id": "2",
         "action_type": "link_click",
         "value": 50.980392156863
      }
   ],
   "placement": "mobile_feed",
   "date_start": "2015-05-25",
   "date_stop": "2015-05-28"
}
```
Também é possível solicitar `cost_per_action_type` para recuperar o detalhamento dos custos por tipo de ação:
```
curl -G \
  -d 'action_breakdowns=["action_type","action_carousel_card_name"]' \
  -d 'level=ad' \
  -d 'breakdowns=placement' \
  -d 'fields=impressions,campaign_name,cost_per_action_type' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```
Modelo de resposta:
```
{
   "data": [
      {
         "impressions": "1862555",
         "campaign_name": "My Campaign",
         "cost_per_action_type": [
            {
               "action_carousel_card_name": "My Carousel Card 1",
               "action_type": "app_custom_event.fb_mobile_activate_app",
               "value": 0.093347346315861
            },
            {
               "action_carousel_card_name": "My Carousel Card 2",
               "action_type": "app_custom_event.fb_mobile_activate_app",
               "value": 0.38324089579301
            },
            ...
         ],
      }
   ]
}
```


- As métricas de detalhamento de carrossel de `action_report_time=impression` são imprecisas para datas anteriores a 20 de junho de 2015.
- As métricas de detalhamento de carrossel de `action_report_time=conversion` são imprecisas para datas anteriores a 20 de julho de 2015.


## Posicionamentos

Se você selecionar somente `right_hand_column` como o posicionamento, poderá usar apenas um formato de carrossel ou de vídeo único no grupo de anúncios. Não há compatibilidade com o formato de vídeo se apenas um posicionamento `right_hand_column` for selecionado. Consulte [Direcionamento e posicionamento avançados](https://developers.facebook.com/docs/marketing-api/targeting-specs).Por exemplo, crie um conjunto de anúncios em que `right_hand_column` é o único posicionamento:
```
curl \
  -F 'name=RHS only Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=500' \
  -F 'start_time=2017-11-21T15:41:36+0000' \
  -F 'end_time=2017-11-28T15:41:36+0000' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'bid_amount=100' \
  -F 'targeting={
    "device_platforms": ["mobile"],
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["facebook"] ,
    "facebook_positions": ["right_hand_column"] ,
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
Forneça um criativo de anúncio com vídeo:
```
curl \
  -F 'name=Sample Creative' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "video_data": {"image_url":"<THUMBNAIL_URL>","video_id":"<VIDEO_ID>"}
  }' \
  -F 'access_token=ACCESS_TOKEN' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
Ou forneça um formato de anúncio do Canvas para o criativo do anúncio:
```
curl \
  -F 'image_hash=<IMAGE_HASH>' \
  -F 'object_story_spec={
    "link_data": {
      "call_to_action": {"type":"LEARN_MORE"},
      "image_hash": "<IMAGE_HASH>",
      "link": "CANVAS_LINK",
      "name": "Creative message"
    },
    "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
Se você tentar criar um anúncio com o conjunto de anúncios e o criativo do anúncio:
```
curl \
  -F 'name=My Ad' \
  -F 'adset_id=<AD_SET_ID>' \
  -F 'creative={"creative_id":"<CREATIVE_ID>"}' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
Caso você receba um código de erro, forneça um criativo compatível ou altere o direcionamento.

## Veja também


- [Guia de carregamento de vídeos no Facebook](https://developers.facebook.com/docs/graph-api/video-uploads)
- [Carrossel para anúncios de app para celular](https://developers.facebook.com/ads/blog/post/2015/05/11/carousel-app-ads)
- [Referência da Graph API para Feed de Página](https://developers.facebook.com/docs/graph-api/reference/page/feed)
- [Posts sem exibição na Página](https://developers.facebook.com/docs/reference/ads-api/unpublished-page-posts)
- [Criativos do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative)
- [Anúncios em carrossel do Instagram](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads#carousel)
Did you find this page helpful?ON THIS PAGELimitaçõesAnúncios em vídeoEtapa 1: fornecer criativos do anúncioEtapa 2: criar campanha de anúnciosEtapa 3: criar um conjunto de anúnciosEtapa 4: criar um anúncioExemplo de reconhecimento da marcaExemplo de alcance e frequênciaVídeo para resposta diretaRemarketingChamada para açãoMétricas de vídeoInsights de post de vídeo, OrgânicoInsights do anúncio em vídeo, PagoTipo de vídeoAnúncios em carrosselCriar em linhaCriar o post e depois o anúncioCriar anúncio em carrossel com vídeosCriar anúncio de app para celularEspecificação de campoEstatísticas do anúncio por produtoPosicionamentosVeja também$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$