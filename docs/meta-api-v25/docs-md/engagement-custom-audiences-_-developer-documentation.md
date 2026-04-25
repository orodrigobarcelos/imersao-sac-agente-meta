<!-- Fonte: Engagement Custom Audiences _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/engagement-custom-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Engagement Custom Audiences

Updated: Jun 14, 2024Create a custom audience based on people who engaged with your content on Facebook or Instagram. Currently supported audience types include Page, Instagram business profile, lead ads, Instant Experience ads, Shopping and augmented reality.This guide describes the API by using Page engagement audiences as an example.
Facebook updates your custom audience for Page engagements by continuously adding people that engage with your Page. When you first create this audience, Facebook prefills it with a list of people who already engaged with your Page in the given retention period.

- Since September 2018, we do not support `subtype` for custom audiences for websites, apps, engagement custom audiences, and audiences from offline conversion data. The exception is that `subtype` is supported for engagement custom audiences for video.
- If you are creating audiences from Europe or targeting people in Europe, see our [Dec 2, 2020 non-versioned change](https://developers.facebook.com/docs/graph-api/changelog/non-versioned-changes/dec-2-2020).


## Create an Audience

To create an engagement custom audience, your ad account must accept the [Terms of Service for Custom Audiences⁠](https://www.facebook.com/ads/manage/customaudiences/tos.php), in [Ads Manager⁠](https://business.facebook.com/adsmanager/manage).To create an audience listing people who engaged with your Page based on the `page_engaged` event:
```
curl -X POST \
  -F 'name="My Test Engagement Custom Audience"' \
  -F 'rule={
       "inclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 31536000,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_engaged"
                 }
               ]
             }
           }
         ]
       }
     }' \
  -F 'prefill=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


### Parameters


| Name | Description |
| --- | --- |
| name string | Required. Custom audience name. |
| rule JSON object | Required. Rules to define the audience. Follows the same syntax as website custom audience . |

Engagement custom audiences are types of custom audiences. For all available fields, see the [Custom Audience Reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience).**Note:** Each ad account can create a maximum of 500 engagement custom audiences.

## Engagement Rules

You can determine if Facebook adds someone to the custom audience or not with the [Audience Rules](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/audience-rules).Specify the `type` and `id` fields inside `event_sources` in the rule to indicate the `type` and `id` of the engagement object. The `id` field takes a single object ID, or an array of IDs of the same type.These are supported event sources and corresponding engagement object IDs:

- `page`: Facebook page ID.
- `lead`: Lead form ID.
- `ig_lead_generation`: Lead form ID.
- `canvas`: Canvas ID.
- `ig_business`: Instagram business profile ID.
- `shopping_page`: Facebook Shop Page ID.
- `shopping_ig`: Instagram Shop ID.
- `ar_experience`: An Instant Expereince that uses an AR effect.
- `ar_effects`: A Facebook or Instagram effect you own. This doesn’t include effects used in ads.
Each rule consists of an `object_id` and an `event_name`.

#### Pages

Set `object_id` to your Page ID. Under `event_name`, use one of the following engagement events:

- `page_engaged`: People who visited your Page or engaged with any of your Page’s content or ads, on Facebook or Messenger. This is the most inclusive engagement type and includes all other types of engagement.
- `page_visited`: People who have visited your Page.
- `page_liked`: People who currently like your Page. ([See details on retention and rules related to page likes](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/engagement-custom-audiences#page-likes-retention-and-rules).)
- `page_messaged`: People who sent a message to your Page.
- `page_cta_clicked`: People who have clicked any call-to-action buttons on your Page (e.g., “Contact Us” or “Shop Now”).
- `page_or_post_save`: People who have saved your Page or any of your Page posts.
- `page_post_interaction`: People who have interacted with any of your Page posts. Interactions include reactions (i.e., Like, Love, Haha, Wow, Sad, Angry), shares, comments, link clicks or carousel swipes.


#### Lead Ads

Set `object_id` to `FORM_ID` and set the `rule` to track one of the following lead ads events:

- `lead_generation_submitted`: All users who completed the form and submitted it.
- `lead_generation_dropoff`: All people who close the form without submitting it. They may or may not have filled in any of the fields.
- `lead_generation_opened`: All people who opened the lead generation form regardless of whether or not they submitted the form.


#### Instant Experiences

Set `object_id` to `"CANVAS_ID"`. The `rule` should track one of the following events:

- `instant_shopping_document_open`
- `instant_shopping_document_pause`
- `instant_shopping_document_resume`
- `instant_shopping_document_close`
- `instant_shopping_did_scroll`
- `instant_shopping_element_click`
- `instant_shopping_element_impression`


#### Instagram Business Profile

The `object_id` should be the `"INSTAGRAM_BUSINESS_PROFILE_ID"`, and the `rule` should track one of the following Instagram business profile events:

- `ig_business_profile_all`: People who visited your Instagram business profile or engaged with any of your Instagram business profile’s content or ads. This is the most inclusive engagement type and includes all other types of engagement. It’s a union of `ig_business_profile_engaged`, `ig_user_messaged_business`, and `ig_user_messaged_business`.
- `ig_business_profile_engaged`: People who engagement with your Instagram business profile or engaged with any of your Instagram business profile’s content or ads.
- `ig_user_messaged_business`: People who messaged your Instagram business profile.
- `ig_business_profile_visit`: People who visited your Instagram business profile.
- `ig_business_profile_ad_saved`: People who saved either organic content or an ad from your Instagram business profile.
- `ig_ad_like`
- `ig_ad_comment`
- `ig_ad_share`
- `ig_ad_save`
- `ig_ad_cta_click`
- `ig_ad_carousel_swipe`
- `ig_organic_like`
- `ig_organic_comment`
- `ig_organic_share`
- `ig_organic_save`
- `ig_organic_swipe`
- `ig_organic_carousel_swipe`
Instagram Media Creator type is currently not supported for video engagement custom audience creation.

#### Shopping

A shopping engagement rule should track one of the following events:

- `VIEW_CONTENT`: People who have viewed your product detail page. This option is available globally.
- `ADD_TO_CART`: People who have added your product to their shopping cart. This is available only to checkout enabled businesses, and only to consumers in the United States.
- `PURCHASE`: People who have purchased your products. This is available only to checkout enabled business, and only to consumers in the United States.
To create a rule that adds people who have viewed your product:
```
curl -i -X POST
-F 'name="test_api"'\
-F 'rule= {
  "inclusions": {
    "operator": "or",
    "rules": [
      {
        "event_sources": [
          {
            "id": "<ID>",
            "type": "shopping_ig"
          }
        ]
        "retention_seconds": <RETENTION_SECONDS>,
        "filter": {
          "operator": "and",
          "filters": [
            {
            "field":"event",
            "operator":"eq",
            "value": "VIEW_CONTENT"
            }
          ]
        }
      }
    ]
  }
}
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
The `page_messaged` and `ig_user_messaged_business` parameters may not be available in Europe due to new privacy rules.

#### Augmented Reality

Augmented reality engagement custom audiences can contain two parts: AR experience and AR effect.

- For an AR experience engagement custom audience, set the `object_id` to the AR ads data container ID and for the `event_name` filed use either `ar_camera_open` or `camera_cta_click`.
- For an AR effect engagement custom audience, set the `object_id` to the AR effect ID and use `ar_effect_open` for the `event_name` field.


### Max Retention Days

For legal and privacy requirements, we allow different maximum retention days for each event source type:

- Lead Generation Ads: 90 days
- Instagram business profile: 730 days
- Page: 730 days - **Note**: [Page likes audience has no retention](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/engagement-custom-audiences#page-likes-retention-and-rules)
- Instant Experiences, formerly known as Canvas: 730 days
- Shopping: 365 days. The data is available since April 2020.
- Augmented reality: 365 days


### Engagement Rules with Exclusion Section

Engagement audience rules are compatible with website custom audience rules. Therefore, they can have multiple inclusion and exclusion rules. Users that match at least one of the rules will be added to the audience.In the following example, we create an audience that includes users that visited your page or engaged with your page, but excludes people who clicked the call-to-action:
```
curl -X POST \
  -F 'name="My Test Engagement Custom Audience"' \
  -F 'rule={
       "inclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 31536000,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_engaged"
                 }
               ]
             }
           }
         ]
       },
       "exclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 31536000,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_cta_clicked"
                 }
               ]
             }
           }
         ]
       }
     }' \
  -F 'prefill=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
For more information, see [Custom Audiences from Your Website](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/website-custom-audiences).

### Multiple Rules

Engagement audiences can have multiple rules, and users that match **at least one** of the rules will be added to the audience. An example of creating an audience that includes users that messaged your page or clicked the call-to-action:
```
curl -X POST \
  -F 'name="My Test Engagement Custom Audience"' \
  -F 'rule={
       "inclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 31536000,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_engaged"
                 },
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_engaged"
                 }
               ]
             }
           }
         ]
       }
     }' \
  -F 'prefill=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


### Multiple Pages

Rules are not limited to a single page. You can have a different page for each rule, and people who engaged with at least one of the pages, and we will include them in the audience.The following is an example of an audience that includes all people that visited at least one of three pages:
```
curl -X POST \
  -F 'name="My Test Engagement Custom Audience"' \
  -F 'rule={
       "inclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               },
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 31536000,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_engaged"
                 }
               ]
             }
           }
         ]
       }
     }' \
  -F 'prefill=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
For details on Custom Audiences see the [Custom Audience Reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience).

### Page Likes Retention and Rules

Page likes audience has no retention (`retention_seconds=0`). Also, Page likes rules can’t be combined with other Page events.The following is an example of creating a Page likes audience:
```
curl -X POST \
  -F 'name="Page Likes Audience Name"' \
  -F 'rule={
       "inclusions": {
         "operator": "or",
         "rules": [
           {
             "event_sources": [
               {
                 "id": "<PAGE_ID>",
                 "type": "page"
               }
             ],
             "retention_seconds": 0,
             "filter": {
               "operator": "and",
               "filters": [
                 {
                   "field": "event",
                   "operator": "eq",
                   "value": "page_liked"
                 }
               ]
             }
           }
         ]
       }
     }' \
  -F 'prefill=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
Did you find this page helpful?ON THIS PAGECreate an AudienceParametersEngagement RulesPagesLead AdsInstant ExperiencesInstagram Business ProfileShoppingAugmented RealityMax Retention DaysEngagement Rules with Exclusion SectionMultiple RulesMultiple PagesPage Likes Retention and Rules$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$