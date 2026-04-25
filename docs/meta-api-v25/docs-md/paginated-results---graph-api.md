<!-- Fonte: Paginated Results - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/results -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Paginated Results



We cover the basics of Graph API terminology and structure in the [Graph API overview](https://developers.facebook.com/docs/graph-api/overview). This document goes into more detail about the results from your API requests.


## Traversing Paged Results



When making an API request to a node or edge, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.


### Cursor-based Pagination



Cursor-based pagination is the most efficient method of paging and should always be used when possible. A cursor refers to a random string of characters which marks a specific item in a list of data. The cursor will always point to the item, however it will be invalidated if the item is deleted or removed. Therefore, your app shouldn't store cursors or assume that they will be valid in the future.


When reading an edge that supports cursor pagination, you see the following JSON response:

```
{
  "data": [
     ... Endpoint data is here
  ],
  "paging": {
    "cursors": {
      "after": "MTAxNTExOTQ1MjAwNzI5NDE=",
      "before": "NDMyNzQyODI3OTQw"
    },
    "previous": "https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw"
    "next": "https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE="
  }
}
```


A cursor-paginated edge supports the following parameters:


- `before` : This is the cursor that points to the start of the page of data that has been returned.
- `after` : This is the cursor that points to the end of the page of data that has been returned.
- `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
- `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
- `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.


Don't store cursors. Cursors can quickly become invalid if items are added or deleted.


### Time-based Pagination



Time pagination is used to navigate through results data using Unix timestamps which point to specific times in a list of data.


When using an endpoint that uses time-based pagination, you see the following JSON response:

```
{
  "data": [
     ... Endpoint data is here
  ],
  "paging": {
    "previous": "https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754",
    "next": "https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774"
  }
}
```


A time-paginated edge supports the following parameters:


- `until` : A Unix timestamp or [`strtotime`](https://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php%3Ffbclid%3DIwZXh0bgNhZW0CMTEAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6XEZP1hy1ZoCHPy_fj9XLey8_6C85cmRFsQnTdXAIbevwlzMFPq5XJjfUYTg_aem_1gnPNDC5RklsUNkvHyWtIA&h=AT6ZJzBGhpmgcd1dFhavIMPDzlgEGrtSnDSQBOkNQMZEbX_nZ74JQodzysJ7c2BJvxZNMNi9DnLmeOCWFo4-jPN4Cng745ah7LYTxf60qB99Z2q0ERdXp7kAzlLjHofPPrKlws648D33ADjL9IUCQ0mSUHQ) data value that points to the end of the range of time-based data.
- `since` : A Unix timestamp or [`strtotime`](https://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php%3Ffbclid%3DIwZXh0bgNhZW0CMTEAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6XEZP1hy1ZoCHPy_fj9XLey8_6C85cmRFsQnTdXAIbevwlzMFPq5XJjfUYTg_aem_1gnPNDC5RklsUNkvHyWtIA&h=AT7u2Na84dPDOOKj6jsKFuEn8w7AtELpIdYDLDod210jM_RD1CHjlqQR8PFCIMo3HgL6pYDeqveX_BOa2j-YpYLlglLa-Z66-DE-XlaAf-jv6gK7pZPmYmtg-71MhYwC2tThFfnrXo2NTsZp5VKDFq64xos) data value that points to the start of the range of time-based data.
- `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
- `next` : The Graph API endpoint that will return the next page of data.
- `previous` : The Graph API endpoint that will return the previous page of data.


For consistent results, specify both `since` and `until` parameters. Also, it is recommended that the time difference is a maximum of 6 months.


### Offset-based Pagination



Offset pagination can be used when you do not care about chronology and just want a specific number of objects returned. Only use this if the edge does not support cursor or time-based pagination.


An offset-paginated edge supports the following parameters:


- `offset` : This offsets the start of each page by the number specified.
- `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
- `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
- `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.


Note that if new objects are added to the list of items being paged, the contents of each offset-based page will change.


Offset based pagination is not supported for all API calls. To get consistent results, we recommend you to paginate using the previous/next links we return in the response.


For objects that have many items returned, such as [comments](https://developers.facebook.com/docs/graph-api/reference/object/comments) which can number in the tens of thousands, you may encounter limits while paging. The API will return an error when your app has reached the cursor limit:

```
{
  "error": {
    "message": "(#100) The After Cursor specified exceeds the max limit supported by this endpoint",
    "type": "OAuthException",
    "code": 100
  }
}
```
[○](https://developers.facebook.com/docs/graph-api/results#)

## Next Steps



Now that you are more familiar with the Graph API visit our [Graph Explorer Tool Guide](https://developers.facebook.com/docs/graph-api/explorer) to explore the Graph without writing code, [Common Uses](https://developers.facebook.com/docs/graph-api/using-graph-api/common-scenarios) to view the most common tasks performed, and [the SDKs available](https://developers.facebook.com/docs/graph-api/using-graph-api/using-with-sdks).
 [○](https://developers.facebook.com/docs/graph-api/results#)[○](https://developers.facebook.com/docs/graph-api/results#)On This Page[Paginated Results](https://developers.facebook.com/docs/graph-api/results#paginated-results)[Traversing Paged Results](https://developers.facebook.com/docs/graph-api/results#paging)[Cursor-based Pagination](https://developers.facebook.com/docs/graph-api/results#cursors)[Time-based Pagination](https://developers.facebook.com/docs/graph-api/results#time)[Offset-based Pagination](https://developers.facebook.com/docs/graph-api/results#offset)[Next Steps](https://developers.facebook.com/docs/graph-api/results#next-steps) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7nDqQsIm5Mnxa9HEl6ahibJXj0aWqjOW_au4UTQiEzW6RDSBEiOs-n6I1ppA_aem_3ZDnk3ZJuerdG6uKnw0U9Q&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7gSEDKzbPOCXjtj2QGKkmYmqmtX3-J1DKPj7gqga9EVGKKYmiOtN7LgkAv2Q_aem_1htIAcMb5QkdRCIGAuHXQA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7qFaD67hmF-5i5_Tl5TDXtboFuUdSLtvXtPylUOzU260msR7JombebgiQ9ug_aem_HyrfrjvnX8gXDzVgmuhBvA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR766C8YJ40R0XvbRHFN5XStH6GKk9FaosF_g_TPhSLubCn4iM-TEXKxQcX7Bg_aem_e3tCLsKQTu7bM1epMXc1Fw&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6ZxNXsfiYOsOPGDpVz2weUEAXyb5xHaqvXOS-cPR4IQeCZo4uM58m8mJfjvA_aem_cf--Q9yzGHQEo5bj7hbPeg&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR766C8YJ40R0XvbRHFN5XStH6GKk9FaosF_g_TPhSLubCn4iM-TEXKxQcX7Bg_aem_e3tCLsKQTu7bM1epMXc1Fw&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR766C8YJ40R0XvbRHFN5XStH6GKk9FaosF_g_TPhSLubCn4iM-TEXKxQcX7Bg_aem_e3tCLsKQTu7bM1epMXc1Fw&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR766C8YJ40R0XvbRHFN5XStH6GKk9FaosF_g_TPhSLubCn4iM-TEXKxQcX7Bg_aem_e3tCLsKQTu7bM1epMXc1Fw&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7nDqQsIm5Mnxa9HEl6ahibJXj0aWqjOW_au4UTQiEzW6RDSBEiOs-n6I1ppA_aem_3ZDnk3ZJuerdG6uKnw0U9Q&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ykoBz9P5sq6Znb2b433dm1FomXRm4th6pKWTOp9fa5tfdIlncLCSSdFwviA_aem_bD8YAWh5aQ-itTbyafOX0A&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7gSEDKzbPOCXjtj2QGKkmYmqmtX3-J1DKPj7gqga9EVGKKYmiOtN7LgkAv2Q_aem_1htIAcMb5QkdRCIGAuHXQA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7qFaD67hmF-5i5_Tl5TDXtboFuUdSLtvXtPylUOzU260msR7JombebgiQ9ug_aem_HyrfrjvnX8gXDzVgmuhBvA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6ZxNXsfiYOsOPGDpVz2weUEAXyb5xHaqvXOS-cPR4IQeCZo4uM58m8mJfjvA_aem_cf--Q9yzGHQEo5bj7hbPeg&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5l8Dj5rurOth_ym_jgSSYrhxXRNWXCNvNeeX1UZHLol_yEJCXQAr8iyUl7-A_aem_lkJgPpNW2Gsv8cRoScs-ZQ&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6ZxNXsfiYOsOPGDpVz2weUEAXyb5xHaqvXOS-cPR4IQeCZo4uM58m8mJfjvA_aem_cf--Q9yzGHQEo5bj7hbPeg&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7gSEDKzbPOCXjtj2QGKkmYmqmtX3-J1DKPj7gqga9EVGKKYmiOtN7LgkAv2Q_aem_1htIAcMb5QkdRCIGAuHXQA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR766C8YJ40R0XvbRHFN5XStH6GKk9FaosF_g_TPhSLubCn4iM-TEXKxQcX7Bg_aem_e3tCLsKQTu7bM1epMXc1Fw&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7qFaD67hmF-5i5_Tl5TDXtboFuUdSLtvXtPylUOzU260msR7JombebgiQ9ug_aem_HyrfrjvnX8gXDzVgmuhBvA&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ykoBz9P5sq6Znb2b433dm1FomXRm4th6pKWTOp9fa5tfdIlncLCSSdFwviA_aem_bD8YAWh5aQ-itTbyafOX0A&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7JtA8h0NSzSRp4ymDu5sLaXGYDfj8R1bAkczsSII5XrShkurIGdjEuwQ_eLw_aem_yNQrxYkcNk9_mpXvmKeGSg&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5UW8HK-VPaZB4cnetb0DPmbMQAhjJLrUEb3d20bK3PnlKJCVpHp1c0zDdx9ZYcBbG52wT-Fz6irguV_KtjquhQuoIXJ6is_-atLxI6qOEjtzPtiEDkIXi9bU8_iyYrJpOIM1sOLv1aDIhfqPEe9h_RK5g)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo