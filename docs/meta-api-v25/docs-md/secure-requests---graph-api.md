<!-- Fonte: Secure Requests - Graph API.html -->
<!-- URL: https://developers.facebook.com/docs/graph-api/guides/secure-requests -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Secure Graph API Calls



Almost every Graph API call requires an [access token](https://developers.facebook.com/docs/facebook-login/access-tokens/). Malicious developers can steal access tokens and use them to send spam from your app. Meta has automated systems to detect this, but you can help us secure your app. This document covers some of the ways you can improve security in your app.


## Meta Crawler



A number of platform services such as Social Plugins and Open Graph require our systems to be able to reach your web pages. We recognize that there are situations where you might not want these pages on the public web, during testing or for other security reasons.


We've provided information on IP allow lists and User Agent strings for Meta's crawlers in our [Meta Crawler guide](https://developers.facebook.com/docs/sharing/webmasters/crawler).
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)

## Login Security



There are a large number of settings you can change to improve the security of your app. Please see our [Login Security](https://developers.facebook.com/docs/facebook-login/security/) documentation for a checklist of things you can do.


It's also worth looking at our [access token](https://developers.facebook.com/docs/facebook-login/access-tokens/) documentation which covers various architectures and the security trade-offs that you should consider.
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)

## Server Allow List



We also enable you to restrict some of your API calls to come from a list of servers that you have allowed to make calls. Learn more in our [login security](https://developers.facebook.com/docs/facebook-login/security#surfacearea) documentation.
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)

## Social Plugin Confirmation Steps



In order to protect users from unintentionally liking content around the web, our systems will occasionally require them to confirm that they intended to interact with one of our Social Plugins via a "confirm" dialog. This is expected behavior and once the system has verified your site as a good actor, the step will be removed automatically.
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)

## Encryption



When connecting to our servers your client must use TLS and be able to verify a certificate signed using [`sha256WithRSAEncryption`](https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.alvestrand.no%2Fobjectid%2F1.2.840.113549.1.1.11.html%3Ffbclid%3DIwZXh0bgNhZW0CMTEAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6p-S7-mDPHt29FZ8O9tAVKUJAjqMNLgRGSSuOUYScmve3OPgbl0qFaEn2Usg_aem_U5qsNjdHJUdUnyajD_ZWig&h=AT7Y0SioX6yFPMgVPsZor9l2FW5GeFHVYg5ClWaM0_h9mdBdZig9GBMgy-EQOMBGuKzo3lr6ccRJ7uBHoGAWQDHUUjRVaG2a9347o6I1Htyls79sg9n59-zIkCai07SexEjenOct-pCfScRtamJaJ4VlEaA).


Graph API supports TLS 1.2 and 1.3 and non-static RSA cipher suites. We are currently deprecating support for older TLS versions and static RSA cipher suites. Version 16.0 no longer supports TLS versions older than 1.1 or static RSA cipher suites. This change will apply to all API versions on May 3, 2023.
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)

## Verify Graph API Calls with `appsecret_proof`



Access tokens are portable. It's possible to take an access token generated on a client by Meta's SDK, send it to a server and then make calls from that server on behalf of the client. An access token can also be stolen by malicious software on a person's computer or a man in the middle attack. Then that access token can be used from an entirely different system that's not the client and not your server, generating spam or stealing data.


Calls from a server can be better secured by adding a parameter called `appsecret_proof`. The app secret proof is a sha256 hash of your access token, using your app secret as the key. The app secret can be found in your app dashboard in **Settings > Basic**.


If you're using the official PHP SDK, the `appsecret_proof` parameter is automatically added.


### Generate the Proof



The following code example is what the call looks like in PHP:

```
$appsecret_proof= hash_hmac('sha256', $access_token, $app_secret);
```


### Add the Proof



You add the result as an `appsecret_proof` parameter to each call you make:

```
curl \
  -F 'access_token=<access_token>' \
  -F 'appsecret_proof=<app secret proof>' \
  -F 'batch=[{"method":"GET", "relative_url":"me"},{"method":"GET", "relative_url":"me/friends?limit=50"}]' \
  https://graph.facebook.com
```


### Require the Proof



To enable **Require App Secret** for all your API calls, go to the Meta App Dashboard and click **App Settings > Advanced** in the left side menu. Scroll to the **Security** section, and click the **Require App Secret** toggle.


If this setting is enabled, all client-initiated calls must be proxied through your backend where the `appsecret_proof` parameter can be added to the request before sending it to the Graph API, or the call will fail.
 [○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)[○](https://developers.facebook.com/docs/graph-api/guides/secure-requests#)On This Page[Secure Graph API Calls](https://developers.facebook.com/docs/graph-api/guides/secure-requests#secure-graph-api-calls)[Meta Crawler](https://developers.facebook.com/docs/graph-api/guides/secure-requests#meta-crawler)[Login Security](https://developers.facebook.com/docs/graph-api/guides/secure-requests#login-security)[Server Allow List](https://developers.facebook.com/docs/graph-api/guides/secure-requests#server-allow-list)[Social Plugin Confirmation Steps](https://developers.facebook.com/docs/graph-api/guides/secure-requests#confirm_steps)[Encryption](https://developers.facebook.com/docs/graph-api/guides/secure-requests#encryption)[Verify Graph API Calls with appsecret_proof](https://developers.facebook.com/docs/graph-api/guides/secure-requests#appsecret_proof)[Generate the Proof](https://developers.facebook.com/docs/graph-api/guides/secure-requests#generate-the-proof)[Add the Proof](https://developers.facebook.com/docs/graph-api/guides/secure-requests#add-the-proof)[Require the Proof](https://developers.facebook.com/docs/graph-api/guides/secure-requests#require-the-proof) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77Qocg2J9JQQCKLLjpJbT69Ovrzv4RXcPS__dXUkkuuqFr-PPj52wQ4_q5aQ_aem_3XrMCDoMSZgKMz0TcFqaaw&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5zknoeBsliNUpkI5ZmqHxWFFrML5uJQaJT9Veuhb3wVGtp1Fvicbwzg211Uw_aem_tiUnYleMahF_rLf8SD6DEQ&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6T65XHQ-nGdym99XB2kn5hapOdcaQKeldV61NYWdf22gYvl2Ue2QWpozMIZw_aem_c85NiqB1XwIpfhmDeQ7_aA&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5w1SHtzbqLXXKuX8C4Xm_hfH6jl0anHVTVq-iQuiDfjClsbdqn7NwtyDJTIw_aem_sonBmFjYvaJ_zHXKWbiXWw&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6T65XHQ-nGdym99XB2kn5hapOdcaQKeldV61NYWdf22gYvl2Ue2QWpozMIZw_aem_c85NiqB1XwIpfhmDeQ7_aA&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eNyGKrj8ED1frbh6s_F67k2j8lVNwQqUqJeHckbUbytRgANF54Kx0Wkq_Pg_aem_Cin8tytctvVoLsOtIzNzFg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eNyGKrj8ED1frbh6s_F67k2j8lVNwQqUqJeHckbUbytRgANF54Kx0Wkq_Pg_aem_Cin8tytctvVoLsOtIzNzFg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR77Qocg2J9JQQCKLLjpJbT69Ovrzv4RXcPS__dXUkkuuqFr-PPj52wQ4_q5aQ_aem_3XrMCDoMSZgKMz0TcFqaaw&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eNyGKrj8ED1frbh6s_F67k2j8lVNwQqUqJeHckbUbytRgANF54Kx0Wkq_Pg_aem_Cin8tytctvVoLsOtIzNzFg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR51qbK8QaH_t-e8LDOdIU6qSgO3w12Cbn0V0XELb8X4h65pc-RcNN5Rt0hhvg_aem_DL641i3nBARc5RSyxduo0g&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5zknoeBsliNUpkI5ZmqHxWFFrML5uJQaJT9Veuhb3wVGtp1Fvicbwzg211Uw_aem_tiUnYleMahF_rLf8SD6DEQ&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5q4FDfQ4BBAgV_1I-l_BG9bnPi2PJ4YVjV20m4qbLGDokRifCLnUmCi9ChiQ_aem_HNFYKecmGs49UkD1rMjivQ&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5w1SHtzbqLXXKuX8C4Xm_hfH6jl0anHVTVq-iQuiDfjClsbdqn7NwtyDJTIw_aem_sonBmFjYvaJ_zHXKWbiXWw&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6VQt0LCYkIUX3zfgBGEpb8Irhy_FG1LGOInejYtg-4WZJ2I_5Lg0MXkowPkg_aem_5wUkYeYAeee1fYsKPJqBtg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR51qbK8QaH_t-e8LDOdIU6qSgO3w12Cbn0V0XELb8X4h65pc-RcNN5Rt0hhvg_aem_DL641i3nBARc5RSyxduo0g&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7eNyGKrj8ED1frbh6s_F67k2j8lVNwQqUqJeHckbUbytRgANF54Kx0Wkq_Pg_aem_Cin8tytctvVoLsOtIzNzFg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR51qbK8QaH_t-e8LDOdIU6qSgO3w12Cbn0V0XELb8X4h65pc-RcNN5Rt0hhvg_aem_DL641i3nBARc5RSyxduo0g&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6VQt0LCYkIUX3zfgBGEpb8Irhy_FG1LGOInejYtg-4WZJ2I_5Lg0MXkowPkg_aem_5wUkYeYAeee1fYsKPJqBtg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7e0Apkp1qmXi7lEwaKf30sCNluBZlYCvTVt0JymSO_Q5XJcv691kuUB2Kcag_aem_Pk4yMfH9ZKcVjDNpSzFUVg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7e0Apkp1qmXi7lEwaKf30sCNluBZlYCvTVt0JymSO_Q5XJcv691kuUB2Kcag_aem_Pk4yMfH9ZKcVjDNpSzFUVg&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5G_S8IZbazvvZh5AORfnQgXigzwMCvZGBLBQXwHwjbLBQ05AO2_aoOSSuRklt004hZ1mP_69g0Q1uqx9Tp7DGmn_isiypdpnapP4nMmWKr0q0pToDpVSEJ5lyI3DjzRI2z-AewkCr8ZdtD8HtAcbcQgnc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Was this document helpful?YesNo