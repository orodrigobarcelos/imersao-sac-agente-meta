<!-- Fonte: Públicos personalizados do site - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Públicos personalizados do site


Crie um público personalizado de usuários que acessaram o site ou que realizaram ações específicas nele usando o Pixel da Meta, os eventos na plataforma da Meta e regras de público.


Depois de criar um público personalizado com dados do site, faça referência a ele para direcionar os anúncios da mesma forma que você faz com os [públicos personalizados](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting) padrão. O Facebook atualiza esse público automaticamente de acordo com a política de retenção definida por você.


Consulte [Custom Audience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience) e [Rastreamento de conversão](https://developers.facebook.com/docs/meta-pixel/implementation/conversion-tracking) para saber mais.


### API de Conversões


Ao compartilhar eventos de conversão usando a API de Conversões, você pode criar um público personalizado do site para usar com anúncios. Você também pode criar um público personalizado offline e um público personalizado de app para celular. Recomendamos que você compartilhe o [`external_id`](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/external-id) como um parâmetro de informações do cliente para melhorar as taxas de correspondência e impulsionar correspondências em diferentes canais.


O mapeamento de [`external_id`](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/external-id) feito pela API de Conversões é diferente daquele usado com o `extern_id` para criar um público personalizado de arquivo de cliente. O mapeamento de `external_id` não pode ser usado para criar um público personalizado de arquivo de cliente. Da mesma forma, o `extern_id` gerado por meio do mapeamento de público personalizado de arquivo de cliente não pode ser usado para criar Públicos Personalizados da web, offline nem de app para celular.


## Antes de começar


Para criar um público personalizado a partir de sites, você precisa aceitar os Termos de Serviço para Públicos Personalizados no [Gerenciador de Anúncios](https://www.facebook.com/ads).
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Criar públicos


Para criar um público personalizado do site, faça uma solicitação `POST` para:

```
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


Use os seguintes parâmetros:


| Nome | Descrição |
| --- | --- |
| name tipo: cadeia de caracteres | Obrigatório. Nome do público. |
| rule tipo: objeto JSON | Obrigatório. Regras do público aplicadas ao URL de referência. Consulte Regras de público . |
| retention_days tipo: número inteiro | Opcional. Número de dias para manter alguém no público. Entre 1 e 180 dias. Se não for especificado, usaremos o valor retention_days do campo retention_seconds na regra. |
| prefill tipo: booliano | Opcional. O padrão é true . Opções disponíveis: true : inclui a atividade do site registrada antes da criação do público.; false : inclui apenas o tráfego do site a partir do momento da criação do público. Se não for especificado, usaremos o valor prefill do campo retention_seconds na regra. O preenchimento automático máximo é de 180 dias. |


Por exemplo:

```
curl -X POST \ -F 'name="My Test Website Custom Audience"' \ -F 'rule={ "inclusions": { "operator": "or", "rules": [ { "event_sources": [ { "id": "<PIXEL_ID>", "type": "pixel" } ], "retention_seconds": 8400, "filter": { "operator": "and", "filters": [ { "field": "url", "operator": "i_contains", "value": "shoes" } ] } } ] } }' \ -F 'prefill=1' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


Modelo de resposta:

```
{
  "id": "123567890"
}
```


### Regras de público


Um público personalizado para Públicos Personalizados de Site deve conter uma regra de público. Cada regra deve ser fornecida como uma string codificada por JSON. Consulte [Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules) para saber mais.


### Público personalizado do site do Pixel da Meta


Use a chamada de API a seguir para criar um público personalizado de pixel:

```
curl -X POST \ -F 'name="My WCA Pixel"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adspixels
```


A chamada retornará a identificação do pixel:

```
{
  "id": "11111"
}
```


### Ler o código de pixel do público personalizado


Recupere o código de pixel do público personalizado:

```
curl -X GET \ -d 'fields="code"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<PIXEL_ID>
```


A resposta a seguir será retornada, em que `code` contém o código de pixel relevante para o público personalizado:

```
{
  "data": [
    {
      "code": "<script>(function() {\n  var _fbq = window._fbq || (window._fbq = []);\n  if (!_fbq.loaded) {\n    var fbds = document.createElement('script');\n    fbds.async = true;\n    fbds.src = 'https://connect.facebook.net/en_US/fbds.js';\n    var s = document.getElementsByTagName('script')[0];\n    s.parentNode.insertBefore(fbds, s);\n    _fbq.loaded = true;\n  }\n  _fbq.push(['addPixelId', '11111']);\n})();\nwindow._fbq = window._fbq || [];\nwindow._fbq.push(['track', 'PixelInitialized', {}]);\n</script>\n<noscript><img height=\"1\" width=\"1\" alt=\"\" style=\"display:none\" src=\"https://www.facebook.com/tr?id=11111&amp;ev=NoScript\" /></noscript>",
      "id": "11111"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MjM4NzQ5Njk5NjI2Mzc2",
      "after": "MjM4NzQ5Njk5NjI2Mzc2"
    }
  }
}
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Gerenciar públicos


### Ler


Para ler públicos de uma conta de anúncios, faça uma solicitação `HTTP GET`:

```
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


Exemplo:

```
curl -X GET \ -d 'fields="id"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


Modelo de resposta:

```
{
  "data": [
    {
      "name": "My Test CA",
      "id": "1234567890"
    },
    {
      "name": "WCA",
      "id": "0987654321"
    },
  ],
}
```


Para ler um público personalizado específico:

```
curl -X GET \ -d 'fields="name,rule"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```


Modelo de resposta:

```
{
  "name": "My WCA",
  "rule": "{\"and\": [\n\t\t{\"url\": {\"i_contains\": \"shoes\"}},\n\t\t{\"url\": {\"i_contains\": \"red\"}}]}",
  "id": "1234567890"
}
```


### Atualizar


Para atualizar o nome de um público personalizado:

```
curl -X POST \ -F 'name="Updated Name for CA"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```


Exemplo de resposta:

```
{
  "success": true
}
```


### Excluir


Exclua um público por `id`:

```
curl -X DELETE \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```


Exemplo de resposta:

```
{
  "success": true
}
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Recurso aprimorado: Públicos Personalizados do site


**Este produto está obsoleto**. Leia [Públicos Personalizados do site aprimorados](https://developers.facebook.com/docs/marketing-api/audiences/guides/enhanced-website-custom-audiences).
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Data dinâmica (*versão beta*)


Permite que os anunciantes de viagens direcionem anúncios aos usuários que pesquisaram hotéis e voos com base na data de check-in. Por exemplo, o anunciante pode criar um público composto apenas por usuários com datas futuras de check-in.


Os anunciantes de viagens devem inserir a data de check-in no campo checkin_date para inicializações do pixel:

```
fbq('track', 'Search', {'checkin_date': '2015-09-15', 'num_of_travelers':2});
```


### Formatos de data/hora compatíveis


No momento, somente o formato ISO-8601 de data/hora é compatível. Por exemplo:


- `YYYYMMDD` (20080921)
- `YYYY-MM-DD` (1997-07-16)
- `YYYY-MM-DDThh:mmTZD` (1997-07-16T19:20+0100)
- `YYYY-MM-DDThh:mm:ssTZD` (1997-07-16T19:20:30+0100)


Onde:


- `YYYY` é o ano com quatro dígitos
- `MM` é o mês com dois dígitos (01=janeiro etc.)
- `DD` é o dia do mês com dois dígitos (01 a 31)
- `hh` são os dois dígitos de hora (00 a 23: o sistema de horário de 12 horas NÃO é permitido)
- `mm` são os dois dígitos de minutos (00 a 59)
- `ss` são os dois dígitos de segundos (00 a 59)
- `TZD` é o designador do fuso horário (+hhmm ou -hhmm)


### Exemplos


Os usuários que pesquisaram hotéis com start_date posterior ao dia de hoje nos últimos 30 dias:

```
curl
-F "name=search_hotel_later_than_today"
-F "pixel_id=PIXEL_ID"
-F "retention_days=30"
-F 'rule={"event": {"i_contains": "search"}}'
-F 'rule_aggregation={"type":"last_event_time_field", "config":{"field":"checkin_date", "time_format":"YYYY-MM-DD"}, "operator":"lt", "value": "0"}'
-F "access_token=ACCESS_TOKEN"
"https://graph.facebook.com/API_VERSION/act_AD_ACCOUNT_ID/customaudiences"
```


### Boas práticas


- Teste as possíveis medidas diferentes de valor, por exemplo, pessoas que acessaram o site com frequência, mas não efetuaram compras ou pessoas que acessaram o site de vários dispositivos.
- Crie Públicos Semelhantes com base nos públicos personalizados de melhor desempenho.
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Perguntas frequentes

[What are the benefits of using Custom Audiences on my website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_245191306346816)

With Custom Audiences, you can reach people who recently visited your website and deliver them highly relevant ads based on interest they express in your products.


Other benefits include:


- Remarket to people using your website
- Make your existing ads more efficient by excluding audiences of people who have already converted on your message
- Create lookalike audiences of people who look like the people browsing your website


By tracking how each customer progresses in a process, you can more effectively influence customers who expressed interest in your products. For example, using Meta Pixel, capture intent based on activity of people who are viewing pages about a loyalty program, browsing a particular product page, or filling out a preferences form. Later, you can serve relevant ads to these people to help them complete the conversion.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_245191306346816)[How do I create a Website Custom Audiences?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_347187002816218)

See [Advertiser Help Center, Custom Audience from your Website](https://www.facebook.com/business/help/1474662202748341)
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_347187002816218)[How do I edit an existing Website Custom Audience?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_478594739551719)

See [Advertiser Help Center, Custom Audience from your Website](https://www.facebook.com/business/help/1474662202748341). When you add or remove people, updates can take a few hours. But your ads continue to run.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_478594739551719)[How many audiences can I create?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_632297880529881)

At this time, there's a maximum of `10000` Custom Audiences from your website that can be created in a single account.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_632297880529881)[Can I exclude a Website Custom Audience from my ad targeting?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_1014974385360238)

Yes. Exclusion targeting prevents a particular audience from seeing your ad to help deliver your advertising more precisely. For example, exclude an audience of your current customers if you run a campaign to acquire new customers.


In Ads Manager, in the audience section of creating an ad, click Exclude and add the custom audience to the list.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_1014974385360238)[How long will customers stay in my website custom audience?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_804553549918026)

The longest duration can be set for `365 days`. After 365 days, audience members are removed, unless they revisit the website again and match the same audience rule.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_804553549918026)[Can I create a Lookalike Audience of a Website Custom Audience?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2242411656022979)

Yes. Open Ad Manager. Under the **Audiences** tab, click the **New Audience** drop-down menu and select **Lookalikes**.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2242411656022979)[Can Dating & Gambling clients use Custom Audiences from your website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_302357224042901)

Dating can use Custom Audiences from your website. However, gambling websites must be approved through the sales team on a managed list, and you must provide demographic restrictions, such as 21 years+.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_302357224042901)[What bid type should we use for Custom Audiences from your website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_403700677149737)

We recommend CPM bidding for Website Custom Audience until your audience has reached a sufficiently large size. Start with CPM, then migrate to `oCPM` or `CPC` once you reach sufficient scale.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_403700677149737)[Can I access mobile and web inventory with Custom Audiences from your website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_327324904632427)

Yes, Custom Audiences from your website works with all native ad formats and serves across desktop, mobile, and tablet.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_327324904632427)[How does Custom Audiences from Your Website relate to 'FBX'?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_1981532501955988)

`FBX` and Website Custom Audiences are complementary products. `FBX` is best when advertisers require product-level dynamic ads, which are as current as possible and are not yet easily facilitated by Custom Audiences from your website. However, FBX is limited to desktop inventory. Custom Audiences from your website allows targeting across browsers, overlaying of Meta data, access to mobile inventory, and usage of all Meta ad units—all of which are not available on `FBX`.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_1981532501955988)[What is user retention based on?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_324254141599761)

Custom Audiences from Your Website requests a duration where customers will be retained within the audience created. The duration is based on when customers visited a website and fired the Meta Pixel. For example, with a retention window of 30 days, if someone visits a website and matches an Audience rule on June 1st, Facebook automatically removes them from the Website Custom Audience on June 30.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_324254141599761)[Can we apply more complex rules for sophisticated clients?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_298613481056240)

You can create rules based on URLs visited or on custom events from Meta Pixel. Using custom data, create audiences based upon SKUs, Pricing, Color, or any other attribute you send to Facebook. See [Meta Pixel](https://developers.facebook.com/docs/marketing-api/audiences/guides/docs/meta-pixel).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_298613481056240)[What privacy features are in Custom Audiences from your website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2272020379524582)

No personal information is reported to the advertiser about any individual person on a website. You can only target an audience once it reaches a certain size; it's impossible to learn the individual identity an any person visiting a website.


Meta also provides an AdChoices link where people can learn more and opt out of targeted ads they receive. Click the “x” in the top-right corner of ads to show more options:


- Hide this ad — Don't see this ad again (Facebook native). This is specific to the ad ID in the campaign only.
- Hide all ads — Don't see any other ads from that advertiser (Facebook native). Hide any ads from either that subdomain, such as `savings.att.com` or `att.com`, or the page `facebook.com/ATT` if we have it. Block the sub-domain or page across ad accounts.
- Why Am I seeing this Ad?
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2272020379524582)[Are View Tags allowed with Custom Audiences from your website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_322796621735315)

View Tags are not yet permitted for Custom Audiences from your website clients. Only Atlas view tag are accepted at this time.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_322796621735315)[Can Website Custom Audiences be shared with another account or FBMP?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_859726221030096)

Yes, it's possible to share Website Custom Audiences.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_859726221030096)[If I delete a Website Custom Audience, what happens to my campaign that's targeting this Website Custom Audience?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_434218667404147)

If an `Active` campaign targets a Website Custom Audience and that audience is deleted, the campaign is put on `Pause`.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_434218667404147)[How quickly does my audience update?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2679588715416394)

We update an audience as soon as technically possible. Once customers go to webpages with a Meta Pixel and match an Audience rule, they're added to that Website Custom Audience. If this Website Custom Audience is being targeted with an ad, the customer is eligible to be served an ad in a matter of minutes.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2679588715416394)[Do I have to add a new Meta Pixel to my website every time I create an audience?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_524284168101598)

No. There's one Meta Pixel generated per account. Add this Meta Pixel to all pages of your website one at a time, and use Audience rules to create different Website Custom Audiences.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_524284168101598)[Can I use a Meta Pixel with another third-party tag?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2323449701309739)

Yes. You can use data from third-party tags, Tag Managers, or a DFA Floodlight tag. This depends on the sophistication of the third-party client. Simple rules are easy to implement, but if you pass dynamic variables through the JavaScript event, your third-party tag should receive them and pass them to the [Meta Pixel](https://developers.facebook.com/docs/meta-pixel/implementation/custom-audiences) via Custom Data fields.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2323449701309739)[What are other benefits of using the JavaScript version of Meta Pixel?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_359125061475611)

The full JavaScript version has the following advantages over the IMG-only pixel:


- It's cross-browser and cross-platform.
- It's fast and loads asynchronously so it doesn't block the page load.
- Built-in cache buster increases effectiveness.
- You can send custom data with large payloads using HTTP POST.
- It captures the original page URL when the pixel is placed in a tag container.
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_359125061475611)[What is a pixel ID?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_405980270246838)

A pixel ID is an identifier of the piece of code placed on an advertiser's website. There's one pixel ID per Meta Ad account.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_405980270246838)[How to obtain a Meta Pixel through the API?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_593120604529250)

See [Meta Pixel](https://developers.facebook.com/docs/facebook-pixel/using-the-pixel).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_593120604529250)[Where should I place Meta Pixel in my website?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_284009965837595)

See [Meta Pixel](https://developers.facebook.com/docs/meta-pixel/get-started#installing-the-pixel).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_284009965837595)[How can I fire Custom Data events using 'fbq'?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_438736210035736)

See [Meta Pixel, with Website Custom Audiences](https://developers.facebook.com/docs/facebook-pixel/pixel-with-ads/website-custom-audiences).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_438736210035736)[How do I refer to custom data in Custom Audiences from your website rules?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2706177122758266)

In your rules, refer to event names under the parameter 'event'. For rules based on custom data, refer to it the same way you do for referring URLs, under the parameter 'url'. For example, to matches all visitors:


- to URLs containing 'signup', or
- associated with event 'SignUp' by fbq.push(['track', 'SignUp']);

```
"filter": {
    "operator": "or",
    "filters": [
        {
            "field": "url",
            "operator": "i_contains",
            "value": "signup"
        }
        {
            "field": "event",
            "operator": "i_contains",
            "value": "SignUp"
        }
    ]
}
```


The following rule matches all visitors who have viewed any product in the TV category by fbq.push(['track', 'ViewProduct', {category: 'TV'}]);.

```
"filter": {
    "operator": "or",
    "filters": [
        {
            "field": "event",
            "operator": "i_contains",
            "value": "ViewProduct"
        }
        {
            "field": "category",
            "operator": "i_contains",
            "value": "TV"
        }
    ]
},
```
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2706177122758266)[How to track conversion events?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2077045749060062)

The above examples shows how to track remarketing events. Use the same way to track conversion events by replacing `eventName` with conversion ID. This ID is created during the regular conversion creation flow (https://www.facebook.com/ads/manage/convtrack.php).

```
window.fbq = window.fbq || [];
fbq.push(['track', 123456, {currency: 'USD', value: 30.00}]);
```


Ideally, you don't need to know whether a fired event is a conversion event or a remarketing event. You only need the conversion ID to fire a conversion event. For example, if the old conversion pixel is:

```
var fb_param = {};
fb_param.pixel_id = '1234567890';
fb_param.value = '5.00';
fb_param.currency = 'USD';
(elided other code)
```


Then, using the new pixel, it is the following:

```
window.fbq = window.fbq || [];
fbq.push(['track', 1234567890, {currency: 'USD', value: 5.00}]);
```


The old conversion pixel allowed either a conversion pixel or a remarketing pixel on a page. Meta Pixel allows multiple pixel firings, including multiple conversion events, multiple remarketing events, or both per page.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2077045749060062)[How do you use an image only version of the Meta Pixel?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2711645618877583)

Manually insert an `IMG` tag:

```
<img height="1" width="1" border="0" alt="" style="display:none"
  src="https://www.facebook.com/tr?id=pixel_ID/ad_account_id&amp;ev=event name&amp;cd[p1]=v1&amp;cd[p2]=v2..." />
```


Custom data is represented as key-value pairs. Each parameter is inside 'cd[...]'. For example:

```
<img height="1" width="1" border="0" alt="" style="display:none"
  src="https://www.facebook.com/tr?id=1234&amp;ev=ViewProduct
       &amp;cd[category]=TV" />
```


Is equivalent to the following JS call:

```
window.fbq = window.fbq || [];
fbq.push(['track', 'ViewProduct', {category: 'TV'}]);
```
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2711645618877583)[How do you use an image pixel to fire conversion events?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2092725907491551)

Use parameter 'ev' to specify conversion ID, parameter 'cd[value]' to specify value, and parameter 'cd[currency]' to specify currency:

```
<img height="1" width="1" border="0" alt="" style="display:none"
  src="https://www.facebook.com/tr?id=1234&amp;ev=1234567890
       &amp;cd[value]=5.00&amp;cd[currency]=USD" />
```
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2092725907491551)[When to use image pixel?](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2253302334987231)

Meta Pixel code tries to fire events using JavaScript first. If JavaScript isn't available, Meta Pixel code tries to use image pixel. However it's recommended to always use the JavaScript pixel:


- Can be fired multiple times on each page load.
- Can control when an event should be fired such as on a button click.
- Not subject to `HTTP GET` limit in sending custom data.
[Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq_2253302334987231)[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)

## Artigos relacionados


- [Pixel da Meta](https://developers.facebook.com/docs/facebook-pixel)
- [Rastreamento de conversão](https://developers.facebook.com/docs/marketing-api/facebook-pixel/conversion-tracking/)
- [Custom Audience](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/)
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#)Nesta Página[Públicos personalizados do site](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#p-blicos-personalizados-do-site)[Antes de começar](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#antes-de-come-ar)[Criar públicos](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#criar-p-blicos)[Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#audiencerules)[Público personalizado do site do Pixel da Meta](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#createpixel)[Ler o código de pixel do público personalizado](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#readpixelcode)[Gerenciar públicos](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#read)[Ler](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#ler)[Atualizar](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#atualizar)[Excluir](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#excluir)[Recurso aprimorado: Públicos Personalizados do site](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#enhanced)[Data dinâmica (versão beta)](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#dynamic_date)[Formatos de data/hora compatíveis](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#formatos-de-data-hora-compat-veis)[Exemplos](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#exemplos)[Boas práticas](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#boas-pr-ticas)[Perguntas frequentes](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#faq)[Artigos relacionados](https://developers.facebook.com/docs/marketing-api/audiences/guides/website-custom-audiences#related) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5h46nHA8qiTr-F97cFfuWNo5yQEGVyzB0tAq69QN_dB9V7mEpixfQycRUrCg_aem_rfP7wGlQsQf-p1vPyEjmWA&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uQJVg04YaMn4mwNyijGUcQk2IN-08zfIPPLHC0qhhqL9xhoZm2keXqaKLpA_aem_LMAXLrWQoa-yGJA5HyevTQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR730k8hdojz6zs6b6T9GoP3mkmqf2aawRkfODMwIFko7H1KgFFGBeZDjd6WjA_aem_jgDRB6RcZi0KMILtGy2pNw&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kWNaY-anT0SQl5lfh2JP3X50rsxjZ0PbPaxQAoi1l9eE3S-WD9SbCs-RPuw_aem_m3rbuJhVF2qUKW8D-u72ug&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR53C2dXDUflPyz7WR1oCKLKxSUaynwCgJECsouJVbO4AqMXHt5Kpy3p2MF-ZQ_aem_ARbWFNLoXiiJyOG4Z-isgg&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uQJVg04YaMn4mwNyijGUcQk2IN-08zfIPPLHC0qhhqL9xhoZm2keXqaKLpA_aem_LMAXLrWQoa-yGJA5HyevTQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR53C2dXDUflPyz7WR1oCKLKxSUaynwCgJECsouJVbO4AqMXHt5Kpy3p2MF-ZQ_aem_ARbWFNLoXiiJyOG4Z-isgg&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kWNaY-anT0SQl5lfh2JP3X50rsxjZ0PbPaxQAoi1l9eE3S-WD9SbCs-RPuw_aem_m3rbuJhVF2qUKW8D-u72ug&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5h46nHA8qiTr-F97cFfuWNo5yQEGVyzB0tAq69QN_dB9V7mEpixfQycRUrCg_aem_rfP7wGlQsQf-p1vPyEjmWA&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Xt8aQAh8TDq7M4gNQkQI7Sn-0wsOMTQkcRU-338B33l1Aha2-EQZ0jRjREg_aem_BsSLsPSgZ226U5c07miOCA&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Xt8aQAh8TDq7M4gNQkQI7Sn-0wsOMTQkcRU-338B33l1Aha2-EQZ0jRjREg_aem_BsSLsPSgZ226U5c07miOCA&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NfOyAxVvOBCsnVT29Towyxl0Nu1sz3csZujuOKCRvsSiXDMncgtvoXbwF-Q_aem_XHT0YECaWbi43kcP2aWLCw&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7MvFYRuGEvRxWGPSfPVHLSgZLSfhpaCo8mV08gz1rc8dXvsC_OVZpY6cg6lQ_aem_t1LO5zJrSVY4DbXwA_O3vQ&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR44wSYqH5zdQVr7MuqQbJetYq6AKET40sC75PyQL5dCzrUR2Bq_yJMKevJ47Q_aem_EdLGYh6yUEn0KjFOUFN9xg&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NfOyAxVvOBCsnVT29Towyxl0Nu1sz3csZujuOKCRvsSiXDMncgtvoXbwF-Q_aem_XHT0YECaWbi43kcP2aWLCw&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7BoAZpjFEKP9Unle0hYKolxDQ7qZqUOQxerQibZzqfCSbXvUeSxgZSKu945kxXpWSb3uSPvaAJpK1ZwIzPtOFH_FY4Ra2Nafk9T5ZnKPn-j0RaqwVkGuTsWHH888TAswvBvKI9RkJHotEHffQPzJGZrDY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão