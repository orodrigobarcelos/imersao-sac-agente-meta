<!-- Fonte: Ad Videos.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Videos

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#)

## Reading


GET GraphAdAccountAdVideosEdge


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fadvideos&version=v25.0)
```
GET /v25.0/{ad-account-id}/advideos HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/advideos',
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
    "/{ad-account-id}/advideos",
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
    "/{ad-account-id}/advideos",
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
                               initWithGraphPath:@"/{ad-account-id}/advideos"
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
| max_aspect_ratio float | Maximum video aspect ratio to be used in the video aspect ratio filter. |
| maxheight int64 | Maximum video height to be used in the video height filter. |
| maxlength int64 | Maximum video duration to be used in the video duration filter. |
| maxwidth int64 | Maximum video width to be used in the video width filter. |
| min_aspect_ratio float | Minimum video aspect ratio to be used in the video aspect ratio filter. |
| minheight int64 | Minimum video height to be used in the video height filter. |
| minlength int64 | Minimum video duration to be used in the video duration filter. |
| minwidth int64 | Minimum video width to be used in the video width filter. |
| title string | Video name used in the video names filter. |


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

A list of [Video](https://developers.facebook.com/docs/graph-api/reference/video/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).


| Field | Description |
| --- | --- |
| total_count unsigned int32 | Total number of videos returned by the query. |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 100 | Invalid parameter |
| 283 | That action requires the extended permission pages_read_engagement and/or pages_read_user_content and/or pages_manage_ads and/or pages_manage_metadata |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#)

## Creating

You can make a POST request to `advideos` edge from the following paths:

- [`/act_{ad_account_id}/advideos`](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/)
When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.

### Parameters


| Parameter | Description |
| --- | --- |
| audio_story_wave_animation_handle string | Everstore handle of wave animation used to burn audio story video |
| composer_session_id string | SELF_EXPLANATORY |
| description UTF-8 string | SELF_EXPLANATORY Supports Emoji |
| edit_description_spec JSON object | This represents the schema that the client should send to WWW for the edit description spec during video upload. |
| → screen_readers array\<JSON object\> |  |
| end_offset int64 | end_offset |
| file_size int64 | The size of the video file in bytes. Using during chunked upload . |
| file_url string | SELF_EXPLANATORY |
| fisheye_video_cropped boolean | Whether the single fisheye video is cropped or not |
| front_z_rotation float | The front z rotation in degrees on the single fisheye video |
| name string | The name of the video in the library. |
| og_action_type_id numeric string or integer | SELF_EXPLANATORY |
| og_icon_id numeric string or integer | SELF_EXPLANATORY |
| og_object_id OG object ID or URL string | SELF_EXPLANATORY |
| og_phrase string | SELF_EXPLANATORY |
| og_suggestion_mechanism string | SELF_EXPLANATORY |
| original_fov int64 | Original field of view of the source camera |
| original_projection_type enum {equirectangular, cubemap, half_equirectangular} | Original Projection type of the video being uploaded |
| prompt_id string | SELF_EXPLANATORY |
| prompt_tracking_string string | SELF_EXPLANATORY |
| referenced_sticker_id numeric string or integer | SELF_EXPLANATORY |
| source string | The video, encoded as form data. See the Video Format doc for more details on video formats. |
| source_instagram_media_id numeric string | The V2 ID of the Instagram video to upload. Cannot be used with upload_phase . |
| start_offset int64 | The start position in byte of the chunk that is being sent, inclusive. Used during chunked upload . |
| time_since_original_post int64 | SELF_EXPLANATORY |
| title UTF-8 string | The name of the video being uploaded. Must be less than 255 characters. Special characters may count as more than 1 character. Supports Emoji |
| transcode_setting_properties string | Properties used in computing transcode settings for the video |
| unpublished_content_type enum {SCHEDULED, SCHEDULED_RECURRING, DRAFT, PUBLISH_PENDING, ADS_POST, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT} | SELF_EXPLANATORY |
| upload_phase enum {start, transfer, finish, cancel} | The phase during chunked upload. Using during chunked upload . |
| upload_session_id numeric string or integer | The session ID of this chunked upload. Using during chunked upload . |
| video_file_chunk string | The chunk of the video, between start_offset and end_offset . Using during chunked upload . |


### Return Type

 Struct  {`id`: numeric string, `upload_session_id`: numeric string, `video_id`: numeric string, `start_offset`: numeric string, `end_offset`: numeric string, `success`: bool, `skip_upload`: bool, `upload_domain`: string, `region_hint`: string, `xpv_asset_id`: numeric string, `is_xpv_single_prod`: bool, `transcode_bit_rate_bps`: numeric string, `transcode_dimension`: numeric string, `should_expand_to_transcode_dimension`: bool, `action_id`: string, `gop_size_seconds`: numeric string, `target_video_codec`: string, `target_hdr`: string, `maximum_frame_rate`: numeric string, }

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 222 | Video not visible |
| 389 | Unable to fetch video file from URL. |
| 190 | Invalid OAuth 2.0 Access Token |
| 352 | The video file you selected is in a format that we don't support. |
| 6001 | There was a problem uploading your video. Please try again. |
| 382 | The video file you tried to upload is too small. Please try again with a larger file. |
| 351 | There was a problem with your video file. Please try again with another file, |
| 6000 | There was a problem uploading your video file. Please try again with another file. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#)

## Deleting

You can dissociate a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) from an [AdAccount](https://developers.facebook.com/docs/graph-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/advideos`](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/).

### Parameters


| Parameter | Description |
| --- | --- |
| video_id video ID | Ad account library video ID Required |


### Return Type

 Struct  {`success`: bool, }

### Error Codes


| Error | Description |
| --- | --- |
| 613 | Calls to this api have exceeded the rate limit. |
| 100 | Invalid parameter |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#)On This Page[Ad Videos](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#Creating)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#parameters-2)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#return-type)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#error-codes-2)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#Deleting)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#parameters-3)[Return Type](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#return-type-2)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/advideos/#error-codes-3) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6FzxdpkflEvXPD7NPkrS_xzIMdEqgDlL7-pvpChTs1qVX2rjynNkuXD4e_vQ_aem_1oitSjal-8QhJpladFA10Q&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4vzCpf7xrvDd3QmD6kQrv9E1ViQM0acrB8nP7UTa0cPWrRUIupvpTUTUUx1A_aem_nYb3wjpWXNUqMm8dBZmcGQ&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4vzCpf7xrvDd3QmD6kQrv9E1ViQM0acrB8nP7UTa0cPWrRUIupvpTUTUUx1A_aem_nYb3wjpWXNUqMm8dBZmcGQ&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qsz8aLHY9KayERe5IIj1CQvWlfV5MGhKVrn-YVnWLilfV56eRj0HZyATb0Q_aem_1YTyXzPb7_gmxECN308PYg&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6QSpWyLVb2J-fBMnCemDJ6e-wh3t27LASMoC3BSEVJjSV-dyfCDXO63H7Grg_aem_sUxueJdvwwjwB9d8rLafVw&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR47eFoznOajU0IdLLNlJI3d_K1tgwfgvDI0QKq4SA0fM8YW5F-Q8pIMoKfqXg_aem_65VnAWQ2s6QZQJHe9rz3Ew&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5EdL6BZshpE-ygTvWgj2MZfxbCdWQS_Gf6eL4VMVN-fCLMkGg4bHZUKQVGtg_aem_zjY1Bk7KqElIlYSvNDsbcw&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4zZDxr5y2VVr2mty7OgAu7gMOvR6_S8utyDR4rRx1BbgqTy60MYIs4hoxFeA_aem_-K5UxrnmfrzzHwo0fdE9CA&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qsz8aLHY9KayERe5IIj1CQvWlfV5MGhKVrn-YVnWLilfV56eRj0HZyATb0Q_aem_1YTyXzPb7_gmxECN308PYg&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6QSpWyLVb2J-fBMnCemDJ6e-wh3t27LASMoC3BSEVJjSV-dyfCDXO63H7Grg_aem_sUxueJdvwwjwB9d8rLafVw&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR47eFoznOajU0IdLLNlJI3d_K1tgwfgvDI0QKq4SA0fM8YW5F-Q8pIMoKfqXg_aem_65VnAWQ2s6QZQJHe9rz3Ew&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5EdL6BZshpE-ygTvWgj2MZfxbCdWQS_Gf6eL4VMVN-fCLMkGg4bHZUKQVGtg_aem_zjY1Bk7KqElIlYSvNDsbcw&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4zZDxr5y2VVr2mty7OgAu7gMOvR6_S8utyDR4rRx1BbgqTy60MYIs4hoxFeA_aem_-K5UxrnmfrzzHwo0fdE9CA&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qsz8aLHY9KayERe5IIj1CQvWlfV5MGhKVrn-YVnWLilfV56eRj0HZyATb0Q_aem_1YTyXzPb7_gmxECN308PYg&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6qsz8aLHY9KayERe5IIj1CQvWlfV5MGhKVrn-YVnWLilfV56eRj0HZyATb0Q_aem_1YTyXzPb7_gmxECN308PYg&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4zZDxr5y2VVr2mty7OgAu7gMOvR6_S8utyDR4rRx1BbgqTy60MYIs4hoxFeA_aem_-K5UxrnmfrzzHwo0fdE9CA&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6HmPY84tVz4wrSjwWG6ZdWK-GQdskTOMXnlXWqJ-kHqw-fiHmvMCjNVDPVjg_aem_KIVEmHMNkksrdyxrL6mwIg&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5EdL6BZshpE-ygTvWgj2MZfxbCdWQS_Gf6eL4VMVN-fCLMkGg4bHZUKQVGtg_aem_zjY1Bk7KqElIlYSvNDsbcw&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4vzCpf7xrvDd3QmD6kQrv9E1ViQM0acrB8nP7UTa0cPWrRUIupvpTUTUUx1A_aem_nYb3wjpWXNUqMm8dBZmcGQ&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6FzxdpkflEvXPD7NPkrS_xzIMdEqgDlL7-pvpChTs1qVX2rjynNkuXD4e_vQ_aem_1oitSjal-8QhJpladFA10Q&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4srj0jdFJ9o21dyTsqwyuZ7NYGQBdHUEq2BMjJutNAG-HnCQaqtYToAYY_yy2qGJy1vn3PCenfEZravk0Z3BPUFh1aguJ1cSc56zynIjoi_rsGVx5vxiTJ4n1hqvGAaHKffB-u3-eWeiM7tz_KYdxX4UQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo