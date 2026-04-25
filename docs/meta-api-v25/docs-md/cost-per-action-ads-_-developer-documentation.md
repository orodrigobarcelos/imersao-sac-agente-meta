<!-- Fonte: Cost Per Action Ads _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/cost-per-action-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Cost Per Action Ads

Updated: Nov 11, 2025Cost Per Actions (CPA) allows you to specify conversion events and get charged by the amount of conversions. CPA for video views is also called CPV.An alternative to CPA is [oCPM](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/guides/optimized-cost-per-mille), which charges per impressions served.

## How It Works

Your bid is defined for an [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign). These fields must follow the restrictions below:

| Name | Description |
| --- | --- |
| billing_event | Defines the action you pay on. Set to LINK_CLICKS , PAGE_LIKES , OFFER_CLAIMS , or THRUPLAY . |
| optimization_goal | Defines the action you optimize for. Set to same value as your billing_event , LINK_CLICKS , PAGE_LIKES , POST_ENGAGEMENT , OFFER_CLAIMS , or THRUPLAY . |
| bid_amount | Value you place on the objective, specified in cents, minimum 1 cent. For example, bid_amount=150 means you would like to bid $1.50 on that action. This should represent the maximum value you are willing to pay for this action. |
| targeting | For those ads which optimize for connections including page_like it is required to use the excluded_connections field in the targeting in order to exclude users who have already performed the one-time conversion for the destination object. See the examples in the section below for how to specify the appropriate excluded connections. |


### Limitations


- The offsite link click action is only supported for links to offsite domains and Facebook hosted app domains.
- CPA billing for non-video view ads are based on one day click through conversions. CPV, or CPA for video view, ads are billed on 10-second video views.
- Offsite link click billing is additionally restricted to link clicks within the advertisement, which are known as *inline*.
Starting on [v9](https://developers.facebook.com/docs/graph-api/changelog/version9.0#bidding), CPA billing for app ads is deprecated, you cannot set both billing event and optimization goal to `APP_INSTALLS`. Instead, we recommend using the `impression` billing events. You can still specify `APP_INSTALLS` under `billing_event` or `optimization_goal`, but not both at the same time.See [ad set](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign) document on allowed updates to ad sets.

### Examples


#### Create

The example below creates a CPA bidded ad set. Note that for CPA ad sets, you must set a `promoted_object`.
```
curl -X POST \
  -F 'name="A CPA Ad Set"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'daily_budget=5000' \
  -F 'start_time="2025-11-18T14:06:35-0800"' \
  -F 'end_time="2025-11-25T14:06:35-0800"' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="REACH"' \
  -F 'bid_amount=1000' \
  -F 'promoted_object={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "geo_locations": {
         "countries": [
           "US"
         ]
       }
     }' \
  -F 'user_os="iOS"' \
  -F 'publisher_platforms="facebook"' \
  -F 'device_platforms="mobile"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
After that, you can create ads and put them into this ad set following the creation flow [here](https://developers.facebook.com/docs/reference/ads-api/guides/chapter-2-objective-connections).

#### Update

Change the bid to a CPA ad set:
```
curl -X POST \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="LINK_CLICKS"' \
  -F 'bid_amount=200' \
  -F 'targeting={
       "geo_locations": {
         "countries": [
           "US"
         ]
       },
       "facebook_positions": [
         "feed"
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<AD_SET_ID>/
```


### CPV example

To create an ad bidding CPV, or CPA for video views, first create an ad campaign with `objective=VIDEO_VIEWS`.
```
curl -X POST \
  -F 'name="Video Views campaign"' \
  -F 'objective="OUTCOME_ENGAGEMENT"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'is_adset_budget_sharing_enabled=0' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```
Then, set the CPA for video views `bid_info` at the ad set:
```
curl \
  -F 'name=A CPV Ad Set' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'daily_budget=500' \
  -F 'start_time=2018-02-06T04:45:29+0000' \
  -F 'end_time=2018-02-13T04:45:29+0000' \
  -F 'billing_event=VIDEO_VIEWS' \
  -F 'optimization_goal=VIDEO_VIEWS' \
  -F 'bid_amount=100' \
  -F 'targeting={
    "device_platforms": ["mobile"],
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["facebook"]
  }' \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
Did you find this page helpful?ON THIS PAGEHow It WorksLimitationsExamplesCreateUpdateCPV example$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$