<!-- Fonte: Ad Creative _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Creative

Updated: Dec 11, 2025Use Facebook ads with your existing customers and to reach new ones. Each guide describes Facebook ads products to help meet your advertising goals. There are several types of ad units with a variety of appearances, placement and creative options. For guidelines on ads units as creative content, see [Facebook Ads Guide⁠](https://www.facebook.com/business/ads-guide/?tab0=Mobile%20News%20Feed).

## Creative

An ad creative is an object that contains all the data for visually rendering the ad itself. In the API, there are different types of ads that you can create on Facebook, all listed [here](https://developers.facebook.com/docs/reference/ads-api/adcreative#overview).If you have a [campaign](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group) with the Page Post Engagement Objective, you can now create an ad that promotes a post made by the page. This is considered a Page post ad. Page post ads require a field called `object_story_id`, which is the `id` property of a Page post. Learn more about [Ad Creative, Reference](https://developers.facebook.com/docs/reference/ads-api/adcreative#create).An ad creative has three parts:

- The ad creative itself, defined by the visual attributes of the creative object
- [Placement](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative#placements) that the ad runs on
- [Preview](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative#previews) of the unit itself, per placement
To create the ad creative object, make the following call:
```
curl -X POST \
  -F 'name="Sample Promoted Post"' \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
The response to the API call is the `id` of the creative object. Store this; you need it for the ad object:
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


### Limits

There are limits on the creative’s text, image size, image aspect ratio and other aspects of the creative. See the [Ads Guide⁠](https://www.facebook.com/business/ads-guide).

### Read

In the Ads API, each field you want to retrieve needs to be asked for explicitly, except for `id`. Each object’s [Reference](https://developers.facebook.com/docs/reference/ads-api/adcreative#read) has a section for reading back the object and lists what fields are readable. For the creative, it’s the same fields as specified when creating the object, and `id`.
```
curl -G \
  -d 'fields=name,object_story_id' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<CREATIVE_ID>
```


## Placements

A placement is where your ad is shown on Facebook, such as on Feed on desktop, Feed on a mobile device or on the right column. See  [Ads Product Guide⁠](https://www.facebook.com/business/ads-guide/).We encourage you to run ads across the full range of available placements. Facebook’s ad auction is designed to deliver ad impressions to the placement most likely to drive campaign results at the lowest possible cost.The easiest way to take advantage of this optimization is to leave this field blank. You can also select specific placements in an ad set’s target_spec.This example has a page post ad. The available placements are Mobile Feed, Desktop Feed and Right column of Facebook. In the API, see [Placement Options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/advanced-targeting#placement). If you choose `desktopfeed` and `rightcolumn` as the `page_type`, the ad runs on Desktop Feed and Right column placements. Any ad created below this ad set has only the desktop placement.
```
curl -X POST \
  -F 'name=Desktop Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=10000' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["facebook","audience_network"]
  }' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=1000' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


## Preview an Ad

You preview an ad in one of two ways—with [ad preview API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/generatepreview) or the [ad preview plugin](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-preview-plugin).There are three ways to generate a preview with the API:

- By ad ID
- By ad creative ID
- By supplying a creative spec
Following the [reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/generatepreview#html) docs for the preview API, the minimum required API call is:
```
curl -G \
  --data-urlencode 'creative="<CREATIVE_SPEC>"' \
  -d 'ad_format="<AD_FORMAT>"' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```
The creative spec is an array of each field and value required to create the ad creative.Currently, our ad creative call looks like this:
```
curl -X POST \
  -F 'name="Sample Promoted Post"' \
  -F 'object_story_id="<PAGE_ID>_<POST_ID>"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
Take `object_story_id` and use it in the preview API call:
```
curl -G \
  -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \
  -d 'ad_format=<AD_FORMAT>' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```
The available values for `ad_format` differ a bit from `page_types`. But, in this scenario, Desktop Feed and Right column of Facebook are selected. This requires you to make two API calls to generate the previews for each placement:
```
curl -G \
  -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \
  -d 'ad_format=DESKTOP_FEED_STANDARD' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```

```
curl -G \
  -d 'creative={"object_story_id":"<PAGE_ID>_<POST_ID>"}' \
  -d 'ad_format=RIGHT_COLUMN_STANDARD' \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/generatepreviews
```
The response is an iFrame that’s valid for 24 hrs.

## See More


- [Ad Creative](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-creative)
- [Facebook App Ads](https://developers.facebook.com/docs/app-ads)
- [Ads Guide⁠](https://www.facebook.com/business/ads-guide)
Did you find this page helpful?ON THIS PAGECreativeLimitsReadPlacementsPreview an AdSee More$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$