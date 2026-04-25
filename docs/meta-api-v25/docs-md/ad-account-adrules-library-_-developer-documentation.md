<!-- Fonte: Ad Account Adrules Library _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adrules_library -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Adrules Library

Updated: Apr 2, 2024

## Reading

AdAccountAdRulesLibrary

#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v25.0/{ad-account-id}/adrules_library HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fadrules_library&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


This endpoint doesn't have any parameters.


#### Fields


Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {}
}
```


##### data


A list of [AdRule](https://developers.facebook.com/docs/marketing-api/reference/ad-rule) nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


#### Error Codes


| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |


## Creating


### /act_{ad_account_id}/adrules_library


You can make a POST request to *adrules_library* edge from the following paths:


- [/act_{ad_account_id}/adrules_library](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adrules_library)

When posting to this edge, an [AdRule](https://developers.facebook.com/docs/marketing-api/reference/ad-rule) will be created.


#### Parameters


| Parameter | Description |
| --- | --- |
| account_id numeric string | Ad Account ID. This is inferred from the path. |
| evaluation_spec Object | Defines the evaluation spec upon which a rule will be executed required evaluation_type enum{SCHEDULE, TRIGGER} required filters list\<Object\> required field string required value numeric, string, boolean, list\<\>, or object-like arrays required operator enum{GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL, IN_RANGE, NOT_IN_RANGE, IN, NOT_IN, CONTAIN, NOT_CONTAIN, ANY, ALL, NONE} required Show child parameters trigger Object type enum{METADATA_CREATION, METADATA_UPDATE, STATS_MILESTONE, STATS_CHANGE, DELIVERY_INSIGHTS_CHANGE} required field string value numeric, string, boolean, list\<\>, or object-like arrays operator enum{GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL, IN_RANGE, NOT_IN_RANGE, IN, NOT_IN, CONTAIN, NOT_CONTAIN, ANY, ALL, NONE} Show child parameters Show child parameters |
| execution_spec Object | Defines the execution spec upon which a rule will be executed required execution_type enum{DCO, PING_ENDPOINT, NOTIFICATION, PAUSE, REBALANCE_BUDGET, CHANGE_BUDGET, CHANGE_BID, ROTATE, UNPAUSE, CHANGE_CAMPAIGN_BUDGET, ADD_INTEREST_RELAXATION, ADD_QUESTIONNAIRE_INTERESTS, INCREASE_RADIUS, UPDATE_CREATIVE, UPDATE_LAX_BUDGET, UPDATE_LAX_DURATION, AUDIENCE_CONSOLIDATION, AUDIENCE_CONSOLIDATION_ASK_FIRST, AD_RECOMMENDATION_APPLY} required is_once_off boolean execution_options list\<Object\> field string required value numeric, string, boolean, list\<\>, or object-like arrays required operator enum{EQUAL, IN} required Show child parameters Show child parameters |
| name string | The friendly name of a rule, optional for inline rules required |
| schedule_spec Object | Specifies the schedule with which a rule will be evaluated schedule_type enum{DAILY, HOURLY, SEMI_HOURLY, CUSTOM} required schedule list\<Object\> start_minute int64 end_minute int64 days list\<int64\> Show child parameters Show child parameters |
| status enum {ENABLED, DISABLED, DELETED, HAS_ISSUES} | The status of a rule |


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
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 2703 | Rules that turn off ads can’t have cost conditions. You need to change the rule’s conditions or action. |
| 190 | Invalid OAuth 2.0 Access Token |


## Updating


You can't perform this operation on this endpoint.


## Deleting


You can't perform this operation on this endpoint.
Did you find this page helpful?ON THIS PAGEReadingCreating/act_{ad_account_id}/adrules_libraryUpdatingDeleting$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5jl7EyP0f6qY1qUji3_2Pi0Pxm9VMqaS7UPOPI_Y1ez9yvFn6ynzd0T3_jxA_aem_8AwsGwoPunhyWOiPR9EB3g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7YvSflSK13RIXAo6sLsp8rNYW2cdLkTJ79CLZXChM5RrHUi3xGVsHSn3lhxQ_aem_Vi3f_mX26laRD2wcQTlbFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4nhMMQ37P76GUE6DA-OQwJGyJizHfRonntAHJQxyNNQ1p1zi0rarEMJqqeDw_aem_nKfOEyx3tsBBmhXQduWUdA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5yr0836EKpc0wiGN9q-Y1u1vjyNPaOKDMRKCKLbG7DmScczH-sl2MzhoJVLw_aem_ZhGprlhmRjQn0_k5yCxOvg&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR52__WRwidcYwR2nRKG_KQzG6o82HeU4p1VhDSlvPq5e9PHDWLedRKliOXCZQ_aem_GFmU0TZAFRANN0I-TyMC9w&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$