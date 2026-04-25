<!-- Fonte: Graph API Reference v25.0_ Ad Account Saved Audiences.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Saved Audiences

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#)

## Reading


saved audiences


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fsaved_audiences&version=v25.0)
```
GET /v25.0/{ad-account-id}/saved_audiences HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/saved_audiences',
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
    "/{ad-account-id}/saved_audiences",
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
    "/{ad-account-id}/saved_audiences",
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
                               initWithGraphPath:@"/{ad-account-id}/saved_audiences"
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
| business_id numeric string or integer | optional param assist with filters such as recently used |
| fields list\<string\> | Fields to be retrieved. Default behavior is to return only the ids. |
| filtering list\<Filter Object\> | Filters on the report data. This parameter is an array of filter objects. |
| → field string | Required |
| → operator enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP} | Required |
| → value string | Required |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [SavedAudience](https://developers.facebook.com/docs/marketing-api/reference/saved-audience/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#)On This Page[Ad Account Saved Audiences](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/saved_audiences/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7LmqgVI3V3z0iw43rc38bUTsQTaoTM7R-O8yHmnE_V07oasLHzwKWY_3g_ww_aem_Pq5Kmk0ZaKjdbmCKRs1T9g&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74M2H71rifsx6K6nl6arY3WDraThHadE_fVtmtjiQiNM0xGm5gjGb7Z0K3AQ_aem_5tK7LIWm1ULQ6G4RS9Z8DA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR51_ICzsVV3nE9i1h9NsqSJeAYNupBZvim-cpieggA2dGwfSzOBK9DKvKzdVQ_aem_S3NypdH0EtOCWWCIQ9hNBg&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ibd9yH06u3TFadRAwEMeFXk6Wswwb2YpkYyXM8BIrF2XdGSbud09gnMnICg_aem_CYAs3ZhS007USF-HzgSYVQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UwU-N8OEQ8OPUbKkjMXD5S4L_Iix4CU4n4thydjmhAqRZNYDTHwpKDGXcDg_aem_bcjVwGOILeqfGjRhjLwzkA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-B7L8qDJh9QFt0fhUYU1Ks852MAO6FjFTZ3y94FLb0apv9wSs4ZHr7i0rlg_aem_f4pvCQdVbNXIufvfx5_lwg&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR547bfKdNet-IwQAuIEbq34eoBXljFboi-koxLruIIqJw8M7Z9b6CfsbHF7Vg_aem_Tuvwh5rC0IO8I3JK7nkVrQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74M2H71rifsx6K6nl6arY3WDraThHadE_fVtmtjiQiNM0xGm5gjGb7Z0K3AQ_aem_5tK7LIWm1ULQ6G4RS9Z8DA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-B7L8qDJh9QFt0fhUYU1Ks852MAO6FjFTZ3y94FLb0apv9wSs4ZHr7i0rlg_aem_f4pvCQdVbNXIufvfx5_lwg&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5unNvzZeJQmsJd0F18dJ-iUWP3j_fspHrVvOvlATvKI1x_xx3s7NGYf1knNg_aem_GCz6h9_XJ6qp7JHLTNj7iA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ibd9yH06u3TFadRAwEMeFXk6Wswwb2YpkYyXM8BIrF2XdGSbud09gnMnICg_aem_CYAs3ZhS007USF-HzgSYVQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5unNvzZeJQmsJd0F18dJ-iUWP3j_fspHrVvOvlATvKI1x_xx3s7NGYf1knNg_aem_GCz6h9_XJ6qp7JHLTNj7iA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UwU-N8OEQ8OPUbKkjMXD5S4L_Iix4CU4n4thydjmhAqRZNYDTHwpKDGXcDg_aem_bcjVwGOILeqfGjRhjLwzkA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6RwqgHiV_BOiriQeGddiMUpuIFZmTyweSog0d9Ko-gp8nzGx7s6XSvzncjfg_aem_Ql_WtvR4PvvTjof-exCrog&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR547bfKdNet-IwQAuIEbq34eoBXljFboi-koxLruIIqJw8M7Z9b6CfsbHF7Vg_aem_Tuvwh5rC0IO8I3JK7nkVrQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ibd9yH06u3TFadRAwEMeFXk6Wswwb2YpkYyXM8BIrF2XdGSbud09gnMnICg_aem_CYAs3ZhS007USF-HzgSYVQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5unNvzZeJQmsJd0F18dJ-iUWP3j_fspHrVvOvlATvKI1x_xx3s7NGYf1knNg_aem_GCz6h9_XJ6qp7JHLTNj7iA&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ibd9yH06u3TFadRAwEMeFXk6Wswwb2YpkYyXM8BIrF2XdGSbud09gnMnICg_aem_CYAs3ZhS007USF-HzgSYVQ&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-B7L8qDJh9QFt0fhUYU1Ks852MAO6FjFTZ3y94FLb0apv9wSs4ZHr7i0rlg_aem_f4pvCQdVbNXIufvfx5_lwg&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rm4Gvp8GXM6uJdspuoFzN5uUOrN5MaclX6kbGvbYv9YCO-h-10XNU0dQ7XA_aem_CcICk0Vw9-0JYIzOp7qH5w&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4i9yfrzChM9A3NIakVhMM8GtodiwsMCgwLYrb0h6VY25VfSvu7YgVHytJntderwHM__NVtBeuK9duwA81uI2rM2vhkBB3sdcHCA_MHuupHtKagaFG1K97q97e2HlOA2oK9z_8Zdjm2SruYSqQqueMri-Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo