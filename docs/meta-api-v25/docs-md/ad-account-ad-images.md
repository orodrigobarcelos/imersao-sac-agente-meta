<!-- Fonte: Ad Account Ad Images.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Ad Images

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#)

## Reading


Ad Images that belong to this Ad Account.


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fadimages&version=v25.0)
```
GET /v25.0/{ad-account-id}/adimages HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/adimages',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

```
/* make the API call */
FB.api(
    "/{ad-account-id}/adimages",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{ad-account-id}/adimages",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{ad-account-id}/adimages"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters


| Parameter | Description |
| --- | --- |
| biz_tag_id int64 | Business tag ID to filter images. |
| business_id numeric string or integer | Optional. Assists with filters such as recently used. |
| hashes list\<string\> | Hash of the image. |
| minheight int64 | Minimum height of the image. |
| minwidth int64 | Minimum width of the image. |
| name string | Image name used in image names filter. |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {},
    "summary": {}
}
```


#### `data`

A list of [AdImage](https://developers.facebook.com/docs/marketing-api/reference/ad-image/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).


| Field | Description |
| --- | --- |
| total_count int32 | Total number of images in the Ad Account. Default |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#)

## Creating

You can make a POST request to `adimages` edge from the following paths:

- [`/act_{ad_account_id}/adimages`](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/)
When posting to this edge, an [AdImage](https://developers.facebook.com/docs/marketing-api/reference/ad-image/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| bytes Base64 UTF-8 string | Image file. Example: bytes = \<image content in bytes format\> |
| copy_from JSON or object-like arrays | This copies the Ad Image from the source to the destination account. {"source_account_id":"\<SOURCE_ACCOUNT_ID\>" , "hash":"02bee5277ec507b6fd0f9b9ff2f22d9c"} |
| → source_account_id numeric string |  |
| → hash string |  |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node represented by `images` in the return type. Map  {string:  Map  {string:  Struct  {`hash`: string, `url`: string, `url_128`: string, `url_256`: string, `url_256_height`: string, `url_256_width`: string, `height`: int32, `width`: int32, `name`: string, }}}

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 613 | Calls to this api have exceeded the rate limit. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#)

## Deleting

You can dissociate an [AdImage](https://developers.facebook.com/docs/marketing-api/reference/ad-image/) from an [AdAccount](https://developers.facebook.com/docs/graph-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/adimages`](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/).

### Parameters


| Parameter | Description |
| --- | --- |
| hash string | Hash of the image you wish to delete. Required |
| image_id string | ID of the image you wish to delete. |


### Return Type

 Struct  {`success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#)On This Page[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#Deleting)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#parameters-3)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#return-type-2)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/adimages/#error-codes-3) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5pIHdbDwa2f8EGNxFhhukTfZu0qWhZjXWxyIV55Q-AGoUdn7fOEcWfULZrhg_aem_Bap_luZERcgrH0b4aJGDdw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7O-IkcT2XmVLnRJ2Z8SBMalR4wObbbzU3zwwmykeYYSn7GARjuijMO3_zOFQ_aem_8DmdDUQCumRBGf-oZuNtbA&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6dg_1BQ0MaaC3gAudYtkXv523Nqg-bzWAsPWgmUBXEH6yMtlaPZqgPNYdvLA_aem_AobTvlC874XOGytIU31hEA&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5pIHdbDwa2f8EGNxFhhukTfZu0qWhZjXWxyIV55Q-AGoUdn7fOEcWfULZrhg_aem_Bap_luZERcgrH0b4aJGDdw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7O-IkcT2XmVLnRJ2Z8SBMalR4wObbbzU3zwwmykeYYSn7GARjuijMO3_zOFQ_aem_8DmdDUQCumRBGf-oZuNtbA&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XcSv8f4N3XR9mn0AG9ZdTCV5AkttResa9i3rwAWKzBVTKfb0BZa96HXkoQg_aem_UeN0KXltIG-iyubdCJtW4g&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4WSXlGE2TYkMEwrEeDetj_cv5azLfZozCyBJsy1bqSLy-27mtlkMsXDvDvrA_aem__zHnoZYSPJcPBtR7eiHTyw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XcSv8f4N3XR9mn0AG9ZdTCV5AkttResa9i3rwAWKzBVTKfb0BZa96HXkoQg_aem_UeN0KXltIG-iyubdCJtW4g&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4WSXlGE2TYkMEwrEeDetj_cv5azLfZozCyBJsy1bqSLy-27mtlkMsXDvDvrA_aem__zHnoZYSPJcPBtR7eiHTyw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6msjiDB3PInuetypJCWq6ySCNkrGyPmH5270mN8rfpDFo76y6Osr6huuH0mA_aem_PD_zOgh0Z6bwKvVORpUH3w&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7XcSv8f4N3XR9mn0AG9ZdTCV5AkttResa9i3rwAWKzBVTKfb0BZa96HXkoQg_aem_UeN0KXltIG-iyubdCJtW4g&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6dg_1BQ0MaaC3gAudYtkXv523Nqg-bzWAsPWgmUBXEH6yMtlaPZqgPNYdvLA_aem_AobTvlC874XOGytIU31hEA&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5egWAhYlziVnR3Je96wDXrwoqdg7gCg_1YtHeEmpKjU6xwOIg-Gig045XABw_aem_pPKpWqAyIc5GoVlPCegwlg&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4WSXlGE2TYkMEwrEeDetj_cv5azLfZozCyBJsy1bqSLy-27mtlkMsXDvDvrA_aem__zHnoZYSPJcPBtR7eiHTyw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4WSXlGE2TYkMEwrEeDetj_cv5azLfZozCyBJsy1bqSLy-27mtlkMsXDvDvrA_aem__zHnoZYSPJcPBtR7eiHTyw&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5MNgWVqKFSWtew4PY_QvXdf-rnzPjSKH5APDMadFLsEo0lJuaIbfDfsgJrE12NEHuBgjktDwQYvPEdKL-OTZRuzCj5thuVlmCDCg1osEUhjlvVDXD1m2-Di9s-vYPLF9LLi9wx3ZyuePaUOa9QANV3dKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo