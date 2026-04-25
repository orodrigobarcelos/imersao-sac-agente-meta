<!-- Fonte: Ads that Click to Multidestination _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ads that Click to Multidestination

Updated: Dec 17, 2025This guide explains how to create and publish ads that click to multidestination using the Marketing API.Ads that click to multidestination send people that click on your ads directly into conversations with your business in the messaging app or apps (Messenger, Instagram, or WhatsApp) that they are most likely to respond from. Use these ads to reach people at scale and deliver standout, individualized service.Multidestination ads means the ad can go to any combination of the destinations: Messenger chat, Instagram chat, WhatsApp chat.If you’d like to create an ad that only goes to one destination, see:

- [Ads that Click to Messenger](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-messenger)
- [Ads that Click to Instagram](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram)
- [Ads that Click to WhatsApp](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp)


### Ad Creation Overview

This document outlines the steps you need to follow to set up your integration for click to multidestination ads. You will need to:

- [Create an ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-1)
- [Create an ad set that links your ads to your ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-2)
- [Create an ad creative for the Multi Destination ad type you want to serve](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-3)
- [Create an ad by linking your ad creative to your ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination#step-4)


## Before you begin

This guide assumes you have:

- [An ad account with Meta⁠](https://adsmanager.facebook.com/adsmanager/)
- [Uploaded any assets, such as images or videos, to be used in your ads to Meta servers](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)


## Step 1: Create an ad campaign

Start by creating your ad campaign. To do this, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/campaigns` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| name string | Required. Name for the click to mutlidestination campaign. |
| objective enum | Required. Campaign’s objective. Supported objectives are OUTCOME_ENGAGEMENT , OUTCOME_SALES , and OUTCOME_TRAFFIC . |
| special_ad_categories list\<Object\> | Required. Special ad categories associated with the click to multidestination campaign. Currently we don’t support special ad categories for ads that click to multidestination, so it needs to be NONE or empty array. See the Ad Campaign reference for more details. |
| status enum | Optional. Valid options are PAUSED and ACTIVE . If this status is PAUSED , all its active ad sets and ads will be paused and have an effective status CAMPAIGN_PAUSED . |


#### Request


```
curl -X POST \
  -F 'name=Click to Multi Destination Campaign' \
  -F 'objective=OUTCOME_ENGAGEMENT' \
  -F 'status=ACTIVE' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```


#### Response

On success, your app receives a JSON response with the ID of your newly created campaign.
```
{  "id": "<AD_CAMPAIGN_ID>"}
```


### Updating

You can update a campaign by making a `POST` request to `/<AD_CAMPAIGN_ID>`.

### Reading

To verify that you have successfully created a click to multidestination campaign, you can make a `GET` request to `/<AD_CAMPAIGN_ID>`. See the [Ad Campaign reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#Reading) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,status,objective' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>
```


#### Response


```
{  "name": "Click to Multi Destination Campaign",  "status": "ACTIVE",  "objective": "OUTCOME_ENGAGEMENT",  "id": "<AD_CAMPAIGN_ID>"}
```


## Step 2: Create an ad set

Once you have an ad campaign, create your ad set. To create an ad set, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/adsets` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| bid_amount unsigned int32 | Required if bid_strategy is set to LOWEST_COST_WITH_BID_CAP or COST_CAP . The maximum amount you want to pay for a result based on your optimization_goal . |
| bid_strategy enum | Optional. The bid strategy for this campaign to suit your specific business goals. See the Ad Campaign reference for more details. Values: LOWEST_COST_WITHOUT_CAP , LOWEST_COST_WITH_BID_CAP , COST_CAP |
| billing_event enum | Required. Must be set to IMPRESSIONS for ads that click to multidestination. Meta bills you when your ad is shown to people. |
| campaign_id numeric string or integer | Required. A valid click to multidestination campaign you wish to add this ad set to. |
| daily_budget int64 | Required if lifetime_budget is not set. The daily budget defined in your account currency. Allowed only for ad sets with a duration (difference between end_time and start_time ) longer than 24 hours. Either daily_budget or lifetime_budget must be greater than 0 . |
| destination_type string | Required. Set to MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP if you want to use all three destinations (Messenger, WhatsApp, and Instagram). Set to MESSAGING_INSTAGRAM_DIRECT_MESSENGER if you want to use Messenger and Instagram. Set to MESSAGING_MESSENGER_WHATSAPP if you want to use Messenger and WhatsApp. Set to MESSAGING_INSTAGRAM_DIRECT_WHATSAPP if you want to use WhatsApp and Instagram. Note: If you include WhatsApp in the destinations, please make sure you have WhatsApp business number connected to your page. If you include Instagram in the destinations, please make sure you have Instagram business account connected to your page. |
| end_time datetime | Required when lifetime_budget is specified. When creating an ad set with a daily_budget , specify end_time=0 or leave this field empty to set the ad set as ongoing with no end date. Example: 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . UTC UNIX timestamp. |
| lifetime_budget int64 | Required if daily_budget is not set. The lifetime budget of the ad set defined in your account currency. If specified, you must also specify an end_time . Either daily_budget or lifetime_budget must be greater than 0 . |
| name string | Required. The name of the click to multidestination ad set. |
| optimization_goal enum | Required. What the ad set is optimizing for. Must be set to CONVERSATIONS for ads that click to multidestination. Depending on the campaign’s objective, the ad set may be eligible for different optimization goals. |
| promoted_object AdPromotedObject | Required. The object this ad set is promoting across all its ads. For ads that click to multidestination, promoted_object has the following conditions: page_id : Required. The ID of the Facebook Page. See Ad Set, Promoted Object for more details. |
| start_time datetime | Optional. The start time of the ad set. This field will default to the current time if no value is provided. Example: 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . UTC UNIX timestamp. |
| status enum | Optional. The status of the ad set. It can be different from the effective status due to its parent campaign. This field will default to ACTIVE if no value is provided. Vales: ACTIVE , PAUSED , DELETED , ARCHIVED |
| targeting Targeting object | Required. The targeting structure of an ad that clicks to Instagram. See Targeting for more details. |
| time_start datetime | Optional. Interchangeable with start_time . |
| time_stop datetime | Required when lifetime_budget is specified. Interchangeable with end_time . |

Visit the [Ad Account Ad Set reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets) for the complete list of available parameters.

#### Request


```
curl -X POST \
  -F 'access_token=<ACCESS_TOKEN>' \
  -F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=<DAILY_BUDGET>' \
  -F 'destination_type=<DESTINATION_TYPE>' \
  -F 'name=<AD_SET_NAME>' \
  -F 'optimization_goal=CONVERSATIONS' \
  -F 'promoted_object={
      "page_id": "<PAGE_ID>"
    }' \
  -F 'status=ACTIVE' \
  -F 'start_time=<START_TIME>' \
  -F 'targeting={
        "geo_locations": { "countries":["US","CA"] },
        "device_platforms": ["mobile", "desktop"]
  }' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Response

On success, your app receives a JSON response with the ID of your newly created ad set.
```
{  "id": "<AD_SET_ID>"}
```


### Updating

You can update an ad set by making a `POST` request to `/<AD_SET_ID>`.

### Reading

To verify that you have successfully created a click to multidestination ad set, you can make a `GET` request to `/<AD_SET_ID>`. See the [Ad Set reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,destination_type,optimization_goal,bid_strategy' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_SET_ID>
```


#### Response


```
{  "name": "<AD_SET_NAME>",  "destination_type": "<DESTINATION_TYPE>",  "optimization_goal": "CONVERSATIONS",  "bid_strategy": "LOWEST_COST_WITHOUT_CAP'"  "id": "<AD_SET_ID>"}
```


## Step 3: Create an ad creative

The ad creative allows you to add assets to your ads. To create an ad creative, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/adcreatives` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| asset_feed_spec | Required. Specify the destinations of ads that click to Multi Destination Required: optimization_type : Must be set to DOF_MESSAGING_DESTINATION for ads that click to multidestination. call_to_actions : Array of the selected destinations of ads that click to multidestination. It needs to match with the destination_type specified in the ad set. Messenger { "type" : "MESSAGE_PAGE" , "value" : { "app_destination" : "MESSENGER" , "link" : "https://fb.com/messenger_doc/" } } WhatsApp { "type" : "WHATSAPP_MESSAGE" , "value" : { "app_destination" : "WHATSAPP" , "link" : "https://api.whatsapp.com/send" } } Instagram { "type" : "INSTAGRAM_MESSAGE" , "value" : { "app_destination" : "INSTAGRAM_DIRECT" , "link" : "https://www.instagram.com" } } |
| name string | Required. The name for your ad creative. |
| object_story_spec AdCreativeObjectStorySpec | Required. An object containing information about a message. See Ad Creative Object Story Spec for more details. Required: page_id : The ID of the Facebook Page instagram_user_id : Instagram Account ID. There are three ways to obtain an Instagram account ID : Business Manager owned Instagram account, Page connected Instagram account, and Page backed Instagram account. Optional: link_data : The spec for a link page post or carousel ad photo_data : The spec for a photo page post text_data : The spec for a text page post video_data : The spec for a video page post |
| degrees_of_freedom_spec | Optional. See Standard Enhancements for Advantage+ Creative for more details. |

Visit th [Ad Creative reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) for the complete list of available parameters.

### Filling out Page Welcome Message

The default message that a customer sees is “Hello! Can I get more info on this?”. You can create more tailored user experiences for your ads that click to multidestination by customizing your ads’ greeting message, icebreakers, and autofill messages in the `page_welcome_message` field under `object_story_spec`.For more information about icebreakers, see the [`ice_breakers` reference](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/ice-breakers).

#### Limitations


- Icebreaker titles must not be more than 80 characters.
- Icebreaker responses must not be more than 300 characters.
- Message text must not be more than 300 characters.


#### Example

Create the `page_welcome_message` object to add icebreakers with a greeting message.
```
"page_welcome_message": {
  "type":"VISUAL_EDITOR",
  "version":2,
  "landing_screen_type":"welcome_message",
  "media_type":"text",
  "text_format":{
    "customer_action_type":"ice_breakers",
    "message":{
      "ice_breakers":[
        {"title":"Can I make a purchase?","response":"This is a response 1"},
        {"title":"Can I see a menu?", "response":"This is a response 2"},
        {"title":"Where are you located?", "response":"This is a response 3"}],
      "quick_replies":[],
      "text":"Hi {{user_first_name}}! Please let us know how we can help you."}
  },
  "user_edit":false,
  "surface":"visual_editor_new"
}
```


### Ad creative create examples

Add the `page_welcome_message` field to the creative as follows.

#### Request


```
curl -X POST \
-F 'name=<CREATIVE_NAME>' \
-F 'object_story_spec={
     "page_id": "438346666550309",
     "link_data": {
       "name": "<AD_HEADLINE>",
       "message": "<AD_PRIMARY_TEXT>",
       "image_hash": "<IMAGE_HASH>"
       "link": "https://fb.com/messenger_doc/",
       "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
       "call_to_action": {
         "type": "MESSAGE_PAGE",
         "value": {
           "app_destination": "MESSENGER"
         }
       }
     }
   }' \
-F 'asset_feed_spec={
     "optimization_type": "DOF_MESSAGING_DESTINATION",
     "call_to_actions": [
       {
         "type": "MESSAGE_PAGE",
         "value": {
           "app_destination": "MESSENGER",
           "link": "https://fb.com/messenger_doc/"
         }
       },
       {
         "type": "WHATSAPP_MESSAGE",
         "value": {
           "app_destination": "WHATSAPP",
           "link": "https://api.whatsapp.com/send"
         }
       },
       {
         "type": "INSTAGRAM_MESSAGE",
         "value": {
           "app_destination": "INSTAGRAM_DIRECT",
           "link": "https://www.instagram.com"
         }
       }
     ]
   }' \
-F 'degrees_of_freedom_spec={
     "creative_features_spec": {
       "standard_enhancements": {
         "enroll_status": "OPT_IN"
       }
     }
   }' \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Response

On success, your app receives a JSON response with the ID of your newly created ad creative.
```
{  "id": "<AD_CREATIVE_ID>"}
```


### Creating ad creatives using Instagram content


#### Instagram Posts

Refer [Use Posts as Instagram Ads](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads) for more details.
```
curl -X POST \
  -F 'name=Sample ad creative from Instagram post' \
  -F 'object_id=<PAGE_ID>' \
  -F 'instagram_user_id=<IG_USER_ID>' \
  -F 'source_instagram_media_id=<INSTAGRAM_POST_ID>' \
  -F 'call_to_action={
       "type": "INSTAGRAM_MESSAGE",
       "value": {
         "link": "https://www.instagram.com"
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Instagram Images


```
curl -X POST \
  -F 'name=Sample ad creative from Instagram image' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_user_id": "<IG_USER_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "picture": "<IMAGE_URL>"
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         }
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Creating ad creatives using Facebook content

Refer to [Use Posts as Instagram Ads: Facebook Posts](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads#facebook-posts) for more details.
```
curl -i -X POST \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives
  ?object_story_id=<postOwnerID_postID>
  &instagram_user_id=<IG_USER_ID>
  &call_to_action="{'type':MESSAGE_PAGE,'value':{'app_destination':'MESSENGER'}}"
  &access_token=<ACCESS_TOKEN>"
```
Where `object_story_id` is the post ID in the format of `postOwnerID_postID` and `instagram_user_id` is either a Page-connected Instagram account ID or the Page-backed Instagram account ID. See more details in [Set Up Instagram Accounts With Pages](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/pages-ig-account).

### Updating

You can update an [ad creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) by making a `POST` request to `/<AD_CREATIVE_ID>`.

### Reading

To verify that you have successfully created a click to multidestination ad creative, you can make a `GET` request to `/<AD_CREATIVE_ID>`. See [Ad Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,object_story_spec{page_welcome_message},asset_feed_spec' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>
```


#### Response


```
{  "name": "<CREATIVE_NAME>",  "object_story_spec": {    "page_welcome_message": {      "type": "VISUAL_EDITOR",      "version": 2,      "landing_screen_type": "welcome_message",      "media_type": "text",      "text_format": {        "customer_action_type": "ice_breakers",        "message": {          "text": "Sample greeting message",          "ice_breakers": [            {              "title": "Sample icebreaker"            },            {              "title": "Sample icebreaker"            },            {              "title": "Sample icebreaker"            }          ]        }      }    }  },  "asset_feed_spec": {    "optimization_type": "DOF_MESSAGING_DESTINATION",    "call_to_actions": [      {        "type": "MESSAGE_PAGE",        "value": {          "app_destination": "MESSENGER",          "link": "https://fb.com/messenger_doc/"        }      },      {        "type": "WHATSAPP_MESSAGE",        "value": {          "app_destination": "WHATSAPP",          "link": "https://api.whatsapp.com/send"        }      },      {        "type": "INSTAGRAM_MESSAGE",        "value": {          "app_destination": "INSTAGRAM_DIRECT",          "link": "https://www.instagram.com"        }      }    ]  },  "id": "<AD_CREATIVE_ID>"}
```


## Step 4: Create an ad

Ads allow you to associate ad creative information with your ad sets. To create an ad, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/ads` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| name string | Required. The name for your ad creative. |
| adset_id numeric string or integer | Required. The ID of the ad set. |
| creative AdCreative | Required. The ad creative to be used by this ad. You may supply the creative_id of an existing ad creative or create a new ad creative by including all required fields. See Ad Creative for more details. |
| status enum | Required. The configured status of the ad. Values: ACTIVE , PAUSED , DELETED , ARCHIVED |


#### Request


```
curl -X POST \
  -F 'name=<AD_NAME>' \
  -F 'adset_id=<AD_SET_ID> \
  -F 'creative={
       "creative_id": "<AD_CREATIVE_ID>"
     }' \
  -F 'status=ACTIVE \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### Response

On success, your app receives a JSON response with the ID of your newly created ad.
```
{  "id": "<AD_ID>"}
```


### Call to action

You can also set a call to action when creating your ad.
```
"asset_feed_spec": {
  "optimization_type": "DOF_MESSAGING_DESTINATION",
  "call_to_actions": [
    {
      "type": "MESSAGE_PAGE",
      "value": {
        "app_destination": "MESSENGER",
        "link": "https://fb.com/messenger_doc/"
      }
    },
    {
      "type": "INSTAGRAM_MESSAGE",
      "value": {
        "app_destination": "INSTAGRAM_DIRECT",
        "link": "https://www.instagram.com"
      }
    }
  ]
}
```
See the [Asset Feed Spec documentation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec) for more information.

### Updating

You can update an [ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) by making a `POST` request to `/<AD_ID>`.

### Reading

To verify that you have successfully created a click to multidestination ad, you can make a `GET` request to `/<AD_ID>`. See the [ad reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=status,adset_id \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


#### Response


```
{  "status": "ACTIVE",  "adset_id": "<AD_SET_ID>",  "id": "<AD_ID>"}
```
Did you find this page helpful?ON THIS PAGEAd Creation OverviewBefore you beginStep 1: Create an ad campaignParametersRequestResponseUpdatingReadingRequestResponseStep 2: Create an ad setParametersRequestResponseUpdatingReadingRequestResponseStep 3: Create an ad creativeParametersFilling out Page Welcome MessageLimitationsExampleAd creative create examplesRequestResponseCreating ad creatives using Instagram contentInstagram PostsInstagram ImagesCreating ad creatives using Facebook contentUpdatingReadingRequestResponseStep 4: Create an adParametersRequestResponseCall to actionUpdatingReadingRequestResponse$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$