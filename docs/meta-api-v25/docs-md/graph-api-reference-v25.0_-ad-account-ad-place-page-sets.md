<!-- Fonte: Graph API Reference v25.0_ Ad Account Ad Place Page Sets.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Ad Place Page Sets

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)

This endpoint applies to published Pages.
[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)

## Reading


The endpoint to retrieve a list of place_page_sets for an ad_account


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fad_place_page_sets&version=v25.0)
```
GET /v25.0/{ad-account-id}/ad_place_page_sets HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/ad_place_page_sets',
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
    "/{ad-account-id}/ad_place_page_sets",
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
    "/{ad-account-id}/ad_place_page_sets",
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
                               initWithGraphPath:@"/{ad-account-id}/ad_place_page_sets"
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
    "paging": {},
    "summary": {}
}
```


#### `data`

A list of [AdPlacePageSet](https://developers.facebook.com/docs/marketing-api/reference/ad-place-page-set/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).


| Field | Description |
| --- | --- |
| total_count unsigned int32 | Total number of page sets in the ad account |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)

## Creating

You can make a POST request to `ad_place_page_sets` edge from the following paths:

- [`/act_{ad_account_id}/ad_place_page_sets`](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/)
When posting to this edge, an [AdPlacePageSet](https://developers.facebook.com/docs/marketing-api/reference/ad-place-page-set/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| location_types list\<enum {recent, home}\> | Type of user location the page set targets (e.g., 'recent', 'home') |
| name string | Name of The Place PageSet Required |
| parent_page numeric string or integer | The parent page ID for all the locations pages Required |
| targeted_area_type enum {CUSTOM_RADIUS, MARKETING_AREA, NONE} | Criteria to define area targeted by the page set |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#)On This Page[Ad Account Ad Place Page Sets](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/ad_place_page_sets/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6l6yPE2Qqze7mA305Fdjr8yrNqzwllC4jlAt4KFU8hI7R5_pW1wltRKRPo4g_aem_juGPIGA9ZEnuTeXBUgBNDw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Ih-6BnhMUsL4VFOqHRR38K8OnUe4JUnlk-mlRbG6-1X23w2JgCMMa-gpfrA_aem_8OhthFua7SiPw4Gt0mBUwQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5SOjr0UxiOLKWAA1kGprFxVc6ZdffAuvamd2YF5S4FmDvS_BNO0k-Ks5AwAg_aem_RXXp3Bu1A7XrpqJNyFtPtw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Ih-6BnhMUsL4VFOqHRR38K8OnUe4JUnlk-mlRbG6-1X23w2JgCMMa-gpfrA_aem_8OhthFua7SiPw4Gt0mBUwQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Ih-6BnhMUsL4VFOqHRR38K8OnUe4JUnlk-mlRbG6-1X23w2JgCMMa-gpfrA_aem_8OhthFua7SiPw4Gt0mBUwQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5SOjr0UxiOLKWAA1kGprFxVc6ZdffAuvamd2YF5S4FmDvS_BNO0k-Ks5AwAg_aem_RXXp3Bu1A7XrpqJNyFtPtw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63ZqWnfxKN17YBbdDtJ3scodo-vcH67PFJktdw36gHUHJ8VxqNxsHeGwMKrQ_aem_qx6is31yIXHqK_kSPzoYVQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Ih-6BnhMUsL4VFOqHRR38K8OnUe4JUnlk-mlRbG6-1X23w2JgCMMa-gpfrA_aem_8OhthFua7SiPw4Gt0mBUwQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5O34vHw6ydyxahp0IJVMWEviMne38gK-7odO6vj6q8oxU0bPjXee7jxQTs0g_aem_HXXtGboKGnlTb0DMAJ7b6Q&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5xRIK1brFrpwTa7cHmxagvwcCSD1cy3kI9duHejYL-BjVtKMhte6TGZiiE2w_aem_T_7dDHvQycSZXd2-QG7n5A&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5xRIK1brFrpwTa7cHmxagvwcCSD1cy3kI9duHejYL-BjVtKMhte6TGZiiE2w_aem_T_7dDHvQycSZXd2-QG7n5A&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR78YhZilylWLoYMRAVZgw_L9CwXjtHmI-6b9Rgd7CmA9s0eQxMUXj0uvoy-HA_aem_nJWxVyAgl9moQJw3FnGi7g&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Ih-6BnhMUsL4VFOqHRR38K8OnUe4JUnlk-mlRbG6-1X23w2JgCMMa-gpfrA_aem_8OhthFua7SiPw4Gt0mBUwQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-hUE3-VYkvNdkuF_CFWvNyfcH7qQCGcOB4UayhwAIyw913wcuJsxyrETZA_aem_52wgDSlNw4NmGuMjtt6AAQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63ZqWnfxKN17YBbdDtJ3scodo-vcH67PFJktdw36gHUHJ8VxqNxsHeGwMKrQ_aem_qx6is31yIXHqK_kSPzoYVQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5SOjr0UxiOLKWAA1kGprFxVc6ZdffAuvamd2YF5S4FmDvS_BNO0k-Ks5AwAg_aem_RXXp3Bu1A7XrpqJNyFtPtw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5xRIK1brFrpwTa7cHmxagvwcCSD1cy3kI9duHejYL-BjVtKMhte6TGZiiE2w_aem_T_7dDHvQycSZXd2-QG7n5A&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5SOjr0UxiOLKWAA1kGprFxVc6ZdffAuvamd2YF5S4FmDvS_BNO0k-Ks5AwAg_aem_RXXp3Bu1A7XrpqJNyFtPtw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5SOjr0UxiOLKWAA1kGprFxVc6ZdffAuvamd2YF5S4FmDvS_BNO0k-Ks5AwAg_aem_RXXp3Bu1A7XrpqJNyFtPtw&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-hUE3-VYkvNdkuF_CFWvNyfcH7qQCGcOB4UayhwAIyw913wcuJsxyrETZA_aem_52wgDSlNw4NmGuMjtt6AAQ&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5evESLAM10gClL5-uTbj3OHUVytOwkWadDr5OV9iTFcxBrJlXZoPe3kMRv6cNb62_RZS19AwRyVCpBQv-Gu3zxt_aVZLUjiYUeU6qamkYgVYWEVLESjgpVPsSZU01-kj-znHhceIFbB4oH5f7L8Puj2Y8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo