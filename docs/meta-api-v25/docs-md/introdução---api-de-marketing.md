<!-- Fonte: Introdução - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Introdução


Com a API de Marketing, você pode criar, mensurar e otimizar anúncios no Instagram usando o **Stream** principal, os **Stories**, a aba **Explorar** e o **Reels**. Para criar anúncios:


- Etapa 1: [obter a identificação da conta do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#account-id).
- Etapa 2: [criar uma campanha](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#campaign).
- Etapa 3: [criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#adset). Escolha um `placement` que inclua o Instagram. Recomendamos incluir o Facebook e o Instagram para que nosso sistema veicule automaticamente anúncios para os melhores públicos nas duas plataformas.
- Etapa 4: [fornecer um criativo](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#creative).
- Etapa 5: [programar a veiculação](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#ad).


É importante lembrar:


- Os anúncios do Instagram não são compatíveis com todos os objetivos de anúncios.
- Nem todos os formatos de criativos suportados pelo Facebook funcionam no Instagram.


Para usar os posts do Instagram e do Facebook como anúncios, consulte [Usar posts como anúncios do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads).


## Etapa 1: obter a identificação da conta do Instagram


Você precisa saber a identificação da sua conta do Instagram antes de começar a criar anúncios. Há diferentes maneiras de obter esse código, dependendo do tipo de conta:


| Tipo de conta do Instagram | Como encontrar a identificação da conta |
| --- | --- |
| Conta do Instagram no Gerenciador de Negócios (Recomendado) – Guia de implementação | Consulte Configurar contas do Instagram no Gerenciador de Negócios, Obter contas associadas . Salve a identificação para usar nos anúncios. |
| Contas do Instagram conectadas a uma Página – Guia de implementação | Consulte Configurar contas do Instagram com Páginas, Obter a identificação da conta . Salve a identificação para usar nos anúncios. |
| Conta do Instagram associada a uma Página (PBIA) – Guia de implementação | Consulte Configurar contas do Instagram com Páginas, Ler PBIA . Salve a identificação para usar nos anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)

## Etapa 2: criar uma campanha


Gerar objetos de anúncio para o Instagram é equivalente a criar anúncios do Facebook. Para começar, [crie uma campanha de anúncios do Facebook](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-campaign) e especifique o objetivo.


Os objetivos compatíveis com o Instagram variam de acordo com o posicionamento do anúncio escolhido:


| Posicionamento do anúncio | Objetivos compatíveis |
| --- | --- |
| Anúncios no Explorar | BRAND_AWARENESS , REACH , LINK_CLICKS , POST_ENGAGEMENT , APP_INSTALLS , VIDEO_VIEWS , LEAD_GENERATION , MESSAGES , CONVERSIONS e PRODUCT_CATALOG_SALES . |
| Anúncios na página inicial do Explorar do Instagram | BRAND_AWARENESS , REACH , LINK_CLICKS , APP_INSTALLS , VIDEO_VIEWS , LEAD_GENERATION , MESSAGES e CONVERSIONS . |
| Anúncios no feed do perfil do Instagram | BRAND_AWARENESS , REACH , LINK_CLICKS , POST_ENGAGEMENT , APP_INSTALLS , VIDEO_VIEWS , MESSAGES , CONVERSIONS e STORE_TRAFFIC |
| Anúncios nos resultados da pesquisa do Instagram | BRAND_AWARENESS , REACH , LINK_CLICKS , POST_ENGAGEMENT , APP_INSTALLS , VIDEO_VIEWS , LEAD_GENERATION , CONVERSIONS e PRODUCT_CATALOG_SALES . |
| Anúncios no Reels | BRAND_AWARENESS , REACH , LINK_CLICKS , APP_INSTALLS , VIDEO_VIEWS , MESSAGES e CONVERSIONS |
| Anúncios nos Stories | BRAND_AWARENESS , REACH , LINK_CLICKS , APP_INSTALLS , VIDEO_VIEWS , LEAD_GENERATION , MESSAGES , CONVERSIONS , PRODUCT_CATALOG_SALES e STORE_TRAFFIC . |
| Anúncios em streams | BRAND_AWARENESS , REACH , LINK_CLICKS , POST_ENGAGEMENT , APP_INSTALLS , VIDEO_VIEWS , LEAD_GENERATION , MESSAGES , CONVERSIONS , PRODUCT_CATALOG_SALES e STORE_TRAFFIC . |


O orçamento de gasto mínimo no Instagram é o mesmo dos anúncios de autoatendimento do Facebook, com diferentes [limites por moeda](https://developers.facebook.com/docs/marketing-api/adset/budget-limits) e [limites com base no `bid_amount`](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign#Creating).


[Saiba mais sobre posicionamentos padrão para seus anúncios](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting) e [`instagram_positions`.](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting#newplacement)


Para campanhas de alcance e frequência, leia [Alcance e frequência do Instagram](https://developers.facebook.com/docs/marketing-api/reachandfrequency#instagram-reach---frequency).
[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)

## Etapa 3: criar um conjunto de anúncios


[Crie um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-set) com as preferências a seguir:


- [Meta de otimização](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt): suas opções de meta dependem do objetivo definido no nível da campanha. Leia nossas [regras de validação](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group#objective-validation).
- [Opções de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference): você pode usar todas as [opções de direcionamento do Facebook](https://developers.facebook.com/docs/marketing-api/audiences/reference) para campanhas do Instagram, incluindo [opções de direcionamento básico](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting) nativas do Facebook, [Públicos Personalizados](https://developers.facebook.com/docs/marketing-api/custom-audience-targeting/) e [Públicos Semelhantes](https://developers.facebook.com/docs/marketing-api/lookalike-audience-targeting/).
- [Orçamento](https://developers.facebook.com/docs/marketing-api/bidding/overview/budgets)
- [Evento de cobrança](https://developers.facebook.com/docs/marketing-api/bidding/overview/billing-events): o `billing_event` depende da `optimization_goal` escolhida. Leia nossas [regras de validação](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt-goal-validation).
- [Programação](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling)


Para campanhas de `APP_INSTALLS` e `CONVERSIONS`, um `promoted_object` também é necessário no nível do conjunto de anúncios.


Se você criar um conjunto de anúncios de [alcance e frequência](https://developers.facebook.com/docs/marketing-api/reachandfrequency), defina um `rf_prediction_id`. Os `destination_ids` da Previsão de alcance e frequência precisam conter a identificação da conta do Instagram.


### Posicionamento


Para veicular anúncios no Instagram, inclua `instagram` em [`publisher_platforms`](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting#newplacement) no conjunto de anúncios. Use os posicionamentos `stream`, `story`, `explore`, `reels`, `explore_home` e `ig_search` do Instagram ou habilite várias plataformas, incluindo as opções do Instagram. Se você escolher diversas plataformas, o Facebook otimizará a veiculação com base no público-alvo em cada uma delas com a [otimização de posicionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting).


- Para mostrar anúncios exclusivamente no stream ou nos Stories, especifique `stream` ou `story` no campo `instagram_positions`.
- Anúncios com `"instagram_positions":["story"]` serão exibidos no feed do Instagram para desktop e para dispositivos móveis.
- Se você quiser exibir os anúncios na aba **Explorar** do Instagram, selecione `stream` e `explore` como posicionamentos.
- Se você quiser exibir os anúncios na **página inicial do Explorar** do Instagram, selecione `stream` e `explore` como posicionamentos.
- Se você quiser exibir os anúncios no **resultado da pesquisa** do Instagram, selecione `stream` como posicionamento.
- Os anúncios nos feeds do Instagram na web usam o posicionamento `stream`, e a elegibilidade deles é verificada para exibição em feeds da web para desktop e dispositivos móveis. Os objetivos compatíveis são `BRAND_AWARENESS`, `REACH`, `LINK_CLICKS`, `POST_ENGAGEMENT`, `VIDEO_VIEWS` e `CONVERSIONS`.


Se as `instagram_positions` não forem especificadas, veicularemos os anúncios nos quatro posicionamentos disponíveis no Instagram.


Para veicular anúncios apenas no Instagram Stories, use `story` somente em `instagram_positions`. Nesse caso, você também deve ter `instagram` como o único valor para `publisher_platforms`.


### Exemplos


Crie um conjunto de anúncios tendo o Instagram como posicionamento:

```
curl \
  -F 'name=Instagram Adset' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["instagram"],
    "user_os": ["iOS"]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Crie um conjunto de anúncios com a página inicial do Explorar do Instagram como posicionamento:

```
curl \
  -F 'name=Instagram Adset' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["instagram"],
    "instagram_positions": ["stream", "explore", "explore_home"],
    "user_os": ["iOS"]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Crie um conjunto de anúncios com o resultado da pesquisa do Instagram como posicionamento:

```
curl \
  -F 'name=Instagram Adset' \
  -F 'optimization_goal=LINK_CLICKS' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "publisher_platforms": ["instagram"],
    "instagram_positions": ["stream", "ig_search"],
    "user_os": ["iOS"]
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)

## Etapa 4: fornecer um criativo do anúncio


Nesse momento, você deve [fornecer o criativo do anúncio](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative). Para os criativos que serão usados apenas no Instagram ou em posicionamentos mistos, você precisa fornecer a [identificação da conta do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#account-id) e a identificação da Página do Facebook. As informações da sua Página não aparecerão em nenhum lugar do seu anúncio do Instagram. Se a conta do Instagram estiver conectada ou for associada a uma Página, a mesma Página deverá ser usada.


Quando você fornece um anúncio, criamos uma publicação sem exibição. Você pode ver a publicação sem exibição na Página ao consultar o [feed promovível](https://developers.facebook.com/docs/graph-api/reference/page/feed) usando a identificação da Página.


### Guias relevantes


- [Usar publicações como anúncios do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads)
- [Adicionar uma chamada para ação opcional](https://developers.facebook.com/docs/instagram/ads-api/guides/call-to-action)
- [Obter uma prévia do anúncio](https://developers.facebook.com/docs/instagram/ads-api/guides/get-ad-preview)
- [Instagram Advantage+ Catalog Ads](https://developers.facebook.com/docs/instagram/ads-api/guides/dynamic-ads)
- [Anúncios em carrossel](https://developers.facebook.com/docs/instagram/ads-api/guides/carousel-ads): você pode criar anúncios em carrossel com o [Gerenciador de Anúncios](https://business.facebook.com/adsmanager/manage) e com a API.
- [Personalizar os Stories](https://developers.facebook.com/docs/instagram/ads-api/guides/customize-stories)
- [Adicionar elementos interativos](https://developers.facebook.com/docs/instagram/ads-api/guides/add-interactive-elements)
[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)

## Etapa 5: programar a veiculação


[Crie o objeto de anúncio para vincular seu criativo ao conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad).


### Processo de análise de anúncio


As políticas da análise de anúncio são as mesmas para o Facebook e o Instagram. Temos disponibilizado o Instagram para um número cada vez maior de empresas e queremos criar a mesma experiência de anúncio de alta qualidade que oferecemos no Facebook.


Para isso, precisamos entender melhor como a comunidade interage com os diferentes tipos de conteúdo do anunciante no Instagram. Como leva tempo para construir o mesmo tipo de modelo que aciona os anúncios do Facebook, atualmente contamos com um processo de análise humana para filtrar uma pequena porcentagem dos anúncios e fornecer sugestões de melhorias.


Nosso objetivo final é tornar a veiculação de campanhas no Facebook e no Instagram uma experiência integrada e fazer com que os anúncios sejam uma parte relevante e valiosa do produto Instagram.
[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)[○](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#)Nesta Página[Introdução](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#introdu--o)[Etapa 1: obter a identificação da conta do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#account-id)[Etapa 2: criar uma campanha](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#campaign)[Etapa 3: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#adset)[Posicionamento](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#targeting)[Exemplos](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#exemplos)[Etapa 4: fornecer um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#creative)[Guias relevantes](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#guias-relevantes)[Etapa 5: programar a veiculação](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#ad)[Processo de análise de anúncio](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#review) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4b5q0t46ZFfyPqEvGSIGbEZYxqjasgmGGnotY4QM-snzGPRXfzGbX5_NkLJg_aem_oeedBkhfyXTcQclw1dZ8iA&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wEEHoRQgadfieJOaDCWosV2IU78Sa8gfeG2zARZWI2W9eEZBm0IsezVIV6g_aem_AUAkKV8TAE6Tgt-oIvabOg&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZE4nAPpn_Mz_78ODGxRF-Evke7emheBCAJE3-8G0Dr6UojtZqFLdj-Zgn-Q_aem_HoxdL6lTDTS2zoUoX9jwEQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ToPtc3GLGhmRVRTmS-alqx96mJCarzgOBuerM4SasDWA2J_BytUaBWwIMsg_aem_inx8gGSKKIP0RKbG9GKTUQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZE4nAPpn_Mz_78ODGxRF-Evke7emheBCAJE3-8G0Dr6UojtZqFLdj-Zgn-Q_aem_HoxdL6lTDTS2zoUoX9jwEQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xGffE7uLqHdeZdiW7y1lGnlB-5w5d-MuKsMV3azzRecvv8DnvrcOzwuAINw_aem_bV-chDXUKy-Fv8llv3avqA&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7QZfaS-yvnYatOJDoEJcucYdRGs4G4k6cgVfOqHzAiiSNJfjhzO_NLXmvOTg_aem_5MJHc0QSu2eagw2o_bOHPQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wEEHoRQgadfieJOaDCWosV2IU78Sa8gfeG2zARZWI2W9eEZBm0IsezVIV6g_aem_AUAkKV8TAE6Tgt-oIvabOg&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6seqyYGE9aK_cMzzQKlNEB14X1F2ub5t-PR68RasM35Nq6iLIpuvnrIcE4jA_aem_Vm9gudc2wsJzJUeHyAE9hg&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ToPtc3GLGhmRVRTmS-alqx96mJCarzgOBuerM4SasDWA2J_BytUaBWwIMsg_aem_inx8gGSKKIP0RKbG9GKTUQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6z-m7-XDIMr2FS7i6StF84T9nSsf-0xuVsCZsU7LI40zAigVDb8l6leDdR_g_aem_Qt0vyshor8T0008X95whgQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4b5q0t46ZFfyPqEvGSIGbEZYxqjasgmGGnotY4QM-snzGPRXfzGbX5_NkLJg_aem_oeedBkhfyXTcQclw1dZ8iA&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Cf6LD_E4P98hbErh0CpN49YqrimMDr5jYIRudvznDXfI0Qruk6rwl-_fFIg_aem_0F7iFXoChXHOYQQEQ9w2cQ&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wEEHoRQgadfieJOaDCWosV2IU78Sa8gfeG2zARZWI2W9eEZBm0IsezVIV6g_aem_AUAkKV8TAE6Tgt-oIvabOg&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4b5q0t46ZFfyPqEvGSIGbEZYxqjasgmGGnotY4QM-snzGPRXfzGbX5_NkLJg_aem_oeedBkhfyXTcQclw1dZ8iA&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L25BGUIhQtBpXP7NiCOXaMGjL1NeEK197mRHUAkCqhEPLv9SWaUEY_80wtKcY4tcIa5NE_M4yzElGpT4doiZXzrH8G7oLs3PvNauHXgRlyv_Gz1K7bTgc0ffl7hV54GgA4JhjagNM7ViFl1vz6-gl1bY)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão