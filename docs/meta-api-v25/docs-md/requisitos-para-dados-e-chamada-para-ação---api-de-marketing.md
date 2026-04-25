<!-- Fonte: Requisitos para dados e chamada para ação - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Requisitos para dados e chamada para ação


## Streaming do Instagram


Os tipos de criativos disponíveis para cada `objective` compatível. Haverá suporte para mais tipos de criativos e combinações de objetivos no futuro.


|  | LINK_DATA (carrossel ou não) | VIDEO_DATA | PHOTO_DATA |
| --- | --- | --- | --- |
| LINK_CLICKS | ✓ | ✓ |  |
| VIDEO_VIEWS |  | ✓ |  |
| MOBILE_APP_INSTALLS | ✓ | ✓ |  |
| CONVERSIONS | ✓ | ✓ |  |
| POST_ENGAGEMENT | ✓ | ✓ | ✓ |
| MOBILE_APP_ENGAGEMENT | ✓ | ✓ |  |


Para anúncios `LINK_CLICKS` ou `CONVERSIONS`, você pode fornecer uma `call_to_action` (CTA) no campo `link_data` ou `video_data` para definir o botão de ação abaixo do anúncio.


- Se você usar `link_data` e a `call_to_action` não estiver especificada, uma `call_to_action` padrão será exibida. O valor `link` é proveniente do campo `link` do `link_data` anterior, e o `type` de CTA padrão é "LEARN_MORE".
- Se você definir claramente uma `call_to_action`, o valor de `link` deverá ser o mesmo que de `link` para o `link_data` anterior. Você pode informar `caption` como o URL exibido.
- Se você usar `video_data`, deverá especificar a `call_to_action`.


Para anúncios `MOBILE_APP_INSTALLS` ou `MOBILE_APP_ENGAGEMENT`, o campo `call_to_action` no `link_data` ou `video_data` é necessário. Os links devem apontar para a App Store da Apple ou o URL do Google Play de um app. A inclusão de [deep links](https://developers.facebook.com/docs/ads-for-apps/mobile-app-ads#deep-linking) também é aceita. Se o `link_data` for usado, o `link` na `call_to_action` deve ser o mesmo que o `link` do `link_data` anterior.


Para anúncios `VIDEO_VIEWS`, os campos `description` e `video_data` são opcionais. O campo `image_hash` ou `image_url` deve ser fornecido.


Para anúncios `POST_ENGAGEMENT`, se você usar `link_data`, uma CTA será exibida, especificada por você ou predefinida como `LEARN_MORE`. Caso não queira incluir uma CTA, poderá usar `photo_data`.


`message` em `link_data`, `description` em `video_data` e `caption` em `photo_data` para criativos do anúncio do Instagram não podem ter mais de 2200 caracteres. O campo `caption` em `link_data` também é exibido como [sobreposição de um toque](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#overlay). Outros campos de título e legenda são usados apenas pelo Facebook, não pelo Instagram.


Se esses campos de mensagem tiverem algum hiperlink, ele não estará ativo no Instagram. Para anúncios `POST_ENGAGEMENT`, se você especificar uma mensagem com um hiperlink usando `photo_data`, ou `video_data` sem CTA, uma CTA padrão com tipo `LEARN_MORE` e um link da mensagem serão exibidos.


**É recomendável usar `#hashtags` na mensagem dos anúncios do Instagram.** Você não pode usar mais de 30 hashtags em cada mensagem.

```
use FacebookAds\Object\AdCreative;
use FacebookAds\Object\AdCreativeLinkData;
use FacebookAds\Object\Fields\AdCreativeLinkDataFields;
use FacebookAds\Object\AdCreativeObjectStorySpec;
use FacebookAds\Object\Fields\AdCreativeObjectStorySpecFields;
use FacebookAds\Object\Fields\AdCreativeFields;

$link_data = new AdCreativeLinkData();
$link_data->setData(array(
  AdCreativeLinkDataFields::IMAGE_CROPS => array(
    '100x100'=> array(array(200,90),array(900,790)),
    '191x100'=> array(array(0,200),array(1146,800))
  );
  AdCreativeLinkDataFields::MESSAGE => 'Great looking SXT handbags in store. #prettybag',
  AdCreativeLinkDataFields::LINK => 'http://example.com',
  AdCreativeLinkDataFields::IMAGE_HASH => '<IMAGE_HASH>',
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

$creative = new AdCreative(null, 'act_<AD_ACCOUNT_ID>');

$creative->setData(array(
  AdCreativeFields::NAME => 'Instagram only creative',
  AdCreativeFields::OBJECT_STORY_SPEC => $object_story_spec,
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
link_data[LinkData.Field.image_crops] = {
    '100x100':[[200,90],[900,790]],
    '191x100':[[0,200],[1146,800]]
}

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

creative = AdCreative(parent_id='act_&lt;AD_ACCOUNT_ID&gt;')
creative[AdCreative.Field.name] = 'Instagram only creative'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
```

```
curl \
-F 'name=Instagram only creative' \
-F 'object_story_spec={
     "page_id":<PAGE_ID>,
     "instagram_user_id":<IG_USER_ID>,
     "link_data":{
         "image_crops":{
              "100x100": [ [200,90], [900, 790] ],
              "191x100": [ [0,200], [1146, 800] ],
         },
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
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/adcreatives
```


### Sobreposição de imagens em anúncios com link


Anúncios com link do Instagram com `objective` definido como `LINK_CLICKS` ou `CONVERSIONS` mostram o nome da sua Página do Facebook e o "URL de exibição" em uma sobreposição de imagem em um toque. Isso aparece quando um usuário clica na imagem de um anúncio. Se um anúncio com link utilizar criativos de vídeo, essa sobreposição não será exibida.


Para anúncios `MOBILE_APP_INSTALLS` e `MOBILE_APP_ENGAGEMENT`, mostramos o nome de Página do Facebook de um anunciante e a chamada “Visualizar na App Store” para anúncios no iOS ou “Visualizar na Play Store” para anúncios no Android.


O "URL de exibição" de um anúncio com link é o valor `link` no `link_data`, exceto se você incluir `caption` no `link_data`. Se o link não for intuitivo, como "http://tracking.com/redirect=client.com", você deverá definir `caption` como `client.com`, que é exibido na sobreposição em vez do `link`.
[○](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#)

## Instagram Stories


Criativos do anúncio para stories do Instagram somente permitem `photo_data`, `video_data` e `link_data`. Entre eles, `photo_data` pode ser usado somente para o objetivo `REACH`, `link_data` pode ser usado somente para o objetivo `LINK_CLICKS` e `video_data` pode ser usado para todos os objetivos `REACH`, `VIDEO_VIEWS` ou `LINK_CLICKS`.


Como anúncios de marca (`REACH` e `VIDEO_VIEWS`) nos stories do Instagram mostram somente o nome da conta e a foto do perfil de um anunciante no Instagram, você não pode definir todos os outros campos visíveis, incluindo mensagem, título, link, legenda etc. Se `link` for especificado em `video_data`, um botão para CTA também será exibido.


Anúncios de resposta direta (`LINK_CLICKS`, `CONVERSIONS` e `APP_INSTALLS`) mostram um botão CTA. Você pode especificar a `call_to_action` do `link_data` ou `video_data`. Se a `call_to_action` não for especificada no `link_data`, o Instagram mostrará um botão `Learn More` com o valor `link` de `link_data`. Não há suporte para determinados tipos de CTA, incluindo `Donate`, `Donate Now`, `Save`, `Call Now` e `Get Directions`. Outros campos como mensagem e título ainda não são usados para anúncios de resposta direta dos stories do Instagram.


Clicar em um anúncio nos stories do Instagram mostra o próximo story e clicar no botão de CTA direciona para o URL de destino.
[○](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#)[○](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#)Nesta Página[Requisitos para dados e chamada para ação](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#requisitos-para-dados-e-chamada-para-a--o)[Streaming do Instagram](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#streaming-do-instagram)[Sobreposição de imagens em anúncios com link](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#overlay)[Instagram Stories](https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements#instagram-stories) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7JYPyDP6vqi0Du87nfW0d57JEOeVt2dmBprY2XC6N8shALHmNpjF3g24tsHA_aem_foqeUYjevz4xJE556sQQDA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6INJIblBLJmQj_QmNemrvYscRrF0yEaVY6DHIuiMgjdCEQzCE3dTbDYhtL0A_aem_MAu7Fl6TQnsrOAMzTnFj0w&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75Th6FSa5i2JVQrJ8qxHnNoiJpNILD21ohmMp8N4RxBjwWCLXvMMCHDQpt9A_aem_1EH6Z4wDg4mDB07waUQPjg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOFk1rADjjSF8_k7KuR_stGdr6SBk2AnniqxmjJvsDucJGoqKvP4eik_A-Q_aem_KI2vDPrZlsAhzKTiUIOhxg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75Th6FSa5i2JVQrJ8qxHnNoiJpNILD21ohmMp8N4RxBjwWCLXvMMCHDQpt9A_aem_1EH6Z4wDg4mDB07waUQPjg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WwkJr0WZUaI4UfWB8-cd6gCABga3A2KUXue3W7ohLaqW9ZobILgsSIBezCA_aem_DEQQmaXpxigIvglwO2GKoA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WwkJr0WZUaI4UfWB8-cd6gCABga3A2KUXue3W7ohLaqW9ZobILgsSIBezCA_aem_DEQQmaXpxigIvglwO2GKoA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7JYPyDP6vqi0Du87nfW0d57JEOeVt2dmBprY2XC6N8shALHmNpjF3g24tsHA_aem_foqeUYjevz4xJE556sQQDA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7JYPyDP6vqi0Du87nfW0d57JEOeVt2dmBprY2XC6N8shALHmNpjF3g24tsHA_aem_foqeUYjevz4xJE556sQQDA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4sCuQjjJoYnbS6HJCmYrwNVLeRvg29Gc5ELmjF48JrNSeCXvopUJQV9Z7CYw_aem_h2ieVNFtQU2qVNeTWgpsIw&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6INJIblBLJmQj_QmNemrvYscRrF0yEaVY6DHIuiMgjdCEQzCE3dTbDYhtL0A_aem_MAu7Fl6TQnsrOAMzTnFj0w&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WwkJr0WZUaI4UfWB8-cd6gCABga3A2KUXue3W7ohLaqW9ZobILgsSIBezCA_aem_DEQQmaXpxigIvglwO2GKoA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOFk1rADjjSF8_k7KuR_stGdr6SBk2AnniqxmjJvsDucJGoqKvP4eik_A-Q_aem_KI2vDPrZlsAhzKTiUIOhxg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OJcfaZlqp5LvfyrtKLE15fLTCExMkpsahkkOYHteXPcSInG53X4ryjE3u2Q_aem_ZZrnfpW6vVcCR0pwC6vAng&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75Th6FSa5i2JVQrJ8qxHnNoiJpNILD21ohmMp8N4RxBjwWCLXvMMCHDQpt9A_aem_1EH6Z4wDg4mDB07waUQPjg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR61EBFQwbtMMA-CEZTbr3fpZjg3EfU4KSq8Gi4AsYPu539kSXdy_sAEM0NaUg_aem_IvPDTy5P4grvdiMjdijc8Q&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6o9ms5Nie6kIeXBfb1y_RDEZrU-mobOjsTqT8Om1Zd0qDOP_sXVKlazeTRIQ_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4sCuQjjJoYnbS6HJCmYrwNVLeRvg29Gc5ELmjF48JrNSeCXvopUJQV9Z7CYw_aem_h2ieVNFtQU2qVNeTWgpsIw&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WwkJr0WZUaI4UfWB8-cd6gCABga3A2KUXue3W7ohLaqW9ZobILgsSIBezCA_aem_DEQQmaXpxigIvglwO2GKoA&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOFk1rADjjSF8_k7KuR_stGdr6SBk2AnniqxmjJvsDucJGoqKvP4eik_A-Q_aem_KI2vDPrZlsAhzKTiUIOhxg&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5blN5fKAI4FweRrBjr2TGjuFDv2zlU2hP-P83oTNiXfRiPOD2VkM1k3jeb-UM2GNgBL_iBbDHnnDwHndHgyRwWAhUDMDbG_NGv3-MAWrKx7UDiOnuCimG9crmkN3SurmzgvHYW_qPMlRAj6hQY7rvCXYo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão