<!-- Fonte: Verificação por senha descartável via smartphone - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Phone One-Time Passcode Verification for Lead Ads



Phone one-time passcodes (OTP) can be implemented for lead ads in one of two ways: in the [ad creative](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#option-1), or in the [leadgen form](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#option-2).


### Limitations



- Both methods require the leadgen form to include a phone number question.


## Option 1: Enable the Phone OTP in the Ad Creative



### Step 1: Create a leadgen form containing a phone question



#### Example request


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "access_token": "<PAGE_ACCESS_TOKEN>",
    "name": "<FORM_NAME>",
    "questions": [
      {
        "type": "FULL_NAME",
        "key": "full_name"
      },
      {
        "type": "PHONE",
        "key": "phone"
      }],
    "legal_content_id": "<CONTENT_ID>",
    "privacy_policy_optional": "true",
    "follow_up_action_url": "http://www.meta.com/"
  }' \
https://graph.facebook.com/v25.0/<PAGE_ID>/leadgen_forms
```


See [Lead Forms for Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create/#lead_form) for more information.


### Step 2: Create an ad creative with the SMS verification type



To enable SMS verification, set the `asset_feed_spec.lead_gen_configuration.verification_type` parameter to `SMS`.

```
asset_feed_spec.lead_gen_configuration.verification_type = 'SMS'
```


The [Ad Account Ad Creatives reference](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adcreatives) lists all the fields for an ad creative object. You can find `lead_gen_configuration` under the `asset_feed_spec` parameter.


#### Example request


```
curl -X POST \
  -F 'access_token=<ACCESS_TOKEN>' \
  -F 'asset_feed_spec={
    "lead_gen_configuration": {
      "verification_type": 'SMS'
    }
  }' \
  -F 'object_story_spec={
    "page_id": "<PAGE_ID>",
    "link_data": {
      "message": "Check out our new product!",
      "link": "https://www.example.com/product",
      "caption": "https://www.example.com/product",
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


Upon success, the response will return the newly created ad creative's ID.


See [Create an Ad Creative](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative) for more information.


### Step 3: Create an ad with the returned ad creative ID



See [Create an Ad](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad) for more information.
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#)

## Option 2: Enable the Phone OTP in a Leadgen Form



### Step 1: Create a leadgen form containing a phone question



Create the leadgen form with the `is_phone_sms_verify_enabled` parameter set to `true`.


The [Page Leadgen Forms reference](https://developers.facebook.com/docs/graph-api/reference/page/leadgen_forms) lists all the parameters for leadgen forms.


#### Example request


```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "access_token": "<PAGE_ACCESS_TOKEN>",
    "name": "<FORM_NAME>",
    "questions": [
      {
        "type": "FULL_NAME",
        "key": "full_name"
      },
      {
        "type": "PHONE",
        "key": "phone"
      }],
    "is_phone_sms_verify_enabled": "true",
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
      "link": "https://www.example.com/product",
      "caption": "https://www.example.com/product",
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
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#)

## Learn More



- [Lead Forms for Ads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/create)
- [Create an Ad Creative](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative)
- [Create an Ad](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad)
- [Ad Account Ad Creatives reference](https://developers.facebook.com/docs/marketing-api/reference/ad-account/adcreatives)
- [Page Leadgen Forms reference](https://developers.facebook.com/docs/graph-api/reference/page/leadgen_forms)
 [○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#)[○](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#)Nesta Página[Phone One-Time Passcode Verification for Lead Ads](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#phone-one-time-passcode-verification-for-lead-ads)[Option 1: Enable the Phone OTP in the Ad Creative](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#option-1)[Step 1: Create a leadgen form containing a phone question](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-1--create-a-leadgen-form-containing-a-phone-question)[Step 2: Create an ad creative with the SMS verification type](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-2--create-an-ad-creative-with-the-sms-verification-type)[Step 3: Create an ad with the returned ad creative ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-3--create-an-ad-with-the-returned-ad-creative-id)[Option 2: Enable the Phone OTP in a Leadgen Form](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#option-2)[Step 1: Create a leadgen form containing a phone question](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-1--create-a-leadgen-form-containing-a-phone-question-2)[Step 2: Create an ad creative with the returned leadgen form ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-2--create-an-ad-creative-with-the-returned-leadgen-form-id)[Step 3: Create an ad with the returned ad creative ID](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#step-3--create-an-ad-with-the-returned-ad-creative-id-2)[Learn More](https://developers.facebook.com/docs/marketing-api/lead-ads/enable-quality-features/phone-otp#learn-more) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iyWkZRSqaQTxHVsxmcQbq1MBc3TeZvtXuOoduYIq-8uoMrpadjtFkgtBQHg_aem_q82mja1xNcSAPEw3Yx6Y1A&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o7krv_AXP7Q0mAyszkUX0r25ehqZkYY7KAxQ8PyyE8clov2aWVa5TeLQsqQ_aem_7zj1SYV-NQ7oFOz3yrWZyA&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4txRLYHujN13ooSoeXup_Kn61f_b9brPFF0RNUYE9IELFc_i3GlUfLCwfSqg_aem_V7DFICbVZdB6_aep26cVgQ&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l-I13aa8Hvc0LNgo7tB2b5l9v3Xl34VmL3nuuX2vqjMrP2DR0-3mb2A97NA_aem_g34y7k6NPhMUCO_adQdeIQ&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62BoDankuqaTT5Oa7ELvrKv0_Bg786CMozsFMEmRygIfbkciI2gc6-W5wZjQ_aem_Xs11l5KIrdu1OgTe9nh0RQ&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6wsvUsEtH5SiYW54hqT9DR4vnaw0q9Nvd68-kBrGtlitl8uDnDOb_3I3dI1A_aem_8LY2eEgvx8tlVo7e7dq7Tg&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6CmeJNr6cYQTHzuCurDVanfNzS0S3dG05wM1BRb5nJaiDBcOZS6M-tkme3ag_aem_McnKPH97nuV4bct0SUbbUw&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Upxpj9eUQSysdBCWpOBKzInSidJiRa1Ygb7I4Qnf6fLQ5rhaR-WOjdaFtXA_aem_eVzMXTzGD2IgBWjbu-OoTg&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gK_7xjzsuPTpv1mjjK0CrE0DshB5LIS9qfOVR_SbiPVoqqDZNUeAYChcTvw_aem_j-bolyKuvvlPjfClDHh61g&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iyWkZRSqaQTxHVsxmcQbq1MBc3TeZvtXuOoduYIq-8uoMrpadjtFkgtBQHg_aem_q82mja1xNcSAPEw3Yx6Y1A&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iyWkZRSqaQTxHVsxmcQbq1MBc3TeZvtXuOoduYIq-8uoMrpadjtFkgtBQHg_aem_q82mja1xNcSAPEw3Yx6Y1A&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l-I13aa8Hvc0LNgo7tB2b5l9v3Xl34VmL3nuuX2vqjMrP2DR0-3mb2A97NA_aem_g34y7k6NPhMUCO_adQdeIQ&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iyWkZRSqaQTxHVsxmcQbq1MBc3TeZvtXuOoduYIq-8uoMrpadjtFkgtBQHg_aem_q82mja1xNcSAPEw3Yx6Y1A&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o7krv_AXP7Q0mAyszkUX0r25ehqZkYY7KAxQ8PyyE8clov2aWVa5TeLQsqQ_aem_7zj1SYV-NQ7oFOz3yrWZyA&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o7krv_AXP7Q0mAyszkUX0r25ehqZkYY7KAxQ8PyyE8clov2aWVa5TeLQsqQ_aem_7zj1SYV-NQ7oFOz3yrWZyA&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Upxpj9eUQSysdBCWpOBKzInSidJiRa1Ygb7I4Qnf6fLQ5rhaR-WOjdaFtXA_aem_eVzMXTzGD2IgBWjbu-OoTg&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7iyWkZRSqaQTxHVsxmcQbq1MBc3TeZvtXuOoduYIq-8uoMrpadjtFkgtBQHg_aem_q82mja1xNcSAPEw3Yx6Y1A&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7gK_7xjzsuPTpv1mjjK0CrE0DshB5LIS9qfOVR_SbiPVoqqDZNUeAYChcTvw_aem_j-bolyKuvvlPjfClDHh61g&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o7krv_AXP7Q0mAyszkUX0r25ehqZkYY7KAxQ8PyyE8clov2aWVa5TeLQsqQ_aem_7zj1SYV-NQ7oFOz3yrWZyA&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Upxpj9eUQSysdBCWpOBKzInSidJiRa1Ygb7I4Qnf6fLQ5rhaR-WOjdaFtXA_aem_eVzMXTzGD2IgBWjbu-OoTg&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Mkanp5Ly70SYw9hwEYbsysoo_GcvuQphH7iUU7n8L8QsEP5ygLdjYuYHEl6RvU3V_XyIBsl_F51oKpeIMCMTm_GF07aCs4xb1SbZpoYVtEuXFDGD5xXRYkP_d1-XySX4awW5neXt0LS53KWOAG4IG_OU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão