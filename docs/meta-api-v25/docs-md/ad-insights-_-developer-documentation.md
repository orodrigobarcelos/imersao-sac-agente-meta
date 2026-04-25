<!-- Fonte: Ad Insights _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup/insights -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Insights

Updated: Mar 17, 2026
Provides a single, consistent interface to retrieve an ad's statistics. See [Insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights).

The Ad Insights API can return several metrics which are estimated or in-development. In some cases a metric may be both estimated and in-development.


- **Estimated** - Provide directional insights for outcomes that are hard to precisely quantify. They may evolve as we gather more data. See [Ads Help Center, Estimated metrics⁠](https://www.facebook.com/business/help/181058782494426?helpref=faq_content#estimated).
- **In Development** - Still being tested and may change as we improve our methodologies. We encourage you to use it for directional guidance, but use caution when using it for historical comparisons or strategic planning. See [Ads Help Center, In development metrics⁠](https://www.facebook.com/business/help/181058782494426?helpref=faq_content#indevelopment).


## Reading

Provides insights on your advertising performance. Allows for deduped metrics across child objects, such as `unique_clicks`, sorting of metrics, and async reporting.

#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL
```
GET /v25.0/<AD_SET_ID>/insights?fields=impressions&breakdown=publisher_platform HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%3CAD_SET_ID%3E%2Finsights%3Ffields%3Dimpressions%26breakdown%3Dpublisher_platform&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


| Parameter | Description |
| --- | --- |
| action_attribution_windows list\<enum{1d_view, 7d_view, 28d_view, 1d_click, 7d_click, 28d_click, 1d_ev, dda, default, 7d_view_first_conversion, 28d_view_first_conversion, 7d_view_all_conversions, 28d_view_all_conversions, skan_view, skan_click, skan_click_second_postback, skan_view_second_postback, skan_click_third_postback, skan_view_third_postback}\> | Default value: default The attribution window for the actions. The attribution window determines the window (e.g. 7d) and engagement type (e.g click) that’s used as a filter to report actions. See About attribution settings and models ⁠ for examples. The default option means ["7d_click","1d_view"] . |
| action_breakdowns list\<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}\> | Default value: Vec How to break down action results. Supports more than one breakdowns. Default value is ["action_type"]. Note: you must also include actions field whenever action_breakdowns is specified. |
| action_report_time enum{impression, conversion, mixed, lifetime} | Determines the report time of action stats. For example, if a person saw the ad on Jan 1st but converted on Jan 2nd, when you query the API with action_report_time=impression , you see a conversion on Jan 1st. When you query the API with action_report_time=conversion , you see a conversion on Jan 2nd. |
| breakdowns list\<enum{ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, fidelity_type, flexible_format_asset_type, gen_ai_asset_type, gender, hsid, image_asset, impression_device, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_id, redownload, region, rta_ugc_topic, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, title_asset, user_persona_id, user_persona_name, video_asset, rule_set_id, rule_set_name, dma, frequency_value, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, mmm, place_page_id, publisher_platform, platform_position, device_platform, standard_event_content_type, conversion_destination, signal_source_bucket, reels_trending_topic, marketing_messages_btn_name, impression_view_time_advertiser_hour_v2}\> | How to break down the result. For more than one breakdown, only certain combinations are available: See Combining Breakdowns and the Breakdowns page. The option impression_device cannot be used by itself. |
| date_preset enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year} | Default value: last_30d Represents a relative time range. This field is ignored if time_range or time_ranges is specified. |
| default_summary boolean | Default value: false Determine whether to return a summary. If summary is set, this param is be ignored; otherwise, a summary section with the same fields as specified by fields will be included in the summary section. |
| export_columns list\<string\> | Select fields on the exporting report file. It is an optional param. Exporting columns are equal to the param fields, if you leave this param blank |
| export_format string | Set the format of exporting report file. If the export_format is set, Report file is asyncrhonizely generated. It expects ["xls", "csv"]. |
| export_name string | Set the file name of the exporting report. |
| fields list\<string\> | Fields to be retrieved. Default behavior is to return impressions and spend. |
| filtering list\<Filter Object\> | Default value: Vec Filters on the report data. This parameter is an array of filter objects. field string required operator enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP} required value string required Show child parameters |
| level enum {ad, adset, campaign, account} | Represents the level of result. |
| limit integer | limit |
| product_id_limit integer | Maximum number of product ids to be returned for each ad when breakdown by product_id . |
| sort list\<string\> | Default value: Vec Field to sort the result, and direction of sorting. You can specify sorting direction by appending "_ascending" or "_descending" to the sort field. For example, "reach_descending". For actions, you can sort by action type in form of "actions:\<action_type\>". For example, ["actions:link_click_ascending"]. This array supports no more than one element. By default, the sorting direction is ascending. |
| summary list\<string\> | If this param is used, a summary section will be included, with the fields listed in this param. |
| summary_action_breakdowns list\<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}\> | Default value: Vec Similar to action_breakdowns , but applies to summary. Default value is ["action_type"]. |
| time_increment enum{monthly, all_days} or integer | Default value: all_days If it is an integer, it is the number of days from 1 to 90. After you pick a reporting period by using time_range or date_preset , you may choose to have the results for the whole period, or have results for smaller time slices. If "all_days" is used, it means one result set for the whole period. If "monthly" is used, you will get one result set for each calendar month in the given period. Or you can have one result set for each N-day period specified by this param. This param is ignored if time_ranges is specified. |
| time_range {‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD} | A single time range object. UNIX timestamp not supported. This param is ignored if time_ranges is provided. since datetime A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. until datetime A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. Show child parameters |
| time_ranges list\<{‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD}\> | Array of time range objects. Time ranges can overlap, for example to return cumulative insights. Each time range will have one result set. You cannot have more granular results with time_increment setting in this case.If time_ranges is specified, date_preset , time_range and time_increment are ignored. since datetime A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. until datetime A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. Show child parameters |
| use_account_attribution_setting boolean | Default value: false When this parameter is set to true , your ads results will be shown using the attribution settings defined for the ad account. |
| use_unified_attribution_setting boolean | When this parameter is set to true , your ads results will be shown using unified attribution settings defined at ad set level and parameter use_account_attribution_setting will be ignored. |


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


A list of AdsInsights nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


##### summary


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like summary=__type__).


| Field | Description |
| --- | --- |
| account_currency string | Currency that is used by your ad account. |
| account_id numeric string | The ID number of your ad account, which groups your advertising activity. Your ad account includes your campaigns, ads and billing. default |
| account_name string | The name of your ad account, which groups your advertising activity. Your ad account includes your campaigns, ads and billing. |
| action_values list\<AdsActionStats\> | The total value of all conversions attributed to your ads. |
| actions list\<AdsActionStats\> | The total number of actions Accounts Center accounts took that are attributed to your ads. Actions may include engagement, clicks or conversions. |
| actions_per_impression numeric string | Total number of actions divided by the number of impessions. |
| actions_results AdsActionStats | The number of actions as a result of your ad. The results you see here are based on your objective. |
| activity_recency string | activity_recency |
| ad_click_actions list\<AdsActionStats\> | ad_click_actions |
| ad_format_asset string | ad_format_asset |
| ad_id numeric string | The unique ID of the ad you're viewing in reporting. default |
| ad_impression_actions list\<AdsActionStats\> | ad_impression_actions |
| ad_name string | The name of the ad you're viewing in reporting. |
| adjusted_offline_purchase numeric string | The number of purchase events that occurred offline and are attributed to your ads, after adjusting attribution settings and based on information received from your offline event set. |
| adset_end string | The date your ad set is scheduled to stop. |
| adset_id numeric string | The unique ID of the ad set you're viewing in reporting. An ad set is a group of ads that share the same budget, schedule, delivery optimization and targeting. default |
| adset_name string | The name of the ad set you're viewing in reporting. An ad set is a group of ads that share the same budget, schedule, delivery optimization and targeting. |
| adset_start string | The date your ad set is scheduled to start running. |
| anchor_event_attribution_setting string | anchor_event_attribution_setting |
| anchor_events_performance_indicator string | anchor_events_performance_indicator |
| app_store_clicks numeric string | The number of clicks on links to an app store in your ads. |
| attention_events_per_impression numeric string | attention_events_per_impression |
| attention_events_unq_per_reach numeric string | attention_events_unq_per_reach |
| attribution_setting string | The default attribution window to be used when attribution result is calculated. Each ad set has its own attribution setting value. The attribution setting for campaign or account is calculated based on existing ad sets. |
| auction_bid numeric string | auction_bid |
| auction_competitiveness numeric string | auction_competitiveness |
| auction_max_competitor_bid numeric string | auction_max_competitor_bid |
| body_asset AdAssetBody | body_asset |
| buying_type string | The method by which you pay for and target ads in your campaigns: through dynamic auction bidding, fixed-price bidding, or reach and frequency buying. This field is currently only visible at the campaign level. |
| call_to_action_clicks numeric string | The number of times Accounts Center accounts clicked the call-to-action button on your ad. |
| campaign_end string | The date your campaign is scheduled to stop. |
| campaign_id numeric string | The unique ID number of the ad campaign you're viewing in reporting. Your campaign contains ad sets and ads. default |
| campaign_name string | The name of the ad campaign you're viewing in reporting. Your campaign contains ad sets and ads. |
| campaign_start string | The date your campaign is scheduled to start. |
| cancel_subscription_actions list\<AdsActionStats\> | cancel_subscription_actions |
| canvas_avg_view_percent numeric string | The average percentage of the Instant Experience that Accounts Center accounts saw. An Instant Experience is a screen that opens after someone interacts with your ad on a mobile device. It may include a series of interactive or multimedia components, including video, images product catalog and more. |
| canvas_avg_view_time numeric string | The average total time, in seconds, that Accounts Center accounts spent viewing an Instant Experience. An Instant Experience is a screen that opens after someone interacts with your ad on a mobile device. It may include a series of interactive or multimedia components, including video, images product catalog and more. |
| card_views numeric string | The number of times Accounts Center accounts viewed a product from your catalog in an ad. If you're using a carousel format, Accounts Center accounts may view multiple products in a single ad. Counts are updated daily, views for today are not included. This metric is currently in beta, and is only available for ads connected to a product catalog. This metric is in development. |
| catalog_segment_actions list\<AdsActionStats\> | The number of actions performed attributed to your ads promoting your catalog segment, broken down by action type. |
| catalog_segment_value list\<AdsActionStats\> | The total value of all conversions from your catalog segment attributed to your ads. |
| catalog_segment_value_in_catalog_currency list\<AdsActionStats\> | The total value of all conversions from your catalog segment attributed to your ads, in the same currency as the catalog. |
| catalog_segment_value_mobile_purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from mobile app purchases for your catalog segment. |
| catalog_segment_value_omni_purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from all purchases for your catalog segment. |
| catalog_segment_value_website_purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from website purchases for your catalog segment. |
| clicks numeric string | The number of clicks on your ads. |
| coarse_conversion_value string | Allows advertisers and ad networks to receive directional post-install quality insights when the volume of campaign conversions isn't high enough to meet the privacy threshold needed to unlock the standard conversion value. Possible values of this breakdown are low , medium and high . Note: This breakdown is only supported by the total_postbacks_detailed_v4 field. |
| comparison_node AdsInsightsComparison | Parent node that encapsulates fields to be compared (current time range Vs comparison time range) |
| comscore_market string | comscore_market |
| conditional_time_spent_ms_over_10s_actions list\<AdsActionStats\> | conditional_time_spent_ms_over_10s_actions |
| conditional_time_spent_ms_over_15s_actions list\<AdsActionStats\> | conditional_time_spent_ms_over_15s_actions |
| conditional_time_spent_ms_over_2s_actions list\<AdsActionStats\> | conditional_time_spent_ms_over_2s_actions |
| conditional_time_spent_ms_over_3s_actions list\<AdsActionStats\> | conditional_time_spent_ms_over_3s_actions |
| conditional_time_spent_ms_over_6s_actions list\<AdsActionStats\> | conditional_time_spent_ms_over_6s_actions |
| contact_actions list\<AdsActionStats\> | contact_actions |
| contact_value list\<AdsActionStats\> | contact_value |
| conversion_values list\<AdsActionStats\> | conversion_values |
| conversions list\<AdsActionStats\> | conversions |
| converted_product_app_custom_event_fb_mobile_purchase list\<AdsActionStats\> | converted_product_app_custom_event_fb_mobile_purchase |
| converted_product_app_custom_event_fb_mobile_purchase_value list\<AdsActionStats\> | converted_product_app_custom_event_fb_mobile_purchase_value |
| converted_product_offline_purchase list\<AdsActionStats\> | converted_product_offline_purchase |
| converted_product_offline_purchase_value list\<AdsActionStats\> | converted_product_offline_purchase_value |
| converted_product_omni_purchase list\<AdsActionStats\> | converted_product_omni_purchase |
| converted_product_omni_purchase_values list\<AdsActionStats\> | converted_product_omni_purchase_values |
| converted_product_quantity list\<AdsActionStats\> | The number of products purchased which are recorded by your merchant partner's pixel or app SDK for a given product ID and driven by your ads. Has to be used together with converted product ID breakdown. |
| converted_product_value list\<AdsActionStats\> | The value of purchases recorded by your merchant partner's pixel or app SDK for a given product ID and driven by your ads. Has to be used together with converted product ID breakdown. |
| converted_product_website_pixel_purchase list\<AdsActionStats\> | converted_product_website_pixel_purchase |
| converted_product_website_pixel_purchase_value list\<AdsActionStats\> | converted_product_website_pixel_purchase_value |
| converted_promoted_product_app_custom_event_fb_mobile_purchase list\<AdsActionStats\> | converted_promoted_product_app_custom_event_fb_mobile_purchase |
| converted_promoted_product_app_custom_event_fb_mobile_purchase_value list\<AdsActionStats\> | converted_promoted_product_app_custom_event_fb_mobile_purchase_value |
| converted_promoted_product_offline_purchase list\<AdsActionStats\> | converted_promoted_product_offline_purchase |
| converted_promoted_product_offline_purchase_value list\<AdsActionStats\> | converted_promoted_product_offline_purchase_value |
| converted_promoted_product_omni_purchase list\<AdsActionStats\> | converted_promoted_product_omni_purchase |
| converted_promoted_product_omni_purchase_values list\<AdsActionStats\> | converted_promoted_product_omni_purchase_values |
| converted_promoted_product_quantity list\<AdsActionStats\> | converted_promoted_product_quantity |
| converted_promoted_product_value list\<AdsActionStats\> | converted_promoted_product_value |
| converted_promoted_product_website_pixel_purchase list\<AdsActionStats\> | converted_promoted_product_website_pixel_purchase |
| converted_promoted_product_website_pixel_purchase_value list\<AdsActionStats\> | converted_promoted_product_website_pixel_purchase_value |
| cost_per_15_sec_video_view list\<AdsActionStats\> | cost_per_15_sec_video_view |
| cost_per_2_sec_continuous_video_view list\<AdsActionStats\> | cost_per_2_sec_continuous_video_view |
| cost_per_action_result AdsActionStats | The average you paid for each action associated with your objective. |
| cost_per_action_type list\<AdsActionStats\> | The average cost of a relevant action. |
| cost_per_ad_click list\<AdsActionStats\> | cost_per_ad_click |
| cost_per_completed_video_view list\<AdsActionStats\> | cost_per_completed_video_view |
| cost_per_contact list\<AdsActionStats\> | cost_per_contact |
| cost_per_conversion list\<AdsActionStats\> | cost_per_conversion |
| cost_per_customize_product list\<AdsActionStats\> | cost_per_customize_product |
| cost_per_dda_countby_convs numeric string | cost_per_dda_countby_convs |
| cost_per_donate list\<AdsActionStats\> | cost_per_donate |
| cost_per_dwell numeric string | The average cost per 1,000 Dwells |
| cost_per_dwell_3_sec numeric string | cost_per_dwell_3_sec |
| cost_per_dwell_5_sec numeric string | cost_per_dwell_5_sec |
| cost_per_dwell_7_sec numeric string | cost_per_dwell_7_sec |
| cost_per_find_location list\<AdsActionStats\> | cost_per_find_location |
| cost_per_inline_link_click numeric string | The average cost of each inline link click. |
| cost_per_inline_post_engagement numeric string | The average cost of each inline post engagement. |
| cost_per_objective_result list\<AdsInsightsResult\> | The average cost per objective result from your ads. Objective results are what you're trying to get the most of in your ad campaign, based on the objective you selected. |
| cost_per_one_thousand_ad_impression list\<AdsActionStats\> | cost_per_one_thousand_ad_impression |
| cost_per_outbound_click list\<AdsActionStats\> | The average cost for each outbound click. |
| cost_per_result list\<AdsInsightsResult\> | The average cost per result from your ads. |
| cost_per_schedule list\<AdsActionStats\> | cost_per_schedule |
| cost_per_start_trial list\<AdsActionStats\> | cost_per_start_trial |
| cost_per_submit_application list\<AdsActionStats\> | cost_per_submit_application |
| cost_per_subscribe list\<AdsActionStats\> | cost_per_subscribe |
| cost_per_thruplay list\<AdsActionStats\> | The average cost for each ThruPlay. This metric is in development. |
| cost_per_total_action numeric string | The average cost of a relevant action. |
| cost_per_unique_action_type list\<AdsActionStats\> | The average cost of each unique action. This metric is estimated. |
| cost_per_unique_click numeric string | The average cost for each unique click (all). This metric is estimated. |
| cost_per_unique_conversion list\<AdsActionStats\> | cost_per_unique_conversion |
| cost_per_unique_inline_link_click numeric string | The average cost of each unique inline link click. This metric is estimated. |
| cost_per_unique_outbound_click list\<AdsActionStats\> | The average cost for each unique outbound click. This metric is estimated. |
| country string | country |
| cpc numeric string | The average cost for each click (all). |
| cpm numeric string | The average cost for 1,000 impressions. |
| cpp numeric string | The average cost to reach 1,000 Accounts Center accounts. This metric is estimated. |
| created_time string | created_time |
| creative_automation_asset_id AdAssetMedia | creative_automation_asset_id |
| creative_relaxation_asset_type string | creative_relaxation_asset_type |
| ctr numeric string | The percentage of times Accounts Center accounts saw your ad and performed a click (all). |
| customize_product_actions list\<AdsActionStats\> | customize_product_actions |
| customize_product_value list\<AdsActionStats\> | customize_product_value |
| date_start string | The start date for your data. This is controlled by the date range you've selected for your reporting view. default |
| date_stop string | The end date for your data. This is controlled by the date range you've selected for your reporting view. default |
| dda_countby_convs numeric string | dda_countby_convs |
| dda_results list\<AdsInsightsDdaResult\> | dda_results |
| deduping_1st_source_ratio numeric string | This is the auction removal rate for the ad set with the highest amount of audience overlap with the selected ad set. |
| deduping_2nd_source_ratio numeric string | This is the auction removal rate for the ad set with the second highest amount of audience overlap with the selected ad set. |
| deduping_3rd_source_ratio numeric string | This is the auction removal rate for the ad set with the third highest amount of audience overlap with the selected ad set. |
| deduping_ratio numeric string | The total auction removal rate is the percentage of auctions that an ad set did not compete in due to audience overlap with other ad sets. |
| deeplink_clicks numeric string | The number of clicks on links to specific parts of an app. |
| description_asset AdAssetDescription | description_asset |
| device_platform string | device_platform |
| dma string | dma |
| donate_actions list\<AdsActionStats\> | donate_actions |
| donate_value list\<AdsActionStats\> | donate_value |
| dwell_3_sec numeric string | dwell_3_sec |
| dwell_5_sec numeric string | dwell_5_sec |
| dwell_7_sec numeric string | dwell_7_sec |
| dwell_rate numeric string | The number of times someone dwells on your display ad divided by the total number of impressions |
| fidelity_type string | To differentiate StoreKit-rendered ads from view-through ads, SKAdNetwork defines a fidelity-type parameter, which you include in the ad signature and receive in the install-validation postback. Use a fidelity-type value of 1 for StoreKit-rendered ads and attributable web ads, and 0 for view-through ads. Note: This breakdown is only supported by the total_postbacks_detailed_v4 field. |
| find_location_actions list\<AdsActionStats\> | find_location_actions |
| find_location_value list\<AdsActionStats\> | find_location_value |
| flexible_format_asset_type string | flexible_format_asset_type |
| frequency numeric string | The average number of times each person saw your ad. This metric is estimated. |
| frequency_value string | frequency_value |
| full_view_impressions numeric string | The number of Full Views on your Page's posts as a result of your ad. |
| full_view_reach numeric string | The number of Accounts Center accounts that performed a Full View on your Page's post as a result of your ad. |
| gen_ai_asset_type string | gen_ai_asset_type |
| hourly_stats_aggregated_by_advertiser_time_zone string | hourly_stats_aggregated_by_advertiser_time_zone |
| hourly_stats_aggregated_by_audience_time_zone string | hourly_stats_aggregated_by_audience_time_zone |
| hsid string | The hsid key is available for ad impressions that use SKAdNetwork 4 and later. This integer can have up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the sourceIdentifier in the first winning postback, depending on the ad impression's postback data tier. Note: This breakdown is only supported by the total_postbacks_detailed_v4 field. |
| image_asset AdAssetImage | image_asset |
| impression_device string | impression_device |
| impressions numeric string | The number of times your ads were on screen. default |
| impressions_auto_refresh string | impressions_auto_refresh |
| impressions_gross string | impressions_gross |
| inline_link_click_ctr numeric string | The percentage of time Accounts Center accounts saw your ads and performed an inline link click. |
| inline_link_clicks numeric string | The number of clicks on links to select destinations or experiences, on or off Facebook-owned properties. Inline link clicks use a fixed 1-day-click attribution window. |
| inline_post_engagement numeric string | The total number of actions that Accounts Center accounts take involving your ads. Inline post engagements use a fixed 1-day-click attribution window. |
| instagram_upcoming_event_reminders_set numeric string | instagram_upcoming_event_reminders_set |
| instant_experience_clicks_to_open numeric string | instant_experience_clicks_to_open |
| instant_experience_clicks_to_start numeric string | instant_experience_clicks_to_start |
| instant_experience_outbound_clicks list\<AdsActionStats\> | instant_experience_outbound_clicks |
| interactive_component_tap list\<AdsActionStats\> | interactive_component_tap |
| is_auto_advance string | is_auto_advance |
| landing_page_view_per_link_click numeric string | landing_page_view_per_link_click |
| marketing_messages_delivered numeric string | The number of messages your business sent to customers that were delivered. Some messages may not be delivered, such as when a customer's device is out of service. This metric doesn’t include messages delivered to Europe and Japan. In some cases, this metric may be estimated and may differ from what’s shown on your invoice due to small variations in data processing. |
| marketing_messages_delivery_rate numeric string | The number of messages delivered divided by the number of messages sent. Some messages may not be delivered, such as when a customer's device is out of service. This metric doesn't include messages sent to Europe and Japan. |
| marketing_messages_read_rate_benchmark string | We calculate this metric as the 75th percentile of read rates across similar businesses, representing the percentage of messages read out of total messages delivered. |
| media_asset AdAssetMedia | media_asset |
| mobile_app_purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from mobile app purchases. This is based on the value that you assigned when you set up the app event. |
| multi_event_conversion_attribution_setting string | multi_event_conversion_attribution_setting |
| newsfeed_avg_position numeric string | The average position where your ad was inserted into news feeds on mobile and desktop. Position 1 is the one at the top of the feed. |
| newsfeed_clicks numeric string | The total number of clicks your ad received in news feed, on mobile and desktop. |
| newsfeed_impressions numeric string | The total number of times your ad was inserted into news feeds, on mobile and desktop. |
| objective string | The objective reflecting the goal you want to achieve with your advertising. It may be different from the selected objective of the campaign in some cases. |
| objective_result_rate list\<AdsInsightsResult\> | The number of objective results you received divided by the number of impressions. |
| objective_results list\<AdsInsightsResult\> | The number of responses you wanted to achieve from your ad campaign, based on your selected objective. For example, if you selected promote your Page as your campaign objective, this metric shows the number of Page likes that happened as a result of your ads. Also known as results. |
| optimization_goal string | The optimization goal you selected for your ad or ad set. Your optimization goal reflects what you want to optimize for the ads. |
| outbound_clicks list\<AdsActionStats\> | The number of clicks on links that take Accounts Center accounts off Facebook-owned properties. |
| outbound_clicks_ctr list\<AdsActionStats\> | The percentage of times Accounts Center accounts saw your ad and performed an outbound click. |
| performance_indicator string | performance_indicator |
| platform_position string | platform_position |
| postback_sequence_index string | Sequence of postbacks received from SkAdNetwork API version 4.0. Possible values of this breakdown are 0 (first postback), 1 (second postback) and 2 (third postback). Note: This breakdown is only supported by the total_postbacks_detailed_v4 field. |
| private_attribution_conversions unsigned integer | private_attribution_conversions |
| product_brand string | product_brand |
| product_brand_breakdown string | product_brand_breakdown |
| product_category string | product_category |
| product_category_breakdown string | product_category_breakdown |
| product_content_id string | product_content_id |
| product_custom_label_0 string | product_custom_label_0 |
| product_custom_label_0_breakdown string | product_custom_label_0_breakdown |
| product_custom_label_1 string | product_custom_label_1 |
| product_custom_label_1_breakdown string | product_custom_label_1_breakdown |
| product_custom_label_2 string | product_custom_label_2 |
| product_custom_label_2_breakdown string | product_custom_label_2_breakdown |
| product_custom_label_3 string | product_custom_label_3 |
| product_custom_label_3_breakdown string | product_custom_label_3_breakdown |
| product_custom_label_4 string | product_custom_label_4 |
| product_custom_label_4_breakdown string | product_custom_label_4_breakdown |
| product_custom_number_0 string | product_custom_number_0 |
| product_custom_number_1 string | product_custom_number_1 |
| product_custom_number_2 string | product_custom_number_2 |
| product_custom_number_3 string | product_custom_number_3 |
| product_custom_number_4 string | product_custom_number_4 |
| product_group_content_id string | product_group_content_id |
| product_group_content_id_breakdown string | product_group_content_id_breakdown |
| product_group_retailer_id string | product_group_retailer_id |
| product_id string | product_id |
| product_name string | product_name |
| product_retailer_id string | product_retailer_id |
| product_set_id_breakdown string | product_set_id_breakdown |
| product_vendor_id string | product_vendor_id |
| product_vendor_id_breakdown string | product_vendor_id_breakdown |
| product_views string | product_views |
| promoted_product_set_result string | promoted product set result |
| publisher_platform string | publisher_platform |
| purchase_per_landing_page_view numeric string | purchase_per_landing_page_view |
| purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from purchases. This is based on information received from one or more of your connected Facebook Business Tools and attributed to your ads. |
| qualifying_question_qualify_answer_rate numeric string | qualifying_question_qualify_answer_rate |
| reach numeric string | The number of Accounts Center accounts that saw your ads at least once. Reach is different from impressions, which may include multiple views of your ads by the same Accounts Center accounts. This metric is estimated. |
| recurring_subscription_payment_actions list\<AdsActionStats\> | recurring_subscription_payment_actions |
| redownload string | Boolean flag that indicates the customer redownloaded and reinstalled the app when the value is true. A 1 indicates customer has reinstalled the app and 0 indicates that customer hasn’t reinstalled the app Note: This breakdown is only supported by the total_postbacks_detailed_v4 field. |
| reels_trending_topic string | reels_trending_topic |
| result_rate list\<AdsInsightsResult\> | The percentage of results you received out of all the views of your ads. |
| result_values_performance_indicator string | result_values_performance_indicator |
| results list\<AdsInsightsResult\> | The number of times your ad achieved an outcome, based on the objective and settings you selected. |
| rta_ugc_topic string | rta_ugc_topic |
| rule_asset AdAssetRule | rule_asset |
| rule_set_id string | rule_set_id |
| rule_set_name string | rule_set_name |
| schedule_actions list\<AdsActionStats\> | schedule_actions |
| schedule_value list\<AdsActionStats\> | schedule_value |
| shops_assisted_purchases string | shops_assisted_purchases |
| skan_version string | skan_version |
| social_spend numeric string | The total amount you've spent so far for your ads showed with social information. (ex: Jane Doe likes this). |
| spend numeric string | The estimated total amount of money you've spent on your campaign, ad set or ad during its schedule. This metric is estimated. default |
| start_trial_actions list\<AdsActionStats\> | start_trial_actions |
| start_trial_value list\<AdsActionStats\> | start_trial_value |
| submit_application_actions list\<AdsActionStats\> | submit_application_actions |
| submit_application_value list\<AdsActionStats\> | submit_application_value |
| subscribe_actions list\<AdsActionStats\> | subscribe_actions |
| subscribe_value list\<AdsActionStats\> | subscribe_value |
| thumb_stops numeric string | The number of times someone dwells on your display ad. |
| title_asset AdAssetTitle | title_asset |
| today_spend numeric string | How much money you've spent on your campaign, ad set or ad since 12 AM today (in your ad account's time zone). If you set a daily budget, you'll see your progress toward it here to determine how much more you can spend before the day ends. This metric is estimated. |
| total_action_value numeric string | total_action_value |
| total_actions numeric string | The total number of actions Accounts Center accounts took that are attributed to your ads. Actions may include engagement, clicks or conversions. |
| total_card_view string | total_card_view |
| total_unique_actions numeric string | The number of Accounts Center accounts that took an action that was attributed to your ads. This metric is estimated. |
| unique_impressions numeric string | The number of Accounts Center accounts that saw your ads at least once. |
| updated_time string | updated_time |
| user_segment_key string | user_segment_key |
| video_30_sec_watched_actions list\<AdsActionStats\> | The number of times your video played for at least 30 seconds, or for nearly its total length if it's shorter than 30 seconds. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. |
| video_asset AdAssetVideo | video_asset |
| video_avg_time_watched_actions list\<AdsActionStats\> | The average time a video was played, including any time spent replaying the video for a single impression. |
| video_complete_watched_actions list\<AdsActionStats\> | This shows the number of total views of at least 30 seconds or to the end of your video, whichever occurs first. |
| video_completed_view_or_15s_passed_actions list\<AdsActionStats\> | video_completed_view_or_15s_passed_actions |
| video_continuous_2_sec_watched_actions list\<AdsActionStats\> | video_continuous_2_sec_watched_actions |
| video_p100_watched_actions list\<AdsActionStats\> | The number of times your video was played at 100% of its length, including plays that skipped to this point. |
| video_p25_watched_actions list\<AdsActionStats\> | The number of times your video was played at 25% of its length, including plays that skipped to this point. |
| video_p50_watched_actions list\<AdsActionStats\> | The number of times your video was played at 50% of its length, including plays that skipped to this point. |
| video_p75_watched_actions list\<AdsActionStats\> | The number of times your video was played at 75% of its length, including plays that skipped to this point. |
| video_p95_watched_actions list\<AdsActionStats\> | The number of times your video was played at 95% of its length, including plays that skipped to this point. |
| video_play_actions list\<AdsActionStats\> | The number of times your video starts to play. This is counted for each impression of a video, and excludes replays. This metric is in development. |
| video_play_curve_actions list\<AdsHistogramStats\> | A video-play based curve graph that illustrates the percentage of video plays that reached a given second. Entries 0 to 14 represent seconds 0 thru 14. Entries 15 to 17 represent second ranges [15 to 20), [20 to 25), and [25 to 30). Entries 18 to 20 represent second ranges [30 to 40), [40 to 50), and [50 to 60). Entry 21 represents plays over 60 seconds. |
| video_play_retention_0_to_15s_actions list\<AdsHistogramStats\> | video_play_retention_0_to_15s_actions |
| video_play_retention_20_to_60s_actions list\<AdsHistogramStats\> | video_play_retention_20_to_60s_actions |
| video_play_retention_graph_actions list\<AdsHistogramStats\> | video_play_retention_graph_actions |
| video_time_watched_actions list\<AdsActionStats\> | video_time_watched_actions |
| website_clicks numeric string | The number of clicks on links to your website in your ads. |
| website_ctr list\<AdsActionStats\> | The percentage of times Accounts Center accounts saw your ad and performed a link click. |
| website_purchase_roas list\<AdsActionStats\> | The total return on ad spend (ROAS) from website purchases. This is based on the value of all conversions recorded by the Facebook pixel on your website and attributed to your ads. |
| wish_bid numeric string | wish_bid |


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 2642 | Invalid cursors values |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |
| 104 | Incorrect signature |
| 613 | Calls to this api have exceeded the rate limit. |
| 2500 | Error parsing graph query |


## Creating


### /{ad_id}/insights


You can make a POST request to *insights* edge from the following paths:


- [/{ad_id}/insights](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup/insights)

When posting to this edge, an [AdReportRun](https://developers.facebook.com/docs/marketing-api/reference/ad-report-run) will be created.


#### Parameters


| Parameter | Description |
| --- | --- |
| action_attribution_windows list\<enum{1d_view, 7d_view, 28d_view, 1d_click, 7d_click, 28d_click, 1d_ev, dda, default, 7d_view_first_conversion, 28d_view_first_conversion, 7d_view_all_conversions, 28d_view_all_conversions, skan_view, skan_click, skan_click_second_postback, skan_view_second_postback, skan_click_third_postback, skan_view_third_postback}\> | Default value: default The attribution window for the actions. The attribution window determines the window (e.g. 7d) and engagement type (e.g click) that’s used as a filter to report actions. See About attribution settings and models ⁠ for examples. The default option means ["7d_view","1d_click"] . |
| action_breakdowns list\<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}\> | Default value: Vec How to break down action results. Supports more than one breakdowns. Default value is ["action_type"] Note: you must also include actions field whenever action_breakdowns is specified. |
| action_report_time enum{impression, conversion, mixed, lifetime} | Determines the report time of action stats. For example, if a person saw the ad on Jan 1st but converted on Jan 2nd, when you query the API with action_report_time=impression , you will see a conversion on Jan 1st. When you query the API with action_report_time=conversion , you will see a conversion on Jan 2nd |
| breakdowns list\<enum{ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, fidelity_type, flexible_format_asset_type, gen_ai_asset_type, gender, hsid, image_asset, impression_device, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_id, redownload, region, rta_ugc_topic, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, title_asset, user_persona_id, user_persona_name, video_asset, rule_set_id, rule_set_name, dma, frequency_value, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, mmm, place_page_id, publisher_platform, platform_position, device_platform, standard_event_content_type, conversion_destination, signal_source_bucket, reels_trending_topic, marketing_messages_btn_name, impression_view_time_advertiser_hour_v2}\> | How to break down the result. For more than one breakdown, only certain combinations are available: See "Combining Breakdowns" in the Breakdowns page. The option impression_device cannot be used by itself |
| date_preset enum{today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year} | Default value: last_30d Represents a relative time range. This field is ignored if time_range or time_ranges is specified |
| default_summary boolean | Default value: false Determine whether to return a summary. If summary is set, this param will be ignored; otherwise, a summary section with the same fields as specified by fields will be included in the summary section |
| export_columns list\<string\> | Select fields on the exporting report file. It is an optional param. Exporting columns will equals to the param fields if you leave this param blank |
| export_format string | Set the format of exporting report file. If the export_format is set, Report file will be asyncrhonizely generated. It expects ["xls", "csv"]. |
| export_name string | Set the file name of the exporting report. |
| fields list\<string\> | Fields to be retrieved. Default behavior is to return a list of most used fields |
| filtering list\<Filter Object\> | Default value: Vec Filters on the report data. This parameter is an array of filter objects field string required operator enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP} required value string required Show child parameters |
| level enum {ad, adset, campaign, account} | Represents the level of result |
| limit integer | limit |
| product_id_limit integer | Maximun number of product ids to be returned for each ad when breakdown by product_id |
| sort list\<string\> | Default value: Vec Field to sort the result, and direction of sorting. You can specify sorting direction by appending "_ascending" or "_descending" to the sort field. For example, "reach_descending". For actions, you can sort by action type in form of "actions:\<action_type\>". For example, ["actions:link_click_ascending"]. This array supports no more than one element. By default, the sorting direction is ascending |
| summary list\<string\> | If this param is used, a summary section will be included, with the fields listed in this param |
| summary_action_breakdowns list\<enum{action_device, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type, action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, is_business_ai_assisted}\> | Default value: Vec Similar to action_breakdowns , but applies to summary. Default value is ["action_type"] |
| time_increment enum{monthly, all_days} or integer | Default value: all_days If it is an integer, it is the number of days from 1 to 90. After you pick a reporting period by using time_range or date_preset , you may choose to have the results for the whole period, or have results for smaller time slices. If "all_days" is used, it means one result set for the whole period. If "monthly" is used, you will get one result set for each calendar month in the given period. Or you can have one result set for each N-day period specified by this param. This param is ignored if time_ranges is specified |
| time_range {‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD} | A single time range object. UNIX timestamp not supported. This param is ignored if time_ranges is provided since datetime A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. until datetime A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. Show child parameters |
| time_ranges list\<{‘since’:YYYY-MM-DD,’until’:YYYY-MM-DD}\> | Array of time range objects. Time ranges can overlap, for example to return cumulative insights. Each time range will have one result set. You cannot have more granular results with time_increment setting in this case.If time_ranges is specified, date_preset , time_range and time_increment are ignored since datetime A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. until datetime A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. Show child parameters |
| use_account_attribution_setting boolean | Default value: false When this parameter is set to true, your ads results will be shown using the attribution settings defined for the ad account |
| use_unified_attribution_setting boolean | When this parameter is set to true , your ads results will be shown using unified attribution settings defined at ad set level and parameter use_account_attribution_setting will be ignored. |


#### Return Type


```
Struct  {
report_run_id: numeric string,
}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |


## Updating


You can't perform this operation on this endpoint.


## Deleting


You can't perform this operation on this endpoint.
Did you find this page helpful?ON THIS PAGEReadingCreating/{ad_id}/insightsUpdatingDeleting$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6KtQ21-SW2gXy2nDV8UqLGhJP69oxKvTB-BZ5RVmmY5aZcY8c29biyGzO3-w_aem_Rl-jqcsK430kGpBpjXr2BQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5t3S_NlQGA6gazDA6jhdEMsEmd4T6bbVqFlDiGECOMNt0UlwahKMga9qt4tQ_aem_cb__PqkiRr-btN2EMtBEHg&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6FpaePKx9j-OpX_xSw6DTxQeWQ5Wu1x8cyPbTShbyrFmDHkaYZwQ8U6Zjfxg_aem_qli4vMIiCB5o5YPbh_bHYw&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5t3S_NlQGA6gazDA6jhdEMsEmd4T6bbVqFlDiGECOMNt0UlwahKMga9qt4tQ_aem_cb__PqkiRr-btN2EMtBEHg&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5t3S_NlQGA6gazDA6jhdEMsEmd4T6bbVqFlDiGECOMNt0UlwahKMga9qt4tQ_aem_cb__PqkiRr-btN2EMtBEHg&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6uKCdHD0uru0tNxgPM2f_Cu8SPa3tDadP8zykNJq0WE-csLrzIQhsB9x0WhA_aem_RF2W492AyQrdXoBmxH4dGQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4AGd8rInRLik2P8xNcnqn5LDEhJKOByaskuQtz7Mbrn1V9NeK95lvPqO-4pA_aem_Jz7A9mgSlWU2c0mgFJMSRQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6uKCdHD0uru0tNxgPM2f_Cu8SPa3tDadP8zykNJq0WE-csLrzIQhsB9x0WhA_aem_RF2W492AyQrdXoBmxH4dGQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6KtQ21-SW2gXy2nDV8UqLGhJP69oxKvTB-BZ5RVmmY5aZcY8c29biyGzO3-w_aem_Rl-jqcsK430kGpBpjXr2BQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4up3osLAbg_T4g58eeVbUTtflFkCNQxfPNF5X2s_-VLeOo0FzBRvxDSCXJbw_aem_ZeNlBK2-X_eRLHNg7WkVNA&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6FpaePKx9j-OpX_xSw6DTxQeWQ5Wu1x8cyPbTShbyrFmDHkaYZwQ8U6Zjfxg_aem_qli4vMIiCB5o5YPbh_bHYw&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4EEY4MB8I6LA2TjeoBqDpZkCtM6XnHa5Z1PrEBRGz3acO_Dyg2Y8Q1-wIOBw_aem_ODgwCOsZgPbFcv1HgbIJKw&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4EEY4MB8I6LA2TjeoBqDpZkCtM6XnHa5Z1PrEBRGz3acO_Dyg2Y8Q1-wIOBw_aem_ODgwCOsZgPbFcv1HgbIJKw&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5EJB8hpFB2AsX-msne5v2jupwqZNQwLvnjqJVx2ssWxzbO0zqTqUydE-HxYw_aem_XVX3aIYF9qI5z60l5lPkkQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6uKCdHD0uru0tNxgPM2f_Cu8SPa3tDadP8zykNJq0WE-csLrzIQhsB9x0WhA_aem_RF2W492AyQrdXoBmxH4dGQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6KtQ21-SW2gXy2nDV8UqLGhJP69oxKvTB-BZ5RVmmY5aZcY8c29biyGzO3-w_aem_Rl-jqcsK430kGpBpjXr2BQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6uKCdHD0uru0tNxgPM2f_Cu8SPa3tDadP8zykNJq0WE-csLrzIQhsB9x0WhA_aem_RF2W492AyQrdXoBmxH4dGQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4AGd8rInRLik2P8xNcnqn5LDEhJKOByaskuQtz7Mbrn1V9NeK95lvPqO-4pA_aem_Jz7A9mgSlWU2c0mgFJMSRQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6KtQ21-SW2gXy2nDV8UqLGhJP69oxKvTB-BZ5RVmmY5aZcY8c29biyGzO3-w_aem_Rl-jqcsK430kGpBpjXr2BQ&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5t3S_NlQGA6gazDA6jhdEMsEmd4T6bbVqFlDiGECOMNt0UlwahKMga9qt4tQ_aem_cb__PqkiRr-btN2EMtBEHg&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT690-XUUPpX5ZRKrzLYaOHF8RhrXsPxiVdNBqmgFouR9T49vy64aKzNkFx3IRUMO4MHwwg10ecDNTjc7xrBa88eZZ_ZBBNPmgwskxZSb8aMyM__m2tPnCNBhpgYvzZCUhbD0JigD9DK4KrunGkJBdmfXMY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$