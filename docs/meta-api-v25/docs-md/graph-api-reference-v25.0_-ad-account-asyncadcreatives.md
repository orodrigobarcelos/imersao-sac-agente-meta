<!-- Fonte: Graph API Reference v25.0_ Ad Account Asyncadcreatives.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Asyncadcreatives

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#)

## Reading


Async ad creative jobs from this Ad Account.


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fasyncadcreatives&version=v25.0)
```
GET /v25.0/{ad-account-id}/asyncadcreatives HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/asyncadcreatives',
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
    "/{ad-account-id}/asyncadcreatives",
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
    "/{ad-account-id}/asyncadcreatives",
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
                               initWithGraphPath:@"/{ad-account-id}/asyncadcreatives"
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


| Parameter | Description |
| --- | --- |
| is_completed boolean | If true , we only return completed ad request sets. |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [AdAsyncRequestSet](https://developers.facebook.com/docs/marketing-api/asyncrequests/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#)

## Creating

You can make a POST request to `asyncadcreatives` edge from the following paths:

- [`/act_{ad_account_id}/asyncadcreatives`](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/)
When posting to this edge, no Graph object will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| creative_spec AdCreative | Specs for ad creative Required Supports Emoji |
| name UTF-8 encoded string | Name of async job Required |
| notification_mode enum{OFF, ON_COMPLETE} | Specify 0 for no notifications and 1 for notification on completion. |
| notification_uri URL | If notifications are enabled, specify the URL to send them. |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#)On This Page[Ad Account Asyncadcreatives](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/asyncadcreatives/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR55j4jioNQrraptLPD6ugK63aYKiByPArzll2dbPy6BvOkqZrZygZ7ErPaIAg_aem_SVBi7jnyXDqNXQzrihI0pQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6jaG_eyTxQSgMwdg_fD4V3saoB9Zy9MfSCYqrAdKs7ufTmTHduDxUtslZrrQ_aem_gI-bkbnTbBVOchwzxACiiA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7F9z_OWHMSQTmtOpGlQ6yi8gC-1OoFiVrEwPujhGlxzLAmynE7kwiS5vO6Ag_aem_DeLYtkfNxOOM0MxP8TmKBg&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR54edy-RI5x73BkY06Fyb8c98kh28up__bHdP_1LM7LQkN2d1wuvAd_RdpeTw_aem_cnrlcFaAOjVzpw3w3WZEhA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR64ZMlLzzOxzUJlNme95l3KbSA3RzVNPr-R0odDSWWzQJG6Rj-CiVtmIWUZQA_aem_v1twK6ZoYrHT7-fdoyFXTQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7F9z_OWHMSQTmtOpGlQ6yi8gC-1OoFiVrEwPujhGlxzLAmynE7kwiS5vO6Ag_aem_DeLYtkfNxOOM0MxP8TmKBg&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7aQ_3KQaDey8Xy86X4F6eWn-PC5mYXh1_ZahjeKM6RNYFag-wCkl9a0aUwyg_aem_gRUvQ-R6X6yj6AuGp1LQjw&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ZywR3R6eqpEuYYi5msFqV2gWpZnUpHvsVTxApO1mQ9_Gc7UgVCccCOkhzoQ_aem_d0Z1npzV_PJsiE1OTWT6QQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ZywR3R6eqpEuYYi5msFqV2gWpZnUpHvsVTxApO1mQ9_Gc7UgVCccCOkhzoQ_aem_d0Z1npzV_PJsiE1OTWT6QQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR55j4jioNQrraptLPD6ugK63aYKiByPArzll2dbPy6BvOkqZrZygZ7ErPaIAg_aem_SVBi7jnyXDqNXQzrihI0pQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR64ZMlLzzOxzUJlNme95l3KbSA3RzVNPr-R0odDSWWzQJG6Rj-CiVtmIWUZQA_aem_v1twK6ZoYrHT7-fdoyFXTQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR54edy-RI5x73BkY06Fyb8c98kh28up__bHdP_1LM7LQkN2d1wuvAd_RdpeTw_aem_cnrlcFaAOjVzpw3w3WZEhA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7F9z_OWHMSQTmtOpGlQ6yi8gC-1OoFiVrEwPujhGlxzLAmynE7kwiS5vO6Ag_aem_DeLYtkfNxOOM0MxP8TmKBg&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6jaG_eyTxQSgMwdg_fD4V3saoB9Zy9MfSCYqrAdKs7ufTmTHduDxUtslZrrQ_aem_gI-bkbnTbBVOchwzxACiiA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR55j4jioNQrraptLPD6ugK63aYKiByPArzll2dbPy6BvOkqZrZygZ7ErPaIAg_aem_SVBi7jnyXDqNXQzrihI0pQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ZywR3R6eqpEuYYi5msFqV2gWpZnUpHvsVTxApO1mQ9_Gc7UgVCccCOkhzoQ_aem_d0Z1npzV_PJsiE1OTWT6QQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7aQ_3KQaDey8Xy86X4F6eWn-PC5mYXh1_ZahjeKM6RNYFag-wCkl9a0aUwyg_aem_gRUvQ-R6X6yj6AuGp1LQjw&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6jaG_eyTxQSgMwdg_fD4V3saoB9Zy9MfSCYqrAdKs7ufTmTHduDxUtslZrrQ_aem_gI-bkbnTbBVOchwzxACiiA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR67Me7ztpHLcio0Gc8KLm_K3LS2i53SuFNm3zGW_cJomlHyRlIq1l7CzjV-HA_aem_FR-NdvCy1s-RVLyrJmIZxA&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ZywR3R6eqpEuYYi5msFqV2gWpZnUpHvsVTxApO1mQ9_Gc7UgVCccCOkhzoQ_aem_d0Z1npzV_PJsiE1OTWT6QQ&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5yF8jEPemVNPvAZDLPvVnumA1EPZKgtQhEYJvlPUIVRVjgb-cU1ib3njBFsifkBSaWFsIHyGzaWhpYljlXiIGz0TOJ4X1Cc-okGET51oAFCnqutxWt3ifEHF65nP3W--bzdYgizKMEvl3KCx6rcWQ9AHE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo