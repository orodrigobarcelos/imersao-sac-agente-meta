<!-- Fonte: Debug Requests - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/guides/debugging -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Debug Requests



## Graph API Debug Mode



When Debug Mode is enabled, Graph API response may contain additional fields that explain potential issues with the request.


To enable debug mode, use the `debug` query string parameter. For example:

```
curl -i -X GET \
  "https://graph.facebook.com/{user-id}
    ?fields=friends
    &debug=all
    &access_token={your-access-token}"
```

```
GraphRequest request = GraphRequest.newMeRequest(
  accessToken,
  new GraphRequest.GraphJSONObjectCallback() {
    @Override
    public void onCompleted(JSONObject object, GraphResponse response) {
      // Insert your code here
    }
});

Bundle parameters = new Bundle();
parameters.putString("fields", "friends");
parameters.putString("debug", "all");
request.setParameters(parameters);
request.executeAsync();
```

```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/{user-id}"
           parameters:@{ @"fields": @"friends",@"debug": @"all",}
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```

```
FB.api(
  '/{user-id}',
  'GET',
  {"fields":"friends","debug":"all"},
  function(response) {
      // Insert your code here
  }
);
```

```
try {
  // Returns a `FacebookFacebookResponse` object
  $response = $fb->get(
    '/{user-id}',
    '{access-token}'
  );
} catch(FacebookExceptionsFacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(FacebookExceptionsFacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
```


If `user_friends` permission was not granted, this produces the following response:

```
{
  "data": [
  ],
  "__debug__": {
    "messages": [
      {
        "message": "Field friends is only accessible on User object, if user_friends permission is granted by the user",
        "type": "warning"
      },
      {
        "link": "https://developers.facebook.com/docs/apps/changelog#v2_0",
        "message": "Only friends who have installed the app are returned in versions greater or equal to v2.0.",
        "type": "info"
      }
    ]
  }
}
```


The `debug` parameter value can be set to "all" or to a minimal requested severity level that corresponds to `type` of the message:


| Debug Param Value | What Will Be Returned |
| --- | --- |
| all | All available debug messages. |
| info | Debug messages with type info and warning . |
| warning | Only debug messages with type warning . |


Debug information, when available, is returned as a JSON object under the `__debug__` key in the `messages` array. Every element of this array is a JSON object that contains the following fields:


| Field | Datatype | Description |
| --- | --- | --- |
| message | String | The message. |
| type | String | The message severity. |
| link | String | [Optional] A URL pointing to related information. |


You can also use Debug Mode with [Graph API Explorer](https://developers.facebook.com/tools/explorer).


### Determining Version used by API Requests



When you're building an app and making Graph API requests, you might find it useful to determine what API version you're getting a response from. For example, if you're making calls without a version specified, the API version that responds may not be known to you.


The Graph API supplies a request header with any response called `facebook-api-version` that indicates the exact version of the API that generated the response. For example, a Graph API call that generates a request with v2.0 produces the following HTTP header:

```
facebook-api-version:v2.0
```


This `facebook-api-version` header allows you to determine whether API calls are being returned from the version that you expect.


### Debug Info for Reporting Bugs



When [reporting a bug](https://developers.facebook.com/bugs/) in the Graph API, we include some additional request headers to send with your bug report to help us pinpoint and reproduce your issue. These request headers are `X-FB-Debug`, `x-fb-rev`, and `X-FB-Trace-ID`.
 [○](https://developers.facebook.com/docs/graph-api/guides/debugging#)On This Page[Debug Requests](https://developers.facebook.com/docs/graph-api/guides/debugging#debug-requests)[Graph API Debug Mode](https://developers.facebook.com/docs/graph-api/guides/debugging#graphapidebugmode)[Determining Version used by API Requests](https://developers.facebook.com/docs/graph-api/guides/debugging#apiversiondebug)[Debug Info for Reporting Bugs](https://developers.facebook.com/docs/graph-api/guides/debugging#bugdebug) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Jd9km-6KKIOoEcfQKVZ6Q3da9lDlpXUCJ2lZeARlH9EEIhQyktySBDcWNtg_aem_2VP8YErLK1TLlXGm7fJTyA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Jd9km-6KKIOoEcfQKVZ6Q3da9lDlpXUCJ2lZeARlH9EEIhQyktySBDcWNtg_aem_2VP8YErLK1TLlXGm7fJTyA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5z-zwbZl9ZD4Xq7-qf6LpgoIgqk1ELNfIGqPR51Tu-XrovtCkknaFmCIDvTQ_aem_nYeRKKvBf0Q_zhbeOVWysQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4j1Tg0R2fyJUQUcO5aSYwSa9P7rTYEq9Dx0kiGpDPUwVqxtERhzz9aC7Qtpw_aem_aYCtYRDXliyxSDUwoclwwg&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5z-zwbZl9ZD4Xq7-qf6LpgoIgqk1ELNfIGqPR51Tu-XrovtCkknaFmCIDvTQ_aem_nYeRKKvBf0Q_zhbeOVWysQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Jd9km-6KKIOoEcfQKVZ6Q3da9lDlpXUCJ2lZeARlH9EEIhQyktySBDcWNtg_aem_2VP8YErLK1TLlXGm7fJTyA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5z-zwbZl9ZD4Xq7-qf6LpgoIgqk1ELNfIGqPR51Tu-XrovtCkknaFmCIDvTQ_aem_nYeRKKvBf0Q_zhbeOVWysQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4bkZyzHyZ6tYobxz1Q7ObxblYUSwrjl3Wj3Ydy5_ahqC65kkd7PrAZZVSNRQ_aem_3h13k9k97sCGCC2X3d809A&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5fp8UUh1Vm-wp8ZAysruQnPnJIl-jFvkfqpEmxTiYuyj2BvdLfjXefVv-8uA_aem_bxiSlfhn_f8oCyhoe7qh7w&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5z-zwbZl9ZD4Xq7-qf6LpgoIgqk1ELNfIGqPR51Tu-XrovtCkknaFmCIDvTQ_aem_nYeRKKvBf0Q_zhbeOVWysQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4EoE0fgxw6wMpYUKxDUoBoxKGosZq5m5eXJpHA9fiQ0TR_fF7t3n923vEsiw_aem_b4nv4Ejrf3HGLL-WtrDISA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4EoE0fgxw6wMpYUKxDUoBoxKGosZq5m5eXJpHA9fiQ0TR_fF7t3n923vEsiw_aem_b4nv4Ejrf3HGLL-WtrDISA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5fp8UUh1Vm-wp8ZAysruQnPnJIl-jFvkfqpEmxTiYuyj2BvdLfjXefVv-8uA_aem_bxiSlfhn_f8oCyhoe7qh7w&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4j1Tg0R2fyJUQUcO5aSYwSa9P7rTYEq9Dx0kiGpDPUwVqxtERhzz9aC7Qtpw_aem_aYCtYRDXliyxSDUwoclwwg&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4Jd9km-6KKIOoEcfQKVZ6Q3da9lDlpXUCJ2lZeARlH9EEIhQyktySBDcWNtg_aem_2VP8YErLK1TLlXGm7fJTyA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4j1Tg0R2fyJUQUcO5aSYwSa9P7rTYEq9Dx0kiGpDPUwVqxtERhzz9aC7Qtpw_aem_aYCtYRDXliyxSDUwoclwwg&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6cdq7qRTTKBpZqUq3iFVQH2wOd7AvO6N_OyrBD3DSHQjvY8qY1L0m95gmgCw_aem_MhmR1UHlFqumkiNcUkErzA&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74dfZN9tzx8TviBmenO4Vr5FKznkKPKRQ9_WKJYDzorX3VNQ1ai05HSii8GQ_aem_PlBKZc0oSVT8vxTdBmr46w&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5z-zwbZl9ZD4Xq7-qf6LpgoIgqk1ELNfIGqPR51Tu-XrovtCkknaFmCIDvTQ_aem_nYeRKKvBf0Q_zhbeOVWysQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Epg4tBvVxr3fCoL7cmmnodqUi0fHVI5AwDjRjj28CIEAhFVG54LwkDHakIQ_aem_l_HrkN6Ll7wIb2YqUxsAcQ&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5-pEulxXYfx6XTSE7stobiK1XhsuH2KS5aHp8UuHd-1eODg96Ap4tPGmHTQpjvkejRHFX1gf5g4_7LbMfoGSs2R0bT-F4cRf1FsnpyBv58vSCTsPUHV7aQ7ueOTuxZosoHoA_9Wi62yo1FXdRxbCjTBhY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo