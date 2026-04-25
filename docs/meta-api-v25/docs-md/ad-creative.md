<!-- Fonte: Ad Creative.html -->
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

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#)On This Page[Reading](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/adgroup/adcreatives/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4y6g5rDOOJ4pJIk-QPmDuYXUUEa57dHOeuxOG6kIY3nMQsAqV0lWsLqUkd-w_aem_kF6VlYpNS5SLkUICcwmspg&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6tws0ZoCGkif8aZ2M7EqkWpZVqp00g9D7lJNMg8q4lDqTBbuAnHR6TpqMYow_aem_E4uAUFO5LZv4G4tISZjJpQ&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6tws0ZoCGkif8aZ2M7EqkWpZVqp00g9D7lJNMg8q4lDqTBbuAnHR6TpqMYow_aem_E4uAUFO5LZv4G4tISZjJpQ&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4n70wdhYoj8JRyBaA1pCauzUXW3QI-pPkLd-lamAYaE5ywQjeers-PRVYMzw_aem_bkWv2iEInlaLG9qDqhXQnw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ybKFeGunypPEDPJbwhX9NRGBG5xLGU9zLelU2PAVIo5fboCHzEbuFmteafg_aem_fQyFfFRI67RVWXoiRgPW0A&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6d_6lY6OzvxgXmRpDF-VBvDImO5-qC7PecqbFwbtCIw8D9i1YvgoxwugqMwA_aem_vrSD2BXcMasZD0KhGjc6ow&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7FvKFKzgZLR8YhBufOvVMQeKwjV4-HL-k9m_xPzqyJvscpC0aZKHl9WBfZAw_aem_5NDaKnFwkYNy5PiCWNc-Tw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iTQiX1QonoDSmpatWwWisSpwD8X9Sjyvp3Lzo8Liz4tpFs8_JqtczJs6d7Q_aem_sJyssUD4qVU1fyMZk6ZfSg&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6d_6lY6OzvxgXmRpDF-VBvDImO5-qC7PecqbFwbtCIw8D9i1YvgoxwugqMwA_aem_vrSD2BXcMasZD0KhGjc6ow&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5ybKFeGunypPEDPJbwhX9NRGBG5xLGU9zLelU2PAVIo5fboCHzEbuFmteafg_aem_fQyFfFRI67RVWXoiRgPW0A&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR46JaKV2MLi-38kBGiUgdhxQt3rSLA0JjrJzePeCDKDDPcf1gbgKnyxI3vFHw_aem_2qmUA0uHxNvrgHlm0IrVdw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6d_6lY6OzvxgXmRpDF-VBvDImO5-qC7PecqbFwbtCIw8D9i1YvgoxwugqMwA_aem_vrSD2BXcMasZD0KhGjc6ow&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7FvKFKzgZLR8YhBufOvVMQeKwjV4-HL-k9m_xPzqyJvscpC0aZKHl9WBfZAw_aem_5NDaKnFwkYNy5PiCWNc-Tw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR69br2a_4y5ppUL9WJET2s3AduHkuxyamzInk8ehF4OQetO4ASiFZaaUp5DmA_aem_Uajx5nFs5GG9yvL9nig1YQ&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5WbqhgfvtEXdDps3zgmeiRkdck80AQV9W-ASxxKSR8Jmn7oosCh1MzIyZvZg_aem__VfBXRqbCO9eqw9M4hwfRA&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4n70wdhYoj8JRyBaA1pCauzUXW3QI-pPkLd-lamAYaE5ywQjeers-PRVYMzw_aem_bkWv2iEInlaLG9qDqhXQnw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR69br2a_4y5ppUL9WJET2s3AduHkuxyamzInk8ehF4OQetO4ASiFZaaUp5DmA_aem_Uajx5nFs5GG9yvL9nig1YQ&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7FvKFKzgZLR8YhBufOvVMQeKwjV4-HL-k9m_xPzqyJvscpC0aZKHl9WBfZAw_aem_5NDaKnFwkYNy5PiCWNc-Tw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7FvKFKzgZLR8YhBufOvVMQeKwjV4-HL-k9m_xPzqyJvscpC0aZKHl9WBfZAw_aem_5NDaKnFwkYNy5PiCWNc-Tw&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6d_6lY6OzvxgXmRpDF-VBvDImO5-qC7PecqbFwbtCIw8D9i1YvgoxwugqMwA_aem_vrSD2BXcMasZD0KhGjc6ow&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4NOGA6Dxt4hXEZ3GP8f8O6u46NgghR_H70bKUxtA-St796OEAKj_mxW4GcQnOMJXdAG5aHb5apY50rb8nsZ3AAVh1beTzyGSvRfJqtYqZNmS4beJ5OzOXqOZjKB5s91mlSTRz0P-PYMlXMip5kHThkB4s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo