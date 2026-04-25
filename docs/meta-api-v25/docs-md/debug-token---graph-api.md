<!-- Fonte: Debug Token - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Debug-Token `/debug_token`


This endpoint returns metadata about a given access token. This includes data such as the user for which the token was issued, whether the token is still valid, when it expires, and what permissions the app has for the given user.


This may be used to programatically debug issues with large sets of access tokens.
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#)

## Reading

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=debug_token%3Finput_token%3D%257Binput-token%257D&version=v25.0)
```
GET /v25.0/debug_token?input_token={input-token} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/debug_token?input_token={input-token}',
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
    "/debug_token?input_token={input-token}",
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
    "/debug_token?input_token={input-token}",
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
                               initWithGraphPath:@"/debug_token?input_token={input-token}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```


### Permissions


- An [app access token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/#apptokens) or an app developer's [user access token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/#usertokens) for the app associated with the `input_token` being inspected is required to access this endpoint.


### Parameters


| Name | Description | Type |
| --- | --- | --- |
| input_token | The Access Token that is being inspected. This parameter must be specified. | string |


### Fields


| Name | Description | Type |
| --- | --- | --- |
| data | Data wrapper around the result. | object |
| app_id | The ID of the application this access token is for. | string |
| application | Name of the application this access token is for. | string |
| → error | Any error that a request to the graph api would return due to the access token. | object |
| → code | The error code for the error. | int |
| → message | The error message for the error. | string |
| → subcode | The error subcode for the error. | int |
| expires_at | Timestamp when this access token expires. | unixtime |
| data_access_expires_at | Timestamp when app's access to user data expires. | unixtime |
| is_valid | Whether the access token is still valid or not. | bool |
| issued_at | Timestamp when this access token was issued. | unixtime |
| metadata | General metadata associated with the access token. Can contain data like 'sso', 'auth_type', 'auth_nonce' | object |
| profile_id | For impersonated access tokens, the ID of the page this token contains. | string |
| scopes | List of permissions that the user has granted for the app in this access token. | string[] |
| granular_scopes | List of granular permissions that the user has granted for the app in this access token. If permission applies to all, targets will not be shown. | shape('scope' =\> string,'target_ids' =\> ?int[],)[] |
| user_id | The ID of the user this access token is for. | string |

[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#)

## Publishing and Deleting


You cannot perform these actions on this edge.
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#)[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#)On This Page[Debug-Token /debug_token](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#debug-token--debug-token)[Reading](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#read)[Permissions](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#readperms)[Parameters](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#fields)[Publishing and Deleting](https://developers.facebook.com/docs/graph-api/reference/v25.0/debug_token#nopublishdeleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4INTjfUPzV2OltakbYHIyjR1u3HvR1gIiF_0VnJaARxMKpR1J4YlN29UVRfw_aem_p9HaHLtUFNRnzMyhHF2yCA&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR59kwD6wZqpZbKR2d0X9ot0N3ZfM_L-UN7eNxoRta288M7Uf5b2XfJqaTDV8g_aem_KEFm_ZOnFhEFXwxTt4a48w&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR59kwD6wZqpZbKR2d0X9ot0N3ZfM_L-UN7eNxoRta288M7Uf5b2XfJqaTDV8g_aem_KEFm_ZOnFhEFXwxTt4a48w&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR72-knDKdtXaBTRCDQ2mjGVgRQu7s_ScOo62BILGwEpbGvZ1eXhDb6uheshUg_aem_xda7FCmy2CGTDtNLxyuUdw&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iUYGyYm2bCWRT3N8jcgvQoZ25kiPG5Wt6-L3rSstH_JlufHLdLXNe1wWpHw_aem_LGvlFJn1sdgAzYyexpp7xQ&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ytAH7iaiPPW_JR2xR2CHSGarW90hwUHoFsSvG5kuhqq8Z0M6flndnfYPoKQ_aem_qC999Rk3hzDtdU31LsF-ww&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iUYGyYm2bCWRT3N8jcgvQoZ25kiPG5Wt6-L3rSstH_JlufHLdLXNe1wWpHw_aem_LGvlFJn1sdgAzYyexpp7xQ&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4-R_EZvziXA5s-DF9U_p0WH3JaQZInUCsZzdQv5Tg34jFo8pXQrScUTeUVXQ_aem_3McJDT0NPV3Ov6_EzuzXng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iUYGyYm2bCWRT3N8jcgvQoZ25kiPG5Wt6-L3rSstH_JlufHLdLXNe1wWpHw_aem_LGvlFJn1sdgAzYyexpp7xQ&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5r5Ecr-s0GFc7SW0FCgWiMSB0vuvhw7ugAPRtn1ishw5K4B41OWZjGHE0kvQ_aem_QKV9vAJX7fXe5bkddMWDqg&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rcGTTlK12Ykx8OXwATd_ROml0lU2nNcm1poZu28s1HBBpetJaam98uvZd4A_aem_JvIMbML9_EhAEHnQjhaSng&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5r5Ecr-s0GFc7SW0FCgWiMSB0vuvhw7ugAPRtn1ishw5K4B41OWZjGHE0kvQ_aem_QKV9vAJX7fXe5bkddMWDqg&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5UiVA2Fa2y5kxK2j-huO8AS9vPxjDPbrEH0YJdH7oGGgIccdmMTuwzo0P-Bg_aem_zq4a3Fj8syRxXvH2aI0K6w&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7ytAH7iaiPPW_JR2xR2CHSGarW90hwUHoFsSvG5kuhqq8Z0M6flndnfYPoKQ_aem_qC999Rk3hzDtdU31LsF-ww&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR72-knDKdtXaBTRCDQ2mjGVgRQu7s_ScOo62BILGwEpbGvZ1eXhDb6uheshUg_aem_xda7FCmy2CGTDtNLxyuUdw&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4wNo2z-1wqTa7e4lN9J5IoXHMeSnQ6_DfXyJM76rsMgTefmpC9_kCFnNYB-jFMbGP6FluVOU5-H1A8TCGZlL3w9Fh9MaiqE57f2Ysn-T_O527Z6_IarCjTS0uV1L70lc8po9ik2-wf9BNQOQPuRj6R6AE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo