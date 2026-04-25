<!-- Fonte: Omnichannel Ads _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/omnichannel-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Omnichannel Ads

Updated: Dec 5, 2025Omnichannel ads is a new optimization solution that lets you drive in-store and website sales using one sales campaign. The solution also includes new store location ad features to make shoppers aware of their nearest store locations.Omnichannel ad setup is only officially supported in the Meta Ads Manager UI for advertisers, who can also use Marketing APIs for campaign setup and creation.The following are the API integrations needed to create omnichannel campaigns, ad sets and ads.

## Prerequisites


### App permission

Apps should have the following permissions:

- `ads_management`
- `ads_read`
More detailed information on permissions and access can be found [here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization#permissions-and-features).

### Assets

Advertisers will need access to the following assets:

- `AD_ACCOUNT_ID`: ID of the ad account that ad campaigns, ad sets and ads will be associated with. More information [here](https://developers.facebook.com/docs/marketing-api/business-asset-management/guides/ad-accounts).
- `PIXEL_ID`: ID of a Meta Pixel. Used in `promoted_object` in ad set creation. More information on setup and permissions [here⁠](https://www.facebook.com/business/help/952192354843755?id=1205376682832142).
- `OFFLINE_CONVERSION_DATASET_ID`: ID of offline dataset. Used in `promoted_object` in ad set creation. More information on setup and permissions [here](https://developers.facebook.com/documentation/ads-commerce/conversions-api/offline-events#prerequisites).


## Supported Ad Features

Omnichannel ads support many features of Meta ads, including:

- [Advantage+ Catalog Ads⁠](https://www.facebook.com/business/help/397103717129942?id=1913105122334058): automatically show people your most relevant products based on their interests, intent and actions. - Omnichannel ads support Advantage+ Catalog ads at the campaign level. To opt-in, the field product_catalog_id will be needed in the promoted_object parameter in omnichannel ad campaign creation. - Besides e-commerce catalog, store-based local inventory (SBLI) catalog will also be available through the same setup flow. It will efficiently deliver relevant products available at a person’s nearby store.
- [Advantage+ Shopping Campaigns⁠](https://www.facebook.com/business/help/1362234537597370): help you reach valuable audiences with less set up time and greater efficiency. - Omnichannel ads support ASC campaigns.
- [Advantage+ Creative⁠](https://www.facebook.com/business/help/297506218282224?id=649869995454285): Optimize your images and videos to versions your audience is more likely to interact with. - Omnichannel ads support all kinds of A+C features - Store locations is the high performance Omnichannel A+C feature that helps drive offline conversions (Only available for non Advantage+ catalog ads). To opt-in, the field local_store_extension will be needed under degrees_of_freedom_spec in ad creative creation.


## Omnichannel Ad Campaigns

To create a new omnichannel ad campaign, make a `POST` request to the `/campaigns` endpoint with the following parameters:

- `name`: The name of the campaign.
- `objective`: The objective of the campaign. Valid value is `OUTCOME_SALES`.
- `status`: The status of the campaign. Valid values are `ACTIVE`, `PAUSED`.
- `promoted_object`: Adding `product_catalog_id` will enable Advantage+ catalog ads.


#### Example:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/campaigns \
-F 'name=My Omni campaign' \
-F 'objective=OUTCOME_SALES' \
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example for Advantage+ catalog ads:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/campaigns \
-F 'name=My Omni campaign' \
-F 'objective=OUTCOME_SALES' \
-F 'promoted_object={"product_catalog_id":"<PRODUCT_CATALOG_ID>"}' \
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


### Sample Response

A successful response will return the ID of the newly created campaign.Example:
```
{
  "id": "23845678901234567"
}
```
An unsuccessful response will return an error object with an explanation for the cause of the error.

#### Example:


```
{
    "error": {
"message": "Invalid parameter",
       "type": "OAuthException",
       "code": 100,
"is_transient": false
}
```


### Error Codes

The error codes that may be returned when creating an omnichannel ad campaign are the same [error codes](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns#error-codes-2) as in regular campaigns.

## Omnichannel Ad Sets

To create a new omnichannel ad set, make a `POST` request to the `/adsets` endpoint with the following parameters:

- `name`: The name of the ad set.
- `campaign_id`: The ID of the campaign that the ad set belongs to.
- `bid_strategy`: The bid strategy for the ad set to suit your specific business goals.
- `daily_budget`: The daily budget for the ad set.
- `attribution_spec`: Conversion attribution spec used for attributing conversions for optimization. For omnichannel ads, only CLICK_THROUGH `event_type` with a 7 `window_days` and VIEW_THROUGH `event_type` with a 1 `window_days`are supported.
- `promoted_object`: The object your ad set is promoting across all its ads. - For an omnichannel ad set, `promoted_object` should have an `omnichannel_object` with Pixel and offline objects. PURCHASE is the only custom event type supported for omnichannel ad sets. Please review the example below. - If you are using a Meta Pixel to track website events and a separate dataset to track offline events, please send both Pixel ID and offline dataset ID (see example 1 below). - If you are using a single dataset to manage both your website and offline events, please use that dataset ID in both fields. (see [example 2 below](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/omnichannel-ads#example-2)). - If you are creating **Advantage+ catalog ads** at ad campaign level, you’ll also need to add `product_set_id` with the `variation` field set to PRODUCT_SET_AND_IN_STORE. See the [example below](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/omnichannel-ads#adv-plus-eg). - You can also create a **website, app and in-store** ad with Advantage+ catalog. You will need to add a `product_set_id`, a `pixel_id` that has an associated offline conversion dataset, an app ID, and a Pixel ID. You will also need to set the `variation` to PRODUCT_SET_WEBSITE_APP_AND_INSTORE. You do not need an `omnichannel_object`. See the [example below](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/omnichannel-ads#web-app-instore).
- `targeting`: The targeting spec for the ad set.
- `optimization_goal`: OFFSITE_CONVERSIONS, which will optimize for people more likely to make a conversion in the site and store
- `status`: The status of the ad set. Valid values are `ACTIVE`, `PAUSED`


#### Example 1 - Using Meta Pixel to track website events and separate dataset to track offline events:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/adsets \
-F 'name=My Omni Adset' \
-F 'campaign_id=<OMNI_CAMPAIGN_ID>' \
-F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
-F 'billing_event=IMPRESSIONS' \
-F 'daily_budget=10000' \
-F 'promoted_object={
"omnichannel_object":{
"offline":[{"offline_conversion_data_set_id":"<OFFLINE_CONVERSION_DATASET_ID>","custom_event_type":"PURCHASE"}],
"pixel":[{"pixel_id":"<PIXEL_ID>","custom_event_type":"PURCHASE"}]
}
}' \
-F 'attribution_spec=[
{"event_type":"CLICK_THROUGH","window_days":"7"},
{"event_type":"VIEW_THROUGH","window_days":"1"}
]' \
-F 'targeting={"facebook_positions":["feed"],"geo_locations":{"countries":["US"],"regions":[{"key":"4081"}],"cities":[{"key":777934,"radius":10,"distance_unit":"mile"}]},"genders":[1],"age_max":24,"age_min":20,"publisher_platforms":["facebook","audience_network"],"device_platforms":["mobile"],"flexible_spec":[{"interests":[{"id":"<INTEREST_ID>","name":"<INTEREST_NAME>"}]}]}' \
-F 'status=ACTIVE' \
-F 'optimization_goal=OFFSITE_CONVERSIONS' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example 2 - Using single dataset to track both online and offline events:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/adsets \
-F 'name=My Omni Adset' \
-F 'campaign_id=<OMNI_CAMPAIGN_ID>' \
-F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
-F 'billing_event=IMPRESSIONS' \
-F 'daily_budget=10000' \
-F 'promoted_object={
"omnichannel_object":{
"offline":[{"offline_conversion_data_set_id":"<DATASET_ID>","custom_event_type":"PURCHASE"}],
"pixel":[{"pixel_id":"<DATASET_ID>","custom_event_type":"PURCHASE"}]
}
}' \
-F 'attribution_spec=[
{"event_type":"CLICK_THROUGH","window_days":"7"},
{"event_type":"VIEW_THROUGH","window_days":"1"}
]' \
-F 'targeting={"facebook_positions":["feed"],"geo_locations":{"countries":["US"],"regions":[{"key":"4081"}],"cities":[{"key":777934,"radius":10,"distance_unit":"mile"}]},"genders":[1],"age_max":24,"age_min":20,"publisher_platforms":["facebook","audience_network"],"device_platforms":["mobile"],"flexible_spec":[{"interests":[{"id":"<INTEREST_ID>","name":"<INTEREST_NAME>"}]}]}' \
-F 'status=ACTIVE' \
-F 'optimization_goal=OFFSITE_CONVERSIONS' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example for Advantage+ catalog ads:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/adsets \
-F 'name=My Omni Adset' \
-F 'campaign_id=<OMNI_CAMPAIGN_ID>' \
-F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
-F 'billing_event=IMPRESSIONS' \
-F 'daily_budget=10000' \
-F 'promoted_object={
"product_set_id":"<PRODUCT_SET_ID>",
"custom_event_type":"PURCHASE",
"variation":"PRODUCT_SET_AND_IN_STORE",
"omnichannel_object":{
"offline":[{"offline_conversion_data_set_id":"<OFFLINE_CONVERSION_DATASET_ID>","custom_event_type":"PURCHASE"}],
"pixel":[{"pixel_id":"<PIXEL_ID>","custom_event_type":"PURCHASE"}]
}
}' \
-F 'attribution_spec=[
{"event_type":"CLICK_THROUGH","window_days":"7"},
{"event_type":"VIEW_THROUGH","window_days":"1"}
]' \
-F 'targeting={"facebook_positions":["feed"],"geo_locations":{"countries":["US"],"regions":[{"key":"4081"}],"cities":[{"key":777934,"radius":10,"distance_unit":"mile"}]},"genders":[1],"age_max":24,"age_min":20,"publisher_platforms":["facebook","audience_network"],"device_platforms":["mobile"],"flexible_spec":[{"interests":[{"id":"<INTEREST_ID>","name":"<INTEREST_NAME>"}]}]}' \
-F 'status=ACTIVE' \
-F 'optimization_goal=OFFSITE_CONVERSIONS' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example for web+app+in-store ads:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/adsets \
-F 'name=My Web+App+In-store Adset' \
-F 'campaign_id=<OMNI_CAMPAIGN_ID>' \
-F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
-F 'billing_event=IMPRESSIONS' \
-F 'daily_budget=10000' \
-F 'promoted_object={
  "pixel_id":"<PIXEL_ID>",
"product_set_id":"<PRODUCT_SET_ID>",
"custom_event_type":"PURCHASE",
"variation":"PRODUCT_SET_WEBSITE_APP_AND_INSTORE"
}' \
-F 'attribution_spec=[
{"event_type":"CLICK_THROUGH","window_days":"7"},
{"event_type":"VIEW_THROUGH","window_days":"1"}
]' \
-F 'targeting={"facebook_positions":["feed"],"geo_locations":{"countries":["US"],"regions":[{"key":"4081"}],"cities":[{"key":777934,"radius":10,"distance_unit":"mile"}]},"genders":[1],"age_max":24,"age_min":20,"publisher_platforms":["facebook","audience_network"],"device_platforms":["mobile"],"flexible_spec":[{"interests":[{"id":"<INTEREST_ID>","name":"<INTEREST_NAME>"}]}]}' \
-F 'status=ACTIVE' \
-F 'optimization_goal=OFFSITE_CONVERSIONS' \
-F 'access_token=<ACCESS_TOKEN>'
```


### Sample Response

A successful response will return the ID of the newly created ad set.

#### Example:


```
{
  "id": "23845678901234567"
}
```
An unsuccessful response will return an error object with an explanation for the cause of the error.

#### Example:


```
{
    "error": {
"message": "Invalid parameter",
       "type": "OAuthException",
       "code": 100,
"error_subcode": 3858449,
"is_transient": false,
"error_user_title": "Ad Account Ineligible For Omnichannel Ads",
"error_user_msg": "Omnichannel ads is only available for eligible Ad Account IDs. Use an eligible Ad Account ID or contact your Meta representative for more info.",
"fbtrace_id": "A8A163-BtrDGjzTEDskGTy"
}
```


### Error Codes

The error codes that may be returned when creating an omnichannel ad campaign are the same [error codes](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets#error-codes-2) as in regular campaigns.

### Error Subcodes

The following error codes may be returned when creating a campaign:

| Subcode | Description |
| --- | --- |
| 2446432 | Omnichannel ads only support the OUTCOME_SALES objective. |
| 3858449 | Omnichannel ads are only available for eligible ad account IDs. Use an eligible ad account ID or contact your Meta representative for more info. |
| 3858450 | Ad set needs a valid Meta Pixel ID for omnichannel ads. Use a valid ID or create a Pixel in Meta Events Manager. |
| 3858451 | Omnichannel ads ad sets need a valid custom event type. The only valid event type is “Purchase”. |
| 3858452 | Omnichannel ads ad sets need a valid offline dataset ID. Use a valid offline dataset or set one up in Events Manager. |
| 3858453 | Omnichannel ads ad sets only support an attribution spec of 7-day click-through and 1-day view-through. |
| 3858454 | Omnichannel ads ad sets only support the offsite_conversions optimization goal. |
| 3858513 | For datasets, Pixel ID and offline dataset ID fields must be the same. |
| 3858514 | Dataset must contain an offline dataset ID. |
| 3858515 | Dataset contains an invalid offline dataset ID. Check the setup of your unified dataset. |


## Omnichannel Ad Creative

To create a new ad, make a `POST` request to the `/adcreatives` endpoint with the following parameters:

- `name`: The name of the ad creative.
- `object_story_spec`: The specifications of a creative containing the page ID and other content to create a new unpublished page post specified using one of `link_data`, `photo_data`, `video_data`, `text_data` or `template_data`.
- `degrees_of_freedom_spec`: Specifies the types of transformations that are enabled for the given creative. - For example: specify `local_store_extension` for a high performance omnichannel ad format. (Only available for non Advantage+ catalog ads).
- `product_set_id`: Use the same product set as in ad set creation, if you are creating Advantage+ catalog ads.
- Recommender_settings: Use for store-based local inventory (SBLI) ads creation. Set `product_sales_channel` to `omni`.


#### Example of non Advantage+ catalog ads with local store extension:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/ads \
-F 'name=My Omni Ad Creative' \
-F object_story_spec={
"page_id":"<PAGE_ID>",
"link_data":{
"link":"<LINK>",
"call_to_action": {"type": "SHOP_NOW"}
}
}' \
-F 'degrees_of_freedom_spec={
"creative_features_spec": {
"standard_enhancements":{
"action_metadata":{"type":"STICKY"},
"enroll_status":"OPT_IN"
},
"local_store_extension":{
"action_metadata":{"type":"MANUAL"},
"enroll_status":"OPT_IN"
}
}
}' \
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example for Advantage+ catalog ads:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/ads \
-F 'name=My Omni Advantage+ Catalog Ad Creative'' \
-F 'object_story_spec={
"page_id":"<PAGE_ID>",
"template_data":{
"call_to_action":{"type":"SHOP_NOW"},
"link":"<LINK>",
"name":"Headline {{product.price}}",
"description": "Description {{product.description}}",
"message": "Test {{product.name | titleize}}",
}
}' \
-F 'product_set_id="<PRODUCT_SET_ID>"' \
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


#### Example for Advantage+ catalog ads with store-based local inventory catalog:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/ads \
-F 'name=My Omni Advantage+ Catalog Ad Creative'' \
-F 'object_story_spec={
"page_id":"<PAGE_ID>",
"template_data":{
"call_to_action":{"type":"SHOP_NOW"},
"link":"<LINK>",
"name":"Headline {{product.price}}",
"description": "Description {{product.description}}",
"message": "Test {{product.name | titleize}}",
}
}' \
-F 'product_set_id="<PRODUCT_SET_ID_FROM_SBLI_CATALOG>"' \
-F 'recommender_settings={"product_sales_channel": "omni"}`
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


## Omnichannel Ads

To create a new ad, make a `POST` request to the `/ads` endpoint with the following parameters

- `name`: The name of the ad.
- `adset_id`: The ID of the ad set that the ad belongs to.
- `creative`: The creative spec or the ID of the ad creative for the ad.
- `status`: The status of the ad. Valid values are `ACTIVE`, `PAUSED`.


#### Example:


```
curl -X POST \
https://graph.facebook.com/v20.0/act_<AD_ACCOUNT_ID>/ads \
-F 'name=My Omni Ad' \
-F 'adset_id=<OMNI_AD_SET_ID>' \
-F '{"creative_id":"<AD_CREATIVE_ID>"}' \
-F 'status=ACTIVE' \
-F 'access_token=<ACCESS_TOKEN>'
```


### Expected Response:

A successful response will return the ID of the newly created ad.

#### Example:


```
{
  "id": "23845678901234567"
}
```


### Error Codes

The error codes that may be returned when creating omnichannel ads are the same [error codes](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/ads#error-codes-2) as in regular ads.

### Error Subcodes

The following error codes may be returned when creating a campaign:

| Subcode | Description |
| --- | --- |
| 3858455 | Omnichannel ads don’t support flexible formats for ad creative. Instead use single image or video, collection or carousel formats. |
| 3858456 | Omnichannel ads don’t support using ad creative from an existing post or creative hub mockup. |


## Other Resources


- [GraphAPI Overview](https://developers.facebook.com/docs/graph-api/overview)
- [Ad Permissions and Access](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization#permissions-and-features)
- API Reference - [Ad Campaign Creation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns#Creating) - [Ad Set Creation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets#Creating) - [Ad Creation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/ads#Creating) - [Ad Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative)
- [Ad Creative: Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative)
- Website and Offline Conversion Tracking Event - [Omni Setup Guide](https://developers.facebook.com/documentation/ads-commerce/marketing-api/best-practices/omni-optimal-setup-guide)
- Highlight Features - [Local store extension setup under Advantage+ Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-features-spec) - [Advantage+ Catalog Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/get-started) - [Advantage+ Shopping Campaign API: Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-shopping-campaigns)
Did you find this page helpful?ON THIS PAGEPrerequisitesApp permissionAssetsSupported Ad FeaturesOmnichannel Ad CampaignsExample:Example for Advantage+ catalog ads:Sample ResponseExample:Error CodesOmnichannel Ad SetsExample 1 - Using Meta Pixel to track website events and separate dataset to track offline events:Example 2 - Using single dataset to track both online and offline events:Example for Advantage+ catalog ads:Example for web+app+in-store ads:Sample ResponseExample:Example:Error CodesError SubcodesOmnichannel Ad CreativeExample of non Advantage+ catalog ads with local store extension:Example for Advantage+ catalog ads:Example for Advantage+ catalog ads with store-based local inventory catalog:Omnichannel AdsExample:Expected Response:Example:Error CodesError SubcodesOther Resources$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$