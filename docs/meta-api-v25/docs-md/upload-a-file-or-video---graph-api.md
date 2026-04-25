<!-- Fonte: Upload a File or Video - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/guides/upload -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Upload a file



The Resumable Upload API allows you to upload large files to Meta's social graph and resume interrupted upload sessions without having to start over. Once you have uploaded your file, you can publish it.


References for endpoints that support uploaded file handles will indicate if the endpoints support handles returned by the Resumable Upload API.


### Before you start



This guide assumes you have read the [Graph API Overview](https://developers.facebook.com/docs/graph-api/overview) and the [Meta Development](https://developers.facebook.com/docs/development) guides and performed the necessary actions needed to develop with Meta.


You will need:


- A Meta app ID
- A file in one of the following formats: - `pdf` - `jpeg` - `jpg` - `png` - `mp4`
- A User access token


## Step 1: Start an upload session



To start an upload session send a `POST` request to the `/<APP_ID>/uploads` endpoint, where `<APP_ID>` is your app's Meta ID, with the following required parameters:


- `file_name` - the name of your file
- `file_length` - file size in bytes
- `file_type` - The file's MIME type. Valid values are: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, and `video/mp4`


#### Request Syntax



*Formatted for readability.*

```
curl -i -X POST "https://graph.facebook.com/v25.0/<APP_ID>/uploads
  ?file_name=<FILE_NAME>
  &file_length=<FILE_LENGTH>
  &file_type=<FILE_TYPE>
  &access_token=<USER_ACCESS_TOKEN>"
```


Upon success, your app will receive a JSON response with the upload session ID.

```
{
  "id": "upload:<UPLOAD_SESSION_ID>"
}
```
[○](https://developers.facebook.com/docs/graph-api/guides/upload#)

## Step 2: Start the upload



Start uploading the file by sending a `POST` request to the `/upload:<UPLOAD_SESSION_ID>` endpoint with the following `file_offset` set to `0`.


#### Request Syntax


```
curl -i -X POST "https://graph.facebook.com/v25.0/upload:<UPLOAD_SESSION_ID>"
  --header "Authorization: OAuth <USER_ACCESS_TOKEN>"
  --header "file_offset: 0"
  --data-binary @<FILE_NAME>
```


You must include the access token in the header or the call will fail.


On success, your app receives the file handle which you will use in your API calls to publish the file to your endpoint.

```
{
  "h": "<UPLOADED_FILE_HANDLE>"
}
```


#### Sample Response


```
{
    "h": "2:c2FtcGxl..."
}
```


### Resume an interrupted upload



If you have initiated an upload session but it is taking longer than expected or has been interrupted, send a `GET` request to the `/upload:<UPLOAD_SESSION_ID>` endpoint from [Step 1](https://developers.facebook.com/docs/graph-api/guides/upload#step-1).

```
curl -i -X GET "https://graph.facebook.com/v25.0/upload:<UPLOAD_SESSION_ID>"
  --header "Authorization: OAuth <USER_ACCESS_TOKEN>"
```


Upon success, your app will receive a JSON response with the `file_offset` value that you can use to resume the upload process from the point of interruption.

```
{
  "id": "upload:<UPLOAD_SESSION_ID>"
  "file_offset": "<FILE_OFFSET>"
}
```


Send another `POST` request, like the you sent in [Step 2](https://developers.facebook.com/docs/graph-api/guides/upload#step-2), with `file_offset` set to this `file_offset` value you just received. This will resume the upload process from the point of interruption.

```
curl -i -X POST "https://graph.facebook.com/v25.0/upload:<UPLOAD_SESSION_ID>"
  --header "Authorization: OAuth <USER_ACCESS_TOKEN>"
  --header "file_offset: <FILE_OFFSET>"
  --data-binary @<FILE_NAME>
```
[○](https://developers.facebook.com/docs/graph-api/guides/upload#)

## Next Steps



- Visit the [Video API documentation](https://developers.facebook.com/docs/video-api/guides/publishing) to publish a video to a Facebook Page.
 [○](https://developers.facebook.com/docs/graph-api/guides/upload#)[○](https://developers.facebook.com/docs/graph-api/guides/upload#)On This Page[Upload a file](https://developers.facebook.com/docs/graph-api/guides/upload#upload-a-file)[Step 1: Start an upload session](https://developers.facebook.com/docs/graph-api/guides/upload#step-1)[Step 2: Start the upload](https://developers.facebook.com/docs/graph-api/guides/upload#step-2)[Resume an interrupted upload](https://developers.facebook.com/docs/graph-api/guides/upload#resume-an-interrupted-upload)[Next Steps](https://developers.facebook.com/docs/graph-api/guides/upload#next-steps) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6jh7Q53FlP68HbnJnH9libdGXnWfHthzlAPciuWeAmzhMyVhx7_yrIh7NGzg_aem_L3c4d-vIyfcuak4dtwhaGw&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6IrP8aX15Pa-rkMiVI8tysTGJ4JYV0k9eB_gOXX55gQ8jAnR3PCxH23Mk3Jw_aem_9aG-syNGnHpUXsFwjxKG9g&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6jh7Q53FlP68HbnJnH9libdGXnWfHthzlAPciuWeAmzhMyVhx7_yrIh7NGzg_aem_L3c4d-vIyfcuak4dtwhaGw&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UNadeUih2EPkTlvvsqggQoIWx6Sg3YnNQr5-UuS65thXS6LlFaAMtiE4ZNQ_aem_nRJ5xTCIkFBFkkoAUVfUBA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UNadeUih2EPkTlvvsqggQoIWx6Sg3YnNQr5-UuS65thXS6LlFaAMtiE4ZNQ_aem_nRJ5xTCIkFBFkkoAUVfUBA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5G9glBxVZVV_OMRd0bUA1CHrrGNak9ob3RqAOZ20he_HCplBU6netVOfkMHw_aem_Eb6WqV7Wr6q3e0zziM9EBg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4kq-5ZoH038PEnXGDx2-YEic2ifBBMNjCgiF_V_9S_9CDUNgth1336zYFxYA_aem_Ji47Dft0sG1_CBD8MeaBYg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7nGktdOcwR8Ux-YJUoeAiq5Sv8aQMxIMz9mL6Uzcfj__-3fI1eS3x_Q0oZog_aem_avHQ-TSM41z-2EE-K5t2Hw&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7nGktdOcwR8Ux-YJUoeAiq5Sv8aQMxIMz9mL6Uzcfj__-3fI1eS3x_Q0oZog_aem_avHQ-TSM41z-2EE-K5t2Hw&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UNadeUih2EPkTlvvsqggQoIWx6Sg3YnNQr5-UuS65thXS6LlFaAMtiE4ZNQ_aem_nRJ5xTCIkFBFkkoAUVfUBA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UNadeUih2EPkTlvvsqggQoIWx6Sg3YnNQr5-UuS65thXS6LlFaAMtiE4ZNQ_aem_nRJ5xTCIkFBFkkoAUVfUBA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7nGktdOcwR8Ux-YJUoeAiq5Sv8aQMxIMz9mL6Uzcfj__-3fI1eS3x_Q0oZog_aem_avHQ-TSM41z-2EE-K5t2Hw&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4kq-5ZoH038PEnXGDx2-YEic2ifBBMNjCgiF_V_9S_9CDUNgth1336zYFxYA_aem_Ji47Dft0sG1_CBD8MeaBYg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6IrP8aX15Pa-rkMiVI8tysTGJ4JYV0k9eB_gOXX55gQ8jAnR3PCxH23Mk3Jw_aem_9aG-syNGnHpUXsFwjxKG9g&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4zoGn8rIFmv7JvDgTCneUO3QDjlBnJLa4tLAWmW7DkY5V9J5gdAwMzT2MP0g_aem_8fFJ1Ut2iSAsS7e9llo2vA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5G9glBxVZVV_OMRd0bUA1CHrrGNak9ob3RqAOZ20he_HCplBU6netVOfkMHw_aem_Eb6WqV7Wr6q3e0zziM9EBg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR56MT9jW5z0o1CWpwOsRiaFmlbQDoslk12ClcXXRCzAdX_VT6RhCwAbDOzSBA_aem_nc2d2TO4FSOWEj7mQp83Yg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5G9glBxVZVV_OMRd0bUA1CHrrGNak9ob3RqAOZ20he_HCplBU6netVOfkMHw_aem_Eb6WqV7Wr6q3e0zziM9EBg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7UNadeUih2EPkTlvvsqggQoIWx6Sg3YnNQr5-UuS65thXS6LlFaAMtiE4ZNQ_aem_nRJ5xTCIkFBFkkoAUVfUBA&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR56OKSyS7o4LychiXVhA8eiHiXoiKyVqWL4pe34Fz-5Roa-hO98QLBLSEPMaA_aem_f5MZpJFM8ItPaITALc1deg&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4JIn-WKFJzwKSZJTUb-B2m_qUyt25m8bxLFtSBSPp7VuNtK8uX8cD2oEuG0fqtivMdVaC10BtsvarzJK4BfMG4PyAZCq_kHdrVZM8x16Bu21Q_ULDAumlxXPXaK_J1rmGsQ53S1VFHGeJsMZc28DfEEXo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo