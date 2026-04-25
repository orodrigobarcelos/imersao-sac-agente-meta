<!-- Fonte: Graph API Reference v25.0_ Ad Account Adspixelss.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Adspixels

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)

## Reading


ad account to ads pixels edge


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CPIXEL_ID%3E%2F%3Ffields%3Dcode&version=v25.0)
```
GET /v25.0/<PIXEL_ID>/?fields=code HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/<PIXEL_ID>/?fields=code',
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
    "/<PIXEL_ID>/",
    {
        "fields": "code"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
Bundle params = new Bundle();
params.putString("fields", "code");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<PIXEL_ID>/",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
NSDictionary *params = @{
  @"fields": @"code",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<PIXEL_ID>/"
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
  -d 'fields="code"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PIXEL_ID>/
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {},
    "summary": {}
}
```


#### `data`

A list of [AdsPixel](https://developers.facebook.com/docs/marketing-api/reference/ads-pixel/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).


| Field | Description |
| --- | --- |
| total_count int32 | Total number of objects on this edge Default |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)

## Creating

You can make a POST request to `adspixels` edge from the following paths:

- [`/act_{ad_account_id}/adspixels`](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/)
When posting to this edge, an [AdsPixel](https://developers.facebook.com/docs/marketing-api/reference/ads-pixel/) will be created.

### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fadspixels%3Fname%3DMy%2BWCA%2BPixel&version=v25.0)
```
POST /v25.0/act_<AD_ACCOUNT_ID>/adspixels HTTP/1.1
Host: graph.facebook.com

name=My+WCA+Pixel
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/adspixels',
    array (
      'name' => 'My WCA Pixel',
    ),
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
    "/act_<AD_ACCOUNT_ID>/adspixels",
    "POST",
    {
        "name": "My WCA Pixel"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
Bundle params = new Bundle();
params.putString("name", "My WCA Pixel");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/adspixels",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
NSDictionary *params = @{
  @"name": @"My WCA Pixel",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/adspixels"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X POST \
  -F 'name="My WCA Pixel"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adspixels
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| name string | Name of the pixel |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 6202 | More than one pixel exist for this account |
| 6200 | A pixel already exists for this account |
| 100 | Invalid parameter |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)On This Page[Ad Account Adspixels](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Creating)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#example-2)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UqCPZiF2x5FX-anNPItmaE3y8e9JDSGqoIrvWGhWfe9tT35n86dfg2z3Rhw_aem_5Q0kbD3Zs-oJEkz1pP5hvA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UqCPZiF2x5FX-anNPItmaE3y8e9JDSGqoIrvWGhWfe9tT35n86dfg2z3Rhw_aem_5Q0kbD3Zs-oJEkz1pP5hvA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5k2P1yd7z73Rw5Pv6OkSTnhpfyaTPfjVFm1M1eCDF7mY3FQEiOcsBJXinshg_aem_ZOk7MtGjGKUHP-q15TqGdw&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5-DDOCo9k8vQpqXVZU7wTZUpLpC_bVRWxUgeI_X4j4a8tdg8MC-gsFCPoL5A_aem_72WaKYGPWi_1W6uO4rnMZA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5CuAsg7ugdBY0576J-FJk_V1TInnwQSgEPuGO4FZidXo-wUfXLu5odnh8HZA_aem_FlW1JKYhMCosUUJTGliY9A&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5CuAsg7ugdBY0576J-FJk_V1TInnwQSgEPuGO4FZidXo-wUfXLu5odnh8HZA_aem_FlW1JKYhMCosUUJTGliY9A&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5-DDOCo9k8vQpqXVZU7wTZUpLpC_bVRWxUgeI_X4j4a8tdg8MC-gsFCPoL5A_aem_72WaKYGPWi_1W6uO4rnMZA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UqCPZiF2x5FX-anNPItmaE3y8e9JDSGqoIrvWGhWfe9tT35n86dfg2z3Rhw_aem_5Q0kbD3Zs-oJEkz1pP5hvA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4HSpDhMFRAoxjHT25hew9AdC0uuaI3eiVC5sHhqWD8sEpu6F9QcHcpJw1AQw_aem_RSfhhpg9038IGetx3fgN4w&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5k2P1yd7z73Rw5Pv6OkSTnhpfyaTPfjVFm1M1eCDF7mY3FQEiOcsBJXinshg_aem_ZOk7MtGjGKUHP-q15TqGdw&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UqCPZiF2x5FX-anNPItmaE3y8e9JDSGqoIrvWGhWfe9tT35n86dfg2z3Rhw_aem_5Q0kbD3Zs-oJEkz1pP5hvA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR78o-g_Sm8Rq6j8FaGcrRPcmuT5PpHPRBlPE9wM0i2LeWbPzEfNw0wvVRaKoA_aem_q3s02Ufr9rDYD7ZwiUm0pQ&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR78o-g_Sm8Rq6j8FaGcrRPcmuT5PpHPRBlPE9wM0i2LeWbPzEfNw0wvVRaKoA_aem_q3s02Ufr9rDYD7ZwiUm0pQ&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6zB20SPeIm3Tbsy78DJjKNecQlK9vU2oZKdU12kAIJTv_caT52H_TcL_E7UA_aem_gtSGwkjPqeTIthEQCk6bnQ&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5jenJBQ3jqN7bDuIFHWkSOs-jxfyPLLolwHk4WRawZIOpOvKwOEQV4pTL8ng_aem_JYtWHesnyvT_TZ3t9pMXgg&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5PHOiQUew9OK7GAZq2TdYOMymKyHyAZ28c1-WbgF2IblB91AMNXYvfaLw73w_aem_p1saC71f3dE31hFY2UYVFA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UqCPZiF2x5FX-anNPItmaE3y8e9JDSGqoIrvWGhWfe9tT35n86dfg2z3Rhw_aem_5Q0kbD3Zs-oJEkz1pP5hvA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5jenJBQ3jqN7bDuIFHWkSOs-jxfyPLLolwHk4WRawZIOpOvKwOEQV4pTL8ng_aem_JYtWHesnyvT_TZ3t9pMXgg&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5-DDOCo9k8vQpqXVZU7wTZUpLpC_bVRWxUgeI_X4j4a8tdg8MC-gsFCPoL5A_aem_72WaKYGPWi_1W6uO4rnMZA&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5jenJBQ3jqN7bDuIFHWkSOs-jxfyPLLolwHk4WRawZIOpOvKwOEQV4pTL8ng_aem_JYtWHesnyvT_TZ3t9pMXgg&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5OVdJjzxKFLYk1sRSfwqyttCfcUdmReyppgZd8Sa95MKgy2CAwPrR0haQfHAET6iKETB8YdqtZNQ44NHJRJqeDWU--Bod4D7lMfsQWj5IH9Q2Exi1Vz2eT_7Qew2-6haP1hckEoZIS2t1nTacPbD7HEd8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo