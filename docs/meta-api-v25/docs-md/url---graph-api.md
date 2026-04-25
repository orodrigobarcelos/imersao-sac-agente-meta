<!-- Fonte: URL - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/v25.0/url -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# URL `/?id={url}`


Represents a URL shared in a Post or in a Comment on a Post.


Refer to our [News Tab Indexing API](https://developers.facebook.com/docs/news-tab-indexing) documentation for additional information.
 [○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)

## Reading



Get information about a URL that was shared in a Post or a Comment on a Post.


### Requirements



| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Any access token can be used to make this request. |
| [Features](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |
| [Page Tasks](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |
| [Permissions](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |


### Limitations



- Engagement values returned are not precise but do reflect user engagement with a URL.
- You are limited to 10 GET requests per URL, per app, per hour.


### Parameters



Include the following query string parameters to augment the request.


| Parameter | Description |
| --- | --- |
| access_token Required string | An access token . |
| fields string | A comma-separated list of fields you want to request. |
| id string | The url to be shared. |
| scopes string | A comma-separated list of scopes. |


### Fields



| Property Name | Description | Type |
| --- | --- | --- |
| `app_links` | AppLinks data associated with this URL, if available. | `AppLinks` |
| id | The URL itself. | string |
| engagement | Counts of different ways people interacted with the URL Note that engagement values are intentionally not precise, but you can be confident they accurately reflect user engagement with a URL. | object |
| → comment_count | Number of comments on the URL. | int |
| → comment_plugin_count | Number of comments on the plugin gathered using the Comments Plugin on your site. | int |
| → reaction_count | Number of reactions to the URL. | int |
| → share_count | Number of times the URL was shared. | int |
| og_object | The Open Graph object that is canonically associated with this URL. | OGObject |
| → id | ID of object. | string |
| → description | The description of the object, if available. | string |
| → title | The title of the object, if available. | string |
| → type | The object type. | og:type |
| → updated_time | When the object was last updated. | datetime |


### Examples



To get information about a URL published in a Post or Comment, send a `GET` request to `https://graph.facebook.com` with the `id` parameter set to the URL, any fields about the URL, and an access token requested from the User or Page who published the Post or Comment.


The follow example shows the engagement for the URL, https://www.facebook.com, that was shared by the User represented by the User access token.
 *Formatted for readability.*
```
curl -i -X GET \
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com
    &fields=engagement
    &access_token={user-access-token}"
```


On success your app receives the following engagement counts for the URL that was shared:

```
{
  "engagement": {
    "reaction_count": 514919172,
    "comment_count": 68687082,
    "share_count": 975739682,
    "comment_plugin_count": 1641
  },
  "id": "https://www.facebook.com"
}
```
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)

## Creating


You can't perform this operation on this endpoint.
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)

## Updating


Update a URL.


### Requirements



| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Any access token can be used to make this request. |
| [Features](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |
| [Page Tasks](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |
| [Permissions](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#) | Not applicable. |


### Examples



To update information about a URL published in a Post or Comment, send a `POST` request to `https://graph.facebook.com` with the `id` parameter set to the URL, the `scrape` parameter set to `true`, any `fields` about the URL, and an access token requested from the User or Page who published the Post or Comment.


The follow example updates the URL, https://www.facebook.com/my-update, that was shared by the User represented by the User access token.
 *Formatted for readability.*
```
curl -i -X POST \
 "https://graph.facebook.com/{latest-graph-api-version}/
    ?id=https://www.facebook.com/my-update
    &scrape=true
    &access_token={user-access-token}"
```


On success your app receives the following engagement counts for the URL that was shared:

```
{
  "success": true
}
```


### Query String Parameters


Include the following query string parameters to augment the request.


| Parameter | Description |
| --- | --- |
| access_token Required string | An access token . |
| fields string | A comma-separated list of fields you want to request. |
| id Required string | The url to be updated. The url must be encoded so that it does not interfere with the scrape parameter. |
| scrape Required boolean | Value must be true . |


#### Example Request


```
POST /{version}/?id={url}&scrape=true
Host: graph.facebook.com
```


#### Example Response


```
{
  "success": true
}
```
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)

## Deleting


You can't perform this operation on this endpoint.
[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)[○](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#)On This Page[URL /?id={url}](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#url---id--url-)[Reading](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#reading)[Requirements](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#requirements)[Limitations](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#limitations)[Parameters](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#fields)[Examples](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#examples)[Creating](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#publish)[Updating](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#update)[Requirements](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#requirements-2)[Examples](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#examples-2)[Query String Parameters](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#readfields)[Deleting](https://developers.facebook.com/docs/graph-api/reference/v25.0/url#delete) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fhqFTAYlPT0n-VDjq88MAMml2ZzfYwKdApH7qvFSOIfzwapTAB5QW3g7-XQ_aem_Dhi9hxdKXcYntrNEI80LYA&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7j0jksf3MThPjKx-jBTi7N-Q1Eaqkx2lzdkGjpcZT96d6oQyiwlCGjWiDoKg_aem_Fap0zGMJW4WZg2wfWE03NA&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5avz9O9JNFn1NTICKeT7phkf-kB89pFdVMur68tyO03moWGmWwBs8fUg0T5A_aem_mVs15rSD62YVUcKt1kAqMQ&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR70Vyo4bOjO_CHEDIV24h4l2Cg0TKxXsCGbmc72Vah0guZvb8jDc1Rnfqm92A_aem_cI3ujI1iICrV16Xls_tH4g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7g8RxRL2v2jMR1IXVY-s6maA601MPVQLz-NV8rNRkIRT5pJsSWH3WGF_GotA_aem_CuCEJ2v327cstOHELWvU5A&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR70Vyo4bOjO_CHEDIV24h4l2Cg0TKxXsCGbmc72Vah0guZvb8jDc1Rnfqm92A_aem_cI3ujI1iICrV16Xls_tH4g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6WR6tfzN3koDU5gLZ8wktbThbuixRfipXxt0_3OX5NGC8SkqG6zGKi7tnuEg_aem_rDDFIgN7sssqMN-b3btMfw&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR70Vyo4bOjO_CHEDIV24h4l2Cg0TKxXsCGbmc72Vah0guZvb8jDc1Rnfqm92A_aem_cI3ujI1iICrV16Xls_tH4g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6fhqFTAYlPT0n-VDjq88MAMml2ZzfYwKdApH7qvFSOIfzwapTAB5QW3g7-XQ_aem_Dhi9hxdKXcYntrNEI80LYA&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4OOXY4zQZvJBqiCnp4QrHs1HKPVtZ8gYEne3aLE8ojKEwLo4-93OvSEeSTcw_aem_lBJmjK67y1JCqm3kpvtF1g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6WR6tfzN3koDU5gLZ8wktbThbuixRfipXxt0_3OX5NGC8SkqG6zGKi7tnuEg_aem_rDDFIgN7sssqMN-b3btMfw&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7j0jksf3MThPjKx-jBTi7N-Q1Eaqkx2lzdkGjpcZT96d6oQyiwlCGjWiDoKg_aem_Fap0zGMJW4WZg2wfWE03NA&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5avz9O9JNFn1NTICKeT7phkf-kB89pFdVMur68tyO03moWGmWwBs8fUg0T5A_aem_mVs15rSD62YVUcKt1kAqMQ&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5bpU5lV7K9NG5PLCsQTBJfA3DmqOhnRpFGmn2wSoR2FCYv4aWtRQ3_SQV68Q_aem_RwHdtNz1G5X7ubnIKhCXfQ&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4OOXY4zQZvJBqiCnp4QrHs1HKPVtZ8gYEne3aLE8ojKEwLo4-93OvSEeSTcw_aem_lBJmjK67y1JCqm3kpvtF1g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7g8RxRL2v2jMR1IXVY-s6maA601MPVQLz-NV8rNRkIRT5pJsSWH3WGF_GotA_aem_CuCEJ2v327cstOHELWvU5A&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5avz9O9JNFn1NTICKeT7phkf-kB89pFdVMur68tyO03moWGmWwBs8fUg0T5A_aem_mVs15rSD62YVUcKt1kAqMQ&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6WOzTiJ_egNYV1HXDKGHjPE3TqTwKdFJ2t5wHvq26stNGT_WO1qrzl1eRnCg_aem_mNkSzgPSfP7AstNTHDdn_Q&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6JQTkq3JkEFW7BbI3_Ku2exV8H5Xc6osbQyyyxX_SUZPWi_ncu8qy00BgLkg_aem_yveQ5e8HgW4DWt6WBdBxlw&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR70Vyo4bOjO_CHEDIV24h4l2Cg0TKxXsCGbmc72Vah0guZvb8jDc1Rnfqm92A_aem_cI3ujI1iICrV16Xls_tH4g&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5QXbeMTQzoMhfiPOsviO_VCDdchl1jV98CZEYHDwRKWqfctLNVcbGenzrpq2e4kW6XPUFPxjc4SE46MgIdHgoI8ezpUHVVZ7JI2jIL7aF90jp_tfxr7PhxEElqUIB46B4O73y1At6NXODhvpccDBhhaGU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo