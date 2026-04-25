<!-- Fonte: Descrição do direcionamento - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Descrição do direcionamento


Tenha descrições legíveis para um conjunto de especificações de direcionamento. Para ler descrições de direcionamento para [`ads`](https://developers.facebook.com/docs/reference/ads-api/adgroup/) específicos, crie um `HTTP GET` para `https://graph.facebook.com/{AD_ID}/targetingsentencelines`.


## Descrição de direcionamento para anúncios existentes


Para obter uma conexão com `targetingsentencelines` de um anúncio existente:

```
curl -G \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>/targetingsentencelines
```


A resposta:

```
{
    "id": "<AD_ID>/targetingsentencelines",
    "targetingsentencelines": [
    {
        "content": "Location - Living In:",
        "children": [
            "Japan",
            "United States"
        ]
    },
    {
        "content": "Age:",
        "children": [
            "20 - 24"
        ]
    },
    {
        "content": "Gender:",
        "children": [
            "Male"
        ]
    }]
}
```


As respostas contêm os seguintes campos:


| Nome | Descrição |
| --- | --- |
| id tipo: string | ID de targetingsentencelines . |
| targetingsentencelines Tipo: matriz de objetos JSON | Descrição legível da especificação de direcionamento. Cada objeto contém o tipo de direcionamento ou content e a especificação de direcionamento ou children . Este campo só considera posicionamentos efetivos . |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#)

## Descrição de direcionamento para contas de anúncios


É possível também obter descrições para uma especificação de direcionamento com um `HTTP GET` para uma conta de anúncios em `https://graph.facebook.com/{AD_ACCOUNT_ID}/targetingsentencelines`.


Por exemplo, para obter descrições de direcionamento para homens de 20 a 24 anos que vivem nos EUA ou no Japão:

```
curl -G \ --data-urlencode 'targeting_spec={ "age_max": 24, "age_min": 20, "genders": [1], "geo_locations": {"countries":["US","JP"]} }' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/targetingsentencelines
```


Resposta:

```
{
    "params": {
        "genders": [1],
        "age_min": 20,
        "age_max": 24,
        "geo_locations": {
            "countries": [
                "US",
                "JP"
            ]
        }
    },
    "targetingsentencelines": [{
        "content": "Location - Living In:",
        "children": [
            "Japan",
            "United States"
        ]
    }, {
        "content": "Age:",
        "children": [
            "20 - 24"
        ]
    }, {
        "content": "Gender:",
        "children": [
            "Male"
        ]
    }]
}
```


Alguns outros parâmetros são:


| Nome | Descrição |
| --- | --- |
| targeting_spec Tipo: objeto JSON | Obrigatório. Obter descrição para essas especificações de direcionamento. |
| hide_targeting_spec_from_return Tipo: booliano | Opcional. Se a resposta solicitou a inclusão de targeting_spec . O padrão é false . |


As respostas têm os seguintes campos:


| Nome | Descrição |
| --- | --- |
| targetingsentencelines Tipo: matriz de objetos JSON | A descrição legível da especificação de direcionamento. Cada objeto contém o tipo de direcionamento ou content e a especificação de direcionamento ou children . |
| params Tipo: objeto JSON | A especificação de direcionamento que você definiu. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#)Nesta Página[Descrição do direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#descri--o-do-direcionamento)[Descrição de direcionamento para anúncios existentes](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#descri--o-de-direcionamento-para-an-ncios-existentes)[Descrição de direcionamento para contas de anúncios](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description#descri--o-de-direcionamento-para-contas-de-an-ncios) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UBv2LhxdZc8JcHtGvUR9c1Dl6khTrr67WlB80MUDZ0XCFEBs95vZT5grBfA_aem_YcVoJTgqQ5yHIc65q1fSUg&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5UBv2LhxdZc8JcHtGvUR9c1Dl6khTrr67WlB80MUDZ0XCFEBs95vZT5grBfA_aem_YcVoJTgqQ5yHIc65q1fSUg&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7TpDSIXuKSkQg9h68U3cHBGRCHXjtQ_latQL_UYG9urBXm4874uxIc4WmgQw_aem_5kc2D-IzQH8Bvm-IbnpQgg&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4lw3AmUJnnh75TFDi8KhBGKcfbM_kFcBppnUEsDL5oX8rv5DgZkwX97MetCg_aem_gKRFHoRYPC9DbWwXiIQ39w&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_jj4b5n8900rZwt_92uFFIb1sOeEVoikMJu5mWemAwsS2lEyXemFXVoHqbw_aem_iG-Zow3U_nAwBTZoNEJGmQ&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4lw3AmUJnnh75TFDi8KhBGKcfbM_kFcBppnUEsDL5oX8rv5DgZkwX97MetCg_aem_gKRFHoRYPC9DbWwXiIQ39w&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR41rlvgTmrLyIEAdLZ1-czedhG9vVkRWWArBl7JXcS7mU3w0aXqS7WZHzePCQ_aem_OdjvDCU4qf32DIaeALg88w&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR41rlvgTmrLyIEAdLZ1-czedhG9vVkRWWArBl7JXcS7mU3w0aXqS7WZHzePCQ_aem_OdjvDCU4qf32DIaeALg88w&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jnAm3Ry5zENS0fiIFmbgjKM8ko-9PlInF5F0PLn3Cbd3CvFyKUibzoyqW2A_aem_f6fWRCRFid-IQuSF-wat9A&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DhY_nwvvqa4TI5HdnkGg5hXm7GTQev9R1clsKudPX26MNFNJhi25SJ-Z0Jg_aem_fjmhsAlNae-1MrW5C4mmRQ&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hhUv93tT288W-lwt1bXdSXlH2DMXrTLgmIspY9BTzrxuq54x_r4ofCdN1xQ_aem_-hYv5GuD1eVrVgeGcqm-Uw&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_jj4b5n8900rZwt_92uFFIb1sOeEVoikMJu5mWemAwsS2lEyXemFXVoHqbw_aem_iG-Zow3U_nAwBTZoNEJGmQ&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5LJN5pfa1L0c0flxA49yMtL9RYxU8qX-Xy5mKu62F6v9-GNPWezkbY7HXigA_aem_77QbJWbtRYFlk0PfLsSvjA&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DhY_nwvvqa4TI5HdnkGg5hXm7GTQev9R1clsKudPX26MNFNJhi25SJ-Z0Jg_aem_fjmhsAlNae-1MrW5C4mmRQ&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4gM4PdEgUAqFagcUbtpbMrXChoc6sNQIHrcPBJNzbdo9KAobj21yc2HF0KdA_aem_Ns7Q-ui6i8Lvf5Ehfu5J7Q&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5LJN5pfa1L0c0flxA49yMtL9RYxU8qX-Xy5mKu62F6v9-GNPWezkbY7HXigA_aem_77QbJWbtRYFlk0PfLsSvjA&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jnAm3Ry5zENS0fiIFmbgjKM8ko-9PlInF5F0PLn3Cbd3CvFyKUibzoyqW2A_aem_f6fWRCRFid-IQuSF-wat9A&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5hhUv93tT288W-lwt1bXdSXlH2DMXrTLgmIspY9BTzrxuq54x_r4ofCdN1xQ_aem_-hYv5GuD1eVrVgeGcqm-Uw&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR41rlvgTmrLyIEAdLZ1-czedhG9vVkRWWArBl7JXcS7mU3w0aXqS7WZHzePCQ_aem_OdjvDCU4qf32DIaeALg88w&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jnAm3Ry5zENS0fiIFmbgjKM8ko-9PlInF5F0PLn3Cbd3CvFyKUibzoyqW2A_aem_f6fWRCRFid-IQuSF-wat9A&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4cVjfoC4HUweftYKvJhdX1n5svR3GSirp12CpoNfqI8Tb5R47lpS2aEnjqOG8TrHNHAabXIpbT8HvgaoBx3nLz3B0cwym4f7BsbMW6Ke9WwOKgTUiExUz8yFpKl3j_Z63xyWEYGr7-coOzSV0P8d5A3yc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão