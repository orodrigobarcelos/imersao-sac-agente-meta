<!-- Fonte: Graph API Reference v25.0_ Ad Account Connected Instagram Accounts.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Connected Instagram Accounts

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#)

## Reading


Retrieve instagram accounts associated with this Ad Account


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fconnected_instagram_accounts&version=v25.0)
```
GET /v25.0/{ad-account-id}/connected_instagram_accounts HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/connected_instagram_accounts',
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
    "/{ad-account-id}/connected_instagram_accounts",
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
    "/{ad-account-id}/connected_instagram_accounts",
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
                               initWithGraphPath:@"/{ad-account-id}/connected_instagram_accounts"
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

A list of [IGUser](https://developers.facebook.com/docs/graph-api/reference/shadow-ig-user/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#)On This Page[Ad Account Connected Instagram Accounts](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/connected_instagram_accounts/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6aGW0XZ39YwQx5wKXnE2ewzTyLwTS8a6fpr2NpddtE68JExeJnekO78anWFw_aem_-aLAEvbdhgQvMRrENPiQSg&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4NybQhDYrAb7quC_ktypwrkgBbUSAGwsWWmq0DgiSXsRuFTCcukkvz4mlDtA_aem_3of-yRfW4X403T7JE_6GQA&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4NybQhDYrAb7quC_ktypwrkgBbUSAGwsWWmq0DgiSXsRuFTCcukkvz4mlDtA_aem_3of-yRfW4X403T7JE_6GQA&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EBA74ghf6juMiAyNMeXB9taKGHZPr3jDFbDstPc9EMXkt1YBIzyD4TDK8PQ_aem_J7yMqURjTgOqKyBEyl-6jw&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6tp6eJgFP2OauulFkA8CfGXLwHpHU9zPqBFx1swr9yfi0XrsJM56zRTZxnIQ_aem_gDvrQZmqdrL9O3gq40uu9Q&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4qAruh8Xmw8feSIPgG4SeDQFHztl5WEg5S0wEIv-W89-bRTMvgbtoHCtgYZw_aem_zSnwj0gt0ehZgANmHFLh5Q&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EBA74ghf6juMiAyNMeXB9taKGHZPr3jDFbDstPc9EMXkt1YBIzyD4TDK8PQ_aem_J7yMqURjTgOqKyBEyl-6jw&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6tp6eJgFP2OauulFkA8CfGXLwHpHU9zPqBFx1swr9yfi0XrsJM56zRTZxnIQ_aem_gDvrQZmqdrL9O3gq40uu9Q&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6aGW0XZ39YwQx5wKXnE2ewzTyLwTS8a6fpr2NpddtE68JExeJnekO78anWFw_aem_-aLAEvbdhgQvMRrENPiQSg&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EBA74ghf6juMiAyNMeXB9taKGHZPr3jDFbDstPc9EMXkt1YBIzyD4TDK8PQ_aem_J7yMqURjTgOqKyBEyl-6jw&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XWCj4sgDC3zHbH5ypUnuDxQqnABYysc5_KGWK-JK912JWROd5EYd-HfD-CQ_aem_jpyLhEBlaIILze4N5neP2A&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XWCj4sgDC3zHbH5ypUnuDxQqnABYysc5_KGWK-JK912JWROd5EYd-HfD-CQ_aem_jpyLhEBlaIILze4N5neP2A&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4qAruh8Xmw8feSIPgG4SeDQFHztl5WEg5S0wEIv-W89-bRTMvgbtoHCtgYZw_aem_zSnwj0gt0ehZgANmHFLh5Q&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Y3Nh3kNSjitrkeZzXx5naYRPo8VY247GriDARPmqATj-hbMXSOo5sOSg9QQ_aem_NAKj8-fXXUDB4qn88kLoXg&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6uFaB3FpJ2oSNc29NjOcotvh57PzxyjGUkvpmgWe2uI2UyW1lmjnaYTFRLvA_aem_fxPwcMPMeMSvHslXn_HOww&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EBA74ghf6juMiAyNMeXB9taKGHZPr3jDFbDstPc9EMXkt1YBIzyD4TDK8PQ_aem_J7yMqURjTgOqKyBEyl-6jw&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6vTOEagohTUpXxf_YfmPGozsDqaD5Xqn4F5eLec6H0Wk4k0FwhXb2vYNei3Q_aem_PYeXBS1tflUGUdMTn-BwtA&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4NybQhDYrAb7quC_ktypwrkgBbUSAGwsWWmq0DgiSXsRuFTCcukkvz4mlDtA_aem_3of-yRfW4X403T7JE_6GQA&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Y3Nh3kNSjitrkeZzXx5naYRPo8VY247GriDARPmqATj-hbMXSOo5sOSg9QQ_aem_NAKj8-fXXUDB4qn88kLoXg&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XWCj4sgDC3zHbH5ypUnuDxQqnABYysc5_KGWK-JK912JWROd5EYd-HfD-CQ_aem_jpyLhEBlaIILze4N5neP2A&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7GOxb-DjzuwsUkkAZJAul4oDE_I-oD6RXykj5AyFna3ohORyoKFLEKE5jpE9a9pBwttl7Ciq4PQPBgfWivBak6GIny_N7cKkjDRcRzCmLR7OkXPRgxpYUTHbS0GEehUzMHOGvVYzvDc-Ai5a0EP254Jfw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo