<!-- Fonte: Ad Account, Ad Campaigns _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account, Ad Campaigns

Updated: Feb 23, 2026
The ad campaigns associated with a given ad account.

On May 1, 2018 with the release of Marketing API 3.0 we removed `kpi_custom_conversion_id`, `kpi_type`, and `kpi_results`.

Beginning September 15, 2022, with the release of Marketing API v15.0, advertisers will no longer be allowed to create incremental conversion optimization campaigns. Existing conversion optimization campaigns will behave normally.


### Ads About Social Issues, Elections, and Politics

Beginning with the release of Marketing API v15.0, advertisers will no longer be able to create Special Ad Audiences. See [Special Ad Audiences details here](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category#special-ad-audiences) for more information.

## Reading

Returns the campaigns under this ad account. A request with no filters returns only campaigns that were not archived or deleted.

#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL
```
GET /v25.0/act_<AD_ACCOUNT_ID>/campaigns?effective_status=%5B%22ACTIVE%22%2C%22PAUSED%22%5D&fields=name%2Cobjective HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=act_%3CAD_ACCOUNT_ID%3E%2Fcampaigns%3Feffective_status%3D%255B%2522ACTIVE%2522%252C%2522PAUSED%2522%255D%26fields%3Dname%252Cobjective&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


| Parameter | Description |
| --- | --- |
| date_preset enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year} | Predefine date range used to aggregate insights metrics. |
| effective_status list\<enum{ACTIVE, PAUSED, DELETED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, PENDING_BILLING_INFO, CAMPAIGN_PAUSED, ARCHIVED, ADSET_PAUSED, IN_PROCESS, WITH_ISSUES}\> | Default value: Vec effective status for the campaigns |
| is_completed boolean | If true , we return completed campaigns. |
| time_range {‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD} | Date range used to aggregate insights metrics since datetime A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. until datetime A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. Show child parameters |


#### Fields


Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {},
"summary": {}
}
```


##### data


A list of [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


##### summary


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like summary=__type__).


| Field | Description |
| --- | --- |
| insights Edge\<AdsInsights\> | Analytics summary for all objects |
| total_count unsigned int32 | Total number of objects default |


#### Error Codes


| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 613 | Calls to this api have exceeded the rate limit. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 2500 | Error parsing graph query |


## Creating


### /act_{ad_account_id}/campaigns


You can make a POST request to *campaigns* edge from the following paths:


- [/act_{ad_account_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns)

When posting to this edge, a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) will be created.


#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL
```
POST /v25.0/act_<AD_ACCOUNT_ID>/campaigns HTTP/1.1Host: graph.facebook.comname=My+campaign&objective=OUTCOME_TRAFFIC&status=PAUSED&special_ad_categories=%5B%5D&is_adset_budget_sharing_enabled=0
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fcampaigns%3Fname%3DMy%2Bcampaign%26objective%3DOUTCOME_TRAFFIC%26status%3DPAUSED%26special_ad_categories%3D%255B%255D%26is_adset_budget_sharing_enabled%3D0&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


| Parameter | Description |
| --- | --- |
| adlabels list\<Object\> | Ad Labels associated with this campaign |
| bid_strategy enum{LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS} | Choose bid strategy for this campaign to suit your specific business goals. Each strategy has tradeoffs and may be available for certain optimization_goal s: LOWEST_COST_WITHOUT_CAP : Designed to get the most results for your budget based on your ad set optimization_goal without limiting your bid amount. This is the best strategy if you care most about cost efficiency. However with this strategy it may be harder to get stable average costs as you spend. This strategy is also known as automatic bidding . Learn more in Ads Help Center, About bid strategies: Lowest cost ⁠ . LOWEST_COST_WITH_BID_CAP : Designed to get the most results for your budget based on your ad set optimization_goal while limiting actual bid to your specified amount. With a bid cap you have more control over your cost per actual optimization event. However if you set a limit which is too low you may get less ads delivery. If you select this, you must provide a bid cap in the bid_amount field for each ad set in this ad campaign. Note: during creation this is the default bid strategy if you don't specify. This strategy is also known as manual maximum-cost bidding . Learn more in Ads Help Center, About bid strategies: Lowest cost ⁠ . Notes: If you do not enable campaign budget optimization, you should set bid_strategy at ad set level. TARGET_COST bidding strategy has been deprecated with Marketing API v9 . |
| budget_schedule_specs list\<JSON or object-like arrays\> | Initial high demand periods to be created with the campaign. Provide list of time_start , time_end , budget_value , and budget_value_type . For example, -F 'budget_schedule_specs=[{ "time_start":1699081200, "time_end":1699167600, "budget_value":100, "budget_value_type":"ABSOLUTE" }]' See High Demand Period for more details on each field. id int64 time_start datetime time_end datetime budget_value int64 budget_value_type enum{ABSOLUTE, MULTIPLIER} recurrence_type enum{ONE_TIME, WEEKLY} weekly_schedule list\<JSON or object-like arrays\> days list\<int64\> minute_start int64 minute_end int64 timezone_type string Show child parameters Show child parameters |
| buying_type string | Default value: AUCTION This field will help Facebook make optimizations to delivery, pricing, and limits. All ad sets in this campaign must match the buying type. Possible values are: AUCTION (default) RESERVED (for reach and frequency ads ). |
| campaign_optimization_type enum{NONE, ICO_ONLY} | campaign_optimization_type |
| daily_budget int64 | Daily budget of this campaign. All adsets under this campaign will share this budget. You can either set budget at the campaign level or at the adset level, not both. |
| execution_options list\<enum{validate_only, include_recommendations}\> | Default value: Set An execution setting validate_only : when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. include_recommendations : this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section recommendations will be included in the response, but only if recommendations for this specification exist. If the call passes validation or review, response will be {"success": true} . If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| is_skadnetwork_attribution boolean | To create an iOS 14 campaign, enable SKAdNetwork attribution for this campaign. |
| is_using_l3_schedule boolean | is_using_l3_schedule |
| iterative_split_test_configs list\<Object\> | Array of Iterative Split Test Configs created under this campaign . |
| lifetime_budget int64 | Lifetime budget of this campaign. All adsets under this campaign will share this budget. You can either set budget at the campaign level or at the adset level, not both. |
| name string | Name for this campaign supports emoji |
| objective enum{APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS} | Campaign's objective. If it is specified the API will validate that any ads created under the campaign match that objective. Currently, with BRAND_AWARENESS objective, all creatives should be either only images or only videos, not mixed. See Outcome Ad-Driven Experience Objective Validation for more information. |
| promoted_object Object | The object this campaign is promoting across all its ads. It’s required for Meta iOS 14+ app promotion (SKAdNetwork or Aggregated Event Measurement) campaign creation. Only product_catalog_id is used at the ad set level. application_id int The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement pixel_id numeric string or integer The ID of a Facebook conversion pixel. Used with offsite conversion campaigns. custom_event_type enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER} The event from an App Event of a mobile app, not in the standard event list. object_store_url URL The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign. object_store_urls list\<URL\> The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign. offer_id numeric string or integer The ID of an Offer from a Facebook Page. page_id Page ID The ID of a Facebook Page product_catalog_id numeric string or integer The ID of a Product Catalog. Used with Dynamic Product Ads . product_item_id numeric string or integer The ID of the product item. instagram_profile_id numeric string or integer The ID of the instagram profile id. product_set_id numeric string or integer The ID of a Product Set within an Ad Set level Product Catalog. Used with Dynamic Product Ads . event_id numeric string or integer The ID of a Facebook Event offline_conversion_data_set_id numeric string or integer The ID of the offline dataset. fundraiser_campaign_id numeric string or integer The ID of the fundraiser campaign. custom_event_str string The event from an App Event of a mobile app, not in the standard event list. mcme_conversion_id numeric string or integer The ID of a MCME conversion. conversion_goal_id numeric string or integer The ID of a Conversion Goal. offsite_conversion_event_id numeric string or integer The ID of a Offsite Conversion Event boosted_product_set_id numeric string or integer The ID of the Boosted Product Set within an Ad Set level Product Catalog. Should only be present when the advertiser has opted into Product Set Boosting. lead_ads_form_event_source_type enum{inferred, meta_source, offsite_crm, offsite_web, onsite_crm, onsite_crm_single_event, onsite_clo_dep_aet, onsite_web, onsite_p2b_call, onsite_messaging} The event source of lead ads form. lead_ads_custom_event_type enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER} The event from an App Event of a mobile app, not in the standard event list. lead_ads_custom_event_str string The event from an App Event of a mobile app, not in the standard event list. lead_ads_offsite_conversion_type enum{default, clo} The offsite conversion type for lead ads value_semantic_type enum {VALUE, MARGIN, LIFETIME_VALUE} The semantic of the event value to be using for optimization variation enum {OMNI_CHANNEL_SHOP_AUTOMATIC_DATA_COLLECTION, PRODUCT_SET_AND_APP, PRODUCT_SET_AND_IN_STORE, PRODUCT_SET_AND_OMNICHANNEL, PRODUCT_SET_AND_PHONE_CALL, PRODUCT_SET_AND_WEBSITE, PRODUCT_SET_AND_WEBSITE_AND_PHONE_CALL, PRODUCT_SET_WEBSITE_APP_AND_INSTORE} Variation of the promoted object for a PCA ad passback_pixel_id numeric string or integer ID of the pixel used for tracking passback events passback_application_id numeric string or integer ID of the application used for tracking passback events product_set_optimization enum{enabled, disabled} Enum defining whether or not the ad should be optimized for the promoted product set full_funnel_objective enum{OFFER_CLAIMS, PAGE_LIKES, EVENT_RESPONSES, POST_ENGAGEMENT, WEBSITE_CONVERSIONS, LINK_CLICKS, VIDEO_VIEWS, LOCAL_AWARENESS, PRODUCT_CATALOG_SALES, LEAD_GENERATION, BRAND_AWARENESS, STORE_VISITS, REACH, APP_INSTALLS, MESSAGES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION} Enum defining the full funnel objective of the campaign dataset_split_id numeric string or integer ID of the dataset split used to perform additional optimization on the dataset dataset_split_ids array\<numeric string\> IDs of the dataset splits used to perform additional optimization on the dataset lead_ads_selected_pixel_id numeric string or integer The selected pixel id for lead ads conversion leads optimization multi_event_product int64 Identifies which action-to-action product the advertiser is using product_sales_channel enum {ONLINE, IN_STORE, OMNI} ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads anchor_event_config JSON object Configuration for anchor event in multi-event optimization campaigns multi_event_conversion_info JSON object Configuration for multi-event conversion info in CLO campaigns live_video_destination string The live video destination type for live video ads smart_pse_enabled boolean Whether Smart Product Set Expansion is enabled for this campaign. smart_pse_setting enum{ENABLED, DISABLED} Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues. lead_ads_follow_up_event enum{whatsapp_conversations} The selected lead follow-up event for lead ads campaigns. omnichannel_object Object app array\<JSON object\> pixel array\<JSON object\> required onsite array\<JSON object\> Show child parameters whats_app_business_phone_number_id numeric string or integer whatsapp_phone_number string Show child parameters |
| source_campaign_id numeric string or integer | Used if a campaign has been copied. The ID from the original campaign that was copied. |
| special_ad_categories array\<enum {NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES}\> | special_ad_categories required |
| special_ad_category_country array\<enum {AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}\> | special_ad_category_country |
| spend_cap int64 | A spend cap for the campaign, such that it will not spend more than this cap. Defined as integer value of subunit in your currency with a minimum value of $100 USD (or approximate local equivalent). Set the value to 922337203685478 to remove the spend cap. Not available for Reach and Frequency or Premium Self Serve campaigns |
| start_time datetime | start_time |
| status enum{ACTIVE, PAUSED, DELETED, ARCHIVED} | Only ACTIVE and PAUSED are valid during creation. Other statuses can be used for update. If it is set to PAUSED , its active child objects will be paused and have an effective status CAMPAIGN_PAUSED . |
| stop_time datetime | stop_time |
| topline_id numeric string or integer | Topline ID |


#### Return Type


This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *id* in the return type.

```
Struct  {
id: numeric string,
success: bool,
}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 300 | Edit failure |


## Updating


You can't perform this operation on this endpoint.


## Deleting


### /act_{ad_account_id}/campaigns


You can dissociate a [Campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) from an [AdAccount](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account) by making a DELETE request to [/act_{ad_account_id}/campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/campaigns).


#### Parameters


| Parameter | Description |
| --- | --- |
| before_date datetime | Set a before date to delete campaigns before this date |
| delete_strategy enum{DELETE_ANY, DELETE_OLDEST, DELETE_ARCHIVED_BEFORE} | Delete strategy required |
| object_count integer | Object count |


#### Return Type


```
Struct  {
objects_left_to_delete_count: unsigned int32,
deleted_object_ids:  List  [numeric string],
}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |

Did you find this page helpful?ON THIS PAGEAds About Social Issues, Elections, and PoliticsReadingCreating/act_{ad_account_id}/campaignsUpdatingDeleting/act_{ad_account_id}/campaigns$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5jl7EyP0f6qY1qUji3_2Pi0Pxm9VMqaS7UPOPI_Y1ez9yvFn6ynzd0T3_jxA_aem_8AwsGwoPunhyWOiPR9EB3g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7YvSflSK13RIXAo6sLsp8rNYW2cdLkTJ79CLZXChM5RrHUi3xGVsHSn3lhxQ_aem_Vi3f_mX26laRD2wcQTlbFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4nhMMQ37P76GUE6DA-OQwJGyJizHfRonntAHJQxyNNQ1p1zi0rarEMJqqeDw_aem_nKfOEyx3tsBBmhXQduWUdA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5yr0836EKpc0wiGN9q-Y1u1vjyNPaOKDMRKCKLbG7DmScczH-sl2MzhoJVLw_aem_ZhGprlhmRjQn0_k5yCxOvg&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR52__WRwidcYwR2nRKG_KQzG6o82HeU4p1VhDSlvPq5e9PHDWLedRKliOXCZQ_aem_GFmU0TZAFRANN0I-TyMC9w&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$