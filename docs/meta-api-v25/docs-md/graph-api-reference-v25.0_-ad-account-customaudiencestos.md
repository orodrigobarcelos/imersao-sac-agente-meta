<!-- Fonte: Graph API Reference v25.0_ Ad Account Customaudiencestos.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Customaudiencestos

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#)

## Reading


AdAccountCustomAudiencesTOS


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fcustomaudiencestos&version=v25.0)
```
GET /v25.0/{ad-account-id}/customaudiencestos HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/customaudiencestos',
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
    "/{ad-account-id}/customaudiencestos",
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
    "/{ad-account-id}/customaudiencestos",
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
                               initWithGraphPath:@"/{ad-account-id}/customaudiencestos"
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

A list of [CustomAudiencesTOS](https://developers.facebook.com/docs/marketing-api/custom-audience-targeting/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#)

## Creating

You can make a POST request to `customaudiencestos` edge from the following paths:

- [`/act_{ad_account_id}/customaudiencestos`](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/)
When posting to this edge, no Graph object will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| business_id string | SELF_EXPLANATORY |
| tos_id string | SELF_EXPLANATORY Required |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node to which you POSTed. Struct  {`success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#)On This Page[Ad Account Customaudiencestos](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiencestos/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Cwoe0UrsoUiESEB9r1n8nuKpwRuiG3K8gNDsXzVIFZ4nS-xQIjVZsltB0tQ_aem_Q-HwimHd2g6DWPEVyS_S3w&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5aI59BUFFKwnE5Wi0aMNZOTJp1vAWc5FC5i-vhy9nIlLc52UJP7WW1NlWkag_aem_PmrZ-guKUgvmFfB2ChM5pw&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77M9XFqh047gfND6hBTDsFQu4KYUVorG7FsL5WavWd5JVb5M7acodiAuYypA_aem_kRa2uRiys4lajBNCWunOkA&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77M9XFqh047gfND6hBTDsFQu4KYUVorG7FsL5WavWd5JVb5M7acodiAuYypA_aem_kRa2uRiys4lajBNCWunOkA&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6q7YuprXqCG09iLoomys7h4bDSS4B1MKIyRGnVfIp4SUTfpgh5TNzvtfO4Ww_aem_wvyd_7djMZrmLiOJ7LmdCg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eKRjOR-Y57sZdUpxqawEMmVAzH7LKucbAx9skRIjAKWpfLTrU_QDEm0WWeA_aem_8gBPkS2kdTvny7JMmZnWAQ&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eKRjOR-Y57sZdUpxqawEMmVAzH7LKucbAx9skRIjAKWpfLTrU_QDEm0WWeA_aem_8gBPkS2kdTvny7JMmZnWAQ&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4wBeUemSIucD964uO5ms-tibzkz6Hecvd4LT5K_oWBL1X2VkSjOpTIi796-g_aem_AZQiGwB1nWkz-CYlZqY-Cw&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR56VMFxrCQqO8tUhGvBA-ZBTxCXcoOx-txtSQCPwhF9eGkC8RJHAG7FiWLs8w_aem_U0soQsWdKBsCWBvyUZwodg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6q7YuprXqCG09iLoomys7h4bDSS4B1MKIyRGnVfIp4SUTfpgh5TNzvtfO4Ww_aem_wvyd_7djMZrmLiOJ7LmdCg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6q7YuprXqCG09iLoomys7h4bDSS4B1MKIyRGnVfIp4SUTfpgh5TNzvtfO4Ww_aem_wvyd_7djMZrmLiOJ7LmdCg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7uoV54oBEkqh66M7ilmwdldOZ1RS8z7j6UY5sOCyCGZFwYPg0NrnbLp-NaeQ_aem_cNMVvv5IDRfjUyoeip3VmQ&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Cwoe0UrsoUiESEB9r1n8nuKpwRuiG3K8gNDsXzVIFZ4nS-xQIjVZsltB0tQ_aem_Q-HwimHd2g6DWPEVyS_S3w&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Cwoe0UrsoUiESEB9r1n8nuKpwRuiG3K8gNDsXzVIFZ4nS-xQIjVZsltB0tQ_aem_Q-HwimHd2g6DWPEVyS_S3w&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77M9XFqh047gfND6hBTDsFQu4KYUVorG7FsL5WavWd5JVb5M7acodiAuYypA_aem_kRa2uRiys4lajBNCWunOkA&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR56VMFxrCQqO8tUhGvBA-ZBTxCXcoOx-txtSQCPwhF9eGkC8RJHAG7FiWLs8w_aem_U0soQsWdKBsCWBvyUZwodg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7uoV54oBEkqh66M7ilmwdldOZ1RS8z7j6UY5sOCyCGZFwYPg0NrnbLp-NaeQ_aem_cNMVvv5IDRfjUyoeip3VmQ&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5aI59BUFFKwnE5Wi0aMNZOTJp1vAWc5FC5i-vhy9nIlLc52UJP7WW1NlWkag_aem_PmrZ-guKUgvmFfB2ChM5pw&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6q7YuprXqCG09iLoomys7h4bDSS4B1MKIyRGnVfIp4SUTfpgh5TNzvtfO4Ww_aem_wvyd_7djMZrmLiOJ7LmdCg&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5aI59BUFFKwnE5Wi0aMNZOTJp1vAWc5FC5i-vhy9nIlLc52UJP7WW1NlWkag_aem_PmrZ-guKUgvmFfB2ChM5pw&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5hPuGKl5z86Hf-e4l9sMT6H4o5SKZBWBzwyECcq7CpZoFlbCV1flWOpJPOjavWrb8K14xw-EkSPt_qNmyHhgsnjpvZQ1icbRePcKUfrpoG0iP23URYLA3k0TI682ZX5dnLke_ph6HRxPnfugUXGWTUMhk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo