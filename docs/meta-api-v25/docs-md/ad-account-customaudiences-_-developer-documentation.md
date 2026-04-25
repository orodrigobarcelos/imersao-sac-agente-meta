<!-- Fonte: Ad Account Customaudiences _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/customaudiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Customaudiences

Updated: Dec 19, 2025

## Reading

The custom audiences associated with the ad account.
**Note:** To retrieve the IDs of lookalike audiences based on your custom audiences, use the `lookalike_audience_ids` field. See [Lookalike Audiences - Managing Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences#read) for more information.

#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL
```
GET /v25.0/act_<AD_ACCOUNT_ID>/customaudiences?fields=id HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=act_%3CAD_ACCOUNT_ID%3E%2Fcustomaudiences%3Ffields%3Did&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


| Parameter | Description |
| --- | --- |
| business_id numeric string or integer | Optional. This param assists with filters, such as recently used. |
| fetch_primary_audience boolean | Default value: false fetch_primary_audience |
| fields list\<string\> | Fields to be retrieved. Default behavior is to return only the IDs. |
| filtering list\<Filter Object\> | Filters on the report data. This parameter is an array of filter objects. field string required operator enum {EQUAL, NOT_EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL, IN_RANGE, NOT_IN_RANGE, CONTAIN, NOT_CONTAIN, CONTAINS_ANY, CONTAINS_ALL, NOT_CONTAINS_ANY, STEM_MATCH, IN, NOT_IN, STARTS_WITH, ENDS_WITH, ANY, ALL, AFTER, BEFORE, ON_OR_AFTER, ON_OR_BEFORE, NONE, TOP} required value string required Show child parameters |
| pixel_id numeric string | Optional. This param fetches audiences associated to specific pixel. |


#### Fields


Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {}
}
```


##### data


A list of [CustomAudience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience) nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#custom-audience. |


## Creating

Your ability to create custom audiences may be limited.It is expected that you have the same audience capabilities independent of your app’s status, which could be *in development* or *live*.To create a custom audience you’ll first need to create a blank audience. Then, you’ll want to add people to the blank audience you just created by updating the [users edge](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/users) of the audience. **You can create a maximum of 500 custom audiences.**

You can't perform this operation on this endpoint.


## Updating


You can't perform this operation on this endpoint.


## Deleting


You can't perform this operation on this endpoint.
Did you find this page helpful?ON THIS PAGEReadingCreatingUpdatingDeleting$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5jl7EyP0f6qY1qUji3_2Pi0Pxm9VMqaS7UPOPI_Y1ez9yvFn6ynzd0T3_jxA_aem_8AwsGwoPunhyWOiPR9EB3g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7YvSflSK13RIXAo6sLsp8rNYW2cdLkTJ79CLZXChM5RrHUi3xGVsHSn3lhxQ_aem_Vi3f_mX26laRD2wcQTlbFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4nhMMQ37P76GUE6DA-OQwJGyJizHfRonntAHJQxyNNQ1p1zi0rarEMJqqeDw_aem_nKfOEyx3tsBBmhXQduWUdA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5yr0836EKpc0wiGN9q-Y1u1vjyNPaOKDMRKCKLbG7DmScczH-sl2MzhoJVLw_aem_ZhGprlhmRjQn0_k5yCxOvg&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR52__WRwidcYwR2nRKG_KQzG6o82HeU4p1VhDSlvPq5e9PHDWLedRKliOXCZQ_aem_GFmU0TZAFRANN0I-TyMC9w&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$