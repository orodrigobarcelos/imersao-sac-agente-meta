<!-- Fonte: Using the API _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/conversions-api/using-the-api -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Using the API

Updated: Feb 6, 2026Once you have completed the prerequisites on the [Get Started](https://developers.facebook.com/documentation/ads-commerce/conversions-api/get-started) page, use this page to learn how to send events and use the Test Events tool. Once you’ve sent an event, [verify your setup](https://developers.facebook.com/documentation/ads-commerce/conversions-api/verifying-setup).The Conversions API is based on Facebook’s [Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api), which was built on top of our [Graph API](https://developers.facebook.com/docs/graph-api). Marketing and Graph APIs have different version deprecation schedules. Our release cycle is aligned with the [Graph API](https://developers.facebook.com/docs/graph-api/changelog), so every version is supported for at least two years. This exception is only valid for the Conversions API.[Conversions API: Overview](https://developers.facebook.com/documentation/ads-commerce/conversions-api)[Parameters](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters)

Web, app, and physical store events shared using the Conversions API require specific parameters. By using the Conversions API, you agree that the [`action_source`](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/server-event#action-source) parameter is accurate to the best of your knowledge. The list of [required parameters is available here](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters).

## Send Requests

To send new events, make a `POST` request to this API’s `/events` edge from this path: `https://graph.facebook.com/{API_VERSION}/{PIXEL_ID}/events?access_token={TOKEN}`. When you post to this edge, Facebook creates new server events.
```
curl -X POST \
  -F 'data=[
       {
         "event_name": "Purchase",
         "event_time": 1762902353,
         "user_data": {
           "em": [
             "309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"
           ],
           "ph": [
             "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4",
             "6f4fcb9deaeadc8f9746ae76d97ce1239e98b404efe5da3ee0b7149740f89ad6"
           ],
           "client_ip_address": "123.123.123.123",
           "client_user_agent": "$CLIENT_USER_AGENT",
           "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
           "fbp": "fb.1.1558571054389.1098115397"
         },
         "custom_data": {
           "currency": "usd",
           "value": 123.45,
           "contents": [
             {
               "id": "product123",
               "quantity": 1,
               "delivery_category": "home_delivery"
             }
           ]
         },
         "event_source_url": "http://jaspers-market.com/product/123",
         "action_source": "website"
       }
     ]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<PIXEL_ID>/events
```
Attach your generated secure access token using the `access_token` query parameter to the request. You can also use [Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=%7BPIXEL_ID%7D%2Fevents%2F&version=v3.2) to `POST` to the `/<pixel_id>/events` endpoint.An example request body looks like this:
```
{
   "data": [
      {
         "event_name": "Purchase",
         "event_time": 1633552688,
         "event_id": "event.id.123",
         "event_source_url": "http:\/\/jaspers-market.com\/product\/123",
         "action_source": "website",
         "user_data": {
            "client_ip_address": "192.19.9.9",
            "client_user_agent": "test ua",
            "em": [
               "309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd"
            ],
            "ph": [
               "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4",
               "6f4fcb9deaeadc8f9746ae76d97ce1239e98b404efe5da3ee0b7149740f89ad6"
            ],
            "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
            "fbp": "fb.1.1558571054389.1098115397"
         },
         "custom_data": {
            "value": 100.2,
            "currency": "USD",
            "content_ids": [
               "product.id.123"
            ],
            "content_type": "product"
         },
         "opt_out": false
      },
      {
         "event_name": "Purchase",
         "event_time": 1633552688,
         "user_data": {
            "client_ip_address": "192.88.9.9",
            "client_user_agent": "test ua2"
         },
         "custom_data": {
            "value": 50.5,
            "currency": "USD"
         },
         "opt_out": false
      }
   ]
}
```


### Upload Time versus Event Transaction Time

[`event_time`](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/server-event#event-time) is the event transaction time. It should be sent as a Unix timestamp in seconds indicating when the actual event occurred. The specified time **may be earlier than the time you send the event to Facebook**. This is to enable batch processing and server performance optimization.The [`event_time`](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/server-event#event-time) can be up to 7 days before you send an event to Meta. If any `event_time` in `data` is greater than 7 days in the past, we return an error for the entire request and process no events. For offline and physical store events with `physical_store` as `action_source`, you should upload transactions within 62 days of the conversion.By using the Conversions API, you agree that the [`action_source`](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/server-event#action-source) parameter is accurate to the best of your knowledge.

### Batch Requests

You can send up to 1,000 events in `data`. However, for optimal performance, we recommend you send events as soon as they occur and ideally within an hour of the event occurring. **If any event you send in a batch is invalid, we reject the entire batch.**

### Hashing

Please check our [customer information parameters](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/customer-information-parameters) page to see which parameters should be hashed before they are sent to Facebook. If you are using one of our [Business SDKs](https://developers.facebook.com/docs/business-sdk), the hashing is done for you by the SDK.

### [Business SDK Features for Conversions API](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/business-sdk-features)

Learn more about three specific Business SDK features designed especially for Conversions API users: [Asynchronous Requests](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/business-sdk-features#asynchronous-requests), [Concurrent Batching](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/business-sdk-features#concurrent-batching), and [HTTP Service Interface](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/business-sdk-features#http-service-interface). Minimum language version required to use these features:

- PHP >= 7.2
- Node.js >= 7.6.0
- Java >= 8
- Python >= 2.7
- Ruby >= 2
Business SDK support for PHP 5 has been deprecated since January 2019. Please upgrade to PHP 7 to use the Business SDK.[Conversions API Parameters](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters)

## Verify Events

After you send your events, confirm that we have received them in [Events Manager⁠](https://www.facebook.com/events_manager2/list):

- On the **Data Sources** page, click on the Pixel corresponding to the `PIXEL_ID` in your `POST` request. For more information see [Business Help Center: Navigate Events Manager⁠](https://www.facebook.com/business/help/898185560232180).
- Then, click **Overview**. You see the number of raw, matched and attributed events we received. Under **Connection Method**, you see the channel in which that event was sent.


- You can click on each event to get more specific information.


- After you start sending events, you should be able to verify them within 20 minutes. Now you can start sending events from your server.


## Test Events Tool

You can verify that your server events are received correctly by Facebook by using the Test Events feature in Events Manager. To find the tool, go to `Events Manager > Data Sources > Your Pixel > Test Events`.The Test Events tool generates a test ID. Send the test ID as a `test_event_code` parameter to start seeing event activity appear in the Test Events window.**Note**: The `test_event_code` field should be used only for testing. You need to remove it when sending your production payload.Events sent with `test_event_code` are not dropped. They flow into Events Manager and are used for targeting and ads measurement purposes.Here’s an example of how the request should be structured:
```
{   "data": [      {         "event_name": "ViewContent",         "event_time": 1764975551,         "event_id": "event.id.123",         "event_source_url": "http:\/\/jaspers-market.com",         "user_data": {            "client_ip_address": "1.2.3.4",            "client_user_agent": "test user agent"         }      }   ],   "test_event_code": "TEST123"}
```


Here’s an example of how the request appears in Graph API Explorer:You can generate this test payload using the [**Payload Helper tool**](https://developers.facebook.com/documentation/ads-commerce/conversions-api/payload-helper). Please note that the test event code is only for testing payload.Your server events appear in the Test Events window once the request is sent.


## [Data Processing Options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/data-processing-options) for US Users

For these two APIs, implement data processing options by adding `data_processing_options`, `data_processing_options_country`, and `data_processing_options_state` inside each event within the [data parameter](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/main-body#data) of your events.**Note:** The App Events and Offline Conversions APIs are no longer recommended for new integrations. Instead, it is recommended that you use the Conversions API as it now supports web, app, and offline events. See [Conversions API for App Events](https://developers.facebook.com/documentation/ads-commerce/conversions-api/app-events) and [Conversions API for Offline Events](https://developers.facebook.com/documentation/ads-commerce/conversions-api/offline-events) for more information.To explicitly not enable Limited Data Use (LDU), specify an empty array for each event or simply remove the field in the payload:
```
{
    "data": [
        {
            "event_name": "Purchase",
            "event_time": <EVENT_TIME>,
            "user_data": {
                "em": "<EMAIL>"
            },
            "custom_data": {
                "currency": "<CURRENCY>",
                "value": "<VALUE>"
            },
            "data_processing_options": []
        }
    ]
}
```
To enable LDU and have Meta perform geolocation:
```
{
    "data": [
        {
            "event_name": "Purchase",
            "event_time": <EVENT_TIME>,
            "user_data": {
                "em": "<EMAIL>",
                "client_ip_address": "256.256.256.256"
            },
            "custom_data": {
                "currency": "<CURRENCY>",
                "value": "<VALUE>"
            },
            "data_processing_options": ["LDU"],
            "data_processing_options_country": 0,
            "data_processing_options_state": 0
        }
    ]
}
```
To enable LDU and manually specify the location, e.g., for California:
```
{
    "data": [
        {
            "event_name": "Purchase",
            "event_time": <EVENT_TIME>,
            "user_data": {
                "em": "<EMAIL>"
            },
            "custom_data": {
                "currency": "<CURRENCY>",
                "value": "<VALUE>"
            },
            "data_processing_options": ["LDU"],
            "data_processing_options_country": 1,
            "data_processing_options_state": 1000
        }
    ]
}
```


#### Manual Upload UI

The Offline Conversions API offers the option to manually upload your events from a `.csv` file. In this case, add Data Processing Options, Data Processing Country, and Data Processing State as columns inside your file. More information about this can be found in the upload user interface.

Learn more about [Data Processing Options](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/data-processing-options).

## API Limits

The Marketing API has its own rate-limiting logic and is excluded from all the [Graph API rate limitations](https://developers.facebook.com/docs/graph-api/overview/rate-limiting). So if you make a Marketing API call, it won’t be calculated into the Graph API throttling.There is no specific rate limit for the Conversions API. Conversions API calls are counted as Marketing API calls. The only limitation is that you can send us up to 1,000 events at a time. See [Send Requests](https://developers.facebook.com/documentation/ads-commerce/conversions-api/using-the-api#send) for more information.[Marketing API Rate Limiting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/rate-limiting)

## Business SDK API Usage in the Conversions API Gateway

This guide helps you navigate Meta Business SDK advanced features designed especially for Conversions API Gateway users. For basic Conversions API Gateway usage, refer to the [Conversions API Gateway documentation](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/gateway).

### Send Events to Your Conversions API Gateway Instance


#### Requirements

Before using any of the features listed below, you need to have the Meta Business SDK installed. See [Get Started with the Meta Business SDK](https://developers.facebook.com/docs/business-sdk/getting-started) or follow the README instructions listed here:

- PHP: [facebook-php-business-sdk⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-php-business-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6CDiQwiM03vpuCpL4wI_IfscquUrMfrsogG1fKx1uQPNN-6PHzEQMeDbXU5w_aem_OOp3RQAVy3_8Z6UiSttI6g&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)
- Node.js: [facebook-nodejs-business-sdk⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-nodejs-business-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4EGc6zDJlEsfr5JoiQaA1HJtbyJIMrBDyoPmbDziIBn5aUN70L3XXhjbo13Q_aem_cntVQB9haBnLLdrwZv41cA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)
- Java: [facebook-java-business-sdk⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-java-business-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)
- Python: [facebook-python-business-sdk⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-python-business-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)
- Ruby: [facebook-ruby-business-sdk⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ruby-business-sdk%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)
Currently, these features are only available on the PHP and Java business SDK. The other languages will be implemented by the end of 2023.The minimum language version required to use these features are:PHP >= 7.2Java >= 8**Note**: To dedupe events to the Conversions API endpoint, please pass the `eventId` in your request. This will help prevent duplicate events from showing up if Conversions API publishing is enabled.

### Formatting the `CAPIGatewayIngressRequest` Parameters


| Parameter | Description |
| --- | --- |
| endpointUrl string | The Conversions API Gateway endpoint that events get sent to. No prevalidation will be done on the parameter other than checking if it is a valid url. Example: https://test.example.com |
| accessKey string | Conversions API Gateway access key that is needed to send events to the Conversions API Gateway events endpoint. These are the instructions for generating it. |


### The `CAPIGatewayIngressRequest` Setters


| Parameter | Description |
| --- | --- |
| setSendToDestinationOnly Boolean | Boolean flag on whether the events get sent to the selected endpoint only. Default: False |
| setFilter CustomEndpointRequest.Filter() function | Filter function that processes each event. If the filtering logic returns true, the event gets passed through. Otherwise, the event gets dropped. You have to implement the shouldSendEvent function in the interface that has the parameter Event. Default: Null |


#### Migration Example: PHP

For systems that already use the Business SDK, you just need to reference the new CAPIGatewayIngressRequest and attach it to the eventRequest’s customEndpoint object.
```
// this is the standard event request that we attach events to
$event_request = new EventRequest($this->pixel_id);
$capiIngressRequest = new CAPIGatewayIngressRequest($this->cb_url, $this->access_key);
$event_request->setCustomEndpoint($capiIngressRequest);
// pass the events to this event Request object
$event_request->setEvents($events);
$event_request->execute()
```


#### Migration Example: Java

For systems that already use the Business SDK, you just need to reference the new CAPIGatewayIngressRequest and attach it to the eventRequest’s customEndpoint object.
```
// this is the standard event request that we attach events to

EventRequest eventRequest = new EventRequest(PIXEL_ID, context);

CAPIGatewayIngressRequest capiSyncRequest = new CAPIGatewayIngressRequest(CB_URL, CAPIG_ACCESS_KEY);
eventRequest.setCustomEndpoint(capiSyncRequest);
eventRequest.addDataItem(testEvent);
eventRequest.execute();
```


### Synchronous option


#### PHP Code Example


```
$api = Api::init(null, null, $this->access_token);
$api->setLogger(new CurlLogger());
$event_request = new EventRequest($this->pixel_id);
$capiIngressRequest = new CAPIGatewayIngressRequest($this->cb_url, $this->access_key);
$event_request->setCustomEndpoint($capiIngressRequest);
$user_data = (new UserData())
   ->setEmails(array('joe@eg.com'))
   ->setPhones(array('12345678901', '14251234567'))
   ->setFbc('fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890')
   ->setFbp('fb.1.1558571054389.1098115397');
$event1 = (new Event())
   ->setEventName('Purchase')
   ->setEventId('125')
   ->setEventTime(time())
   ->setEventSourceUrl('http://jaspers-market.com/product/123')
   ->setUserData($user_data);
$events = array($event1, $event2);
$event_request->setEvents($events);
$response = $event_request->execute();
print($response->__toString());
```


#### Java Code Example


```
EventRequest eventRequest = new EventRequest(PIXEL_ID, context);
UserData userData = new UserData()
       .email("abc@eg.com");
CAPIGatewayIngressRequest capiSyncRequest = new CAPIGatewayIngressRequest(CB_URL, CAPIG_ACCESS_KEY);
eventRequest.setCustomEndpoint(capiSyncRequest);
Event testEvent = new Event();
testEvent.eventId("125").eventName("Purchase")
       .eventTime(System.currentTimeMillis() / 1000L)
       .userData(userData)
       .dataProcessingOptions(new String[]{}).setEventId("134423232");
eventRequest.namespaceId("11")
       .uploadId("22222")
       .uploadTag("upload-tag-4")
       .uploadSource("upload-source-4")
       .testEventCode("test-event-code-5")
       .partnerAgent("partner-agent-6");
eventRequest.addDataItem(testEvent);
eventRequest.execute();
```


### Asynchronous option


#### PHP Code Example


```
$api = Api::init(null, null, $this->access_token);
$api->setLogger(new CurlLogger());
$event_request = new EventRequestAsync($this->pixel_id);
$capiIngressRequest = new CAPIGatewayIngressRequest($this->cb_url, $this->access_key);
$capiIngressRequest->setSendToDestinationOnly(true);
$event_request->setCustomEndpoint($capiIngressRequest);
$event1 = (new Event())
   ->setEventName('test Async Event')
   ->setEventId('134423232')
   ->setEventTime(time())
   ->setEventSourceUrl('http://jaspers-market.com/product/123');
$events = array($event1, $event2);
$event_request->setEvents($events);
$response = $event_request->execute()->wait();
```


#### Java Code Example


```
EventRequest eventRequest = new EventRequest(PIXEL_ID, context);
UserData userData = new UserData()
       .email("abc@eg.com");
CAPIGatewayIngressRequest capiSyncRequest = new CAPIGatewayIngressRequest(CB_URL, CAPIG_ACCESS_KEY);
capiSyncRequest.setSendToDestinationOnly(true);
eventRequest.setCustomEndpoint(capiSyncRequest);
Event testEvent = new Event();
testEvent.eventName("test Async Event")
       .eventTime(System.currentTimeMillis() / 1000L)
       .userData(userData)
       .dataProcessingOptions(new String[]{}).setEventId("134423232");
eventRequest.namespaceId("11222")
       .uploadId("22222")
       .uploadTag("upload-tag-4")
       .uploadSource("upload-source-4")
       .testEventCode("test-event-code-5")
       .partnerAgent("partner-agent-6");
eventRequest.addDataItem(testEvent);
eventRequest.executeAsync();
```


### Filter Functionality


#### PHP Code Example


```
lass APIFilter implements Filter {
   public function shouldSendEvent(Event $event): bool
   {
       if ($event->getEventId() === '125') {
           return false;
       }
       return true;
   }
}
$capiIngressRequest = new CAPIGatewayIngressRequest($this->cb_url, $this->access_key);
$event_request->setCustomEndpoint($capiIngressRequest);
$capiIngressRequest->setFilter(new APIFilter());
```


#### Java Code Example


```
CAPIGatewayIngressRequest capiSyncRequest = new CAPIGatewayIngressRequest(CB_URL, CAPIG_ACCESS_KEY);
eventRequest.setCustomEndpoint(capiSyncRequest);

capiSyncRequest.setFilter(new CustomEndpointRequest.Filter() {
   @Override
   public boolean shouldSendEvent(Event event) {
   if (event.getEventId().equals("125")) {
       return true;
   }
   return false;
}
});
```


## Learn More


- [Conversions API Gateway](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/gateway)
- [Conversions API Gateway for Multiple Accounts](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/gateway-multiple-accounts)
- [Conversions API Parameters](https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters)
- [Best Practices](https://developers.facebook.com/documentation/ads-commerce/conversions-api/best-practices)
Did you find this page helpful?ON THIS PAGESend RequestsUpload Time versus Event Transaction TimeBatch RequestsHashingBusiness SDK Features for Conversions APIVerify EventsTest Events ToolData Processing Options for US UsersManual Upload UIAPI LimitsBusiness SDK API Usage in the Conversions API GatewaySend Events to Your Conversions API Gateway InstanceRequirementsFormatting the CAPIGatewayIngressRequest ParametersThe CAPIGatewayIngressRequest SettersMigration Example: PHPMigration Example: JavaSynchronous optionPHP Code ExampleJava Code ExampleAsynchronous optionPHP Code ExampleJava Code ExampleFilter FunctionalityPHP Code ExampleJava Code ExampleLearn More$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$