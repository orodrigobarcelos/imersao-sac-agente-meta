<!-- Fonte: Públicos Personalizados offline - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Públicos Personalizados offline


Agrupe as pessoas que visitaram sua loja, ligaram para o seu atendimento ao cliente ou realizaram ações offline e direcione anúncios do Facebook para elas.


Por exemplo, se você quiser fazer o direcionamento para pessoas que gastaram mais de US$ 1.000 nos últimos 90 dias:

```
curl \
-F 'name=90d High Value' \
-F 'rule={"inclusions":{"operator":"or","rules":[{"retention_seconds":7776000,"event_sources":[{"id":"<OFFLINE_EVENT_SET_ID>","type":"offline_events"}],"filter":{"operator":"and","filters":[{"operator":"=","field":"event","value":"Purchase"}]},"aggregation":{"type":"sum","field":"value","operator":">","value":"1000"}}]}}' \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/customaudiences"
```


Os Públicos Personalizados de conversões offline são baseados em eventos de conversão carregados em um conjunto de eventos offline. Confira a documentação da [API de Conversões Offline](https://developers.facebook.com/docs/marketing-apis/offline-conversions/).


Desde setembro de 2018, não aceitamos `subtype` de públicos personalizados de sites, de aplicativos e de engajamento nem públicos de dados de conversão offline. A única exceção é que continuamos a aceitar `subtype` de públicos personalizados de engajamento para vídeo.


## Criar um público


Para criar um Público Personalizado do seu conjunto de eventos offline, a conta já deve ter aceitado os Termos de Serviço para Públicos Personalizados no [Gerenciador de Anúncios](https://www.facebook.com/ads/manage/powereditor/):

```
curl \
  -F 'name=My New Offline Event Set' \
  -F 'rule={"inclusions":{"operator":"or","rules":[{"retention_seconds":2592000,"event_sources":[{"id":"<OFFLINE_EVENT_SET_ID>","type":"offline_events"}],"filter":{"operator":"and","filters":[{"operator":"=","field":"event","value":"purchase"},{"operator":">","field":"value","value":"50+Sheet1!A2+Sheet1!A2+Sheet1!A2+"}]}}]}}'
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/customaudiences
```


Estes são os parâmetros mais relevantes para Públicos Personalizados do site:


| Nome | Descrição |
| --- | --- |
| name tipo: string | Obrigatório. O nome do cluster. |
| rule tipo: string | Obrigatório. Regras de público que serão aplicadas à URL do referenciador. |
| description tipo: string | Opcional. Descrição do Público Personalizado. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#)

## Regras de público


As regras determinam se uma conta do Centro de Contas deve ser adicionada a esse público. Elas se aplicam a eventos offline enviados por meio da [API de Conversões Offline](https://developers.facebook.com/docs/marketing-apis/offline-conversions/) ou carregados manualmente com o gerenciador de eventos offline. As regras são aplicadas a eventos específicos ou ao campo `custom_data`. Consulte [Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules) para saber mais. Veja também:


- [Sintaxe das regras de público](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#audience-rules-syntax).
- [Sintaxe do conjunto de regras](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#rule_set_syntax).
- [Sintaxe das regras de inclusão e exclusão](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#inclusion-exclusion): em `event_source`, defina `id` como sua identificação do pixel e `type` como `pixel`.
- [Filtros](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#filter).
- [Regras de filtro](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#filter-rules): em `field`, use `"event"` caso o filtro especifique um evento. Parâmetros que correspondem a eventos enviados pelo pixel (por exemplo, `'ViewContent'` ou `'Purchase'`).
- [Funções agregadas](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#aggregate).


### Exemplo de regras de Público Personalizado offline


```
//Match all referring `favorite_food` containing the string `'pizza'` in the last 30 days:

{
    "inclusions": {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "type": "offline_events",
                        "id": "<OFFLINE_EVENT_SET_ID>",
                    }
                ],
                "retention_seconds": 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "custom_data.favorite_food",
                            "operator": "i_contains",
                            "value": "pizza"
                        }
                    ]
                },
            }
        ]
    }
}
```


Corresponde aos eventos Purchase em que o custo é maior ou igual a US$ 100 nos últimos 30 dias. Considere usar essa regra no seguinte evento:

```
{
    "inclusions": {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "type": "offline_events",
                        "id": "<OFFLINE_EVENT_SET_ID>"
                    }
                ],
                "retention_seconds": 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "eq",
                            "value": "Purchase"
                        },
                        {
                            "operator": "or",
                            "filters": [
                                {
                                    "field": "value",
                                    "operator": ">=",
                                    "value": "100"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```


Corresponde aos eventos Purchase em que a cor do produto é `blue` definida por atributos de evento offline no campo `custom_data` chamado "color" nos últimos 30 dias. Considere usar essa regra no seguinte evento:

```
{
    "inclusions": {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "type": "offline_events",
                        "id": "<OFFLINE_EVENT_SET_ID>"
                    }
                ],
                "retention_seconds": 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "eq",
                            "value": "Purchase"
                        },
                        {
                            "operator": "or",
                            "filters": [
                                {
                                    "field": "custom_data.color",
                                    "operator": "eq",
                                    "value": "blue"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#)

## Boas práticas


- Experimente com diferentes públicos, por exemplo, pessoas que compraram com frequência no passado e não voltaram recentemente ou pessoas que só compraram de uma categoria.
- Crie públicos semelhantes com base nos públicos de melhor desempenho.
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#)[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#)Nesta Página[Públicos Personalizados offline](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#p-blicos-personalizados-offline)[Criar um público](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#create)[Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#audiencerules)[Exemplo de regras de Público Personalizado offline](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#exemplo-de-regras-de-p-blico-personalizado-offline)[Boas práticas](https://developers.facebook.com/docs/marketing-api/audiences/guides/offline-custom-audiences#boas-pr-ticas) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eJjOOn4b3tS5uG07S-J0z7uMaEbK6cYyuef1GPPQinK3fkShAL1Ac8N9IBg_aem__gtnJbuIGD8RGd_d1gTBQg&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4KJ7INgMgmOKchJV4VAhEPjAmkDyipPHZddKPtRLer277VvZ8_5DgqNgADmQ_aem_s8bJIfm6uRBSLbCzVTpk7w&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51im91aGSE4TVFpPfqzzU0EjJ0e07K56sTMjg6yOjqN_pASjrv6hJZAtNC_w_aem_lM6m3lcRMcBRACi3jzs90w&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WYSMNrTVok46G5ATMm4NHUkPJugRtIbsx0r-PiShWrV9MxYqZWk_OHUVvrg_aem_repHgq3C588fAViNLyGNQA&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EIg9ikU6zRPUpqJNrsjXjX307igWHTXDpm2Yf9vQIjxuuSip-EmbFNFS_OA_aem_Nk5-LLNK433ESRV8EZBFDw&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UzMYOlS2I28uBSST52mvZVkF59ccJ86J9FaBCZ-wK4jMgjf8uo8A158ow1g_aem_zJCAXU_WXQiAWZ_8d6LWcA&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eJjOOn4b3tS5uG07S-J0z7uMaEbK6cYyuef1GPPQinK3fkShAL1Ac8N9IBg_aem__gtnJbuIGD8RGd_d1gTBQg&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR51im91aGSE4TVFpPfqzzU0EjJ0e07K56sTMjg6yOjqN_pASjrv6hJZAtNC_w_aem_lM6m3lcRMcBRACi3jzs90w&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EIg9ikU6zRPUpqJNrsjXjX307igWHTXDpm2Yf9vQIjxuuSip-EmbFNFS_OA_aem_Nk5-LLNK433ESRV8EZBFDw&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6hpucVFpRX80IKupXA8naFBpdkr21WOK5xNDo41LEU-HuTmkBGLwWMf0GDlQ_aem_kOM3_BzFavnrgDbbP9CvwQ&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UzMYOlS2I28uBSST52mvZVkF59ccJ86J9FaBCZ-wK4jMgjf8uo8A158ow1g_aem_zJCAXU_WXQiAWZ_8d6LWcA&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4KJ7INgMgmOKchJV4VAhEPjAmkDyipPHZddKPtRLer277VvZ8_5DgqNgADmQ_aem_s8bJIfm6uRBSLbCzVTpk7w&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47kC4ISQL7HC2X3MgP1vKk8ySrOBFuTZj2oyBVQFb7Zn1Mkse2DxVcA2R3pQ_aem_w_z7Ah2vBrjNsgdhZD4EMQ&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WYSMNrTVok46G5ATMm4NHUkPJugRtIbsx0r-PiShWrV9MxYqZWk_OHUVvrg_aem_repHgq3C588fAViNLyGNQA&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eJjOOn4b3tS5uG07S-J0z7uMaEbK6cYyuef1GPPQinK3fkShAL1Ac8N9IBg_aem__gtnJbuIGD8RGd_d1gTBQg&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EIg9ikU6zRPUpqJNrsjXjX307igWHTXDpm2Yf9vQIjxuuSip-EmbFNFS_OA_aem_Nk5-LLNK433ESRV8EZBFDw&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6hpucVFpRX80IKupXA8naFBpdkr21WOK5xNDo41LEU-HuTmkBGLwWMf0GDlQ_aem_kOM3_BzFavnrgDbbP9CvwQ&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4bGr3-L6ojDOJOFqW4RK2FUOV13xYDDEb7QpmWC1AMgEPTY6fHHTrXSAgN1A_aem_1r_e0zG_E1VJaLW6ZhYFhQ&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4bGr3-L6ojDOJOFqW4RK2FUOV13xYDDEb7QpmWC1AMgEPTY6fHHTrXSAgN1A_aem_1r_e0zG_E1VJaLW6ZhYFhQ&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eJjOOn4b3tS5uG07S-J0z7uMaEbK6cYyuef1GPPQinK3fkShAL1Ac8N9IBg_aem__gtnJbuIGD8RGd_d1gTBQg&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT62uXk1Onelj6p2BQf3iHv82AkJb3LW18gxC9xUbmGXRzSu2A8u__pwGxnr3pPCyvPkEIGTJm588z919RHkYldDz50Ko_7uQoRolNOqgRWvSm0nOtzmZORJIZZSenHIQ8VCGtgiWCMIWrRwtRMAHWYbSWo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão