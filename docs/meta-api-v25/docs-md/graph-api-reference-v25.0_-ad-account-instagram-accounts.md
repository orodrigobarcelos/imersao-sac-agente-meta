<!-- Fonte: Graph API Reference v25.0_ Ad Account Instagram Accounts.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Instagram Accounts

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#)

## Reading


Retrieve instagram accounts associated with this Ad Account


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Finstagram_accounts&version=v25.0)
```
GET /v25.0/{ad-account-id}/instagram_accounts HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/instagram_accounts',
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
    "/{ad-account-id}/instagram_accounts",
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
    "/{ad-account-id}/instagram_accounts",
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
                               initWithGraphPath:@"/{ad-account-id}/instagram_accounts"
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

This endpoint doesn't have any parameters.

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

A list of [IGUser](https://developers.facebook.com/docs/graph-api/reference/shadow-ig-user/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`


Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).


| Field | Description |
| --- | --- |
| total_count int32 | Total number of objects on this edge Default |


### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80002 | There have been too many calls to this Instagram account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 2635 | You are calling a deprecated version of the Ads API. Please update to the latest version. |
| 100 | Invalid parameter |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#)On This Page[Ad Account Instagram Accounts](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/instagram_accounts/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77Oly61wj59Jy7z9Fhady-kdR915nHkT4k1F4sBX1MOENtsabH0xXdPAlKNQ_aem_4aGnl47wXQSIC8DEPc9ZRQ&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iN5QjhWZ2BViuVcMnK483Lu5aoZuMSgJ62uGG71xrPeEpjVWHtorjs00p7A_aem_Eyc37H_2KhtT9x_DPwJosw&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR60m9S5crUi33iIVMoyWdR2hAv7-vpuLbWko_jnvXlpbwfKxrei8b3Cn3K0Hg_aem_tISmjWbmASS7s0UwadQIVA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4VPQj9Ujr3E54D9AW1JOruVCohwRJozK1RE_wxhwrkgAvC-vfpiv9B4oAq_g_aem_NyjCGfUih2_QjTmi1uNs1w&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4E0g5J-eSMHopwI_TreZGx8YwEp0S7F9he2xq_vMDAKd-NEoPy98JgekGrpQ_aem_e4MBS0KTca9RBoEJByCUrw&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7E_mMZH1CX9cyKOfx0k_UO_fS2H7rcz0SJh9rYcGKdts45at0UL8gnR1_3kA_aem_YE6jSSLslCkH4q0GIyMpHA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4VPQj9Ujr3E54D9AW1JOruVCohwRJozK1RE_wxhwrkgAvC-vfpiv9B4oAq_g_aem_NyjCGfUih2_QjTmi1uNs1w&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4VPQj9Ujr3E54D9AW1JOruVCohwRJozK1RE_wxhwrkgAvC-vfpiv9B4oAq_g_aem_NyjCGfUih2_QjTmi1uNs1w&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4E0g5J-eSMHopwI_TreZGx8YwEp0S7F9he2xq_vMDAKd-NEoPy98JgekGrpQ_aem_e4MBS0KTca9RBoEJByCUrw&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7yKllQ4_hOPQDd-2d6xMi1MlIMIxWg-PW2gLooCGHHvUPkGbFM4Ngj3xTw3A_aem_RMH_MFdlbpmspC9DmNQu2Q&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4E0g5J-eSMHopwI_TreZGx8YwEp0S7F9he2xq_vMDAKd-NEoPy98JgekGrpQ_aem_e4MBS0KTca9RBoEJByCUrw&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7AVU1EyUP3obFWL_C37YS59J8T0hjufFuEhKUWnJQFMwBkGbGLeULuUblFcg_aem_c4avwGguUBwx-j1rs3O-HA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7AVU1EyUP3obFWL_C37YS59J8T0hjufFuEhKUWnJQFMwBkGbGLeULuUblFcg_aem_c4avwGguUBwx-j1rs3O-HA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4VPQj9Ujr3E54D9AW1JOruVCohwRJozK1RE_wxhwrkgAvC-vfpiv9B4oAq_g_aem_NyjCGfUih2_QjTmi1uNs1w&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7E_mMZH1CX9cyKOfx0k_UO_fS2H7rcz0SJh9rYcGKdts45at0UL8gnR1_3kA_aem_YE6jSSLslCkH4q0GIyMpHA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7E_mMZH1CX9cyKOfx0k_UO_fS2H7rcz0SJh9rYcGKdts45at0UL8gnR1_3kA_aem_YE6jSSLslCkH4q0GIyMpHA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7AVU1EyUP3obFWL_C37YS59J8T0hjufFuEhKUWnJQFMwBkGbGLeULuUblFcg_aem_c4avwGguUBwx-j1rs3O-HA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR60m9S5crUi33iIVMoyWdR2hAv7-vpuLbWko_jnvXlpbwfKxrei8b3Cn3K0Hg_aem_tISmjWbmASS7s0UwadQIVA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7AVU1EyUP3obFWL_C37YS59J8T0hjufFuEhKUWnJQFMwBkGbGLeULuUblFcg_aem_c4avwGguUBwx-j1rs3O-HA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7E_mMZH1CX9cyKOfx0k_UO_fS2H7rcz0SJh9rYcGKdts45at0UL8gnR1_3kA_aem_YE6jSSLslCkH4q0GIyMpHA&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT46IiAY3ggty0mlLEL9-k4xffa3NzYBH0UlRA0TiLPM91P-7C8qEL_W6litmZ0Fw-jrWOX3YC_zf6Ng0tk-EL3zMWN6AaNj02O9I-PmO2pP5cs7EbX1MsHP5KGvbXGtXtcGOUEBxrjMJhlKVl5oqpdgXyM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo