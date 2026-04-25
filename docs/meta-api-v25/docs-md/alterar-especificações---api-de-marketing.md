<!-- Fonte: Alterar especificações - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/overview/change-spec -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Alterar especificações de regras de anúncios


Esta página aborda em detalhes o `change_spec`, especificamente como criar a opção de execução e como usar os recursos mais avançados.


O `change_spec` é usado para tipos de execução como `CHANGE_BUDGET` e `CHANGE_BID` e contém estes parâmetros: `amount`, `limit`, `unit` e `target_field`.


| Campo | Descrição |
| --- | --- |
| amount | Obrigatório. Determina a quantia para alterar o orçamento ou lance. Os valores de outros parâmetros em change_spec determinam como essa quantia é usada. Valores compatíveis: um valor numérico, como 3000 ou -50 . |
| limit | Opcional. Especifica a quantia máxima ou mínima do orçamento ou lance. Por exemplo, se o orçamento ou lance estiver sendo aumentado, esse número define um limite superior. Se target_field estiver presente, o valor especifica um intervalo entre o limite inferior e o superior de valores. Valores compatíveis: moeda, como 5000 para representar US$ 50 ou, para target_field , um intervalo de moedas, como [4000, 6000] para representar de US$ 40 a US$ 60. |
| unit | Obrigatório, a menos que target_field esteja presente. Especifica a unidade do valor amount . Por exemplo, se a unidade for PERCENTAGE , um amount de -50 significa -50% . Valores compatíveis: ACCOUNT_CURRENCY ou PERCENTAGE . |
| target_field | Opcional. Especifica se os orçamentos ou lances devem ou não ser escalonados conforme um valor de destino. Se estiver presente, amount representa o valor de destino do campo de destino. O orçamento ou lance aumenta ou diminui proporcionalmente, dependendo se o valor atual do conjunto de anúncios para o campo de destino for mais baixo ou mais alto do que amount . Valores compatíveis: um campo de insights, cost_per_mobile_app_install ou mobile_app_purchase_roas . |


## Exemplos


Aqui está um exemplo de uma regra `CHANGE_BUDGET` que diminui os orçamentos em 30% para todos os conjuntos de anúncios com baixo desempenho (com `frequency` vitalícia alta de maneira estável). Essa regra só funciona à meia-noite nas terças e sextas-feiras.

```
curl \
-F 'name=Test Change Budget Rule' \
-F 'schedule_spec={
     "schedule_type": "CUSTOM",
     "schedule": [
       {
          "start_minute": 0,
         "days": [2, 5]
       }
     ]
   }' \
-F 'evaluation_spec={
     "evaluation_type": "SCHEDULE",
     "filters": [
       {
         "field": "entity_type",
         "value": "ADSET",
         "operator": "EQUAL"
       },
       {
         "field": "time_preset",
         "value": "LIFETIME",
         "operator": "EQUAL"
       },
       {
         "field": "impressions",
         "value": 8000,
         "operator": "GREATER_THAN"
       },
       {
         "field": "frequency",
         "value": 5.0,
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
           "amount": -30,
           "unit": "PERCENTAGE"
         },
         "operator": "EQUAL"
       },
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Aqui está outro exemplo, onde o lance é escalonado diariamente com base em um valor de destino `cost_per_mobile_app_install` para o conjunto de anúncios `123`.


**Também adicionamos um filtro de intervalo para `cost_per_mobile_app_install` para lançar uma janela de tolerância de 10%.** Com isso, mudanças proporcionais pequenas não são realizadas se o valor atual estiver próximo o suficiente do valor de destino.

```
curl \
-F 'name=Test Change Bid Rule' \
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
         "value": "LIFETIME",
         "operator": "EQUAL"
       },
       {
         "field": "mobile_app_install",
         "value": 100,
         "operator": "GREATER_THAN"
       },
       {
         "field": "cost_per_mobile_app_install",
         "value": [4.5, 5.5],
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
           "amount": 5.0,
           "limit": [2.0, 10.0],
           "target_field": "cost_per_mobile_app_install"
         },
         "operator": "EQUAL"
       },
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Por exemplo, se o valor atual for `4.0`, o lance aumentará em `25%`, pois essa é a diferença proporcional entre o valor de destino de `5.0` e o valor atual.


O limite impede que o lance aumente para mais de `10.0` e diminua para menos de `2.0`.
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/change-spec#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/change-spec#)Nesta Página[Alterar especificações de regras de anúncios](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/change-spec#alterar-especifica--es-de-regras-de-an-ncios)[Exemplos](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/change-spec#exemplos) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6hnvPCHrHdfvWZCYUzlvxekRHi_e0OHhuBRCNuA-q4HV6Z-j41u5ngTsgFzA_aem_KOIdJwvZIRZFM4_YnWdvIQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6TQuHAAmkBxJgWch4kFmUxM6ms74NCv4zlRGfFwVisZ0z-GwDz8HlLqjU92Q_aem_nVUm3_U06cLVVEGKaUbBhw&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7T0LIDY2Yma2b--rxLkfPok3Sj5jDcs3IC5zNRRMDp0Dy7XFGBwLjr91DGgA_aem_Xrlb0fgWegZPbmak1RjnXA&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LB5ZrgY2aO6fIJHmDDdmUwiC3N2aDXpgvoF0zbbdxPCF7qSqikoT14bV4fA_aem_WUvo-QrtzhPv_5nvjDN0TA&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6X8OysD_jrnJZrjsx-J2BrQhIrvGHv_y1ykb-7S89p2uSDMfmDA6barsNtbg_aem_N1OmQrD979E7_wwdImU9_w&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6TQuHAAmkBxJgWch4kFmUxM6ms74NCv4zlRGfFwVisZ0z-GwDz8HlLqjU92Q_aem_nVUm3_U06cLVVEGKaUbBhw&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_iSktV6YDKp2BBuMqQbXDzp3FPFIdObo2JWUocXVONtrxqKK9s8BWMjkWWA_aem_P5g5CGSLex6h5stVTZxxYQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67tOJTcS-QwwNpZMpY4UUGt7mWQHCr0FLkLwh2T0bPw0YL6QafqEgaqA21qw_aem_UGpPMkdFtYqu3KlQkP5RUg&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dwNmL3SgG2nB65pu5eaOzdgySAayg5vZFhD2X4GR29F9oxmyIX6AmKRjBow_aem_353aAim-jYBqhx1lKtvlGQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_iSktV6YDKp2BBuMqQbXDzp3FPFIdObo2JWUocXVONtrxqKK9s8BWMjkWWA_aem_P5g5CGSLex6h5stVTZxxYQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6hnvPCHrHdfvWZCYUzlvxekRHi_e0OHhuBRCNuA-q4HV6Z-j41u5ngTsgFzA_aem_KOIdJwvZIRZFM4_YnWdvIQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7T0LIDY2Yma2b--rxLkfPok3Sj5jDcs3IC5zNRRMDp0Dy7XFGBwLjr91DGgA_aem_Xrlb0fgWegZPbmak1RjnXA&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Ch8ipJyC6_fCFzrcG13rne8EkRsu-rIDPPj2XzwXyrzZkJT5xdvx1G_8IBA_aem_dgr4wMaB15nTs2r90Z6Ctg&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Ch8ipJyC6_fCFzrcG13rne8EkRsu-rIDPPj2XzwXyrzZkJT5xdvx1G_8IBA_aem_dgr4wMaB15nTs2r90Z6Ctg&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_iSktV6YDKp2BBuMqQbXDzp3FPFIdObo2JWUocXVONtrxqKK9s8BWMjkWWA_aem_P5g5CGSLex6h5stVTZxxYQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67tOJTcS-QwwNpZMpY4UUGt7mWQHCr0FLkLwh2T0bPw0YL6QafqEgaqA21qw_aem_UGpPMkdFtYqu3KlQkP5RUg&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67tOJTcS-QwwNpZMpY4UUGt7mWQHCr0FLkLwh2T0bPw0YL6QafqEgaqA21qw_aem_UGpPMkdFtYqu3KlQkP5RUg&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LB5ZrgY2aO6fIJHmDDdmUwiC3N2aDXpgvoF0zbbdxPCF7qSqikoT14bV4fA_aem_WUvo-QrtzhPv_5nvjDN0TA&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6hnvPCHrHdfvWZCYUzlvxekRHi_e0OHhuBRCNuA-q4HV6Z-j41u5ngTsgFzA_aem_KOIdJwvZIRZFM4_YnWdvIQ&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7T0LIDY2Yma2b--rxLkfPok3Sj5jDcs3IC5zNRRMDp0Dy7XFGBwLjr91DGgA_aem_Xrlb0fgWegZPbmak1RjnXA&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7IAC_e9Qb0Q2lKrtF7fTwpfQF60b45H0xzPvAume4TlzaW2uLbpnGoy3NntMZT7C8bct1KPAMcWhFp3iheGok4RvYc4K9VXH6Lx2P__DuC3Qf-ZpVJP3KTKmpllC52FXKYZLp02DeQPb963sR62IhDGG4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão