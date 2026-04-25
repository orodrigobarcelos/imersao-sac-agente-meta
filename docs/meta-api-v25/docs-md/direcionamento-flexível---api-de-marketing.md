<!-- Fonte: Direcionamento flexível - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Direcionamento flexível


Combine diversas opções de direcionamento para alcançar um conjunto específico de usuários em `flexible_spec` com declarações `AND` e `OR`. O Facebook avalia o direcionamento em `flexible_spec` via `AND` com todos os segmentos que não fazem parte da especificação, como idade, gênero e geolocalização. Além disso, é feita uma avaliação de cada elemento de matriz principal em `flexible_spec` com `AND` e outra de elementos de matriz secundários com `OR`.


Os segmentos de direcionamento, como comportamentos especificados em `flexible_spec`, não estão disponíveis para uso fora de `flexible_spec`.


## Campos


| Campo | Descrição |
| --- | --- |
| flexible_spec Tipo: objeto JSON | Matriz de matrizes. Cada uma contém um segmento de direcionamento em um formato adequado, como interesses, comportamentos e dados demográficos. A matriz principal tem um limite de 25, enquanto a matriz secundária tem um limite de 1.000. |


Use os seguintes campos no direcionamento flexível:


- `custom_audiences`
- `interests`
- `behaviors`
- `college_years`
- `education_majors`
- `education_schools`
- `education_statuses`
- `family_statuses`
- `income`
- `industries`
- `life_events`
- `user_adclusters`
- `work_positions`
- `work_employers`
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#)

## Exemplos


#### Direcionamento flexível


Para direcionar conteúdo a pessoas que vivem nos EUA, com 18 a 43 anos de idade, que **não** se mudaram recentemente **e** que gostam de viajar, de futebol ou de filmes **e** são recém-casadas ou gostam de música:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=150' \
  -F 'daily_budget=2000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "age_max": 43,
    "age_min": 18,
    "flexible_spec": [
      {
        "behaviors": [{"id":6002714895372,"name":"Frequent Travelers"}],
        "interests": [
          {"id":6003107902433,"name":"Association football (Soccer)"},
          {"id":6003139266461,"name":"Movies"}
        ]
      },
      {
        "interests": [{"id":6003020834693,"name":"Music"}],
        "life_events": [{"id":6002714398172,"name":"Newlywed (1 year)"}]
      }
    ],
    "geo_locations": {"countries":["US"]}
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v2.11/act_<AD_ACCOUNT_ID>/adsets
```


Com esta especificação flexível, o público resultante é:


(segmento 1 `or` segmento 2 `or` segmento 3) **e** (segmento 4 `or` segmento 5) **e** segmento 6

```
flexible_spec=
[
  {
    'segment_type':[segment1, segment2],
    'segment_type':[segment3]
  },
  {
    'segment_type':[segment4, segment5]
  },
  {
    'segment_type':[segment6]
  }
]
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#)Nesta Página[Direcionamento flexível](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#direcionamento-flex-vel)[Campos](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#campos)[Exemplos](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting#exemplos) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wkrihrvOVnyAeNfmFhhi66CjtZZMeaSz4LJZlioMak_Q-Ry2zDmniDiMBaw_aem_O9VrTg0CcKvFSYVN7MqJXg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jMWfBwIGvQqDeE85y4pp3Y94kFDO4yhlN6u2KRUJmcKtVk3Vy4SDSBPIEPg_aem_lDSyNQAuuY61yOBS2cYkIQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jsYUbWumoTek8F89gGFUHfmJYPmeREo0J2rJ15GNmCnJHWIuuVBRA5B2hKA_aem_Y1EIrT-xZjE7mwuc6zQ4-g&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6X6UImnb2BX5_V_LmUnak-HOirrfLavtPKzB6QELJgjQuPVVD3SZFW3aVvYA_aem_8nR8CSqW6cXRxn43e4wkiQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jsYUbWumoTek8F89gGFUHfmJYPmeREo0J2rJ15GNmCnJHWIuuVBRA5B2hKA_aem_Y1EIrT-xZjE7mwuc6zQ4-g&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jMWfBwIGvQqDeE85y4pp3Y94kFDO4yhlN6u2KRUJmcKtVk3Vy4SDSBPIEPg_aem_lDSyNQAuuY61yOBS2cYkIQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4PXRAscwOu9qa1Kedw3DVU-lzDLhBmGWoPX0dXplQqPg8Bl2iFnnsXjEHG9A_aem_JOUtoVT_WWWuZWFXncjbUQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Sjn1vbaaIqSP2UD1cEkx0cXQ8L9qvZuUIzPwEAiyYDv4MaKpNSe489s6puA_aem_ceENhlxQgeUuRePI3H7zqg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jMWfBwIGvQqDeE85y4pp3Y94kFDO4yhlN6u2KRUJmcKtVk3Vy4SDSBPIEPg_aem_lDSyNQAuuY61yOBS2cYkIQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wkrihrvOVnyAeNfmFhhi66CjtZZMeaSz4LJZlioMak_Q-Ry2zDmniDiMBaw_aem_O9VrTg0CcKvFSYVN7MqJXg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wkrihrvOVnyAeNfmFhhi66CjtZZMeaSz4LJZlioMak_Q-Ry2zDmniDiMBaw_aem_O9VrTg0CcKvFSYVN7MqJXg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jMWfBwIGvQqDeE85y4pp3Y94kFDO4yhlN6u2KRUJmcKtVk3Vy4SDSBPIEPg_aem_lDSyNQAuuY61yOBS2cYkIQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4z9NuF8Y-QWf_2TIeJOcCxqzyoMoTNcWAgglCJ6HfXxr8UBgRKT2gPPBWvFg_aem_X_6boQ-FDL4iXB5WznohWA&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Sjn1vbaaIqSP2UD1cEkx0cXQ8L9qvZuUIzPwEAiyYDv4MaKpNSe489s6puA_aem_ceENhlxQgeUuRePI3H7zqg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6jsYUbWumoTek8F89gGFUHfmJYPmeREo0J2rJ15GNmCnJHWIuuVBRA5B2hKA_aem_Y1EIrT-xZjE7mwuc6zQ4-g&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5WWqUXv7ZqpE5q39f8V8WkS3H1V1kuP8xWFgvebDcfWffSLXKprF_hcdRFRA_aem_Em-D2uJpZfGQ5NZHjTYn_g&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7od21kVmK2IAH5m1-Q5ZYDUPZU3OSr4KW8FcWtrM6X-SAJkacNS3eWZVP5fA_aem_x_h_sU1gkQHq_0Y06dn6rw&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6X6UImnb2BX5_V_LmUnak-HOirrfLavtPKzB6QELJgjQuPVVD3SZFW3aVvYA_aem_8nR8CSqW6cXRxn43e4wkiQ&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Sjn1vbaaIqSP2UD1cEkx0cXQ8L9qvZuUIzPwEAiyYDv4MaKpNSe489s6puA_aem_ceENhlxQgeUuRePI3H7zqg&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7od21kVmK2IAH5m1-Q5ZYDUPZU3OSr4KW8FcWtrM6X-SAJkacNS3eWZVP5fA_aem_x_h_sU1gkQHq_0Y06dn6rw&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4aa-mNdbBQJGqfuPP72E7TuicDXzqZDzmkv9exmq5PlH--0k8KEn0l8DzBsGjUBZvex_8v4RxD3fSVIOJeSYSzJpnkw4XmbKWcFwkRFesII38FVC6umw_wrNtQm6bOxZSh4xjKunaTcgUrkNZ89M2QVGs)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão