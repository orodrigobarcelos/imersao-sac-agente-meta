<!-- Fonte: Volume de anúncios.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Volume de anúncios


Veja o volume de anúncios *em veiculação ou em análise* das suas contas de anúncios. Esses anúncios são contabilizados no limite de anúncios por página instituído no início de 2021. Consulte o número de anúncios em veiculação ou em análise de determinada conta de anúncios.


## Ver volume da sua conta de anúncios


Para ver o volume de anúncios da sua conta:

```
curl -G \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/v<API_VERSION>/act_<AD_ACCOUNT_ID>/ads_volume"
```


**Resposta**

```
{"data":[{"ads_running_or_in_review_count":2}]}
```


Consulte [Sobre o gerenciamento do volume de anúncios](https://www.facebook.com/business/help/2720085414702598) para mais informações.
[○](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#)

## Verificar status em veiculação ou em análise


Para ver se um anúncio está em veiculação ou em análise, verifique `effective_status`, `configured_status` e o status da conta de anúncios:


- Se o `effective_status` de um anúncio for `1` - `active`, isso significa que o estado dele é *em veiculação ou em análise*.
- Se o `configured_status` de um anúncio for `active` e o `effective_status` for `9` - `pending review` ou `17` - `pending processing`, isso significa que o anúncio está *em veiculação* ou *em análise*.
- O anúncio só poderá estar *em veiculação* ou *em análise* se o status da conta de anúncio for `1` - `active`, `8` - `pending settlement` ou `9` - `in grace period`.


Também determinamos se um anúncio está em veiculação ou em análise com base na programação do conjunto de anúncios:


- Se a hora de início for anterior à atual e a hora atual for anterior à hora de término, isso significa que o anúncio está em veiculação ou em análise.
- Se a hora de início for anterior à atual e o conjunto de anúncios não tiver uma hora de término, isso também significa que o anúncio está em veiculação ou em análise.


Por exemplo, se a veiculação do conjunto de anúncios estiver programada para o futuro, isso significa que os anúncios não estão em veiculação ou em análise. No entanto, se a veiculação do conjunto de anúncios estiver programada entre agora e 3 meses no futuro, isso significa que os anúncios estão em veiculação ou em análise.


Se você estiver usando recursos especiais de programação de anúncios (como divisão do dia), consideraremos o anúncio como em veiculação ou em análise durante o *dia todo*, não só na parte do dia em que o anúncio começou a ser veiculado.
[○](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#)

## Detalhamento por atores


Use o campo `show_breakdown_by_actor` para obter um detalhamento dos limites de anúncios por um `actor_id` específico:

```
curl -G \
  -d "show_breakdown_by_actor=true" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/v<API_VERSION>/act_<AD_ACCOUNT_ID>/ads_volume"
```


**Resposta**

```
{
  "data": [
    {
      "ads_running_or_in_review_count": 0,
      "current_account_ads_running_or_in_review_count": 0,
      "actor_id": "<ACTOR_ID_1>",
      "recommendations": [
      ]
    },
    {
      "ads_running_or_in_review_count": 2,
      "current_account_ads_running_or_in_review_count": 2,
      "actor_id": "<ACTOR_ID_2>",
      "recommendations": [
      ]
    }
  ],
}
```


Use `page_id` para obter os limites de anúncios de uma página específica:

```
curl -G \
  -d "page_id=<PAGE_ID>" \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/v<API_VERSION>/act_<AD_ACCOUNT_ID>/ads_volume"
```


**Resposta**

```
{
  "data": [
    {
      "ads_running_or_in_review_count": 2,
      "current_account_ads_running_or_in_review_count": 2,
      "actor_id": "<ACTOR_ID>",
      "recommendations": [
      ]
    }
  ],
}
```


### Campos compatíveis


| Campo | Descrição |
| --- | --- |
| actor_id | Ator ao qual o limite é aplicado. No momento, ele é representado pela identificação da página. |
| ads_running_or_in_review_count | Número de anúncios em veiculação ou em análise de um ator específico. |
| current_account_ads_running_or_in_review_count | Número de anúncios em veiculação ou em análise de um ator específico na conta de anúncios atual. |
| actor_name | Ator ao qual o volume de anúncios foi agregado. No momento, ele é representado pelo nome da página. |
| ad_limit_scope_business | Usado quando uma conta de anúncios pertence a um Gerenciador de Negócios e está sujeita aos limites de anúncios no respectivo nível. Esse campo tem a empresa que define os limites de anúncio na conta de anúncios. |
| ad_limit_scope_business_manager_id | Usado quando uma conta de anúncios pertence a um Gerenciador de Negócios e está sujeita aos limites de anúncios no respectivo nível. Esse campo tem o ID do Gerenciador de Negócios de uma empresa que define os limites de anúncio na conta. |
| ad_limit_set_by_page_admin | Limite de anúncios definido por um administrador da página da empresa proprietária da conta. |
| ads_running_or_in_review_count_subject_to_limit_set_by_page | Número de anúncios em veiculação ou em análise de um grupo de contas. Nesse caso, o grupo pode conter contas de anúncios pertencentes a uma conta empresarial ou individual. Se o limite de anúncios não for definido pelo proprietário da página, o valor retornado será null . Se o limite de anúncios for definido pelo proprietário da página, o valor retornado será o número de anúncios em veiculação ou em análise no grupo de contas. |
| future_limit_activation_date | A data de início do limite de anúncios que entrará em vigor. |
| future_limit_on_ads_running_or_in_review | O limite de anúncios que entrará em vigor. Esse limite é relacionado ao número de anúncios em veiculação ou em análise de determinado ator. |
| limit_on_ads_running_or_in_review | O limite de anúncios atual do ID de determinado ator. Esse limite está relacionado ao número de anúncios em veiculação ou em análise. |
| recommendations | Recomendações para reduzir o volume de anúncios. Atualmente, os seguintes valores são compatíveis: zero_impression; learning_limited; top_campaigns_with_ads_under_cap; top_adsets_with_ads_under_cap Para mais informações, acesse a Central de Ajuda para Empresas . |


### Parâmetros


| Campo | Descrição |
| --- | --- |
| recommendation_type | Tipo de recomendação para reduzir o volume de anúncios. Atualmente, os seguintes valores são compatíveis: zero_impression; learning_limited; top_campaigns_with_ads_under_cap; top_adsets_with_ads_under_cap Saiba mais Sobre o gerenciamento do volume de anúncios . |

[○](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#)[○](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#)Nesta Página[Volume de anúncios](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#volume-de-an-ncios)[Ver volume da sua conta de anúncios](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#ver-volume-da-sua-conta-de-an-ncios)[Verificar status em veiculação ou em análise](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#view-status)[Detalhamento por atores](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#breakdown-by-actors)[Campos compatíveis](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#campos-compat-veis)[Parâmetros](https://developers.facebook.com/docs/marketing-api/insights-api/ads-volume#par-metros) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_1KA9QEiL0ZAuePKyb5D2a1q5FXuysx_VcD0shDphGgM7YXaN8192mf9wmQ_aem_7yA23LyVaEbr30wvIl5U7Q&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dmo3hl1l44WGDuUoguxVRl9A4dbuKRDKKGRKsACAECKbqtGWpjp5NLcsgQg_aem_kYXrdYSuErSJ--z80ONGtg&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nKSrGYkAg0b_ehmHILCL4yYEwrbUBdle9vluw92huJ2Y7doSbscBadKny2w_aem_G9bHDR-rxFSpoQcEZjNpyw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_6SYrs1cIb1PvYV1ZK5lfSIevWMocrW2hxEI6l9nvRgfOQeBgRbMfw_XxUQ_aem_leVcYZPUOicVpGMXB6nDSA&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6WZIczIvpmpknD8CKdsUZge1P_aMvOcvwDQ5-BUQ8lc1nzLBvQMUdsr8ZkIQ_aem_uz9PVy8gax85vC8WlVpLBw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_6SYrs1cIb1PvYV1ZK5lfSIevWMocrW2hxEI6l9nvRgfOQeBgRbMfw_XxUQ_aem_leVcYZPUOicVpGMXB6nDSA&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7Bz4bd7UUEFeCt0lg0bpZ0O-iRbfA0JSWOpKcJ3-mYK6rciIhp85PAtUuohA_aem_pe4B4pwju1MauPYLs5NyGQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR46stq1yoU-RUuEZF9kUcOB3rsUGc9X8F_4rKPGKKvKb_WES_nRrkj6VY3xHg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR46stq1yoU-RUuEZF9kUcOB3rsUGc9X8F_4rKPGKKvKb_WES_nRrkj6VY3xHg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6C_TZAEnF_9GNfcxXMd_Iga_WSSvMC9pv7WtpBoW97j5mOg-umZ3mexO_pPQ_aem_hA_O283mDGw1jUC_xZp-Rw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6yXAHknfU0dWrfJp9YN53Ds-lQBP5tMw0xc3Yz0ApeND2jt_XXMwWDtFQrDg_aem_hkmMME8ns_yxsMvL6e-DRw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vGnffEJdVuSVTvSZWeSSzTbmSugVmGvLtVVcA2ByyeuNup_EKtoVQ42yqlg_aem_YPZlb-iP3Yp5p1eMuaQ7PQ&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nKSrGYkAg0b_ehmHILCL4yYEwrbUBdle9vluw92huJ2Y7doSbscBadKny2w_aem_G9bHDR-rxFSpoQcEZjNpyw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5_6SYrs1cIb1PvYV1ZK5lfSIevWMocrW2hxEI6l9nvRgfOQeBgRbMfw_XxUQ_aem_leVcYZPUOicVpGMXB6nDSA&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6yXAHknfU0dWrfJp9YN53Ds-lQBP5tMw0xc3Yz0ApeND2jt_XXMwWDtFQrDg_aem_hkmMME8ns_yxsMvL6e-DRw&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5lHHtTWYEon-OqHOJmbHAxDRQQAOPptZdAqZT7Np_hv7hBO5-LDjHc9GGF-ouEKTkpzPQH_06cubvb6-5YBWXxjGGwENFPu7eE0iT-TpvgEK6sSoqmklh_a5Z-WC_ltc8XjfAbUc3-0q6OVt1QoHJy8t0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão