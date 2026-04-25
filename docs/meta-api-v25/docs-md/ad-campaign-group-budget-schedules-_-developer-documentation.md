<!-- Fonte: Ad Campaign Group Budget Schedules _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/budget_schedules -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Campaign Group Budget Schedules

Updated: Nov 17, 2023
Budget scheduling allows you to schedule budget increases for your campaign or ad set budget based on days or times when you anticipate higher sales opportunities, peak traffic periods or other promotional time periods. You can find additional information in the [Meta Business Help Center⁠](https://www.facebook.com/business/help/633318028866693) and in the [About budget scheduling](https://developers.facebook.com/docs/graph-api/reference/high-demand-period) section


## Reading


#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v25.0/{campaign-id}/budget_schedules HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcampaign-id%7D%2Fbudget_schedules&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

### Search Parameter Usage Example :


If we have three high demand periods set up with following specs

```
high_demand_periods:[{
      id:1,
      time_start:1,
      time_end:3,
      ...
},{
      id:2,
      time_start:3,
      time_end:5,
      ...
},{
      id:3,
      time_start:6,
      time_end:8,
      ...
}]
```

A request can be made with `time_start` prameter as shown below

```
curl -X GET
 -d 'access_token={ACCESS_TOKEN}'
 https://graph.facebook.com/{API_VERSION}/{CAMPAIGN_ID}/budget_schedules?time_start=5
```

This request will fetch all high demand periods with `time_end` value greater than `time_start` parameter, returning

```
data:[{
      id:3,
      time_start:6,
      time_end:8,
      ...
}]
```

A similar request can be made with `time_stop` parameter as shown below

```
curl -X GET
 -d 'access_token={ACCESS_TOKEN}'
 https://graph.facebook.com/{API_VERSION}/{CAMPAIGN_ID}/budget_schedules?time_stop=3
```

This request will fetch all high demand periods with `time_start` value less than `time_stop` parameter, returning

```
data:[{
      id:1,
      time_start:1,
      time_end:3,
      ...
}]
```


#### Parameters


| Parameter | Description |
| --- | --- |
| time_start datetime/timestamp | Search period start time. Filters out any HDPs with stop time \<= time_start from the response. |
| time_stop datetime/timestamp | Search period stop time. Filters out any HDPs with start time \>= time_stop from the response. |


#### Fields


Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {}
}
```


##### data


A list of [HighDemandPeriod](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/high-demand-period) nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


#### Error Codes


| Error Code | Description |
| --- | --- |
| 613 | Calls to this api have exceeded the rate limit. |
| 100 | Invalid parameter |


## Creating


### /{campaign_id}/budget_schedules


You can make a POST request to *budget_schedules* edge from the following paths:


- [/{campaign_id}/budget_schedules](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign-group/budget_schedules)

When posting to this edge, no Graph object will be created.


#### Parameters


| Parameter | Description |
| --- | --- |
| budget_value int64 | Amount of budget increase during the high demand period. Can be expressed in either an absolute amount, or a multiplier value. The type is specified through the budget value type. required |
| budget_value_type enum{ABSOLUTE, MULTIPLIER} | Type of budget value. This sets if the specified budget value is an increase by an absolute amount or by a multiplier value. required |
| time_end int64 | Time when the high demand period should end. required |
| time_start int64 | Time when the high demand period should start. required |


#### Return Type


This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *id* in the return type.

```
Struct  {
id: numeric string,
}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |


## Updating


You can't perform this operation on this endpoint.


## Deleting


You can't perform this operation on this endpoint.
Did you find this page helpful?ON THIS PAGEReadingCreating/{campaign_id}/budget_schedulesUpdatingDeleting$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5jl7EyP0f6qY1qUji3_2Pi0Pxm9VMqaS7UPOPI_Y1ez9yvFn6ynzd0T3_jxA_aem_8AwsGwoPunhyWOiPR9EB3g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7YvSflSK13RIXAo6sLsp8rNYW2cdLkTJ79CLZXChM5RrHUi3xGVsHSn3lhxQ_aem_Vi3f_mX26laRD2wcQTlbFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4nhMMQ37P76GUE6DA-OQwJGyJizHfRonntAHJQxyNNQ1p1zi0rarEMJqqeDw_aem_nKfOEyx3tsBBmhXQduWUdA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5yr0836EKpc0wiGN9q-Y1u1vjyNPaOKDMRKCKLbG7DmScczH-sl2MzhoJVLw_aem_ZhGprlhmRjQn0_k5yCxOvg&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR52__WRwidcYwR2nRKG_KQzG6o82HeU4p1VhDSlvPq5e9PHDWLedRKliOXCZQ_aem_GFmU0TZAFRANN0I-TyMC9w&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$