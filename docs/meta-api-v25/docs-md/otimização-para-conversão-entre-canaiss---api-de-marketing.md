<!-- Fonte: Otimização para conversão entre canaiss - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/ccco -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Otimização para conversão entre canais


A otimização para conversão entre canais permite otimizar conversões tanto para o site quanto para o app dentro de uma única campanha. Selecionar um site e app como os locais onde você deseja que as conversões ocorram captura mais dados, o que pode ajudar a diminuir o custo por ação (CPA, pelas iniciais em inglês) e levar a um aumento nas conversões.


Aqui estão os principais motivadores de valor que repercutem com anunciantes:


- Simplicidade: em vez de gerenciar várias campanhas, otimize para site e app em uma única campanha
- Mais conversões: com mais dados capturados, as chances de exibir anúncios para pessoas que farão conversões aumentam
- Economia: atinja o maior número de pessoas a um custo menor


## Primeiros passos


A otimização para conversão entre canais melhora as conversões tanto para o site quanto para o app (iOS + Android) em uma única campanha. Se uma impressão levar a uma conversão no site ou uma conversão no app, ou ambas, o produto contará todas as conversões como eventos otimizados.


### Restrições


#### Objetivo


A otimização para conversão entre canais aceita somente o objetivo `CONVERSIONS`.


#### Eventos


A otimização para conversão entre canais aceita os seguintes eventos:


- `PURCHASE`
- `COMPLETE_REGISTRATION`
- `ADD_PAYMENT_INFO`
- `ADD_TO_CART`
- `INITIATED_CHECKOUT`
- `SEARCH`
- `CONTENT_VIEW`
- `LEAD`
- `ADD_TO_WISHLIST`
- `SUBSCRIBE 1`
- `START_TRIAL 1`


#### Estratégia de lance


Com ou sem otimização de orçamento de campanha (CBO, pelas iniciais em inglês), a otimização para conversão entre canais aceita somente estas estratégias de lance:


- `LOWEST_COST_WITHOUT_CAP`
- `LOWEST_COST_WITH_BID_CAP`


#### Posicionamentos


A otimização para conversão entre canais está disponível para todos os posicionamentos do Instagram e do Facebook, incluindo posicionamentos automáticos. **Exceções**: Audience Network, Messenger, Facebook Instant Articles e Personalização de ativo de posicionamento.


`SUBSCRIBE` e `START_TRIAL` estão sendo considerados atualmente.
[○](https://developers.facebook.com/docs/ccco#)

## Conjunto de anúncios


Otimize a veiculação dos seus anúncios com base em uma meta de conversões fora do site, como `OFFSITE_CONVERSIONS`, se você configurar seu pixel para enviar conversões fora do site.


Para usar a otimização para conversão entre canais, defina os seguintes campos com seus respectivos valores:


- Meta de otimização > Defina para `OFFSITE_CONVERSIONS`.
- Estratégia de lance > Consulte Estratégia de lance.
- Evento de cobrança > Defina para `IMPRESSIONS`.


### Objeto omnichannel


Incluímos o novo campo `omnichannel_object` no [Ad Set](https://developers.facebook.com/docs/marketing-api/reference/ad-promoted-object/).


Para validação de objeto omnicanal:


- Todos os campos `custom_event_type` no app e pixel devem ser do mesmo evento.
- Tanto o SDK do app quanto o pixel são obrigatórios.
- As contas de anúncio atuais devem ter acesso a todos os objetos promovidos por apps e pixels.


| Campo | Tipo | Descrição |
| --- | --- | --- |
| app | list\<AppPromotedObject\> | Objetos promovidos por apps associados a este objeto omnicanal. application_id — Tipo: string. ID de app sendo promovido.; object_store_urls — Tipo: list\<string\> . Lista de URLs da loja de objetos associadas a application_id (Loja do Google Play e/ou iTunes).; custom_event_type — Tipo: Enumeração de evento O evento que será otimizado. Para validação de objeto promovido por app: Todas as object_store_urls devem ser associadas a esse app. É possível configurar isso em developers.facebook.com nas configurações do app.; O custom_event_type deve ser um destes eventos compatíveis. |
| pixel | list\<PixelPromotedObject\> | Objetos promovidos por pixels associados a este objeto omnicanal. pixel_id – Tipo: string. O ID de pixel sendo promovido.; pixel_rule – Tipo: JSON. Opcional. Regra de conversão personalizada de pixels.; custom_event_type — Tipo: Enumeração de evento O evento que será otimizado. Para validação de objeto promovido por app, o custom_event_type deve ser um destes eventos compatíveis. |


#### Exemplo


```
{
     daily_budget: 20000,
     optimization_goal: CONVERSIONS,
     promoted_object: {
         omnichannel_object: {
             app: [
                 {
                     application_id: ,
                     custom_event_type: PURCHASE,
                     object_store_urls: [
                         "https://play.google.com/store/apps/details?id=com.facebook.ka"
                         "https://apps.apple.com/us/app/facebook/id284882215",
                     ],
                 },
             ],
             pixel:  [
                 {
                     pixel_id,
                     custom_event_type: PURCHASE
                 },
             ],
         }
     }
}
```
[○](https://developers.facebook.com/docs/ccco#)

## Anúncio


Você pode selecionar o destino desejado onde os anunciantes desejam que os usuários aterrissem quando clicarem no seu anúncio — desde um desktop ou app. Os anunciantes devem inserir os links correspondentes — site, deep link do app iOS ou deep link do app Android, dada a opção de destino escolhida. Saiba mais sobre [deep links de produtos](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-deep-links).


| Campo | Tipo | Descrição |
| --- | --- | --- |
| creative | Especificação do criativo | Obrigatório para criar . O ID ou a especificação do criativo do criativo do anúncio deve ser usado por esse anúncio. Saiba mais sobre criativos de anúncio . {"creative_id": } ou especificação do criativo conforme a seguir: { "creative" : { "name" : "" , "applink_treatment" : "" "object_story_spec" : , "omnichannel_link_spec" : } } |
| tracking_specs | Lista de especificações de rastreamento | Especificação de rastreamento necessária para o rastreamento de conversão. Para validação de anúncios, veja as especificações necessárias abaixo e os respectivos exemplos. |


Para validação de anúncio:


- O `pixel_id` da especificação de rastreamento (`tracking_specs`) e o `application_id` devem ser consistentes com aqueles no `promoted_object`.
- `tracking_specs` deve incluir estes requisitos:


| Especificação de rastreamento | Exemplo de código |
| --- | --- |
| Pixel | { "action.type" : [ "offsite_conversion" ], "fb_pixel" : [ pixel_id ] } |
| Instalação do app | { "action.type" : [ "mobile_app_install" ], "application" : [ application_id ] } |
| Evento do app | { "action.type" : [ "app_custom_event" ], "application" : [ application_id ] } |


#### Exemplo


```
{
     "name": "sample ad"
     "adset_id": "6170648652866",
     "creative": {
         "creative_id": creative_id,
    }
    "status": "PAUSED",
    "tracking_specs": [
        {
            "action.type": ["offsite_conversion"],
            "fb_pixel": [pixel_id]
        }
        {
            "action.type": ["mobile_app_install"],
            "application": [application_id]
        }
        {
            "action.type": ["app_custom_event"],
            "application": [application_id]
        }
    ]
}
```
[○](https://developers.facebook.com/docs/ccco#)

## Criativo


### Anúncios de catálogo Advantage+


Para anúncios de catálogo Advantage+, `template_url_spec` pode ser usado para especificar deep links no criativo. Nesse campo, você pode usar campos dinâmicos, como URL ou identificação do produto.


`template_url_spec` segue essa especificação.


#### Exemplo


```
{
   "creative":{
      "applink_treatment":"deeplink_with_web_fallback",
      "template_url_spec":{
         "android":{
            "url":"example://product/{{product.retailer_id | urlencode}}"
         },
         "config":{
            "app_id":"<APPLICATION_ID>"
         },
         "ios":{
            "url":"example://product/{{product.name | urlencode}}"
         },
         "web":{
            "url":"https://www.example.com/deeplink/{{product.name | urlencode}}"
         }
      }
   },
}
```


### Carregar manualmente os anúncios


Para carregar manualmente os anúncios, é preciso usar `omnichannel_link_spec` em vez `template_url_spec`. Isso inclui os campos a seguir:


| Campo | Tipo | Descrição |
| --- | --- | --- |
| web | Configuração da Web | Objetos promovidos por pixels associados a este objeto omnicanal. url – Tipo: string. O site que o usuário abre por meio do navegador. Para validação na web, a url deve ser a mesma que o link fornecido em link_data . |
| app | Configuração de destino do app | Objetos promovidos por apps associados a este objeto omnicanal. application_id — Tipo: string. O site que o usuário abre por meio do navegador. Para validação na web, application_id deve ser consistente como o application_id em omnichannel_object no promoted_object .; platform_specs – Tipo: JSON. Configuração de destino de pouso pela plataforma. |


### Especificações da plataforma


| Campo | Tipo | Descrição |
| --- | --- | --- |
| android | JSON | Configuração de pouso para app Android. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url – Tipo: string. Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| ios | JSON | Configuração de pouso para o app iOS. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url – Tipo: string. Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| ipad | JSON | Configuração de pouso para app exclusivo para iPad. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url – Tipo: string. Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| iphone | JSON | Configuração de pouso para app exclusivo para iPhone. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url – Tipo: string. Deep link para abrir o app. Saiba mais sobre deep links de produtos . |


#### Exemplo


```
{
  "applink_treatment": "deeplink_with_web_fallback",
  "omnichannel_link_spec": {
      "web": {
        "url": web_url
      },
      "app": {
        "application_id": application_id,
        "platform_specs": {
          "android": {
            "url": android_deeplink
          },
          "ios": {
            "url": ios_deeplink
          }
        }
      }
   },
  "object_story_spec": {
    "instagram_user_id": "<IG_USER_ID>",
    "page_id": "",
    "link_data": {
      "call_to_action": {
        "type": "LEARN_MORE",
      },
      "link": web_url,
      "message": "Purchase now!",
      "name": "Sample creative"
    }
  },
  "object_type": "SHARE"
}
```
[○](https://developers.facebook.com/docs/ccco#)[○](https://developers.facebook.com/docs/ccco#)Nesta Página[Otimização para conversão entre canais](https://developers.facebook.com/docs/ccco#otimiza--o-para-convers-o-entre-canais)[Primeiros passos](https://developers.facebook.com/docs/ccco#primeiros-passos)[Restrições](https://developers.facebook.com/docs/ccco#restri--es)[Conjunto de anúncios](https://developers.facebook.com/docs/ccco#conjunto-de-an-ncios)[Objeto omnichannel](https://developers.facebook.com/docs/ccco#objeto-omnichannel)[Anúncio](https://developers.facebook.com/docs/ccco#an-ncio)[Criativo](https://developers.facebook.com/docs/ccco#criativo)[Anúncios de catálogo Advantage+](https://developers.facebook.com/docs/ccco#an-ncios-de-cat-logo-advantage-)[Carregar manualmente os anúncios](https://developers.facebook.com/docs/ccco#carregar-manualmente-os-an-ncios)[Especificações da plataforma](https://developers.facebook.com/docs/ccco#especifica--es-da-plataforma) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HC7_e1qY7ZNKTX2pgBYofJQF9wrvUbInlbXNYsr63avnUfz43UuNnwWdZOQ_aem_zPQYDNJWPpCfUONQbuMUnw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4gB6cq7quc2pAUfi5E6QOhETrvIRSlz_OxIvmTxVSayotyFw48NskGb673hg_aem_ts3caXiTOT5SZ5tEK7L9JA&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4gB6cq7quc2pAUfi5E6QOhETrvIRSlz_OxIvmTxVSayotyFw48NskGb673hg_aem_ts3caXiTOT5SZ5tEK7L9JA&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ehkt-dWHTvJktA0oQMp65ezfDsSk-WxVk6eJ1sBklGlGEXNeMAUYJJUml3w_aem_-ggVCYxsHZmwv4AdtwbpRQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-ZlMdtHtZpKee9VV_bLXIEp_mB-1IvbXS0IM0bW1w2ohbZFsl3KfkE6EUhw_aem_F96jJeNfV_NKEQwHJh0ntQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HC7_e1qY7ZNKTX2pgBYofJQF9wrvUbInlbXNYsr63avnUfz43UuNnwWdZOQ_aem_zPQYDNJWPpCfUONQbuMUnw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ehkt-dWHTvJktA0oQMp65ezfDsSk-WxVk6eJ1sBklGlGEXNeMAUYJJUml3w_aem_-ggVCYxsHZmwv4AdtwbpRQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HXd5dkjOj5jGUjRRgw59Sy2VZbXTQOU0hcIAfMbPPQUlnfCx5Tsuoqt_dYg_aem_a1FXGeHIYijpcG7k03aG6w&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HC7_e1qY7ZNKTX2pgBYofJQF9wrvUbInlbXNYsr63avnUfz43UuNnwWdZOQ_aem_zPQYDNJWPpCfUONQbuMUnw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ETUo7qW2mWnyuoliFDp9sBlhnLZHT0L61JPjkkttbfmKuKWr5bGD4nbQdyw_aem_ODO_LazAJLmRZ29yhi9HIg&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5qlsm_I1LaGK7EbqnZg--UxBNShobUFFUZzoaXnAX9znvrYFxX_oybataUHw_aem_967DYWRhf6U7yeyMPraJUw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-ZlMdtHtZpKee9VV_bLXIEp_mB-1IvbXS0IM0bW1w2ohbZFsl3KfkE6EUhw_aem_F96jJeNfV_NKEQwHJh0ntQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ehkt-dWHTvJktA0oQMp65ezfDsSk-WxVk6eJ1sBklGlGEXNeMAUYJJUml3w_aem_-ggVCYxsHZmwv4AdtwbpRQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-ZlMdtHtZpKee9VV_bLXIEp_mB-1IvbXS0IM0bW1w2ohbZFsl3KfkE6EUhw_aem_F96jJeNfV_NKEQwHJh0ntQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ehkt-dWHTvJktA0oQMp65ezfDsSk-WxVk6eJ1sBklGlGEXNeMAUYJJUml3w_aem_-ggVCYxsHZmwv4AdtwbpRQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7LgCT3JDPWcJZxw-4anr2LmqehcXL16sfdpJzHPFqd5dhb75TowkRN01M4jg_aem_iC7SuBTo_zlxHeJURn1Oxw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-ZlMdtHtZpKee9VV_bLXIEp_mB-1IvbXS0IM0bW1w2ohbZFsl3KfkE6EUhw_aem_F96jJeNfV_NKEQwHJh0ntQ&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ETUo7qW2mWnyuoliFDp9sBlhnLZHT0L61JPjkkttbfmKuKWr5bGD4nbQdyw_aem_ODO_LazAJLmRZ29yhi9HIg&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56BXL4hBkA0cQXwQNO5MHNgyM4DnsHI3-HEhHVO1L_EgUt2H5MFYs5zmNDBg_aem_8Qd2IP3PbvbvHd1dXqTc4Q&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR562VxmHOncHxfCwSqOxVOFRKYhtO8yiAoyWhhYBKJeHN3DqqDOFNjpa9_hpA_aem_K6Dap8R1VcM1rUDSsX9FNw&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT45vtwMGYNicIZNV9uF5pLBzmDjT19QEty0-lowMCAxIg3UbmrXI5PNvFMQVQ91kWmyk_8Xv0x7LdPLbHavhF8o65vKHlpGBxE47m6MR3-n5gCprPd1oFPElwNCjn5T0peC_aNWWXCh5eDLr-9UfetEzRY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão