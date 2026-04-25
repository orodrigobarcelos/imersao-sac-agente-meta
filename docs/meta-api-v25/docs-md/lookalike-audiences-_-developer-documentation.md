<!-- Fonte: Lookalike Audiences _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Lookalike Audiences

Updated: Nov 7, 2025Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences that may suggest information not permitted under our terms. For example, any custom audience or lookalike audience suggesting specific health conditions (e.g., “arthritis”, “diabetes”) or financial status (e.g., “credit score”, “high income”) will be flagged and prevented from being used to run ad campaigns.**What these restrictions mean for your campaigns:**

- You won’t be able to use flagged custom audiences when creating new campaigns.
- If you have an active campaign using flagged custom audiences, you should edit or pause it and choose a different audience to avoid performance and delivery issues.
**For API developers:**

- Beginning September 2, 2025, `operation_statu`s will return `471` to signal if your custom audiences have been flagged.
More information on this update and how to resolve flagged custom audiences can be found [here⁠](https://www.facebook.com/business/help/1055828013359808).Target people most like your established customers. Lookalike audiences take several sets of people as “seeds” then Facebook builds an audience of similar people. You can use lookalikes for any business objective: Targeting people similar your customers for fan acquisition, site registration, off-Facebook purchases, coupon claims, or simply to drive awareness of a brand.Seed audiences can be:

- [Existing Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences#custom-audience)
- [Campaign or Ad Set conversions](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences#campaign)
- [Page fans](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences#page_fan_lookalikes)
Facebook refreshes members in a lookalike every 3 days if the lookalike belongs to an adgroup.

## Create

**Lookalike audiences can take 1-6 hours to fully populate.** While audiences populate, you can create and run ad sets targeting the audience. Once the audience is ready, Facebook delivers to people populated in the audience and ads delivery will catchup and work as normal. See [Delivery Status](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences#delivery-status). Create a new lookalike audience at: `https://graph.facebook.com/{API_VERSION}/act_{AD_ACCOUNT_ID}/customaudiences`.Example creation call for lookalike from a custom audience:
```
curl \
  -F 'name=My lookalike audience' \
  -F 'subtype=LOOKALIKE' \
  -F 'origin_audience_id=<SEED_AUDIENCE_ID>' \
  -F 'lookalike_spec={"type":"similarity","country":"US"}' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
To create lookalike audiences with [PHP Ads SDK⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-php-ads-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0) or [Python Ads SDK⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-python-ads-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0), use `CustomAudience`.The response contains:

| Name | Description |
| --- | --- |
| id type: integer | ID of lookalike audience |


### Custom Audience Lookalike

If you have a Custom Audience with at least 100 people, you can build lookalike audiences based on it. This includes Custom Audiences for your Website and Custom Audiences for your Mobile App.

| Name | Description |
| --- | --- |
| name type: string | Required. Custom Audience name |
| origin_audience_id type: long | Required. ID of Custom Audience. Origin audiences must have at least 100 members. |
| lookalike_spec type: array | Required. See description below. |
| lookalike_spec.type type: string | Required. Set either type or ratio . similarity or reach |
| lookalike_spec.starting_ratio type: float | Optional. Start percentage for lookalike. For example, starting_ratio 0.01 and ratio 0.02 creates a lookalike from 1% to 2% of a lookalike segment. starting_ratio must be less than ratio |
| lookalike_spec.ratio type: float | Required. Set either type or ratio . 0.01 - 0.20 incremented by 0.01. Top x% of original audience in a selected country |
| lookalike_spec.allow_international_seeds type: boolean | Optional. At least 100 seed audience members from a country. If not, allow_international_seeds set to true means Facebook finds this minimum number of audience members in another country. Default false . |
| lookalike_spec.country type: string | Required. Set country or location_spec . Find lookalike audience members in this country |
| lookalike_spec.location_spec type: array | Required. Either country or location_spec . Find audience members in these locations. List of countries or country groups such as Asia |
| lookalike_spec.location_spec.geo_locations type: array | Required. At least one entry under countries or country_groups . Include these locations |
| lookalike_spec.location_spec.geo_locations.countries type: array of strings | Optional. Target countries. Array of country codes, see Targeting Search API, Countries . Example : 'countries': ['US'] |
| lookalike_spec.location_spec.geo_locations.country_groups type: array of strings | Optional. Target countries in global regions and free trade areas. Array of country group codes. For full options, see Targeting, Location, country_groups and Targeting Search, country_groups . Example : 'country_groups': ['asia','mercosur'] |
| lookalike_spec.location_spec.excluded_geo_locations type: array | Optional. Locations to exclude |
| lookalike_spec.location_spec.excluded_geo_locations.countries type: array of strings | Optional. Same as countries under geo_locations |
| lookalike_spec.location_spec.excluded_geo_locations.country_groups type: array of strings | Optional. Same as country_groups under geo_locations |


### Types

Optimize your audience for “Similarity” or “Greater reach”.

- Similarity - Audience includes the top 1% of people in a selected country who are most similar to the seed Custom Audience. The new audience’s reach is smaller, matching is more precise.
- Greater Reach - Audience includes the top 5% of people in the selected country that are similar to the seed Custom Audience, but with a less precise match.
**Instead of using types you can manually set `ratio` to represent the top x% of the audience in the selected country.** `ratio` should be from 1%-20% and in intervals of 1%.

### Campaign or Ad Set Conversion Lookalikes

Facebook has campaign and ad set conversion lookalikes to target people similar to those converting from previous or current campaigns or ad sets; for example, campaigns or ads that are optimizing for conversions. We measure conversions based on a campaign or ad set type in [Conversion Specs](https://developers.facebook.com/documentation/ads-commerce/marketing-api/tracking-specs). For example, target people that took action on your website or installed your app within 28 days of clicking your ad.
```
curl \
  -F 'subtype=LOOKALIKE' \
  -F 'lookalike_spec={
    "origin_ids": "<CAMPAIGN_ID>",
    "starting_ratio": 0.03,
    "ratio": 0.05,
    "conversion_type": "campaign_conversions",
    "country": "US"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
You need at least 100 unique conversions from your campaigns or ad sets. More converters result in a better predictive model and we suggest 200 or more members who converted. You should also select campaigns or ad sets with similar objectives.To create this lookalike, specify one or more of your campaigns or ad sets. For example, specify one campaign and two ad sets of another campaign.Facebook uses up to 180 days of past conversion data and identifies people converting on your campaigns and ad sets as examples. We train prediction model then create a lookalike audience. Facebook constantly updates the underlying prediction model as campaigns or ad sets get new conversions.

| Name | Description |
| --- | --- |
| lookalike_spec type: array | Required. See description below. |
| lookalike_spec.origin_ids type: array of integers | Required. Array of ad object ids. People who convert on these ads are used to model a lookalike. One or more campaign IDs or ad set IDs , or a mix of them. |
| lookalike_spec.conversion_type type: string | Required. campaign_conversions . Indicates audience is a campaign conversion lookalike |
| lookalike_spec.country type: string | Required. Country to find lookalike members. |
| lookalike_spec.allow_international_seeds type: boolean | Optional. At least 100 seed audience members from a country. If not, allow_international_seeds set to true means Facebook finds this minimum number of members in another country. Defaults to false . |
| lookalike_spec.starting_ratio type: float | Optional. Start percentage for lookalike. For example, starting_ratio 0.01 and ratio 0.02 creates a lookalike from 1% to 2% of a lookalike segment. starting_ratio must be less than ratio |
| lookalike_spec.ratio type: float | Required. Range of 0.01 - 0.20 . Top x% of original audience in the selected country. |

Currently, the following campaign conversion types are eligible for Lookalike Audiences:

- Link clicks
- Offer ads
- Page likes
- Canvas App installs
- Event responses
- Post engagement
- Website conversions
- Mobile app installs
- Mobile app engagement
- Video views
- Local awareness


### Page Fan Lookalikes

Create a lookalike audience based on people who like your Page:
```
curl \
  -F 'subtype=LOOKALIKE' \
  -F 'lookalike_spec={
    "ratio": 0.01,
    "country": "US",
    "page_id": "<PAGE_ID>",
    "conversion_type": "page_like"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


| Name | Description |
| --- | --- |
| lookalike_spec type: array | Required. See description below. |
| lookalike_spec.page_id type: int | Required. Facebook ID of the page whose fans will be used for the lookalike |
| lookalike_spec.conversion_type type: string | Required. page_like - Indicates that this is a page fan lookalike |
| lookalike_spec.country type: string | Required. The country to find the lookalike people. The default is ‘US’ |
| lookalike_spec.allow_international_seeds type: boolean | Optional. You need at least 100 seed audience members from a country. If this minimum is not satisfied, allow_international_seeds set to true means Facebook finds this minimum number of seed audience members in another country. Defaults to false . |
| lookalike_spec.starting_ratio type: float | Optional. Starting percentage of the lookalike. For example, a starting_ratio of 0.01 and a ratio of 0.02 would create a lookalike from the 1% to 2% lookalike segment. The value of starting_ratio should always be less than that of ratio |
| lookalike_spec.ratio type: float | Required. Range 0.01-0.20. How much of the country the lookalike should target. |


### Flagged custom and lookalike audiences

If the seed audience is flagged with an `operation_status` of `471`, attempts to create a lookalike audience based on the seed audience will fail with an error.
```
{  "error": {    "message": "Invalid parameter",    "code": 100,    "error_subcode": 1713232,    "error_user_title": "Seed audience restricted",    "error_user_msg": "The seed audience you selected cannot be used to create a lookalike audience because it has integrity restrictions. Please use a different seed audience",  },}
```


## Targeting

Targeting lookalikes is the same as targeting **Custom Audiences**. See [Custom Audiences, Targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience#targeting). This also applies for exclusion targeting and conjunctive `AND` targeting. To target when you create an ad:
```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "custom_audiences": [{"id":"<LOOKALIKE_AUDIENCE_ID>"}],
    "geo_locations": {"countries":["US"]}
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
More examples at [Targeting Specs](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting).

## Managing Audiences

Get details on custom audiences used to create lookalikes as well as lookalikes. We return the same fields as [Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience#read). Below is a sample response for a Custom Audience used to create lookalikes. `lookalike_audience_ids` specifies which lookalike audiences were generated from this audience.
```
{
  "id": "6006164557194",
  "account_id": 12345,
  "approximate_count": 816400,
  "lookalike_audience_ids": [
    6006183285954,
    6006183285955
  ],
  "name": "Boys Apparel",
  "parent_audience_id": 0,
  "parent_category": "Custom",
  "status": "ready",
  "subtype": "CUSTOM",
  "type": 4,
  "type_name": "Advertiser Generated",
  "time_updated": 1362439491
},
```
Lookalike audiences contain a `subtype` of 2. We also return `lookalike_spec`, an array in this format:

| Name | Description |
| --- | --- |
| type type: string | similarity , reach or custom_ratio - Always returned |
| starting_ratio type: float | Returned if starting_ratio specified |
| ratio type: float | Multiple of 0.01 . Returned if type is custom_ratio |
| country type: string | Country code |
| origin type: array | See description below. |
| origin.deleted type: boolean | true , Returned when the origin deleted |
| origin.id type: int | Origin ID |
| origin.name type: string | Origin name |
| origin.type type: string | custom_audience or page |
| target_countries type: array of strings | All countries used to create audience |

Another audience below where `subtype` is `LOOKALIKE`:
```
{
 "id": "6006183285954",
 "account_id": 12345,
 "approximate_count": 1782100,
 "name": "Boys Apparel_lookalike_US_Similarity",
 "origin_audience_id": 6006567610735,
 "parent_audience_id": 0,
 "parent_category": "Custom",
 "status": "ready",
 "subtype": "LOOKALIKE",
 "type": 4,
 "type_name": "Advertiser Generated",
 "time_updated": 1362506552
},
```


### Delivery Status

After you create a lookalike audience we return a Custom Audience ID. It can take about one hour to fully populate an audience. You can get the status at: `/{lookalike_audience_ID}?fields=delivery_status`. This returns a JSON response with `delivery_status` or code 200 if an audience populates:
```
"delivery_status": {
  "code": 200,
  "description": "This audience is ready for use."
},
```
For testing, you should check the status of the list with [Ads Manager⁠](https://www.facebook.com/ads/audience_manager/).To delete a lookalike audience, you do the same as you do for [Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience).

## Inactive Audiences

A Lookalike audience is considered inactive when it has not been used in active ads for 90 days. Inactive lookalike audiences have different `approximate_count`, `operation_status`, and `delivery_estimate`.

| Field | Changes for Inactive Lookalikes |
| --- | --- |
| approximate_count | You are not able to retrieve a size. A call for this field returns -1 for inactive lookalikes. |
| operation_status | 450 : This lookalike audience is inactive. It can be used in ads but will not have an estimate till the campaign is published. 100 : If an audience hasn’t been used in an active ad set for over 2 years, it will begin to expire. Expiring audiences that remain unused for 90 days will be deleted. 471 : The lookalike audience has been flagged for integrity reasons. |
| delivery_estimate | You are not able to retrieve a delivery estimate. A call for this field returns -1 for inactive lookalikes. This field is available under Ad Account and Ad Set nodes. Both exhibit the same behavior for inactive lookalikes. |
| delete_time | When an audience’s operation_status has been marked as expiring (code 100 ), the delete_time field tells you in Unix time when the audience will be deleted. |

You can still start a campaign using an inactive lookalike audience. The reach estimate information is available after your new ad gets published.

### Deletion

For all advertisers beginning June 8, 2021 and going forward, we will automatically be moving audiences to the “Expiring Audience” stage once they have been inactive for over two years. This means that once an audience meets the threshold of not being used in an active ad set for over two years, it will be automatically flagged as an “Expiring Audience”, and the `delete_time` field will be marked with the estimated deletion time (i.e., 90 days from the time of flagging) when the audience is scheduled to be deleted.You will then be able to either proactively delete the audience or use the audience in an active ad set to prevent deletion. You can see which of your audiences are in the expiring stage at any time by filtering on their `operation_status` or `delete_time` fields.For more information, see the [Custom Audiences Overview](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/overview#custom-audiences-deletion) documentation.

## Best Practices


- Seed Custom Audience - Make it as large as possible so we have enough data to find similar people.
- Combine Lookalikes - With other Facebook’s targeting for additional demographics or interests.
- If your seed audience has attributes such as gender or geography, the lookalikes generate may not adhere to those attributes.


## Upcoming Lookalike Changes

**UPDATED APRIL 28, 2021:** The removal of the`location_spec` and `country` parameters from lookalike audience creation is currently delayed. Updates on when this change will go into effect will be forthcoming.We will remove the `location_spec` and `country` parameters from lookalike audience creation. The location for the lookalikes will be defined by the country location in the campaign’s targeting specification. The target location won’t be a part of the lookalike audience specification. The reach estimate of the campaign using a newly created lookalike will be populated only in a few hours after the ad being published.There will be no impact on existing campaigns given this change. This requirement will only impact new and edited campaigns.We will automatically convert legacy lookalike audiences into new lookalikes without target locations.

### Changes to Lookalike Creation


#### Location parameter changes

**Endpoint:** `act_{AD_ACCOUNT_ID}/customaudiences`**Example Request**
```
curl POST \
  -F 'name=My lookalike audience' \
  -F 'subtype=LOOKALIKE' \
  -F 'origin_audience_id=<SEED_AUDIENCE_ID>' \
  -F ‘lookalike_spec={
  "is_financial_service":false,
  "allow_international_seeds":true,
  "ratio":0.01,
  "type":"custom_ratio"}
    ’}\
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/act_<AD_ACCOUNT_ID>/customaudiences
```
The following parameters will be ignored if passed during creation:

- `lookalike_spec.country`
- `lookalike_spec.location_spec`
- `lookalike_spec.location_spec.geo_locations`
- `lookalike_spec.location_spec.geo_locations.countries`
- `lookalike_spec.location_spec.geo_locations.country_groups`
- `lookalike_spec.location_spec.excluded_geo_locations`
- `lookalike_spec.location_spec.excluded_geo_locations.countries`
- `lookalike_spec.location_spec.excluded_geo_locations.country_groups`


#### Size parameter changes

**Endpoint:** `act_{AD_ACCOUNT_ID}?fields=approximate_count`There will be no size associated with new lookalike audiences, and the `approximate_count` field will return `-1` for all lookalike audiences.**Example Response**
```
{
    "approximate_count": -1,
    "id": "6126486105659",
}
```


#### Delivery and operation status

**Endpoints:**

- `{AD_ACCOUNT_ID}?fields=delivery_status`
- `{AD_ACCOUNT_ID}?fields=operation_status`
The `delivery_status` field for old lookalike audiences with location specifications will return a code `400` with a `This audience is disabled.` description. For new lookalike audiences it will return a code `200` response.The `operation_status` field will return a retirement notification for old lookalike audiences with location specifications. For new lookalike audiences it will return a code `200` and `Normal` description response.See [Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience) for more information about these fields.

### Changes to Ad Sets


#### Ad creation and editing

We will automatically upgrade ads to use new lookalikes if the targeting of the existing campaigns containing the legacy lookalike is edited. The legacy lookalike will no longer be available for use in newly created ad campaigns.With location specifications removed from lookalike audience creation, you will need to set location targets during Ad Set creation. Attempting to create an Ad Set without location targeting will result in an error.All the above changes will also be applicable when audiences are included in `excluded_custom_audiences`,  `flexible_spec`, and `exclusions` in the campaign.**Endpoint:** `act_{AD_ACCOUNT_ID}/adsets`**Example Request**
```
curl POST \
  -F 'targeting={
        "geo_locations":{
            "countries":["US"],
        },
        "age_min":25,
        "age_max":40,
        "custom_audiences":[{"id": <CUSTOM_AUDIENCE_ID>}]
  ‘}\
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/act_<AD_ACCOUNT_ID>/adsets
```
Attempting to create an Ad Set without location targeting will result in an error.
```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": {
      "blame_field_specs": [["targeting" ] ]
    },
    "error_subcode": 192342134,
    "is_transient": false,
    "error_user_title": "Missing Location while using Lookalike",
    "error_user_msg": "You need to use a location with your lookalike    audience.",
    "fbtrace_id": "F78cCCJoZPx"
  },
  "__fb_trace_id__": "F78cCCJoZPx",
  "__www_request_id__": "AcwlIc7_uK5uTXjzjIa38yc"
}
```
If you try to edit an Ad Set containing a shared legacy lookalike and don’t have a corresponding new lookalike in the owning ad account, an error will occur. Request the owning ad account share the new lookalike audience with you to resolve the issue.
```
{
  "error": {
    "message": "Invalid parameter",
    "type": "FacebookApiException",
    "code": 100,
    "error_data": {
      "blame_field_specs": [["targeting" ] ]
    },
    "error_subcode": 192342135,
    "is_transient": false,
    "error_user_title": "",
    "error_user_msg": "Please ask the owner of the audience 1234 to share the new lookalike which does not contain location with you. You will be able to use the new audience"
    "fbtrace_id": "F78cCCJoZPx"
  },
  "__fb_trace_id__": "F78cCCJoZPx",
  "__www_request_id__": "AcwlIc7_uK5uTXjzjIa38yc"
}
```


#### Sharing lookalike audiences

During the rollout period of these changes, sharing lookalikes between ad accounts in the rollout and ad accounts not in the rollout is not supported via the API. Please use Audience Manager to handle the sharing. After May 24, 2021, you can continue to use sharing via API in the following developer document to share new lookalike audiences between ad accounts.**Endpoint:** `{AD_ACCOUNT_ID}/adaccounts?adaccounts={SHARED_TO_AD_ACCOUNT_ID}`

### Reach and delivery estimate changes

**Endpoints:**

- `act_{AD_ACCOUNT_ID}/reachestimate`
- `act_{AD_ACCOUNT_ID}/delivery_estimate`
These endpoints will return a new `targeting_status` parameter with one of the following descriptions:

- `lookalike_container_without_country` — A new lookalike does not have a country specified in the campaign targeting. A country is needed to see the estimated users number.
- `lookalike_container_without_delivery_lookalike` — A new lookalike does not have a corresponding backend lookalike. The new lookalike needs to be used in an Ad Set for it to actually have reach.
- `none` — There is no issue with the reach.
The `reachestimate` endpoint will return `-1` for the `users` parameter the first time a new lookalike audience and country target is used; thereafter the estimated user count will be returned.The `estimate_dau` and `estimate_mau` parameters will return `-1` for the `users` parameter the first time a new lookalike audience and country target is used; thereafter the estimated user count will be returned..**Example Responses**
```
// Reach estimate response
{
    "users": -1,
    "estimate_ready": true,
    "targeting_status": "lookalike_container_without_delivery_lookalike"
}

// Delivery estimate response

{
    "data": [{
        "daily_outcomes_curve": [{
            "spend": 0,
            "reach": 0,
            "impressions": 0,
            "actions": 0
        }],
        "estimate_dau": -1,
        "estimate_mau": -1,
        "estimate_ready": true ,
        "targeting_status": "lookalike_container_without_delivery_lookalike"
    }]
}
```


### FAQ

**When will these changes go into affect?****UPDATED APRIL 28, 2021:** The removal of the`location_spec` and `country` parameters from lookalike audience creation is currently delayed. Updates on when this change will go into effect will be forthcoming.**Will I be able to share the new Lookalikes that don’t have location specs with other ad accounts still under legacy Lookalikes during the release?****UPDATED APRIL 28, 2021:** The removal of the`location_spec` and `country` parameters from lookalike audience creation is currently delayed. Updates on when this change will go into effect will be forthcoming.During the period between Marketing API v10 and v11, sharing lookalikes between ad accounts in the rollout and ad accounts not in the rollout is not supported via the API. Please use Audience Manager to handle the sharing.
After the release of Marketing API v11, you can continue to use sharing via the API to share new lookalike audiences between ad accounts.Did you find this page helpful?ON THIS PAGECreateCustom Audience LookalikeTypesCampaign or Ad Set Conversion LookalikesPage Fan LookalikesFlagged custom and lookalike audiencesTargetingManaging AudiencesDelivery StatusInactive AudiencesDeletionBest PracticesUpcoming Lookalike ChangesChanges to Lookalike CreationLocation parameter changesSize parameter changesDelivery and operation statusChanges to Ad SetsAd creation and editingSharing lookalike audiencesReach and delivery estimate changesFAQ$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$