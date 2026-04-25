<!-- Fonte: Introdução ao criativo Advantage+  - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Introdução ao criativo Advantage+


Este guia cobre a geração de anúncios e criativos com recursos do criativo Advantage+ habilitados.


Anteriormente, o criativo Advantage+ só estava disponível por meio dos aprimoramentos padrão, um pacote de recursos do criativo Advantage+. Na versão 22.0 da API de Marketing e em todas as versões subsequentes, a funcionalidade de aceitação e prévia dos aprimoramentos padrão ficará obsoleta. Em vez disso, você poderá habilitar ou visualizar recursos individuais do criativo Advantage+ seguindo as diretrizes descritas neste documento.


## Antes de começar


Configure suas campanhas de anúncios seguindo estas instruções:


- [Criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-campaign)
- [Criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-set)
[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)

## Etapa 1: fornecer um anúncio ou um criativo com os recursos do criativo Advantage+ habilitados


[Crie um anúncio](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad) usando o [ponto de extremidade `/ads`](https://developers.facebook.com/docs/marketing-api/reference/adgroup) ou [gere um criativo independente](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) por meio do ponto de extremidade [`/adcreatives`](https://developers.facebook.com/docs/marketing-api/reference/ad-creative). Em qualquer abordagem, especifique os recursos a serem habilitados no parâmetro `creative_features_spec`.


### Exemplo de solicitação


Para implementar os recursos de habilitação `image_touchups`, `inline_comment` e `image_templates`:

```
// creative example curl -X POST \ -F 'name=Advantage+ Creative Creative' \ -F 'degrees_of_freedom_spec={ "creative_features_spec": { "image_touchups": { "enroll_status": "OPT_IN" }, "inline_comment": { "enroll_status": "OPT_IN" }, "image_template": { "enroll_status": "OPT_IN" } } }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives // ad example curl -X POST \ -F 'adset_id=<ADSET_ID>' \ -F 'creative={ "name": "Advantage+ Creative Adgroup", "object_story_spec": { "link_data": { "image_hash": "<IMAGE_HASH>", "link": "<URL>", "message": "You got this.", }, "page_id": "<PAGE_ID>" }, "degrees_of_freedom_spec": { "creative_features_spec": { "image_touchups": { "enroll_status": "OPT_IN" }, "inline_comment": { "enroll_status": "OPT_IN" }, "image_template": { "enroll_status": "OPT_IN" } } } }' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Recursos


Confira os recursos de habilitação do criativo Advantage+ que podem ser implementados no parâmetro `creative_features_spec`.


| Nome | Descrição |
| --- | --- |
| adapt_to_placement | Opcional. O padrão é ativar. Habilite se quiser ajustar automaticamente as imagens aos posicionamentos com base no que é previsto para funcionar melhor. Por padrão, os posicionamentos 4:5 e 9:16 são habilitados. Se quiser controlar como as imagens são ajustadas, use o campo customizations para definir as configurações. Para saber mais, consulte os campos aspect_ratio_config e image_crop_style na documentação de referência Personalizações de recursos do criativo do anúncio . O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como **Retoques de imagem* no Gerenciador de Anúncios. |
| add_text_overlay | Opcional. Habilite se quiser adicionar informações de itens do catálogo como sobreposições visualmente únicas. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Adicionar sobreposições dinâmicas no Gerenciador de Anúncios. Se você quiser controlar a forma como a sobreposição é renderizada, consulte Ad Creative Link Data Image Layer Spec para saber mais. |
| creative_stickers | Opcional. Ative se quiser adicionar figurinhas geradas por IA para contar melhor sua história e deixar as chamadas para ação mais claras. Incluiremos figurinhas de CTA de forma automática no local com probabilidade de gerar melhor desempenho. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Criar chamada para ação de figurinha no Gerenciador de Anúncios. |
| description_automation | Opcional. Habilite em anúncios de catálogo Advantage+ se quiser que as informações dos itens do seu catálogo sejam usadas na descrição do anúncio com base na probabilidade de interação de cada pessoa que visualiza a publicidade. Habilite em anúncios em carrossel estáticos se quiser que a descrição do seu carrossel seja escolhida dinamicamente quando for exibida. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Descrição dinâmica no Gerenciador de Anúncios. |
| enhance_cta | Opcional. Habilite se quiser que as frases relevantes das suas fontes de anúncios sejam alinhadas com sua CTA. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . O campo customizations pode ser definido abaixo para usar frases de alto desempenho em potencial identificadas pela IA : { "text_extraction": { "enroll_status": "OPT_IN" } Observação: este recurso aparece como Aprimorar CTA no Gerenciador de Anúncios. |
| image_background_gen | Opcional. Habilite se quiser criar planos de fundo diferentes para imagens de produtos qualificados e veicular a versão com maior probabilidade de repercutir no seu público. Este recurso é gerado por IA. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Gerar planos de fundo no Gerenciador de Anúncios. |
| image_brightness_and_contrast | Opcional. Habilite se quiser que o brilho e o contraste da sua imagem sejam ajustados quando houver probabilidade de melhorar o desempenho. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Ajustar brilho e contraste no Gerenciador de Anúncios. |
| image_templates | Opcional. Habilite se quiser adicionar sobreposições que mostrem o texto fornecido com o criativo do anúncio selecionado quando houver probabilidade de melhorar o desempenho. Este recurso é gerado por IA. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Adicionar sobreposições no Gerenciador de Anúncios. |
| image_touchups | Opcional. Habilite se quiser que a mídia escolhida seja automaticamente cortada e expandida para caber em mais posicionamentos. Aplicável apenas a anúncios de imagem. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Retoques visuais no Gerenciador de Anúncios. |
| image_uncrop | Opcional. Habilite se quiser que a imagem seja expandida automaticamente para caber em mais posicionamentos. Este recurso é gerado por IA. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Expandir imagem no Gerenciador de Anúncios. |
| inline_comment | Opcional. Habilite se quiser que o comentário mais relevante seja exibido abaixo do seu anúncio no Facebook e no Instagram. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Comentários relevantes no Gerenciador de Anúncios. |
| media_type_automation | Opcional. Habilite se quiser que os vídeos do seu catálogo sejam exibidos (com imagens) em posicionamentos compatíveis. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Mídia dinâmica no Gerenciador de Anúncios. Consulte Mídia dinâmica para saber mais. |
| pac_relaxation | Opcional. Habilite se quiser mostrar a mídia escolhida para uma taxa de proporção específica em todos os posicionamentos quando houver probabilidade de melhorar o desempenho. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Mídia flex ou Mídia flexível no Gerenciador de Anúncios. |
| product_extensions | Opcional. Habilite se quiser que itens do seu catálogo sejam exibidos ao lado da mídia selecionada quando houver probabilidade de melhorar o desempenho. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso é chamado de Mostrar produtos no menu suspenso Coleção, em opções de exibição de formato no Gerenciador de Anúncios. Consulte Recursos de extensões de produto (Adicionar itens do catálogo) na API de Marketing para saber mais. |
| reveal_details_over_time | Opcional. Ative se quiser que as informações do seu site ou da página de produtos na loja de apps sejam reveladas quando as pessoas passarem alguns segundos olhando para o anúncio. Isso pode ajudar as pessoas a se sentirem mais seguras antes de clicarem na sua chamada para ação. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Revelar detalhes com o tempo no Gerenciador de Anúncios. |
| text_optimizations | Opcional. Habilite se quiser que as opções de texto fornecidas por você apareçam como texto principal, título ou descrição quando houver probabilidade de melhorar o desempenho. Podemos adicionar uma introdução de legenda às suas opções de título e destacar frases relevantes quando houver probabilidade de melhorar o desempenho. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . O campo customizations pode ser definido abaixo para usar frases de alto desempenho em potencial identificadas pela IA : { "text_extraction": { "enroll_status": "OPT_IN" } Observação: este recurso aparece como Melhorias no texto no Gerenciador de Anúncios. |
| text_translation | Opcional. Habilite se quiser que o anúncio seja traduzido para diferentes idiomas no Facebook e no Instagram. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Traduzir texto no Gerenciador de Anúncios. |
| video_auto_crop | Opcional. Habilite se quiser que a mídia escolhida seja automaticamente cortada e expandida para caber em mais posicionamentos. Aplicável apenas a anúncios em vídeo. O campo enroll_status pode ser definido como OPT_IN ou OPT_OUT . Observação: este recurso aparece como Retoques visuais no Gerenciador de Anúncios. |


Os recursos especificados como `OPT_IN` que não forem qualificados para a configuração de anúncio fornecida serão automaticamente removidos do parâmetro `creative_features_spec`. Por exemplo, `image_templates` (ou **Adicionar sobreposições**) não pode ser aplicado a criativos em formato de vídeo. Se você habilitar esse recurso em um anúncio em vídeo, ele será removido automaticamente por não estar qualificado.


Se quiser confirmar a configuração final, use uma solicitação `GET` para recuperar o parâmetro `creative_features_spec`.


Não se preocupe se você vir `standard_enhancements` ou qualquer sub-recursos dos aprimoramentos padrão anexados a `creative_features_spec` ao fazer a recuperação. Enquanto não estiverem definidos como `OPT_IN`, eles não serão aplicados. O processo para tornar os aprimoramentos padrão obsoletos está em progresso, e eliminaremos esse comportamento gradualmente quando a descontinuação for concluída.


A maioria dos recursos do criativo Advantage+ pode ser habilitada usando o parâmetro `creative_features_spec`, com exceção do recurso `music`, que é implementado com o parâmetro `asset_feed_spec`. Para desativar o recurso `music`, passe o parâmetro `assest_feed_spec.audios` como vazio.


#### Exemplo de solicitação


Para habilitar o recurso `music` usando o parâmetro `asset_feed_spec`:

```
curl -X POST \ -F 'name="Advantage+ Creative Music"' \ -F 'object_story_spec={ "page_id": "<PAGE_ID>" }' \ -F 'asset_feed_spec={ "audios": [ { "type": "random" } ] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Se as funcionalidades habilitadas incluírem recursos gerados por IA, você deverá criar o anúncio com o status `PAUSED` e seguir as etapas 2 e 3 abaixo para concluir o processo de publicação. Se nenhum recurso gerado por IA for incluído, as etapas 2 e 3 serão opcionais. Assim, você poderá criar o anúncio com o status `ACTIVE`.


**Observação:** ao criar um anúncio por meio do ponto de extremidade `/ads`, o campo `status` será definido como `PAUSED` por padrão.
[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)

## Etapa 2: ver uma prévia do criativo Advantage+


Consulte a [referência sobre prévia do anúncio](https://developers.facebook.com/docs/marketing-api/generatepreview) para saber mais sobre essa funcionalidade.


Para ver uma prévia de um recurso do criativo Advantage+, adicione o parâmetro `creative_feature` ao seu pedido de prévia existente, com o nome do recurso desejado especificado.


Recursos compatíveis com a geração de prévias: `image_templates`, `image_touchups`, `video_auto_crop`, `enhance_cta`, `text_optimizations`, `image_background_gen`, `image_uncrop` e `description_automation`.


#### Exemplo de solicitação


```
curl -X GET -G \ -d 'ad_format="DESKTOP_FEED_STANDARD"' \ -d 'creative_feature=<FEATURE_NAME> \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>/previews
```


#### Exemplo de resposta


```
{ "data": [ { "body": "<iframe src='<PREVIEW_URL>'></iframe>", "transformation_spec": { "<FEATURE_NAME>": [ { "body": "<iframe src='<PREVIEW_URL>'></iframe>", "status": "eligible" } ] } } ] }
```


Clique no URL retornado para ver as prévias.


**Observação:** se um objeto `transformation_spec` não for retornado, isso significa que o criativo não está qualificado para o recurso do criativo Advantage+ no posicionamento escolhido e, portanto, o recurso não será aplicado.


Depois que você analisar as prévias e considerá-las prontas ​​para publicação, defina o anúncio como `ACTIVE`, caso ainda não tenha feito isso. Se alguma das prévias não for aceitável, gere um novo anúncio ou criativo sem habilitar os recursos correspondentes.
[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)

## Etapa 3: definir o status do anúncio como `ACTIVE`


Quando seu anúncio estiver pronto, defina o status dele como `ACTIVE`.


#### Exemplo de solicitação


```
curl -X POST \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)

## Saiba mais


Outros recursos do criativo Advantage+:


- [Criativo Advantage+ para catálogo:](https://developers.facebook.com/docs/marketing-api/advantage-creative-for-catalog)`adapt_to_placement` e `media_type_automation`
- [Recursos de extensões de produto (Adicionar itens do catálogo) na API de Marketing:](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions)`product_extensions`
- [Comece a usar os recursos de IA generativa na API de Marketing:](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features) text_generation, `image_background_gen` e `image_uncrop`


Outros recursos para criativos de anúncios:


- [Ad Creative Degrees Of Freedom Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-degrees-of-freedom-spec/)
- [Ad Creative Features Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-features-spec/)
- [Ad Creative Feature Details](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-feature-details/)
- [Ad Creative Object Story Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/)
- [Ad Creative Asset Feed Spec](https://developers.facebook.com/docs/marketing-api/ad-creative/asset-feed-spec/)


Anteriormente, o criativo Advantage+ estava disponível como aprimoramentos padrão:


- [Aprimoramentos padrão no criativo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements/)
- [API de Prévia para criativos Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/creative-preview)
[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)[○](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#)Nesta Página[Introdução ao criativo Advantage+](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#introdu--o-ao-criativo-advantage-)[Antes de começar](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#antes-de-come-ar)[Etapa 1: fornecer um anúncio ou um criativo com os recursos do criativo Advantage+ habilitados](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#etapa-1--fornecer-um-an-ncio-ou-um-criativo-com-os-recursos-do-criativo-advantage--habilitados)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#exemplo-de-solicita--o)[Recursos](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#recursos)[Etapa 2: ver uma prévia do criativo Advantage+](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#etapa-2--ver-uma-pr-via-do-criativo-advantage-)[Etapa 3: definir o status do anúncio como ACTIVE](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#etapa-3--definir-o-status-do-an-ncio-como-active)[Saiba mais](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ivQyRo5-tLdZA7AVPx_TcVfvt0rK2k2qvbv_CZb1txFrRTOPZCI1IdtZnnQ_aem__EHt2kXRG3kZZ9t0CELrCg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR44FGVu6FpBSTQMvLd_MCwj1WiKrsHFtBe25UKEzIEHgd5XfKfyMeBY9RLo8g_aem_rpqOBMwzr-03h1Y0kLoUbg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4y6Pv0xYrosFobTmaW-QOGeEp_mYSFGSLIiFegWplOhfl86_xffzP7S6qYQQ_aem_CIVbU12H25fA6Ymy2GDy0w&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ivQyRo5-tLdZA7AVPx_TcVfvt0rK2k2qvbv_CZb1txFrRTOPZCI1IdtZnnQ_aem__EHt2kXRG3kZZ9t0CELrCg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wT0qEOc628cN7-qMMqNUzFdVLJ0v93bZ4qrJYlHCp_YYzj6IwIPkr1cH-FQ_aem_KozUFor00_w3iQQ_N65yTg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7C50_7s4ve2fAx6BD4KRO48y8NfnMYr3S9p1hIUbScvSAiKPVl081IMKdKSQ_aem_KYSeDx02zkqv650WVYUFsA&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ivQyRo5-tLdZA7AVPx_TcVfvt0rK2k2qvbv_CZb1txFrRTOPZCI1IdtZnnQ_aem__EHt2kXRG3kZZ9t0CELrCg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45aVa_3T29Qa3TigAaiVjUkl2elFgWycXnAtTWCOu_lSMwnSDfql25gj1q2g_aem_KOgJ8RHmmkuX5Qsbejj_Mg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xONMuy-GB5FFTxKA3lCdEq-fi81rjuA5GRpnOSc8O6GtXQtKAKtZV3zHpfQ_aem_S6WXBWFTsSRiymK_ECFAtg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wT0qEOc628cN7-qMMqNUzFdVLJ0v93bZ4qrJYlHCp_YYzj6IwIPkr1cH-FQ_aem_KozUFor00_w3iQQ_N65yTg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5qhDIZYrDHIXFnFYygEcTNgv4yvwAZl5PGRtq_9YHLsGwEDrJ_czjY4B4BtA_aem_WxNIjBb-Wh8dDlJwxoisMg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7C50_7s4ve2fAx6BD4KRO48y8NfnMYr3S9p1hIUbScvSAiKPVl081IMKdKSQ_aem_KYSeDx02zkqv650WVYUFsA&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45aVa_3T29Qa3TigAaiVjUkl2elFgWycXnAtTWCOu_lSMwnSDfql25gj1q2g_aem_KOgJ8RHmmkuX5Qsbejj_Mg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4y6Pv0xYrosFobTmaW-QOGeEp_mYSFGSLIiFegWplOhfl86_xffzP7S6qYQQ_aem_CIVbU12H25fA6Ymy2GDy0w&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45aVa_3T29Qa3TigAaiVjUkl2elFgWycXnAtTWCOu_lSMwnSDfql25gj1q2g_aem_KOgJ8RHmmkuX5Qsbejj_Mg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7C50_7s4ve2fAx6BD4KRO48y8NfnMYr3S9p1hIUbScvSAiKPVl081IMKdKSQ_aem_KYSeDx02zkqv650WVYUFsA&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xONMuy-GB5FFTxKA3lCdEq-fi81rjuA5GRpnOSc8O6GtXQtKAKtZV3zHpfQ_aem_S6WXBWFTsSRiymK_ECFAtg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xONMuy-GB5FFTxKA3lCdEq-fi81rjuA5GRpnOSc8O6GtXQtKAKtZV3zHpfQ_aem_S6WXBWFTsSRiymK_ECFAtg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xONMuy-GB5FFTxKA3lCdEq-fi81rjuA5GRpnOSc8O6GtXQtKAKtZV3zHpfQ_aem_S6WXBWFTsSRiymK_ECFAtg&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5mdqVbnywSQdUpzyDzdU8d9iQ1zqXkBXxFqQ9yV_dqOWOupzFx9QCfbvQ4OA_aem_StoOh2RmRFSTbc2ytACXhA&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5vRyVcdWup5zERmTCWj4FRolsoULxZFtsjSNk5vehuuv9K44mkAsMfSnUxrH3RRBatbWTmrntabTqGPoxHvuu3245I5_8L7uzZ7QKspEPOAY9r48-gmG_sIHcTzZxcD79kg3jOudQyyDGF63i-3BRisaQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão