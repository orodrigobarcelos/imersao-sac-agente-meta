<!-- Fonte: Ad Set, Reference.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Adsets

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)

Due to the iOS 14.5 launch, changes have been made to this endpoint.


- Mobile App Custom Audiences for inclusion targeting is no longer supported for the `POST /{ad-account-id}/adsets` endpoint for iOS 14.5 SKAdNetwork campaigns.
- New iOS 14.5 app install campaigns will no longer be able to use app connections targeting.
 [○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)

## Reading


The adsets of this ad account


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=act_%3CAD_ACCOUNT_ID%3E%2Fadsets%3Ffields%3Dname%252Cid%252Cstatus&version=v25.0)
```
GET /v25.0/act_<AD_ACCOUNT_ID>/adsets?fields=name%2Cid%2Cstatus HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/act_<AD_ACCOUNT_ID>/adsets?fields=name%2Cid%2Cstatus',
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
    "/act_<AD_ACCOUNT_ID>/adsets",
    {
        "fields": "name,id,status"
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
params.putString("fields", "name,id,status");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/adsets",
    params,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
NSDictionary *params = @{
  @"fields": @"name,id,status",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/adsets"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X GET -G \
  -d 'fields="name,id,status"' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| date_preset enum {TODAY, YESTERDAY, THIS_MONTH, LAST_MONTH, THIS_QUARTER, MAXIMUM, DATA_MAXIMUM, LAST_3D, LAST_7D, LAST_14D, LAST_28D, LAST_30D, LAST_90D, LAST_WEEK_MON_SUN, LAST_WEEK_SUN_SAT, LAST_QUARTER, LAST_YEAR, THIS_WEEK_MON_TODAY, THIS_WEEK_SUN_TODAY, THIS_YEAR} | Predefine date range used to aggregate insights metrics |
| effective_status list\<enum{ACTIVE, PAUSED, DELETED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, PENDING_BILLING_INFO, CAMPAIGN_PAUSED, ARCHIVED, ADSET_PAUSED, IN_PROCESS, WITH_ISSUES}\> | Effective status of adset |
| is_completed boolean | Filter adset by completed status |
| time_range {'since':YYYY-MM-DD,'until':YYYY-MM-DD} | Date range used to aggregate insights metrics |
| → since datetime | A date in the format of "YYYY-MM-DD", which means from the beginning midnight of that day. |
| → until datetime | A date in the format of "YYYY-MM-DD", which means to the beginning midnight of the following day. |
| updated_since integer | Time since the Adset has been updated. |


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

A list of [AdSet](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=insights`).


| Field | Description |
| --- | --- |
| insights Edge\<AdsInsights\> | Analytics summary for all objects. Use nested parameters with this field. insights.time_range({'until':'2018-01-01', 'since':'2017-12-12'}).time_increment(1) |
| total_count unsigned int32 | Total number of objects Default |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 613 | Calls to this api have exceeded the rate limit. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 3018 | The start date of the time range cannot be beyond 37 months from the current date |
| 2500 | Error parsing graph query |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)

## Creating


Mobile App Install CPA Billing will no longer be supported. The [billing event](https://developers.facebook.com/docs/marketing-api/bidding/overview/billing-events) cannot be App Install if the Optimization goal is App Install.
 You can make a POST request to `adsets` edge from the following paths:

- [`/act_{ad_account_id}/adsets`](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/)
When posting to this edge, an [AdSet](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/) will be created.

### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=act_%3CAD_ACCOUNT_ID%3E%2Fadsets%3Fname%3DMy%2BFirst%2BAdset%26lifetime_budget%3D20000%26start_time%3D2026-03-30T17%253A17%253A34-0700%26end_time%3D2026-04-09T17%253A17%253A34-0700%26campaign_id%3D%253CAD_CAMPAIGN_ID%253E%26bid_amount%3D100%26billing_event%3DLINK_CLICKS%26optimization_goal%3DLINK_CLICKS%26targeting%3D%257B%2522facebook_positions%2522%253A%255B%2522feed%2522%255D%252C%2522geo_locations%2522%253A%257B%2522countries%2522%253A%255B%2522US%2522%255D%257D%252C%2522publisher_platforms%2522%253A%255B%2522facebook%2522%252C%2522audience_network%2522%255D%257D%26status%3DPAUSED&version=v25.0)
```
POST /v25.0/act_<AD_ACCOUNT_ID>/adsets HTTP/1.1
Host: graph.facebook.com

name=My+First+Adset&lifetime_budget=20000&start_time=2026-03-30T17%3A17%3A34-0700&end_time=2026-04-09T17%3A17%3A34-0700&campaign_id=%3CAD_CAMPAIGN_ID%3E&bid_amount=100&billing_event=LINK_CLICKS&optimization_goal=LINK_CLICKS&targeting=%7B%22facebook_positions%22%3A%5B%22feed%22%5D%2C%22geo_locations%22%3A%7B%22countries%22%3A%5B%22US%22%5D%7D%2C%22publisher_platforms%22%3A%5B%22facebook%22%2C%22audience_network%22%5D%7D&status=PAUSED
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/act_<AD_ACCOUNT_ID>/adsets',
    array (
      'name' => 'My First Adset',
      'lifetime_budget' => '20000',
      'start_time' => '2026-03-30T17:17:34-0700',
      'end_time' => '2026-04-09T17:17:34-0700',
      'campaign_id' => '<AD_CAMPAIGN_ID>',
      'bid_amount' => '100',
      'billing_event' => 'LINK_CLICKS',
      'optimization_goal' => 'LINK_CLICKS',
      'targeting' => '{"facebook_positions":["feed"],"geo_locations":{"countries":["US"]},"publisher_platforms":["facebook","audience_network"]}',
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
    "/act_<AD_ACCOUNT_ID>/adsets",
    "POST",
    {
        "name": "My First Adset",
        "lifetime_budget": "20000",
        "start_time": "2026-03-30T17:17:34-0700",
        "end_time": "2026-04-09T17:17:34-0700",
        "campaign_id": "<AD_CAMPAIGN_ID>",
        "bid_amount": "100",
        "billing_event": "LINK_CLICKS",
        "optimization_goal": "LINK_CLICKS",
        "targeting": "{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}",
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
params.putString("name", "My First Adset");
params.putString("lifetime_budget", "20000");
params.putString("start_time", "2026-03-30T17:17:34-0700");
params.putString("end_time", "2026-04-09T17:17:34-0700");
params.putString("campaign_id", "<AD_CAMPAIGN_ID>");
params.putString("bid_amount", "100");
params.putString("billing_event", "LINK_CLICKS");
params.putString("optimization_goal", "LINK_CLICKS");
params.putString("targeting", "{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}");
params.putString("status", "PAUSED");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/act_<AD_ACCOUNT_ID>/adsets",
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
  @"name": @"My First Adset",
  @"lifetime_budget": @"20000",
  @"start_time": @"2026-03-30T17:17:34-0700",
  @"end_time": @"2026-04-09T17:17:34-0700",
  @"campaign_id": @"<AD_CAMPAIGN_ID>",
  @"bid_amount": @"100",
  @"billing_event": @"LINK_CLICKS",
  @"optimization_goal": @"LINK_CLICKS",
  @"targeting": @"{\"facebook_positions\":[\"feed\"],\"geo_locations\":{\"countries\":[\"US\"]},\"publisher_platforms\":[\"facebook\",\"audience_network\"]}",
  @"status": @"PAUSED",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/act_<AD_ACCOUNT_ID>/adsets"
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
  -F 'name="My First Adset"' \
  -F 'lifetime_budget=20000' \
  -F 'start_time="2026-03-30T17:17:34-0700"' \
  -F 'end_time="2026-04-09T17:17:34-0700"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'bid_amount=100' \
  -F 'billing_event="LINK_CLICKS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| adlabels list\<Object\> | Specifies list of labels to be associated with this object. This field is optional |
| adset_schedule list\<Object\> | Ad set schedule, representing a delivery schedule for a single day |
| → start_minute int64 | A 0 based minute of the day representing when the schedule starts Required |
| → end_minute int64 | A 0 based minute of the day representing when the schedule ends Required |
| → days list\<int64\> | Array of ints representing which days the schedule is active. Valid values are 0-6 with 0 representing Sunday, 1 representing Monday, ... and 6 representing Saturday. Required |
| → timezone_type enum {USER, ADVERTISER} | Default value: USER |
| attribution_spec list\<JSON object\> | Conversion attribution spec used for attributing conversions for optimization. Supported window lengths differ by optimization goal and campaign objective. |
| → event_type enum {CLICK_THROUGH, VIEW_THROUGH, ENGAGED_VIDEO_VIEW} | Required |
| → window_days int64 | Required |
| → weight float | Default value: 100 |
| automatic_manual_state enum{UNSET, AUTOMATIC, MANUAL} | automatic_manual_state |
| bid_amount integer | Bid cap or target cost for this ad set. The bid cap used in a lowest cost bid strategy is defined as the maximum bid you want to pay for a result based on your optimization_goal . The target cost used in a target cost bid strategy lets Facebook bid to meet your target on average and keep costs stable as you spend. If an ad level bid_amount is specified, updating this value will overwrite the previous ad level bid. Unless you are using Reach and Frequency , bid_amount is required if bid_strategy is set to LOWEST_COST_WITH_BID_CAP or COST_CAP . The bid amount's unit is cents for currencies like USD, EUR, and the basic unit for currencies like JPY, KRW. The bid amount for ads with IMPRESSION or REACH as billing_event is per 1,000 occurrences, and has to be at least 2 US cents or more. For ads with other billing_event s, the bid amount is for each occurrence, and has a minimum value 1 US cents. The minimum bid amounts of other currencies are of similar value to the US Dollar values provided. |
| bid_strategy enum{LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS} | Choose bid strategy for this ad set to suit your specific business goals. Each strategy has tradeoffs and may be available for certain optimization_goal s: LOWEST_COST_WITHOUT_CAP : Designed to get the most results for your budget based on your ad set optimization_goal without limiting your bid amount. This is the best strategy if you care most about cost efficiency. However with this strategy it may be harder to get stable average costs as you spend. This strategy is also known as automatic bidding . Learn more in Ads Help Center, About bid strategies: Lowest cost . LOWEST_COST_WITH_BID_CAP : Designed to get the most results for your budget based on your ad set optimization_goal while limiting actual bid to your specified amount. With a bid cap you have more control over your cost per actual optimization event. However if you set a limit which is too low you may get less ads delivery. If you select this, you must provide a bid cap with the bid_amount field. Note: during creation this bid strategy is set if you provide bid_amount only. This strategy is also known as manual maximum-cost bidding . Learn more in Ads Help Center, About bid strategies: Lowest cost . Notes: If you enable campaign budget optimization, you should set bid_strategy at the parent campaign level. TARGET_COST bidding strategy has been deprecated with Marketing API v9 . |
| billing_event enum{APP_INSTALLS, CLICKS, IMPRESSIONS, LINK_CLICKS, NONE, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING_INTERACTION} | The billing event that this ad set is using: APP_INSTALLS: Pay when people install your app. CLICKS: Deprecated. IMPRESSIONS: Pay when the ads are shown to people. LINK_CLICKS: Pay when people click on the link of the ad. OFFER_CLAIMS: Pay when people claim the offer. PAGE_LIKES: Pay when people like your page. POST_ENGAGEMENT: Pay when people engage with your post. VIDEO_VIEWS: Pay when people watch your video ads for at least 10 seconds. THRUPLAY: Pay for ads that are played to completion, or played for at least 15 seconds. |
| budget_schedule_specs list\<JSON or object-like arrays\> | Initial high demand periods to be created with the ad set. Provide list of time_start , time_end , budget_value , and budget_value_type . For example, -F 'budget_schedule_specs=[{ "time_start":1699081200, "time_end":1699167600, "budget_value":100, "budget_value_type":"ABSOLUTE" }]' See High Demand Period for more details on each field. |
| → id int64 |  |
| → time_start datetime |  |
| → time_end datetime |  |
| → budget_value int64 |  |
| → budget_value_type enum{ABSOLUTE, MULTIPLIER} |  |
| → recurrence_type enum{ONE_TIME, WEEKLY} |  |
| → weekly_schedule list\<JSON or object-like arrays\> |  |
| → → days list\<int64\> |  |
| → → minute_start int64 |  |
| → → minute_end int64 |  |
| → → timezone_type string |  |
| budget_source enum{NONE, RMN} | budget_source |
| budget_split_set_id numeric string or integer | budget_split_set_id |
| campaign_attribution enum{} | campaign_attribution |
| campaign_id numeric string or integer | The ad campaign you wish to add this ad set to. |
| campaign_spec Campaign spec | Provide name , objective and buying_type for a campaign you want to create. Otherwise you need to provide campaign_id for an existing ad campaign. For example: -F 'campaign_spec={ "name": "Inline created campaign", "objective": "CONVERSIONS", "buying_type": "AUCTION" }' Please refer to the Outcome-Driven Ads Experiences mapping table to find new objectives and their corresponding destination types, optimization goals and promoted objects. |
| contextual_bundling_spec Object | settings of Contextual Bundle to support ads serving in Facebook contextual surfaces |
| → status enum{OPT_OUT, OPT_IN} |  |
| creative_sequence list\<numeric string or integer\> | Order of the adgroup sequence to be shown to users |
| daily_budget int64 | The daily budget defined in your account currency , allowed only for ad sets with a duration (difference between end_time and start_time ) longer than 24 hours. Either daily_budget or lifetime_budget must be greater than 0. |
| daily_imps int64 | Daily impressions. Available only for campaigns with buying_type=FIXED_CPM |
| daily_min_spend_target int64 | Daily minimum spend target of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| daily_spend_cap int64 | Daily spend cap of the ad set defined in your account currency. To use this field, daily budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap. |
| destination_type enum{WEBSITE, APP, MESSENGER, APPLINKS_AUTOMATIC, WHATSAPP, INSTAGRAM_DIRECT, FACEBOOK, MESSAGING_MESSENGER_WHATSAPP, MESSAGING_INSTAGRAM_DIRECT_MESSENGER, MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP, MESSAGING_INSTAGRAM_DIRECT_WHATSAPP, SHOP_AUTOMATIC, ON_AD, ON_POST, ON_EVENT, ON_VIDEO, ON_PAGE, INSTAGRAM_PROFILE, FACEBOOK_PAGE, INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE, INSTAGRAM_LIVE, FACEBOOK_LIVE, IMAGINE} | Destination of ads in this Ad Set. Options include: Website, App, Messenger, INSTAGRAM_DIRECT , INSTAGRAM_PROFILE . |
| dsa_beneficiary string | dsa_beneficiary |
| dsa_payor string | dsa_payor |
| end_time datetime | End time, required when lifetime_budget is specified. e.g. 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . When creating a set with a daily budget, specify end_time=0 to set the set to be ongoing and have no end date. UTC UNIX timestamp |
| execution_options list\<enum{validate_only, include_recommendations}\> | Default value: Set An execution setting validate_only : when this option is specified, the API call will not perform the mutation but will run through the validation rules against values of each field. include_recommendations : this option cannot be used by itself. When this option is used, recommendations for ad object's configuration will be included. A separate section recommendations will be included in the response, but only if recommendations for this specification exist. If the call passes validation or review, response will be {"success": true} . If the call does not pass, an error will be returned with more details. These options can be used to improve any UI to display errors to the user much sooner, e.g. as soon as a new value is typed into any field corresponding to this ad object, rather than at the upload/save stage, or after review. |
| existing_customer_budget_percentage int64 | existing_customer_budget_percentage |
| frequency_control_specs list\<Object\> | An array of frequency control specs for this ad set. Writes to this field are only available in ad sets where REACH and THRUPLAY are the performance goal. |
| → event enum{IMPRESSIONS, VIDEO_VIEWS, VIDEO_VIEWS_2S, VIDEO_VIEWS_15S} | Event name, only IMPRESSIONS currently. Required |
| → interval_days integer | Interval period in days, between 1 and 90 (inclusive) Required |
| → max_frequency integer | The maximum frequency, between 1 and 90 (inclusive) Required |
| → type enum{NONE, CAP, TARGET} |  |
| is_dynamic_creative boolean | Indicates the ad set must only be used for dynamic creatives. Dynamic creative ads can be created in this ad set. Defaults to false |
| is_sac_cfca_terms_certified boolean | is_sac_cfca_terms_certified |
| lifetime_budget int64 | Lifetime budget, defined in your account currency . If specified, you must also specify an end_time . Either daily_budget or lifetime_budget must be greater than 0. |
| lifetime_imps int64 | Lifetime impressions. Available only for campaigns with buying_type=FIXED_CPM |
| lifetime_min_spend_target int64 | Lifetime minimum spend target of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. This target is not a guarantee but our best effort. |
| lifetime_spend_cap int64 | Lifetime spend cap of the ad set defined in your account currency. To use this field, lifetime budget must be specified in the Campaign. Set the value to 922337203685478 to remove the spend cap. |
| max_budget_spend_percentage int64 | max_budget_spend_percentage |
| min_budget_spend_percentage int64 | min_budget_spend_percentage |
| multi_event_conversion_attribution_window_seconds int64 | multi_event_conversion_attribution_window_seconds |
| multi_optimization_goal_weight enum{UNDEFINED, BALANCED, PREFER_INSTALL, PREFER_EVENT} | multi_optimization_goal_weight |
| name string | Ad set name, max length of 400 characters. Required Supports Emoji |
| optimization_goal enum{NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, ENGAGED_PAGE_VIEWS, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE, MESSAGING_PURCHASE_CONVERSION, SUBSCRIBERS, REMINDERS_SET, MEANINGFUL_CALL_ATTEMPT, PROFILE_VISIT, PROFILE_AND_PAGE_ENGAGEMENT, ADVERTISER_SILOED_VALUE, AUTOMATIC_OBJECTIVE, MESSAGING_APPOINTMENT_CONVERSION} | What the ad set is optimizing for. APP_INSTALLS : Will optimize for people more likely to install your app. ENGAGED_USERS : Will optimize for people more likely to take a particular action in your app. EVENT_RESPONSES : Will optimize for people more likely to attend your event. IMPRESSIONS : Will show the ads as many times as possible. LEAD_GENERATION : Will optimize for people more likely to fill out a lead generation form. LINK_CLICKS : Will optimize for people more likely to click in the link of the ad. OFFER_CLAIMS : Will optimize for people more likely to claim the offer. OFFSITE_CONVERSIONS : Will optimize for people more likely to make a conversion in the site PAGE_ENGAGEMENT : Will optimize for people more likely to engage with your page. PAGE_LIKES : Will optimize for people more likely to like your page. POST_ENGAGEMENT : Will optimize for people more likely to engage with your post. REACH : Optimize to reach the most unique users of each day or interval specified in frequency_control_specs . SOCIAL_IMPRESSIONS : Increase the number of impressions with social context. For example, with the names of one or more of the user's friends attached to the ad who have already liked the page or installed the app. VALUE : Will optimize for maximum total purchase value within the specified attribution window. THRUPLAY : Will optimize delivery of your ads to people are more likely to play your ad to completion, or play it for at least 15 seconds. AD_RECALL_LIFT : Optimize for people more likely to remember seeing your ads. VISIT_INSTAGRAM_PROFILE : Optimize for visits to the advertiser's instagram profile. |
| optimization_sub_event enum{NONE, VIDEO_SOUND_ON, TRIP_CONSIDERATION, TRAVEL_INTENT, TRAVEL_INTENT_NO_DESTINATION_INTENT, TRAVEL_INTENT_BUCKET_01, TRAVEL_INTENT_BUCKET_02, TRAVEL_INTENT_BUCKET_03, TRAVEL_INTENT_BUCKET_04, TRAVEL_INTENT_BUCKET_05, POST_INTERACTION} | Optimization sub event for a specific optimization goal (ex: Sound-On event for Video-View-2s optimization goal) |
| pacing_type list\<string\> | Defines the pacing type, standard by default or using ad scheduling |
| placement_soft_opt_out Object | placement_soft_opt_out |
| → publisher_platforms list\<string\> |  |
| → effective_publisher_platforms list\<string\> |  |
| → facebook_positions list\<string\> |  |
| → effective_facebook_positions list\<string\> |  |
| → instagram_positions list\<string\> |  |
| → effective_instagram_positions list\<string\> |  |
| → messenger_positions list\<string\> |  |
| → effective_messenger_positions list\<string\> |  |
| → whatsapp_positions list\<string\> |  |
| → effective_whatsapp_positions list\<string\> |  |
| → oculus_positions list\<string\> |  |
| → effective_oculus_positions list\<string\> |  |
| → threads_positions list\<string\> |  |
| → effective_threads_positions list\<string\> |  |
| → device_platforms list\<string\> |  |
| → effective_device_platforms list\<string\> |  |
| → audience_network_positions list\<string\> |  |
| → effective_audience_network_positions list\<string\> |  |
| → excluded_publisher_categories list\<string\> |  |
| → brand_safety_content_severity_levels list\<string\> |  |
| → brand_safety_content_filter_levels list\<string\> |  |
| → excluded_brand_safety_content_types list\<string\> |  |
| → excluded_publisher_list_ids list\<string\> |  |
| → user_device list\<string\> |  |
| → excluded_user_device list\<string\> |  |
| → excluded_mobile_device_model list\<string\> |  |
| → user_os list\<string\> |  |
| → wireless_carrier list\<string\> |  |
| → direct_install_devices boolean |  |
| → instream_video_skippable_excluded boolean |  |
| → contextual_targeting_categories list\<JSON or object-like arrays\> |  |
| → → id int64 |  |
| → → name string |  |
| → marketing_message_channels list\<string\> |  |
| promoted_object Object | The object this ad set is promoting across all its ads. Required with certain campaign objectives. CONVERSIONS pixel_id (Conversion pixel ID) pixel_id (Facebook pixel ID) and custom_event_type pixel_id (Facebook pixel ID) and pixel_rule and custom_event_type event_id (Facebook event ID) and custom_event_type application_id , object_store_url , and custom_event_type for mobile app events offline_conversion_data_set_id (Offline dataset ID) and custom_event_type for offline conversions PAGE_LIKES page_id OFFER_CLAIMS page_id LINK_CLICKS application_id and object_store_url for mobile app or Canvas app engagement link clicks APP_INSTALLS application_id and object_store_url if the optimization_goal is OFFSITE_CONVERSIONS application_id , object_store_url , and custom_event_type (Standard Events) application_id , object_store_url , custom_event_type = OTHER and custom_event_str (Custom Events) PRODUCT_CATALOG_SALES product_set_id product_set_id and custom_event_type When optimization_goal is LEAD_GENERATION , page_id needs to be passed as promoted_object. Please refer to the Outcome-Driven Ads Experiences mapping table to find new objectives and their corresponding destination types, optimization goals and promoted objects. |
| → application_id int | The ID of a Facebook Application. Usually related to mobile or canvas games being promoted on Facebook for installs or engagement |
| → pixel_id numeric string or integer | The ID of a Facebook conversion pixel. Used with offsite conversion campaigns. |
| → custom_event_type enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER} | The event from an App Event of a mobile app, not in the standard event list. |
| → object_store_url URL | The uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign. |
| → object_store_urls list\<URL\> | The vec of uri of the mobile / digital store where an application can be bought / downloaded. This is platform specific. When combined with the "application_id" this uniquely specifies an object which can be the subject of a Facebook advertising campaign. |
| → offer_id numeric string or integer | The ID of an Offer from a Facebook Page. |
| → page_id Page ID | The ID of a Facebook Page |
| → product_catalog_id numeric string or integer | The ID of a Product Catalog. Used with Dynamic Product Ads . |
| → product_item_id numeric string or integer | The ID of the product item. |
| → instagram_profile_id numeric string or integer | The ID of the instagram profile id. |
| → product_set_id numeric string or integer | The ID of a Product Set within an Ad Set level Product Catalog. Used with Dynamic Product Ads . |
| → event_id numeric string or integer | The ID of a Facebook Event |
| → offline_conversion_data_set_id numeric string or integer | The ID of the offline dataset. |
| → fundraiser_campaign_id numeric string or integer | The ID of the fundraiser campaign. |
| → custom_event_str string | The event from an App Event of a mobile app, not in the standard event list. |
| → mcme_conversion_id numeric string or integer | The ID of a MCME conversion. |
| → conversion_goal_id numeric string or integer | The ID of a Conversion Goal. |
| → offsite_conversion_event_id numeric string or integer | The ID of a Offsite Conversion Event |
| → boosted_product_set_id numeric string or integer | The ID of the Boosted Product Set within an Ad Set level Product Catalog. Should only be present when the advertiser has opted into Product Set Boosting. |
| → lead_ads_form_event_source_type enum{inferred, meta_source, offsite_crm, offsite_web, onsite_crm, onsite_crm_single_event, onsite_clo_dep_aet, onsite_web, onsite_p2b_call, onsite_messaging} | The event source of lead ads form. |
| → lead_ads_custom_event_type enum{AD_IMPRESSION, RATE, TUTORIAL_COMPLETION, CONTACT, CUSTOMIZE_PRODUCT, DONATE, FIND_LOCATION, SCHEDULE, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE, ADD_TO_CART, ADD_TO_WISHLIST, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, PURCHASE, LEAD, COMPLETE_REGISTRATION, CONTENT_VIEW, SEARCH, SERVICE_BOOKING_REQUEST, MESSAGING_CONVERSATION_STARTED_7D, LEVEL_ACHIEVED, ACHIEVEMENT_UNLOCKED, SPENT_CREDITS, LISTING_INTERACTION, D2_RETENTION, D7_RETENTION, OTHER} | The event from an App Event of a mobile app, not in the standard event list. |
| → lead_ads_custom_event_str string | The event from an App Event of a mobile app, not in the standard event list. |
| → lead_ads_offsite_conversion_type enum{default, clo} | The offsite conversion type for lead ads |
| → value_semantic_type enum {VALUE, MARGIN, LIFETIME_VALUE} | The semantic of the event value to be using for optimization |
| → variation enum {OMNI_CHANNEL_SHOP_AUTOMATIC_DATA_COLLECTION, PRODUCT_SET_AND_APP, PRODUCT_SET_AND_IN_STORE, PRODUCT_SET_AND_OMNICHANNEL, PRODUCT_SET_AND_PHONE_CALL, PRODUCT_SET_AND_WEBSITE, PRODUCT_SET_AND_WEBSITE_AND_PHONE_CALL, PRODUCT_SET_WEBSITE_APP_AND_INSTORE} | Variation of the promoted object for a PCA ad |
| → passback_pixel_id numeric string or integer | ID of the pixel used for tracking passback events |
| → passback_application_id numeric string or integer | ID of the application used for tracking passback events |
| → product_set_optimization enum{enabled, disabled} | Enum defining whether or not the ad should be optimized for the promoted product set |
| → full_funnel_objective enum{OFFER_CLAIMS, PAGE_LIKES, EVENT_RESPONSES, POST_ENGAGEMENT, WEBSITE_CONVERSIONS, LINK_CLICKS, VIDEO_VIEWS, LOCAL_AWARENESS, PRODUCT_CATALOG_SALES, LEAD_GENERATION, BRAND_AWARENESS, STORE_VISITS, REACH, APP_INSTALLS, MESSAGES, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION} | Enum defining the full funnel objective of the campaign |
| → dataset_split_id numeric string or integer | ID of the dataset split used to perform additional optimization on the dataset |
| → dataset_split_ids array\<numeric string\> | IDs of the dataset splits used to perform additional optimization on the dataset |
| → lead_ads_selected_pixel_id numeric string or integer | The selected pixel id for lead ads conversion leads optimization |
| → multi_event_product int64 | Identifies which action-to-action product the advertiser is using |
| → product_sales_channel enum {ONLINE, IN_STORE, OMNI} | ProductSalesChannel of the promoted object for Omni L3 DA SBLI ads |
| → anchor_event_config JSON object | Configuration for anchor event in multi-event optimization campaigns |
| → multi_event_conversion_info JSON object | Configuration for multi-event conversion info in CLO campaigns |
| → live_video_destination string | The live video destination type for live video ads |
| → smart_pse_enabled boolean | Whether Smart Product Set Expansion is enabled for this campaign. |
| → smart_pse_setting enum{ENABLED, DISABLED} | Setting for Smart Product Set Expansion. Uses an enum instead of a boolean to avoid TAO null handling issues. |
| → lead_ads_follow_up_event enum{whatsapp_conversations} | The selected lead follow-up event for lead ads campaigns. |
| → omnichannel_object Object |  |
| → → app array\<JSON object\> |  |
| → → pixel array\<JSON object\> | Required |
| → → onsite array\<JSON object\> |  |
| → whats_app_business_phone_number_id numeric string or integer |  |
| → whatsapp_phone_number string |  |
| rf_prediction_id numeric string or integer | Reach and frequency prediction ID |
| source_adset_id numeric string or integer | The source adset id that this ad is copied from (if applicable). |
| start_time datetime | The start time of the set, e.g. 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . UTC UNIX timestamp |
| status enum{ACTIVE, PAUSED, DELETED, ARCHIVED} | Only ACTIVE and PAUSED are valid for creation. The other statuses can be used for update. If it is set to PAUSED , all its active ads will be paused and have an effective status ADSET_PAUSED . |
| targeting Targeting object | An ad set's targeting structure. "countries" is required. See targeting . |
| time_based_ad_rotation_id_blocks list\<list\<int64\>\> | Specify ad creative that displays at custom date ranges in a campaign as an array. A list of Adgroup IDs. The list of ads to display for each time range in a given schedule. For example display first ad in Adgroup for first date range, second ad for second date range, and so on. You can display more than one ad per date range by providing more than one ad ID per array. For example set time_based_ad_rotation_id_blocks to [[1], [2, 3], [1, 4]]. On the first date range show ad 1, on the second date range show ad 2 and ad 3 and on the last date range show ad 1 and ad 4. Use with time_based_ad_rotation_intervals to specify date ranges. |
| time_based_ad_rotation_intervals list\<int64\> | Date range when specific ad creative displays during a campaign. Provide date ranges in an array of UNIX timestamps where each timestamp represents the start time for each date range. For example a 3-day campaign from May 9 12am to May 11 11:59PM PST can have three date ranges, the first date range starts from May 9 12:00AM to May 9 11:59PM, second date range starts from May 10 12:00AM to May 10 11:59PM and last starts from May 11 12:00AM to May 11 11:59PM. The first timestamp should match the campaign start time. The last timestamp should be at least 1 hour before the campaign end time. You must provide at least two date ranges. All date ranges must cover the whole campaign length, so any date range cannot exceed campaign length. Use with time_based_ad_rotation_id_blocks to specify ad creative for each date range. |
| time_start datetime | Time start |
| time_stop datetime | Time stop |
| tune_for_category enum{NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES} | tune_for_category |
| value_rule_set_id numeric string or integer | Value Rule Set ID |
| value_rules_applied boolean | value_rules_applied |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `id` in the return type. Struct  {`id`: numeric string, `success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 2695 | The ad set creation reached its campaign group(ios14) limit. |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 2641 | Your ad includes or excludes locations that are currently restricted |
| 190 | Invalid OAuth 2.0 Access Token |
| 900 | No such application exists. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)

## Deleting


This operation has been deprecated with [Marketing API V8](https://developers.facebook.com/docs/graph-api/changelog/version8.0/#ad-accounts).
 You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#)On This Page[Ad Account Adsets](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#Creating)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#example-2)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/adsets/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR69pvSJY5B8Ryiltad5ssOSlstRQKqe1xB05QYgBZfEkK8PKbmXKJpic_DV5g_aem_U0AXNApKg0AaFqFt0Swy0w&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6hChnCMzDekVzNIabuYhgTLv9g5B-ZdIfjCtAfHS04tNFDvXZoVEsV8HUWGQ_aem_2Kl8yXQbOtJ1V3g2xUJcag&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7I6zH67AZejYtPN3eNVXMEnofp6gICMhvuxVwqlbMwjOeT7OJ3x6tRAD7FWA_aem_qAB0e0dJH8JbOk8_CH7I-Q&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR71JUo29SG2A9iUf6jKL9FZFzI7KvIXVaTJlD1NedOTzmiEiO36jtWMF6eaJA_aem_2CMroDhN9Sm6fYIJWWPDoQ&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63tTtnnBFNAqtKS3MTbsTeMUgX6sAoyBhWAMjL6AYxJFKpv8xZKxEzKK9lCQ_aem_LT8QfXpkmngPGUOLCvnUwA&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4HM40G0Q4yvqyPQfKa59S1w_dm6uOf8Zic73XPJ7L1uH2L2RRIxoD51Zmjxw_aem_1LqjHanh0JjXzWtU_JQ45g&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63tTtnnBFNAqtKS3MTbsTeMUgX6sAoyBhWAMjL6AYxJFKpv8xZKxEzKK9lCQ_aem_LT8QfXpkmngPGUOLCvnUwA&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6LQ6p32fAo_uKnkTWlfgoSRTgDaTN1V_-2t1Y-87tdoGeEieWJ6CXUHNSamA_aem_XLkUmoXspz-2GEd6MqUWRg&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7I6zH67AZejYtPN3eNVXMEnofp6gICMhvuxVwqlbMwjOeT7OJ3x6tRAD7FWA_aem_qAB0e0dJH8JbOk8_CH7I-Q&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6LQ6p32fAo_uKnkTWlfgoSRTgDaTN1V_-2t1Y-87tdoGeEieWJ6CXUHNSamA_aem_XLkUmoXspz-2GEd6MqUWRg&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7I6zH67AZejYtPN3eNVXMEnofp6gICMhvuxVwqlbMwjOeT7OJ3x6tRAD7FWA_aem_qAB0e0dJH8JbOk8_CH7I-Q&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4HM40G0Q4yvqyPQfKa59S1w_dm6uOf8Zic73XPJ7L1uH2L2RRIxoD51Zmjxw_aem_1LqjHanh0JjXzWtU_JQ45g&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63tTtnnBFNAqtKS3MTbsTeMUgX6sAoyBhWAMjL6AYxJFKpv8xZKxEzKK9lCQ_aem_LT8QfXpkmngPGUOLCvnUwA&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7I6zH67AZejYtPN3eNVXMEnofp6gICMhvuxVwqlbMwjOeT7OJ3x6tRAD7FWA_aem_qAB0e0dJH8JbOk8_CH7I-Q&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7dXD-vanhqrsqWgGGw1J-O6jdOOcENIPvXDx7iZUms6KMgpAICxX8z97B_3g_aem_bEcG9NuoDYWuffUyYa0uog&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR71JUo29SG2A9iUf6jKL9FZFzI7KvIXVaTJlD1NedOTzmiEiO36jtWMF6eaJA_aem_2CMroDhN9Sm6fYIJWWPDoQ&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6LQ6p32fAo_uKnkTWlfgoSRTgDaTN1V_-2t1Y-87tdoGeEieWJ6CXUHNSamA_aem_XLkUmoXspz-2GEd6MqUWRg&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR71JUo29SG2A9iUf6jKL9FZFzI7KvIXVaTJlD1NedOTzmiEiO36jtWMF6eaJA_aem_2CMroDhN9Sm6fYIJWWPDoQ&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4HM40G0Q4yvqyPQfKa59S1w_dm6uOf8Zic73XPJ7L1uH2L2RRIxoD51Zmjxw_aem_1LqjHanh0JjXzWtU_JQ45g&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7I6zH67AZejYtPN3eNVXMEnofp6gICMhvuxVwqlbMwjOeT7OJ3x6tRAD7FWA_aem_qAB0e0dJH8JbOk8_CH7I-Q&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51umzFymvSZ3cjTu7Od5O9IJoA2feUA4q94Q1uF5RrVEYvvBkn1iFGVysZF2orH-Y968kl92QkqEVTVb9SJiiyZTcwtf3GU7ZhTaHC4XW1jLIfNyFSijv3irWnwkaqnutxftkzacRZFswBMv0lYDkduro)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo