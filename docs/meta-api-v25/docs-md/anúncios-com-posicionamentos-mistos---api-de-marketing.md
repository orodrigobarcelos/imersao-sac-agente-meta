<!-- Fonte: Anúncios com posicionamentos mistos - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/guides/mixed-placements-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios com posicionamentos mistos


É possível criar um conjunto de anúncios com "posicionamento misto" que seja veiculado em posicionamentos do Facebook e no stream do Instagram. Todos os criativos usados pelos anúncios nesse conjunto funcionarão em ambas as plataformas. Forneça diferentes [especificações de corte](https://developers.facebook.com/docs/marketing-api/image-crops/) para a mesma imagem, com 100x100 ou 191x100 para o Instagram e 100x100 para o Facebook. Ou use imagens diferentes para o Facebook e o Instagram.


O Instagram ignorará a especificação de corte de imagem `191x100` na criação do anúncio, a menos que você use `platform_customizations`.


## Começar


Gere o criativo do anúncio com a imagem que você quer usar no Facebook, incluindo Facebook para desktop, dispositivos móveis, Audience Network e assim por diante. Depois, forneça uma imagem diferente como substituição apenas para o Instagram, usando o parâmetro `platform_customizations`.

```
use FacebookAds\Object\AdCreative;
use FacebookAds\Object\AdCreativeLinkData;
use FacebookAds\Object\Fields\AdCreativeLinkDataFields;
use FacebookAds\Object\AdCreativeObjectStorySpec;
use FacebookAds\Object\Fields\AdCreativeObjectStorySpecFields;
use FacebookAds\Object\Fields\AdCreativeFields;

$link_data = new AdCreativeLinkData();
$link_data->setData(array(
AdCreativeLinkDataFields::MESSAGE => 'Great looking SXT handbags in store. #prettybag',
AdCreativeLinkDataFields::LINK => 'http://example.com',
AdCreativeLinkDataFields::IMAGE_HASH => '<IMAGE_HASH>',
AdCreativeLinkDataFields::CAPTION => 'www.example.com',
AdCreativeLinkDataFields::CALL_TO_ACTION => array(
  'type' => 'LEARN_MORE',
  'value' =>array(
    'link' => 'http://example.com',
  )
),
));

$object_story_spec = new AdCreativeObjectStorySpec();
$object_story_spec->setData(array(
AdCreativeObjectStorySpecFields::PAGE_ID => <PAGE_ID>,
AdCreativeObjectStorySpecFields::instagram_user_id => <IG_USER_ID>,
AdCreativeObjectStorySpecFields::LINK_DATA => $link_data,
));

$platform_customizations = array(
  'instagram' => array(
    'image_url' => 'sample.com/ig-friendly-image.jpg',
    'image_crops' => array(
      '100x100'=> array(array(200,90),array(900,790))
    ),
));

$creative = new AdCreative(null, 'act_<AD_ACCOUNT_ID>');

$creative->setData(array(
AdCreativeFields::NAME => 'Instagram only creative',
AdCreativeFields::OBJECT_STORY_SPEC => $object_story_spec,
'platform_customizations' => $platform_customizations,
));

$creative->create();
```

```
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData

link_data = LinkData()
link_data[LinkData.Field.message] = 'Great looking SXT handbags in store. #prettybag'
link_data[LinkData.Field.link] = 'http://example.com'
link_data[LinkData.Field.caption] = 'www.example.com'
link_data[LinkData.Field.image_hash] = '<IMAGE_HASH>'

call_to_action = {
  'type': 'LEARN_MORE',
}
call_to_action['value'] = {
  'link':'http://example.com',
}

link_data[LinkData.Field.call_to_action] = call_to_action

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = <PAGE_ID>
object_story_spec[ObjectStorySpec.Field.instagram_user_id] = <IG_USER_ID>
object_story_spec[ObjectStorySpec.Field.link_data] = link_data

platform_customizations = {
  'instagram': {
      'image_url': 'sample.com/ig-friendly-image.jpg',
      'image_crops': {'100x100':[[200,90],[900,790]],}
  }
}

creative = AdCreative(parent_id='act_&lt;AD_ACCOUNT_ID&gt;')
creative[AdCreative.Field.name] = 'Instagram only creative'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative['platform_customizations'] = platform_customizations
creative.remote_create()
```

```
curl \
-F 'name=Instagram only creative' \
-F 'object_story_spec={
   "page_id":<PAGE_ID>,
   "instagram_user_id":<IG_USER_ID>,
   "link_data":{
       "call_to_action":{
           "type":"LEARN_MORE",
           "value":{
               "link":"http://example.com",
        }},
        "image_hash":"<IMAGE_HASH>",
        "link":"http://example.com",
        "message":"Great looking SXT handbags in store. #prettybag",
        "caption":"www.example.com",
        }}' \
-F 'platform_customizations={
   "instagram": {
        "image_url": "sample.com/ig-friendly-image.jpg",
        "image_crops": {"100x100": [[0, 0],[800, 800]]}},
  }' \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/adcreatives
```


O parâmetro `platform_customizations` pode conter apenas uma chave `instagram`. Com isso, é possível especificar uma imagem alternativa usando `image_url` ou `image_hash`, além de uma especificação de corte da imagem opcional. Você também pode especificar um vídeo diferente com `video_id`.


Esse recurso pode ser usado para substituir imagens e vídeos em anúncios do Instagram. Use essa opção para `link_data`, `photo_data` e `video_data`. Não é possível usar o recurso para substituir texto nem para fornecer substituições em anúncios do Facebook. Se a imagem original do Facebook for especificada em um post com `object_story_id`, também será possível usar essa opção para exibir uma imagem ou um vídeo, em vez do conteúdo incluído em `object_story_spec`.


Isso não funciona com [anúncios de catálogo Advantage+](https://developers.facebook.com/docs/instagram/ads-api/guides/dynamic-ads).
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/mixed-placements-ads#)[○](https://developers.facebook.com/docs/instagram/ads-api/guides/mixed-placements-ads#)Nesta Página[Anúncios com posicionamentos mistos](https://developers.facebook.com/docs/instagram/ads-api/guides/mixed-placements-ads#an-ncios-com-posicionamentos-mistos)[Começar](https://developers.facebook.com/docs/instagram/ads-api/guides/mixed-placements-ads#come-ar) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ySJXxv3S233w0voLQ4o2W7PK3_YN5dgiuujfVHyq0sVcnjOMy_SuHfu49Fg_aem_SEogmNeGiziJ6RPIqJJEAA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67KSYYpmRqQd8eF18gGI0bNOWstMSqM9GX9o-Il6JbyIVF_iK3b6A8PEcucQ_aem_CWdmX0rHzPaw63I4-WFKYw&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xwlCpPpeb8Pjxwm4aTAnXqzBwd0b3qJ-3MQhvpo4OfK5GWXxMlSu3PMgwJw_aem_i9Zwa7DbgXhRBcwNE6v1GQ&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67KSYYpmRqQd8eF18gGI0bNOWstMSqM9GX9o-Il6JbyIVF_iK3b6A8PEcucQ_aem_CWdmX0rHzPaw63I4-WFKYw&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7261kYUutoxGF9hbNGrF8y0FYKs7vZRUaC0sdmRugHRkJjm6wLnaLnEQzYzA_aem__msIiRoWGbyxf23wy-isNw&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR53rDwqM6x5gNFnubXnNQOC9_fizrWoKogcj4OlYUJ_VQAbEyNDB1NAcgjOhw_aem_ieTLcPbK8HKXzB2knxgiYA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WtVI0C-eiOprs2aKe5jJvpbPyiLdqw907QkdSFwqfZlcfPTxgvDhCjM-MUw_aem_Bb42ZMdj2E7TQnPgHMQUJA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ySJXxv3S233w0voLQ4o2W7PK3_YN5dgiuujfVHyq0sVcnjOMy_SuHfu49Fg_aem_SEogmNeGiziJ6RPIqJJEAA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6qlWEuEunax5Lcw64mvTV-3ohrzAhz75bxs70MVd2Q9nEaVNrk2BspRBQ3Eg_aem_RDyBdj7XEaJVp6RmRNmwqA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR53rDwqM6x5gNFnubXnNQOC9_fizrWoKogcj4OlYUJ_VQAbEyNDB1NAcgjOhw_aem_ieTLcPbK8HKXzB2knxgiYA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ySJXxv3S233w0voLQ4o2W7PK3_YN5dgiuujfVHyq0sVcnjOMy_SuHfu49Fg_aem_SEogmNeGiziJ6RPIqJJEAA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR53rDwqM6x5gNFnubXnNQOC9_fizrWoKogcj4OlYUJ_VQAbEyNDB1NAcgjOhw_aem_ieTLcPbK8HKXzB2knxgiYA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-tuhrRx3WXNktsBqDFWVfMEGVbzndGDWRdIscMkuxuHy5ynoMqnGeSJeiUw_aem_uimBR35NkbjJ4tTMQYvIyA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ySJXxv3S233w0voLQ4o2W7PK3_YN5dgiuujfVHyq0sVcnjOMy_SuHfu49Fg_aem_SEogmNeGiziJ6RPIqJJEAA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o9b_InLwsmqouSTj0uDvT5f6u5-Eey7iuyeELvBBgz6_3ZPQE0aMqPz7N_w_aem_hTDDj6de-AXZ0LCqr4pEOQ&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67KSYYpmRqQd8eF18gGI0bNOWstMSqM9GX9o-Il6JbyIVF_iK3b6A8PEcucQ_aem_CWdmX0rHzPaw63I4-WFKYw&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xwlCpPpeb8Pjxwm4aTAnXqzBwd0b3qJ-3MQhvpo4OfK5GWXxMlSu3PMgwJw_aem_i9Zwa7DbgXhRBcwNE6v1GQ&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xwlCpPpeb8Pjxwm4aTAnXqzBwd0b3qJ-3MQhvpo4OfK5GWXxMlSu3PMgwJw_aem_i9Zwa7DbgXhRBcwNE6v1GQ&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4uApjwQV9sDB188xgQgHIsb89qrG3pMRwFnZiPUD8EO2nSw7N3RBdaGHuqOg_aem_Dij_pDfi5NMvVIUudrEZ7A&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-tuhrRx3WXNktsBqDFWVfMEGVbzndGDWRdIscMkuxuHy5ynoMqnGeSJeiUw_aem_uimBR35NkbjJ4tTMQYvIyA&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4LdZACVQONHBylPX231yClJvwjJSGvHNIM8N2A3N0bUTqHTvPV79MXnJ77RwOZltnB2zIY9JFuX1cMJM5csgb-5L3I1QkMoJUle8jV9euMzDNB52n3p-NqtGKFPwDfQoRpeyg6ofSMsrXTME8ZjttWX8Y)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão