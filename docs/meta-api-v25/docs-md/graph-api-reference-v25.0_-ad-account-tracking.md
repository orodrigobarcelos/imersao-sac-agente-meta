<!-- Fonte: Graph API Reference v25.0_ Ad Account Tracking.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Tracking

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#)

## Reading


AdAccountTracking


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Ftracking&version=v25.0)
```
GET /v25.0/{ad-account-id}/tracking HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/tracking',
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
    "/{ad-account-id}/tracking",
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
    "/{ad-account-id}/tracking",
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
                               initWithGraphPath:@"/{ad-account-id}/tracking"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
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

A list of AdAccountTrackingData nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#)

## Creating

You can make a POST request to `tracking` edge from the following paths:

- [`/act_{ad_account_id}/tracking`](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/)
When posting to this edge, no Graph object will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| tracking_specs Object | Tracking specs to add to the account level Required |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node to which you POSTed. Struct  {`success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#)On This Page[Ad Account Tracking](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/tracking/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ked6bnpJXXknTz3a8qYlt1mzwbPsbWFltvPT9QVxBTq-_F86VfCqeobAAJw_aem_xdy_bbdglmwREC1POs-FBA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Ts36ScKcQPFQ29fO_WtR1BPrc6b1zLiRMlYIEGxx384yUvrsG34yhQ1qMhw_aem_xfivKJjtH7846oKi7ayWRg&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7hW2lfheaGXiN0ylSGS1I5-dpgi93WpV3A3NpoTXTp4QDSz1cgFWPznNbHJw_aem_G8ydKK2EjW7E9kMs3mYMWA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ked6bnpJXXknTz3a8qYlt1mzwbPsbWFltvPT9QVxBTq-_F86VfCqeobAAJw_aem_xdy_bbdglmwREC1POs-FBA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58gdrCTn4A4PISntYAZwIEczgRO4T_DXrfuORRTSLjyQI27mIU3Rf323TpIA_aem_HliaXfCVfGj1fWD9eUc7xw&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6f_BNycPmIJnfmPLCU_tD077jWfLy1f1j6TNTS2iimbg84YofvtZR7lzDYFg_aem_A51zsWlAgOVgIXdvvu3qbQ&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58gdrCTn4A4PISntYAZwIEczgRO4T_DXrfuORRTSLjyQI27mIU3Rf323TpIA_aem_HliaXfCVfGj1fWD9eUc7xw&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58gdrCTn4A4PISntYAZwIEczgRO4T_DXrfuORRTSLjyQI27mIU3Rf323TpIA_aem_HliaXfCVfGj1fWD9eUc7xw&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6f_BNycPmIJnfmPLCU_tD077jWfLy1f1j6TNTS2iimbg84YofvtZR7lzDYFg_aem_A51zsWlAgOVgIXdvvu3qbQ&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR47uLg08nsV5QYzkSxQlLk_ianxShDmi_FkJkAaupE3CSRtOthhyBv3loewUA_aem_uiN5deyEq6TU61eHjZEBhg&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ngaRcOnKSTQdU7iPby8SvKaFi4vDx7M5Uwwi_9bMVCYfZuRBItFARUu72Hg_aem_D2tDA47F0Obn2xxGxz1B0w&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Ts36ScKcQPFQ29fO_WtR1BPrc6b1zLiRMlYIEGxx384yUvrsG34yhQ1qMhw_aem_xfivKJjtH7846oKi7ayWRg&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6aDHaxw-4hCpJBpFomREnCoGfzzaSHeefL56IdE4T6mCTtRavSH6lhjC4k7w_aem_FRWk1jJoAcx35n3YLTc3xA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7hW2lfheaGXiN0ylSGS1I5-dpgi93WpV3A3NpoTXTp4QDSz1cgFWPznNbHJw_aem_G8ydKK2EjW7E9kMs3mYMWA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58gdrCTn4A4PISntYAZwIEczgRO4T_DXrfuORRTSLjyQI27mIU3Rf323TpIA_aem_HliaXfCVfGj1fWD9eUc7xw&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Btq_P2dbY_mY_S6wlyiZqNxmKuFvfmgtLlw1x_bquSlqW2HB4FXjZ72o7uQ_aem_jW-IuQpS832A14_WxwxnNQ&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ghsfxxBXlplgdlolzFL4Qu2AeEgUlYXGpYGNGfiXwW9sINvDh0OmGvIsSvA_aem_UXNpjHDSR7JjRHRKFWV2BA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ked6bnpJXXknTz3a8qYlt1mzwbPsbWFltvPT9QVxBTq-_F86VfCqeobAAJw_aem_xdy_bbdglmwREC1POs-FBA&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6f_BNycPmIJnfmPLCU_tD077jWfLy1f1j6TNTS2iimbg84YofvtZR7lzDYFg_aem_A51zsWlAgOVgIXdvvu3qbQ&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Ts36ScKcQPFQ29fO_WtR1BPrc6b1zLiRMlYIEGxx384yUvrsG34yhQ1qMhw_aem_xfivKJjtH7846oKi7ayWRg&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7DGlPSKlWVU1IupTJRQ_3O1qYkWG8OtjRiXWZ-HdKioaracBnMSxNDmfp_g6fxIJ7A2S4fwEd7biIlpcE2JY8wrhoU3741VE3Wms1RQ-e6xtvWd3Bb2AmKnyF7PhAk0gCX1g3FbpbEI0-dpt31GwDXiWE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo