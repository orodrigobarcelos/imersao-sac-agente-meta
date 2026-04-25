<!-- Fonte: Ads that Click to Instagram _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ads that Click to Instagram

Updated: Dec 17, 2025This guide explains how to create and publish ads that click to Instagram using the Marketing API.Ads that click to Instagram Direct send people that click on your ads directly into conversations with your business in Instagram Direct. Use these ads to reach people at scale and deliver standout, individualized service.Ads that click to Instagram support ads with an image, a video, a carousel, or a slideshow. You can also include call prompts in your ad.If you’re interested in creating ads that send people to Messenger or WhatsApp chats, see [Ads that Click to Messenger](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp) and [Ads that Click to WhatsApp](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp) for guidance. You can also create ads that pick the destination the user is most likely to respond from, see [Ads that Click to Multidestination](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-multidestination) for more information.

### Ad Creation Overview

This document outlines the steps you need to follow to set up your integration for click to Instagram ads. You will need to:

- [Create an ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-1)
- [Create an ad set that links your ads to your ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-2)
- [Create an ad creative for the Instagram ad type you want to serve](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-3)
- [Create an ad by linking your ad creative to your ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-4)
- [Publish your ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-instagram#step-5)


## Before you begin

This guide assumes you have:

- [An ad account with Meta⁠](https://adsmanager.facebook.com/adsmanager/)
- [An Instagram account](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/instagramads/get-started#account-id)
- [Uploaded any assets, such as images or videos, to be used in your ads to Meta servers](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)
To make successful calls to all endpoints in this guide, you will need:

- A Page access token requested by a person who can perform the ADVERTISE task on the Page
- The following permissions must be granted a person using your app: - `ads_management` - `pages_manage_ads` - `pages_read_engagement` - `pages_show_list`


## Step 1: Create an ad campaign

Start by creating your ad campaign. To do this, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/campaigns` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| name string | Required. Name for the click to Instagram campaign. |
| objective enum | Required. Campaign’s objective. Supported objectives are OUTCOME_ENGAGEMENT , OUTCOME_SALES , and OUTCOME_TRAFFIC . |
| special_ad_categories list\<Object\> | Required. Special ad categories associated with the click to Instagram campaign. See the Ad Campaign reference for more details. |
| status enum | Optional. Valid options are PAUSED and ACTIVE . If this status is PAUSED , all its active ad sets and ads will be paused and have an effective status CAMPAIGN_PAUSED . |


#### Request


```
curl -X POST \
  -F 'name=Click to Instagram Campaign' \
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

To verify that you have successfully created a click to Instagram campaign, you can make a `GET` request to `/<AD_CAMPAIGN_ID>`. See the [Ad Campaign reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group#Reading) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,status,objective' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>
```


#### Response


```
{  "name": "Click to Instagram Campaign",  "status": "ACTIVE",  "objective": "OUTCOME_ENGAGEMENT",  "id": "<AD_CAMPAIGN_ID>"}
```


## Step 2: Create an ad set

Once you have an ad campaign, create your ad set. To create an ad set, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/adsets` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| bid_amount unsigned int32 | Required if bid_strategy is set to LOWEST_COST_WITH_BID_CAP or COST_CAP . The maximum amount you want to pay for a result based on your optimization_goal . |
| bid_strategy enum | Optional. The bid strategy for this campaign to suit your specific business goals. See the Ad Campaign reference for more details. Values: LOWEST_COST_WITHOUT_CAP , LOWEST_COST_WITH_BID_CAP , COST_CAP |
| billing_event enum | Required. Must be set to IMPRESSIONS for ads that click to Instagram. Meta bills you when your ad is shown to people. |
| campaign_id numeric string or integer | Required. A valid click to Instagram campaign you wish to add this ad set to. |
| daily_budget int64 | Required if lifetime_budget is not set. The daily budget defined in your account currency. Allowed only for ad sets with a duration (difference between end_time and start_time ) longer than 24 hours. Either daily_budget or lifetime_budget must be greater than 0 . |
| destination_type string | Required. Set to INSTAGRAM_DIRECT for single-destination click to Instagram ads. |
| end_time datetime | Required when lifetime_budget is specified. When creating an ad set with a daily_budget , specify end_time=0 or leave this field empty to set the ad set as ongoing with no end date. Example: 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . UTC UNIX timestamp. |
| lifetime_budget int64 | Required if daily_budget is not set. The lifetime budget of the ad set defined in your account currency. If specified, you must also specify an end_time . Either daily_budget or lifetime_budget must be greater than 0 . |
| name string | Required. The name of the click to Instagram ad set. |
| optimization_goal enum | Required. What the ad set is optimizing for. Depending on the campaign’s objective, the ad set may be eligible for different optimization goals. OUTCOME_ENGAGEMENT : Engagement objective can optimize for CONVERSATIONS , and LINK_CLICKS . OUTCOME_SALES : Sales objective can optimize for CONVERSATIONS , OFFSITE_CONVERSIONS , LINK_CLICKS , IMPRESSIONS , and REACH . OUTCOME_TRAFFIC : Traffic objective can optimize for CONVERSATIONS , LANDING_PAGE_VIEWS , LINK_CLICKS , IMPRESSIONS , REACH , and POST_ENGAGEMENT . |
| promoted_object AdPromotedObject | Required. The object this ad set is promoting across all its ads. For ads that click to Instagram, promoted_object has the following conditions: page_id : Required. The ID of the Facebook Page. See Ad Set, Promoted Object for more details. |
| start_time datetime | Optional. The start time of the ad set. This field will default to the current time if no value is provided. Example: 2015-03-12 23:59:59-07:00 or 2015-03-12 23:59:59 PDT . UTC UNIX timestamp. |
| status enum | Optional. The status of the ad set. It can be different from the effective status due to its parent campaign. This field will default to ACTIVE if no value is provided. Vales: ACTIVE , PAUSED , DELETED , ARCHIVED |
| targeting Targeting object | Required. The targeting structure of an ad that clicks to Instagram. See Targeting for more details. |
| time_start datetime | Optional. Interchangeable with start_time . |
| time_stop datetime | Required when lifetime_budget is specified. Interchangeable with end_time . |

Visit the [Ad Account Ad Set reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adsets) for the complete list of available parameters.

#### Request


```
curl -X POST \  -F 'access_token=<ACCESS_TOKEN>' \  -F 'bid_strategy=LOWEST_COST_WITHOUT_CAP' \  -F 'billing_event=IMPRESSIONS' \  -F 'campaign_id=<AD_CAMPAIGN_ID>' \  -F 'daily_budget=<DAILY_BUDGET>' \  -F 'destination_type=INSTAGRAM_DIRECT' \  -F 'name=Click to Instagram Ad Set' \  -F 'optimization_goal=CONVERSATIONS' \  -F 'promoted_object={    "page_id": "<PAGE_ID>"  }' \  -F 'status=ACTIVE' \  -F 'start_time=<START_TIME>' \  -F 'targeting={    "geo_locations": { "countries":["US","CA"] },    "device_platforms": ["mobile", "desktop"]  }' \https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/adsets
```


#### Response


```
{  "id": "<AD_SET_ID>"}
```


### Updating

You can update an ad set by making a `POST` request to `/<AD_SET_ID>`.

### Reading

To verify that you have successfully created a click to Instagram ad set, you can make a `GET` request to `/<AD_SET_ID>`. See the [Ad Set reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,destination_type,optimization_goal,bid_strategy,status' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>
```


#### Response


```
{  "name": "Click to Instagram Ad Set",  "destination_type": "INSTAGRAM_DIRECT",  "optimization_goal": "CONVERSATIONS",  "bid_strategy": "LOWEST_COST_WITHOUT_CAP",  "status": "ACTIVE",  "id": "<AD_SET_ID>"}
```


## Step 3: Create an ad creative

The ad creative allows you to add assets to your ads. To create an ad creative, make a `POST` request to the `/act_<AD_ACCOUNT_ID>/adcreatives` endpoint where `<AD_ACCOUNT_ID>` is the ID for your Meta ad account. Your request must include:

### Parameters


| Name | Description |
| --- | --- |
| name string | Required. The name for your ad creative. |
| object_story_spec AdCreativeObjectStorySpec | Required. An object containing information about a message. See Ad Creative Object Story Spec for more details. Required: page_id : The ID of the Facebook Page instagram_actor_id : Instagram Account ID. There are three ways to obtain an Instagram account ID : Business Manager owned Instagram account, Page connected Instagram account, and Page backed Instagram account. Optional: link_data : The spec for a link page post or carousel ad photo_data : The spec for a photo page post text_data : The spec for a text page post video_data : The spec for a video page post |
| degrees_of_freedom_spec | Optional. See Standard Enhancements for Advantage+ Creative for more details. |

Visit th [Ad Creative reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) for the complete list of available parameters.If you see the error “Creative Must Provide enroll_status for Standard Enhancements” on v17.0+, refer to [Standard Enhancements for Advantage+ Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/standard-enhancements) and fix it.

### Filling out a Page welcome message

The default message that a customer sees is “Hello! Can I get more info on this?”. You can create more tailored user experiences for your ads that click to Instagram by customizing your ads’ greeting message in the `page_welcome_message` field under `object_story_spec`.

#### Example

Adding text icebreakers with an optional automated response. String interpolation `{{user_first_name}}`, `{{user_last_name}}`, `{{user_full_name}}`, and `{{page_name}}` can be used in the greeting message and automated response. For example, “Hi {{user_first_name}}. Welcome to {{page_name}}!”
```
"page_welcome_message": {
  "type": "VISUAL_EDITOR",
  "version": 2,
  "landing_screen_type": "welcome_message",
  "media_type": "text",
  "text_format": {
    "customer_action_type": "ice_breakers",
    "message": {
      "text": "<GREETING_MESSAGE>",
      "ice_breakers": [
        {
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        },
        {
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        },
        {
          "title": "<ICEBREAKER>",
          "response": "<AUTO_RESPONSE>"
        }
      ]
    }
  }
}
```


### Ad creative create examples


#### Image Creative

Refer to [Ad, Image](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image) for more details.
```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "image_hash": "<IMAGE_HASH>"
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


#### Video Creative

Refer to [Video and Carousel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads) for more details.
```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "message": "<AD_PRIMARY_TEXT>",
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "video_data": {
         "video_id": "<VIDEO_ID>",
         "image_url": "<THUMBNAIL_URL>"
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


#### Ad that uses a messaging flow configured on a partner app


```
curl -X POST \  -F 'name=Sample ad creative' \  -F 'object_story_spec={       "page_id": "<PAGE_ID>",       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",       "link_data": {         "message": "<AD_PRIMARY_TEXT>",         "image_hash": "<IMAGE_HASH>"           "call_to_action": {           "type": "INSTAGRAM_MESSAGE",           "value": {             "app_destination": "INSTAGRAM_DIRECT"           }         }       }     }' \  -F 'asset_feed_spec={       "additional_data": {         "partner_app_welcome_message_flow_id": "<FLOW_ID>",       }     }' \  -F 'access_token=<ACCESS_TOKEN>' \https://graph.facebook.com/v19.0/act_<AD_ACCOUNT_ID>/adcreatives
```
For more information about messaging app flows, refer to [Welcome message flows](https://developers.facebook.com/docs/messenger-platform/ads/ads-welcome-message-flows) in the Messenger Platform documentation.

#### Carousel Creative

Refer to [Video and Carousel Ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads) for more details.
```
curl -X POST \
  -F 'name=Sample ad creative' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_actor_id": "<INSTAGRAM_ACCOUNT_ID>",
       "link_data": {
         "message": "<AD_PRIMARY_TEXT>",
         "page_welcome_message": "<PAGE_WELCOME_MESSAGE>",
         "call_to_action": {
           "type": "INSTAGRAM_MESSAGE",
           "value": {
             "app_destination": "INSTAGRAM_DIRECT"
           }
         },
         "child_attachments": [
              {
                "image_hash": "<IMAGE_HASH>",
                "call_to_action": {
                  "type": "INSTAGRAM_MESSAGE",
                  "value": {
                    "app_destination": "INSTAGRAM_DIRECT"
                  }
                },
                "name": "<AD_HEADLINE>"
              },
              {
                "video_id": "<VIDEO_ID>",
                "picture": "<THUMBNAIL_URL>",
                "call_to_action": {
                  "type": "INSTAGRAM_MESSAGE",
                  "value": {
                    "app_destination": "INSTAGRAM_DIRECT"
                  }
                },
                "name": "<AD_HEADLINE>"
              }
         ],
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
  -F 'instagram_user_id=<INSTAGRAM_USER_ID>' \
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
       "instagram_actor_id": "<INSTAGRAM_ACTOR_ID>",
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
  &instagram_actor_id=<IG_USER_ID>
  &call_to_action="{'type':MESSAGE_PAGE,'value':{'app_destination':'MESSENGER'}}"
  &access_token=<ACCESS_TOKEN>"
```
Where `object_story_id` is the post ID in the format of `postOwnerID_postID` and `instagram_actor_id` is either a Page-connected Instagram account ID or the Page-backed Instagram account ID. See more details in [Set Up Instagram Accounts With Pages](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/pages-ig-account).

### Updating

You can update an [ad creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) by making a `POST` request to `/<AD_CREATIVE_ID>`.

### Reading

To verify that you have successfully created a click to Instagram ad creative, you can make a `GET` request to `/<AD_CREATIVE_ID>`. See [Ad Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=name,object_story_spec{link_data{call_to_action,page_welcome_message}}' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>
```


#### Response


```
{  "name": "Sample ad creative",  "object_story_spec": {    "link_data": {      "call_to_action": {        "type": "INSTAGRAM_MESSAGE",        "value": {          "app_destination": "INSTAGRAM_DIRECT"        }      },      "page_welcome_message": {        "type": "VISUAL_EDITOR",        "version": 2,        "landing_screen_type": "welcome_message",        "media_type": "text",        "text_format": {          "customer_action_type": "ice_breakers",          "message": {            "text": "Sample greeting message",            "ice_breakers": [              {                "title": "Sample icebreaker 1"              },              {                "title": "Sample icebreaker 2"              },              {                "title": "Sample icebreaker 3"              }            ]          }        }      }    }  },  "id": "<AD_CREATIVE_ID>"}
```


### Alternative objective ID in creating an ad creative

Use this API to get connected Instagram accounts with the Instagram Account Backed Page ID (IABP ID).
```
curl -X GET \
  -F 'fields="iabp_id"' \
  -F 'business_id=<BUSINESS_ID>' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/connected_instagram_accounts_with_iabp
```
Then when you [use post as ads](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads), you can use the IABP ID as the value of `object_id`.
```
curl -i -X POST \
  "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives
  ?object_id=<IABP_ID> // iabp_id instead of page_id
  &instagram_user_id=<IG_USER_ID>
  &source_instagram_media_id=<IG_ORGANIC_MEDIA_ID>
  &access_token=<API_ACCESS_TOKEN>"
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
  -F 'name=Click to Instagram Ad' \
  -F 'adset_id=<AD_SET_ID> \
  -F 'creative={
       "creative_id": "<AD_CREATIVE_ID>"
     }' \
  -F 'status=PAUSED \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### Response


```
{  "id": "<AD_ID>"}
```


### Call to action

You can also set a call to action when creating your ad.
```
"call_to_action": {
  "value": {"app_destination":"INSTAGRAM_DIRECT"},
  "type": "MESSAGE_PAGE"
}
```


### Updating

You can update an [ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) by making a `POST` request to `/<AD_ID>`.

### Reading

To verify that you have successfully created a click to Instagram ad, you can make a `GET` request to `/<AD_ID>`. See the [ad reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) for the complete list of available parameters.

#### Request


```
curl -X GET -G \
  -d 'fields=status,adset_id,campaign_id \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


#### Response


```
{  "status": "PAUSED",  "adset_id": "<AD_SET_ID>",  "campaign_id": "<AD_CAMPAIGN_ID>",  "id": "<AD_ID>"}
```


## Step 5: Publish your ad

Verify your ad exists in Ads Manager. When you are ready to publish your changes, select your campaign, the ad set for the campaign, and the ad, and click the **Publish** button.You can also publish your ad using the API by sending a `POST` request to `/<AD_ID>` with the `status` parameter set to `ACTIVE` where `<AD_ID>` is the ad you want to publish.

### Request


```
curl -X POST \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


### Response


```
{  "success": true}
```
Your ad will be reviewed by Meta, and the `effective_status` will be `PENDING_REVIEW`. Once approved, the status will automatically update to `ACTIVE`, and your ad will be delivered.

### Request


```
curl -X GET -G \
  -d 'fields=status,effective_status' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>
```


### Response


```
{  "status": "ACTIVE",  "effective_status": "PENDING_REVIEW",  "id": "<AD_ID>"}
```
Did you find this page helpful?ON THIS PAGEAd Creation OverviewBefore you beginStep 1: Create an ad campaignParametersRequestResponseUpdatingReadingRequestResponseStep 2: Create an ad setParametersRequestResponseUpdatingReadingRequestResponseStep 3: Create an ad creativeParametersFilling out a Page welcome messageExampleAd creative create examplesImage CreativeVideo CreativeAd that uses a messaging flow configured on a partner appCarousel CreativeResponseCreating ad creatives using Instagram contentInstagram PostsInstagram ImagesCreating ad creatives using Facebook contentUpdatingReadingRequestResponseAlternative objective ID in creating an ad creativeStep 4: Create an adParametersRequestResponseCall to actionUpdatingReadingRequestResponseStep 5: Publish your adRequestResponseRequestResponse$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$