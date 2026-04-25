<!-- Fonte: Customer File Custom Audiences _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Customer File Custom Audiences

Updated: Feb 5, 2026Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences that may suggest information not permitted under our terms. For example, any custom audience or lookalike audience suggesting specific health conditions (e.g., “arthritis”, “diabetes”) or financial status (e.g., “credit score”, “high income”) will be flagged and prevented from being used to run ad campaigns.**What these restrictions mean for your campaigns:**

- You won’t be able to use flagged custom audiences when creating new campaigns.
- If you have an active campaign using flagged custom audiences, you should edit or pause it and choose a different audience to avoid performance and delivery issues.
**For API developers:**

- Beginning September 2, 2025, `operation_statu`s will return `471` to signal if your custom audiences have been flagged.
More information on this update and how to resolve flagged custom audiences can be found [here⁠](https://www.facebook.com/business/help/1055828013359808).The Marketing API allows you to build target Custom Audiences from customer information. This includes email addresses, phone numbers, names, dates of birth, gender, locations, [App User IDs](https://developers.facebook.com/docs/graph-api/reference/user), [Page Scoped User IDs](https://developers.facebook.com/docs/app-events/bots-for-messenger), Apple’s Advertising Identifier (IDFA), or [Android Advertising ID⁠](https://l.facebook.com/l.php?u=https%3A%2F%2Fdeveloper.android.com%2Fgoogle%2Fplay-services%2Fid.html%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0).As the owner of your business’s data, you are responsible for creating and managing this data. This includes information from your Customer Relationship Management (CRM) systems. To create audiences, you must share your data in a hashed format to maintain privacy. See [Hashing and Normalizing Data](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences#hash). Meta compares this with our hashed data to see if we should add someone on Facebook to your ad’s audience.You can add an unlimited number of records to an audience, but only up to 10000 at a time. Changes to your Custom Audiences don’t happen immediately and usually take up to 24 hours. The number of records you request to remove and/or the number of Custom Audiences your account contains will increase the amount of time it takes to process this request.To improve how advertisers create and manage their audiences, Customer File Custom Audiences that have not been used in any active ad sets in over two years will be flagged for deletion on a rolling basis. You will need to provide us with your instructions before we take any action. Once audiences are moved to the “Expiring Audience” stage and flagged, you will need to provide your instructions by either using the flagged audience in an active ad set, which we will consider an instruction to retain the audience, or by deciding not to use the flagged audience in an active ad set, which we will consider an instruction to delete the audience. For more information, see the [Custom Audiences Overview](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/overview#custom-audiences-deletion) documentation.If you share conversion events using the [**Conversions API**](https://developers.facebook.com/documentation/ads-commerce/conversions-api), you can create a [website custom audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/website-custom-audiences) without additional data uploads. However, you can continue uploading supported customer information to create a Customer File Custom Audience.

## Build a Custom Audience


### Step 1: Create an Empty [Custom Audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience)

Specify `subtype=CUSTOM` and `customer_file_source` in your API call.
```
curl -X POST \
  -F 'name="My new Custom Audience"' \
  -F 'subtype="CUSTOM"' \
  -F 'description="People who purchased on my website"' \
  -F 'customer_file_source="USER_PROVIDED_ONLY"' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


#### Parameters


| Name | Description |
| --- | --- |
| customer_file_source enum string | Describes how the customer information in your Custom Audience was originally collected. Values: USER_PROVIDED_ONLY Advertisers collected information directly from customers PARTNER_PROVIDED_ONLY Advertisers sourced information directly from partners (e.g., agencies or data providers) BOTH_USER_AND_PARTNER_PROVIDED Advertisers collected information directly from customers and it was also sourced from partners (e.g., agencies) |
| name string | Custom Audience name |
| description string | Custom Audience description |
| subtype string | Type of Custom Audience |


### Step 2: Specify a List of Users

Use a `POST` API call to the `/{audience_id}/users` endpoint to specify the list of users you want to add to your Custom Audience.

#### Parameters


| Name | Description |
| --- | --- |
| session JSON Object | Required Use the session parameter to track if a specific batch of users has been uploaded. If you have an upload with more than 10,000 users, you need to split it into separate batches; each request can take up to 10,000 users. Example { "session_id" : 9778993 , "batch_seq" : 10 , "last_batch_flag" : true , "estimated_num_total" : 99996 } |
| payload JSON Object | Required Includes schema and data . Example { "schema" : "EMAIL_SHA256" , "data" : [ [ "\<HASHED_DATA\>" ], [ "\<HASHED_DATA\>" ], [ "\<HASHED_DATA\>" ] ] } |


#### Data Processing Options for US Users

If you want to enable Limited Data Use for people in California via customer list custom audiences on or after June 1, 2023, you must upload new audiences or [update your existing audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences) with the Limited Data Use flag. Regularly update and maintain your audiences and people’s Limited Data Use statuses as needed.Please note that a Limited Data Use flag applied to a user in one audience will not automatically carry over to different audiences. In the same way advertisers must manage each of their existing customer list custom audiences separately by the criteria they select, the Limited Data Use flag must be applied separately to each audience they leverage for their advertising.To explicitly NOT enable `LDU` for the record, you can either send an empty `data_processing_options` array or remove the field in the payload. Example of an empty array:
```
{
   "payload": {
       "schema": [
           "EMAIL",
                    "DATA_PROCESSING_OPTIONS"
       ],
       "data": [
           [
               "<HASHED_DATA>
",
                           []
           ]
       ]
   }
}
```
To explicitly enable `LDU`, and have Meta perform geolocation (by not including state and country of the given record), specify an array containing `LDU` for each record:
```
{
   "payload": {
       "schema": [
           "EMAIL",
                    "DATA_PROCESSING_OPTIONS"
       ],
       "data": [
           [
               "<HASHED_DATA>
",
                           ["LDU"]
           ]
       ]
   }
}
```
To enable LDU and manually specify the location:
```
{
    "customer_consent": true,
    "payload": {
        "schema": [
            "EMAIL",
            "DATA_PROCESSING_OPTIONS",
            "DATA_PROCESSING_OPTIONS_COUNTRY",
            "DATA_PROCESSING_OPTIONS_STATE"
        ],
        "data": [
            [
                "<HASHED_DATA>",
                ["LDU"],
                1,
                1000
            ]
        ]
    }
}
```


#### `session` Fields


| Name | Description |
| --- | --- |
| session_id positive 64-bit integer | Required Identifier used to track the session. This number must be generated by the advertiser and unique within a specific ad account. |
| batch_seq positive integer | Required Number to identify the request listed in the current session. This number must be sequential and start from 1 . |
| last_batch_flag boolean | Required Indicate to our systems that all batches for the ongoing Replace session have been provided. When set to true , the current request is the last one from the current session, and we don’t accept any further batches for that session. If you don’t send this flag, we automatically terminate the session 90 minutes after we receive your first batch. Any batch received after 90 minutes is also discarded. You must mark the last request to let Meta know that this is the last batch. |
| estimated_num_total integer | Optional Estimated total number of users to be uploaded in this session. This field is used to improve this session’s processing. |


#### Response

A successful response includes a JSON object with the following fields:

| Name | Description |
| --- | --- |
| audience_id numeric string | Audience identifier |
| session_id integer | Session ID you passed in |
| num_received integer | Total number of users received in this session so far |
| num_invalid_entries integer | Number of entries sent with incorrect hashing. Those entries did not return a match and are not added to the custom audience. This is not an exact number, but it represents the number range of users that did not match. |
| invalid_entry_samples JSON Array of String or Map {string: string} | Up to 100 samples of invalid entries found in the current request |

Learn more about [sharing your Custom Audience with business objects](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/adaccounts).

### Error Codes

These are errors that may be received when creating custom audiences.

| Error Code | Error Subcode | Description | Resolution |
| --- | --- | --- | --- |
| 1 |  | Please reduce the amount of data you’re asking for, then retry your request | This relates to the limit of data to return in an API response. Whilst there is no specific maximum limit, the best practice is to use a limit of 20 with pagination. |
| 100 | 1713098 | Invalid rule JSON format | Check the JSON format and parameters for issues, and retry the call. |
| 200 | 1870050 | Permissions error | Check that the ad account is linked to the Business Manager account. |
| 200 | 1870090 | Custom Audience Terms Not Accepted | Follow the Terms of Service guidelines for custom audiences, specifically for the business the account is acting on behalf of or a shared ad account. To sign the contracts for the original business, a user has to switch to an ad account not acting on behalf of or owned by the business they need to accept. |


## Remove Members from a Custom Audience

Use a `DELETE` API call to the `/{audience_id}/users` endpoint to specify the list of users you want to remove from your Custom Audience.
```
curl -X DELETE \
  --data-urlencode 'payload={
    "schema": "EMAIL_SHA256",
    "data": [
      "<HASHED_DATA>",
      "<HASHED_DATA>",
      "<HASHED_DATA>"
    ]
  }' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```
Or, you can add the `method` parameter and set it to `DELETE` in the `POST` request used to add audience members.You can remove people from a list with `EXTERN_ID`, if available.
```
curl -X DELETE \
  --data-urlencode 'payload={
    "schema": "EXTERN_ID",
    "data": [
      "<ID>",
      "<ID>",
      "<ID>"
    ]
  }' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```
You can remove a list of people from all custom audiences across your ad account using this endpoint.There may be some reasons why this information is not processed. For example, if the ad account is not owned by a business portfolio, you have not yet accepted the [Custom Audience Terms⁠](https://www.facebook.com/legal/terms/customaudience), or the information does not match with a user.To remove an Accounts Center account, include the same fields as in [user update](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/users) and make a `HTTP DELETE` call to:
```
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/usersofanyaudience
```


## Multi-Key Matching

To increase the match rate for your records, provide multiple keys in an array of individual keys; for example, [`EXTERN_ID`, `LN`, `FN`, `EMAIL`]. While you don’t need to hash `EXTERN_ID`, you must hash all personally identifying information, such as emails and names. For details, see [Hashing and Normalizing Data](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences#hash).You can provide some or all multi-keys for a record.

#### Add Users with Multi-Key Matches


```
curl \
  -F 'payload={
    "schema": [
      "FN",
      "LN",
      "EMAIL"
    ],
    "data": [
      [
        "<HASH>",
        "<HASH>",
        "<HASH>"
      ],
      [
        "<HASH>",
        "<HASH>",
        "<HASH>"
      ]
    ]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```


### Using `PAGEUID`

If you use the `PAGEUID` key, you must also include a list of page IDs. You can only send us one `PAGEUID`, which should be an array with one element.
```
curl -X POST \
  -F 'payload={
       "schema": [
         "PAGEUID"
       ],
       "is_raw": "true",
       "page_ids": [
            "<PAGE_IDs>"
            ],
       "data": [
         [
           "<HASH>",
           "<ID>",
           "<ID>",
           "<VALUE>"
         ],
         [
           "<HASH>",
           "<ID>",
           "<ID>",
           "<VALUE>"
         ],
         [
           "<HASH>",
           "<ID>",
           "<ID>",
           "<VALUE>"
         ]
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```


### Hashing and Normalization for Multi-Key

You must hash data as `SHA256`; we don’t support other hashing mechanisms. This is required for all data except [External Identifiers](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences#external_identifiers), [App User IDs](https://developers.facebook.com/docs/graph-api/reference/user), [Page Scoped User IDs](https://developers.facebook.com/docs/app-events/bots-for-messenger) and Mobile Advertiser IDs.Before you hash your data, normalize it so we can handle it. **Only First name (`FN`) and Last Name (`LN`) support special characters and non-Roman alphabets. For the best match results, provide the Roman alphabet translation with no special characters.**[Please download this CSV file](https://l.facebook.com/l.php?u=https%3A%2F%2Fscontent.fcgh38-1.fna.fbcdn.net%2Fv%2Ft39.8562-6%2F314008612_2367937923355843_814664035015443172_n.csv%3F_nc_cat%3D101%26ccb%3D1-7%26_nc_sid%3Db8d81d%26_nc_eui2%3DAeFneDTKQtfeM9aZ5vVLNTrkC9ZBm5vzIpAL1kGbm_MikG-n1J5hcHywlSDx_XQZCx5Nzd71vIcaNSIwDWMklhBf%26_nc_ohc%3DwvqqN4mmuwYQ7kNvwFiXQiy%26_nc_oc%3DAdqbhF8AVSYeYwsbH9iEXOz1De8xNFTECxanBOlmPXlMRyFlUmqbkc0P3cmoNA3S_s3oGeT8jEXIIImEkMImUPJS%26_nc_zt%3D14%26_nc_ht%3Dscontent.fcgh38-1.fna%26_nc_gid%3D-XN5VtgKwcQwP_kHQWyOvw%26_nc_ss%3D7a3a8%26oh%3D00_AfwL7ykycd70MAmBdouvFMzpAMGFgwlkDcgWmfu4qbNThg%26oe%3D69D0F124&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0) for examples of properly normalized and hashed data for the parameters below.

[Download (Right-click > Save Link As)](https://l.facebook.com/l.php?u=https%3A%2F%2Fscontent.fcgh38-1.fna.fbcdn.net%2Fv%2Ft39.8562-6%2F314008612_2367937923355843_814664035015443172_n.csv%3F_nc_cat%3D101%26ccb%3D1-7%26_nc_sid%3Db8d81d%26_nc_eui2%3DAeFneDTKQtfeM9aZ5vVLNTrkC9ZBm5vzIpAL1kGbm_MikG-n1J5hcHywlSDx_XQZCx5Nzd71vIcaNSIwDWMklhBf%26_nc_ohc%3DwvqqN4mmuwYQ7kNvwFiXQiy%26_nc_oc%3DAdqbhF8AVSYeYwsbH9iEXOz1De8xNFTECxanBOlmPXlMRyFlUmqbkc0P3cmoNA3S_s3oGeT8jEXIIImEkMImUPJS%26_nc_zt%3D14%26_nc_ht%3Dscontent.fcgh38-1.fna%26_nc_gid%3D-XN5VtgKwcQwP_kHQWyOvw%26_nc_ss%3D7a3a8%26oh%3D00_AfwL7ykycd70MAmBdouvFMzpAMGFgwlkDcgWmfu4qbNThg%26oe%3D69D0F124&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)

| Key | Guidelines |
| --- | --- |
| EMAIL criteria: email addresses | Hashing required Trim leading and trailing white space, and convert all characters to lowercase. |
| PHONE criteria: phone numbers | Hashing required Remove symbols, letters, and any leading zeroes. You should prefix the country code if the COUNTRY field is not specified. |
| GEN criteria: gender | Hashing required Use these values: m for male, f for female. |
| DOBY criteria: birth year | Hashing required Use the YYYY format: 1900 to the current year. |
| DOBM criteria: birth month | Hashing required Use the MM format: 01 to 12 . |
| DOBD criteria: birthday | Hashing required Use the DD format: 01 to 31 . |
| LN and FN criteria: last and first names | Hashing required Use a - z only. Lowercase only, no punctuation. Special characters in UTF-8 format. |
| FI criteria: first name initial | Hashing required Use a - z only. Lowercase only. Special characters in UTF-8 format. |
| ST criteria: US states | Hashing required Use the 2-character ANSI abbreviation code ⁠ , lowercase. Normalize states outside the US in lowercase, with no punctuation, no special characters, and no white space. |
| CT criteria: city | Hashing required Use a - z only. Lowercase only, with no punctuation, no special characters, and no white space. |
| ZIP criteria: zip code | Hashing required Use lowercase, and no white space. For the US, use only the first 5 digits. For the UK, use the Area/District/Sector format. |
| COUNTRY criteria: country code | Hashing required Use lowercase, 2-letter country codes in ISO 3166-1 alpha-2 ⁠ . |
| MADID criteria: mobile advertiser ID | Do not hash Use all lowercase, and keep hyphens. |


## Hashing

Provide `SHA256` values for normalized keys and `HEX` representations of this value, using lowercase for A through F. The hash function in PHP converts normalized emails and phone numbers.

| Example | Result |
| --- | --- |
| hash("sha256", "mary@example.com") | f1904cf1a9d73a55fa5de0ac823c4403ded71afd4c3248d00bdcd0866552bb79 |
| hash("sha256", "15559876543") | 1ef970831d7963307784fa8688e8fce101a15685d62aa765fed23f3a2c576a4e |


## External Identifiers

You can match people for an audience with your own identifiers, known as External Identifiers (`EXTERN_ID`). This can be any unique ID from the advertiser, such as loyalty membership IDs, user IDs, and external cookie IDs.While you don’t need to hash this ID, you must hash all Personally Identifying Information (PII) that you send with the `EXTERN_ID`s.For better matching, you should also use the exact format when you send the IDs. For example, if you choose to hash using SHA256, make sure to use the same hashed value.You can use these IDs as individual keys to delete people from Custom Audiences or create new Custom Audiences. This way you don’t need to re-upload any other matching keys. If you tag someone with hashed personal information and `EXTERN_ID`, we give `EXTERN_ID` lower precedence when we match them with people on Facebook.The data retention period for `EXTERN_ID` is 90 days.You can reuse the `EXTERN_ID` mapping to build customer file custom audiences within a single ad account.If you have an audience of `EXTERN_ID` fields in your ad account, create a new audience with just these identifiers.
```
curl \
  -F 'payload={"schema":"EXTERN_ID","data":["<ID>","<ID>"]}' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```
You can also add people tagged `EXTERN_ID` and with multi-key matching.
```
curl \
  -F 'payload={
    "schema": [
      "EXTERN_ID",
      "FN",
      "EMAIL",
      "LN"
    ],
    "data": [
      [
        "<ID>",
        "<HASH>",
        "<HASH>",
        "<HASH>"
      ],
      [
        "<ID>",
        "<HASH>",
        "<HASH>",
        "<HASH>"
      ],
      [
        "<ID>",
        "<HASH>",
        "<HASH>",
        "<HASH>"
      ]
    ]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/<CUSTOM_AUDIENCE_ID>/users
```
We support `EXTERN_ID` parameters for individual [ad accounts](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference). We cannot use values from one ad account for any other ad accounts, even if the accounts belong to the same entity.

## Replace Users API

The `/<CUSTOM_AUDIENCE_ID>/usersreplace` endpoint allows you to perform 2 actions with one API call:

- Completely remove existing users from a specific audience
- Replace those users with a new set of users.
Using the `/<CUSTOM_AUDIENCE_ID>/usersreplace` endpoint allows you to automatically delete all existing users rather than having to upload a list of users you want to delete. **This endpoint does not reset your ad set’s [learning phase⁠](https://www.facebook.com/business/help/112167992830700) when an audience is part of active ad sets unlike POST or DELETE API calls to the [`/<CUSTOM_AUDIENCE_ID>/users` endpoint](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/users).**The Replace Users API only works with audiences that meet the following requirements:

- The number of users in place before running a replace process must be smaller than 100 million. If your audience is larger than 100 million, we suggest leveraging the [`/<CUSTOM_AUDIENCE_ID>/users` endpoint](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/users) to add and remove users.
- Subtype must be set to `CUSTOM`.
- You cannot replace a value-based customer file custom audience with a non-value based customer file custom audience, or vice-versa.


### Get Started

Before you start a replace process, we recommend the following:

- Make sure your audience’s `operation_status` is `Normal`.
You cannot perform a replace operation if there is one already being executed.

- Don’t add or remove users via `/<CUSTOM_AUDIENCE_ID>/users` during an ongoing replace operation via `/<CUSTOM_AUDIENCE_ID>/usersreplace`. If you try performing a second replace operation before the first is completed, you will receive a message indicating a replace operation is already in progress.
- The maximum duration window for 1 replace session is 90 minutes. The API will reject any batches for a session received after 90 minutes from the time the session started. If you need to send batches for a duration longer than 90 minutes, wait until the replace operation for that session is done, then use the `/<CUSTOM_AUDIENCE>/users` endpoint’s add operation for the rest of your uploads.
- Once your audience is ready, specify the list of users you want to replace with your custom audience using a `POST` call to `/<CUSTOM_AUDIENCE_ID>/usersreplace`. - Once you start the replacement progress, your audience’s `operation_status` switches to `replace_in_progress`. - If your replacement operation is incomplete, your audience’s `operation_status` switches to `replace_error`. - If an operation_status of 471 is returned, the custom audience has been flagged for integrity reasons.


### Sample Request


```
curl POST \
  --data '{
    "session": {
      "session_id":9778993,
      "batch_seq":10,
      "last_batch_flag":true,
      "estimated_num_total":99996
    },
    "payload": {
      "schema": ["EMAIL","DATA_PROCESSING_OPTIONS"],
      "data": [
        ["<HASHED_DATA>"], ["<HASHED_DATA>"]
      ]
    },
  }'
https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>/usersreplace?access_token=<ACCESS_TOKEN>
```


### Call Parameters

You can include the following parameters in your `POST` call to `/<CUSTOM_AUDIENCE_ID>/usersreplace`:

| Name | Description |
| --- | --- |
| session JSON object | Required. Used to track if a specific batch of users has been uploaded. Must include a session ID and batch information. See Session Fields . You can add up to 10,000 people to an audience at a given time. If you have more than 10,000 people, split your session into multiple batches, which should all have 1 session ID. Example: { 'session_id':9778993, 'batch_seq':10, 'last_batch_flag':true, 'estimated_num_total':99996 } |
| payload JSON object | Required. Used to provide the information you want to be uploaded to your audience. Must include schema and data . See Payload Fields for more information. Example: { "schema":"EMAIL", "data":[ [" \< HASHED_EMAIL \> "], [" \< HASHED_EMAIL \> "], [" \< HASHED_EMAIL \> "] ] } |


#### `session` object fields


| Name | Description |
| --- | --- |
| session_id 64-bit integer | Required. Used to track the session. You must generate this identifier and the number must be unique within the same ad account. |
| batch_seq integer | Required. Must start at 1 . A new replace session starts when we receive a batch_seq of 1 . We recommend not sending duplicate batches with a sequence of 1 for a given session_id . Labeling the first batch is important; the rest of the batches of a session can be duplicates or any number except 1 because we use this parameter to identify the start of the session. All non-first batches for a session should be sent after the first batch. Consider the first batch as a trigger/pre-step for the replace operation. |
| last_batch_flag Boolean | Optional. Indicates all batches for the ongoing replace session have been provided. When set to true, no further batches are accepted for that session. If you do not set this flag, the session is automatically terminated 90 minutes after the first batch is received. Any batch received after 90 minutes is also discarded. |
| estimated_num_total integer | Optional. Estimated total number of users to be uploaded in this session. Used by our system to improve a session’s processing. |


#### `payload` object fields


| Name | Description |
| --- | --- |
| schema string or JSON string array | Required. Specify what type of information you will provide. It can be a single key or multi-key from this list: EMAIL PHONE GEN DOBY DOBM DOBD LN FN FI CT ST ZIP COUNTRY MADID ["hash1", "hash2", ...] Example: ["PHONE", "LN”, “FN”, “ZIP”, “DOBYM"] |
| data JSON array | Required. List of data corresponding to the schema. Examples: If the schema is "EMAIL" , the data should be a list of email sha256 hashes. If the schema is a list of hashes as in the previous example, the data should be like "phone_hash_value" , "LN_FN_ZIP_DOBYM" . |

Once you make your `POST` request, you get a response with the following fields:

| Name | Description |
| --- | --- |
| account_id integer | Account identifier. |
| session_id integer | Session ID you have previously provided. |
| num_received integer | Total number of users received in this session so far. |
| num_invalid_entries integer | Total number of users with an invalid format or unable to be decoded. If this number is not zero, recheck your data. |
| invalid_entry_samples JSON string array | Up to 100 samples of invalid entries in current request. Recheck your data. |


### Replace Users API common errors

All errors returned from the `/{custom-sudience-id}/usersreplace` endpoint have the error code **2650**. Here are some of the most common error subcodes returned, as well as guidance on how to resolve them.

| Error SubCode | Description | What To Do |
| --- | --- | --- |
| 1870145 | Audience Update In Progess | You can’t replace a customer list custom audience that is in the process of being updated. Wait for the audience availability to become “Normal” and try again. |
| 1870158 | Replace Session Timed Out | You’ve reached the 90-minute time limit for your replace batch session. Your customer list custom audience will be replaced with what you’ve uploaded so far. To add more to the custom audience, wait until the replace process is finished, and then use the ADD operation. |
| 1870147 | Invalid Upload Batch for Replace | The first batch_seq was not detected. You must start your batch_seq at integer 1 . |
| 1870159 | Replace Session Finished | This replace operation is already finished because you uploaded a batch with last_batch_flag==true . To add additional batches to the custom audience, wait until the replace process is finished, and then use the ADD operation. |
| 1870148 | Something Went Wrong | Your customer list was not fully updated. If your audience size is significantly differ than expected, consider trying again. |
| 1870144 | DFCA Size Not Supported For Replace | You can’t replace a customer list customer audience that has a size of 100 million or more. |


## FAQ

**What is the recommended maximum value of “limit” that should be used in the /customaudiences endpoint?**The `limit` field is the maximum number of objects that may be returned in an API call. There is no specific maximum value of the `limit` parameter when querying the custom audience endpoints.However, the best practice is to use a limit of 20 with pagination. See the [Paginated Results documentation](https://developers.facebook.com/docs/graph-api/results) for more information.**What are the limits on the number of custom audiences we can have in an account?**The limits we have on the number of custom audiences in an account:

- Standard Data File Custom Audiences: 500
- Custom Audiences from your website: 10000
- Mobile App Custom Audiences: 200
- Lookalike Audiences: 500
**Is hashing required for Mobile Advertiser IDs (MADID)?**No.**Are there any restrictions on an audience based on the Customer File Source (i.e., USER_PROVIDED_ONLY, PARTNER_PROVIDED_ONLY, BOTH_USER_AND_PARTNER_PROVIDED)?**Currently, there are no restrictions on the `customer_file_source` field when creating a custom audience using the Marketing API.**How do you resolve the “Custom Audience Terms Not Accepted” error?**The “Custom Audience Terms Not Accepted” error typically occurs when attempting to create or use a custom audience on Meta’s advertising platform without accepting the necessary terms and conditions or when accepting the terms and conditions for an ad account on behalf of or shared with different businesses.Please see the [Custom Audiences Terms of Service](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/custom-audience-terms-of-service) document for more information on accepting the terms of service while checking the special use cases of shared ad accounts or on behalf of ad accounts.

## Resources

There are other types of audiences you can build and target, or share:

- **[Custom Audiences From Your Website](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/website-custom-audiences)** — Create an audience based on people who visited a specific page or made action on your website. Build an audience based on data from [Meta Pixel](https://developers.facebook.com/docs/marketing-api/audiences-api/pixel) on your site.
- **[Custom Audiences From Your Mobile App](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/mobile-app-custom-audiences)** — Create an audience based on people who use your mobile app. Build an audience based on data from [App Events](https://developers.facebook.com/docs/app-events).
- **[Lookalike Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/lookalike-audiences)** — Identify people you already know and advertise to similar people on the Facebook app.
- **[Offline Custom Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/offline-custom-audiences)** — Create an audience based on people who visited your store, made calls to your customer service, or took action through other offline means.
- **[Canvas Engagement Audiences](https://developers.facebook.com/documentation/ads-commerce/marketing-api/creative/collection-ads#audience)** — Create an audience that contains anyone who engaged with your Canvas.


## See Also


- [Custom Audience](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience)
- [Custom Audience Users](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/custom-audience/users)
- [Custom Audience Session](https://developers.facebook.com/docs/marketing-api/reference/custom-audience-session)
- [Custom Audience Terms Of Service](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/custom-audience-terms-of-service)
Did you find this page helpful?ON THIS PAGEBuild a Custom AudienceStep 1: Create an Empty Custom AudienceParametersStep 2: Specify a List of UsersParametersData Processing Options for US Userssession FieldsResponseError CodesRemove Members from a Custom AudienceMulti-Key MatchingAdd Users with Multi-Key MatchesUsing PAGEUIDHashing and Normalization for Multi-KeyHashingExternal IdentifiersReplace Users APIGet StartedSample RequestCall Parameterssession object fieldspayload object fieldsReplace Users API common errorsFAQResourcesSee Also$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6UZ9jK5YV3SsAVWYrt8wRiUhxHpflkUMxzfKx84gt9EmuzFwZkzIoKq8lVMA_aem_jZ_QnfniNzQyFNsRysKQLQ&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WjUaJABxhIEfEco4d2T3ZdHdKnf0ay-Bh5wMd2sfuHvbK0OX73lRGDGDCOg_aem_MpiyZmyCffOJYN5zfFbuow&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4mMGQKovbJkPkdc9A1c7_tkVdL7eka1RiyUOJVz-pS4Z1smNgftHycOh02VA_aem_xGemM-thXznVMfsI0-_bVg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7nFmnXXAoNHcrh3MkYmP5irss0jqs7lZRAtpnrJlNUjh5xLqAMlsXal0hY6A_aem_z_iMRZeOLIsn1AOS6oDapA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5qJwWwg2JOUs_MWY-kdXT6nfyr1uRr8GBSxFyg3u6-wLs9oqu6eFcEV-Y1WQ_aem_5l4NVifQJhJP-Eo1Q9ztwg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6o33yrPKNj8oGSCoCRQuV5FUd_9W4Uf3BVB-3AsPxgQVuLBqxg46D8-WWQLQ_aem_rfn1X2FrSEw__lLPdGSRAA&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR62TDL6EBiPi7IlpAshb8SvV3cwnJvH2wduvhc0eryzk70xnWM7l2cBjfme9A_aem_NPAcIPwxYonkk75lpfFnRw&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExWHJ0WTRlYzB4bzl2NlZvZ3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6izWTyBeixwL4pi2mvR0tGhkBPKw4751_BqEAr6Xv-mUpIUlp86UPDtykDnA_aem_uwrTD8SWo4jQGTxXJpu-Wg&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5zUFgh7ov-ZjmXCC_e26gujOW_H_NXaJRWwU67MnmmmoEQ98zLSFuCcV6lvyETRF3l9MDWnTq-m_IcByL1vErJPvVPlpaUMGf6ZpFlbLYRkrt6oTA1b4xG5XvNzyyavAIDMTgWSp-8qRBc_3MrZ4VulP0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$