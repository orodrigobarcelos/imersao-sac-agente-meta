<!-- Fonte: Get Started with Advantage+ Creative _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/advantage-creative/get-started -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Get Started with Advantage+ Creative

Updated: Feb 3, 2026This guide covers creating ads and ad creatives with opted-in Advantage+ creative features.Previously, Advantage+ creative was only supported through standard enhancements, a bundle of Advantage+ creative features. Starting with Marketing API v22.0 and applying to all subsequent versions, the opt-in and preview functionality for standard enhancements will be deprecated. Instead, you can opt-in to or preview individual Advantage+ creative features by following the guidelines outlined in this document.

## Before You Begin

Set up your ad campaigns using the following instructions:

- [Create an ad campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad-campaign)
- [Create an ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad-set)


## Step 1: Create an d or ad creative opted into Advantage+ creative features

[Create an ad](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad) using the [`/ads` endpoint](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/adgroup) or [create a standalone ad creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) using the [`/adcreatives`](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative) endpoint. With either approach, specify the individual opt-in features in the `creative_features_spec` parameter.

### Example request

To implement the `image_touchups`, `inline_comment`, and `image_templates` opt-in features:
```
// creative example
curl -X POST \
  -F 'name=Advantage+ Creative Creative' \
  -F 'degrees_of_freedom_spec={
    "creative_features_spec": {
      "image_touchups": {
        "enroll_status": "OPT_IN"
      },
     "inline_comment": {
        "enroll_status": "OPT_IN"
      },
     "image_template": {
        "enroll_status": "OPT_IN"
      }
    }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives

// ad example
curl -X POST \
  -F 'adset_id=<ADSET_ID>' \
  -F 'creative={
    "name": "Advantage+ Creative Adgroup",
    "object_story_spec": {
      "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<URL>",
         "message": "You got this.",
      },
      "page_id": "<PAGE_ID>"
    },
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "image_touchups": {
          "enroll_status": "OPT_IN"
        },
       "inline_comment": {
          "enroll_status": "OPT_IN"
        },
       "image_template": {
          "enroll_status": "OPT_IN"
        }
      }
    }
  }' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Features

These are the Advantage+ creative opt-in features that can be implemented in the `creative_features_spec` parameter.

| Name | Description |
| --- | --- |
| adapt_to_placement | Optional. Default is opt-in. Opt-in if you want to automatically fit images to placements based on what is predicted to work best. By default, 4:5 and 9:16 placements are enabled. If you wish to control how the images are adjusted, you can use the customizations field to control the settings. See the aspect_ratio_config and image_crop_style fields in the Ad Creative Feature Customizations reference documentation for more details. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled *Image touch-ups in Ads Manager. |
| add_text_overlay | Optional. Opt-in if you want to add information from catalog items as visually-unique overlays The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Add dynamic overlays in Ads Manager. If you want to have manual control on how the overlay is rendered, see the Ad Creative Link Data Image Layer Spec reference documentation for more details. |
| creative_stickers | Optional. Opt-in if you want to add AI-generated stickers to help tell your story better and make your call-to-actions easier to understand. We’ll automatically place CTA stickers based on where they’re likely to perform best. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Create sticker CTA in Ads Manager. |
| description_automation | Optional. For Advantage+ catalog ads, opt-in if you want item information from your catalog to be used for your ad’s description based on what each person who views your ad is likely to engage with. For static carousel ads, opt-in if you want your carousel description to be dynamically chosen when to show. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Dynamic description in Ads Manager. |
| enhance_cta | Optional. Opt-in if you want keyphrases from your ad sources to be paired with your CTA. The enroll_status field can be set to OPT_IN or OPT_OUT . The customizations field can be set to below to use potential high-performing phrases identified by AI : { "text_extraction": { "enroll_status": "OPT_IN" } Note: This feature is labeled Enhance CTA in Ads Manager. |
| image_background_gen | Optional. Opt-in if you want different backgrounds for eligible product images to be created and the version that your audience is most likely to respond to delivered. This feature is generated with AI. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Generate backgrounds in Ads Manager. |
| image_brightness_and_contrast | Optional. Opt-in if you want the brightness and contrast of your image to be adjusted when likely to improve performance. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Adjust brightness and contrast in Ads Manager. |
| image_templates | Optional. Opt-in if you want overlays added that show text you have provided along with your selected ad creative when it is likely to improve performance. This feature is generated with AI. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Add overlays in Ads Manager. |
| image_touchups | Optional. Opt-in if you want your chosen media to be automatically cropped and expanded to fit more placements. Only applicable to image ads. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Visual-touch ups in Ads Manager. |
| image_uncrop | Optional. Opt-in if you want your image to be automatically expanded to fit more placements. This feature is generated with AI. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Expand image in Ads Manager. |
| inline_comment | Optional. Opt-in if you want the most relevant comment to be displayed below your ad on Facebook and Instagram. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Relevant comments in Ads Manager. |
| media_type_automation | Optional. Opt-in if you want videos from your catalog to be displayed (along with images) in supported placements. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Dynamic media in Ads Manager. See Dynamic Media for more information. |
| pac_relaxation | Optional. Opt-in if you want to show media you chose for a specific aspect ratio across all placements when it’s likely to improve performance. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Flex media or Flexible media in Ads Manager. |
| product_extensions | Optional. Opt-in if you want items from your catalog to be shown next to your selected media when it’s likely to improve performance. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Show products in the Collection dropdown within format display options in Ads Manager. See Product Extensions (Add Catalog Items) Features on Marketing API for more details. |
| reveal_details_over_time | Optional. Opt-in if you want information from your website or app store product page to be revealed when people spend a few seconds looking at your ad. This can help people feel more confident before they click your call-to-action. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Reveal details over time in Ads Manager. |
| text_optimizations | Optional. Opt-in if you want text options you provide appear as primary text, headline or description when it’s likely to improve performance. We may add a caption introduction from your headline options and highlight key sentences when it’s likely to improve performance. The enroll_status field can be set to OPT_IN or OPT_OUT . The customizations field can be set to below to use potential high-performing phrases identified by AI : { "text_extraction": { "enroll_status": "OPT_IN" } Note: This feature is labeled Text improvements in Ads Manager. |
| text_translation | Optional. Opt-in if you want your ad to be translated to different languages on Facebook and Instagram. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Translate Text in Ads Manager. |
| video_auto_crop | Optional. Opt-in if you want your chosen media to be automatically cropped and expanded to fit more placements. Only applicable to video ads. The enroll_status field can be set to OPT_IN or OPT_OUT . Note: This feature is labeled Visual-touch ups in Ads Manager. |

Features specified as `OPT_IN` but ineligible for the given ad setup will be automatically removed from the `creative_features_spec` parameter. For example, `image_templates` (or **Add overlays**) is not eligible to be applied to video format creatives — if you opt-in to this feature on a video ad, it will be automatically removed as ineligible.To confirm the final configuration, use a `GET` request to retrieve the `creative_features_spec` parameter.Don’t worry if you see `standard_enhancements` or any standard enhancements sub-features appended to `creative_features_spec` when you retrieve it. As long as they are not set to `OPT_IN`, they will not be applied. Standard enhancements are in the process of being deprecated, and this behavior will be phased out once the deprecation is complete.Most Advantage+ creative features can be opted into using the `creative_features_spec` parameter with the exception of the `music` feature which is implemented with the `asset_feed_spec` parameter. To opt out of the `music` feature, pass the `assest_feed_spec.audios` parameter in as empty.

#### Example request

To opt into the `music` feature using the `asset_feed_spec` parameter:
```
curl -X POST \
  -F 'name="Advantage+ Creative Music"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'asset_feed_spec={
       "audios": [
         {
           "type": "random"
         }
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
If the opted-in features include features generated with AI, you must create the ad with a `PAUSED` status, then follow Step 2 and Step 3 below to complete the publishing process. If no AI-generated features are included, Step 2 and Step 3 are optional, and you can create the ad with an `ACTIVE` status.**Note:** When creating an ad through the `/ads` endpoint, the `status` field on the ad is set to `PAUSED` by default.

## Step 2: Preview for Advantage+ creative

See the [Ad Previews reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/generatepreview) for more information on the existing functionality of previews.To preview an Advantage+ creative feature, add the `creative_feature` parameter to your existing preview request with the desired feature name specified.Features that support preview include: `image_templates`, `image_touchups`, `video_auto_crop`, `enhance_cta`, `text_optimizations`, `image_background_gen`, `image_uncrop`, and `description_automation`.

#### Example request


```
curl -X GET -G \
  -d 'ad_format="DESKTOP_FEED_STANDARD"' \
  -d 'creative_feature=<FEATURE_NAME> \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_ID>/previews
```


#### Example response


```
{  "data": [    {      "body": "<iframe src='<PREVIEW_URL>'></iframe>",      "transformation_spec": {        "<FEATURE_NAME>": [          {            "body": "<iframe src='<PREVIEW_URL>'></iframe>",            "status": "eligible"          }        ]      }    }  ]}
```
Click on the returned URL to see the previews.**Note:** If a `transformation_spec` object is not returned, the creative is not eligible for the Advantage+ creative feature on the chosen placement, and the feature will not be applied.Once you have reviewed the previews and deemed them acceptable to publish, set the ad to `ACTIVE`, if it is not already. If any of the previews are not acceptable, create a new ad or ad creative without the corresponding features opted-in.

## Step 3: Set the ad status to `ACTIVE`

When your ad is ready, set its status to `ACTIVE`.

#### Example request


```
curl -X POST \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_ID>
```


## Learn More

Other Advantage+ creative features:

- [Advantage+ Creative for Catalog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-creative-for-catalog): `adapt_to_placement` and `media_type_automation`
- [Product Extensions (Add Catalog Items) Features on Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/product-extensions): `product_extensions`
- [Get Started with the Generative AI Features on Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/generative-ai-features): text_generation, `image_background_gen` and `image_uncrop`
Other adcreative resources:

- [Ad Creative Degrees Of Freedom Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-degrees-of-freedom-spec)
- [Ad Creative Features Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-features-spec)
- [Ad Creative Feature Details](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-feature-details)
- [Ad Creative Object Story Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec)
- [Ad Creative Asset Feed Spec](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/asset-feed-spec)
Advantage+ creative was previously available as standard enhancements:

- [Standard Enhancements for Advantage+ Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/standard-enhancements)
- [Advantage+ Creative Preview API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/creative-preview)
Did you find this page helpful?ON THIS PAGEBefore You BeginStep 1: Create an d or ad creative opted into Advantage+ creative featuresExample requestFeaturesExample requestStep 2: Preview for Advantage+ creativeExample requestExample responseStep 3: Set the ad status to ACTIVEExample requestLearn More$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$