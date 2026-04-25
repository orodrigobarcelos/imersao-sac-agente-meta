<!-- Fonte: Público Advantage+ - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Público Advantage+


Habilite o público Advantage+ nas suas campanhas para criar o público mais amplo possível para fazer pesquisas. As restrições comerciais não negociáveis NÃO são expandidas, incluindo restrições de localização, idade mínima, idioma e exclusões de público personalizado.


- Para aceitar, defina o parâmetro `advantage_audience` dentro de `targeting_automation` para `1`.
- Para recusar, defina o parâmetro `advantage_audience` dentro de `targeting_automation` para `0`.


Antes da versão 23.0, o parâmetro `advantage_audience` dentro do `targeting_automation` era opcional e não era explicitamente exigido para ser definido na especificação de direcionamento ao criar um novo conjunto de anúncios ou atualizar um existente.


A partir da versão 23.0, o parâmetro `advantage_audience` dentro do `targeting_automation` será automaticamente predefinido para `1` ou exigirá uma configuração explícita para `1` ou `0`. Esse comportamento aplica-se apenas ao criar um novo conjunto de anúncios, enquanto a atualização de um conjunto de anúncios existente não demonstrará esse comportamento em nenhuma versão.


## Habilitar o público Advantage+


Quando o público Advantage+ é habilitado, é possível definir o parâmetro `age_range` dentro de `targeting_spec`.

```
"targeting": { "age_range": [25, 35], "geo_locations": { "countries": ["GB"] }, "targeting_automation": { "advantage_audience": 1 } }
```


- Quando `age_range` não for enviado, a faixa etária será criada a partir de idade mínima/máxima.
- Quando o público Advantage+ está habilitado, os valores de idade mínima/máxima são redefinidos para valores padrão.
- Quando o público Advantage+ está habilitado, os anunciantes podem enviar valores `age_min` somente entre 18 e 25.
- Quando o público Advantage+ está habilitado, os anunciantes não podem definir valores `age_max`. Ele é definido como apenas 65.


### Exemplo de solicitação


```
curl -X POST \ -F 'name="advantage audience test"' \ -F 'is_autobid="true"' \ -F 'daily_budget="100"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'campaign_id="<CAMPAIGN ID>"' \ -F 'targeting={"age_max": 65, "age_min": 18, "age_range": [25,35], "geo_locations": {"countries": ["US", "GB"]},"targeting_automation": {"advantage_audience": 1 }}' \ -F 'access_token="<ACCESS_TOKEN>"' \ https://facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#)

## Casos aceitos padrão


O parâmetro `advantage_audience` dentro do `targeting_automation` será predefinido para `1` salvo se explicitamente especificado nos seguintes cenários:


- **Configuração de direcionamento padrão:** ao passar valores padrão para idade, gênero, inclusão de público personalizado e inclusão de direcionamento detalhado, ou omitir esses campos.
- **Configuração de direcionamento flexível:** ao usar uma configuração flexível aplicando configurações de relaxamento individuais para idade, gênero, inclusão de público personalizado e inclusão de direcionamento detalhado.


### Exemplos


#### Configuração padrão


```
{ "targeting":{ "geo_locations":{ "countries":[ "US" ] }, "age_max":65, "age_min":18, } }
```


#### Configuração flexível


```
{ "targeting":{ "age_max":65, "age_min":18, "custom_audiences":[ { "id":"<CUSTOM_AUDIENCE_ID>" }, { "id":"<LOOKALIKE_ID>" } ], "flexible_spec":[ { "interests":[ { "id":"<INTEREST_ID>" } ] } ], "geo_locations":{ "countries":[ "US" ], "location_types":[ "home", "recent" ] }, "targeting_relaxation_types":{ "custom_audience":1, "lookalike":1 }, "targeting_optimization":"expansion_all" } }
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#)

## Solução de problemas


Caso sua configuração não seja padrão ou flexível, ao criar um conjunto de anúncios, um erro será retornado, o que significa que você tem:


- Configurações não padrão usadas para qualquer idade, gênero, inclusão de público personalizado e inclusão de direcionamento detalhado.
- Configurações individuais de flexibilização não usadas para estes parâmetros.


### Exemplo


```
{ "targeting":{ "age_max":50, "age_min":30, "custom_audiences":[ { "id":"<CUSTOM_AUDIENCE_ID>" } ], "geo_locations":{ "countries":[ "US" ], "location_types":[ "home", "recent" ] } } }
```


Para resolver isso, será preciso definir explicitamente o parâmetro `advantage_audience` dentro de `targeting_automation` para `1` ou `0`.
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#)

## Saiba mais


- [Central de Ajuda: Sobre o público Advantage+](https://www.facebook.com/business/help/273363992030035).
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#)Nesta Página[Público Advantage+](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#p-blico-advantage-)[Habilitar o público Advantage+](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#habilitar-o-p-blico-advantage-)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#exemplo-de-solicita--o)[Casos aceitos padrão](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#casos-aceitos-padr-o)[Exemplos](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#exemplos)[Solução de problemas](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#solu--o-de-problemas)[Exemplo](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#exemplo)[Saiba mais](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BhRP8zQJwc9VAGY8_Jg9OFfHx-6mgPU7GJmnzAeAafrAPq2qh6jklQZwvpA_aem_T8XdFd5GkKjR2rXKrIMiBA&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BhRP8zQJwc9VAGY8_Jg9OFfHx-6mgPU7GJmnzAeAafrAPq2qh6jklQZwvpA_aem_T8XdFd5GkKjR2rXKrIMiBA&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7KTsRLaGVE0Fkrx5eD7PVQtq0ExaCSOQ74sQoViJsyzbrxW-uq8V_Z7imDdw_aem_O8FgMCEvlt6nvGi_YfYscg&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dkP__auIWkTXEhI13TTTFTjImh_Qesvmp4m1e_s1OHLVysz-pI7RcMDnaxA_aem_qKb5s0RLARVTcnm5pkZf7g&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_YWB7rQjKIR2X-KXLVvwSS4lWBhVo1nLaka365UdZq-kQhK5HXZ2kSxbHqw_aem_hcBr0ch1oiWKhWzSDi_ucA&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6IhJd-n17PCHNdaYUi6xFpMDR2TlMSut4jehIuFTFBhXddgF1IDezVsyntSA_aem_8T7uxgATYsd9KthgTVh6vw&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45vlePgE1RgM8VB0vAH14QnVsGPJo34xp1yzNHjXtBih9n1s8dJ25MqtflgA_aem_RZ3U0vqXkczrSymwTSExew&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7SoFrt-0jRhbuyWHTq8ZRz6E06T3qOMl5NEysKPZ0Mbw_U1J70hEYcQ-FqCg_aem_M0i0e93ZYjkEBSJJc7uVEA&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dkP__auIWkTXEhI13TTTFTjImh_Qesvmp4m1e_s1OHLVysz-pI7RcMDnaxA_aem_qKb5s0RLARVTcnm5pkZf7g&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6IhJd-n17PCHNdaYUi6xFpMDR2TlMSut4jehIuFTFBhXddgF1IDezVsyntSA_aem_8T7uxgATYsd9KthgTVh6vw&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6IhJd-n17PCHNdaYUi6xFpMDR2TlMSut4jehIuFTFBhXddgF1IDezVsyntSA_aem_8T7uxgATYsd9KthgTVh6vw&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7KTsRLaGVE0Fkrx5eD7PVQtq0ExaCSOQ74sQoViJsyzbrxW-uq8V_Z7imDdw_aem_O8FgMCEvlt6nvGi_YfYscg&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BhRP8zQJwc9VAGY8_Jg9OFfHx-6mgPU7GJmnzAeAafrAPq2qh6jklQZwvpA_aem_T8XdFd5GkKjR2rXKrIMiBA&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dkP__auIWkTXEhI13TTTFTjImh_Qesvmp4m1e_s1OHLVysz-pI7RcMDnaxA_aem_qKb5s0RLARVTcnm5pkZf7g&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR437_6vB5bg8n85tC8fBzlDPOTofeQUoNt0DYuN9vLah_0wNnw81YMi8h5KPw_aem_nDoZp6wayQQ1r5oUAgo4Kw&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dkP__auIWkTXEhI13TTTFTjImh_Qesvmp4m1e_s1OHLVysz-pI7RcMDnaxA_aem_qKb5s0RLARVTcnm5pkZf7g&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7KTsRLaGVE0Fkrx5eD7PVQtq0ExaCSOQ74sQoViJsyzbrxW-uq8V_Z7imDdw_aem_O8FgMCEvlt6nvGi_YfYscg&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5DtVGgtsnLdsUihMksL8clYM4VA5SYaVF-ixhrxzx3oNOSrwfxaQro0ZBg8A_aem_6WTY4hs5gWdGtAFo_1ix2A&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6IhJd-n17PCHNdaYUi6xFpMDR2TlMSut4jehIuFTFBhXddgF1IDezVsyntSA_aem_8T7uxgATYsd9KthgTVh6vw&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5A9L0DUXQhlRZDU66NJrqO1uP0cb6EQQGKsu-65LFu3eIb5yNa0bNc7HNAXA_aem__Fzz_WqfwEx2xQP_hM7lug&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5BQ0I-SlnM8I2QvHHG6Fp7sP9HtoKI9KVce2KGVnGweI39cU5P5xRske38iz5LYMGu-BxKIiTG2V3BahSEMHRM6BcBDIUbexzIm4P8oTo5-TSNSKmxdXz54e7evVlruuUn8k0BYYl8d_WUSd8hfX392pE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão