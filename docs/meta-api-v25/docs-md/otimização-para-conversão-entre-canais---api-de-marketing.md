<!-- Fonte: Otimização para conversão entre canais - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Otimização para conversão entre canais em campanhas de compras Advantage+


A otimização para conversão entre canais permite otimizar conversões tanto para o site quanto para o app em uma única campanha. Selecionar um site e app como os locais onde você deseja que as conversões ocorram captura mais dados, o que pode ajudar a diminuir o custo por ação (CPA, pelas iniciais em inglês) e levar a um aumento nas conversões.


Não há alterações no nível da campanha. Há alterações no nível do conjunto de anúncios e do anúncio.


## Conjunto de anúncios


No nível do conjunto de anúncios, você precisa especificar as informações do app em `promoted_object`. Para fazer isso, use e coloque `omnichannel_object` sob `promoted_object`.


Para validação de objeto omnicanal:


- Todos os campos `custom_event_type` no app e no pixel devem ter o mesmo evento.
- Tanto o SDK do app quanto o pixel são obrigatórios.
- As contas de anúncio atuais devem ter acesso a todos os objetos promovidos por apps e pixels.


Também é possível criar anúncios das Lojas com as campanhas de compras Advantage+ definindo o `destination_type` como `SHOP_AUTOMATIC` no nível do conjunto de anúncios e especificando a identificação da conta comercial (`commerce_merchant_settings_id`) no `omnichannel_object` sob `promoted_object`.


| Campo | Descrição |
| --- | --- |
| app list\<AppPromotedObject\> | Objetos promovidos por apps associados a este objeto omnicanal. application_id string ID do app sendo promovido. object_store_urls List\<string\> Lista de URLs da loja de objetos associadas a application_id (Loja do Google Play e/ou iTunes). custom_event_type : o conjunto de anúncios de compras Advantage+ é compatível com os eventos PURCHASE , ADD_TO_CART , INITIATED_CHECKOUT , ADD_PAYMENT_INFO , ADD_TO_WISHLIST , CONTENT_VIEW , COMPLETE_REGISTRATION , START_TRIAL , SUBSCRIBE e SEARCH . Para validação de objeto promovido por app: Todos os object_store_urls devem ser associados ao application_id do app. É possível configurar isso em developers.facebook.com nas configurações do app. custom_event_type : o conjunto de anúncios de compras Advantage+ é compatível com os eventos PURCHASE , ADD_TO_CART , INITIATED_CHECKOUT , ADD_PAYMENT_INFO , ADD_TO_WISHLIST , CONTENT_VIEW , COMPLETE_REGISTRATION , START_TRIAL , SUBSCRIBE e SEARCH . |
| pixel list\<PixelPromotedObject\> | Objetos promovidos por pixels associados a este objeto omnicanal. pixel_id string O ID de pixel sendo promovido. custom_event_type : o conjunto de anúncios de compras Advantage+ é compatível com os eventos PURCHASE , ADD_TO_CART , INITIATED_CHECKOUT , ADD_PAYMENT_INFO , ADD_TO_WISHLIST , CONTENT_VIEW , COMPLETE_REGISTRATION , START_TRIAL , SUBSCRIBE e SEARCH . |
| onsite list | Obrigatório para anúncios das Lojas. commerce_merchant_settings_id String Identificação da conta comercial |


#### Exemplo


```
{
     daily_budget: 20000,
     promoted_object: {
         omnichannel_object: {
             app: [
                 {
                     application_id: <application_id>,
                     custom_event_type: PURCHASE,
                     object_store_urls: [
                         "https://play.google.com/store/apps/details?id=com.facebook.ka"
                         "https://apps.apple.com/us/app/facebook/id284882215",
                     ],
                 },
             ],
             pixel:  [
                 {
                     Pixel_id: <pixel_id>,
                     custom_event_type: PURCHASE
                 },
             ],
         }
     }
}
```
[○](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#)

## Anúncio


No nível do anúncio, os anunciantes podem especificar o destino primário e secundário para enviar os usuários que clicarem nos anúncios. Por exemplo, eles podem usar um app como destino primário. Porém, se o app não estiver instalado no dispositivo, o destino secundário pode ser um site ou a loja de apps. Para configurar o destino, use `applink_treatment`. Os [anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/get-started#specify-desired-behavior-of-ads-click-from-mobile) já usam esses campos.


O `applink_treatment` tem os seguintes valores com a respectiva descrição:


| Nome | Descrição |
| --- | --- |
| web_only | Sempre envia o usuário à URL da web em questão. |
| deeplink_with_web_fallback | Se o app estiver instalado no telefone do usuário e tivermos informações de deep link correspondentes, enviaremos o usuário para o app. Se alguma dessas condições não for atendida, enviará para o site. |
| deeplink_with_appstore_fallback | É o padrão quando App Links são apresentados para o produto. Se o app estiver instalado no telefone do usuário e tivermos informações de deep link correspondentes, enviaremos o usuário para o app. Caso o app não esteja instalado, encaminha à loja de apps correspondente. |


A campanha de compras Advantage+ não é compatível com o modo `automatic`.


Também há opções para especificar deep links nos apps ou nos destinos de sites. Saiba mais sobre [deep links de produtos](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-deep-links).


O modo para especificar deep links é diferente em anúncios de catálogos e outros anúncios.


### Anúncios de catálogo


Nos anúncios de catálogo, a mesma configuração `applink_treatment` pode ser usada. Entretanto, para especificar deep links, `template_url_spec` é usado em vez de `omnichannel_link_spec`. Nesse campo, é possível usar campos dinâmicos, como URL ou identificação do produto.


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
            "app_id":"<application_id>"
         },
         "ios":{
            "url":"example://product/{{product.name | urlencode}}"
         },
         "web":{
            "url":"https://www.example.com/deeplink/{{product.name | urlencode}}"
         }
      }
   },
   "tracking_specs":[
      {
         "action.type":"offsite_conversion",
         "fb_pixel":"<pixel_id>"
      }
   ]
}
```


### Anúncios que não são de catálogo


Nos anúncios de carregamento manual, acrescentamos o novo campo `omnichannel_link_spec` no criativo. Ele inclui os campos a seguir.


| Campo | Descrição |
| --- | --- |
| web Configuração da web | Objetos promovidos por pixels associados a este objeto omnicanal. url string O site que o usuário abre por meio do navegador. Para validação na web, o URL deve ser o mesmo que o link fornecido em link_data. |
| app Configuração de destino do app | Objetos promovidos por apps associados a este objeto omnicanal. application_id string O app que o usuário abre por meio do navegador. Para validação, application_id deve ser consistente com o application_id em omnichannel_object no promoted_object . platform_specs JSON Configuração de destino de pouso pela plataforma. |


### Especificações da plataforma


| Campo | Descrição |
| --- | --- |
| android JSON | Configuração de pouso para app Android. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url string Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| ios JSON | Configuração de pouso para o app iOS. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url string Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| ipad JSON | Configuração de pouso para app exclusivo para iPad. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url string Deep link para abrir o app. Saiba mais sobre deep links de produtos . |
| iphone JSON | Configuração de pouso para app exclusivo para iPhone. Para validação na web, ios , ipad , iphone são mutuamente exclusivos. Podem haver somente uma dessas chaves que existem nas platform_specs . url string Deep link para abrir o app. Saiba mais sobre deep links de produtos . |


#### Exemplo


```
{
  “creative”:
{
  "applink_treatment": "deeplink_with_web_fallback",
  "omnichannel_link_spec": {
      "web": {
        "url": <web_url>
      },
      "app": {
        "application_id": <application_id>,
        "platform_specs": {
          "android": {
            "url": <android_deeplink>
          },
          "ios": {
            "url": <ios_deeplink>
          }
        }
      }
   },
  "object_story_spec": {
    "instagram_user_id": <IG_USER_ID>,
    "page_id": <page_id>,
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
}
```


| Campo | Descrição |
| --- | --- |
| creative Especificação do criativo | Obrigatório para criação. O ID ou a especificação do criativo que será usado no anúncio. Saiba mais sobre criativos do anúncio. {"creative_id": \<creative_id\>} Ou a especificação de criativo como no exemplo anterior . |
| tracking_specs Lista de especificação de rastreamento | Especificação de rastreamento necessária para o rastreamento de conversão. Para validação de anúncios, veja as especificações necessárias abaixo e os respectivos exemplos. |


Para validação de anúncio:


O `pixel_id` e o `application_id` de `tracking_specs` devem ser consistentes com os que estão em promoted_object. `tracking_specs` deve incluir estas especificações:


| Especificação de rastreamento | Exemplo de código |
| --- | --- |
| Pixel | { "action.type" : [ "offsite_conversion" ], "fb_pixel" : [\< pixel_id \>] } |
| Instalação do app | { "action.type" : [ "mobile_app_install" ], "application" : [\< application_id \>] } |
| Evento do app | { "action.type" : [ "app_custom_event" ], "application" : [\< application_id \>] } |


#### Exemplo


```
{
     "name": "sample ad"
     "adset_id": "6170648652866",
     "creative": {
         "creative_id": <creative_id>,
    }
    "status": "PAUSED",
    "tracking_specs": [
        {
            "action.type": ["offsite_conversion"],
            "fb_pixel": [<pixel_id>]
        }
        {
            "action.type": ["mobile_app_install"],
            "application": [<application_id>]
        }
        {
            "action.type": ["app_custom_event"],
            "application": [<application_id>]
        }
    ]
}
```
[○](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#)

## Saiba mais


- [Campanhas](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/)
- [Conjuntos de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/)
- [Anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup/)
- [Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)
[○](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#)[○](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#)Nesta Página[Otimização para conversão entre canais em campanhas de compras Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#otimiza--o-para-convers-o-entre-canais-em-campanhas-de-compras-advantage-)[Conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#conjunto-de-an-ncios)[Anúncio](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#an-ncio)[Anúncios de catálogo](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#an-ncios-de-cat-logo)[Anúncios que não são de catálogo](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#an-ncios-que-n-o-s-o-de-cat-logo)[Especificações da plataforma](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#especifica--es-da-plataforma)[Saiba mais](https://developers.facebook.com/docs/marketing-api/advantage-shopping-campaigns/cross-channel-conversion#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zA5PIOLW85bbko-5d2ldZnyZeA-YvmDB6d1YDjxNywDIYSqu7fzzHBeXntQ_aem_FKuGzIqwV1qy83aphCtxew&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iUP7-wmBs3KxDsfhYZniSyFnZUFm6yw0dSF09NdAkg3z0l6E-pKGLQdKJvQ_aem_AA2R5xd98yziA7dmOK5soQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iUP7-wmBs3KxDsfhYZniSyFnZUFm6yw0dSF09NdAkg3z0l6E-pKGLQdKJvQ_aem_AA2R5xd98yziA7dmOK5soQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7u2cg7jxhD2ynkOVrK4pSupmluk0CyC7pX82jPe2xtsyCwTbYzv4HFvZyVHg_aem_jBVPLeL0VuQgnhUCmbxBQQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wm7QSngnUI25oMI-SypZdD8mo_VuK_E8GQCW14ny51bEPqyRAoNoQ0L9oaA_aem_Y6jCYLVvIqJSa0LvoJZpcA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tNlTgzYtlzTB1hoFAnbhY-8j748TRhRi7Nc-LTdrp1zAZisJwwVMEvG3k4w_aem_MIXwCt3UTmW-ifSHT9ScJA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zA5PIOLW85bbko-5d2ldZnyZeA-YvmDB6d1YDjxNywDIYSqu7fzzHBeXntQ_aem_FKuGzIqwV1qy83aphCtxew&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7u2cg7jxhD2ynkOVrK4pSupmluk0CyC7pX82jPe2xtsyCwTbYzv4HFvZyVHg_aem_jBVPLeL0VuQgnhUCmbxBQQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tNlTgzYtlzTB1hoFAnbhY-8j748TRhRi7Nc-LTdrp1zAZisJwwVMEvG3k4w_aem_MIXwCt3UTmW-ifSHT9ScJA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zA5PIOLW85bbko-5d2ldZnyZeA-YvmDB6d1YDjxNywDIYSqu7fzzHBeXntQ_aem_FKuGzIqwV1qy83aphCtxew&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iUP7-wmBs3KxDsfhYZniSyFnZUFm6yw0dSF09NdAkg3z0l6E-pKGLQdKJvQ_aem_AA2R5xd98yziA7dmOK5soQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wm7QSngnUI25oMI-SypZdD8mo_VuK_E8GQCW14ny51bEPqyRAoNoQ0L9oaA_aem_Y6jCYLVvIqJSa0LvoJZpcA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5pJhq-JLQM2p8VoS3ZIjIWJseUsQV5CqyZZJfcPIpXQB51115lC_P2cpiS-A_aem_nOny0eLk720pPg9QnvsPuw&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tNlTgzYtlzTB1hoFAnbhY-8j748TRhRi7Nc-LTdrp1zAZisJwwVMEvG3k4w_aem_MIXwCt3UTmW-ifSHT9ScJA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zA5PIOLW85bbko-5d2ldZnyZeA-YvmDB6d1YDjxNywDIYSqu7fzzHBeXntQ_aem_FKuGzIqwV1qy83aphCtxew&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4E2BmBfMBTkimEEchhURLtWgEL9qVL8zBoYPCJMVksV6GeiNzvRKFn0gEWgw_aem_V643SMC8zDWhfNN9wc_3_w&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7u2cg7jxhD2ynkOVrK4pSupmluk0CyC7pX82jPe2xtsyCwTbYzv4HFvZyVHg_aem_jBVPLeL0VuQgnhUCmbxBQQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iUP7-wmBs3KxDsfhYZniSyFnZUFm6yw0dSF09NdAkg3z0l6E-pKGLQdKJvQ_aem_AA2R5xd98yziA7dmOK5soQ&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wm7QSngnUI25oMI-SypZdD8mo_VuK_E8GQCW14ny51bEPqyRAoNoQ0L9oaA_aem_Y6jCYLVvIqJSa0LvoJZpcA&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5gY2od36-HSJFTV9xHxhtwUAmsHK5lhbklNhNGDiXstLXgVRmTYbvlRD7qHA_aem_zYwlsiGhfqep9itG7tlLbg&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT57rC8zK6r-CF7mFShecOfSca7_qVM7TPdp708cTAa7hacPjEjNvN2JNZqC4BPRWKDGjvWD4TFyGRqQUXuppJAS7ctKcXUUldQHRxS84uYQAc7C5oYY_Hy8-cbILLiSX_RAesQFJzskQTe7KARmx5mwuQQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão