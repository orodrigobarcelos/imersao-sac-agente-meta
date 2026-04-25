<!-- Fonte: Versioning - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/guides/versioning -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Platform Versioning



Facebook's Platform supports versioning so that app builders can roll out changes over time. This document explains how SDKs and APIs affected by versions and how to use those versions in your requests.


## Versioning



Not all APIs and SDKs share the same versioning system. For example, the Graph API is versioned with a different pace and numbering compared to the Facebook SDK for iOS. All Facebook SDKs support the ability to interact with different versions of our APIs. Multiple versions of APIs or SDKs can exist at the same time with different functionality in each version.


### What is the latest Graph API Version?



The latest Graph API version is `v25.0`


### Why do we have versions?



The goal for having versioning is for developers building apps to be able to understand in advance when an API or SDK might change. They help with web development, but are critical with mobile development because a person using your app on their phone may take a long time to upgrade (or may never upgrade).


Each version will remain for at least 2 years from release giving you a solid timeline for how long your app will remain working, and how long you have to update it to newer versions.


### Version Schedules



Each version is guaranteed to operate for at least two years. **A version will no longer be usable two years after the date that the subsequent version is released.** For example, if API version v2.3 is released on March 25th, 2015 and API version v2.4 is released August 7th, 2015 then v2.3 would expire on August 7th, 2017, two years after the release of v2.4.


For APIs, once a version is no longer usable, any calls made to it will be defaulted to the next oldest, usable version. Here is a timeline example:


For SDKs, a version will always remain available as it is a downloadable package. However, the SDK may rely upon APIs or methods which no longer work, so you should assume an end-of-life SDK is no longer functional.


You can find specific information about our version timelines, changes, and release dates on our [changelog page](https://developers.facebook.com/docs/graph-api/changelog).


### Will everything remain completely unchanged in a version?



Facebook does reserve the right to make changes in any API in a short period of time for issues related to security or privacy. These changes don't happen often, but they do happen.


### What happens if I don't specify a version for an API?



We refer to an API call made without specifying a version as an **unversioned** call. For example, let's say the current version is v4.0. The call is as follows:

```
curl -i -X "https://graph.facebook.com/v4.0/{my-user-id}&access_token={access-token}"
```


The same unversioned call is as follows:

```
curl -i -X "https://graph.facebook.com/{my-user-id}&access_token={access-token}"
```


An unversioned call uses the version set in the app dashboard **Upgrade API Version** card under **Settings > Advanced**. In following example, the version set in the app dashboard is v2.10 and the unversioned call is equivalent to:

```
curl -i -X "https://graph.facebook.com/v2.10/{my-user-id}&access_token={access-token}"
```


We recommend you always specify the version where possible.


#### Limitations



- You can not make unversioned API calls to the Facebook JavaScript SDK.


### Can my app make calls to versions older than the current version?



You can specify older versions in your API calls as long as they are available and your app has made calls to that version. For example, if your app was created after v2.0 was released and makes calls using v2.0, it will be able to make calls to v2.0 until the version expires even after newer versions have been released. If you created your app after v2.0 but did not make any calls until v2.2, your app will not be able to make calls using v2.0 or to v2.1. It will only be able to make calls using v2.2 and newer versions.


### Marketing API Versioning



The [Marketing API](https://developers.facebook.com/docs/marketing-apis) has its own versioning scheme. Both version numbers and their schedules are different from the Graph API's state of things.
 [Learn more about Marketing API Versioning](https://developers.facebook.com/docs/marketing-api/versions)[○](https://developers.facebook.com/docs/graph-api/guides/versioning#)

## Making Versioned Requests



### Graph API



Whether core or extended, almost all Graph API endpoints are available through a versioned path. We've a [full guide to using versions with the Graph API](https://developers.facebook.com/docs/graph-api/quickstart#versions) in our [Graph API quickstart guide](https://developers.facebook.com/docs/graph-api/quickstart).


### Dialogs



Versioned paths aren't just true for API endpoints, they're also true for dialogs and social plugins. For example, if you want to generate the Facebook Login dialog for a web app, you can prepend a version number to the endpoint that generates the dialog:

```
https://www.facebook.com/v25.0/dialog/oauth?
  client_id={app-id}
  &redirect_uri={redirect-uri}
```


### Social Plugins



If you're using the HTML5 or xfbml versions of [our social plugins](https://developers.facebook.com/docs/plugins/), the version rendered will be determined by the version specified when you're [initialising the JavaScript SDK](https://developers.facebook.com/docs/graph-api/guides/versioning#jssdk).


If you're inserting an iframe or plain link version of one of our plugins, you'd prepend the version number to the source path of the plugin:

```
<iframe
  src="//www.facebook.com/v25.0/plugins/like.php?href=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;width&amp;layout=standard&amp;action=like&amp;show_faces=true&amp;share=true&amp;height=80&amp;appId=634262946633418"
  scrolling="no"
  frameborder="0"
  style="border:none; overflow:hidden; height:80px;"
  allowTransparency="true">
</iframe>
```
[○](https://developers.facebook.com/docs/graph-api/guides/versioning#)

## Making Versioned Requests from SDKs



If you're using the Facebook SDK for iOS, Android or JavaScript, making versioning calls is largely automatic. Note that this is distinct from each SDKs own versioning system.


### JavaScript



The JavaScript SDK can only use different API versions if you're [using the `sdk.js` path](https://developers.facebook.com/docs/apps/changelog/#v2_0_js_sdk).


If you're using `FB.init()` from the [JavaScript SDK](https://developers.facebook.com/docs/javascript), you need to use the version parameter, like this:

```
FB.init({
  appId      : '{app-id}',
  version    : 'v25.0'
});
```


If you set the version flag in the init, then any calls to [`FB.api()`](https://developers.facebook.com/docs/javascript/reference/FB.api) will automatically have the version prepended to the path that's called. The same is true for any dialogs for Facebook Login that happen to get called. You will get the Facebook Login dialog for that version of the API.


If you need to, you can override a version by just prepending the version to the path of the endpoint in the `FB.api()` call.


### iOS



Each version of the Facebook SDK for iOS that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with [`[FBSDKGraphRequest initWithGraphPath]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequest/#initWithGraphPath:parameters:)). The API version is listed with the release of each version of the [Facebook SDK for iOS](https://developers.facebook.com/docs/ios).


Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for iOS. For example, if `v2.7` was the most recent version of the API, the call `/me/friends` - used in the following code sample - will actually call `/v2.7/me/friends`:

```
[[[FBSDKGraphRequest alloc] initWithGraphPath:@"me/friends"
  parameters:@{@"fields": @"cover,name,start_time"}]
    startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        (...)
    }];
```


You can override the version of the call with [`[FBSDKGraphRequestConnection overrideVersionPartWith]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequestConnection/#overrideVersionPartWith:).


### Android



Each version of the Facebook SDK for Android that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with `GraphRequest.setVersion()`). The API version is listed with the release of each version of the Facebook SDK for Android.


Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for Android. For example, if `v2.7` was the most recent version of the API, the call `/me` - used in the following code sample - will actually call `/v2.7/me`:

```
GraphRequest request = GraphRequest.newGraphPathRequest (
        accessToken,
        "/me/friends",
        new GraphRequest.GraphJSONObjectCallback() {
            @Override
            public void onCompleted(
                   JSONObject object,
                   GraphResponse response) {
                // Application code
            }
        });
Bundle parameters = new Bundle();
parameters.putString("fields", "id,name,link");
request.setParameters(parameters);
request.executeAsync();
```


You can override the version of the call with `GraphRequest.setVersion()`.
 [○](https://developers.facebook.com/docs/graph-api/guides/versioning#)[○](https://developers.facebook.com/docs/graph-api/guides/versioning#)On This Page[Platform Versioning](https://developers.facebook.com/docs/graph-api/guides/versioning#platform-versioning)[Versioning](https://developers.facebook.com/docs/graph-api/guides/versioning#versioning)[What is the latest Graph API Version?](https://developers.facebook.com/docs/graph-api/guides/versioning#latest)[Why do we have versions?](https://developers.facebook.com/docs/graph-api/guides/versioning#whyversion)[Version Schedules](https://developers.facebook.com/docs/graph-api/guides/versioning#howlong)[Will everything remain completely unchanged in a version?](https://developers.facebook.com/docs/graph-api/guides/versioning#stability)[What happens if I don't specify a version for an API?](https://developers.facebook.com/docs/graph-api/guides/versioning#unversioned_calls)[Can my app make calls to versions older than the current version?](https://developers.facebook.com/docs/graph-api/guides/versioning#calling_older_versions)[Marketing API Versioning](https://developers.facebook.com/docs/graph-api/guides/versioning#marketing-api)[Making Versioned Requests](https://developers.facebook.com/docs/graph-api/guides/versioning#calling_versioned_apis)[Graph API](https://developers.facebook.com/docs/graph-api/guides/versioning#graphapiversions)[Dialogs](https://developers.facebook.com/docs/graph-api/guides/versioning#dialogs)[Social Plugins](https://developers.facebook.com/docs/graph-api/guides/versioning#plugins)[Making Versioned Requests from SDKs](https://developers.facebook.com/docs/graph-api/guides/versioning#calling_from_supported_sdks)[JavaScript](https://developers.facebook.com/docs/graph-api/guides/versioning#jssdkcalls)[iOS](https://developers.facebook.com/docs/graph-api/guides/versioning#ioscalls)[Android](https://developers.facebook.com/docs/graph-api/guides/versioning#androidcalls) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4M9eNZe2ciKjjbAxFpq6wQUBNphupREs9aRwbvs2b0fIObDqoYYEye3jYyrQ_aem_VoL8rzLJbaNCxrQMlB2KhA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5DxnYTebxubqVC1h51OgynkaF5hYmzbN3KUTkQ-szSHjqpJZf89Fy1cEC-tA_aem_15JvNTy_KqwiQwkoHrTjDA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Mt77bUSSwY8snOKJ2Zsa1OY4hhDyNehb5Mczy5BoGOuGbeD7kzfQ2zz_-dQ_aem_6cJDSzptM_nJXiNdMcu3yg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5I3Jmq_rBUwspOw2gi1DfCuEXetGCQRZb80amFeyhXIIZV-lfIhHLGnZHPtA_aem_Jnk1WrsBqPzNKHwAqQiKsA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7_e48wlhAiKHYV870G-gjLL6bkHRc4o8PcgZMNWsoqkYegzTtUISEcd9FGjQ_aem_7RMptba_Hw7NUJ_krdbUCg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR45fJsRdJZV9Ax4AscLDZPt5bMYRVSpwRckCwcmFMuz0wMFhwVaO63jTfEKMA_aem_21OeCZZgq9WeNzgobc017w&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6Luy_9AAwj7WENwjuNReJ-S8Gj6CRC8y1TnlCirbGH55eXxW_8ZZe28-OLkA_aem_di-MblcAQRYtE6t_TwvRvA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7fIrDDObdSXa0p12EUy6TOFH9JAh1lsyUKpPcvTBi7-8C9KuSwAd-3ThFcbw_aem_FB7IVzqTXXCKb5CffSnKpA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4M9eNZe2ciKjjbAxFpq6wQUBNphupREs9aRwbvs2b0fIObDqoYYEye3jYyrQ_aem_VoL8rzLJbaNCxrQMlB2KhA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4i_VSNFoj0cbNgEEByjPqyks_9i1szwmXApikz30s1IL-7L4ylcjrOEiJUMw_aem_hSvW-PlfqpzAZC5wHzWZAQ&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Mt77bUSSwY8snOKJ2Zsa1OY4hhDyNehb5Mczy5BoGOuGbeD7kzfQ2zz_-dQ_aem_6cJDSzptM_nJXiNdMcu3yg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Mt77bUSSwY8snOKJ2Zsa1OY4hhDyNehb5Mczy5BoGOuGbeD7kzfQ2zz_-dQ_aem_6cJDSzptM_nJXiNdMcu3yg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Mt77bUSSwY8snOKJ2Zsa1OY4hhDyNehb5Mczy5BoGOuGbeD7kzfQ2zz_-dQ_aem_6cJDSzptM_nJXiNdMcu3yg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4i_VSNFoj0cbNgEEByjPqyks_9i1szwmXApikz30s1IL-7L4ylcjrOEiJUMw_aem_hSvW-PlfqpzAZC5wHzWZAQ&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4M9eNZe2ciKjjbAxFpq6wQUBNphupREs9aRwbvs2b0fIObDqoYYEye3jYyrQ_aem_VoL8rzLJbaNCxrQMlB2KhA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7wSTvHSkVZabsMUI1FJmY7-BZecqFXtAchItmSEYCa9WLP01jLsYv-m9SUBg_aem_hNXYSIhuOYCzn9t9xZ8VxQ&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7fIrDDObdSXa0p12EUy6TOFH9JAh1lsyUKpPcvTBi7-8C9KuSwAd-3ThFcbw_aem_FB7IVzqTXXCKb5CffSnKpA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5I3Jmq_rBUwspOw2gi1DfCuEXetGCQRZb80amFeyhXIIZV-lfIhHLGnZHPtA_aem_Jnk1WrsBqPzNKHwAqQiKsA&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7wSTvHSkVZabsMUI1FJmY7-BZecqFXtAchItmSEYCa9WLP01jLsYv-m9SUBg_aem_hNXYSIhuOYCzn9t9xZ8VxQ&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7Mt77bUSSwY8snOKJ2Zsa1OY4hhDyNehb5Mczy5BoGOuGbeD7kzfQ2zz_-dQ_aem_6cJDSzptM_nJXiNdMcu3yg&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT50NddQt_vuiJhzrvIBQlqMEiUQY_pdZ-YEBWguBzNcO4fEBlGxRxR6AFN0cBYNroeSnUcsct--RFqXnABsgcXPoYTEttKcc3R-U3pMXAI9icImfHafN4xm5ocFiGfbMIZXDEsUGZDDqhd0Ff4OZxQ_XKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo