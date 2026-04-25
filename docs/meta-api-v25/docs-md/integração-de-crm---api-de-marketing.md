<!-- Fonte: Integração de CRM - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Webhooks da Meta sobre anúncios de cadastro para a gestão do relacionamento com o cliente


Este guia ensina a implementar os Webhooks da Meta sobre anúncios de cadastro para integrar a gestão do relacionamento com o cliente.


## Visão geral


Um usuário deve entrar no app por meio do Login do Facebook e conceder ao app as permissões necessárias para a respectiva Página do Facebook que assinou os Webhooks da Meta sobre cadastros. O Login do Facebook retornará um token de acesso à Página com as permissões necessárias para permitir que o usuário do app visualize as notificações de cadastro enviadas ao seu servidor pela Meta.


## Antes de começar


Você precisará do seguinte:


- Um [ID do app da Meta](https://developers.facebook.com/docs/development/create-an-app)
- O token de acesso à Página de um anunciante, cliente ou usuário do app que possa executar a tarefa [`ADVERTISE` na Página](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks)
- Estas permissões: - `pages_read_engagement` - `pages_manage_metadata` - `pages_show_list` - `ads_management` - `lead_retrieval`
- Um [servidor da web com um ponto de extremidade para receber Webhooks da Meta](https://developers.facebook.com/docs/graph-api/webhooks/getting-started)
- A [assinatura do webhook de geração de cadastros](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-leadgen)
- O [SDK do Facebook para JavaScript](https://developers.facebook.com/docs/javascript/quickstart/) adicionado ao app
- O [Login do Facebook](https://developers.facebook.com/docs/facebook-login) implementado no app


O conteúdo a seguir foi retirado de [https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-leadgen](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-leadgen).


## Webhooks for Leads



Webhooks for Leads can send you real-time notifications of changes to your [Page's Lead ads](https://developers.facebook.com/docs/graph-api/webhooks/reference/page/#leadgen). For example, you can receive real-time updates whenever users click on a lead ad.


First, set up a Page Webhook:


- [Set up your endpoint and configure the Webhooks product](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#set-up-endpoint-and-product).
- [Install your app](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#install-app) using your Facebook page.
 [○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)

## Setting Up Your Endpoint and Webhook Product



Follow our [Getting Started guide](https://developers.facebook.com/docs/graph-api/webhooks/getting-started) to create your endpoint and configure the Webhooks product. During configuration, make sure to choose the **Page** object and subscribe to the **leadgen** field.
 [○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)

## Install Your App



Webhook notifications will only be sent if your Page has installed your Webhooks configured-app, and if the Page has not disabled the **App** platform in its [App Settings](https://www.facebook.com/settings?tab=applications). To get your Page to install the app, have your app send a `POST` request to the Page's [subscribed_apps](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps) edge using the Page's acccess token.


### Requirements



- A Page access token requested from a person who can perform the [ADVERTISE task](https://developers.facebook.com/docs/pages/overview#tasks) on the Page being queried
- The following [permissions](https://developers.facebook.com/docs/permissions/): - `leads_retrieval` - `pages_manage_metadata` - `pages_show_list` - `pages_read_engagement` - `ads_management`


#### Sample Request



*Formatted for clarity*

```
curl -i -X POST "https://graph.facebook.com/{page-id}/subscribed_apps
  ?subscribed_fields=leadgen
  &access_token={page-access-token}"
```


#### Sample Response


```
{
  "success": "true"
}
```


To see which app's your Page has installed, send a `GET` request instead:


#### Sample Request



*Formatted for clarity*

```
curl -i -X GET "https://graph.facebook.com/{page-id}/subscribed_apps
  ?access_token={page-access-token}
```


#### Sample Response


```
{
  "data": [
    {
      "category": "Business",
      "link": "https://my-clever-domain-name.com/app",
      "name": "My Sample App",
      "id": "{page-id}"
    }
  ]
}
```


If your Page has not installed any apps, the API will return an empty data set.


#### Graph API Explorer



If you don't want to install your app programmatically, you can easily do it with the [Graph API Explorer](https://developers.facebook.com/tools/explorer) instead:


- Select your app in the **Application** dropdown menu. This will return your app's access token.
- Click the **Get Token** dropdown and select **Get User Access Token**, then choose the `pages_manage_metadata` permission. This will exchange your app token for a User access token with the `pages_manage_metadata` permission granted.
- Click **Get Token** again and select your Page. This will exchange your User access token for a Page access token.
- Change the operation method by clicking the `GET` dropdown menu and selecting `POST`.
- Replace the default `me?fields=id,name` query with the Page's **id** followed by `/subscribed_apps?subscribed_fields=leadgen`, then submit the query.
 [○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)

## Common Uses



### Getting Page LeadGen Details



Your app can subscribe to a Page's Leads and get notified anytime a change occurs. For example, here's a notification sent when a User clicked on a lead ad.


#### Sample Webhook Response


```
{
   "object": "page",
   "entry": [
       {
           "id": 153125381133,
           "time": 1438292065,
           "changes": [
               {
                   "field": "leadgen",
                   "value": {
                       "leadgen_id": 123123123123,
                       "page_id": 123123123,
                       "form_id": 12312312312,
                       "adgroup_id": 12312312312,
                       "ad_id": 12312312312,
                       "created_time": 1440120384
                   }
               },
               {
                   "field": "leadgen",
                   "value": {
                       "leadgen_id": 123123123124,
                       "page_id": 123123123,
                       "form_id": 12312312312,
                       "adgroup_id": 12312312312,
                       "ad_id": 12312312312,
                       "created_time": 1440120384
                   }
               }
           ]
       }
   ]
}
```
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)

## See Also



- Visit our [Lead Ads Retrieval guide](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving/) to learn how to use the `leadgen_id` from the notification to retrieve data associated with the leads.
 [○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#)Nesta Página[Webhooks da Meta sobre anúncios de cadastro para a gestão do relacionamento com o cliente](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#webhooks-da-meta-sobre-an-ncios-de-cadastro-para-a-gest-o-do-relacionamento-com-o-cliente)[Webhooks for Leads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#webhooks-for-leads)[Setting Up Your Endpoint and Webhook Product](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#set-up-endpoint-and-product)[Install Your App](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#install-app)[Requirements](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#requirements)[Common Uses](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#common-uses)[Getting Page LeadGen Details](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#getting-page-leadgen-details)[See Also](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/quickstart/webhooks-integration#see-also) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jCN7nUZsIszDPUunFzWLpkSKxxWuV3lE2hwWQJ-rxaVC_lxCIB0nDXqamQw_aem_rUEwhonQ6ANufYZQfMivmw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Ctpr6_Shf6ZWWZpStj6teevMF_Npx_hWzhawUWFmHUrDaYU1MVJqwQmud5w_aem_RzZsJRKaMKQMEM7nhm-w1w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dXwRAgGDzZkMjq61qlyLSd7sAcdSjeMMKmAPzdlJ_Om6tGqCb6F3tYGjVmQ_aem_6tTNPt6dAMYmD2MSg9CN8w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jCN7nUZsIszDPUunFzWLpkSKxxWuV3lE2hwWQJ-rxaVC_lxCIB0nDXqamQw_aem_rUEwhonQ6ANufYZQfMivmw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4z5aDufP907RI1oY-7eIAvkM6YXQOTsAIz2jQzCFUvMvQdjV9CNJEAObxwwg_aem_924ixfNgJs1TpGU4O1uRyg&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tfSymWKc1xDy93aG_pAwSrxhjZftO7hQ17t-UA7WEFHyuzW5G3SMKOw2A2A_aem_3xwX0JvOEwaOcPINTr-2Xw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Ctpr6_Shf6ZWWZpStj6teevMF_Npx_hWzhawUWFmHUrDaYU1MVJqwQmud5w_aem_RzZsJRKaMKQMEM7nhm-w1w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tfSymWKc1xDy93aG_pAwSrxhjZftO7hQ17t-UA7WEFHyuzW5G3SMKOw2A2A_aem_3xwX0JvOEwaOcPINTr-2Xw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4z5aDufP907RI1oY-7eIAvkM6YXQOTsAIz2jQzCFUvMvQdjV9CNJEAObxwwg_aem_924ixfNgJs1TpGU4O1uRyg&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wDAbanzVyVPLC03kLDvefnAm_bfH7It47bLVkDKG9nPz6O-IBURIRHQQjlQ_aem_of8LkJvbTDyh4aYOZ6e1ow&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4D9u01SjG9OrjizgMU1VN_txavPaSwf8VYiCVFrUwFId2zvLRpvbQTFXLxYg_aem_VkQObS6aAPPuwr2viVIj6g&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tfSymWKc1xDy93aG_pAwSrxhjZftO7hQ17t-UA7WEFHyuzW5G3SMKOw2A2A_aem_3xwX0JvOEwaOcPINTr-2Xw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dXwRAgGDzZkMjq61qlyLSd7sAcdSjeMMKmAPzdlJ_Om6tGqCb6F3tYGjVmQ_aem_6tTNPt6dAMYmD2MSg9CN8w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ysNYcoevyx7tGb7gV36PrarOSEAJo5vW9Jb7t0Pn-alGhM_rbOtwL-Mw33Q_aem_g5cbRyDdc73KqwVHyL8RRg&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7sdRPA6vMHNwEzdNtGER5AcxOMYYzpjM0WRhC2Z1--Hj3zoCWXPoDiNF1Vgg_aem_ukEFPwkrH00MIGoCGmBFxA&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ysNYcoevyx7tGb7gV36PrarOSEAJo5vW9Jb7t0Pn-alGhM_rbOtwL-Mw33Q_aem_g5cbRyDdc73KqwVHyL8RRg&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tfSymWKc1xDy93aG_pAwSrxhjZftO7hQ17t-UA7WEFHyuzW5G3SMKOw2A2A_aem_3xwX0JvOEwaOcPINTr-2Xw&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wDAbanzVyVPLC03kLDvefnAm_bfH7It47bLVkDKG9nPz6O-IBURIRHQQjlQ_aem_of8LkJvbTDyh4aYOZ6e1ow&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dXwRAgGDzZkMjq61qlyLSd7sAcdSjeMMKmAPzdlJ_Om6tGqCb6F3tYGjVmQ_aem_6tTNPt6dAMYmD2MSg9CN8w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dXwRAgGDzZkMjq61qlyLSd7sAcdSjeMMKmAPzdlJ_Om6tGqCb6F3tYGjVmQ_aem_6tTNPt6dAMYmD2MSg9CN8w&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT66xYtW5wI5zkEG-UwBQkfzJIlvGLqBJECefk4PfigXJqzgzqx6uB2Yzo7U72gWyKzaTVk1DI6HxcdSj3CeQKNtDgpAeSZpesYbZyBZt3Wczc_9I93dvlmXnBDf3_VrJm-6WkpucTnt_mfUlWjlsE4jq68)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão