<!-- Fonte: Criativo do anúncio - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/creative -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Criativo do anúncio


Use os anúncios do Facebook com seus clientes existentes e também para alcançar novos clientes. Cada guia descreve produtos de anúncios do Facebook para ajudar a atingir suas metas de publicidade. Há vários tipos de unidades de anúncio com diversas opções de aparência, posicionamento e criativo. Confira as diretrizes sobre unidades de anúncio como conteúdo do criativo no [Guia de anúncios do Facebook](https://www.facebook.com/business/ads-guide/?tab0=Mobile%20News%20Feed).


## Criativo


Um criativo do anúncio é um objeto que contém todos os dados necessários para renderizar visualmente o próprio anúncio. A API inclui diferentes tipos de anúncios que podem ser criados no Facebook. Eles estão listados [aqui](https://developers.facebook.com/docs/reference/ads-api/adcreative#overview).


Caso você tenha uma [campanha](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group) com o objetivo de engajamento com o post da Página, agora será possível criar um anúncio que promove um post feito pela Página. Consideramos isso um anúncio de post da Página. Os anúncios de post da Página exigem um campo `object_story_id`, que é a propriedade `id` de um post desse tipo. Saiba mais na [referência Criativo do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative#create).


Um criativo do anúncio tem três partes:


- O criativo do anúncio em si, definido pelos atributos visuais do objeto correspondente
- O [posicionamento](https://developers.facebook.com/docs/marketing-api/creative#placements) no qual o anúncio é veiculado
- A [prévia](https://developers.facebook.com/docs/marketing-api/creative#previews) da unidade conforme o posicionamento


Para criar o objeto do criativo do anúncio, faça a seguinte chamada:

```
curl -X POST \ -F 'name="Sample Promoted Post"' \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


A resposta à chamada de API é o `id` do objeto do criativo. Guarde isso, você precisará dele para o objeto do anúncio:

```
curl -X POST \ -F 'name="My Ad"' \ -F 'adset_id="<AD_SET_ID>"' \ -F 'creative={ "creative_id": "<CREATIVE_ID>" }' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Limites


Existem limites sobre texto, tamanho da imagem, taxa de proporção da imagem e outros aspectos do criativo. Consulte o [Guia de anúncios](https://www.facebook.com/business/ads-guide).


### Ler


Na API de Anúncios, é necessário solicitar de forma explícita todos os campos que você quer recuperar, exceto `id`. A [referência](https://developers.facebook.com/docs/reference/ads-api/adcreative/#read) de cada objeto tem uma seção sobre a leitura e informa quais campos são legíveis. Para o criativo, são os mesmos campos especificados durante a criação do objeto, além de `id`.

```
curl -G \ -d 'fields=name,object_story_id' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<CREATIVE_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/creative#)

## Posicionamentos


Um posicionamento é o local onde o anúncio aparece no Facebook, como o Feed no desktop, Feed em dispositivos móveis ou a coluna da direita. Consulte o [Guia de anúncios do Facebook](https://www.facebook.com/business/ads-guide/).


Recomendamos que você execute anúncios em todos os posicionamentos disponíveis. O leilão de anúncios do Facebook foi desenvolvido para veicular impressões de anúncios no posicionamento que tem mais chances de gerar resultados de campanhas com o menor custo possível.


A maneira mais fácil de obter vantagens dessa otimização é deixar esse campo em branco. Você também pode selecionar posicionamentos específicos em uma target_spec do conjunto de anúncios.


Este exemplo tem um anúncio de post da Página. Os posicionamentos disponíveis são Feed do celular, Feed do desktop e coluna da direita do Facebook. Na API, consulte as [opções de posicionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/#placement). Se você escolher `desktopfeed` e `rightcolumn` como `page_type`, o anúncio será veiculado nos posicionamentos da coluna da direita e do Feed do desktop. Qualquer anúncio criado abaixo deste conjunto de anúncios tem apenas o posicionamento em desktop.

```
curl -X POST \ -F 'name=Desktop Ad Set' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'daily_budget=10000' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "publisher_platforms": ["facebook","audience_network"] }' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=1000' \ -F 'status=PAUSED' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/creative#)

## Ver prévia de um anúncio


Você pode fazer a prévia de um anúncio de duas formas: com a [API de Prévia do Anúncio](https://developers.facebook.com/docs/reference/ads-api/generatepreview/) ou com o [plugin de prévia do anúncio](https://developers.facebook.com/docs/reference/ads-api/ad-preview-plugin).


Há três formas de gerar uma prévia com a API:


- Pela identificação do anúncio
- Pela identificação do criativo do anúncio
- Informando as especificações do criativo


De acordo com os documentos de [referência](https://developers.facebook.com/docs/reference/ads-api/generatepreview/#html) da API de Prévia, a chamada mínima obrigatória será a seguinte:

```
curl -G \ --data-urlencode 'creative="<CREATIVE_SPEC>"' \ -d 'ad_format="<AD_FORMAT>"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```


A especificação do criativo é uma matriz de cada campo e valor necessário para elaborar o criativo do anúncio.


No momento, nossa chamada de criativo do anúncio tem a seguinte aparência:

```
curl -X POST \ -F 'name="Sample Promoted Post"' \ -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Use `object_story_id` na chamada da API de Prévia:

```
curl -G \ -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \ -d 'ad_format=<AD_FORMAT>' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```


Os valores disponíveis para `ad_format` diferem um pouco de `page_types`. Mas, neste cenário, o Feed do desktop e a coluna da direita do Facebook são selecionados. Isso exige que você realize duas chamadas da API para gerar as prévias para cada posicionamento:

```
curl -G \ -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \ -d 'ad_format=DESKTOP_FEED_STANDARD' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```

```
curl -G \ -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \ -d 'ad_format=RIGHT_COLUMN_STANDARD' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```


A resposta será um iFrame válido por 24 horas.
[○](https://developers.facebook.com/docs/marketing-api/creative#)

## Ver mais


- [Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)
- [Anúncios de app no Facebook](https://developers.facebook.com/docs/app-ads)
- [Guia de anúncios](https://www.facebook.com/business/ads-guide)
[○](https://developers.facebook.com/docs/marketing-api/creative#)[○](https://developers.facebook.com/docs/marketing-api/creative#)Nesta Página[Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/creative#criativo-do-an-ncio)[Criativo](https://developers.facebook.com/docs/marketing-api/creative#criativo)[Limites](https://developers.facebook.com/docs/marketing-api/creative#limits)[Ler](https://developers.facebook.com/docs/marketing-api/creative#read)[Posicionamentos](https://developers.facebook.com/docs/marketing-api/creative#placements)[Ver prévia de um anúncio](https://developers.facebook.com/docs/marketing-api/creative#previews)[Ver mais](https://developers.facebook.com/docs/marketing-api/creative#ver-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5F9h25vgta9fylRxJvQQSGANN8XrLc5V9Zm5zhTu2wPGd00HbReisI0fzkww_aem_s-bWwWKiVx3Bz3foueDwvw&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ASRrJDYmvD1M7UyoAml85NgZjhzkidU9F6AzX13fhBRp2FFjv_sI6ZZp27w_aem_GPm4_IqKFcwVAQyIN6ywgQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ABMtqrO6IrFz3ivl9J9Lz3uJCt1MiIC7gxnbgmWdfH1bkYc232GseoYDfjw_aem_jGYVWdUEqVePnWftAqEGLQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5POWb9akSTNJ43HApOp4JgSz0HN2KyOI0JAq72mHLvpdHF71mx8BH-cG6Y_A_aem_8Rxf5vBzX6UvUvf9fqxY1Q&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UxGVH4cpnD9eYZ9XpPjmPQeWn44AuBJfblQrSBNvduIqLHU1ynqebP46P3g_aem_MxcnDYYwp5ONaTEZXDTJfA&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ASRrJDYmvD1M7UyoAml85NgZjhzkidU9F6AzX13fhBRp2FFjv_sI6ZZp27w_aem_GPm4_IqKFcwVAQyIN6ywgQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UxGVH4cpnD9eYZ9XpPjmPQeWn44AuBJfblQrSBNvduIqLHU1ynqebP46P3g_aem_MxcnDYYwp5ONaTEZXDTJfA&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR761LtPm9ou42wM3ZQbT6ksUJ3cFSw9pFPX7cQfL36qMl8AU4UFsuMRGOTFtg_aem_yth8co_M5G3FtbpR3qHnCg&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR41jXc1EdMqBbFnt9lmY546TUO0ZDFRQdNlamy825Z_1AYfN-ZRrzuOHZvjyw_aem_LzwvCmbZVMcjMtiBlyVFMQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ABMtqrO6IrFz3ivl9J9Lz3uJCt1MiIC7gxnbgmWdfH1bkYc232GseoYDfjw_aem_jGYVWdUEqVePnWftAqEGLQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UxGVH4cpnD9eYZ9XpPjmPQeWn44AuBJfblQrSBNvduIqLHU1ynqebP46P3g_aem_MxcnDYYwp5ONaTEZXDTJfA&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62iEhg0rdW1y8V-9mbE2AhIzqejfBJGsjYjLQprfDzbfXXbKK78zMusfzA2w_aem_eIk9xCAW2VrnGzfBkCpFPg&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ASRrJDYmvD1M7UyoAml85NgZjhzkidU9F6AzX13fhBRp2FFjv_sI6ZZp27w_aem_GPm4_IqKFcwVAQyIN6ywgQ&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hI6n62pwk9R0IrJ4ULi8JqlS-86CRFkoQu6rK1AbGyXY1sbYvR05kldpGDQ_aem_MRf12zJDdHMcBUeDVFFG9g&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5F9h25vgta9fylRxJvQQSGANN8XrLc5V9Zm5zhTu2wPGd00HbReisI0fzkww_aem_s-bWwWKiVx3Bz3foueDwvw&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5POWb9akSTNJ43HApOp4JgSz0HN2KyOI0JAq72mHLvpdHF71mx8BH-cG6Y_A_aem_8Rxf5vBzX6UvUvf9fqxY1Q&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hI6n62pwk9R0IrJ4ULi8JqlS-86CRFkoQu6rK1AbGyXY1sbYvR05kldpGDQ_aem_MRf12zJDdHMcBUeDVFFG9g&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hI6n62pwk9R0IrJ4ULi8JqlS-86CRFkoQu6rK1AbGyXY1sbYvR05kldpGDQ_aem_MRf12zJDdHMcBUeDVFFG9g&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62iEhg0rdW1y8V-9mbE2AhIzqejfBJGsjYjLQprfDzbfXXbKK78zMusfzA2w_aem_eIk9xCAW2VrnGzfBkCpFPg&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5POWb9akSTNJ43HApOp4JgSz0HN2KyOI0JAq72mHLvpdHF71mx8BH-cG6Y_A_aem_8Rxf5vBzX6UvUvf9fqxY1Q&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT606gVJ_lOi2pqdc03v60QdmnrPGSdQP-qD9c1W-y3wPz-2uO5GG2FFHjgB0Nl92DA8pdt5OvidXfjzSwfwXe4ENjHrdUlPT70yARIQDG0faI9RtqotS5M9ulQaGV2mCHRzaShDQVQ-opjXsygE25URxXw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão