<!-- Fonte: Ad Account Custom Conversions.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account, Custom Conversions

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)

Data on custom conversion events from event sources, such as a Meta Pixel. You can query this data to measure the effectiveness of our ads. Or use it to optimize ad delivery to target people who converted as defined by your customization and rules.
[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)

## Reading


Ad Account Custom Conversions


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fcustomconversions&version=v25.0)
```
GET /v25.0/{ad-account-id}/customconversions HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/customconversions',
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
    "/{ad-account-id}/customconversions",
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
    "/{ad-account-id}/customconversions",
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
                               initWithGraphPath:@"/{ad-account-id}/customconversions"
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

A list of [CustomConversion](https://developers.facebook.com/docs/marketing-api/reference/custom-conversion/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)

## Creating

You can make a POST request to `customconversions` edge from the following paths:

- [`/act_{ad_account_id}/customconversions`](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/)
When posting to this edge, a [CustomConversion](https://developers.facebook.com/docs/marketing-api/reference/custom-conversion/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| action_source_type enum {app, chat, email, other, phone_call, physical_store, system_generated, website, business_messaging} | Action source type the custom conversion is created from. |
| advanced_rule string | Advanced ruleset for the custom conversion being created allowing multiple sources. |
| custom_event_type enum {ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, COMPLETE_REGISTRATION, CONTENT_VIEW, INITIATED_CHECKOUT, LEAD, PURCHASE, SEARCH, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, LISTING_INTERACTION, FACEBOOK_SELECTED, OTHER} | The custom event type of the conversion being created. |
| default_conversion_value float | Default value: 0 The default conversion value of the conversion being created. |
| description string | The description of the conversion being created. |
| event_source_id numeric string or integer | Event source ID, where event sources are a Pixel, offline event sets and so on. Aggregate custom conversion data from these sources. |
| name string | The name of the conversion being created. Required |
| rule string | Only count an event as a custom conversion if it fulfills this rule. |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, `is_custom_event_type_predicted`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#)On This Page[Ad Account, Custom Conversions](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/customconversions/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ci_qiXg81SEc0hnHViysACs2KBSR3j8pz2hGVWLVTd0UP-9XvmSsfLuHYHw_aem_9WbFrLe8-dVnCiDsLMN2dg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5U0rY3ESAawSWAQuFqCshNvliG0zsEJbiI1ur3Z1jXA8ygxz5nonMM91f1Fg_aem_fYAat3SWFpMm_Um4hmeWUw&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ID8WG-TOzCMenIldXXauRhRiGz-2jGahb0ge2_pyBICgFLOy6Au5vgfGuIg_aem_SWnLj-2x14TsfEftlYS5zg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ID8WG-TOzCMenIldXXauRhRiGz-2jGahb0ge2_pyBICgFLOy6Au5vgfGuIg_aem_SWnLj-2x14TsfEftlYS5zg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6UT6uBpcZ9GxLFjifWvuD2_qRExzhryp6iUVZvxDlO-6XPylSjEyqMbOAZJg_aem_p2tbvaagil3zD48HGP8lbA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4xO5A1C_tk4ODAkx5lMBdwpaFBd8jWG3Oss9nJMtO0YNqtd8MwzUFvjlfq-A_aem_YpPpDIX09KtD8nA-UWJVnw&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6UT6uBpcZ9GxLFjifWvuD2_qRExzhryp6iUVZvxDlO-6XPylSjEyqMbOAZJg_aem_p2tbvaagil3zD48HGP8lbA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4xO5A1C_tk4ODAkx5lMBdwpaFBd8jWG3Oss9nJMtO0YNqtd8MwzUFvjlfq-A_aem_YpPpDIX09KtD8nA-UWJVnw&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ID8WG-TOzCMenIldXXauRhRiGz-2jGahb0ge2_pyBICgFLOy6Au5vgfGuIg_aem_SWnLj-2x14TsfEftlYS5zg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6YH9ECMn48ulpsvi98N2WtqsMfRBoXbeA8Vo-PJxWc7F95zmHjiZCZ8TG9Nw_aem_I84kGxnZARAp7hxs6lHBFA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5U0rY3ESAawSWAQuFqCshNvliG0zsEJbiI1ur3Z1jXA8ygxz5nonMM91f1Fg_aem_fYAat3SWFpMm_Um4hmeWUw&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6UT6uBpcZ9GxLFjifWvuD2_qRExzhryp6iUVZvxDlO-6XPylSjEyqMbOAZJg_aem_p2tbvaagil3zD48HGP8lbA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Jr6FBMqwXu0BLfLAD8xaMfzPBQ9Pfs7aYVpIJJIdcq7Lw5kQrISx-RgiACQ_aem_9F2OGUQ2HIlQf0-NkXR1pg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7gPkDf8rAJLEZrS9MA7zmnXAwAAD1a2EZ3JAx-wVNJy1ThbY6AHp87xsAi5g_aem_u-EEcQ-lkhz1A__mOyj-wQ&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR71ZjxWd3w1QtV4nDulYv9EwXaNK3xLQ6RGlEnHcLn0P96nDyOYLvKmKBrg4A_aem_YUxLIVQsnVIzKtNi-OVrfQ&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74CPbYO_y6M4ioPCWnW5xGef-soTOPm-nrQZLHve5cZs3vKr3RRwKg1JPhiw_aem_kvyG_SjdTEuicfmoOpC-ZA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ci_qiXg81SEc0hnHViysACs2KBSR3j8pz2hGVWLVTd0UP-9XvmSsfLuHYHw_aem_9WbFrLe8-dVnCiDsLMN2dg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Jr6FBMqwXu0BLfLAD8xaMfzPBQ9Pfs7aYVpIJJIdcq7Lw5kQrISx-RgiACQ_aem_9F2OGUQ2HIlQf0-NkXR1pg&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6YH9ECMn48ulpsvi98N2WtqsMfRBoXbeA8Vo-PJxWc7F95zmHjiZCZ8TG9Nw_aem_I84kGxnZARAp7hxs6lHBFA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6UT6uBpcZ9GxLFjifWvuD2_qRExzhryp6iUVZvxDlO-6XPylSjEyqMbOAZJg_aem_p2tbvaagil3zD48HGP8lbA&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4q860bKqFwJDRL8p08Wrh4z4C1g3natDWs_YRMLggjw3IbaGzPRMFLtsxALlukHfCzVggcYuve24skh-8yIXEzu9XyF491_9r9aaEJ6z3sF_dA20Ofr9R1sGHR1keGZjHJ78zgmtLnmYm-XsUzLI-IypI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo