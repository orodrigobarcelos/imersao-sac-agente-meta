<!-- Fonte: Ad Account Custom Audiencess.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Customaudiences

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#)

## Reading


The custom audiences associated with the ad account.

**Note:** To retrieve the IDs of lookalike audiences based on your custom audiences, use the `lookalike_audience_ids` field. See [Lookalike Audiences - Managing Audiences](https://developers.facebook.com/docs/marketing-api/audiences/guides/lookalike-audiences#read) for more information.



### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=act_%3CAD_ACCOUNT_ID%3E%2Fcustomaudiences%3Ffields%3Did&version=v25.0)
```
GET /v25.0/act_<AD_ACCOUNT_ID>/customaudiences?fields=id HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/act_<AD_ACCOUNT_ID>/customaudiences?fields=id',
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
    "/act_<AD_ACCOUNT_ID>/customaudiences",
    {
        "fields": "id"
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
params.putString("fields", "id");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/customaudiences",
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
  @"fields": @"id",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/customaudiences"
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
  -d 'fields="id"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| business_id numeric string or integer | Optional. This param assists with filters, such as recently used. |
| fetch_primary_audience boolean | Default value: false fetch_primary_audience |
| fields list\<string\> | Fields to be retrieved. Default behavior is to return only the IDs. |
| filtering list\<Filter Object\> | Filters on the report data. This parameter is an array of filter objects. |
| → field string | Required |
| → operator enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP} | Required |
| → value string | Required |
| pixel_id numeric string | Optional. This param fetches audiences associated to specific pixel. |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [CustomAudience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#custom-audience. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#)

## Creating


Your ability to create custom audiences may be limited.


It is expected that you have the same audience capabilities independent of your app's status, which could be *in development* or *live*.


To create a custom audience you'll first need to create a blank audience. Then, you'll want to add people to the blank audience you just created by updating the [users edge](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/) of the audience. **You can create a maximum of 500 custom audiences.**

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#)On This Page[Ad Account Customaudiences](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/customaudiences/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fqTJL-IN_HYKqEcxE-EqXtXwQQJLcNJlxHTcKJ-O2De805cfAgTHYvrQMlQ_aem_P_AUytCVjHxcK6bmkWG66A&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Yno4DNkQUdkdyz1nhqentJ1b89Aq4rWnal76cKF2p-t5RD0-Bx8LGLp7c6g_aem_mXDz2n4rjR-kMaeBl0-gNA&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7VUEMsBRgB7uKKOyIMFscpWX-qRhO5qHibE2Vv8S6ldmzRkMnfDm28JHmsnQ_aem_8RiCCCcHV_S6nu5L7NI8Xg&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7McaKXr6c1GREef37gAlS4Bij3IpzESEenxsesqMykuuN93BwzIaJXiIgVwA_aem_pNf5Oz1IqY06YgoYozNHzQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR50-41GrzK5BpU7U2QRHYqMD8aTOlyy1D7Sq1YxSpYi3aEKX8YhZVMyukSSww_aem_qkhK0uAWBz9sKI2FhwxY5Q&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5OMEe7uNEIwsppn-AXwDZLxmzsIxSQ34LUvYqnnRqbat4HawBh88fVfhgolA_aem_pscDw7Pv42ZbysjHxsllWQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR76wbVuD4cWZQq5w9BBlUqFyhys2tiVX7rV5AkDbIgLt4RwLPyBU-OaG0ch_A_aem_bEEtBMomhrXW1GlKKy9hpQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fqTJL-IN_HYKqEcxE-EqXtXwQQJLcNJlxHTcKJ-O2De805cfAgTHYvrQMlQ_aem_P_AUytCVjHxcK6bmkWG66A&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR76wbVuD4cWZQq5w9BBlUqFyhys2tiVX7rV5AkDbIgLt4RwLPyBU-OaG0ch_A_aem_bEEtBMomhrXW1GlKKy9hpQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Yno4DNkQUdkdyz1nhqentJ1b89Aq4rWnal76cKF2p-t5RD0-Bx8LGLp7c6g_aem_mXDz2n4rjR-kMaeBl0-gNA&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Q0Cv8JD9EwcP_1n1hcwjV4aMzkCLdQoVvMfCewPQebK26hzXzLZJv4mMwUg_aem_vVxSiHBv8mZl2gOtx8lkDA&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7McaKXr6c1GREef37gAlS4Bij3IpzESEenxsesqMykuuN93BwzIaJXiIgVwA_aem_pNf5Oz1IqY06YgoYozNHzQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR50-41GrzK5BpU7U2QRHYqMD8aTOlyy1D7Sq1YxSpYi3aEKX8YhZVMyukSSww_aem_qkhK0uAWBz9sKI2FhwxY5Q&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fqTJL-IN_HYKqEcxE-EqXtXwQQJLcNJlxHTcKJ-O2De805cfAgTHYvrQMlQ_aem_P_AUytCVjHxcK6bmkWG66A&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5OMEe7uNEIwsppn-AXwDZLxmzsIxSQ34LUvYqnnRqbat4HawBh88fVfhgolA_aem_pscDw7Pv42ZbysjHxsllWQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5yXzJFh6mGL_G3YE-0rghNPAvVhXBQVa9SRdeBSvTcWYPOAqMlEJHjYlg36Q_aem_zxpZYTVTUQmfQ87lnKDAmA&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR50-41GrzK5BpU7U2QRHYqMD8aTOlyy1D7Sq1YxSpYi3aEKX8YhZVMyukSSww_aem_qkhK0uAWBz9sKI2FhwxY5Q&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR76wbVuD4cWZQq5w9BBlUqFyhys2tiVX7rV5AkDbIgLt4RwLPyBU-OaG0ch_A_aem_bEEtBMomhrXW1GlKKy9hpQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4kjBlhK_whO5cY_1iOYYJ7pWmHu4HVc4aooo6WokbpEvQyWiNCamy8bnbalQ_aem_O2vDZqSdO63-zORYKF90XQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4kjBlhK_whO5cY_1iOYYJ7pWmHu4HVc4aooo6WokbpEvQyWiNCamy8bnbalQ_aem_O2vDZqSdO63-zORYKF90XQ&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TJ0AZnHZotCoSqW7JmD8EZyCsuREl40GOdnPhLfNEEw9CT7ZZag5lzZ1fc1KWf15nvDAl6Wv5Cm0sRBat0Fl_lj9RQJBXbstweu516b4cKsNXnXfewpB3a67u6Vd9StDqJYo1U-ANmVFKkcmwKNnwRvw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo