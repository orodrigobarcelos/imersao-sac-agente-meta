<!-- Fonte: Anúncios no Audience Network - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audience-network -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios no Audience Network


O [Audience Network](https://developers.facebook.com/products/app-monetization/audience-network/) do Facebook exibe anúncios em sites para celular e apps iOS e Android de outros publishers. Você pode usar as opções de direcionamento do Facebook para encontrar o seu público nesses apps e sites para celular.


Nesta página, veja as [Regras do Audience Network para posicionamento e criativo do anúncio](https://developers.facebook.com/docs/marketing-api/audience-network#creative-placement). Depois, veja como criar anúncios:


- [Anúncio básico do Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#create-audience-network-ad)
- [Anúncios para dispositivos móveis](https://developers.facebook.com/docs/marketing-api/audience-network#mobile-ads)
- [Anúncios em carrossel](https://developers.facebook.com/docs/marketing-api/audience-network#example_carousel)
- [Anúncios de vídeo](https://developers.facebook.com/docs/marketing-api/audience-network#example_video)
- [Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/audience-network#example_dpa)


Saiba também como [ver uma prévia](https://developers.facebook.com/docs/marketing-api/audience-network#preview) e [mensurar](https://developers.facebook.com/docs/marketing-api/audience-network#measurement) o anúncio.


## Criativo do anúncio e posicionamento


O Audience Network do Facebook entrega a imagem do anúncio ao app de destino:


#### Criativo do anúncio compatível


- [Anúncios de imagem no app para celular](https://developers.facebook.com/docs/reference/ads-api/mobile-app-ads)
- [Anúncios de vídeo no app para celular](https://developers.facebook.com/docs/marketing-api/mobile-app-ads/#create_video)
- [Anúncios com link](https://developers.facebook.com/docs/marketing-api/audience-network#example_link)
- Anúncios de vídeo com link
- [Link em carrossel e anúncios de app](https://developers.facebook.com/docs/marketing-api/guides/carousel-ads)
- [Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads)


#### [Objetivos](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group) compatíveis


- `MOBILE_APP_INSTALLS`
- `MOBILE_APP_ENGAGEMENT`
- `LINK_CLICKS`, consulte [Blog, Expansões de vídeo para cliques para o site](https://developers.facebook.com/ads/blog/post/2015/06/09/video-website-clicks/)
- `CONVERSIONS`, consulte [Blog, Opções extras para vídeos](https://developers.facebook.com/ads/blog/post/2015/04/09/expansion-video-objectives/#web_conv)
- `PRODUCT_CATALOG_SALES`


#### Lances


Use a combinação de tipos de lance, `billing event` e `optimization goal`.


#### Plataforma do publisher


É preciso usar `audience_network` com outra plataforma, como o `facebook`. **Não é possível exibir anúncios somente no Audience Network.**


| publisher_platform | Descrição |
| --- | --- |
| audience_network | Isso permite a exibição do anúncio no Audience Network. |


#### Restrições


Os tamanhos IAB não são compatíveis.
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Criar anúncio no Audience Network


Por exemplo, para criar um anúncio com link a ser veiculado:


#### Etapa 1


Crie uma campanha de anúncios. Defina `objective` como `LINK_CLICKS` ou `CONVERSIONS`:

```
curl -X POST \ -F 'name="My campaign"' \ -F 'objective="OUTCOME_TRAFFIC"' \ -F 'status="PAUSED"' \ -F 'special_ad_categories=[]' \ -F 'is_adset_budget_sharing_enabled=0' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Etapa 2


Crie um conjunto de anúncios com posicionamento do Audience Network:

```
curl \ -F 'name=My Ad Set' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'billing_event=LINK_CLICKS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "device_platforms": ["mobile"], "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Para o [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset), especifique um [posicionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/#placement) e defina `publisher_platforms` no `targeting` do anúncio como `audience_network`.


#### Etapa 3


Forneça o criativo do anúncio com link:

```
curl \ -F 'name=Sample Creative' \ -F 'object_story_spec={ "link_data": { "image_hash": "<IMAGE_HASH>", "link": "<URL>", "message": "try it out" }, "page_id": "<PAGE_ID>" }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Etapa 4


Criar anúncio:

```
curl -X POST \ -F 'name="My Ad"' \ -F 'adset_id="<AD_SET_ID>"' \ -F 'creative={ "creative_id": "<CREATIVE_ID>" }' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Anúncios para dispositivos móveis


### Anúncio de imagem para o Audience Network


Para criar um anúncio de imagem para app para celular com o posicionamento do Audience Network:


#### Etapa 1


Crie uma campanha de anúncios. Defina `objective` como `APP_INSTALLS` ou [`MOBILE_APP_ENGAGEMENT`](https://developers.facebook.com/docs/app-ads/formats/engagement-ads):

```
curl -X POST \ -F 'name="Mobile App Installs Campaign"' \ -F 'objective="OUTCOME_APP_PROMOTION"' \ -F 'status="PAUSED"' \ -F 'special_ad_categories=[]' \ -F 'is_adset_budget_sharing_enabled=0' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Etapa 2


Crie o conjunto de anúncios. Especifique o posicionamento do Audience Network e defina `promoted_object` como ID do app:

```
curl \ -F 'name=Mobile App Installs Ad Set' \ -F 'promoted_object={"application_id":"<APP_ID>","object_store_url":"<APP_STORE_URL>"}' \ -F 'optimization_goal=APP_INSTALLS' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "device_platforms": ["mobile"], "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"], "user_os": ["IOS"] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Etapa 3


Elabore o criativo de imagem do anúncio de app para celular:

```
curl \ -F 'object_story_spec={ "link_data": { "call_to_action": {"type":"INSTALL_MOBILE_APP","value":{"link":"<APP_STORE_URL>"}}, "image_hash": "<IMAGE_HASH>", "link": "<APP_STORE_URL>", "message": "Message", "name": "Link title" }, "page_id": "<PAGE_ID>" }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Etapa 4


Criar anúncio:

```
curl -X POST \ -F 'name="My Ad"' \ -F 'adset_id="<AD_SET_ID>"' \ -F 'creative={ "creative_id": "<CREATIVE_ID>" }' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


Consulte [Anúncios de app para celular](https://developers.facebook.com/docs/reference/ads-api/mobile-app-ads).


### Anúncio de vídeo para o Audience Network


Para criar um anúncio de vídeo de app para celular com o posicionamento do Audience Network, siga as etapas 1 e 2 em **Anúncio de imagem para o Audience Network**. Em seguida, forneça o criativo do vídeo:

```
curl \ -F 'object_story_spec={ "page_id": "<PAGE_ID>", "video_data": { "call_to_action": {"type":"INSTALL_MOBILE_APP","value":{"link":"<APP_STORE_URL>"}}, "image_url": "<THUMBNAIL_URL>", "video_id": "<VIDEO_ID>" } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Por fim, crie o anúncio. Veja a etapa 4 em **Anúncio de imagem para o Audience Network**.


### Anúncio de vídeo com link para o Audience Network


Para criar um anúncio de vídeo com link com o posicionamento do Audience Network:


#### Etapa 1


Crie uma campanha de anúncios com o `objective` definido como `LINK_CLICKS` ou `CONVERSIONS`:

```
curl -X POST \ -F 'name="My campaign"' \ -F 'objective="OUTCOME_TRAFFIC"' \ -F 'status="PAUSED"' \ -F 'special_ad_categories=[]' \ -F 'is_adset_budget_sharing_enabled=0' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Etapa 2


Crie um conjunto de anúncios com posicionamento do Audience Network:

```
curl \ -F 'name=My Ad Set' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'billing_event=LINK_CLICKS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "device_platforms": ["mobile"], "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Etapa 3


Carregue um vídeo com o link. Carregue um [vídeo na sua página](https://developers.facebook.com/docs/graph-api/reference/page/videos), que ainda não tenha sido publicado, com um link de chamada para ação. Também é possível carregar vídeos na [biblioteca de vídeos](https://developers.facebook.com/docs/marketing-api/advideo) da conta de anúncios:

```
curl \ -F "title=Book your trip to Alaska" \ -F "picture=http://thumbnailurl.com/pic1" \ -F "source=<VIDEO_FORM_DATA>" \ -F "published=0" \ -F "call_to_action={'type':'BOOK_TRAVEL','value':{'link':'http://example.com'}}" \ -F "access_token=<PAGE_TOKEN>" \ https://graph-video.facebook.com/v25.0/<PAGE_ID>/videos
```


#### Etapa 4


Forneça o [criativo do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative). Use a identificação do post da Página para fornecer:

```
curl -X POST \ -F 'name="Sample Promoted Post"' \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Etapa 5


Criar anúncio:

```
curl -X POST \ -F 'name="My Ad"' \ -F 'adset_id="<AD_SET_ID>"' \ -F 'creative={ "creative_id": "<CREATIVE_ID>" }' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Anúncios em carrossel


No Audience Network, o Facebook exibe somente os dois primeiros `child_attachments` no seu carrossel, na ordem fornecida. Para anúncios em carrossel no Audience Network, observe que:


- O `objective` da campanha precisa ser `MOBILE_APP_INSTALLS`, `MOBILE_APP_ENGAGEMENT`, `LINK_CLICKS` ou `CONVERSIONS`
- A `targeting/publisher_platforms` do conjunto de anúncios precisa incluir `audience_network`


Consulte [Guia de anúncios de produtos](https://www.facebook.com/business/ads-guide/), [API de Prévia](https://developers.facebook.com/docs/marketing-api/generatepreview) e [Anúncios em carrossel](https://developers.facebook.com/docs/marketing-api/guides/carousel-ads#create).
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Anúncios em vídeo


Especifique o posicionamento do Audience Network no direcionamento no nível do conjunto de anúncios:

```
"audience_network_positions": [ "classic", "instream_video"]
```


Consulte [Anúncios de vídeo](https://developers.facebook.com/docs/marketing-api/guides/videoads).
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Anúncios de catálogo Advantage+


Para usar o Audience Network como posicionamento de Anúncios de Catálogo Advantage+:


- A campanha precisa conter `objective=PRODUCT_CATALOG_SALES`
- A `targeting/publisher_platforms` do conjunto de anúncios precisa incluir `audience_network`


Consulte [Advantage+ Catalog Ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management).
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Prévia do anúncio


Para ver uma prévia do anúncio no Audience Network:


#### Etapa 1


Faça uma chamada do tipo `/previews` para o [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup)


#### Etapa 2


Especifique `ad_format=`:


- `MOBILE_BANNER` no caso de app para celular ou banner da web,
- `MOBILE_INTERSTITIAL` no caso de app intersticial para celular ou
- `MOBILE_NATIVE` no caso de app para celular ou prévias de formato nativo da web
- `MOBILE_MEDIUM_RECTANGLE`
- `MOBILE_FULLWIDTH`
- `AUDIENCE_NETWORK_INSTREAM_VIDEO`
- `AUDIENCE_NETWORK_OUTSTREAM_VIDEO`
- `AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE`
- `AUDIENCE_NETWORK_REWARDED_VIDEO`
- `AUDIENCE_NETWORK_NATIVE_BANNER`
- `MESSENGER_MOBILE_INBOX_MEDIA`


#### Etapa 3


As prévias de web móvel são exibidas da mesma maneira que em apps para celular.

```
https://graph.facebook.com/<API_VERSION>/<AD_ID>/previews?ad_format=MOBILE_BANNER
https://graph.facebook.com/<API_VERSION>/<AD_ID>/previews?ad_format=MOBILE_INTERSTITIAL
https://graph.facebook.com/<API_VERSION>/<AD_ID>/previews?ad_format=MOBILE_NATIVE
```


A API retorna um iFrame que faz referência ao próprio CSS e gera a imagem da prévia. O iFrame é válido por apenas 24 horas. Consulte [referência sobre prévias do anúncio](https://developers.facebook.com/docs/reference/ads-api/generatepreview).
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)

## Mensuração


Para saber mais sobre o desempenho do anúncio em feeds de vídeos sugeridos, consulte `/insights` com `breakdowns=['publisher_platform']`. Veja a [Guia de Insights sobre anúncios](https://developers.facebook.com/docs/marketing-api/insights-api/getting-started). Os resultados têm esta aparência:

```
{
  ......
  "spend": 9.23,
  "today_spend": 0,
  "total_action_value": 0,
  "total_actions": 1,
  "total_unique_actions": 1,
  "link_clicks": 0,
  "placement": "mobile_feed"
},
{
  ......
  "spend": 7.73,
  "today_spend": 0,
  "total_action_value": 0,
  "total_actions": 6,
  "total_unique_actions": 5,
  "link_clicks": 3,
  "placement": "mobile_video_channel"
},
{
  ......
  "spend": 6.23,
  "today_spend": 0,
  "total_action_value": 0,
  "total_actions": 3,
  "total_unique_actions": 2,
  "link_clicks": 1,
  "placement": "desktop_video_channel"
},
```


`mobile_feed` refere-se ao Feed no Facebook para Celular, `mobile_video_channel` são feeds de vídeos sugeridos para celular e `desktop_video_channel` são feeds de vídeos sugeridos para desktop.
[○](https://developers.facebook.com/docs/marketing-api/audience-network#)[○](https://developers.facebook.com/docs/marketing-api/audience-network#)Nesta Página[Anúncios no Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#an-ncios-no-audience-network)[Criativo do anúncio e posicionamento](https://developers.facebook.com/docs/marketing-api/audience-network#creative-placement)[Criar anúncio no Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#create-audience-network-ad)[Anúncios para dispositivos móveis](https://developers.facebook.com/docs/marketing-api/audience-network#mobile-ads)[Anúncio de imagem para o Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#an-ncio-de-imagem-para-o-audience-network)[Anúncio de vídeo para o Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#an-ncio-de-v-deo-para-o-audience-network)[Anúncio de vídeo com link para o Audience Network](https://developers.facebook.com/docs/marketing-api/audience-network#an-ncio-de-v-deo-com-link-para-o-audience-network)[Anúncios em carrossel](https://developers.facebook.com/docs/marketing-api/audience-network#example_carousel)[Anúncios em vídeo](https://developers.facebook.com/docs/marketing-api/audience-network#example_video)[Anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/audience-network#example_dpa)[Prévia do anúncio](https://developers.facebook.com/docs/marketing-api/audience-network#preview)[Mensuração](https://developers.facebook.com/docs/marketing-api/audience-network#measurement) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6HtpotCWTrMMFdfCWRlslHBxCUJcdBziKsaaTzIzOMQoJjhkMspbUzNSb7Kw_aem_e6TRMwIwRNwexBZgUMjWRw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eTeXK2M2-c9HcQl8PVfLbJ9h5E7v8-Fi-TYxQv3yWTffIDH1WvP4CUqyqQw_aem_x_otxain2Abc9V0rtXbTVA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7uonhbAiX2B7ehp3RqyZoyHFAnWLNYNVRK7mGkzR6lrTADeIptbXqe5NXS9w_aem_4G9T_6tudjIeNAneLJUylA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eTeXK2M2-c9HcQl8PVfLbJ9h5E7v8-Fi-TYxQv3yWTffIDH1WvP4CUqyqQw_aem_x_otxain2Abc9V0rtXbTVA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5lR86YqlQUx6QRpR4o2vVQoZurCzBxXzdwsBV8iDXgVYLYPamCg4E0GxiBWw_aem_iXh0IyuP1O6HhYU0AEwRZA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5sjmreJ6AxmVf6CZzAzYeLkqodwIOfQH965D0iznkQR0BwUYhGFfr35_PoEw_aem_kpQmrD5As_dhSip05rr-dg&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Qtx3slX59aQQ3AT7GMy4x2xspG7Ipd3Nf-tBrXFQVJn8l_iCO3Y6u1fSfyA_aem_O02N2tORx1Cw4khT1yleUw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5mUFH3W2vJQDRaElWYM6hcfdtmr2H-1mUicXQ2uB6iEgGKKOOtkFH00iD3hw_aem_7iV-53FGDwGDEQHaFZ_bnw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eTeXK2M2-c9HcQl8PVfLbJ9h5E7v8-Fi-TYxQv3yWTffIDH1WvP4CUqyqQw_aem_x_otxain2Abc9V0rtXbTVA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Qtx3slX59aQQ3AT7GMy4x2xspG7Ipd3Nf-tBrXFQVJn8l_iCO3Y6u1fSfyA_aem_O02N2tORx1Cw4khT1yleUw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6qFT8B6wyYkIbLpMnQb_O8ocCANdUAgdOHLshqaBAAifiJIl91xu_uR_5isw_aem_b__i2nil1qofS9FFUnyiuQ&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Qtx3slX59aQQ3AT7GMy4x2xspG7Ipd3Nf-tBrXFQVJn8l_iCO3Y6u1fSfyA_aem_O02N2tORx1Cw4khT1yleUw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5mUFH3W2vJQDRaElWYM6hcfdtmr2H-1mUicXQ2uB6iEgGKKOOtkFH00iD3hw_aem_7iV-53FGDwGDEQHaFZ_bnw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Qtx3slX59aQQ3AT7GMy4x2xspG7Ipd3Nf-tBrXFQVJn8l_iCO3Y6u1fSfyA_aem_O02N2tORx1Cw4khT1yleUw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5mUFH3W2vJQDRaElWYM6hcfdtmr2H-1mUicXQ2uB6iEgGKKOOtkFH00iD3hw_aem_7iV-53FGDwGDEQHaFZ_bnw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6HtpotCWTrMMFdfCWRlslHBxCUJcdBziKsaaTzIzOMQoJjhkMspbUzNSb7Kw_aem_e6TRMwIwRNwexBZgUMjWRw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6HtpotCWTrMMFdfCWRlslHBxCUJcdBziKsaaTzIzOMQoJjhkMspbUzNSb7Kw_aem_e6TRMwIwRNwexBZgUMjWRw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6SemcfrzXe1l-ClnGkHv7WAyUX1RTf2bFzJGhXt15pogoT2mGWyuIdq2-3YQ_aem_b35YgfEIj5lLI7X3WzqCcw&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4eTeXK2M2-c9HcQl8PVfLbJ9h5E7v8-Fi-TYxQv3yWTffIDH1WvP4CUqyqQw_aem_x_otxain2Abc9V0rtXbTVA&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5C5HEQUTynrmu9IxSmJQp2uSSGHRK0FlMNxM5YBReEmbKhci7b20p9zyjelA_aem_ZZM3AIK1u4b2XxOZo00V6g&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4WD1yJ3oA9sSyzwwhenuAahP1Y2n2Vw0rKjadGpFa8v3P6KwqmiQLeF6ug_EKvtlBdRY28Olsor7r_Rf70tPO68SEG7Evwmi1EKaDT-tmNp6fnEQFUAJdqnQxhX2ZIZ8YXAvnKmd6NkzaMjxuyDF-abmo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão