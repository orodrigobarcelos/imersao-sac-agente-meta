<!-- Fonte: Anúncios de Catálogo Advantage+ para celular - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de Catálogo Advantage+ de app para celular


É possível configurar Anúncios de Catálogo Advantage+ para celular com SDKs do Facebook. Incorpore o deep linking e o deep linking diferido ao app para proporcionar a melhor experiência possível às pessoas.


## Etapa 1: configurar o SDK do Facebook para Celular (iOS ou Android)


Integre o SDK do Facebook para [iOS](https://developers.facebook.com/docs/ios/getting-started) ou [Android](https://developers.facebook.com/docs/android/getting-started).
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)

## Etapa 2: configurar Eventos do App para celular


Na web, use os eventos de Pixel da Meta, como `ViewContent`, para rastrear as interações de eventos. Em celulares, é possível rastrear os mesmos eventos com Eventos do App.


Envie os mesmos três eventos obrigatórios do app e do Pixel: `ViewContent`, `AddToCart` e `Purchase`. Para funcionar corretamente, os Anúncios de Catálogo Advantage+ precisam desses eventos.


| Evento para iOS | Evento para Android | Equivalente para a web |
| --- | --- | --- |
| FBSDKAppEventNameViewedContent | AppEventsConstants:: EVENT_NAME_VIEWED_CONTENT | ViewContent |
| FBSDKAppEventNameAddedToCart | AppEventsConstants:: EVENT_NAME_ADDED_TO_CART | AddToCart |
| [[FBSDKAppEvents shared] logPurchase:(double) currency:(NSString *) parameters:(NSDictionary *)]; | AppEventsConstants:: EVENT_NAME_PURCHASED | Purchase |


Por exemplo, um evento `ViewContent` é disparado quando alguém visualiza um produto no app:

```
[[FBSDKAppEvents shared] logEvent:FBSDKAppEventNameViewedContent
  valueToSum:54.23
  parameters:@{
    FBSDKAppEventParameterNameCurrency    : @"USD",
    FBSDKAppEventParameterNameContentType : @"product",
    FBSDKAppEventParameterNameContentID   : @"123456789"
  }
];
```

```
Bundle parameters = new Bundle();
parameters.putString(AppEventsConstants.EVENT_PARAM_CURRENCY, "USD");
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_TYPE, "product");
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_ID, "1234");

logger.logEvent(AppEventsConstants.EVENT_NAME_VIEWED_CONTENT,
                120.00,
                parameters);
```


Também é possível fornecer uma matriz de valores em JSON de IDs de produto quando ocorrer um evento em diversos produtos. Por exemplo, você pode enviar vários produtos com o evento `Purchase`.

```
[[FBSDKAppEvents shared] logPurchase:54.23 currency : @"USD" parameters:@{
  FBSDKAppEventParameterNameContentID   : @"['1234','5678']",
  FBSDKAppEventParameterNameContentType : @"product"
  }
];
```

```
Bundle parameters = new Bundle();
parameters.putString(AppEventsConstants.EVENT_PARAM_CURRENCY, "USD");
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_TYPE, "product");
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_ID, "['1234', '5678']");

logger.logEvent(AppEventsConstants.EVENT_NAME_PURCHASED,
                180.00,
                parameters);
```


### Diversas identificações de conteúdo


Se houver várias identificações de conteúdo, forneça uma matriz JSON com escape, por exemplo:

```
"[\"1234\",\"5678\"]"
```


### Parâmetros opcionais


Para cada evento do app, é possível enviar parâmetros adicionais. Envie-os quando alguém fizer uma compra:


| Nome | Descrição |
| --- | --- |
| _valueToSum string | Opcional. Valor do produto ou da compra |
| fb_currency string | Opcional. A moeda usada no valor do produto ou da compra |


### Como usar um Parceiro de Métricas para Aplicativos


Se você usar um Parceiro de Métricas para Aplicativos (MMP, pelas iniciais em inglês) aprovado para relatar eventos ao Facebook, poderá ajustar sua implementação para enviar também os eventos obrigatórios. O processo varia de acordo com o MMP, mas normalmente é assim:


- Ajuste sua integração para relatar os [três eventos obrigatórios ao MMP](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#mmprequiredevents), bem como os parâmetros necessários.
- Com o MMP, mapeie o nome dos seus eventos em relação aos do Facebook.
- [Teste os Eventos do App](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#testing-app-events).


### Eventos obrigatórios para o MMP


Os eventos a seguir são **obrigatórios**.


| Nome | Descrição |
| --- | --- |
| fb_mobile_content_view | Quando uma conta da Central de Contas visualizou um produto. |
| fb_mobile_add_to_cart | Quando um item foi adicionado ao carrinho. |
| fb_mobile_purchase | Quando itens foram comprados. |


Você também precisa enviar estes dois parâmetros adicionais para que os Anúncios de Catálogo Advantage+ funcionem:


- A identificação do item visualizado, adicionado ao carrinho ou comprado
- Se a identificação é um `product` ou `product_group`


Os parâmetros adicionais disponíveis são os seguintes:


| Nome | Descrição |
| --- | --- |
| fb_content_type string | product ou product_group |
| fb_content_id string | Obrigatório. Uma string com uma matriz codificada em JSON das identificações de produto ou grupo de produtos do varejista |
| _valueToSum string | Opcional. O valor do produto comprado |
| fb_currency string | Opcional. A moeda usada no valor do produto ou da compra |


**Observação:** quando itens forem comprados, envie também os parâmetros `_valueToSum` e `fb_currency`.


### Como testar Eventos do App


O [Auxiliar para Anúncios no Aplicativo](https://developers.facebook.com/tools/app-ads-helper/) é a forma mais fácil de testar se a integração funcionou, para ver os eventos e parâmetros informados ao Facebook em tempo real.


- Selecione um app.
- Você verá duas ferramentas na parte inferior da página. Selecione **Testar os eventos do app**.
- Há duas opções: ver os eventos sendo relatados por você ou por uma identificação do anunciante específica. Na maioria dos casos, basta selecionar **Eu**. Verifique se você tem o Facebook instalado no dispositivo e se fez login.
- À medida que você realiza ações no app, os eventos serão exibidos na ferramenta com os respectivos parâmetros.


Você verá estes três nomes de eventos se a integração for concluída:


- `FB_MOBILE_CONTENT_VIEW`
- `FB_MOBILE_ADD_TO_CART`
- `FB_MOBILE_PURCHASE`


Saiba mais sobre os eventos do app para [iOS](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/getting-started-app-events-ios) e para [Android](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/getting-started-app-events-android).


Para verificar a função de eventos do app, confira os eventos recentes no
[Gerenciador de Eventos do Facebook](https://www.facebook.com/events_manager2)

.
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)

## Etapa 3: configurar deep linking


Ao fornecer deep links no feed de produtos, qualquer pessoa que interagir com o anúncio no Facebook poderá ir diretamente a um local específico no app. Por exemplo, se alguém clicar em um anúncio enquanto usa o Facebook em um dispositivo móvel, essa pessoa verá o produto no seu app para celular. Para ver mais informações, consulte [Deep Linking](https://developers.facebook.com/docs/app-ads/deep-linking) e [Verify Deep Linking](https://developers.facebook.com/tools/app-ads-helper).


### Fallback para web em comparação com App Store


Ao usar deep links, você pode especificar o comportamento de fallback se alguém não tiver o app instalado. Ao fornecer deep links no feed de produtos, quem não tiver o app verá a URL da web do produto no anúncio.


Sua meta provavelmente é aumentar as vendas do catálogo. Por isso, talvez você prefira que as pessoas vejam as páginas dos produtos, e não o app para instalação. Portanto, nosso padrão são as URLs da web, embora seja possível especificar um comportamento diferente para ter mais controle. Defina o comportamento de fallback como `applink_treatment` ao criar o Anúncio de Catálogo Advantage+ e use uma destas opções:


| Nome | Descrição |
| --- | --- |
| web_only | Sempre encaminha alguém à URL da web especificada. Substitui todos os deep links do seu feed. |
| deeplink_with_web_fallback | Encaminha alguém ao seu app se ele estiver instalado e houver deep links correspondentes. Caso uma dessas condições não seja atendida, encaminha à URL do site. |
| deeplink_with_appstore_fallback | Encaminha alguém ao app se ele estiver instalado e houver informações de deep link correspondentes. Caso o aplicativo não esteja instalado, encaminha à loja de aplicativos correspondente. |

[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)

## Etapa 4: configurar feed de produtos


Forneça agora deep links para Anúncios de Catálogo Advantage+. Para ver mais informações, consulte [Product Catalog, Deep Linking](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-catalog#deep-linking).
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)

## Etapa 5: definir especificações de rastreamento


Para mensurar eventos de conversão do site e dos apps para celular, verifique se todos os Anúncios de Catálogo Advantage+ têm as [especificações de rastreamento](https://developers.facebook.com/docs/marketing-api/tracking-specs) adequadas definidas para estes eventos:


| Evento | Especificação de rastreamento |
| --- | --- |
| offsite_conversion | { 'action.type': 'offsite_conversion', 'fb_pixel': FB_PIXEL_ID } |
| app_custom_event | {'action.type':'app_custom_event','application':APP_ID} |
| mobile_app_install | {'action.type':'mobile_app_install','application':APP_ID} |


O Facebook pode rastrear todos os eventos com origem em um Anúncio de Catálogo Advantage+ independentemente de alguém visualizar o site ou app. Para definir as especificações de rastreamento:

```
curl \ -F 'tracking_spec=[ {"action.type":["app_custom_event"],"application":["101"]}, {"action.type":["offsite_conversion"],"offsite_pixel":["<PIXEL_ID>"]}, {"action.type":["mobile_app_install"],"application":["101"]} ]' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#)Nesta Página[Anúncios de Catálogo Advantage+ de app para celular](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#an-ncios-de-cat-logo-advantage--de-app-para-celular)[Etapa 1: configurar o SDK do Facebook para Celular (iOS ou Android)](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#etapa-1--configurar-o-sdk-do-facebook-para-celular--ios-ou-android-)[Etapa 2: configurar Eventos do App para celular](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#etapa-2--configurar-eventos-do-app-para-celular)[Diversas identificações de conteúdo](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#diversas-identifica--es-de-conte-do)[Parâmetros opcionais](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#par-metros-opcionais)[Como usar um Parceiro de Métricas para Aplicativos](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#como-usar-um-parceiro-de-m-tricas-para-aplicativos)[Eventos obrigatórios para o MMP](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#mmprequiredevents)[Como testar Eventos do App](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#como-testar-eventos-do-app)[Etapa 3: configurar deep linking](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#etapa-3--configurar-deep-linking)[Fallback para web em comparação com App Store](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#fallback-para-web-em-compara--o-com-app-store)[Etapa 4: configurar feed de produtos](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#etapa-4--configurar-feed-de-produtos)[Etapa 5: definir especificações de rastreamento](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/mobile-apps#trackingspecs) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zjx7ZEgyawOBuW0YjjgCl0TCNAIZleAJO0oL81nRQ4j93N8kMSXp-TfzbHA_aem_Iikj0Ie9CAsg94LtSCTJ1w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-5-a1ZWeqnVDyU4OJvOokel3rbn4ve5JIW8mB_rhFXTdmOwjO5KEWqtj8CA_aem_Ep6SCek_AsdYUnXFTVrBAw&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7SFUqz8fis3YZX-lwIn663kLSzkMbdycuynE8NGwexVObLZy0olvWjJUxqag_aem_QS2ycNssKN1kPqXVZprjSg&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IM0Af6xp5N5FSdEe4og5bhQW4j-wftXW6DpmfnQQnvgMqLKAYBp6lGJHWAA_aem_CqsuOw5XR_gDU-JMngQsTg&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IM0Af6xp5N5FSdEe4og5bhQW4j-wftXW6DpmfnQQnvgMqLKAYBp6lGJHWAA_aem_CqsuOw5XR_gDU-JMngQsTg&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zjx7ZEgyawOBuW0YjjgCl0TCNAIZleAJO0oL81nRQ4j93N8kMSXp-TfzbHA_aem_Iikj0Ie9CAsg94LtSCTJ1w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4MIrA7fJtc1jt0gdtTfg-AB9QHX0qrh-IBP_BRhkiSu_u_qOv3BCOPCvsIMg_aem_wvIGpR38Dud1bUQGpb1WEA&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4gep7o4_Qs6wc8ezd5nWW_GqXHx4l8QuPgcYLgiqKyZSs5RXFpdjiknW_GXw_aem_yszJbkbvN7j9jt_VOC7S2w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4MIrA7fJtc1jt0gdtTfg-AB9QHX0qrh-IBP_BRhkiSu_u_qOv3BCOPCvsIMg_aem_wvIGpR38Dud1bUQGpb1WEA&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4gep7o4_Qs6wc8ezd5nWW_GqXHx4l8QuPgcYLgiqKyZSs5RXFpdjiknW_GXw_aem_yszJbkbvN7j9jt_VOC7S2w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zjx7ZEgyawOBuW0YjjgCl0TCNAIZleAJO0oL81nRQ4j93N8kMSXp-TfzbHA_aem_Iikj0Ie9CAsg94LtSCTJ1w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4MIrA7fJtc1jt0gdtTfg-AB9QHX0qrh-IBP_BRhkiSu_u_qOv3BCOPCvsIMg_aem_wvIGpR38Dud1bUQGpb1WEA&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4MIrA7fJtc1jt0gdtTfg-AB9QHX0qrh-IBP_BRhkiSu_u_qOv3BCOPCvsIMg_aem_wvIGpR38Dud1bUQGpb1WEA&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7SFUqz8fis3YZX-lwIn663kLSzkMbdycuynE8NGwexVObLZy0olvWjJUxqag_aem_QS2ycNssKN1kPqXVZprjSg&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-5-a1ZWeqnVDyU4OJvOokel3rbn4ve5JIW8mB_rhFXTdmOwjO5KEWqtj8CA_aem_Ep6SCek_AsdYUnXFTVrBAw&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-5-a1ZWeqnVDyU4OJvOokel3rbn4ve5JIW8mB_rhFXTdmOwjO5KEWqtj8CA_aem_Ep6SCek_AsdYUnXFTVrBAw&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-5-a1ZWeqnVDyU4OJvOokel3rbn4ve5JIW8mB_rhFXTdmOwjO5KEWqtj8CA_aem_Ep6SCek_AsdYUnXFTVrBAw&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-5-a1ZWeqnVDyU4OJvOokel3rbn4ve5JIW8mB_rhFXTdmOwjO5KEWqtj8CA_aem_Ep6SCek_AsdYUnXFTVrBAw&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Ns8tGC5AOcrl9bv85YN9Djv5erfI_NAhQP6Jrv0w1kNfMBKPIyfzh8LTYbQ_aem_o_NyqxPzgCe7wPq5J2s71A&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zjx7ZEgyawOBuW0YjjgCl0TCNAIZleAJO0oL81nRQ4j93N8kMSXp-TfzbHA_aem_Iikj0Ie9CAsg94LtSCTJ1w&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6tw3A9XVJkhY3M_qE6rqC0z7_FLI5OXcBubd9Ajkv0tGvmi4XK5WT8QzYMfupbq9Nhfwofx56JQLWqFh2BOug_gwpNO6IsXPmUmIgHie_GqVPc2TelOaY-4lzMv_HAQndPwF5eNE2IhPcKXWKP7ebj69A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão