<!-- Fonte: Extensões de produto para criativo Advantage+  - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Extensões de produto para criativo Advantage+


As [extensões de produto (recurso "Adicionar itens de catálogo" no Gerenciador de Anúncios da Meta)](https://www.facebook.com/business/help/336325168874197) são uma otimização do criativo Advantage+ que mostra os produtos do seu catálogo abaixo da mídia única estática quando há probabilidade de melhorar o desempenho. Este documento mostra como utilizar os recursos de extensões de produto para anúncios.


#### Suporte à API para extensões de produto


A implementação do criativo de extensão de produto é compatível com todas as versões da API de Marketing. Porém, todas as solicitações de criação qualificadas para extensões de produto a partir da versão 20.0 precisam especificar se o anúncio usará a funcionalidade ou não. O campo `enroll_status` precisa ser fornecido com um valor `OPT_IN` ou `OPT_OUT`.


## Critérios de qualificação


- Campanha com objetivo `SALES` ou `TRAFFIC`
- Formato de anúncio de imagem ou vídeo único
- Um catálogo
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#)

## Antes de começar


Siga as etapas abaixo para configurar suas campanhas de anúncios.


- [Criar uma campanha](https://developers.facebook.com/docs/marketing-apis/get-started/#campaign)
- [Criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-apis/get-started/#ad-set-budget)


### Implementação de criativo independente


#### Antes


```
curl -X POST \
  -F 'name=Product Extension Creative' \
  -F 'object_story_spec={
      "link_data": {
         "link": "<URL>",
      },
      "page_id": "<PAGE_ID>",
      "instagram_actor_id": "<INSTAGRAM_ACTOR_ID>",
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Depois (os campos novos são destacados em negrito)


```
curl -X POST \
  -F 'name=Product Extension Creative' \
  -F 'object_story_spec={
      "link_data": {
         "link": "<URL>",
      },
      "page_id": "<PAGE_ID>",
      "instagram_actor_id": "<INSTAGRAM_ACTOR_ID>",
  }' \
  -F 'creative_sourcing_spec={
    "associated_product_set_id": "<PRODUCT_SET_ID>",
  }' \
  -F 'degrees_of_freedom_spec={
    "creative_features_spec": {
      "product_extensions": {
        "enroll_status": "OPT_IN",
        "action_metadata": {
           "type": "MANUAL",
        },
      },
    },
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Criação de anúncios


#### Antes


```
curl -X POST \
  -F 'creative={
    "object_story_spec": {
      "page_id": "<PAGE_ID>",
      "link_data": {
        "link": "<WEBSITE_URL>",
      }
    },
  }' \
  -F "adset_id=<ADSET_ID>" \
  -F "name=New Ad" \
  -F "status=PAUSED" \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


#### Depois (os campos novos estão em negrito)


```
curl -X POST \
  -F 'creative={
    "object_story_spec": {
      "page_id": "<PAGE_ID>",
      "link_data": {
        "link": "<WEBSITE_URL>",
      }
    },
    "creative_sourcing_spec": {
      "associated_product_set_id": "<PRODUCT_SET_ID>",
    },
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "product_extensions": {
          "enroll_status": "OPT_IN",
          "action_metadata": {
            "type": "MANUAL"
          },
        }
      }
    }
  }' \
  -F "adset_id=<ADSET_ID>" \
  -F "name=New Ad" \
  -F "status=PAUSED" \
  -F "access_token=<ACCESS_TOKEN>" \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Parâmetros


| Nome | Descrição |
| --- | --- |
| `product_extensions` | As extensões de produto são uma otimização de criativos Advantage+ que mostra os produtos do seu catálogo abaixo da mídia única estática quando houver probabilidade de melhorar o desempenho. Defina o campo enroll_status com OPT_IN para habilitá-lo. Pode ser adicionado a creative_features_spec . Para obter mais detalhes, consulte a documentação de referência Ad Creative Features Details . |
| `associated_product_set_id` | Especifica a identificação do conjunto de produtos para extensões de produto na otimização do criativo Advantage+. Este conjunto de produtos será mostrado abaixo da sua mídia única. Pode ser adicionado a creative_sourcing_spec . Para obter mais detalhes, consulte a documentação de referência Ad Creative Sourcing Spec . |

[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#)

## Saiba mais


### Central de Ajuda para Empresas


- [Sobre Adicionar itens do catálogo](https://www.facebook.com/business/help/336325168874197)


### Referência da API de Marketing


- [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative#fields)
- [Ad Creative Degrees Of Freedom Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-degrees-of-freedom-spec/)
- [Ad Creative Features Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-features-spec/)
- [Ad Creative Feature Details](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-feature-details/)
- [Ad Creative Object Story Spec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/)
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#)Nesta Página[Extensões de produto para criativo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#extens-es-de-produto-para-criativo-advantage-)[Critérios de qualificação](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#crit-rios-de-qualifica--o)[Antes de começar](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#antes-de-come-ar)[Implementação de criativo independente](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#implementa--o-de-criativo-independente)[Criação de anúncios](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#cria--o-de-an-ncios)[Parâmetros](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#par-metros)[Saiba mais](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#saiba-mais)[Central de Ajuda para Empresas](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#central-de-ajuda-para-empresas)[Referência da API de Marketing](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/product-extensions#refer-ncia-da-api-de-marketing) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6MfW5QyRXmmHUbHGU_yOgfS8Fu5yz5HWv3TnGVdr0Ts1jGLs4FaG3yPGtnJQ_aem_e4H9te4IR3F-zimT9GYZXg&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5h4ds_upj2T1bh8zCPyKiF5Aw6WJd2vviKXNkiwfz5L1Gad-Yu25rlNNlXvA_aem_eev1GXEmzRL-rLDd0iHSOw&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOWzRhRE-YUH8ng5qC_NVZYWYR5wEi8MtmBknlODq5qwiNtwmrx3eM6raLA_aem_SC-p6EB3E8i6ut4bSMrFPA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOWzRhRE-YUH8ng5qC_NVZYWYR5wEi8MtmBknlODq5qwiNtwmrx3eM6raLA_aem_SC-p6EB3E8i6ut4bSMrFPA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LfGAFH64cLMHU51nxmsYyxb8uWGgdYEySFcb_U7UJc6W-IHKZupFC7lm68Q_aem_snSw5wEEvT7fQDP5bXPaeg&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7TPAx84edPK_BFUm3Iv0MDHLJzh3cA39heFc5Rl2uPnHSNIARWWErgB3SvqA_aem_q23K0X-kkxTnGx4NwEgGow&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7TPAx84edPK_BFUm3Iv0MDHLJzh3cA39heFc5Rl2uPnHSNIARWWErgB3SvqA_aem_q23K0X-kkxTnGx4NwEgGow&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4CXaGDx7Q0fElVgemksVAn66rYFqNB5AcxH2GECVV9lqWfMBLcsKDKYrRwOA_aem_s0REYitbeGVLSrrqx1bu8Q&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7sUJZjilp2qd03jIXpKIddfUU_go1B1TgfDoLpJajPBa7ionIywHHGH8Xs0Q_aem_YdgWc0Kams5OhdyzLO36bA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EgHIFen2Fi2wYkSHYzE5G1XiXrQtRPWo3KHCZbs32gnbwkZkyKPhPsjF4oA_aem_Fvjynl1_fxVqXogwAWqJFQ&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOWzRhRE-YUH8ng5qC_NVZYWYR5wEi8MtmBknlODq5qwiNtwmrx3eM6raLA_aem_SC-p6EB3E8i6ut4bSMrFPA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EgHIFen2Fi2wYkSHYzE5G1XiXrQtRPWo3KHCZbs32gnbwkZkyKPhPsjF4oA_aem_Fvjynl1_fxVqXogwAWqJFQ&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7TPAx84edPK_BFUm3Iv0MDHLJzh3cA39heFc5Rl2uPnHSNIARWWErgB3SvqA_aem_q23K0X-kkxTnGx4NwEgGow&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7sUJZjilp2qd03jIXpKIddfUU_go1B1TgfDoLpJajPBa7ionIywHHGH8Xs0Q_aem_YdgWc0Kams5OhdyzLO36bA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4AOWzRhRE-YUH8ng5qC_NVZYWYR5wEi8MtmBknlODq5qwiNtwmrx3eM6raLA_aem_SC-p6EB3E8i6ut4bSMrFPA&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7TPAx84edPK_BFUm3Iv0MDHLJzh3cA39heFc5Rl2uPnHSNIARWWErgB3SvqA_aem_q23K0X-kkxTnGx4NwEgGow&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4T_5t26a71bB7BkR46yOLxMRc_qq4SoHNLQBhz-ykKjm3pK4KbrQ8kXmxM-A_aem_E7uGhyOn-00ryIv5NST2ng&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6MfW5QyRXmmHUbHGU_yOgfS8Fu5yz5HWv3TnGVdr0Ts1jGLs4FaG3yPGtnJQ_aem_e4H9te4IR3F-zimT9GYZXg&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7EgHIFen2Fi2wYkSHYzE5G1XiXrQtRPWo3KHCZbs32gnbwkZkyKPhPsjF4oA_aem_Fvjynl1_fxVqXogwAWqJFQ&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4CXaGDx7Q0fElVgemksVAn66rYFqNB5AcxH2GECVV9lqWfMBLcsKDKYrRwOA_aem_s0REYitbeGVLSrrqx1bu8Q&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5PPmXLBTq5PXkpnnh9-eWFNMSu6nS5fFzO0PWA-SAje3bwRMaHIOjJN5c6359hQVAKbwUXo9Ju1ZTv5BAydHKOrEIu_b3NoHz-z47ijiEWX3th6bHqPzpd40oFgZv7-mDCrzFE9UIDysfdtdH1T-dbaeI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão