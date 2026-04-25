<!-- Fonte: Anúncios no App - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/mobile-app-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de app


Este documento descreve várias unidades de anúncio desenvolvidas para impulsionar mais instalações e engajamento com apps para celular e computador.


Use essa unidade de anúncio se quiser atrair pessoas ao seu app para computador ou celular para fins de instalação ou engajamento via foto, vídeo, [carrossel](https://developers.facebook.com/docs/marketing-api/guides/multi-product-ads) ou [criativos interativos](https://www.facebook.com/business/help/412951382532338).


Em termos conceituais, isso possibilita os seguintes anúncios:


|  | Foto | Vídeo | Carrossel | Interativos |
| --- | --- | --- | --- | --- |
| Anúncio de instalação de app para celular | ✓ | ✓ | ✓ | ✓ |
| Anúncio de engajamento de app para celular | ✓ | ✓ | ✓ |  |
| Anúncio de instalação para desktop | ✓ | ✓ | ✓ |  |
| Anúncio de engajamento para desktop | ✓ | ✓ | ✓ |  |
| Anúncios de app para desktop de mercadorias virtuais | ✓ | ✓ | ✓ |  |


Os anúncios de app para desktop de mercadorias virtuais são um subconjunto do engajamento para desktop. Você pode usar ofertas de mercadorias virtuais para retomar o engajamento e convencer os pagantes a usar o app novamente. Por exemplo, um app pode oferecer desconto em um item ou um conjunto da moeda no app em um feed para envolver novamente os antigos clientes. Veja como configurar o app para aceitar pagamentos [aqui](https://developers.facebook.com/docs/payments/ads_virtual_goods).


Para sua referência, a unidade com a imagem de instalação no app para celular é assim:


O anúncio de app para desktop de mercadorias virtuais com imagem é assim:


### Pré-requisitos


- Para criar um anúncio de app, o desenvolvedor deverá concluir as etapas deste [tutorial](https://developers.facebook.com/docs/tutorials/mobile-app-ads/).
- O anunciante deve ter uma Página do Facebook por meio da qual veiculará esses anúncios.


## Criar


Ao [criar](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#create) o anúncio, observe os seguintes requisitos:


- O objetivo da [campanha](https://developers.facebook.com/docs/marketing-api/adcampaign) deve ser `APP_INSTALLS`, `LINK_CLICKS` ou `CONVERSIONS`.
- O [objeto promovido do conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/adset/#promoted_object) deve ser definido.
- [Direcionamento](https://developers.facebook.com/docs/marketing-api/targeting-specs).
- Para anúncios de app para celular, é obrigatório usar o campo [`user_os` da especificação de direcionamento móvel](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/#mobile). O [posicionamento](https://developers.facebook.com/docs/marketing-api/targeting-specs/#placement) deve ter um campo `device_platforms` com o valor ["`mobile`"] e recomendar o uso dos outros campos da especificação para fazer o direcionamento de dispositivos móveis no Facebook. Opcionalmente, se quiser usar somente certas plataformas, você poderá especificar `publisher_platforms`.
- Para anúncios de app de canvas, `device_platforms` deve ser `desktop`. Opcionalmente, será possível especificar `facebook_positions` se você não quiser o Feed nem a coluna do lado direito do Facebook para desktop.
- Em caso de uso de `GET_OFFER` para mercadorias virtuais, deverá haver desconto no preço. Consulte a documentação sobre [mercadorias virtuais](https://developers.facebook.com/docs/payments/ads_virtual_goods) para saber mais.


### Chamadas para ação de anúncio de app:


As chamadas para ação adicionais listadas abaixo estão disponíveis para anúncios de app no campo `call_to_action` de um [post](https://developers.facebook.com/docs/graph-api/reference/page/feed) ou na [`object_story_spec` de um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/adcreative/#object_story_spec). Você também pode especificar o deep link do app para celular no campo `app_link` ou o objeto de mercadoria virtual do app para computador no campo `product_link`.


| Chave | Valor | Obrigatório |
| --- | --- | --- |
| tipo | Tipos de chamada para ação de dispositivos móveis independentemente de instalação ou de engajamento: SHOP_NOW BOOK_TRAVEL LEARN_MORE SIGN_UP DOWNLOAD INSTALL_MOBILE_APP USE_MOBILE_APP WATCH_VIDEO WATCH_MORE OPEN_LINK Tipos de chamada para ação de instalação ou engajamento para computador: USE_APP (apps para computador) PLAY_GAME (apps de jogos para desktop) Tipos de chamada para ação para anúncios de app para desktop de mercadorias virtuais: BUY_NOW GET_OFFER | sim |
| valor | Dicionário JSON de {"link": "\<APP_STORE_LINK\>", "app_link": "\<MOBILE_DEEP_LINK\>", "product_link": "\<VIRTUAL_GOOD_DEEP_LINK\>", "link_title": "\<NAME_FOR_LINK\>"} | sim Apenas alguns valores são obrigatórios. |
| value.link | Faz referência a App Store, Google Play Store ou URL do app Canvas do Facebook, por exemplo: https://itunes.apple.com/br/app/facebook/id284882215 | sim |
| value.app_link | Definir o destino do deep link somente para apps para celular, por exemplo, myapp://product/12345 . Para especificar um deep link de apps para computador, determine-o diretamente no campo de link de URL. | Sim, apenas para anúncios de engajamento ou de instalação de app para celular. |
| value.product_link | Para definir a URL que aponta para o objeto da mercadoria virtual Open Graph do produto. Saiba mais sobre os detalhes da configuração aqui . | Sim, somente para mercadorias virtuais para desktop. |
| value.link_title | Permite personalizar o nome do link, que será exibido sob a imagem do anúncio. | não |


#### Especificação de campos


### Criar com foto


Para criar um anúncio de app para celular ou desktop com uma foto, primeiro faça um post de link na Página com uma foto por meio do campo [`object_story_spec: {'link_data': ...}` do criativo do anúncio](https://developers.facebook.com/docs/marketing-api/adcreative/#object_story_spec).


**Exemplo:**

```
curl -X POST \ -F 'name="Sample Creative"' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "link_data": { "call_to_action": { "type": "INSTALL_MOBILE_APP", "value": { "link": "<APP_STORE_URL>" } }, "image_hash": "<IMAGE_HASH>", "link": "<APP_STORE_URL>", "message": "Try it out" } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Como alternativa, você pode criar o post da Página por meio do [ponto de extremidade do feed](https://developers.facebook.com/docs/graph-api/reference/page/feed) da Página e usar a identificação do post no criativo. Consulte abaixo a seção [Exemplos](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#examples) para saber mais.


### Criar com carrossel


Para criar um anúncio de instalação do app para celular ou um anúncio de engajamento por meio do formato de anúncio em carrossel, siga as instruções nos [documentos sobre anúncios em carrossel](https://developers.facebook.com/docs/marketing-api/guides/multi-product-ads), mas especifique um link da loja de apps em cada campo `link` de `child_attachments`.


#### Considerações


- No momento, os anúncios de app para celular em carrossel são compatíveis somente com um app.
- Número mínimo de 3 imagens (em comparação com 2 nos anúncios em carrossel que não são de app).
- Anúncios de app para celular em carrossel devem ter uma chamada para ação definida.
- O cartão final (que normalmente mostra a foto de perfil da Página) não será exibido para anúncios de app para celular em carrossel.


É necessário especificar o mesmo link da loja de apps em cada `child_attachment`. Você não precisa especificar o link novamente em `call_to_action:{'value':{'link':... }}}`.

```
curl -X POST \ -F 'name="Carousel app ad"' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "link_data": { "message": "My message", "link": "http://www.example.com/appstoreurl", "caption": "WWW.ITUNES.COM", "name": "The link name", "description": "The link description", "child_attachments": [ { "link": "http://www.example.com/appstoreurl", "image_hash": "<IMAGE_HASH>", "call_to_action": { "type": "USE_MOBILE_APP", "value": { "app_link": "<DEEP_LINK>" } } }, { "link": "http://www.example.com/appstoreurl", "image_hash": "<IMAGE_HASH>", "call_to_action": { "type": "USE_MOBILE_APP", "value": { "app_link": "<DEEP_LINK>" } } }, { "link": "http://www.example.com/appstoreurl", "image_hash": "<IMAGE_HASH>", "call_to_action": { "type": "USE_MOBILE_APP", "value": { "app_link": "<DEEP_LINK>" } } }, { "link": "http://www.example.com/appstoreurl", "image_hash": "<IMAGE_HASH>", "call_to_action": { "type": "USE_MOBILE_APP", "value": { "app_link": "<DEEP_LINK>" } } } ], "multi_share_optimized": true } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Criar com vídeo


Para criar um anúncio de app com um vídeo, primeiro carregue o vídeo em questão na [biblioteca de vídeos da conta de anúncios](https://developers.facebook.com/docs/marketing-api/advideo). Depois, use o ID do vídeo no campo [`object_story_spec: {'video_data':...}` do criativo do anúncio](https://developers.facebook.com/docs/marketing-api/adcreative/#object_story_spec).


**Exemplo:**

```
curl \ -F 'name=Sample Creative' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "video_data": { "call_to_action": {"type":"INSTALL_MOBILE_APP","value":{"link":"<APP_STORE_URL>"}}, "image_url": "<THUMBNAIL_URL>", "video_id": "<VIDEO_ID>" } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Como alternativa, você pode criar o post por meio do [ponto de extremidade de vídeo](https://developers.facebook.com/docs/graph-api/reference/video) da Página e usar o ID do vídeo no criativo. Consulte abaixo a seção [Exemplos](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#examples) para saber mais.
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Ler


Para recuperar detalhes sobre seu post da Página, consulte os [documentos sobre post de link na Página](https://developers.facebook.com/docs/graph-api/reference/link) ou [post de vídeo na Página](https://developers.facebook.com/docs/graph-api/reference/video).


Você pode listar todos os posts da borda [`/promotable_posts`](https://developers.facebook.com/docs/graph-api/reference/page/feed/) da Página.

```
curl https://graph.facebook.com/v25.0/<PAGE_ID>/promotable_posts
```


Para recuperar detalhes do seu criativo do anúncio, consulte a [documentação sobre criativos do anúncio.](https://developers.facebook.com/docs/reference/ads-api/adcreative#read)
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Mensuração de apps para celular


[Consulte a documentação principal dos anúncios de app.](https://developers.facebook.com/docs/app-ads/measuring-your-app-ad)
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Deep links


### Antes de começar


- Configure o app para que ele [aceite deep links](https://developers.facebook.com/docs/ads-for-apps/mobile-app-ads#deep-linking).
- A [permissão `pages_manage_ads`](https://developers.facebook.com/docs/pages/overview#permissions).
- Um token de acesso à Página solicitado por uma pessoa que possa executar a [tarefa `ADVERTISE`](https://developers.facebook.com/docs/pages/overview#tasks) na Página.
- O [link do app](https://developers.facebook.com/docs/applinks/), se houver compatibilidade com esse tipo de link.


#### Exemplo de código


```
"call_to_action={ 'type':'LEARN_MORE', 'value':{ 'link':'https://itunes.apple.com/us/app/facebook/id284882215', 'app_link':'facebook://path/to/page' } }"
```


Antes de especificar um link de app, é necessário confirmar se ele foi extraído. Para isso, faça a chamada a seguir:

```
https://graph.facebook.com/v25.0/?type=og&scrape=true&id=<APP_LINK>
```
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Insights sobre o app para celular


Os insights são aplicados somente a anúncios com um [objeto promovido](https://developers.facebook.com/docs/marketing-api/adset/#promoted_object) que contenha o ID do app. Para obter esse ID, [inscreva](https://developers.facebook.com/docs/tutorials/mobile-app-ads) o app no Facebook.


A Meta fornecerá insights diários agregados sobre os dados demográficos das pessoas que instalaram o app. Para recuperar esses dados, use um token de acesso ao app e faça uma consulta

```
https://graph.facebook.com/v25.0/<APP_ID>/insights/application_mobile_app_installs?&access_token=<ACCESS_TOKEN
```


Também é possível detalhar as estatísticas ao especificar um parâmetro adicional de URL, `breakdown`, equivalente a um dos valores a seguir. No momento, não é possível combinar detalhamentos.


| Nome | Descrição |
| --- | --- |
| gender_age | Detalhe suas estatísticas sobre idade e gênero do público. |
| country | Detalhe suas estatísticas sobre o país do público. |
| locale | Detalhe suas estatísticas sobre a localidade do público. |


**Exemplos:**

```
https://graph.facebook.com/v25.0/<APP_ID>/insights/application_mobile_app_installs?breakdown=gender_age&access_token=<ACCESS_TOKEN> https://graph.facebook.com/v25.0/<APP_ID>/insights/application_mobile_app_installs?breakdown=country&access_token=<ACCESS_TOKEN> https://graph.facebook.com/v25.0/<APP_ID>/insights/application_mobile_app_installs?breakdown=locale&access_token=<ACCESS_TOKEN>
```
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Exemplos


### Criar um anúncio de imagem para instalação do app para celular


Etapa 1: crie o post da Página com a imagem. Lembre-se de que é necessário usar o `PAGE_ACCESS_TOKEN` e a sessão de API da Página para criar um post.

```
curl \ -F 'message=Sign up today' \ -F 'picture=<IMAGE_URL>' \ -F 'link=<LINK>' \ -F 'published=1' \ -F 'call_to_action={"type":"SIGN_UP","value":{"link":"<LINK>"}}' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```


Etapa 2: desenvolva o criativo do anúncio (`{STORY_ID}` está como `'{PAGE_ID}_{POST_ID}'`).

```
curl -X POST \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Etapa 3: use o criativo em um anúncio.

```
curl -X POST \ -F 'name="My AdGroup with Redownload"' \ -F 'adset_id="<AD_SET_ID>"' \ -F 'creative={ "creative_id": "<CREATIVE_ID>" }' \ -F 'redownload=1' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Criar um anúncio de imagem para app para celular com um deep link, otimizando-o para cliques e pagando por impressões


Etapa 1: crie o post da Página com a imagem. Lembre-se de que é necessário usar o `PAGE_ACCESS_TOKEN` e a sessão de API da Página para criar um post.

```
url -X POST \ -F 'message="This is a test message"' \ -F 'call_to_action={ "type": "BUY_NOW", "value": { "link": "<APP_STORE_URL>", "app_link": "<DEEP_LINK>" } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```


Etapa 2: desenvolva o criativo do anúncio.

```
curl -X POST \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Etapa 3: defina os lances no conjunto de anúncios, otimizando para cliques e pagando por impressões.

```
curl \ -F 'name=LifetimeBudgetSet' \ -F 'lifetime_budget=100000' \ -F 'bid_amount=500' \ -F 'billing_event=IMPRESSIONS' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'promoted_object={"application_id":"<APP_ID>","object_store_url":"<APP_STORE_URL>"}' \ -F 'targeting={ "facebook_positions": ["feed"], "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"], "user_os": ["IOS"] }' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'end_time=2018-02-06T04:45:30+0000' \ -F 'status=PAUSED' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Etapa 4: use o criativo em um anúncio.

```
curl \ -F 'name=My Ad' \ -F 'adset_id=<AD_SET_ID>' \ -F 'creative={"creative_id":"<CREATIVE_ID>"}' \ -F 'redownload=1' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Criar um anúncio de imagem de engajamento com o app para celular com um [link de app](https://l.facebook.com/l.php?u=http%3A%2F%2Fapplinks.org%2F&h=AT5L1KXkjNXDpxXwRebVXTkPsGzWoaRmDPDAhGgQh5ikS9FPJ2DhSk3UP7rm1Q-xyMUW4N_NqxajcHmmNs2SoCY4T1Ewv000dNlFtlbz99MtHFO6osk6TEIrz3XG4_kUp5GSD1I6TKRlODVQC7lWvKeV0Dc), otimizando para eventos do app e pagando por impressões


Etapa 1: crie o post da Página com a imagem. Lembre-se de que é necessário usar o `PAGE_ACCESS_TOKEN` e a sessão de API de Páginas para criar um post.

```
curl \ -F 'message=Check out this App today. Available on iTunes.' \ -F 'published=1' \ -F 'link=<APP_STORE_URL>' \ -F 'picture=<IMAGE_URL>' \ -F 'call_to_action={ "type": "LEARN_MORE", "value": {"link":"<APP_STORE_URL>","app_link":"<APP_DEEP_LINK>"} }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```


Etapa 2: desenvolva o criativo do anúncio.

```
curl -X POST \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Etapa 3: defina os lances no conjunto de anúncios, otimizando para obter mais eventos do app e pagando por impressões.


Observe que também é necessário definir o `promoted_object` do conjunto de anúncios para incluir um `custom_event_type` para a otimização. Consulte os [documentos sobre conjuntos de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) para saber mais.

```
curl -X POST \ -F 'name="A CPA Ad Set optimized for App Events"' \ -F 'campaign_id="<AD_CAMPAIGN_ID>"' \ -F 'daily_budget=300' \ -F 'start_time="2025-11-13T15:11:01-0800"' \ -F 'end_time="2025-11-20T15:11:01-0800"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'optimization_goal="OFFSITE_CONVERSIONS"' \ -F 'bid_amount=100' \ -F 'status="PAUSED"' \ -F 'promoted_object={ "application_id": "<APP_ID>", "object_store_url": "<APP_STORE_URL>", "custom_event_type": "PURCHASE" }' \ -F 'targeting={ "facebook_positions": [ "feed" ], "geo_locations": { "countries": [ "US" ] }, "user_os": [ "iOS" ] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Etapa 4: use o criativo em um anúncio.

```
curl \ -F 'name=My Ad' \ -F 'adset_id=<AD_SET_ID>' \ -F 'creative={"creative_id":"<CREATIVE_ID>"}' \ -F 'redownload=1' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Exemplos de anúncios de post da Página


Lembre-se de que é necessário usar o `PAGE_ACCESS_TOKEN` e a sessão de API de Páginas para criar um post.


### Criar um anúncio de vídeo para instalação do app para celular


```
curl \ -F 'name=My Video' \ -F 'message=Check out this app!' \ -F 'thumbnail=<APP_STORE_URL>' \ -F 'published=0' \ -F 'call_to_action={"type":"INSTALL_MOBILE_APP","value":{"link":"<APP_STORE_URL>"}}' \ -F 'source=@<VIDEO_PATH>' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/videos
```


### Criar um anúncio de vídeo para apps para celular com um deep link


```
curl \ -F 'name=My Video' \ -F 'message=Check out this app!' \ -F 'thumbnail=<APP_STORE_URL>' \ -F 'published=0' \ -F 'call_to_action={ "type": "LEARN_MORE", "value": {"link":"<APP_STORE_URL>","app_link":"<APP_DEEP_LINK>"} }' \ -F 'source=@<VIDEO_PATH>' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/videos
```


### Criar um anúncio de vídeo para instalação do app para computador


```
curl \ -F 'name=My Video' \ -F 'message=Check out this app!' \ -F 'thumbnail=<THUMBNAIL_PATH>' \ -F 'published=0' \ -F 'call_to_action={"type":"PLAY_GAME","value":{"link":"<THUMBNAIL_PATH>"}}' \ -F 'source=@<VIDEO_PATH>' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/videos
```


### Criar anúncios de app para computador para anúncio de imagem de mercadorias virtuais


```
curl \ -F 'message=Buy coins now!' \ -F 'picture=<IMAGE_URL>' \ -F 'link=<LINK>' \ -F 'published=1' \ -F 'call_to_action={"type":"BUY_NOW","value":{"link":"<LINK>","product_link":"<PRODUCT_LINK>"}}' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/feed
```


### Criar anúncios de app para computador para um anúncio de vídeo de mercadorias virtuais


```
curl \ -F 'name=My Video' \ -F 'message=Buy coins now!' \ -F 'thumbnail=<THUMBNAIL_PATH>' \ -F 'published=0' \ -F 'call_to_action={ "type": "BUY_NOW", "value": {"link":"<THUMBNAIL_PATH>","product_link":"<THUMBNAIL_PATH>"} }' \ -F 'source=@<VIDEO_PATH>' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PAGE_ID>/videos
```


### Criar anúncios de app com objetivos Reconhecimento


Para fornecer tratamento universal de link para o objetivo Reconhecimento, é possível incluir o ID do app em `creative.template_url_spec`. Caso ele não seja fornecido, o anúncio levará os usuários para seu site.

```
curl \ -F 'name=Advantage+ Catalog Ads Template Creative Sample' \ -F 'template_url_spec={ "config": { "app_id": "1596400373958175" } }' \ -F 'access_token=<CCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Criar anúncios estáticos com o comportamento de app fallback da web do objetivo Tráfego


Quando um app é selecionado em um conjunto de anúncios, esta será a alteração em `object_story_spec` depois que o fallback da web for adicionado.

```
curl -X POST \ -F 'name="Traffic app fallback web sample"' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "template_data": { "call_to_action": { "type": "INSTALL_MOBILE_APP", "value": { "link": "https://www.example.com" “app_link”: “<DEEPLINK_URL> “object_store_urls”: [ <STORE_URL_OF_APP> ] } }, "message": "Test {{product.name | titleize}}", "link": "https://www.example.com"", "name": "Headline {{product.price}}", "description": "Description {{product.description}}" } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Se o fallback precisar ser uma loja, forneça o respectivo URL no campo `link`. Se o fallback precisar ser um site, forneça o valor `object_store_urls` como uma lista com apenas um valor — o URL da loja de apps do app — e o campo `link` com o URL de fallback do site.
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Anúncios de catálogo Advantage+ para instalação do app para celular


Os [anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/) podem incentivar pessoas a instalar seu app para celular. Dessa forma, você pode redirecionar anúncios de instalação de app para celular às pessoas de acordo com o comportamento dos usuários.


Etapa 1: crie uma campanha para seu catálogo de produtos.

```
curl -X POST \ -F 'name="App Installs Campaign with Dynamic Product Ads"' \ -F 'objective="OUTCOME_APP_PROMOTION"' \ -F 'status="PAUSED"' \ -F 'special_ad_categories=[]' \ -F 'is_adset_budget_sharing_enabled=0' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


Etapa 2: crie um conjunto de anúncios para um conjunto de produtos específico do catálogo de produtos acima.

```
curl \ -F 'name=Mobile App Installs Ad Set with Dynamic Product Ads' \ -F 'bid_amount=3000' \ -F 'billing_event=IMPRESSIONS' \ -F 'optimization_goal=APP_INSTALLS' \ -F 'daily_budget=15000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"], "device_platforms": ["mobile"], "user_os": ["IOS"], "dynamic_audience_ids": ["<PRODUCT_AUDIENCE_ID>"] }' \ -F 'promoted_object={ "product_set_id": "<PRODUCT_SET_ID>", "application_id": "<APP_ID>", "object_store_url": "<APP_STORE_URL>" }' \ -F 'status=PAUSED' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Etapa 3: desenvolva o criativo dos anúncios de catálogo Advantage+ usando o modelo.

```
curl -X POST \ -F 'name="Advantage+ catalog ads template creative sample"' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "template_data": { "call_to_action": { "type": "INSTALL_MOBILE_APP", "value": { "link": "http://www.example.com/appstoreurl" } }, "message": "Test {{product.name | titleize}}", "link": "http://www.example.com/appstoreurl", "name": "Headline {{product.price}}", "description": "Description {{product.description}}" } }' \ -F 'product_set_id="<PRODUCT_SET_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Etapa 4: use o criativo do anúncio acima em um anúncio.

```
curl \ -F 'name=My Ad' \ -F 'adset_id=<AD_SET_ID>' \ -F 'creative={"creative_id":"<CREATIVE_ID>"}' \ -F 'redownload=1' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Carregar o arquivo HTML interativo na conta de anúncios


```
curl -X POST \ -F "name=<NAME>" \ -F "source=<>" \ -F "access_token=<ACCESS_TOKEN>" \ "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adplayables"
```


- `name`: nome que diferencia o ativo dos outros anúncios interativos na conta de anúncios, por exemplo, `{ad_name}` -> `{playable_asset_name}`
- `source`: caminho absoluto do arquivo na sua máquina local.
- `access_token`: pode ser gerado no [Explorador da Graph API](https://developers.facebook.com/tools/explorer/).
- Você também pode usar um número de identificação do ativo interativo na conta de anúncios.


#### Metatag em arquivo HTML interativo


É possível adicionar duas tags de metadados ao seu arquivo HTML 5 interativo. Isso permite que a Meta atribua ao seu app o elemento interativo nos anúncios.

```
... <head> ... <meta name="ref-application-id" content="<YOUR_APP_ID>"><meta name="ref-asset-id" content="<YOUR_ASSET_ID>"> ... </head> ...
```


- Forneça a identificação do app da Meta e a metatag do número de identificação do ativo no arquivo HTML interativo. Isso ajuda a Meta a fornecer insights precisos sobre o ativo quando ele aparecer no seu anúncio.
- O número de identificação do ativo identifica esse elemento interativo no seu sistema.


#### Criar anúncios na conta de anúncios


- Configure posicionamentos no Feed do Facebook. Apenas vídeo com incentivo e intersticial do Audience Network. Entre em contato com seu parceiro da Meta para obter mais informações.
- O criativo só pode ser um vídeo com taxa de proporção >= 1.
- Configurar o orçamento e a programação
- Gere o criativo interativo na API:

```
curl \ -F 'name=Sample Creative' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "video_data": { "call_to_action": { "type":"INSTALL_MOBILE_APP", "value":{ "application":<APP_ID>, "link":"<APP_STORE_URL>" } }, "image_url": "<THUMBNAIL_URL>", "link_description": "try it out", "video_id": "<VIDEO_ID>" } }' \ -F 'playable_asset_id=<PLAYABLE_ASSET_ID>' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


- Crie o anúncio na API:

```
curl \ -F 'name=My Ad' \ -F 'status=ACTIVE' \ -F 'adset_id=<AD_SET_ID>' \ -F 'creative={"creative_id":"<CREATIVE_ID>"}' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Otimização de eventos do app


[Consulte a documentação sobre otimização de eventos do app para Anúncios no App](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad#app-events-opt-via-api).


### Otimização de valor


[Consulte a documentação sobre otimização de valor para Anúncios no App](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad#value-optimization).
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)

## Saiba mais


- [Anúncios de app no Facebook](https://developers.facebook.com/docs/app-ads/creating-ads)
- [Anúncios de engajamento no app para celular](https://developers.facebook.com/docs/app-ads/formats/engagement-ads)
- [Anúncios do app para computador](https://developers.facebook.com/docs/ads-for-apps/installs-desktop)
- [Deep linking dos apps para celular](https://developers.facebook.com/docs/app-ads/deep-linking)
- [Audience Network](https://developers.facebook.com/docs/reference/ads-api/audience-network)
[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)[○](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#)Nesta Página[Anúncios de app](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#an-ncios-de-app)[Criar](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#create)[Chamadas para ação de anúncio de app:](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#cta_definitions)[Criar com foto](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#create_image)[Criar com carrossel](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#create_carousel)[Criar com vídeo](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#create_video)[Ler](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#read)[Mensuração de apps para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#measurement)[Deep links](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#deep_links)[Antes de começar](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#antes-de-come-ar)[Insights sobre o app para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#insights)[Exemplos](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#examples)[Criar um anúncio de imagem para instalação do app para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-um-an-ncio-de-imagem-para-instala--o-do-app-para-celular)[Criar um anúncio de imagem para app para celular com um deep link, otimizando-o para cliques e pagando por impressões](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-um-an-ncio-de-imagem-para-app-para-celular-com-um-deep-link--otimizando-o-para-cliques-e-pagando-por-impress-es)[Criar um anúncio de imagem de engajamento com o app para celular com um link de app, otimizando para eventos do app e pagando por impressões](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#example_mae_ocpm_app_events)[Exemplos de anúncios de post da Página](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#exemplos-de-an-ncios-de-post-da-p-gina)[Criar um anúncio de vídeo para instalação do app para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-um-an-ncio-de-v-deo-para-instala--o-do-app-para-celular)[Criar um anúncio de vídeo para apps para celular com um deep link](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-um-an-ncio-de-v-deo-para-apps-para-celular-com-um-deep-link)[Criar um anúncio de vídeo para instalação do app para computador](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-um-an-ncio-de-v-deo-para-instala--o-do-app-para-computador)[Criar anúncios de app para computador para anúncio de imagem de mercadorias virtuais](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-an-ncios-de-app-para-computador-para-an-ncio-de-imagem-de-mercadorias-virtuais)[Criar anúncios de app para computador para um anúncio de vídeo de mercadorias virtuais](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-an-ncios-de-app-para-computador-para-um-an-ncio-de-v-deo-de-mercadorias-virtuais)[Criar anúncios de app com objetivos Reconhecimento](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-an-ncios-de-app-com-objetivos-reconhecimento)[Criar anúncios estáticos com o comportamento de app fallback da web do objetivo Tráfego](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#criar-an-ncios-est-ticos-com-o-comportamento-de-app-fallback-da-web-do-objetivo-tr-fego)[Anúncios de catálogo Advantage+ para instalação do app para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#dpa)[Carregar o arquivo HTML interativo na conta de anúncios](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#playable-html)[Otimização de eventos do app](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#mai_eventopt)[Otimização de valor](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#otimiza--o-de-valor)[Saiba mais](https://developers.facebook.com/docs/marketing-api/mobile-app-ads#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e9mmMuXuQ-lgihMNNVCMJMHA1sSk0WOVksi1CIeecLe4DZN7PvPGAWidrnA_aem_c1Z7Pgdm1UG2P8H7aEwMhg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5S76bU9qaoBrO_CPx_GWHHJcsVg7arrKPw5VWhvxsLaGceibNtLQVQGFLnEQ_aem_bIMH9QYHnms0b-W6wSqfCA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4nkdXpOBte4B2Fy6n0_AUeRYxJ1TRTXnUXEmcQ1Olufvooj3SnzinpthB-JA_aem_BXR7tHQcn3b_7UhsPmhP3A&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e9mmMuXuQ-lgihMNNVCMJMHA1sSk0WOVksi1CIeecLe4DZN7PvPGAWidrnA_aem_c1Z7Pgdm1UG2P8H7aEwMhg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e9mmMuXuQ-lgihMNNVCMJMHA1sSk0WOVksi1CIeecLe4DZN7PvPGAWidrnA_aem_c1Z7Pgdm1UG2P8H7aEwMhg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6AiSd1eRSCVQCVX_R1Aj51sI9lsuTJGbme6SDPl437FZ-7KzRKA1RhR7Ssdg_aem_s4_fkMvcUUUYEZvrm9lQcg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4nkdXpOBte4B2Fy6n0_AUeRYxJ1TRTXnUXEmcQ1Olufvooj3SnzinpthB-JA_aem_BXR7tHQcn3b_7UhsPmhP3A&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4PtOHFJ49EWi434-nl0PoLlvvTWDmPB8co6sbS190s_7zB4xgsdMgQ5TYXJA_aem_VT6bY3yLo95sr-DHslPQxA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e9mmMuXuQ-lgihMNNVCMJMHA1sSk0WOVksi1CIeecLe4DZN7PvPGAWidrnA_aem_c1Z7Pgdm1UG2P8H7aEwMhg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51zYGO5QUL3miO8SNruXcO7C-VOZc9RFrR_a4OauKA0lA-gVAxryYxCbdRJw_aem_h-U7wTHQ5d2d6GIX2WSNtA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65somQFvo0kAX-ZUX-wiXG5NyIQOs_FQ4HaEwJJj9zkU8lcmIvRIlp4lHvWw_aem_a-WtfR7IgKsVB9mZrIpdpA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65somQFvo0kAX-ZUX-wiXG5NyIQOs_FQ4HaEwJJj9zkU8lcmIvRIlp4lHvWw_aem_a-WtfR7IgKsVB9mZrIpdpA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5N-AqsYV7gfAGf5aiuvlDpZisZq6Kosojtn7dXh0DnYpT3S2SY9jg72E0uNA_aem_aqX4w66Z3HPF56BoAf9ubg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65somQFvo0kAX-ZUX-wiXG5NyIQOs_FQ4HaEwJJj9zkU8lcmIvRIlp4lHvWw_aem_a-WtfR7IgKsVB9mZrIpdpA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6AiSd1eRSCVQCVX_R1Aj51sI9lsuTJGbme6SDPl437FZ-7KzRKA1RhR7Ssdg_aem_s4_fkMvcUUUYEZvrm9lQcg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ZrSK4FtyXkMnAyn0U_9TubJxIjAm9_mykYE8yAwlrZOdcZmXs1g8Ja_9zmA_aem_OTs5Af7NMr9rY3vOYf_exQ&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5N-AqsYV7gfAGf5aiuvlDpZisZq6Kosojtn7dXh0DnYpT3S2SY9jg72E0uNA_aem_aqX4w66Z3HPF56BoAf9ubg&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5S76bU9qaoBrO_CPx_GWHHJcsVg7arrKPw5VWhvxsLaGceibNtLQVQGFLnEQ_aem_bIMH9QYHnms0b-W6wSqfCA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65somQFvo0kAX-ZUX-wiXG5NyIQOs_FQ4HaEwJJj9zkU8lcmIvRIlp4lHvWw_aem_a-WtfR7IgKsVB9mZrIpdpA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4PtOHFJ49EWi434-nl0PoLlvvTWDmPB8co6sbS190s_7zB4xgsdMgQ5TYXJA_aem_VT6bY3yLo95sr-DHslPQxA&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7S2wTU5XqjwfLeb4rVyciSbRuaoV-UdyOWkWZXz6A0RxXCbq7ddhXRdKIPqMtnCL7uBYgde2A-ILupXpjyBVIrL7Sl5_3BSQtBXUM7zfGtAkoNMK8ZZJSiI2bx2A0tWqUGrOuvNuGszHvFWs_RJxx0a3o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão