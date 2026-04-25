<!-- Fonte: Graph API Reference v25.0_ Ad Account Deprecatedtargetingadsets.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Deprecatedtargetingadsets

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#)

## Reading


AdAccountDeprecatedTargetingAdsets


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fdeprecatedtargetingadsets&version=v25.0)
```
GET /v25.0/{ad-account-id}/deprecatedtargetingadsets HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/deprecatedtargetingadsets',
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
    "/{ad-account-id}/deprecatedtargetingadsets",
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
    "/{ad-account-id}/deprecatedtargetingadsets",
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
                               initWithGraphPath:@"/{ad-account-id}/deprecatedtargetingadsets"
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
| type string | Default value: deprecating Query ad sets according to deprecation type. Valid options are deprecating and delivery_paused . |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [AdSet](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#)On This Page[Ad Account Deprecatedtargetingadsets](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/deprecatedtargetingadsets/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6dqGQOyFEGFjpbKvNiiIuqEPRKn_1lqPOHU29PEuMkY24Xu4Eeh7sDNvjDhg_aem_Sy8rneROab7t0OK6LR65RQ&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6rNBYlT5fK-A3mPf0X1mKQ2XwbWCrmk7k-1NK8iS8NlGd11iGm9FkRdBaesw_aem_FEIbZHuwg6Far7G3F9Uu2A&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5O8zrq0W15X1wUa4T9GLWZb3SvlqtRFOM2DMrF5XvjzUFmHXXkigMJ5yBYng_aem_SAuby1re3U7EYzk-npCVlw&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rPSKDMd7-AMCr3JY4O6IzFY5q7K-kct8nL1zYBNykUXzHKLPyahFUbRhilA_aem_3n7EWqLZ0ylUw7hMGoGl1g&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7HdS8BHpL4ey-aNaXlCL_2QoBf0cQPblPu7lIZIKMJbzVar7fuko3nMvHoog_aem_xu57h8uMLcc5lEUVy3bGqA&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6rNBYlT5fK-A3mPf0X1mKQ2XwbWCrmk7k-1NK8iS8NlGd11iGm9FkRdBaesw_aem_FEIbZHuwg6Far7G3F9Uu2A&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rPSKDMd7-AMCr3JY4O6IzFY5q7K-kct8nL1zYBNykUXzHKLPyahFUbRhilA_aem_3n7EWqLZ0ylUw7hMGoGl1g&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4PMol-TR8a-zFoINel4O1LJFvJdnfUQDkLyuwa3-tLcqJ8DRn_T30CBXA47g_aem_jUo4_QqFjky85fsNRmLGHg&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5O8zrq0W15X1wUa4T9GLWZb3SvlqtRFOM2DMrF5XvjzUFmHXXkigMJ5yBYng_aem_SAuby1re3U7EYzk-npCVlw&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rPSKDMd7-AMCr3JY4O6IzFY5q7K-kct8nL1zYBNykUXzHKLPyahFUbRhilA_aem_3n7EWqLZ0ylUw7hMGoGl1g&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EaOKx-kJZWz7N9kBOw3QZMNzVxffRVkJZ1ZGDCTkVKwDnZPSVDF0DT7HylQ_aem_pYed1bdfPkeeEJEljbYKhg&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6dqGQOyFEGFjpbKvNiiIuqEPRKn_1lqPOHU29PEuMkY24Xu4Eeh7sDNvjDhg_aem_Sy8rneROab7t0OK6LR65RQ&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6rNBYlT5fK-A3mPf0X1mKQ2XwbWCrmk7k-1NK8iS8NlGd11iGm9FkRdBaesw_aem_FEIbZHuwg6Far7G3F9Uu2A&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6dqGQOyFEGFjpbKvNiiIuqEPRKn_1lqPOHU29PEuMkY24Xu4Eeh7sDNvjDhg_aem_Sy8rneROab7t0OK6LR65RQ&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rPSKDMd7-AMCr3JY4O6IzFY5q7K-kct8nL1zYBNykUXzHKLPyahFUbRhilA_aem_3n7EWqLZ0ylUw7hMGoGl1g&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4PMol-TR8a-zFoINel4O1LJFvJdnfUQDkLyuwa3-tLcqJ8DRn_T30CBXA47g_aem_jUo4_QqFjky85fsNRmLGHg&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6rNBYlT5fK-A3mPf0X1mKQ2XwbWCrmk7k-1NK8iS8NlGd11iGm9FkRdBaesw_aem_FEIbZHuwg6Far7G3F9Uu2A&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6EaOKx-kJZWz7N9kBOw3QZMNzVxffRVkJZ1ZGDCTkVKwDnZPSVDF0DT7HylQ_aem_pYed1bdfPkeeEJEljbYKhg&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4PMol-TR8a-zFoINel4O1LJFvJdnfUQDkLyuwa3-tLcqJ8DRn_T30CBXA47g_aem_jUo4_QqFjky85fsNRmLGHg&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rPSKDMd7-AMCr3JY4O6IzFY5q7K-kct8nL1zYBNykUXzHKLPyahFUbRhilA_aem_3n7EWqLZ0ylUw7hMGoGl1g&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4I1HofZgosBPcjtWLP_PxMDaqw82QhAWxlQAABqFAYiKdxH8T8EP6MK9Xej7xwoP5-xANrhoNK4gdwidWvplMii83I3XEDY3GEc06nODxHD0Eiv41sDjJrXevM5q_dSk7Wj9Qq-AWLtNnp0nQ5LTSu9zQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo