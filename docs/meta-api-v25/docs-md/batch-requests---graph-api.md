<!-- Fonte: Batch Requests - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/batch-requests -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Batch Requests



Send a single HTTP request that contains multiple Facebook Graph API calls. Independent operations are processed in parallel while dependent operations are processed sequentially. Once all operations are complete, a consolidated response is passed back to you and the HTTP connection is closed.


The ordering of responses correspond with the ordering of operations in the request. You should process responses accordingly to determine which operations were successful and which should be retried in a subsequent operation.


### Limitations



- Batch requests are limited to 50 requests per batch. Each call within the batch is counted separately for the purposes of calculating API call limits and resource limits. For example, a batch of 10 API calls will count as 10 calls and each call within the batch contributes to CPU resource limits in the same manner. Please see our [Rate Limiting Guide](https://developers.facebook.com/docs/graph-api/overview/rate-limiting) for more information.
- Batch requests cannot include multiple [Adsets](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) under the same [Campaign](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group). Learn more about [batching Marketing API requests](https://developers.facebook.com/docs/marketing-api/asyncrequests).


## Batch Request



A batch request takes a JSON object consisting of an array of your requests. It returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array, and an optional body (which is a JSON encoded string).


To make a batched request, send a `POST` request to an endpoint where the `batch` parameter is your JSON object.

```
POST /ENDPOINT?batch=[JSON-OBJECT]
```


**Sample Batch Request**


In this example, we are getting information about two Pages that our app manages.
 *Formatted for readability.*
```
curl -i -X POST 'https://graph.facebook.com/me?batch=
  [
    {
      "method":"GET",
      "relative_url":"PAGE-A-ID"
    },
    {
      "method":"GET",
      "relative_url":"PAGE-B-ID"
    }
  ]
  &include_headers=false             // Included to remove header information
  &access_token=ACCESS-TOKEN'
```


Once all operations are complete, a response is sent with the result of each operation. Because the headers returned can sometimes be much larger than the actual API response, you might want to remove them for efficiency. To include header information, remove the `include_headers` parameter or set it to `true`.


**Sample Response**


The body field contains a string encoded JSON object:

```
[
  {
    "code": 200,
    "body": "{
      \"name\": \"Page A Name\",
      \"id\": \"PAGE-A-ID\"
      }"
  },
  {
    "code": 200,
    "body": "{
      \"name\": \"Page B Name\",
      \"id\": \"PAGE-B-ID\"
      }"
  }
]
```
[○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Complex Batch Requests



It is possible to combine operations that would normally use different HTTP methods into a single batch request. While `GET` and `DELETE` operations can only have a `relative_url` and a `method` field, `POST` and `PUT` operations may contain an optional `body` field. The body should be formatted as a raw HTTP POST string, similar to a URL query string.


**Sample Request**


The following example publishes a post to a Page we manage and have publish permissions and then the Page's feed in a single operation:

```
curl "https://graph.facebook.com/PAGE-ID?batch=
  [
    {
      "method":"POST",
      "relative_url":"PAGE-ID/feed",
      "body":"message=Test status update"
    },
    {
      "method":"GET",
      "relative_url":"PAGE-ID/feed"
    }
  ]
  &access_token=ACCESS-TOKEN"
```


The output of this call would be:

```
[
    { "code": 200,
      "headers": [
          { "name":"Content-Type",
            "value":"text/javascript; charset=UTF-8"}
       ],
      "body":"{\"id\":\"…\"}"
    },
    { "code": 200,
      "headers": [
          { "name":"Content-Type",
            "value":"text/javascript; charset=UTF-8"
          },
          { "name":"ETag",
            "value": "…"
          }
      ],
      "body": "{\"data\": [{…}]}
    }
]
```


The following example creates a new ad for a campaign, and then gets the details of the newly created object. Note the **URLEncoding** for the body param:

```
curl \
-F 'access_token=...' \
-F 'batch=[
  {
    "method":"POST",
    "name":"create-ad",
    "relative_url":"11077200629332/ads",
    "body":"ads=%5B%7B%22name%22%3A%22test_ad%22%2C%22billing_entity_id%22%3A111200774273%7D%5D"
  },
  {
    "method":"GET",
    "relative_url":"?ids={result=create-ad:$.data.*.id}"
  }
]' \
https://graph.facebook.com
```


The following example adds multiple pages to a Business Manager:

```
curl \
-F 'access_token=<ACCESS_TOKEN>' \
-F 'batch=[
  {
    "method":"POST",
    "name":"test1",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_1>"
  },
  {
    "method":"POST",
    "name":"test2",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_2>"
  },
  {
    "method":"POST",
    "name":"test3",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_3>"
  },
]' \
"https://graph.facebook.com/v12.0"
```


Where:


- `<ACCESS_TOKEN>` is an access token with the `business_management` permission.
- `<BUSINESS_ID>` is the ID of the Business Manager to which the pages should be claimed.
- `<PAGE_ID_n>` are the Page IDs to be claimed.
 [○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Errors



Its possible that one of your requested operations may throw an error. This could be because, for example, you don't have permission to perform the requested operation. The response is similiar to the standard Graph API, but encapsulated in the batch response syntax:

```
[
    { "code": 403,
      "headers": [
          {"name":"WWW-Authenticate", "value":"OAuth…"},
          {"name":"Content-Type", "value":"text/javascript; charset=UTF-8"} ],
      "body": "{\"error\":{\"type\":\"OAuthException\", … }}"
    }
]
```


Other requests within the batch should still complete successfully and will be returned, as normal, with a `200` status code.
 [○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Timeouts



Large or complex batches may timeout if it takes too long to complete all the requests within the batch. In such a circumstance, the result is a partially-completed batch. In a partially-completed batch, requests that are completed successful will return the normal output with the `200` status code. Responses for requests that are not successful will be `null`. You can retry any unsuccessful request.
 [○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Batch calls with JSONP



The Batch API supports JSONP, just like the rest of the Graph API - the JSONP callback function is specified using the `callback` query string or form post parameter.
 [○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Using Multiple Access Tokens



Individual requests of a single batch request can specify its own access tokens as a query string or form post parameter. In that case the top level access token is considered a fallback token and is used if an individual request has not explicitly specified an access token.


This may be useful when you want to query the API using several different User or Page access tokens, or if some of your calls need to be made using an app access token.


You must include an access token as a top level parameter, even when all individual requests contain their own tokens.
 [○](https://developers.facebook.com/docs/graph-api/batch-requests#)

## Upload Binary Data



You can upload multiple binary items as part of a batch call. In order to do this, you need to add all the binary items as multipart/mime attachments to your request, and need each operation to reference its binary items using the `attached_files` property in the operation. The `attached_files` property can take a comma separated list of attachment names in its value.


The following example shows how to upload 2 photos in a single batch call:

```
curl
     -F 'access_token=…' \
     -F 'batch=[{"method":"POST","relative_url":"me/photos","body":"message=My cat photo","attached_files":"file1"},{"method":"POST","relative_url":"me/photos","body":"message=My dog photo","attached_files":"file2"},]' \
     -F 'file1=@cat.gif' \
     -F 'file2=@dog.jpg' \
    https://graph.facebook.com
```
[○](https://developers.facebook.com/docs/graph-api/batch-requests#)



  -->
[○](https://developers.facebook.com/docs/graph-api/batch-requests#)On This Page[Batch Requests](https://developers.facebook.com/docs/graph-api/batch-requests#batch-requests)[Batch Request](https://developers.facebook.com/docs/graph-api/batch-requests#batch-request)[Complex Batch Requests](https://developers.facebook.com/docs/graph-api/batch-requests#complex-batch-requests)[Errors](https://developers.facebook.com/docs/graph-api/batch-requests#errors)[Timeouts](https://developers.facebook.com/docs/graph-api/batch-requests#timeouts)[Batch calls with JSONP](https://developers.facebook.com/docs/graph-api/batch-requests#jsonp)[Using Multiple Access Tokens](https://developers.facebook.com/docs/graph-api/batch-requests#differentaccesstokens)[Upload Binary Data](https://developers.facebook.com/docs/graph-api/batch-requests#binary) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6TSQa38WhkAXWNJrj7vJ4WaEF-24NpYytraE7P7U94kBfunWcGp-rmLrwMGA_aem_WgBx8PUMZNKGq_-SZpu8Rw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7SRuTiCATx4OLEjxpHwVXbPZfkN9oWiU3oQ9lavKDzt9YHD_R1vPdiJSSXXg_aem_HuSORV1VShZRHdCLsXuVEw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4sqwkeRPr1GfH-sffXrU1vB_3GT65Hy6OU03yJWWkZbCG2MkJaaPDKLmdj2A_aem__vS2xkEWO-lgSdo-3DRpgw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KKdEJpjdZVCjdBgniIO2OGMPlptX3hwQlX8Frn--u7u6erpz8oN57rSZT1A_aem_2bImP3XXeKD0imzdlDnNwg&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6TSQa38WhkAXWNJrj7vJ4WaEF-24NpYytraE7P7U94kBfunWcGp-rmLrwMGA_aem_WgBx8PUMZNKGq_-SZpu8Rw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4sqwkeRPr1GfH-sffXrU1vB_3GT65Hy6OU03yJWWkZbCG2MkJaaPDKLmdj2A_aem__vS2xkEWO-lgSdo-3DRpgw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KKdEJpjdZVCjdBgniIO2OGMPlptX3hwQlX8Frn--u7u6erpz8oN57rSZT1A_aem_2bImP3XXeKD0imzdlDnNwg&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4sqwkeRPr1GfH-sffXrU1vB_3GT65Hy6OU03yJWWkZbCG2MkJaaPDKLmdj2A_aem__vS2xkEWO-lgSdo-3DRpgw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6lbSyfk7oYGLoPy_N24f4ZxSxxbISE9hM-SlMCHcx_581xFZ2i6A04SHQN0A_aem_GvsJ_l_c40NkumWWdQY4NA&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6lbSyfk7oYGLoPy_N24f4ZxSxxbISE9hM-SlMCHcx_581xFZ2i6A04SHQN0A_aem_GvsJ_l_c40NkumWWdQY4NA&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KKdEJpjdZVCjdBgniIO2OGMPlptX3hwQlX8Frn--u7u6erpz8oN57rSZT1A_aem_2bImP3XXeKD0imzdlDnNwg&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR76ZkL7Z_yF5wOY_2A1_PiR87AV8GmELLcPPvYNAw0uif86J0rZkjpFL5hHYw_aem_r1EgHCg2ZjY2oVEztRtGoQ&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6SezGsMAIYOYt1_1Buy_NQk_Z2B0DISrIIT5qEtrFImo_zWrH7bxHmj_5PzQ_aem_lLM0bZNla9DerRuz51XMIw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KKdEJpjdZVCjdBgniIO2OGMPlptX3hwQlX8Frn--u7u6erpz8oN57rSZT1A_aem_2bImP3XXeKD0imzdlDnNwg&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4sqwkeRPr1GfH-sffXrU1vB_3GT65Hy6OU03yJWWkZbCG2MkJaaPDKLmdj2A_aem__vS2xkEWO-lgSdo-3DRpgw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KKdEJpjdZVCjdBgniIO2OGMPlptX3hwQlX8Frn--u7u6erpz8oN57rSZT1A_aem_2bImP3XXeKD0imzdlDnNwg&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6SezGsMAIYOYt1_1Buy_NQk_Z2B0DISrIIT5qEtrFImo_zWrH7bxHmj_5PzQ_aem_lLM0bZNla9DerRuz51XMIw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4sqwkeRPr1GfH-sffXrU1vB_3GT65Hy6OU03yJWWkZbCG2MkJaaPDKLmdj2A_aem__vS2xkEWO-lgSdo-3DRpgw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7rqbZEc1ve1Or2_3RT3gCrGHxFpZWsevXetMkyGk1wcYQgk9QOI-Kc86BdVg_aem_dxDmDT9BKqY0rH1u_e9zBA&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6SezGsMAIYOYt1_1Buy_NQk_Z2B0DISrIIT5qEtrFImo_zWrH7bxHmj_5PzQ_aem_lLM0bZNla9DerRuz51XMIw&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6sc0UYSojfjAxGVNzrtQupEn4a-p7uuVU49oJ7pvs5SnEWQnTALfOGpUjrlfTFHVstm5_qPC6UYuUC_JtrNXIL_YzEJd5X8Fu40zLdV1oAN829fW8lRCadRgNSQyjGZzxfvufS0AOvEFTlQW4Hl7YNXQ4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo