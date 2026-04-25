<!-- Fonte: Referência da API - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/reference/v25.0 -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Referência da API de Marketing


#### Nós raiz da API de Marketing


Esta é uma lista completa de nós raiz da API de Marketing do Facebook, com links para documentos de referência sobre cada item. Para saber mais sobre a arquitetura da API e ver como chamar nós raiz e as respectivas bordas, consulte [Visão geral](https://developers.facebook.com/docs/graph-api/using-graph-api).


Para acessar todas as informações de referência, entre no Facebook primeiro.


| Nó | Descrição |
| --- | --- |
| /{AD_ACCOUNT_USER_ID} | Uma pessoa que cria anúncios no Facebook. Os usuários de anúncios podem ter funções em várias contas de anúncios. |
| /act_{AD_ACCOUNT_ID} | Representa a entidade empresarial que gerencia os anúncios. |
| /{AD_ID} | Contém informações sobre um anúncio, como elementos criativos e informações de mensuração. |
| /{AD_CREATIVE_ID} | O formato de imagem, carrossel, coleção ou anúncio de vídeo. |
| /{AD_SET_ID} | Contém todos os anúncios com o mesmo orçamento, cronograma, lance e direcionamento. |
| /{AD_CAMPAIGN_ID} | Define o objetivo da sua campanha. Contém um ou mais conjuntos de anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Usuário


### Bordas


| Borda | Descrição |
| --- | --- |
| /adaccounts | Todas as contas de anúncios associadas à pessoa. |
| /accounts | Todas as páginas e os locais nos quais uma pessoa atua como administrador. |
| /promotable_events | Todos os eventos criados ou de páginas que possam ser promovidos e que pertençam a páginas nas quais você atua como administrador. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Conta de anúncios


Todas as coleções de objetos de anúncio das APIs de Marketing pertencem a uma [conta de anúncios](https://developers.facebook.com/docs/reference/ads-api/adaccount).


### Bordas


As bordas mais populares do nó de conta de anúncios. Acesse a [referência de bordas da conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-account#edges) para ver uma lista com todas as bordas.


| Borda | Descrição |
| --- | --- |
| /adcreatives | Define a aparência e o conteúdo do anúncio. |
| /adimages | Biblioteca de imagens para usar em criativos de anúncios. É possível carregar e gerenciar de forma independente. |
| /ads | Os dados de um anúncio, como elementos criativos e informações de mensuração. |
| /adsets | Contém todos os anúncios com o mesmo orçamento, cronograma, lance e direcionamento. |
| /advideos | Biblioteca de vídeos para uso em criativos de anúncios. É possível carregar e gerenciar de forma independente. |
| /campaigns | Define o objetivo das campanhas e contém um ou mais conjuntos de anúncios. |
| /customaudiences | Os Públicos Personalizados que pertencem ou são compartilhados com essa conta de anúncios. |
| /insights | Interface de informações. Elimina resultados duplicados em objetos filhos e fornece classificações e relatórios assíncronos. |
| /users | Lista de pessoas associadas a uma conta de anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Anúncio


Um anúncio individual associado ao conjunto de anúncios.


### Bordas


As bordas mais populares do nó de anúncio. Acesse a [referência de bordas de anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup#edges) para ver uma lista com todas as bordas.


| Borda | Descrição |
| --- | --- |
| /adcreatives | Define a aparência e o conteúdo do anúncio. |
| /insights | Insights sobre seu desempenho de publicidade. |
| /leads | Os leads associados ao anúncio de lead. |
| /previews | Gera prévias com base em um anúncio existente. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Conjunto de anúncios


Um conjunto de anúncios é um grupo de anúncios com o mesmo orçamento diário ou total, programação, tipo de lance, informações do lance e dados de direcionamento.


### Bordas


As bordas mais populares do nó de conjunto de anúncios. Acesse a [referência de bordas do conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) para ver uma lista com todas as bordas.


| Borda | Descrição |
| --- | --- |
| /activities | Registro das ações executadas no conjunto de anúncios. |
| /adcreatives | Define o conteúdo e a aparência do anúncio. |
| /ads | Os dados necessários de um anúncio, como elementos criativos e informações de mensuração. |
| /insights | Insights sobre seu desempenho de publicidade. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Campanha de anúncio


A campanha é o nível mais alto da estrutura organizacional da conta de anúncios e deve representar um objetivo único para o anunciante.


### Bordas


As bordas mais populares do nó de campanha de anúncios. Acesse a [referência de bordas de campanha de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group) para ver uma lista com todas as bordas.


| Borda | Descrição |
| --- | --- |
| /ads | Os dados necessários de um anúncio, como elementos criativos e informações de mensuração. |
| /adsets | Contém todos os anúncios com o mesmo orçamento, cronograma, lance e direcionamento. |
| /insights | Insights sobre seu desempenho de publicidade. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)

## Criativo do anúncio


O formato que fornece o layout e o conteúdo do anúncio.


### Bordas


As bordas mais populares do nó de criativo do anúncio. Acesse a [referência de bordas do criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative#edges) para ver uma lista com todas as bordas.


| Borda | Descrição |
| --- | --- |
| /previews | Gera prévias de anúncio com base em um objeto de criativo do anúncio existente. |

[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)[○](https://developers.facebook.com/docs/marketing-api/reference/v25.0#)Nesta Página[Referência da API de Marketing](https://developers.facebook.com/docs/marketing-api/reference/v25.0#refer-ncia-da-api-de-marketing)[Usuário](https://developers.facebook.com/docs/marketing-api/reference/v25.0#user)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#user_edges)[Conta de anúncios](https://developers.facebook.com/docs/marketing-api/reference/v25.0#account)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#account_edges)[Anúncio](https://developers.facebook.com/docs/marketing-api/reference/v25.0#ad)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#ad_edges)[Conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/v25.0#adset)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#adset_edges)[Campanha de anúncio](https://developers.facebook.com/docs/marketing-api/reference/v25.0#campaign)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#campaign_edges)[Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/v25.0#creative)[Bordas](https://developers.facebook.com/docs/marketing-api/reference/v25.0#creative_edges) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6yungKHSc_IHIbJemf_Shbs84ly07znejH68uAxiVGSOiY5YvmwMlYOxGFSw_aem_eRPTJCbhuqRhNn2YmXPAOA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iP3RXIre2bv2Rf7TZLvI7RAE39HqGvyVNo-01LFBgKLf2VUNn-Mls69WcBg_aem_RNZ3qk42hUFaA_uO81_WDA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6MCMUx0Cr67fKgyvf6r4I1ktAP_KiL0wdHwBK7R1lr0txzjERGFnCPmWfQUg_aem_ewHngXxoyEAePLjgoe1gVg&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NRrCC-PyyvNLIIBFpueSaz_v9PFVvHvLJyHQSaoHU5iD8tknJIKMzXu8owA_aem_E87yPl7Npj85SU_ctPmEpQ&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iP3RXIre2bv2Rf7TZLvI7RAE39HqGvyVNo-01LFBgKLf2VUNn-Mls69WcBg_aem_RNZ3qk42hUFaA_uO81_WDA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5f5w9NvzscpGCGZZ_5nwxlFt5UD-Fsv9pFbTu4HVGLmyBGP8xQssFgyFTZNA_aem_PKau1iiFcff_PUd4OHsYsw&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7iP3RXIre2bv2Rf7TZLvI7RAE39HqGvyVNo-01LFBgKLf2VUNn-Mls69WcBg_aem_RNZ3qk42hUFaA_uO81_WDA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5PTeumgpAzvmoBB-RqjvMVewI672QMsAcHkL1isw5sLuSPM-X0h7ynDrq7qg_aem_3m8GX1tvleQan3thU1Q8gA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NRrCC-PyyvNLIIBFpueSaz_v9PFVvHvLJyHQSaoHU5iD8tknJIKMzXu8owA_aem_E87yPl7Npj85SU_ctPmEpQ&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6yungKHSc_IHIbJemf_Shbs84ly07znejH68uAxiVGSOiY5YvmwMlYOxGFSw_aem_eRPTJCbhuqRhNn2YmXPAOA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6wv8nzOxcKJbP6cl_OF4Zjqow-bSiXgFzo2DZsc0RphwiD6WjLrmVkwmz82g_aem_MBUHOBPtkbTHzTEeBovFSA&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5f5w9NvzscpGCGZZ_5nwxlFt5UD-Fsv9pFbTu4HVGLmyBGP8xQssFgyFTZNA_aem_PKau1iiFcff_PUd4OHsYsw&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4ittw5o5quwixdIU1aUI_am4IHUxA3Y98uaT69sFbgSAvmFFAqTD2DE2M1kg_aem_rVIaDps7gJ3CiazqYzSc2Q&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://metastatus.com/?fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5f5w9NvzscpGCGZZ_5nwxlFt5UD-Fsv9pFbTu4HVGLmyBGP8xQssFgyFTZNA_aem_PKau1iiFcff_PUd4OHsYsw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4g0NYihF2vj8g-MeViIumNDIvKgTsD2IkFdyQtjzVJQAQ6WBDz4qYirAhDNhue0X79xI9AjZF43_c793YGk7jx80xpKTLT8RvCJI0_hRjuphnshy63iuXAuZs3al5HqLlcpDFpVIczBhbT91ln9rm8ZM8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão