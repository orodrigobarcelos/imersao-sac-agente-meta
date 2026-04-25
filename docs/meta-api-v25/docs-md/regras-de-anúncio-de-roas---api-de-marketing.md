<!-- Fonte: Regras de anúncio de ROAS - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/roas-ad-rules -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Regras de anúncio de ROAS


Em métricas relacionadas ao retorno sobre o investimento em publicidade (ROAS), é importante usar uma combinação de filtros para especificar exatamente como calcular a métrica em questão. Os filtros importantes incluem `attribution_window`, `time_preset` (janela de lookback) e `hours_since_creation`. "ROAS" significa retorno sobre o investimento em publicidade.


Por exemplo, digamos que você pretenda calcular o ROAS de compra no app para celular de clique de 7 dias, mas queira apenas 7 dias de dados maduros:


- Defina uma `attribution_window` de `7D_CLICK`.
- Defina uma `time_preset` de `LAST_ND_14_8`.


Serão atribuídos todos os valores de compra no app para celular em um período de 7 dias referentes a usuários que clicaram no anúncio durante a janela de lookback, sem contabilizar os 7 dias mais recentes, já que eles incluem dados imaturos. Se o usuário tiver clicado no anúncio ontem, não o incluiremos no cálculo do ROAS, já que ainda haverá 6 dias de compras potenciais.


"Valores de compra" são os valores dos eventos de compra no app para celular e de compra de conversão no site (Pixel do Facebook) para as respectivas métricas de ROAS. Na API, esses seriam os valores de compra das métricas de contagem de `app_custom_event.fb_mobile_purchase` e `offsite_conversion.fb_pixel_purchase`, respectivamente.


Se a janela de atribuição incluir janelas de clique e visualização, o ROAS calculado será a soma dos valores. Por exemplo, se a `attribution_window` for `1D_VIEW_7D_CLICK`, calcularemos a soma do valor do ROAS de `1D_VIEW` e `7D_CLICK`. Isso ocorre porque as duas atribuições não são vinculadas e podem ser somadas corretamente sem sobreposição.


Para usar essa métrica da melhor forma possível, o ideal é incluir também um filtro baseado em tempo a fim de garantir que tenham decorrido dias suficientes para a geração de dados maduros. Se o caso de uso exigir dados maduros, recomendamos a aplicação de um filtro como `hours_since_creation` para garantir que o conjunto de anúncios esteja em veiculação há tempo suficiente.


Veja um exemplo de regra:


- Aumento do orçamento em 20% se o ROAS de compra no site de clique de 7 dias for maior que `0.50` (50%)
- Para 7 dias de dados maduros
- Verificação uma vez por dia


Como essas regras são muito específicas, elas geralmente se aplicam a uma lista específica de conjuntos de anúncios, como `id` = `123`. Usamos `8*24` para horas desde a criação a fim de obter pelo menos um dia inteiro de dados maduros.

```
curl \
-F 'name=Test Website ROAS Rule' \
-F 'schedule_spec={
     "schedule_type": "DAILY"
   }' \
-F 'evaluation_spec={
     "evaluation_type": "SCHEDULE",
     "filters": [
       {
         "field": "id",
         "value": [123],
         "operator": "IN"
       },
       {
         "field": "time_preset",
         "value": "LAST_ND_14_8",
         "operator": "EQUAL"
       },
       {
         "field": "attribution_window",
         "value": "7D_CLICK",
         "operator": "EQUAL"
       },
       {
         "field": "hours_since_creation",
         "value": 192,
         "operator": "GREATER_THAN"
       },
       {
         "field": "website_purchase_roas",
         "value": 0.50,
         "operator": "GREATER_THAN"
       }
     ]
   }' \
-F 'execution_spec={
     "execution_type": "CHANGE_BUDGET",
     "execution_options": [
       {
         "field": "change_spec",
         "value": {
           "amount": 20,
           "unit": "PERCENTAGE"
         },
         "operator": "EQUAL"
       },
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Veja um exemplo de regra:


- Ajusta o lance diariamente para alcançar um valor desejado do ROAS (0,80) de compra no app para celular de visualização e clique de 1 dia
- Com uma janela de tolerância de 5% definida por um filtro de intervalo no valor do ROAS


Como mencionamos antes, para obter apenas dados maduros, use predefinições de tempo que não incluam os dados de hoje, como `LAST_7D` e `LAST_14D`.

```
curl \
-F 'name=Test Mobile App ROAS Rule' \
-F 'schedule_spec={
     "schedule_type": "DAILY"
   }' \
-F 'evaluation_spec={
     "evaluation_type": "SCHEDULE",
     "filters": [
       {
         "field": "id",
         "value": [123],
         "operator": "IN"
       },
       {
         "field": "time_preset",
         "value": "LAST_7D",
         "operator": "EQUAL"
       },
       {
         "field": "attribution_window",
         "value": "1D_VIEW_1D_CLICK",
         "operator": "EQUAL"
       },
       {
         "field": "hours_since_creation",
         "value": 48,
         "operator": "GREATER_THAN"
       },
       {
         "field": "mobile_app_purchase_roas",
         "value": [0.76, 0.84],
         "operator": "NOT_IN_RANGE"
       }
     ]
   }' \
-F 'execution_spec={
     "execution_type": "CHANGE_BID",
     "execution_options": [
       {
         "field": "change_spec",
         "value": {
           "amount": 0.80,
           "target_field": "mobile_app_purchase_roas"
         },
         "operator": "EQUAL"
       },
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/roas-ad-rules#)Nesta Página[Regras de anúncio de ROAS](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/roas-ad-rules#regras-de-an-ncio-de-roas) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qxOR8PKl3B-NgISLPPukaM4na7B_YHs5-NLB8NOhnWUqkE6D9q0xCnCyL7A_aem_XRjVOk-6e7KHhoEHJrtuzA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4EfJpn1ms5BiTmKopb7jCMSQY__FjoqQJijcmsC0RBbK9eLjr4pwplnR3hhA_aem_lgOlfdWq-_OOFmJb9pnGKw&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4OCPqBI4jPYPp0Mop9DA1Uz43s6LPrTgqBcwOpxcvXCetrCngayc6pv9CDBg_aem_ZMVr_Asib5-mjAlCKawTVg&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6re2V1GwWHcVWxRmRdwgSfiOh2-Mw9Vrvdb7lKXSdVZ1qcPDxkDWMLw174rg_aem_STJ3IMJzqa1msUMEq__yGA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6re2V1GwWHcVWxRmRdwgSfiOh2-Mw9Vrvdb7lKXSdVZ1qcPDxkDWMLw174rg_aem_STJ3IMJzqa1msUMEq__yGA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4OCPqBI4jPYPp0Mop9DA1Uz43s6LPrTgqBcwOpxcvXCetrCngayc6pv9CDBg_aem_ZMVr_Asib5-mjAlCKawTVg&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6re2V1GwWHcVWxRmRdwgSfiOh2-Mw9Vrvdb7lKXSdVZ1qcPDxkDWMLw174rg_aem_STJ3IMJzqa1msUMEq__yGA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4EfJpn1ms5BiTmKopb7jCMSQY__FjoqQJijcmsC0RBbK9eLjr4pwplnR3hhA_aem_lgOlfdWq-_OOFmJb9pnGKw&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7OmM2f7qpIhZmZJnUzjAN0tElDHWJrOH07KA1YkoMCicFEHV1PzreOpopV3A_aem_FpwwvnSFMPPcT4gEKrd-FA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7OmM2f7qpIhZmZJnUzjAN0tElDHWJrOH07KA1YkoMCicFEHV1PzreOpopV3A_aem_FpwwvnSFMPPcT4gEKrd-FA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6re2V1GwWHcVWxRmRdwgSfiOh2-Mw9Vrvdb7lKXSdVZ1qcPDxkDWMLw174rg_aem_STJ3IMJzqa1msUMEq__yGA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qxOR8PKl3B-NgISLPPukaM4na7B_YHs5-NLB8NOhnWUqkE6D9q0xCnCyL7A_aem_XRjVOk-6e7KHhoEHJrtuzA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qxOR8PKl3B-NgISLPPukaM4na7B_YHs5-NLB8NOhnWUqkE6D9q0xCnCyL7A_aem_XRjVOk-6e7KHhoEHJrtuzA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6icfbwpC_OU-wO4IdhxnCi2HC-AqLLrSjpMQqNyAXfUgq4of_e-b08rotJcw_aem_Jtea-oFNyDiL2evt59Dq6g&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qxOR8PKl3B-NgISLPPukaM4na7B_YHs5-NLB8NOhnWUqkE6D9q0xCnCyL7A_aem_XRjVOk-6e7KHhoEHJrtuzA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6icfbwpC_OU-wO4IdhxnCi2HC-AqLLrSjpMQqNyAXfUgq4of_e-b08rotJcw_aem_Jtea-oFNyDiL2evt59Dq6g&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qxOR8PKl3B-NgISLPPukaM4na7B_YHs5-NLB8NOhnWUqkE6D9q0xCnCyL7A_aem_XRjVOk-6e7KHhoEHJrtuzA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4EfJpn1ms5BiTmKopb7jCMSQY__FjoqQJijcmsC0RBbK9eLjr4pwplnR3hhA_aem_lgOlfdWq-_OOFmJb9pnGKw&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4EfJpn1ms5BiTmKopb7jCMSQY__FjoqQJijcmsC0RBbK9eLjr4pwplnR3hhA_aem_lgOlfdWq-_OOFmJb9pnGKw&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6re2V1GwWHcVWxRmRdwgSfiOh2-Mw9Vrvdb7lKXSdVZ1qcPDxkDWMLw174rg_aem_STJ3IMJzqa1msUMEq__yGA&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4YLdBxAuh9cM2zAKq1b0Qmg_FmsnXGBgyGyXgUn50JgyDDYVHfmGE9h-Lv_EpPRKeX3ciQZraiWCPiGN7vO1yn6ixQZjoFAzp4l0Gfv-fAAFD3OojwniHyMdf4UjLcSwkjUOGv3XKgErNVbhO2l9y6euU)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão