<!-- Fonte: Graph API Reference v25.0_ Ad Account Adspixels.html -->
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

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#)On This Page[Ad Account Adspixels](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Creating)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#example-2)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/adspixels/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4CjZNaV19CpLI8h9vfmFNUqrgwRlxBk31ryvCN1pERX8XoUNsTfk-pv69AJA_aem_fKs6gztZdWdHecoFil-6yQ&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4x-3evR5FlMaeoNqybsimaUQ0oM23F5miT55OsAWRWiMItSPkiiryWCIAVLA_aem_0me-k9rRiRYIjSGl5jy-Wg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Zv3r0BzV2lOW6PHX5T_urH4isJkaAM6EvM7lUWDShku3eLZYmdhh-NcNcVA_aem_TkhIUgmsvAtGY-GZ4p0RXg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4x-3evR5FlMaeoNqybsimaUQ0oM23F5miT55OsAWRWiMItSPkiiryWCIAVLA_aem_0me-k9rRiRYIjSGl5jy-Wg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR45iMt1O-cyZX4U0xmqqoHfJWfsVjIpjm3WYv_M85gJhETprOHgNFbEOGQsrw_aem_jDj5v9snPbFH813yx63v7g&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5_DvRRmI9evVTXO-nLapbljK0A4knHdt5TCyD44Bsg-hoartuJYr82EfibSQ_aem_oaSb2_GMAKgVl0Koxn6P2w&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4CjZNaV19CpLI8h9vfmFNUqrgwRlxBk31ryvCN1pERX8XoUNsTfk-pv69AJA_aem_fKs6gztZdWdHecoFil-6yQ&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5_DvRRmI9evVTXO-nLapbljK0A4knHdt5TCyD44Bsg-hoartuJYr82EfibSQ_aem_oaSb2_GMAKgVl0Koxn6P2w&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5_DvRRmI9evVTXO-nLapbljK0A4knHdt5TCyD44Bsg-hoartuJYr82EfibSQ_aem_oaSb2_GMAKgVl0Koxn6P2w&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Ces6zGQaITMd7ZHPxlz8lJap103Y4tVrgBZ_SFhS6b5cu0nuch5OPZ1xQ5A_aem_Jy5e6nzSknGq4nPmgsdjZg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Ces6zGQaITMd7ZHPxlz8lJap103Y4tVrgBZ_SFhS6b5cu0nuch5OPZ1xQ5A_aem_Jy5e6nzSknGq4nPmgsdjZg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4CjZNaV19CpLI8h9vfmFNUqrgwRlxBk31ryvCN1pERX8XoUNsTfk-pv69AJA_aem_fKs6gztZdWdHecoFil-6yQ&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Zv3r0BzV2lOW6PHX5T_urH4isJkaAM6EvM7lUWDShku3eLZYmdhh-NcNcVA_aem_TkhIUgmsvAtGY-GZ4p0RXg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4x-3evR5FlMaeoNqybsimaUQ0oM23F5miT55OsAWRWiMItSPkiiryWCIAVLA_aem_0me-k9rRiRYIjSGl5jy-Wg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6GdiPOoZcAPIYdwSb3_ARcPTo5aF1dS1Y4brI6SuK84yjnQUPDDNSHn5iWfg_aem_mEq7vmea9KVHqr3YmAY1GA&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Ces6zGQaITMd7ZHPxlz8lJap103Y4tVrgBZ_SFhS6b5cu0nuch5OPZ1xQ5A_aem_Jy5e6nzSknGq4nPmgsdjZg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5_DvRRmI9evVTXO-nLapbljK0A4knHdt5TCyD44Bsg-hoartuJYr82EfibSQ_aem_oaSb2_GMAKgVl0Koxn6P2w&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4x-3evR5FlMaeoNqybsimaUQ0oM23F5miT55OsAWRWiMItSPkiiryWCIAVLA_aem_0me-k9rRiRYIjSGl5jy-Wg&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5l6FcYW5fhgMiP7ZTfPQhh85e4G1FgFncVGYujja7mOBvHJO8RUpQaG6m3_Q_aem_fVIX0q-CMk1UPTjSCK65tQ&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR45iMt1O-cyZX4U0xmqqoHfJWfsVjIpjm3WYv_M85gJhETprOHgNFbEOGQsrw_aem_jDj5v9snPbFH813yx63v7g&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5nrMtb7qtJfUl8mQb-WPKibKYXNNYDgFmzlnktgScr3SOyJoSE5g70tYBS1XKaBtVv8u8eLtw34uS_WMNhSrS2zDHtbq_lCyg21SYTXz6YGy-p932TeT4zNT4A_xDtN3embtU-t7xYxTvDetyWugMcOek)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo