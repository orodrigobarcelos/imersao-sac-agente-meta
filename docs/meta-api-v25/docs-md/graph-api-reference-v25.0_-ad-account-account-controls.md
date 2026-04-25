<!-- Fonte: Graph API Reference v25.0_ Ad Account Account Controls.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Account Controls

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Reading


Get default fields on an [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) node associated with this [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account). Refer to the [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) reference for a list of these fields and their descriptions.


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Faccount_controls&version=v25.0)
```
GET /v25.0/{ad-account-id}/account_controls HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/account_controls',
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
    "/{ad-account-id}/account_controls",
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
    "/{ad-account-id}/account_controls",
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
                               initWithGraphPath:@"/{ad-account-id}/account_controls"
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

A list of [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Creating

You can make a POST request to `account_controls` edge from the following paths:

- [`/act_{ad_account_id}/account_controls`](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/)
When posting to this edge, an [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| audience_controls JSON or object-like arrays | audience_controls Required |
| → age_min int64 |  |
| → geo_locations JSON or object-like arrays |  |
| → excluded_geo_locations JSON or object-like arrays |  |
| → exclusions JSON or object-like arrays |  |
| placement_controls JSON or object-like arrays | This field contains another field called placement_exclusion that provides information on which placements need to be excluded while targeting. All the other placements will be included. Each placement is denoted by a string that concatenates the publisher platform of the placement and a position inside the publisher platform, separated by an underscore. What is provided as parameter is a list of placements. For e.g. If we want to exclude the rewarded videos position from the audience network publisher platform, we provide the field as follows: { "placement_controls": { "placement_exclusions": ["audience_network_rewarded_video"] } } Only a few placements are allowed to be excluded: audience_network_classic (native, banner & interstitial positions of audience network) audience_network_rewarded_video (rewarded videos of audience network) audience_network_instream_video (instream videos of audience network) facebook_marketplace (marketplace section inside facebook) facebook_rhc (right hand column inside facebook) |
| → placement_exclusions array\<enum {AUDIENCE_NETWORK_CLASSIC, AUDIENCE_NETWORK_REWARDED_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO, FACEBOOK_MARKETPLACE, FACEBOOK_RIGHT_HAND_COLUMN}\> |  |
| → campaign_ids_to_set_ap array\<numeric string\> |  |


### Return Type

 Struct  {`id`: string, `success`: bool, `error_code`: string, `error_message`: string, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2641 | Your ad includes or excludes locations that are currently restricted |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Updating


Use the [`POST /act_<AD_ACCOUNT_ID>/account_controls`](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Creating) endpoint to update the [AdAccountBusinessConstraints](https://developers.facebook.com/docs/marketing-api/reference/ad-account-business-constraints/) associated with this [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account).
 You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#)On This Page[Ad Account Account Controls](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/account_controls/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7P1NXMnOfMqpJpvBRGXrRhvybhahmWUqNjXsJpjV7tinumRMm-9e1-YQOimw_aem_aJu4DIUUpxEMdV17jbcF5w&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5wcqGUMjyEkOZKRcDNnH0kMLFg7d0qhDYd6wrTGw7Xz8UsBUwm3gewq2S_FA_aem_W98hyC74Zf4fBXeVdhhLXg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7lrJRfx9ZbUtBJKYPXXZEMbZM5iS1B3D4wPMA2W-iXSniPlP0GjyfPqZXDzw_aem_goq_WcKb6t5C13_cxyuouA&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7vOwuXzjb3u228FIp_eLGoq5_eAMVocX7yyXK0Mg3U5Lh9tBsxBD5Gnu5I6g_aem_rVKD1xMoVhR_Ipb7AcqQoQ&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7P1NXMnOfMqpJpvBRGXrRhvybhahmWUqNjXsJpjV7tinumRMm-9e1-YQOimw_aem_aJu4DIUUpxEMdV17jbcF5w&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7lrJRfx9ZbUtBJKYPXXZEMbZM5iS1B3D4wPMA2W-iXSniPlP0GjyfPqZXDzw_aem_goq_WcKb6t5C13_cxyuouA&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4B0k515W9AFF0qD__2ACd-SbFaNxWr52QF28P3cZgTgeFOqMGa3tZxrTpTlQ_aem_pWgQIlgrh4HElvAqefyVww&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7lrJRfx9ZbUtBJKYPXXZEMbZM5iS1B3D4wPMA2W-iXSniPlP0GjyfPqZXDzw_aem_goq_WcKb6t5C13_cxyuouA&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4B0k515W9AFF0qD__2ACd-SbFaNxWr52QF28P3cZgTgeFOqMGa3tZxrTpTlQ_aem_pWgQIlgrh4HElvAqefyVww&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7f8TpZGHEBLAyiNd0sW3r1KMa_0ERxcuBCnxf34VdmNgZF3IeUNZMlIfVILQ_aem_1OtwpWX-ysNZGSyKpRUDmg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gP48sJQ6A7DJKyWONFM2l8svh6HLOUwcFuyS3DDVgc3xO2skXzIba4bWXiA_aem_yCkrdM6PfAwUNsaLtzY8Bg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6JJNeVY22GISQVBeXqBQ7ddlVq7GUkZXcP9CN_Z--6rWGXWVK1ZgWOK7C4gw_aem_l0mhpESojNChR5VWYdgV1w&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gP48sJQ6A7DJKyWONFM2l8svh6HLOUwcFuyS3DDVgc3xO2skXzIba4bWXiA_aem_yCkrdM6PfAwUNsaLtzY8Bg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7P1NXMnOfMqpJpvBRGXrRhvybhahmWUqNjXsJpjV7tinumRMm-9e1-YQOimw_aem_aJu4DIUUpxEMdV17jbcF5w&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4B0k515W9AFF0qD__2ACd-SbFaNxWr52QF28P3cZgTgeFOqMGa3tZxrTpTlQ_aem_pWgQIlgrh4HElvAqefyVww&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5wcqGUMjyEkOZKRcDNnH0kMLFg7d0qhDYd6wrTGw7Xz8UsBUwm3gewq2S_FA_aem_W98hyC74Zf4fBXeVdhhLXg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5wcqGUMjyEkOZKRcDNnH0kMLFg7d0qhDYd6wrTGw7Xz8UsBUwm3gewq2S_FA_aem_W98hyC74Zf4fBXeVdhhLXg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5wcqGUMjyEkOZKRcDNnH0kMLFg7d0qhDYd6wrTGw7Xz8UsBUwm3gewq2S_FA_aem_W98hyC74Zf4fBXeVdhhLXg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7lrJRfx9ZbUtBJKYPXXZEMbZM5iS1B3D4wPMA2W-iXSniPlP0GjyfPqZXDzw_aem_goq_WcKb6t5C13_cxyuouA&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gP48sJQ6A7DJKyWONFM2l8svh6HLOUwcFuyS3DDVgc3xO2skXzIba4bWXiA_aem_yCkrdM6PfAwUNsaLtzY8Bg&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6MAVtAVy1RSTCmAalgmCTJ3jCU1W5GURinntOCVoMgya52gpwZo4xvGQkiVs9X_3o4mszR4QwXbrM0F1Z0T3YrVI-xr3F4s9R5bL0hwbivQa5YdlZs4KL4PghTn0NjNeP_suwrHvrgzir4aJc9oMvH_DM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo