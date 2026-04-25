<!-- Fonte: Custom Audience.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/reference/custom-audience/ -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Custom Audience


Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences that may suggest information not permitted under our terms. For example, any custom audience or lookalike audience suggesting specific health conditions (e.g., "arthritis", "diabetes") or financial status (e.g., "credit score", "high income") will be flagged and prevented from being used to run ad campaigns.


**What these restrictions mean for your campaigns:**


- You won't be able to use flagged custom audiences when creating new campaigns.
- If you have an active campaign using flagged custom audiences, you should edit or pause it and choose a different audience to avoid performance and delivery issues.


**For API developers:**


- Beginning September 2, 2025, `operation_statu`s will return `471` to signal if your custom audiences have been flagged.


More information on this update and how to resolve flagged custom audiences can be found [here](https://www.facebook.com/business/help/1055828013359808).


Build an audience of your customers, website visitors, mobile app visitors or people similar to them. To add or remove users from a custom audience, see the [Custom Audience User reference](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/).


To use custom audiences, business users must first sign our [Terms Of Service](https://developers.facebook.com/docs/marketing-api/audiences-api/custom-audience-terms-of-service).


To improve how audiences are created and managed, custom audiences that have not been used in any active ad sets in over two years will be deleted on a rolling basis automatically. See the [Custom Audiences: Overview: Deletion](https://developers.facebook.com/docs/marketing-api/audiences/overview#custom-audiences-deletion) for more information.


### Flagged custom and lookalike audiences



If one or more custom or lookalike audience is flagged with an `operation_status` of `471`, the `effective_status` field of the ad set will change to `WITH_ISSUES` and the `issues_info` list will be populated with one issue per flagged audience. The `fields_violating_integrity_policy` field will be populated with the list of flagged fields.


Attempting to edit a flagged custom audience without changing the custom audience fields listed in the `fields_violating_integrity_policy` field will result in an error.

```
{
  "error": {
    "message": "Invalid parameter",
    "code": 100,
    "error_subcode": 1713231,
    "error_user_title": "Update Restricted Fields and Rule",
    "error_user_msg": "This custom audience has integrity restrictions. To continue, you must update the restricted fields and the rule in your current edit",
  },
}
```


Attempting to edit a flagged lookalike audience or customer file custom audience (DFCA) will result in an error.

```
{
  "error": {
    "message": "Invalid parameter",
    "code": 100,
    "error_subcode": 1713228,
    "error_user_title": "Custom Audience Cannot Be Edited",
    "error_user_msg": "This audience cannot be edited due to integrity restrictions. Please appeal the restrictions or create a new audience",
  },
}
```


**Example**

```
{
    "account_id": "<OWNER_ACCOUNT_ID>",
    "approximate_count": 5000,
    "approximate_count_lower_bound": 4900,
    "approximate_count_upper_bound": 5100,
    "customer_file_source": "USER_PROVIDED_ONLY",
    "description": "Audience Description",
    "fields_violating_integrity_policy": ["<FIELD>", ...],
    "id": "<CUSTOM_AUDIENCE_ID>",
    "name": "Audience Name",
    "operation_status": {
        "code": 471,
        "description": "The custom audience or lookalike is blocked because it suggests the use of information (e.g., health, financial) not allowed under Meta's terms, and is restricted from running ads. Review the audience and remove prohibited information, or choose a different one."
    },
    "retention_days": 0,
    "subtype": "CUSTOM",
    "time_created": 1755083743,
    "time_updated": 1755083943,
    "time_content_updated": 1755083943,
    "owner_account_info": {
        "account_id": "<OWNER_ACCOUNT_ID>",
        "account_name": "Account Name",
        "business_id": "<OWNER_BUSINESS_ID>",
        "business_name": "Business Name"
    },
    ...
}
```


#### To resolve flagged audiences



If your custom or lookalike audiences are flagged, consider these options.


To resolve flagged custom audiences:


- **Review flagged audiences**: Use Audience Manager to review your custom audience along with other information included in an audience, and remove any information that is not allowed under [Meta's terms](https://www.facebook.com/legal/terms/businesstools/).
- **Create new or choose different audiences**: Alternatively, you can create a new custom audience or choose a different existing custom audience and make sure that it does not include information not allowed under our terms and use that to run campaigns.


To resolve flagged lookalike audiences:


- **Resolve issues with the underlying custom audience**: If the underlying custom audience (also known as the seed audience) of your lookalike audience is flagged, you will need to resolve the issue with the underlying custom audience on which the lookalike audience is built. Please refer to the preceding section on how to resolve flagged custom audiences.
- **Create new audiences**: Consider developing new lookalike audiences and make sure that they don't include information that is not allowed under our terms.


##### Request a review



If you believe your custom audience or lookalike audience has been flagged in error and doesn't include non-permitted information, you can request a review via Ads Manager under the campaigns table or, or in Audience Manager by clicking on individual audiences and under the summary tab of the impacted audience.


## Leitura


Custom audiences are designed to provide advertisers the ability to target their ads to a specific set of people with whom they have already established a relationship on and off Facebook. Advertisers may choose to define audiences by email address, Facebook User IDs, phone numbers, names, date of birth, gender, locations, [app user IDs](https://developers.facebook.com/docs/app-ads/targeting/mobile-advertiser-ids), Apple's Advertising Identifier (IDFA), [Android's advertising ID](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.google.com%2Fads%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTEAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4YbSOgIfF3GLO6GbmojZmRXt_ZEzowXW4tavYw0mlTye95QUch67v6Xt3Cmg_aem_-7Qdj4XKOvAA3WtkQ4arIA%23apps&h=AT701-DMt8tgQmLA_ValeJW2NM7jqk89bHe3E1moavcjqBhCyceL6dnWR94KmmkHjMaONN6ptPp62CAaggS4jNvH01_9lEovz43VyQLzbeuRCiJxO11k4_OQosOJmeTsbsG4yj5fwho) or by a combination of rules used to identify users who took specific actions on their website.


When utilizing Facebook User IDs please ensure you comply with [Facebook Platform Terms](https://developers.facebook.com/terms) and [Developer Policies](https://developers.facebook.com/devpolicy). You must accept the [Custom Audience Terms of Service](https://developers.facebook.com/docs/marketing-api/audiences-api/custom-audience-terms-of-service) in order to use custom audiences. You can query which terms have been accepted by checking the `tos_accepted` field of a given ad account. See [Ad Account](https://developers.facebook.com/docs/marketing-api/adaccount/) for more information.


### Example


```
curl -G \
  -d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```


### Parâmetros


| Parâmetro | Descrição |
| --- | --- |
| ad_account_id numeric string | ID of the recipient ad account in which custom audience is used. |
| special_ad_categories list\<string\> | special_ad_categories |
| special_ad_category_countries list\<string\> | special_ad_category_countries |


### Campos


| Campo | Descrição |
| --- | --- |
| id numeric string | Custom audience ID Padrão |
| account_id numeric string | Ad Account ID |
| approximate_count_lower_bound integer | Lower bound of the approximate number of people in this audience. A call for this field returns -1 for inactive lookalikes . |
| approximate_count_upper_bound integer | Upper bound of the approximate number of people in this audience. A call for this field returns -1 for inactive lookalikes . |
| customer_file_source string | Source of customer information in the uploaded file |
| data_source CustomAudienceDataSource | JSON dictionary of type , sub_type to indicate by which method the custom audience was created. Note: Subtypes IG_BUSINESS_EVENTS , FB_EVENT_SIGNALS and MULTI_DATA_EVENTS can only be created through Ads Manager, Audience Manager, and not through the API. |
| delivery_status CustomAudienceStatus | JSON dictionary of code and description . It indicates whether or not an audience can be used in ads. Possible values include: 200 : Returned if the audience is active and ready to be used. 300 : Returned if the audience is smaller than it should be. This audience is currently inactive and cannot be used. 400 and above: Returned if the audience is not usable for a variety of reasons, including policy violation. |
| description string | Custom audience description |
| external_event_source AdsPixel | Read-only JSON dictionary with id keys containing the Pixel ID whose traffic generated this custom audience. Will throw an error if the app making the call lacks the required permissions. |
| fields_violating_integrity_policy list\<string\> | A list of custom audience fields (either name, description or rule) that are flagged for a custom audience that may suggest information not permitted under our terms. |
| is_value_based bool | Whether the audience is used to seed value based lookalike |
| lookalike_audience_ids list\<numeric string\> | The IDs of the lookalike audiences generated from this audience |
| lookalike_spec LookalikeSpec | Generated only when the subtype is LOOKALIKE . More info at Lookalike Audience |
| name string | Custom audience name |
| operation_status CustomAudienceStatus | JSON dictionary of code to int value and description to a description string. The operation status represents the status of the last operation performed on an audience. In general, it will have following states: 0 : Status not available 100 : If an audience hasn't been used in an active ad set for over 2 years, it will begin to expire. Expiring audiences that remain unused for 90 days will be deleted. 200 : Normal. There is no updating or issues found 400 : Warning. There is some message we would like advertisers to know 410 : No upload. No file has been uploaded 411 : Low match rate. Low rate of matched people 412 : High rate of invalid entries in the last upload session. Customer file has unusable data 414 : Replace in progress 415 : Replace failed 421 : No pixel. Your Facebook pixel hasn't been installed on your website yet 422 : Pixel not firing. Your Facebook pixel isn't firing 423 : Invalid pixel. Your Facebook pixel is invalid 431 : Lookalike Audience refresh failed 432 : Lookalike Audience build failed 433 : Lookalike Audience build failed 434 : Lookalike Audience build retrying 441 : We're finding people who fit your audience criteria. You can start running ads with this audience right away, but be aware that your audience size will increase as the audience is populated 442 : Your Custom Audience could not be prefilled 450 : This audience either hasn't been used in an ad for at least 30 days or was created over 90 days ago and has never been used. For this reason, your audience is out of date. 470 : The account that created this audience is no longer active 471 : The audience has been flagged for integrity reasons. 500 : Error: there is some error and advertisers need to take action items to fix the error |
| opt_out_link string | Your opt-out URL so people can choose not to be targeted |
| page_deletion_marked_delete_time integer | This field is used to tell when the audience will be deleted from the system if it is created using a page which has been deleted |
| permission_for_actions AudiencePermissionForActions | JSON dictionary of permissions (string) to boolean value if the custom audience has that permission |
| pixel_id numeric string | ID of the pixel which is collecting events for this Website Custom audience |
| retention_days int32 | Number of days to keep the user in this cluster. You can use any value between 1 and 180 days. Defaults to forever, if not specified. Only available for Customer File Custom Audience, including Custom Audiences created from CRM data. |
| rule string | Audience rules to be applied on the referrer URL |
| rule_aggregation string | Aggregation on top of the rule, examples of aggregations include: count, sum etc |
| sharing_status CustomAudienceSharingStatus | Sharing status of this custom audience for the ad account |
| subtype string | Type of custom audience, derived from original data source. Note: Subtypes IG_BUSINESS , FB_EVENT , EXPERIMENTAL and MULTI_DATA can only be created through Ads Manager, Audience Manager, and not through the API. |
| time_content_updated unsigned int32 | Last update of people in this custom audience, this field is only supported for Customer List Custom Audiences. |
| time_created unsigned int32 | Creation time |
| time_updated unsigned int32 | Last time this audience metadata was updated |


### Bordas


| Borda | Descrição |
| --- | --- |
| adaccounts Edge\<CustomAudienceAdAccount\> | The ad account ids associated with this custom audience |
| ads Edge\<Adgroup\> | Ads that are using this custom audience |
| health Edge\<CustomAudienceHealth\> | health |
| sessions Edge\<CustomAudienceSession\> | Data upload sessions of this custom audience |
| shared_account_info Edge\<CustomAudiencesharedAccountInfo\> | List of Ad Accounts and Businesses this Audience is shared to |


### Error Codes


| Erro | Descrição |
| --- | --- |
| 100 | Invalid parameter |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#custom-audience. |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 2500 | Error parsing graph query |


## Criando


### Limitations



- The `subtype` field for engagement custom audiences is only supported for video.
- Mobile app custom audiences for inclusion targeting is no longer supported for the `POST /{ad-account-id}/adsets` endpoint for iOS 14+ SKAdNetwork campaigns.
- New iOS 14+ app install campaigns will no longer be able to use app connections targeting.


### Examples


Create a blank audience:

```
curl \
  -F 'name="My new CA"' \
  -F 'subtype=CUSTOM' \
  -F 'description="People who bought from my website"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```
Não é possível executar esta operação neste ponto de extremidade.

## Atualizando


If a person opted out of being targeted, you must remove them from all custom audiences in which they appear. To opt-out a person from an audience after they have clicked through to your opt-out URL, make an `HTTP DELETE` call to:

```
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/usersofanyaudience
```


Provide the same fields as you do in a [user update](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/). This will remove the people you specify from **ALL** custom file custom audiences belonging to the specified ad account.


### Examples


To update the audience name:

```
curl \
  -F 'name=Updated Name for CA' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```


To edit an opt-out link:

```
curl \
  -F 'opt_out_link=http://www.yourdomain.com/optout' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>
```
You can update a [CustomAudience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/) by making a POST request to [`/{custom_audience_id}`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/).

### Exemplo

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=%3CCUSTOM_AUDIENCE_ID%3E%2F%3Fname%3DUpdated%2BName%2Bfor%2BCA&version=v25.0)
```
POST /v25.0/<CUSTOM_AUDIENCE_ID>/ HTTP/1.1
Host: graph.facebook.com

name=Updated+Name+for+CA
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/<CUSTOM_AUDIENCE_ID>/',
    array (
      'name' => 'Updated Name for CA',
    ),
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
    "/<CUSTOM_AUDIENCE_ID>/",
    "POST",
    {
        "name": "Updated Name for CA"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
Bundle params = new Bundle();
params.putString("name", "Updated Name for CA");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<CUSTOM_AUDIENCE_ID>/",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
NSDictionary *params = @{
  @"name": @"Updated Name for CA",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<CUSTOM_AUDIENCE_ID>/"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X POST \
  -F 'name="Updated Name for CA"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>/
```
Se quiser saber como usar a Graph API, leia nosso [guia sobre Como usar a Graph API](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parâmetros


| Parâmetro | Descrição |
| --- | --- |
| allowed_domains list\<string\> | A list of domains that the audience is restricted to |
| claim_objective enum {AUTOMOTIVE_MODEL, COLLABORATIVE_ADS, HOME_LISTING, MEDIA_TITLE, PRODUCT, TRAVEL, VEHICLE, VEHICLE_OFFER} | Specifies the objective of audiences with subtype=CLAIM |
| content_type enum {AUTOMOTIVE_MODEL, DESTINATION, FLIGHT, GENERIC, HOME_LISTING, HOTEL, LOCAL_SERVICE_BUSINESS, MEDIA_TITLE, OFFLINE_PRODUCT, PRODUCT, VEHICLE, VEHICLE_OFFER} | Specifies a mandatory content type for claim_objective : TRAVEL , AUTO_OFFER , HOME_LISTING , VEHICLE . |
| customer_file_source enum {USER_PROVIDED_ONLY, PARTNER_PROVIDED_ONLY, BOTH_USER_AND_PARTNER_PROVIDED} | Source of customer information in the uploaded file |
| description string | The description for this custom audience |
| enable_fetch_or_create boolean | Fetch custom audience instead of create new one when there exists custom audience with identical name, claim_objective, content_type, event_source_group/event_sources/sliced_event_source_group, inclusions, exclusions and rule |
| event_source_group numeric string or integer | Specifies a mandatory content type for claim_objective : TRAVEL , AUTO_OFFER , HOME_LISTING , VEHICLE . |
| event_sources array\<JSON object\> | Specifies a mandatory content type for claim_objective : TRAVEL , AUTO_OFFER , HOME_LISTING , VEHICLE . |
| → id int64 | id Obrigatório |
| → type enum {APP, OFFLINE_EVENTS, PAGE, PIXEL} | type Obrigatório |
| lookalike_spec JSON-encoded string | The specification for creating a lookalike audience |
| name string | The name of this custom audience |
| opt_out_link string | Your opt-out URL so people can choose not to be targeted |
| product_set_id numeric string or integer | The Product Set to target with this audience |
| rule string | Audience rule to be applied on the referrer URL. Used for website custom audiences , product audiences , and video remarketing audiences . |
| rule_aggregation string | Aggregation rule |
| use_for_products list\<enum {ADS, MARKETING_MESSAGES}\> | use_for_products |
| use_in_campaigns boolean | use_in_campaigns |


### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview/#read-after-write) and will read the node to which you POSTed. Struct  {`success`: bool, `message`: string, }

### Error Codes


| Erro | Descrição |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 2650 | Failed to update the custom audience |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#custom-audience. |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |


## Excluindo


When you delete a custom audience, it will be permanently removed from your account and your ads using it will stop running. You won't be able to restart any ads that used this audience in the past.
You can delete a [CustomAudience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/) by making a DELETE request to [`/{custom_audience_id}`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/).

### Exemplo

[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=DELETE&path=%3CCUSTOM_AUDIENCE_ID%3E%2F&version=v25.0)
```
DELETE /v25.0/<CUSTOM_AUDIENCE_ID>/ HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/<CUSTOM_AUDIENCE_ID>/',
    array (),
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
    "/<CUSTOM_AUDIENCE_ID>/",
    "DELETE",
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
    "/<CUSTOM_AUDIENCE_ID>/",
    null,
    HttpMethod.DELETE,
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
                               initWithGraphPath:@"/<CUSTOM_AUDIENCE_ID>/"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X DELETE -G \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CUSTOM_AUDIENCE_ID>/
```
Se quiser saber como usar a Graph API, leia nosso [guia sobre Como usar a Graph API](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parâmetros

Este ponto de extremidade não tem nenhum parâmetro.

### Return Type

 Struct  {`success`: bool, }

### Error Codes


| Erro | Descrição |
| --- | --- |
| 200 | Permissions error |
| 2656 | Failed to delete custom audience because associated lookalikes exist |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |

Nesta Página[Custom Audience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#overview)[Leitura](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#Reading)[Example](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#example)[Parâmetros](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#par-metros)[Campos](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#campos)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#bordas)[Error Codes](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#error-codes)[Criando](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#Creating)[Limitations](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#limitations)[Examples](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#examples)[Atualizando](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#Updating)[Examples](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#examples-2)[Exemplo](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#exemplo)[Parâmetros](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#par-metros-2)[Return Type](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#return-type)[Error Codes](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#error-codes-2)[Excluindo](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#Deleting)[Exemplo](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#exemplo-2)[Parâmetros](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#par-metros-3)[Return Type](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#return-type-2)[Error Codes](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#error-codes-3) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4fDnkv30w0gZWfI7_wacl3MKV4rPmcWfxHpiS--NLsfv-jCGcxrHgw8_aovg_aem_6DkTAstZek-oST26dnZLxg&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4DyerS-nczG5RRR8ze6SM0WUL0lZQA3ktg6vEHGW_m9DP24eX0l6iXDCk4Ag_aem_-UfJiBBAByBIqBF0OWpBEg&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4L52mVCNKCZZW9gCEiP7Lh2YtNJ69gwVJi4ERuK066VZ2xylT4ieAHR_sHtA_aem_ddrGQeYXTH_8UMB6lOcrdw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4fDnkv30w0gZWfI7_wacl3MKV4rPmcWfxHpiS--NLsfv-jCGcxrHgw8_aovg_aem_6DkTAstZek-oST26dnZLxg&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR5wLMoQiSrLERxmyHJohVs_omu8epuG_h-Cmaoow9wpPMzKcCQQkqJ3DlYzag_aem_4Ztb5iv3omEzbukMz01Cqw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR789Y46GDMoWI4WZq-_KI0ovaFjWOuWIvOZqAvuNR8bqCDCUCd6QyLzz1MOiQ_aem_gyo8oxHpWgl_4qFC0HmgNA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR5wLMoQiSrLERxmyHJohVs_omu8epuG_h-Cmaoow9wpPMzKcCQQkqJ3DlYzag_aem_4Ztb5iv3omEzbukMz01Cqw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6_Siydv9_WEqwgbg3sSEAhJhlt5-C8iGxGDjr74X3eZ-FmeZPX80-2KhAfVA_aem_CVH6aNHYdGiTbDtz05bN0w&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4L52mVCNKCZZW9gCEiP7Lh2YtNJ69gwVJi4ERuK066VZ2xylT4ieAHR_sHtA_aem_ddrGQeYXTH_8UMB6lOcrdw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6_Siydv9_WEqwgbg3sSEAhJhlt5-C8iGxGDjr74X3eZ-FmeZPX80-2KhAfVA_aem_CVH6aNHYdGiTbDtz05bN0w&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4L52mVCNKCZZW9gCEiP7Lh2YtNJ69gwVJi4ERuK066VZ2xylT4ieAHR_sHtA_aem_ddrGQeYXTH_8UMB6lOcrdw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6HBBV_pyEcS8j16SOOtlgPNQ8PZiOQFsyB5I5PPeXqpva7KfgNp5vLWU21kw_aem_PDbypzawXHbtGryOFTZSyA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR770yEiC_0To1YwqseS7Rjd_49YbDIuW48tDktcFbjsV4wmyTWMmEPySBfNng_aem_ORkLhQLPgtZi4z9VM0-7dA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR770yEiC_0To1YwqseS7Rjd_49YbDIuW48tDktcFbjsV4wmyTWMmEPySBfNng_aem_ORkLhQLPgtZi4z9VM0-7dA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6_Siydv9_WEqwgbg3sSEAhJhlt5-C8iGxGDjr74X3eZ-FmeZPX80-2KhAfVA_aem_CVH6aNHYdGiTbDtz05bN0w&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4fDnkv30w0gZWfI7_wacl3MKV4rPmcWfxHpiS--NLsfv-jCGcxrHgw8_aovg_aem_6DkTAstZek-oST26dnZLxg&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6HBBV_pyEcS8j16SOOtlgPNQ8PZiOQFsyB5I5PPeXqpva7KfgNp5vLWU21kw_aem_PDbypzawXHbtGryOFTZSyA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR789Y46GDMoWI4WZq-_KI0ovaFjWOuWIvOZqAvuNR8bqCDCUCd6QyLzz1MOiQ_aem_gyo8oxHpWgl_4qFC0HmgNA&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR6LFS4TaXkOVtpTfN7J6m0ko1n5Wt-gmrYOW3IISVbUOJOGfJvENw0LyoiYVw_aem_bGkbSV2BdLF_3xHlvjCsRQ&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExTXpjYWZzRGx5cDc2ZkI4YnNydGMGYXBwX2lkATAAAR4L52mVCNKCZZW9gCEiP7Lh2YtNJ69gwVJi4ERuK066VZ2xylT4ieAHR_sHtA_aem_ddrGQeYXTH_8UMB6lOcrdw&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4XqmdR7_119sAgMHEH75JKZCIMzgM-X5-preMQZZ7tgASIKK1TVM3-Fo-rBM0-I-QOSR08AtMRXeUUSq8CTkTdApkdL-__E0GvkEXv6sVqzqOvMzK-rM0n8Nez6uetjAw9UxWdMaE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão