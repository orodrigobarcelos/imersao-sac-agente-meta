<!-- Fonte: Ad Creativee.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Creative

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)

Contains content for an ad, including images, videos and so on.
[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)

## Reading


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-id%7D%2Fadcreatives&version=v25.0)
```
GET /v25.0/{ad-id}/adcreatives HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-id}/adcreatives',
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
    "/{ad-id}/adcreatives",
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
    "/{ad-id}/adcreatives",
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
                               initWithGraphPath:@"/{ad-id}/adcreatives"
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

A list of [AdCreative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 104 | Incorrect signature |
| 2500 | Error parsing graph query |

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)On This Page[Reading](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4tHpTwkZKO7qby1ns6JiUJ_0dl_A-jSnGPULqaBnul4_lTdajCWIlZGdLvnA_aem_8Z8CbtYqLyUfT54uJ6Hrvg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4eRv9J71pjHb8rgoSD-lJTK9wKT1GX49VwEXnUck6450hvo3QG2fbMsm7XCg_aem_1qbyRgfdaLE5-iZtE9NTnw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qlFXBt3GptLqwLH5qdBaQAx4_8Qlc6IFd8kFJVoAmEkoEqkpPvrO5znxDIw_aem_v4IuD0Dm-u9UkPINAjgMOA&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5O6PXh-ZOKNBxVsooCvf6d30H3eEL6emOBt2t68UW1HzkZqFamlI_nDgw2vg_aem_etSOmrgJ7gK6hGC_3izg2g&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7C4WOUP3qszOWqo7bdzgWwIVhx4trZGNwzeVeCQ0dooXPfCFvAGEjMcalrUA_aem_pT6cdMj_HqheEHSywtG4bg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7C4WOUP3qszOWqo7bdzgWwIVhx4trZGNwzeVeCQ0dooXPfCFvAGEjMcalrUA_aem_pT6cdMj_HqheEHSywtG4bg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6KxHfE0_wlPxloZDqMSTnvRVeHfy1wshVb6w7zz4lKitPs50PuPOmArrMkmQ_aem_gopywqW2XO7pM--Q5Qa9Hw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gKvIj-QWwMVfms0W7K-5JfwcZs_Uy-V3kY19n9lVpfJQGHOtIRZBhNppEig_aem_y8jhdnMvDZ6dbZgi_6m6ug&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4eRv9J71pjHb8rgoSD-lJTK9wKT1GX49VwEXnUck6450hvo3QG2fbMsm7XCg_aem_1qbyRgfdaLE5-iZtE9NTnw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qlFXBt3GptLqwLH5qdBaQAx4_8Qlc6IFd8kFJVoAmEkoEqkpPvrO5znxDIw_aem_v4IuD0Dm-u9UkPINAjgMOA&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6KxHfE0_wlPxloZDqMSTnvRVeHfy1wshVb6w7zz4lKitPs50PuPOmArrMkmQ_aem_gopywqW2XO7pM--Q5Qa9Hw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR46yQDPkL6MN-xk0ucHPKjDEeVxhlRKgFOMKLy3URievovztcHFQsAytvCaYg_aem_4rTHTuog2ej32_MlZbjlkA&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR40_NK_3BrB4fyCU4pS9iPsZ_nzhTdff72aG36VqWUMz4A8ebobtZdW7547mA_aem_IhwmVxgjYDBGNxFwggnl1A&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7C4WOUP3qszOWqo7bdzgWwIVhx4trZGNwzeVeCQ0dooXPfCFvAGEjMcalrUA_aem_pT6cdMj_HqheEHSywtG4bg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4tHpTwkZKO7qby1ns6JiUJ_0dl_A-jSnGPULqaBnul4_lTdajCWIlZGdLvnA_aem_8Z8CbtYqLyUfT54uJ6Hrvg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4eRv9J71pjHb8rgoSD-lJTK9wKT1GX49VwEXnUck6450hvo3QG2fbMsm7XCg_aem_1qbyRgfdaLE5-iZtE9NTnw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4tHpTwkZKO7qby1ns6JiUJ_0dl_A-jSnGPULqaBnul4_lTdajCWIlZGdLvnA_aem_8Z8CbtYqLyUfT54uJ6Hrvg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR40_NK_3BrB4fyCU4pS9iPsZ_nzhTdff72aG36VqWUMz4A8ebobtZdW7547mA_aem_IhwmVxgjYDBGNxFwggnl1A&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4tHpTwkZKO7qby1ns6JiUJ_0dl_A-jSnGPULqaBnul4_lTdajCWIlZGdLvnA_aem_8Z8CbtYqLyUfT54uJ6Hrvg&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6KxHfE0_wlPxloZDqMSTnvRVeHfy1wshVb6w7zz4lKitPs50PuPOmArrMkmQ_aem_gopywqW2XO7pM--Q5Qa9Hw&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6v9G5ZNvdlfw31QVVBouUQZtSrKWKFc0PzeExKQCHWrFsUnaJjcaCtR6qLEYt1LRT6_YV7QZbEI_cGgM7UbFrhYc0ralkIlqVcM0dAHTTDHTbdf3dPDPthePbwwMvoZDShN_ib-G891HtEDp50HfS3gsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo