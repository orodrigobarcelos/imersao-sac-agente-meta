<!-- Fonte: Standard Enhancements for Advantage+ Creative  - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Standard Enhancements for Advantage+ Creative



Starting with Marketing API v22.0, opting in or out of standard enhancements will no longer be available. Instead, you can opt in or out of individual Advantage+ Creative features by following the instructions in [Get Started with Advantage+ Creative](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started). Opting in or out of sub-features within the standard enhancements bundle will have the same effect as previously opting in or out of standard enhancements.


The sub-features within the standard enhancement bundle for single image ads include `image_template`, `image_touchups`, `text_optimizations`, and `inline_comment`. For single video ads, the sub-features are `video_auto_crop`, `text_optimizations`, and `inline_comment`.


Standard enhancements is for ads using a single image, video, or carousel. It automatically creates multiple variations of your ad and shows a personalized variation to each Account Center account based on what they're most likely to respond to. You can create ads with standard enhancements using the `TRAFFIC` or `CONVERSIONS` objectives to help drive performance and deliver more tailored ads to each Account Center account. For more information, please see [About Advantage+ creative](https://www.facebook.com/business/help/297506218282224).


## API Support for Standard Enhancements



### Standalone Creative Creation



#### Before:


```
curl -X POST \
  -F 'name="My creative title"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_user_id": "<IG_USER_ID>",
       "link_data": {
             "link": "www.google.com",
      }
     }' \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### After (new fields are in bold):


```
curl -X POST \
  -F 'name="My creative title"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "instagram_user_id": "<IG_USER_ID>",
       "link_data": {
             "link": "www.google.com",
      }
     }' \
  -F 'degrees_of_freedom_spec={
      "creative_features_spec": {
        "standard_enhancements": {
          "enroll_status": "OPT_IN"
        }
      }
    }' \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Ad Creation



#### Before:


```
curl -X POST \
  -F 'creative={
    "object_story_spec": {
      "page_id": "<PAGE_ID>",
      "link_data": {
        "link": "<WEBSITE_URL>",
      }
    },
  }' \
  -F "adset_id=<ADSET_ID>" \
  -F "name=New Ad" \
  -F "status=PAUSED" \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### After (new fields are in bold):


```
curl -X POST \
  -F 'creative={
    "object_story_spec": {
      "page_id": "<PAGE_ID>",
      "link_data": {
        "link": "<WEBSITE_URL>",
      }
    },
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "standard_enhancements": {
          "enroll_status": "OPT_IN"
        }
      }
    }
  }' \
  -F "adset_id=<ADSET_ID>" \
  -F "name=New Ad" \
  -F "status=PAUSED" \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


For more details, see [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative#create_example).


### Parameters



| Name | Description |
| --- | --- |
| degrees_of_freedom_spec | Specifies the types of transformations that are enabled for the given creative. For more information, see Ad Creative Degrees Of Freedom Spec, Reference . |


The following features can be opted in the `creative_features_spec`:


| Name | Description |
| --- | --- |
| standard_enhancements | Basic set of enhancements to optimize your ad creative and improve performance. This can include: Automatically adjusting the aspect ratio of your image or video; Applying a template to your image to help it better fit certain ad placements; Displaying relevant Meta comments below your ad. The enroll_status field can be set to OPT_IN or OPT_OUT . For more details, see Ad Creative Features Details, Reference . |

[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#)

## Learn More



### Marketing API Reference



- [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative#fields) - [Ad Creative Degrees Of Freedom Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-degrees-of-freedom-spec/) - [Ad Creative Features Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-features-spec/) - [Ad Creative Feature Details](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-feature-details/) - [Ad Creative Object Story Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/)
 [○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#)Nesta Página[Standard Enhancements for Advantage+ Creative](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#standard-enhancements-for-advantage--creative)[API Support for Standard Enhancements](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#api-support)[Standalone Creative Creation](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#standalone-creative-creation)[Ad Creation](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#ad-creation)[Parameters](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#parameters)[Learn More](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#learn-more)[Marketing API Reference](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements#marketing-api-reference) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4s5_uotan8rUCeybSlyUadtXXL9H_-58pKMHZEPUt59tmatckXQXh6bcqnjA_aem_mhLu8NEIXuJYxrcFxGReuw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Ah3izRIlpph9JAfGyF3hJJqParo4RC2dbmLdHoD0ZD98svKkBuWHF3kBCqw_aem_KC1d2wmC0KMvQuRW_IbavQ&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4s5_uotan8rUCeybSlyUadtXXL9H_-58pKMHZEPUt59tmatckXQXh6bcqnjA_aem_mhLu8NEIXuJYxrcFxGReuw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TVtNuFq0J_-RqtWleozmwdhwYNxFBAmdMk9Tr79q_W3BjseuYFj6AOos26w_aem_xFMKPh9aNBE3XCV5iQAjNw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5iq6isy7GqQWjCTcfX197ZUtbe8LGn-5Br45t8Fs9BK9D-eFPRy2CS402Sgw_aem_QwzdbxXfVkLGREutVDYkhw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4s5_uotan8rUCeybSlyUadtXXL9H_-58pKMHZEPUt59tmatckXQXh6bcqnjA_aem_mhLu8NEIXuJYxrcFxGReuw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Ah3izRIlpph9JAfGyF3hJJqParo4RC2dbmLdHoD0ZD98svKkBuWHF3kBCqw_aem_KC1d2wmC0KMvQuRW_IbavQ&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sHBGmJujcpFLxV8kY750vG1BVY1PqzZbvA6NFFTcyOxlPtLAp78aVkQ7Wmw_aem_iSVyJVyHh6_XiXKOAf1yrQ&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6WGPJcBqC05Kb2Hii5Adcd29yMtccIVdzr5I01SzZbYUMOkaK5B03jL8lGZQ_aem_3wsJEQ2gErEV1wRNC6Vn4w&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45QNRdRWMi2pRCc_kMKNnayU1QUt0Wy8EoDWiVefnew5x2cS6bPGZcwr_AWA_aem_7HSYSsENZSdOvG8AT1nFNw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45QNRdRWMi2pRCc_kMKNnayU1QUt0Wy8EoDWiVefnew5x2cS6bPGZcwr_AWA_aem_7HSYSsENZSdOvG8AT1nFNw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sHBGmJujcpFLxV8kY750vG1BVY1PqzZbvA6NFFTcyOxlPtLAp78aVkQ7Wmw_aem_iSVyJVyHh6_XiXKOAf1yrQ&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wtDNxUtpc8KvC2ulJ7vsuKgBH0OQJ6gmIhf7gKqiZ_nIRJ7F7O_JJZM-d-w_aem_uI7QmE_m1nM0MGiVtsKHtg&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TVtNuFq0J_-RqtWleozmwdhwYNxFBAmdMk9Tr79q_W3BjseuYFj6AOos26w_aem_xFMKPh9aNBE3XCV5iQAjNw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5iq6isy7GqQWjCTcfX197ZUtbe8LGn-5Br45t8Fs9BK9D-eFPRy2CS402Sgw_aem_QwzdbxXfVkLGREutVDYkhw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5gQkYaXRLX8Pg3vqfCLXKZt2HhR9gBBKakE5qQWClO9uU8vwYrvKlxuZL7_g_aem_vquU9B3e2RUsdSJ7UInwlw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6WGPJcBqC05Kb2Hii5Adcd29yMtccIVdzr5I01SzZbYUMOkaK5B03jL8lGZQ_aem_3wsJEQ2gErEV1wRNC6Vn4w&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TVtNuFq0J_-RqtWleozmwdhwYNxFBAmdMk9Tr79q_W3BjseuYFj6AOos26w_aem_xFMKPh9aNBE3XCV5iQAjNw&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Ah3izRIlpph9JAfGyF3hJJqParo4RC2dbmLdHoD0ZD98svKkBuWHF3kBCqw_aem_KC1d2wmC0KMvQuRW_IbavQ&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6WGPJcBqC05Kb2Hii5Adcd29yMtccIVdzr5I01SzZbYUMOkaK5B03jL8lGZQ_aem_3wsJEQ2gErEV1wRNC6Vn4w&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6FhJNHE6z9gJHOKnMxg3-7SqBaKRWr3gNUdqWngZfbZz-LZ9ViPsgdx3ER0JtI8XwSUiorCzTSvpk2DeW-RUzaz4lj4cRtWGZcKBfCJtXdekQ6cCZb5c0Sl4z-i2iEwS_s7MRaFZoroHifp-f5LMiTh-I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão