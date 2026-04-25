<!-- Fonte: Graph API Reference v25.0_ Ad Leads.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Leads

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)

Any leads associated with with a Lead Ad. Since these leads belong to a business' Page, not the ad itself, you need to be a Page Admin to access these. Alternately you can have permissions granted to you by the Page Admin. See [Retrieving Leads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving).
[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)

## Reading


GraphAdgroupLeadsEdge


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Badgroup-id%7D%2Fleads&version=v25.0)
```
GET /v25.0/{adgroup-id}/leads HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{adgroup-id}/leads',
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
    "/{adgroup-id}/leads",
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
    "/{adgroup-id}/leads",
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
                               initWithGraphPath:@"/{adgroup-id}/leads"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X GET -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/{adgroup-id}/leads
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [UserLeadGenInfo](https://developers.facebook.com/docs/marketing-api/reference/user-lead-gen-info/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 104 | Incorrect signature |

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#)On This Page[Ad Leads](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/adgroup/leads/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7wtXHhImJcoWa5Ni81INmgy6Hf6l9Q-QAjGy29i-w-pW27D4UXZxGwb5OHRA_aem_RKTgSom-1yAU1brhHQJDIg&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fHL3sxwDhDCIgXN3EAfGNplGUEfcB4nJ8eQZuCkC9RR_ndAXQ8Vd8wM_deg_aem_TBjUe4SNfFqhipU4mv2DIw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fHL3sxwDhDCIgXN3EAfGNplGUEfcB4nJ8eQZuCkC9RR_ndAXQ8Vd8wM_deg_aem_TBjUe4SNfFqhipU4mv2DIw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7wtXHhImJcoWa5Ni81INmgy6Hf6l9Q-QAjGy29i-w-pW27D4UXZxGwb5OHRA_aem_RKTgSom-1yAU1brhHQJDIg&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7wtXHhImJcoWa5Ni81INmgy6Hf6l9Q-QAjGy29i-w-pW27D4UXZxGwb5OHRA_aem_RKTgSom-1yAU1brhHQJDIg&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7-ViSL0_Y-mSzFLGV0i8fWcPQpBoPhRhTpoX_pVWjBNsEOoHU9GeMxgNLF1w_aem_9Ct2B6IlcTaC0qiaWsG3qQ&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5cX9tEBBYRNz6j7Gna8xJG2J9Qy0X5KyqfgeARlLTVm4l66vpSwPkxGoScGA_aem_Rj-2TXD_Diytd2DRmq527A&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7-ViSL0_Y-mSzFLGV0i8fWcPQpBoPhRhTpoX_pVWjBNsEOoHU9GeMxgNLF1w_aem_9Ct2B6IlcTaC0qiaWsG3qQ&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63tTAMOF2OOqzdCqXMSMLoNX1zGUXzI6HMTKzRnEpoFniJkyonaGqgM7PBQw_aem_xhsxs5k_MFMRGRphBo2EsA&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7-ViSL0_Y-mSzFLGV0i8fWcPQpBoPhRhTpoX_pVWjBNsEOoHU9GeMxgNLF1w_aem_9Ct2B6IlcTaC0qiaWsG3qQ&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7DYMy1vYBAeTdMI_pQt-AkuXyi_bMoTE2LxDN27zkmxn6LGkaLMGkVZakHsQ_aem_luvJo12UnjTKr04ZT4iO2Q&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63tTAMOF2OOqzdCqXMSMLoNX1zGUXzI6HMTKzRnEpoFniJkyonaGqgM7PBQw_aem_xhsxs5k_MFMRGRphBo2EsA&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7-ViSL0_Y-mSzFLGV0i8fWcPQpBoPhRhTpoX_pVWjBNsEOoHU9GeMxgNLF1w_aem_9Ct2B6IlcTaC0qiaWsG3qQ&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5cX9tEBBYRNz6j7Gna8xJG2J9Qy0X5KyqfgeARlLTVm4l66vpSwPkxGoScGA_aem_Rj-2TXD_Diytd2DRmq527A&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5F2gmTe0agRScGlBjunuqF7ZoKbvZgPmsx9HOfsXfGFUBA3hYeUHTCUKmPsw_aem_AppX4z44LCw7f7T1ZbSEOw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5bAOCuVZm9p4EQDDUlDKNT7v0mgQCPGZFARbAFH-qY4O_MujvBkVigbQ1aAg_aem_jXRiXGBfUYgFz54cKeYFIw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7-ViSL0_Y-mSzFLGV0i8fWcPQpBoPhRhTpoX_pVWjBNsEOoHU9GeMxgNLF1w_aem_9Ct2B6IlcTaC0qiaWsG3qQ&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5F2gmTe0agRScGlBjunuqF7ZoKbvZgPmsx9HOfsXfGFUBA3hYeUHTCUKmPsw_aem_AppX4z44LCw7f7T1ZbSEOw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4mQGNWAJ2aDruZwGhv6cXuAO1wxdDCtXgTKStcVuExkSekhgdl7zxRWRwwsA_aem_ZLHFmb1a5RnTZ21-36_MqA&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5bAOCuVZm9p4EQDDUlDKNT7v0mgQCPGZFARbAFH-qY4O_MujvBkVigbQ1aAg_aem_jXRiXGBfUYgFz54cKeYFIw&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5ez9p8s2R-0hLTHFtmIHbWrPGxJOBnENq0p35dyA8RmtH4GEnUXpHwOkgn6Bg1K2sCugGVqrnT4VOngemzuAH-3emfe9g_JMsKoWVPAO4u41RPnpyDyEzt9LGHEFDKVs8fEiJbryCR53COcdCAruFLLEI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo