<!-- Fonte: Ad Account Ad Images _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adimages -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Ad Images

Updated: Mar 24, 2026

## Reading

Ad Images that belong to this Ad Account.

#### Example

Select languageHTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK
```
GET /v25.0/{ad-account-id}/adimages HTTP/1.1Host: graph.facebook.com
```

Try it in [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fadimages&version=v25.0)
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api)

#### Parameters


| Parameter | Description |
| --- | --- |
| biz_tag_id int64 | Business tag ID to filter images. |
| business_id numeric string or integer | Optional. Assists with filters such as recently used. |
| hashes list\<string\> | Hash of the image. |
| minheight int64 | Minimum height of the image. |
| minwidth int64 | Minimum width of the image. |
| name string | Image name used in image names filter. |


#### Fields


Reading from this edge will return a JSON formatted result:

```
{
"data": [],
"paging": {},
"summary": {}
}
```


##### data


A list of [AdImage](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image) nodes.


##### paging


For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api#paging).


##### summary


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like summary=__type__).


| Field | Description |
| --- | --- |
| total_count int32 | Total number of images in the Ad Account. default |


#### Error Codes


| Error Code | Description |
| --- | --- |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |


## Creating


### /act_{ad_account_id}/adimages


You can make a POST request to *adimages* edge from the following paths:


- [/act_{ad_account_id}/adimages](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adimages)

When posting to this edge, an [AdImage](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image) will be created.


#### Parameters


| Parameter | Description |
| --- | --- |
| bytes Base64 UTF-8 string | Image file. Example: bytes = \<image content in bytes format\> |
| copy_from JSON or object-like arrays | This copies the Ad Image from the source to the destination account. {"source_account_id":"\<SOURCE_ACCOUNT_ID\>" , "hash":"02bee5277ec507b6fd0f9b9ff2f22d9c"} source_account_id numeric string hash string Show child parameters |


#### Return Type


This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and will read the node represented by *images* in the return type.

```
Map  {
string:  Map  {
string:  Struct  {
hash: string,
url: string,
url_128: string,
url_256: string,
url_256_height: string,
url_256_width: string,
height: int32,
width: int32,
name: string,
}}}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 613 | Calls to this api have exceeded the rate limit. |


## Updating


You can't perform this operation on this endpoint.


## Deleting


### /act_{ad_account_id}/adimages


You can dissociate an [AdImage](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-image) from an [AdAccount](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account) by making a DELETE request to [/act_{ad_account_id}/adimages](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/adimages).


#### Parameters


| Parameter | Description |
| --- | --- |
| hash string | Hash of the image you wish to delete. required |
| image_id string | ID of the image you wish to delete. |


#### Return Type


```
Struct  {
success: bool,
}
```


#### Error Codes


| Error Code | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to /docs/graph-api/overview/rate-limiting#ads-management. |

Did you find this page helpful?ON THIS PAGEReadingCreating/act_{ad_account_id}/adimagesUpdatingDeleting/act_{ad_account_id}/adimages$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5jl7EyP0f6qY1qUji3_2Pi0Pxm9VMqaS7UPOPI_Y1ez9yvFn6ynzd0T3_jxA_aem_8AwsGwoPunhyWOiPR9EB3g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7YvSflSK13RIXAo6sLsp8rNYW2cdLkTJ79CLZXChM5RrHUi3xGVsHSn3lhxQ_aem_Vi3f_mX26laRD2wcQTlbFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6Yl0ECMkiD06KiqEHY6z4DY3c7-seyDc-bJrMnJm8FKvN-IFWKehYB03-QyQ_aem_1qt3946lTt9Y3f_2zrtRFQ&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4_n4qWSu25xHDITS_9tbt4RHW3_fqmTQ46j9KaBsFS6OSrqoDB1RjGHu0xQQ_aem_AcozHModAmHuRcBAV-9TcA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4nhMMQ37P76GUE6DA-OQwJGyJizHfRonntAHJQxyNNQ1p1zi0rarEMJqqeDw_aem_nKfOEyx3tsBBmhXQduWUdA&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5yr0836EKpc0wiGN9q-Y1u1vjyNPaOKDMRKCKLbG7DmScczH-sl2MzhoJVLw_aem_ZhGprlhmRjQn0_k5yCxOvg&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4NoKpQNz6ha24B5FvGfxpCVQX-NCyBoTs7YaGdbMVvS3IasC29iBacXSSr-w_aem_13Rqs_GxQR35rDXqC-Pd8A&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7hh19JGNAoCnjCwrqaic0YLB7_g0d49s8r0SfwKKXwb8ZNgqLQnB5GSWUSmw_aem_IFSztUbUU0ZUt1TtiAWK-Q&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR607TSQ-yFjSeInoGCgViuDxUEMB6o5bJgnYC2a5cX-gXuRkLtw-nUFqSMP1A_aem_uuUaYdln8VqyYnkjYz752g&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR52__WRwidcYwR2nRKG_KQzG6o82HeU4p1VhDSlvPq5e9PHDWLedRKliOXCZQ_aem_GFmU0TZAFRANN0I-TyMC9w&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46nelDlmgj25oR4LWI8TsGzI__g4RSAc-pk7HoWk06ZnXokUgyzTpN91v94YKVlNAS3DJPobH4Irb3t2UMn2FZmacOI270ABruonD6cKr_KYL2d6_RTfgSFq22r_f9Ww5K8aUnQJHNmL8VDrfyGkBOX6Q)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$