<!-- Fonte: Graph API Reference v25.0_ Ad Account Ads.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Ads

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)

Ads belonging to this ad account.
[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)

## Reading


Ads belonging to this ad account

```
curl GET \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Parameters


| Parameter | Description |
| --- | --- |
| date_preset enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year} | Predefine date range used to aggregate insights metrics |
| effective_status list\<string\> | Filter ads by effective status |
| time_range {'since':YYYY-MM-DD,'until':YYYY-MM-DD} | Date range used to aggregate insights metrics |
| → since datetime | A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. |
| → until datetime | A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. |
| updated_since integer | Time since the Ad has been updated. |


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
| total_count unsigned int32 | Total number of Ads returned by the query Default |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 613 | Calls to this api have exceeded the rate limit. |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)

## Creating

You can make a POST request to `ads` edge from the following paths:

- [`/act_{ad_account_id}/ads`](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/)
When posting to this edge, an [Ad](https://developers.facebook.com/docs/graph-api/reference/adgroup/) will be created.

### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fads%3Fname%3DMy%2BAd%26adset_id%3D%253CAD_SET_ID%253E%26creative%3D%257B%2522creative_id%2522%253A%2522%253CCREATIVE_ID%253E%2522%257D%26status%3DPAUSED&version=v25.0)
```
POST /v25.0/act_<AD_ACCOUNT_ID>/ads HTTP/1.1
Host: graph.facebook.com

name=My+Ad&adset_id=%3CAD_SET_ID%3E&creative=%7B%22creative_id%22%3A%22%3CCREATIVE_ID%3E%22%7D&status=PAUSED
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/ads',
    array (
      'name' => 'My Ad',
      'adset_id' => '<AD_SET_ID>',
      'creative' => '{"creative_id":"<CREATIVE_ID>"}',
      'status' => 'PAUSED',
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
    "/act_<AD_ACCOUNT_ID>/ads",
    "POST",
    {
        "name": "My Ad",
        "adset_id": "<AD_SET_ID>",
        "creative": "{\"creative_id\":\"<CREATIVE_ID>\"}",
        "status": "PAUSED"
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
params.putString("name", "My Ad");
params.putString("adset_id", "<AD_SET_ID>");
params.putString("creative", "{\"creative_id\":\"<CREATIVE_ID>\"}");
params.putString("status", "PAUSED");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/ads",
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
  @"name": @"My Ad",
  @"adset_id": @"<AD_SET_ID>",
  @"creative": @"{\"creative_id\":\"<CREATIVE_ID>\"}",
  @"status": @"PAUSED",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/ads"
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
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
       "creative_id": "<CREATIVE_ID>"
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| ad_schedule_end_time datetime | An optional parameter that defines the end time of an individual ad. If no end time is defined, the ad will run on the campaign’s schedule. This parameter is only available for sales and app promotion campaigns. |
| ad_schedule_start_time datetime | An optional parameter that defines the start time of an individual ad. If no start time is defined, the ad will run on the campaign’s schedule. This parameter is only available for sales and app promotion campaigns. |
| adlabels list\<Object\> | Ad labels associated with this ad |
| adset_id int64 | The ID of the ad set, required on creation. |
| adset_spec Ad set spec | The ad set spec for this ad. When the spec is provided, adset_id field is not required. |
| audience_id string | The ID of the audience. |
| bid_amount integer | Deprecated. We no longer allow setting the bid_amount value on an ad. Please set bid_amount for the ad set. |
| conversion_domain string | The domain where conversions happen. Required to create or update an ad in a campaign that shares data with a pixel. This field will be auto-populated for existing ads by inferring from destination URLs . Note that this field should contain only the first and second level domains, and not the full URL. For example facebook.com . |
| creative AdCreative | This field is required for create. The ID or creative spec of the ad creative to be used by this ad. You can read more about creatives here . You may supply the ID within an object as follows: {"creative_id": \<CREATIVE_ID\>} or creative spec as follow: {"creative": {\"name\": \"\<NAME\>\", \"object_story_spec\": \<SPEC\>}} Required Supports Emoji |
| creative_asset_groups_spec string (CreativeAssetGroupsSpec) | creative_asset_groups_spec Supports Emoji |
| date_format string | The format of the date. |
| display_sequence int64 | The sequence of the ad within the same campaign |
| engagement_audience boolean | Flag to create a new audience based on users who engage with this ad |
| execution_options list\<enum{validate_only, synchronous_ad_review, include_recommendations}\> | Default value: Set An execution setting validate_only : when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. include_recommendations : this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section recommendations will be included in the response, but only if recommendations for this specification exist. synchronous_ad_review : this option should not be used by itself. It should always be specified with validate_only . When these options are specified, the API call will perform Ads Integrity validations, which include message language checking, image 20% text rule, and so on, as well as the validation logics. If the call passes validation or review, response will be {"success": true} . If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| include_demolink_hashes boolean | Include the demolink hashes. |
| name string | Name of the ad. Required Supports Emoji |
| priority int64 | Priority |
| source_ad_id numeric string or integer | ID of the source Ad, if applicable. |
| status enum{ACTIVE, PAUSED, DELETED, ARCHIVED} | Only ACTIVE and PAUSED are valid during creation. Other statuses can be used for update. When an ad is created, it will first go through ad review, and will have the ad status PENDING_REVIEW before it finishes review and reverts back to your selected status of ACTIVE or PAUSED . During testing, it is recommended to set ads to a PAUSED status so as to not incur accidental spend. |
| tracking_specs Object | With Tracking Specs, you log actions taken by people on your ad. See Tracking and Conversion Specs . |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, `success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 613 | Calls to this api have exceeded the rate limit. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 194 | Missing at least one required parameter |
| 500 | Message contains banned content |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 105 | The number of parameters exceeded the maximum for this operation |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#)On This Page[Ad Account Ads](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#Reading)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#Creating)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/ads/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4B0K7ZKvM2f1UHHUn7-odmDGuF8pgZRvfXYHHxBmmNQQb8CHcBlKmdwL1ylQ_aem_dJAUibWNieovhB654qktEQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4wB3j5dYEnHOSdYyB6dBBo20zJ62z7hfOlb7W88oqzli9r5O1cGAlxgn6XSA_aem_qohR2QMz1JYRx_YjRlQdbw&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5kxWqRE0vdd02kW6z4WJ7APPPVKIlLTdYVrdA2Y77hRoNSycC-REKo73Efpg_aem_-BZvFGpknOs2VJiRNVUB8Q&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR68LYv24b8SJJJD5JGpQy5BgdeXxMVJKnHXK5c-oXpt_qFoklPVUSt_t-n0zA_aem_XH6ibBJ5qaH21by3wrEVeQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6U93pu3DKyq1Z_yS6O4M_h0ZB9G21CfstXyeRH_gbxtwRKx-ZbeEtit96oxw_aem_QwBK_WMfW9HmqaVEfs1x-w&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4wB3j5dYEnHOSdYyB6dBBo20zJ62z7hfOlb7W88oqzli9r5O1cGAlxgn6XSA_aem_qohR2QMz1JYRx_YjRlQdbw&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR68lJICk-wY40xSZSqovHqH4hbzXSVbZm6wX97dygbbCc5ROH-8lHozTM1bTA_aem_t-kQCRkkwQVVkBPocl8efQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR68LYv24b8SJJJD5JGpQy5BgdeXxMVJKnHXK5c-oXpt_qFoklPVUSt_t-n0zA_aem_XH6ibBJ5qaH21by3wrEVeQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6TWSjmhUKVEOopvc4-wlxfguvFg4MUt_oax2fz7gowPugeAn3XAurifKA_Ww_aem_KNtRO6txUXhL6qrW7Ekyqg&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6TWSjmhUKVEOopvc4-wlxfguvFg4MUt_oax2fz7gowPugeAn3XAurifKA_Ww_aem_KNtRO6txUXhL6qrW7Ekyqg&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6U93pu3DKyq1Z_yS6O4M_h0ZB9G21CfstXyeRH_gbxtwRKx-ZbeEtit96oxw_aem_QwBK_WMfW9HmqaVEfs1x-w&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4fHCM4v7aEV-G6fdSYlLax9WNdUhy6E6HWLCkSyVT5CweQ_86EvXMzgFdRVw_aem_GZdMkqkCWqWeKc_EUjJBMA&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7vyuhWSULR0FttrfG0ltLRxKplFPw4bHYtzf3TWN05AyCAls7facSdGkvpNw_aem_HkiE6lRU-IOwj-s-LN8tzg&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5kxWqRE0vdd02kW6z4WJ7APPPVKIlLTdYVrdA2Y77hRoNSycC-REKo73Efpg_aem_-BZvFGpknOs2VJiRNVUB8Q&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR68lJICk-wY40xSZSqovHqH4hbzXSVbZm6wX97dygbbCc5ROH-8lHozTM1bTA_aem_t-kQCRkkwQVVkBPocl8efQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6U93pu3DKyq1Z_yS6O4M_h0ZB9G21CfstXyeRH_gbxtwRKx-ZbeEtit96oxw_aem_QwBK_WMfW9HmqaVEfs1x-w&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR68LYv24b8SJJJD5JGpQy5BgdeXxMVJKnHXK5c-oXpt_qFoklPVUSt_t-n0zA_aem_XH6ibBJ5qaH21by3wrEVeQ&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5kxWqRE0vdd02kW6z4WJ7APPPVKIlLTdYVrdA2Y77hRoNSycC-REKo73Efpg_aem_-BZvFGpknOs2VJiRNVUB8Q&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7vyuhWSULR0FttrfG0ltLRxKplFPw4bHYtzf3TWN05AyCAls7facSdGkvpNw_aem_HkiE6lRU-IOwj-s-LN8tzg&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6TWSjmhUKVEOopvc4-wlxfguvFg4MUt_oax2fz7gowPugeAn3XAurifKA_Ww_aem_KNtRO6txUXhL6qrW7Ekyqg&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6YgKTyQ-T8g5YaufHNDpH5H9eFzOyxcar77iO5m16e2I6wmqS3wm1cf2YXujIfSU7zsqxTzROwJk7Hp8EAko0tAtZtozA6IblL9UfoHhpmHW09hVZAeXO67Kf4PHlnUZU8_SKbfmpl1WDzsbep-DkwcpY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo