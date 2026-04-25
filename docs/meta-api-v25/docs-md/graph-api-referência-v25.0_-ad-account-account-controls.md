<!-- Fonte: Graph API Referência v25.0_ Ad Account Account Controls.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Account Controls

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Leitura


Get default fields on an [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) node associated with this [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account). Refer to the [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) reference for a list of these fields and their descriptions.


### Exemplo

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Faccount_controls&version=v25.0)
```
GET /v25.0/{ad-account-id}/account_controls HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/account_controls',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

```
/* make the API call */
FB.api(
    "/{ad-account-id}/account_controls",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{ad-account-id}/account_controls",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{ad-account-id}/account_controls"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
Se quiser saber como usar a Graph API, leia nosso [guia sobre Como usar a Graph API](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parâmetros

Este ponto de extremidade não tem nenhum parâmetro.

### Campos


A leitura desta borda retornará um resultado formatado em JSON:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

Uma lista de nós [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/).

#### `paging`

Para saber mais detalhes sobre paginação, consulte o [Guia da Graph API](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Erro | Descrição |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Criando

You can make a POST request to `account_controls` edge from the following paths:

- [`/act_{ad_account_id}/account_controls`](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/)
When posting to this edge, an [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) will be created.

### Parâmetros


| Parâmetro | Descrição |
| --- | --- |
| audience_controls JSON or object-like arrays | audience_controls Obrigatório |
| → age_min int64 |  |
| → geo_locations JSON or object-like arrays |  |
| → excluded_geo_locations JSON or object-like arrays |  |
| → exclusions JSON or object-like arrays |  |
| placement_controls JSON or object-like arrays | This field contains another field called placement_exclusion that provides information on which placements need to be excluded while targeting. All the other placements will be included. Each placement is denoted by a string that concatenates the publisher platform of the placement and a position inside the publisher platform, separated by an underscore. What is provided as parameter is a list of placements. For e.g. If we want to exclude the rewarded videos position from the audience network publisher platform, we provide the field as follows: { "placement_controls": { "placement_exclusions": ["audience_network_rewarded_video"] } } Only a few placements are allowed to be excluded: audience_network_classic (native, banner & interstitial positions of audience network) audience_network_rewarded_video (rewarded videos of audience network) audience_network_instream_video (instream videos of audience network) facebook_marketplace (marketplace section inside facebook) facebook_rhc (right hand column inside facebook) |
| → placement_exclusions array\<enum {AUDIENCE_NETWORK_CLASSIC, AUDIENCE_NETWORK_REWARDED_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO, FACEBOOK_MARKETPLACE, FACEBOOK_RIGHT_HAND_COLUMN}\> |  |
| → campaign_ids_to_set_ap array\<numeric string\> |  |


### Return Type

 Struct  {`id`: string, `success`: bool, `error_code`: string, `error_message`: string, }

### Error Codes


| Erro | Descrição |
| --- | --- |
| 100 | Invalid parameter |
| 2641 | Your ad includes or excludes locations that are currently restricted |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Atualizando


Use the [`POST /act_<AD_ACCOUNT_ID>/account_controls`](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Creating) endpoint to update the [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) associated with this [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account).
 Não é possível executar esta operação neste ponto de extremidade.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Excluindo

Não é possível executar esta operação neste ponto de extremidade.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)Nesta Página[Ad Account Account Controls](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#overview)[Leitura](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Reading)[Exemplo](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#exemplo)[Parâmetros](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#par-metros)[Campos](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#campos)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#error-codes)[Criando](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Creating)[Parâmetros](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#par-metros-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#error-codes-2)[Atualizando](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Updating)[Excluindo](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-0tvOzCiCTjYqEEZFQ7c3xVLUUjKejRTQ7nzYLX9rELntvlbIz3HmAML7NQ_aem_jRH4HJYQyr4XuUS4KtGI9g&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5CK2Hm3ltTrzqsIh4tBD2Ja9iCkrRmpdCvwrzvhvSjPpbX-i3VyIHKCp7dow_aem_ocsBKlzIkJU0Js9nS8w77A&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5o6FGWxr1Z1L3tKUJVJ4DcYWr4RsMYbRFLyi9SkTQKh6FTowXjfwOPSayMpQ_aem__G58ionng3n_jQCYGRecwQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58HRyim8sGN0bUYIgVXwMyYAZrsJ6MT0SGdCl_m8W09i1R8x8mD42_A8JBNw_aem_oz8HxTArWm0LOxME-OvvFw&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6eRtgHc_Zaqm0qaXlWQ7-IO_PR6wBQc1Hi_z95nLZE9QDBxkr7KwlF0r40_w_aem_JX1jBHunWk7IWyvXIVQNJQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6cwbozNPu59sImYRjptt5gV3mxitGzET0IbePXPzGt4rzrXvlwwLomhtvTfA_aem_WV37FUgqXkGfP_I9w_SALw&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-0tvOzCiCTjYqEEZFQ7c3xVLUUjKejRTQ7nzYLX9rELntvlbIz3HmAML7NQ_aem_jRH4HJYQyr4XuUS4KtGI9g&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58HRyim8sGN0bUYIgVXwMyYAZrsJ6MT0SGdCl_m8W09i1R8x8mD42_A8JBNw_aem_oz8HxTArWm0LOxME-OvvFw&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5rcFXs0MyooojJahSfV00lwXiUYt1hw-V7RSiai9cr-GGj4tVg_JXcDqboTw_aem_FqIZxVNcYMGN13Lt-voECQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-0tvOzCiCTjYqEEZFQ7c3xVLUUjKejRTQ7nzYLX9rELntvlbIz3HmAML7NQ_aem_jRH4HJYQyr4XuUS4KtGI9g&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6eRtgHc_Zaqm0qaXlWQ7-IO_PR6wBQc1Hi_z95nLZE9QDBxkr7KwlF0r40_w_aem_JX1jBHunWk7IWyvXIVQNJQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-0tvOzCiCTjYqEEZFQ7c3xVLUUjKejRTQ7nzYLX9rELntvlbIz3HmAML7NQ_aem_jRH4HJYQyr4XuUS4KtGI9g&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5noUIm-sgo_B6TLCbiPUBf7kpBZ7_rQ7ajXIY76PbyG81qqDwXWqYuM8ZnBA_aem_SYpVD13ke7oxn0xYwG_bxQ&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5CK2Hm3ltTrzqsIh4tBD2Ja9iCkrRmpdCvwrzvhvSjPpbX-i3VyIHKCp7dow_aem_ocsBKlzIkJU0Js9nS8w77A&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ZjLuZjZjjno6zBkDX1k9kvwEpvoEwZLrzKPuTSKyKLx2ypVmFyC_Vy9cjCw_aem_p_DqQmRKh84oufPLrf_0pg&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4uky1SMDqpFk8uSm2RfPcIDcDGCkkT6co5EiLsPzAz6F8TwV--pzcs466CoHmXrBB_wbffGQV7dGEkdMr4vCdymHiNUrJGXsRQRTaSXNZys1wDhDUxLvCLC2rskLMB09xH5J3zdeYqsar34QSJzoRaSzk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão