<!-- Fonte: Work Email Validation - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Lead Ads Work Email Validation



You can enable a work email validation feature in lead ads to ensure people enter their work email address before submitting the form.


This feature can be enabled in one of two ways: in the [ad creative](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#option-1), or in the [lead gen form](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#option-2).


### Limitations



- Both methods require the lead gen form to include a work email question.


## Option 1: Enable the Work Email Validation in the Ad Creative



### Step 1: Create a leadgen form containing a work email question



#### Example request


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "access_token": "<PAGE_ACCESS_TOKEN>",
    "name": "<FORM_NAME>",
    "questions": [{
      "type": "FULL_NAME",
      "key": "full_name"
    },
    {
      "type": "PHONE",
      "key": "phone"
    },
    {
      "type": "WORK_EMAIL",
      "key": "work_email"
    }],
    "legal_content_id": "<CONTENT_ID>",
    "privacy_policy_optional": "true",
    "follow_up_action_url": "http://www.meta.com/"
  }' \
https://graph.facebook.com/v25.0/<PAGE_ID>/leadgen_forms
```


See [Lead Forms for Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create/#lead_form) for more information.


### Step 2: Create an ad creative with the work email validation feature enabled



Create an ad creative with the `asset_feed_spec.lead_gen_configuration.is_work_email_enforcement_enabled` parameter set to `true`.


The [Ad Account Ad Creatives reference](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adcreatives) lists all the fields for an ad creative object. You can find `lead_gen_configuration` under the `asset_feed_spec` parameter.


#### Example request


```
curl -X POST \
  -F 'access_token=<ACCESS_TOKEN>' \
  -F 'asset_feed_spec={
    "lead_gen_configuration": {
    "is_work_email_enforcement_enabled": true
    }
  }' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "link_data": {
      "message": "Check out our new product!",
      "link": "<LINK_URL>",
      "caption": "<CAPTION>",
      "call_to_action": {
        "type": "SIGN_UP",
        "value": {
          "lead_gen_form_id": "<LEAD_GEN_FORM_ID>"
        }
      }
    }
  }'
https://graph.facebook.com/v25.0/act_<ACCOUNT_ID>/adcreatives
```


Upon success, the response will return the newly created ad creative's ID.


See [Create an Ad Creative](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) for more information.


### Step 3: Create an ad with the returned ad creative ID



See [Create an Ad](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad) for more information.
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#)

## Option 2: Enable the Work Email Validation in a Lead Gen Form



### Step 1: Create a leadgen form containing a work email question



Create the leadgen form with the `should_enforce_work_email` parameter set to `true`.


The [Page Leadgen Forms reference](https://developers.facebook.com/docs/graph-api/reference/page/leadgen_forms) lists all the parameters for leadgen forms.


#### Example request


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "access_token": "<PAGE_ACCESS_TOKEN>",
    "name": "<FORM_NAME>",
    "questions": [{
      "type": "FULL_NAME",
      "key": "full_name"
    },
    {
      "type": "PHONE",
      "key": "phone"
    },
    {
      "type": "WORK_EMAIL",
      "key": "work_email"
    }],
    "should_enforce_work_email": "true",
    "legal_content_id": "<CONTENT_ID>",
    "privacy_policy_optional": "true",
    "follow_up_action_url": "http://www.meta.com/"
  }' \
https://graph.facebook.com/v25.0/<PAGE_ID>/leadgen_forms
```


Upon success, the response will return a leadgen form ID.


See [Lead Forms for Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create/#lead_form) for more information.


### Step 2: Create an ad creative with the returned leadgen form ID



#### Example request


```
curl -X POST \
  -F 'access_token=<ACCESS_TOKEN>' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "link_data": {
      "message": "Check out our new product!",
      "link": "<LINK_URL>",
      "caption": "<CAPTION>",
      "call_to_action": {
        "type": "SIGN_UP",
        "value": {
          "lead_gen_form_id": "<LEAD_GEN_FORM_ID>"
        }
      }
    }
  }' \
https://graph.facebook.com/v25.0/act_<ACCOUNT_ID>/adcreatives
```


Upon successful creation, the response will return the newly created ad creative's ID.


See [Lead Forms for Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create#adcreative) and [Create an Ad Creative](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) for more information.


### Step 3: Create an ad with the returned ad creative ID



See [Create an Ad](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad) for more information.
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#)

## Learn More



- [Business Help Center: Enable the work email validation feature to help improve lead quality](https://www.facebook.com/business/help/10003852069627862)
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#)[○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#)Nesta Página[Lead Ads Work Email Validation](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#lead-ads-work-email-validation)[Option 1: Enable the Work Email Validation in the Ad Creative](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#option-1)[Step 1: Create a leadgen form containing a work email question](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-1--create-a-leadgen-form-containing-a-work-email-question)[Step 2: Create an ad creative with the work email validation feature enabled](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-2--create-an-ad-creative-with-the-work-email-validation-feature-enabled)[Step 3: Create an ad with the returned ad creative ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-3--create-an-ad-with-the-returned-ad-creative-id)[Option 2: Enable the Work Email Validation in a Lead Gen Form](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#option-2)[Step 1: Create a leadgen form containing a work email question](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-1--create-a-leadgen-form-containing-a-work-email-question-2)[Step 2: Create an ad creative with the returned leadgen form ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-2--create-an-ad-creative-with-the-returned-leadgen-form-id)[Step 3: Create an ad with the returned ad creative ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#step-3--create-an-ad-with-the-returned-ad-creative-id-2)[Learn More](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/work-email-validation#learn-more) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Z5JuPr2Nctb-lEZybViITWPKVCHa0dllkSLNiiv9tER_zjuC39L0MQkK7eQ_aem_I-Wjb4EcJmwqWVmTtN83Ig&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_ufkklj7Gqjz_ePV0gZx1JIID47kZV-QkQbDw3CqjKSdT-fndGPgat0zNQg_aem_wg1T5uvO_hWVuz6Ozp6mBw&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR54JxkbEhF7Emr14tSWLSB6FWwQi-viAor7317I8n_GEmZlws9yLL4orACgGw_aem_S6x3W6fO6po44ikHWSNU0Q&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Z5JuPr2Nctb-lEZybViITWPKVCHa0dllkSLNiiv9tER_zjuC39L0MQkK7eQ_aem_I-Wjb4EcJmwqWVmTtN83Ig&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR49driefZkGjehASbvUZh-YkB9GL2EtkDmmq4wqQG4uHgPn1ZKFtzQwvzodRw_aem_3dBswy6ZmJl2gLiUdMjIdQ&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4odCJNRbqldQyiIZ51UAxfT2-tvw-m8QCJDtN1nuAZSQPhuwvZG3MAXixJ7g_aem_M7AKPfBy75EZ9hPC756H8w&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vsb1QZ1r5OVeuNWlZhN6HarCrj6LXRGE14Zo742MGMvFpaPnrvL7gIh3ijA_aem_2PN8XIYtwcD-cn-W48Itzw&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR54JxkbEhF7Emr14tSWLSB6FWwQi-viAor7317I8n_GEmZlws9yLL4orACgGw_aem_S6x3W6fO6po44ikHWSNU0Q&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR54JxkbEhF7Emr14tSWLSB6FWwQi-viAor7317I8n_GEmZlws9yLL4orACgGw_aem_S6x3W6fO6po44ikHWSNU0Q&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6cAaywWlmoVp_p_Xtyv_X7CTGFj_qje5ICjdAaybTSRSaUt0RScMROaZaIfw_aem_Y7gVFRg_NcYmBpGgGHM1uQ&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vsb1QZ1r5OVeuNWlZhN6HarCrj6LXRGE14Zo742MGMvFpaPnrvL7gIh3ijA_aem_2PN8XIYtwcD-cn-W48Itzw&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6cAaywWlmoVp_p_Xtyv_X7CTGFj_qje5ICjdAaybTSRSaUt0RScMROaZaIfw_aem_Y7gVFRg_NcYmBpGgGHM1uQ&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4odCJNRbqldQyiIZ51UAxfT2-tvw-m8QCJDtN1nuAZSQPhuwvZG3MAXixJ7g_aem_M7AKPfBy75EZ9hPC756H8w&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dIODx-HJAByfRc2suR-WKUfUHHY0KempS0C-hq5zKOOtkqkx4qP8cCi7C5g_aem_Lj6V7JyD5hUVF3B3whlhmg&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR49driefZkGjehASbvUZh-YkB9GL2EtkDmmq4wqQG4uHgPn1ZKFtzQwvzodRw_aem_3dBswy6ZmJl2gLiUdMjIdQ&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT49pAvge41LcdOrxtmL6fJyZCNBoZiW08Hw9wv-8UmY66sf9JWs9iS7BIbpilQgboZ1g0GA-WU47ELwW74unbP19PGzNsmHog4JZUG1eDV26R3EBbGpuqzWXjAuDpo0rpfF2RJERsSA7A_04ZnzOyX8TyI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão