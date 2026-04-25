<!-- Fonte: Graph API Reference v25.0_ Ad Account Product Audiences.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Product Audiences

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#)

## Reading

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#)

## Creating

You can make a POST request to `product_audiences` edge from the following paths:

- [`/act_{ad_account_id}/product_audiences`](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/)
When posting to this edge, an [AdAccount](https://developers.facebook.com/docs/graph-api/reference/ad-account/) will be created.

### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fproduct_audiences%3Fname%3DTest%2BIphone%2BProduct%2BAudience%26product_set_id%3D%253CPRODUCT_SET_ID%253E%26inclusions%3D%255B%257B%2522retention_seconds%2522%253A86400%252C%2522rule%2522%253A%257B%2522and%2522%253A%255B%257B%2522event%2522%253A%257B%2522eq%2522%253A%2522AddToCart%2522%257D%257D%252C%257B%2522userAgent%2522%253A%257B%2522i_contains%2522%253A%2522iPhone%2522%257D%257D%255D%257D%257D%255D%26exclusions%3D%255B%257B%2522retention_seconds%2522%253A172800%252C%2522rule%2522%253A%257B%2522event%2522%253A%257B%2522eq%2522%253A%2522Purchase%2522%257D%257D%257D%255D&version=v25.0)
```
POST /v25.0/act_<AD_ACCOUNT_ID>/product_audiences HTTP/1.1
Host: graph.facebook.com

name=Test+Iphone+Product+Audience&product_set_id=%3CPRODUCT_SET_ID%3E&inclusions=%5B%7B%22retention_seconds%22%3A86400%2C%22rule%22%3A%7B%22and%22%3A%5B%7B%22event%22%3A%7B%22eq%22%3A%22AddToCart%22%7D%7D%2C%7B%22userAgent%22%3A%7B%22i_contains%22%3A%22iPhone%22%7D%7D%5D%7D%7D%5D&exclusions=%5B%7B%22retention_seconds%22%3A172800%2C%22rule%22%3A%7B%22event%22%3A%7B%22eq%22%3A%22Purchase%22%7D%7D%7D%5D
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/product_audiences',
    array (
      'name' => 'Test Iphone Product Audience',
      'product_set_id' => '<PRODUCT_SET_ID>',
      'inclusions' => '[{"retention_seconds":86400,"rule":{"and":[{"event":{"eq":"AddToCart"}},{"userAgent":{"i_contains":"iPhone"}}]}}]',
      'exclusions' => '[{"retention_seconds":172800,"rule":{"event":{"eq":"Purchase"}}}]',
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
    "/act_<AD_ACCOUNT_ID>/product_audiences",
    "POST",
    {
        "name": "Test Iphone Product Audience",
        "product_set_id": "<PRODUCT_SET_ID>",
        "inclusions": "[{\"retention_seconds\":86400,\"rule\":{\"and\":[{\"event\":{\"eq\":\"AddToCart\"}},{\"userAgent\":{\"i_contains\":\"iPhone\"}}]}}]",
        "exclusions": "[{\"retention_seconds\":172800,\"rule\":{\"event\":{\"eq\":\"Purchase\"}}}]"
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
params.putString("name", "Test Iphone Product Audience");
params.putString("product_set_id", "<PRODUCT_SET_ID>");
params.putString("inclusions", "[{\"retention_seconds\":86400,\"rule\":{\"and\":[{\"event\":{\"eq\":\"AddToCart\"}},{\"userAgent\":{\"i_contains\":\"iPhone\"}}]}}]");
params.putString("exclusions", "[{\"retention_seconds\":172800,\"rule\":{\"event\":{\"eq\":\"Purchase\"}}}]");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/product_audiences",
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
  @"name": @"Test Iphone Product Audience",
  @"product_set_id": @"<PRODUCT_SET_ID>",
  @"inclusions": @"[{\"retention_seconds\":86400,\"rule\":{\"and\":[{\"event\":{\"eq\":\"AddToCart\"}},{\"userAgent\":{\"i_contains\":\"iPhone\"}}]}}]",
  @"exclusions": @"[{\"retention_seconds\":172800,\"rule\":{\"event\":{\"eq\":\"Purchase\"}}}]",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/product_audiences"
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
  -F 'name="Test Iphone Product Audience"' \
  -F 'product_set_id="<PRODUCT_SET_ID>"' \
  -F 'inclusions=[
       {
         "retention_seconds": 86400,
         "rule": {
           "and": [
             {
               "event": {
                 "eq": "AddToCart"
               }
             },
             {
               "userAgent": {
                 "i_contains": "iPhone"
               }
             }
           ]
         }
       }
     ]' \
  -F 'exclusions=[
       {
         "retention_seconds": 172800,
         "rule": {
           "event": {
             "eq": "Purchase"
           }
         }
       }
     ]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/product_audiences
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| associated_audience_id int64 | SELF_EXPLANATORY |
| creation_params dictionary { string : \<string\> } | SELF_EXPLANATORY |
| description string | SELF_EXPLANATORY |
| enable_fetch_or_create boolean | enable_fetch_or_create |
| event_sources array\<JSON object\> | event_sources |
| → id int64 | id Required |
| → type enum {APP, OFFLINE_EVENTS, PAGE, PIXEL} | type Required |
| exclusions list\<Object\> | SELF_EXPLANATORY |
| → booking_window Object |  |
| → → min_seconds int64 |  |
| → → max_seconds int64 |  |
| → count Object |  |
| → event string |  |
| → type enum {CUSTOM, PRIMARY, WEBSITE, APP, OFFLINE_CONVERSION, CLAIM, MANAGED, PARTNER, VIDEO, LOOKALIKE, ENGAGEMENT, BAG_OF_ACCOUNTS, STUDY_RULE_AUDIENCE, FOX, MEASUREMENT, REGULATED_CATEGORIES_AUDIENCE, BIDDING, EXCLUSION, MESSENGER_SUBSCRIBER_LIST} |  |
| → retention Object |  |
| → → min_seconds integer | Required |
| → → max_seconds integer | Required |
| → retention_days int64 |  |
| → retention_seconds integer |  |
| → rule Object |  |
| → pixel_id int64 |  |
| inclusions list\<Object\> | SELF_EXPLANATORY |
| → booking_window Object |  |
| → → min_seconds int64 |  |
| → → max_seconds int64 |  |
| → count Object |  |
| → event string |  |
| → type enum {CUSTOM, PRIMARY, WEBSITE, APP, OFFLINE_CONVERSION, CLAIM, MANAGED, PARTNER, VIDEO, LOOKALIKE, ENGAGEMENT, BAG_OF_ACCOUNTS, STUDY_RULE_AUDIENCE, FOX, MEASUREMENT, REGULATED_CATEGORIES_AUDIENCE, BIDDING, EXCLUSION, MESSENGER_SUBSCRIBER_LIST} |  |
| → retention Object |  |
| → → min_seconds integer | Required |
| → → max_seconds integer | Required |
| → retention_days int64 |  |
| → retention_seconds integer |  |
| → rule Object |  |
| → pixel_id int64 |  |
| name string | SELF_EXPLANATORY Required |
| opt_out_link string | SELF_EXPLANATORY |
| parent_audience_id int64 | SELF_EXPLANATORY |
| product_set_id numeric string or integer | SELF_EXPLANATORY Required |
| subtype enum {CUSTOM, PRIMARY, WEBSITE, APP, OFFLINE_CONVERSION, CLAIM, MANAGED, PARTNER, VIDEO, LOOKALIKE, ENGAGEMENT, BAG_OF_ACCOUNTS, STUDY_RULE_AUDIENCE, FOX, MEASUREMENT, REGULATED_CATEGORIES_AUDIENCE, BIDDING, EXCLUSION, MESSENGER_SUBSCRIBER_LIST} | SELF_EXPLANATORY |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, `message`: string, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2654 | Failed to create custom audience |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#)On This Page[Ad Account Product Audiences](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#Reading)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#Creating)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#parameters)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#error-codes)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/product_audiences/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-2BCj20cZCWGH4OtZsmnR0AchVh6LeOaI7YsVBBtUlruzLn27qgun36Ppg_aem_8D8qX1KS9s21QZo6uxTVtA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5tOzGbgdBKt0OShlVPNxC1fdQCHom8sklwL25-h0MPq6ImsH8WaKyRPUk6Hw_aem_XkUGoNWpeaBjbiTag8-WSA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-2BCj20cZCWGH4OtZsmnR0AchVh6LeOaI7YsVBBtUlruzLn27qgun36Ppg_aem_8D8qX1KS9s21QZo6uxTVtA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iQ2p80hKi0Trqevd9vztK1tQvkdDnJfiODyjQKv804y7yVrCVxt08ZQLU8Q_aem_i6spoS4uliZZHMGPU1Q4kw&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77GP0WkaGL66FvJXH6Ctnq83NhT179XxvlHRcDdXeC7C0fe9wpTcVghceXbg_aem_PhSJMnWtsptt-QxEN-YzMg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5bGIuTvF8yb50VqD5qHwwzxDUOGZM-3kGoN1GsbnOLztWKvFrCpNRPZtpfIA_aem_VHXJasL6nU5BoxY6Nu1m5w&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77GP0WkaGL66FvJXH6Ctnq83NhT179XxvlHRcDdXeC7C0fe9wpTcVghceXbg_aem_PhSJMnWtsptt-QxEN-YzMg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iQ2p80hKi0Trqevd9vztK1tQvkdDnJfiODyjQKv804y7yVrCVxt08ZQLU8Q_aem_i6spoS4uliZZHMGPU1Q4kw&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5tOzGbgdBKt0OShlVPNxC1fdQCHom8sklwL25-h0MPq6ImsH8WaKyRPUk6Hw_aem_XkUGoNWpeaBjbiTag8-WSA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7m_uYDzp2hgZBQbCpTMiejZc27ck410r2tq_mv4f3pHG0Xj-TzRI_20_2VbQ_aem_GHoPOKP2MBQr69iKZ_TWpg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7m_uYDzp2hgZBQbCpTMiejZc27ck410r2tq_mv4f3pHG0Xj-TzRI_20_2VbQ_aem_GHoPOKP2MBQr69iKZ_TWpg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-2BCj20cZCWGH4OtZsmnR0AchVh6LeOaI7YsVBBtUlruzLn27qgun36Ppg_aem_8D8qX1KS9s21QZo6uxTVtA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5bGIuTvF8yb50VqD5qHwwzxDUOGZM-3kGoN1GsbnOLztWKvFrCpNRPZtpfIA_aem_VHXJasL6nU5BoxY6Nu1m5w&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7m_uYDzp2hgZBQbCpTMiejZc27ck410r2tq_mv4f3pHG0Xj-TzRI_20_2VbQ_aem_GHoPOKP2MBQr69iKZ_TWpg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-2BCj20cZCWGH4OtZsmnR0AchVh6LeOaI7YsVBBtUlruzLn27qgun36Ppg_aem_8D8qX1KS9s21QZo6uxTVtA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR48-2BCj20cZCWGH4OtZsmnR0AchVh6LeOaI7YsVBBtUlruzLn27qgun36Ppg_aem_8D8qX1KS9s21QZo6uxTVtA&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7m_uYDzp2hgZBQbCpTMiejZc27ck410r2tq_mv4f3pHG0Xj-TzRI_20_2VbQ_aem_GHoPOKP2MBQr69iKZ_TWpg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77GP0WkaGL66FvJXH6Ctnq83NhT179XxvlHRcDdXeC7C0fe9wpTcVghceXbg_aem_PhSJMnWtsptt-QxEN-YzMg&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4_prsxBKsDHo3WoVi1fhj5zZFPNlmpzqt5AwzobHN-bJQOIsNU5kVebkPQVw_aem_mh5oSk_mk5oq13vhHQ3V0w&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iQ2p80hKi0Trqevd9vztK1tQvkdDnJfiODyjQKv804y7yVrCVxt08ZQLU8Q_aem_i6spoS4uliZZHMGPU1Q4kw&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6i5YkPtSbGUTUN9sETtEk_A30m8Fvptej5uSJZQ6RCEuP08tkDgR6hB5u8yr3Z5tHiMdQLhVzaiQZnmN86Cjcilgy1aOzsTKYBHJ0j5Z4QBmDzSBuAUcLCPT7qgNvLOTxdbxGeNwfjOAJF3y6GsrTb0L8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo