<!-- Fonte: Graph API Reference v25.0_ Ad Copies.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Copies

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)

The Marketing API has it is own rate limiting logic. If you are encountering errors mentioning a reached limit, see [Rate Limiting](https://developers.facebook.com/docs/marketing-apis/rate-limiting).
 [○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)

## Reading


The copies of this ad.


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-id%7D%2Fcopies&version=v25.0)
```
GET /v25.0/{ad-id}/copies HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-id}/copies',
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
    "/{ad-id}/copies",
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
    "/{ad-id}/copies",
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
                               initWithGraphPath:@"/{ad-id}/copies"
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
| date_preset enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year} | Preset date range used to aggregate insights metrics |
| effective_status list\<string\> | Filter Ads by effective status |
| time_range {'since':YYYY-MM-DD,'until':YYYY-MM-DD} | Time range used to aggregate insights metrics |
| → since datetime | A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. |
| → until datetime | A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. |
| updated_since integer | Filter ads by updated since time |


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

A list of [Ad](https://developers.facebook.com/docs/graph-api/reference/adgroup/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=insights`).


| Field | Description |
| --- | --- |
| insights Edge\<AdsInsights\> | Analytics summary for all objects |
| total_count unsigned int32 | Total number of objects Default |


### Error Codes


| Error | Description |
| --- | --- |
| 104 | Incorrect signature |

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)

## Creating


### Targeting DSA Regulated Locations (European Union)


To copy an ad set targeted in the European Union's Digital Services Act (DSA) regulated locations, please set the payor/beneficiary information first. Otherwise the copying request may respond with one of the following errors: **Payor missing error**

```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": "{\"blame_field_specs\":[[\"dsa_payor\"]]}",
    "error_subcode": 3858079,
    "is_transient": false,
    "error_user_title": "No payor provided in DSA regulated region",
    "error_user_msg": "The DSA requires ads to provide payor information in regulated regions. Updating/creating ad needs to provide payor of the ad.",
    "fbtrace_id": "fbtrace_id"
  },
  "__fb_trace_id__": "fbtrace_id",
  "__www_request_id__": "request_id"
}
```
**Beneficiary missing error**
```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": "{\"blame_field_specs\":[[\"dsa_beneficiary\"]]}",
    "error_subcode": 3858081,
    "is_transient": false,
    "error_user_title": "No payor/beneficiary provided in DSA regulated location",
    "error_user_msg": "The DSA requires ads to provide beneficiary information in regulated regions. Updating/creating ad needs to provide beneficiary of the ad.",
    "fbtrace_id": "fbtrace_id"
  },
  "__fb_trace_id__": "fbtrace_id",
  "__www_request_id__": "request_id"
}
```


### Creative Parameters


When making a copy of an ad, you may overwrite fields on the creative spec by using the `creative_parameters` argument. Currently, this supports overwriting the API spec at the top-level parameter level, i.e. when `creative_parameter` supplied, the new creative will use all of the newly provided value for any valid parameter. Otherwise, the values from the source ad’s creative will be used.


Find out more about the available fields in our [documentation for ad creatives](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adcreatives/).


#### Creative spec overwrite example


    Original creative

```
{
  "body": "original ad body",
  "degrees_of_freedom_spec": {
    "creative_features_spec": {
      "text_optimizations": {
        "enroll_status": "OPT_IN"
      },
      "inline_comment": {
        "enroll_status": "OPT_IN"
      }
    }
  },
  "image_url": "https://example.com/my-image-url",
  "name": "original ad name",
  "title": "original ad body"
}
```

    Supplied input for copy operation

```
{
  "degrees_of_freedom_spec": {
    "creative_features_spec": {
      "text_optimizations": {
        "enroll_status": "OPT_IN"
      },
      "image_touchups": {
        "enroll_status": "OPT_IN"
      }
    }
  },
  "image_url": "https://example.com/my–other-image-url",
  "url_tags": "source=fb_ad"
}
```

    Resulting creative

```
{
  "body": "original ad body",
  "degrees_of_freedom_spec": {
    "creative_features_spec": {
      "text_optimizations": {
        "enroll_status": "OPT_IN"
      },
      "image_touchups": {
        "enroll_status": "OPT_IN"
      }
    }
  },
  "image_url": "https://example.com/my–other-image-url",
  "name": "original ad name",
  "title": "original ad body",
  "url_tags": "source=fb_ad"
}
```


Note the following:


- `body`, `name`, `title` are not supplied in the input spec, so they are carried over from the original
- `url_tags` is defined in the input spec, but not in the original spec. It is defined in the new spec
- `image_url `is defined in both. The input value is used in the new spec.
- `degrees_of_freedom_spec` defines opt-ins for `text_optimizations` and `inline_comment` in the original spec, and only `text_optimizations` and `image_touchups` in the new spec. The input `degrees_of_freedom_spec` completely overrides the old one, and previously defined sub-fields are not used.
You can make a POST request to `copies` edge from the following paths:

- [`/{ad_id}/copies`](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/)
When posting to this edge, an [Ad](https://developers.facebook.com/docs/graph-api/reference/adgroup/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| adset_id numeric string or integer | Single ID of an adset object to make the parent of the copy. Ignore if you want to keep the copy under the original adset parent. |
| creative_parameters AdCreative | Creative inputs which will be used to construct the creative in the new ad. Overwrites happen at the top level. If no input is provided, the new ad will be created with an identical ad creative. If some input is provided, those parameters will be assigned to the ad creative created by this API call. Accepts all ad creative parameters as specified in https://developers.facebook.com/docs/marketing-api/reference/ad-account/adcreatives/ Supports Emoji |
| rename_options JSON or object-like arrays | Rename options |
| → rename_strategy enum {DEEP_RENAME, ONLY_TOP_LEVEL_RENAME, NO_RENAME} | Default value: ONLY_TOP_LEVEL_RENAME DEEP_RENAME : will change this object's name and children's names in the copied object. ONLY_TOP_LEVEL_RENAME : will change the this object's name but won't change the children's name in the copied object. NO_RENAME : will change no name in the copied object |
| → rename_prefix string | A prefix to copy names. Defaults to null if not provided. |
| → rename_suffix string | A suffix to copy names. Defaults to null if not provided and appends a localized string of - Copy based on the ad account locale. |
| status_option enum {ACTIVE, PAUSED, INHERITED_FROM_SOURCE} | Default value: PAUSED ACTIVE : the copied ad will have active status. PAUSED : the copied ad will have paused status. INHERITED_FROM_SOURCE : the copied ad will have the parent status. |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `copied_ad_id` in the return type. Struct  {`copied_ad_id`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#)On This Page[Ad Copies](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#Creating)[Targeting DSA Regulated Locations (European Union)](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#targeting-dsa-regulated-locations--european-union-)[Creative Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#-creative-parameters-)[Parameters](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/adgroup/copies/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7JzEsWTOL7iW7F1p_WEkcNS6JjtGwYpFIsJuBlcOovrMJF_0hsPcjqWOdfxw_aem_TwMU60bMLF8ovZffXzkrog&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR41WEeImgICUOOijVnHQXsmrr5J7SAajT2h6CzWICBC4ae6BaQOjj8HhiyiEQ_aem_eRrdNF0lY8upirvSgfz_aA&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR495XBrQFDN_sQkuolt93Y_Mj0miDWM4CxzU61Eu1tX209ijR7mOWg-o8HWPA_aem_2kIF9fK5foWCIv4nOPpm3A&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-bDm1dGplfUno-k6BcSmB5HWvE4_O6qUQGLRCI5a5f7NOM7XCKAkFF_pQiw_aem_fYzBAmApL1ygvSDNc0nF9w&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Z1akm2QEy6EVQrAohP_NlaW21P9Rh3L336UwxO5QJqxdcUfEzEKreUvCthw_aem_BbtMeLwMVFzduELQdhrTiw&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4r89xZjuw1U5xhmLox8-YOrt25SFL3wsv7riozxvq5n8hlO9mROAsWGgdHPg_aem_Hq0-AdoqfPIMN_gx616VWQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4r89xZjuw1U5xhmLox8-YOrt25SFL3wsv7riozxvq5n8hlO9mROAsWGgdHPg_aem_Hq0-AdoqfPIMN_gx616VWQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5eirNOdR-47G0HkSVQ6IvuKkZqFs91jmKf9-9SjJKK-9Ms_GHUGoL6gvT5vQ_aem_L4F6qqXqKYkDh9wohEABCg&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4n8y1mguRY-YPV3uLOqJtGTMM0P_qhgqOoUWoqIVXAE4kREEV1i-M3Q1F1dg_aem_XPjLMWjrPHJDQQogf2JFcw&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Z1akm2QEy6EVQrAohP_NlaW21P9Rh3L336UwxO5QJqxdcUfEzEKreUvCthw_aem_BbtMeLwMVFzduELQdhrTiw&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4r89xZjuw1U5xhmLox8-YOrt25SFL3wsv7riozxvq5n8hlO9mROAsWGgdHPg_aem_Hq0-AdoqfPIMN_gx616VWQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4u3Cj7QiH1XA5Kd_RJ0ofVN8TuGi1InppSv8Jx4Vnw4TpBWKxvYiGn8MrfpA_aem_fuI86z2ac8artugS_pvhdQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5eirNOdR-47G0HkSVQ6IvuKkZqFs91jmKf9-9SjJKK-9Ms_GHUGoL6gvT5vQ_aem_L4F6qqXqKYkDh9wohEABCg&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7tBXNYgCcWqEv8835hJwBaWbmDou72ymZBlp7UVlCU4-x52Nfc8AumX1KCfg_aem_u3oy5V7b8rD4X3duW31xUw&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7JzEsWTOL7iW7F1p_WEkcNS6JjtGwYpFIsJuBlcOovrMJF_0hsPcjqWOdfxw_aem_TwMU60bMLF8ovZffXzkrog&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4r89xZjuw1U5xhmLox8-YOrt25SFL3wsv7riozxvq5n8hlO9mROAsWGgdHPg_aem_Hq0-AdoqfPIMN_gx616VWQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4u3Cj7QiH1XA5Kd_RJ0ofVN8TuGi1InppSv8Jx4Vnw4TpBWKxvYiGn8MrfpA_aem_fuI86z2ac8artugS_pvhdQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR41WEeImgICUOOijVnHQXsmrr5J7SAajT2h6CzWICBC4ae6BaQOjj8HhiyiEQ_aem_eRrdNF0lY8upirvSgfz_aA&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR41WEeImgICUOOijVnHQXsmrr5J7SAajT2h6CzWICBC4ae6BaQOjj8HhiyiEQ_aem_eRrdNF0lY8upirvSgfz_aA&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4u3Cj7QiH1XA5Kd_RJ0ofVN8TuGi1InppSv8Jx4Vnw4TpBWKxvYiGn8MrfpA_aem_fuI86z2ac8artugS_pvhdQ&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6rPC9qfCGl-VMyBlQQjOOcRxVF6bpEtR6JJzOXbBCk_aDOM8n2z6Zjp35O9sALiV2mtqWMcgAvd2SOwdXIYlHlxJiopvcEpPjCSPEBiv4L2ffG0uBOPRq25fi6qLrPD9YMib8c17eSv6N7u1i3OQYbUpU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo