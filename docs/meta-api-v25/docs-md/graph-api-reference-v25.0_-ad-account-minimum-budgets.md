<!-- Fonte: Graph API Reference v25.0_ Ad Account Minimum Budgets.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Ad Account Minimum Budgets

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#)

## Reading


The minimum daily budget value for an ad set in an Auction campaign, given the bid_amount if use manual bid


### Example

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bad-account-id%7D%2Fminimum_budgets&version=v25.0)
```
GET /v25.0/{ad-account-id}/minimum_budgets HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{ad-account-id}/minimum_budgets',
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
    "/{ad-account-id}/minimum_budgets",
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
    "/{ad-account-id}/minimum_budgets",
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
                               initWithGraphPath:@"/{ad-account-id}/minimum_budgets"
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
| bid_amount integer | Provide this value if you want to get values for manual bid. |


### Fields


Reading from this edge will return a JSON formatted result:

```
{
    "data": [],
    "paging": {}
}
```


#### `data`

A list of [MinimumBudget](https://developers.facebook.com/docs/marketing-api/reference/minimum-budget/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes


| Error | Description |
| --- | --- |
| 200 | Permissions error |

[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#)

## Creating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#)

## Updating

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#)

## Deleting

You can't perform this operation on this endpoint.[○](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#)On This Page[Ad Account Minimum Budgets](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#overview)[Reading](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#Reading)[Example](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#example)[Parameters](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#parameters)[Fields](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#fields)[Error Codes](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#error-codes)[Creating](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#Creating)[Updating](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#Updating)[Deleting](https://developers.facebook.com/docs/graph-api/reference/ad-account/minimum_budgets/#Deleting) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6CtJAIP48vbqfvxvrXGG1CnLXdf6OSp2mCDPVrxTGSTyhXGSccktlImulJVg_aem_mLLOlOw9b9TV0YFsnkUV3Q&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7IxmIjJs0C6_ntAUVcvxYMkVjMHvI9OV8o55raAntviPTc_1HlZJULMsFxJQ_aem_-e0r2C4I31999OvWfd6XiQ&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR73GUYechVlJEXEaeW_FsZsxoX6fDYjb-UKzXfANvbMuc2QXiUFP0SWaeokyQ_aem_203qgKn4WTquZ6rNG_kVWA&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4i4WjWWeF6he7Vwu129gY4eaSaLN5UMYDbsZlxj0rTJh0-TOU6cUQ0h43qTw_aem_hv_Oc1l74qmv70-lilG9dg&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5BqpvOusR74bLfrm494wpOLek5boRymEc0Zg9cnP-NnsxWl3bis2OHhRVjhw_aem_An3C_93nhHrD_L-yyotsUQ&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6CtJAIP48vbqfvxvrXGG1CnLXdf6OSp2mCDPVrxTGSTyhXGSccktlImulJVg_aem_mLLOlOw9b9TV0YFsnkUV3Q&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR73GUYechVlJEXEaeW_FsZsxoX6fDYjb-UKzXfANvbMuc2QXiUFP0SWaeokyQ_aem_203qgKn4WTquZ6rNG_kVWA&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5BqpvOusR74bLfrm494wpOLek5boRymEc0Zg9cnP-NnsxWl3bis2OHhRVjhw_aem_An3C_93nhHrD_L-yyotsUQ&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gcGJ3LKHTiV-phTU__NiffRxrs9MtDOILny15msQy-0YCcBGzHpgc1uFVWw_aem_PrTFodGwdFmR7VSaa7lKLg&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5HW9Gl5OulzADboRsDhoWttxeuqwPM6t2N04uqi9DlVuj_5zMwN1b3Y_YVdQ_aem_HHESE4GTts15R9iZxf9WEg&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rhqY1q-L5ftvmbryqnnEB5kV_aCFscDoLC7XHgqxeV6HR3ZeUAOkV-VgfWg_aem_14RqkUmbfGofHKKMJ67Rnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7guNslls9oOR36wWAYRVB6BA1YkytlXCqQNDmnbt_90WBwlgSINzV1xl12eg_aem_QswJlYi8wqTHiuojGqvgnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rhqY1q-L5ftvmbryqnnEB5kV_aCFscDoLC7XHgqxeV6HR3ZeUAOkV-VgfWg_aem_14RqkUmbfGofHKKMJ67Rnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rhqY1q-L5ftvmbryqnnEB5kV_aCFscDoLC7XHgqxeV6HR3ZeUAOkV-VgfWg_aem_14RqkUmbfGofHKKMJ67Rnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7IxmIjJs0C6_ntAUVcvxYMkVjMHvI9OV8o55raAntviPTc_1HlZJULMsFxJQ_aem_-e0r2C4I31999OvWfd6XiQ&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5k8baZvIkN9i6vQs6prXmineboGusX0esGO1kep0UKuBdDNCoKWXB-WaZNHw_aem_MfjuIBppJKkFv8tmLnGwCw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5BqpvOusR74bLfrm494wpOLek5boRymEc0Zg9cnP-NnsxWl3bis2OHhRVjhw_aem_An3C_93nhHrD_L-yyotsUQ&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rhqY1q-L5ftvmbryqnnEB5kV_aCFscDoLC7XHgqxeV6HR3ZeUAOkV-VgfWg_aem_14RqkUmbfGofHKKMJ67Rnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5HW9Gl5OulzADboRsDhoWttxeuqwPM6t2N04uqi9DlVuj_5zMwN1b3Y_YVdQ_aem_HHESE4GTts15R9iZxf9WEg&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4rhqY1q-L5ftvmbryqnnEB5kV_aCFscDoLC7XHgqxeV6HR3ZeUAOkV-VgfWg_aem_14RqkUmbfGofHKKMJ67Rnw&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7NrgSqT80Z-7GVfN38GncEp3KD9kqlHHjcSXk0_3xEbRfiAs5gR-kzFP9ch8kpFdSl5qiBsHXJcY5RG3DYp7faY2iWzPm5o4Dyznky6pPzrl6UWlTGX93BWXC9vwmmzQiFrP2ufljctuBW4hUFLOg4sHY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo