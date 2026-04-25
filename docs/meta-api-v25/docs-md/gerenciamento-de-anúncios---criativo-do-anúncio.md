<!-- Fonte: Gerenciamento de anúncios - Criativo do anúncio.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de Catálogo Advantage+ para o setor imobiliário – Como criar anúncios


Os Anúncios de Catálogo Advantage+ para o setor imobiliário são criados da mesma forma que os Anúncios de Catálogo Advantage+ normais.


- [**Etapa 1: criar uma campanha**](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#campaign)
- [**Etapa 2: criar um conjunto de anúncios**](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#adset)
- [**Etapa 3: fornecer o criativo do anúncio**](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#creative)
- [**Etapa 4: criar um anúncio**](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#ad)


Se quiser criar uma campanha de Anúncios de Catálogo Advantage+ para o setor imobiliário, você precisará de:


- uma [Página do Facebook](https://www.facebook.com/pages/create/) que represente o anunciante;
- uma [conta de anúncios](https://www.facebook.com/ads/manager/accounts) com informações de pagamento registradas;
- um [público do setor imobiliário](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-real-estate/audience) disponível na sua conta de anúncios;
- um [catálogo de listagem de imóveis](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-real-estate/catalog), como o que está disponível no seu Gerenciador de Negócios.


Todos os anúncios no Facebook devem fazer parte de um conjunto de anúncios que define os respectivos lances e o direcionamento. Por sua vez, o conjunto de anúncios deve fazer parte de uma campanha que tenha um objetivo definido. É necessário criar cada nível de uma campanha para poder veicular os anúncios.


## Etapa 1. criar uma campanha de anúncios


Os Anúncios de Catálogo Advantage+ para o setor imobiliário usam o objetivo `PRODUCT_CATALOG_SALES`. Você deve especificar um catálogo imobiliário no `promoted_object` no nível da campanha:

```
curl \
  -F 'name=DARE campaign' \
  -F 'objective=PRODUCT_CATALOG_SALES' \
  -F 'promoted_object={"product_catalog_id":"
```
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#)

## Etapa 2. criar um conjunto de anúncios


Crie o [conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) que define as opções de lances e direcionamento para os seus anúncios.

```
curl \
  -F 'name=adset name' \
  -F 'bid_amount=3000' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=OFFSITE_CONVERSIONS' \
  -F 'daily_budget=15000' \
  -F 'campaign_id=
```

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#)

## Etapa 3. fornecer o criativo do anúncio


Forneça o criativo do modelo de Anúncios de Catálogo Advantage+, semelhante aos [criativos do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative). A principal diferença é que você pode adicionar [parâmetros de modelo](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/#templateandtransform) que o Facebook usa no tempo de execução com base nos dados do seu catálogo e no interesse de alguém pelo imóvel anunciado.


Da mesma forma que para os [Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/#adtemplate), defina os `template_data` em `object_story_spec` no criativo do anúncio. Você também pode usar a `template_url` para configurar a URL de modo mais flexível em vez de usar a URL do feed. Se a `template_url` não puder ser construída no tempo de renderização dos anúncios, será usada a URL do catálogo.


Veja abaixo um exemplo de como gerar um criativo de carrossel para uma listagem de imóveis.

```
curl \
  -F 'name=DARE creative' \
  -F 'object_story_spec={
    "page_id": "
```


### Opções de formato do criativo


Escolha entre exibir um único produto ou vários produtos em um carrossel. Para anúncios de itens individuais, você pode mostrar várias imagens do produto no respectivo carrossel. Também é possível mostrar cartões estáticos e cartões dinâmicos. Consulte Anúncios de Catálogo Advantage+ – [Criar um modelo de criativo](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/#adtemplate).


### Tags de modelo


Ao veicular seu anúncio, substituímos as tags em `{{...}}` pelos valores adequados.


| Tag de modelo | Descrição |
| --- | --- |
| home_listing.description | Descrição da listagem de imóveis |
| home_listing.name | Nome |
| home_listing.num_beds | Quantidade de camas |
| home_listing.num_baths | Quantidade de banheiros |
| home_listing.num_units | Quantidade de unidades |
| home_listing.price | Preço da listagem de imóveis |
| home_listing.year_built | Ano de construção do imóvel |
| home_listing.city | Cidade divulgada no catálogo |
| home_listing.country | País divulgado no catálogo |
| home_listing.region | Região divulgada no catálogo |
| home_listing.street_address | Endereço divulgado no catálogo |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#)

## Etapa 4. criar o anúncio


Por fim, crie o [anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) que veiculará criativos dinâmicos para o usuário com base no seu catálogo:

```
curl \
  -F 'name=DARE Alpha Ad' \
  -F 'adset_id=
```


Seu anúncio agora está visível no Gerenciador de Anúncios e está pausado.
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#)[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#)Nesta Página[Anúncios de Catálogo Advantage+ para o setor imobiliário – Como criar anúncios](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#an-ncios-de-cat-logo-advantage--para-o-setor-imobili-rio---como-criar-an-ncios)[Etapa 1. criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#campaign)[Etapa 2. criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#adset)[Etapa 3. fornecer o criativo do anúncio](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#creative)[Opções de formato do criativo](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#creative-options)[Tags de modelo](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#template)[Etapa 4. criar o anúncio](https://developers.facebook.com/docs/marketing-api/real-estate-ads/ads-management#ad) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5m5-rpsvXCgiPhoSCs7KB_n2QGXtvtufY3uy7s9Ssv3jJZOsQTEsxD_aKiVg_aem_1Uakb5yFfSY-wyT5sloHWg&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7QFuixZYdvL6l7VqyVzCaI9JTSoTzFTOVrbPcJDRcSWczuzoeFYL_VPoA_qw_aem_NGoxhtqOoFSpyY5x2-rTSg&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7YSpDsrCcy8m5kKehdBm8OmPeWTDn4Fz-H5zmBQSKjJ6j_vCme8M417uVg5g_aem_MigxNDNgOu2mAAj_jBovYw&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4oLLx2vsJgEhUF6RiUPon5cI-lkt7ah219_EjRiMi1X9f-Iv2jmB5tc9sMJw_aem_ojU5LTBmPjz7i0rDX2eV7Q&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6LwL98U36eogxUc0c-oMozHqw0E5spqABoKcDGaIr89XDas_-LIK8N2jTnyw_aem_q1jAlzq-S-HacAXO26SFrQ&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7QFuixZYdvL6l7VqyVzCaI9JTSoTzFTOVrbPcJDRcSWczuzoeFYL_VPoA_qw_aem_NGoxhtqOoFSpyY5x2-rTSg&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR40F1ue7GvJvPDy986UDNbanjXmRpRm3EZwFZgQ_gk6VHl_33-aWnyN4FXvPw_aem_aqgaJVODtrSIXqNkAHPFXA&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ly3Wo2HmPgKAl_-o-sYX_MW0f3rucU4l7dQazNoAq8ihOEw8H1B4BxlPMkw_aem_PHQXhXxJsKs5ZGcHbVrF7g&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5m5-rpsvXCgiPhoSCs7KB_n2QGXtvtufY3uy7s9Ssv3jJZOsQTEsxD_aKiVg_aem_1Uakb5yFfSY-wyT5sloHWg&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4BYQNGsKiRCoF5izQzLMryEQo97Omfte4p8JWZXZpGBHesZFxqF4mcteNQGg_aem_anU7qas2h-EtbqQsAowd-w&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6LwL98U36eogxUc0c-oMozHqw0E5spqABoKcDGaIr89XDas_-LIK8N2jTnyw_aem_q1jAlzq-S-HacAXO26SFrQ&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7YSpDsrCcy8m5kKehdBm8OmPeWTDn4Fz-H5zmBQSKjJ6j_vCme8M417uVg5g_aem_MigxNDNgOu2mAAj_jBovYw&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR40F1ue7GvJvPDy986UDNbanjXmRpRm3EZwFZgQ_gk6VHl_33-aWnyN4FXvPw_aem_aqgaJVODtrSIXqNkAHPFXA&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR74zOYplTKZcGfM6_vJLGElUkYP9QvWFyTwhEaTl7cAoWeKVRnwR-FreK_Fgw_aem_8jwYPtczhqCOIesX9RhZYg&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ly3Wo2HmPgKAl_-o-sYX_MW0f3rucU4l7dQazNoAq8ihOEw8H1B4BxlPMkw_aem_PHQXhXxJsKs5ZGcHbVrF7g&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4BYQNGsKiRCoF5izQzLMryEQo97Omfte4p8JWZXZpGBHesZFxqF4mcteNQGg_aem_anU7qas2h-EtbqQsAowd-w&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ly3Wo2HmPgKAl_-o-sYX_MW0f3rucU4l7dQazNoAq8ihOEw8H1B4BxlPMkw_aem_PHQXhXxJsKs5ZGcHbVrF7g&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4oLLx2vsJgEhUF6RiUPon5cI-lkt7ah219_EjRiMi1X9f-Iv2jmB5tc9sMJw_aem_ojU5LTBmPjz7i0rDX2eV7Q&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4IuMc5JuduJcg86hYXKC91R1x9g3T_KN5oD0DhfvqM_lz9r_F3t7lHiyr_Mw_aem_RwCmqPbUxsznQ40_t-zB2Q&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7YSpDsrCcy8m5kKehdBm8OmPeWTDn4Fz-H5zmBQSKjJ6j_vCme8M417uVg5g_aem_MigxNDNgOu2mAAj_jBovYw&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6-eK5Z_irmPBwVCIGvP-DZceXmVOaJiXTu6jdL9Lqp2EUty-p-_1xCYwK7UQDuatehpcm6T90QSG-eMUQwKcLi8qsMGSqLplMWm_cNX1snmw3IO3KuzYDGaADfso5pMpET-zROeAvQxdrrkJV093Eyu30)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão