<!-- Fonte: Visão geral dos lances - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/bidding/overview -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Visão geral dos lances


Um *lance* expressa o quanto você valoriza que seu anúncio alcance um público-alvo e forneça resultados na `optimization_goal`. O `bid_amount` é o valor que você deseja gastar para adquirir um determinado evento com base na `optimization_goal`, e a `bid_strategy` define como você quer controlar seus gastos em determinado evento com base na `optimization goal`.


No leilão de anúncios do Facebook, o Facebook avalia a `bid strategy`, o `bid_amount` e a probabilidade de cumprir a `optimization_goal` para calcular um **lance efetivo**. Dessa forma, você só ganhará leilões e exibirá anúncios quando for possível atingir sua `optimization_goal` com certas restrições de lances, como custo por resultado.


Como parte dos nossos esforços para simplificar a oferta de produtos, otimizamos o alcance e as impressões para ajudar os anunciantes a alcançar objetivos com mais eficácia.


Quando a otimização de alcance for selecionada na API, o valor de "Impressões" será retornado em `optimization_goal` com a configuração de controle de frequência do anunciante.


Os conceitos principais dos lances e da otimização incluem o seguinte:


- [**Estratégias de lance**](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy): como você quer que os lances sejam feitos.
- [**Metas de otimização**](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt): as metas que você quer atingir quando o Facebook veicular seus anúncios.
- [**Orçamentos**](https://developers.facebook.com/docs/marketing-api/bidding/overview/budgets)
- [**Regularidade e programação**](https://developers.facebook.com/docs/marketing-api/pacing): como seu orçamento de anúncios é gasto ao longo do tempo.
- [**Otimização do orçamento da campanha**](https://developers.facebook.com/docs/marketing-api/bidding/guides/campaign-budget-optimization): uma forma de otimizar a distribuição de um orçamento nos conjuntos de anúncios da sua campanha.
- [**Eventos de cobrança**](https://developers.facebook.com/docs/marketing-api/bidding-and-optimization/billing-events): os eventos pelos quais você deseja pagar, como impressões, cliques ou ações diversas.


## Configuração de lance


Ao escolher seu lance:


- leve em consideração o valor real: analise seu objetivo de publicidade e faça o lance do valor máximo que você se dispõe a pagar pelo objetivo em questão;
- decida se quer maximizar o lucro ou o crescimento.


Também é possível definir `objective` e `billing_event`, mas isso não afetará diretamente o `bid_amount` ou seu lance efetivo. Se um `bid_amount` for definido, seu custo real por resultado geralmente será próximo a ou menor que `bid_amount`, dependendo das [**estratégias de lance**](https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy).


Por exemplo, use essas configurações para gastar cerca de US$ 10,00 por 1.000 visualizações diárias exclusivas:


- `objective` da campanha – `APP_INSTALLS`
- `optimization_goal` do conjunto de anúncios – `REACH`
- `billing_event` do conjunto de anúncios – `IMPRESSIONS`


Por outro lado, para gastar US$ 10,00 **por instalação do app**, use as seguintes configurações:


- `objective` da campanha – `APP_INSTALLS`
- `optimization_goal` do conjunto de anúncios – `APP_INSTALLS`
- `billing_event` do conjunto de anúncios – `IMPRESSIONS`
[○](https://developers.facebook.com/docs/marketing-api/bidding/overview#)

## Metas de otimização


Defina as metas de anúncios que você deseja atingir quando o Facebook veicular seus anúncios. Usamos a `optimization_goal` do seu [conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) para decidir quais pessoas receberão o anúncio. Por exemplo, para `APP_INSTALLS`, o Facebook veicula o anúncio às pessoas com maior probabilidade de instalar o app.


`optimization_goal` é uma meta associada ao seu `objective` por padrão. Por exemplo, se `objective` for `APP_INSTALLS`, `optimization_goal` será `APP_INSTALLS` por padrão.


### Validação


Estes objetivos antigos ficaram obsoletos a partir do lançamento da [versão 17.0 da API de Marketing](https://developers.facebook.com/docs/graph-api/changelog/version17.0#marketing-api). Consulte a tabela [Objective Mapping](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group#odax-mapping) para encontrar novos objetivos e os tipos de destino correspondentes, metas de otimização e objetos promovidos.


Alguns [`objectives` da campanha](https://developers.facebook.com/docs/reference/ads-api/adcampaign) aceitam apenas determinadas `optimization_goal`s dos conjuntos de anúncios:


| Objetivo da campanha | optimization_goal padrão | Outra optimization_goal válida |
| --- | --- | --- |
| APP_INSTALLS , promover um app de experiência instantânea | APP_INSTALLS | IMPRESSIONS , POST_ENGAGEMENT |
| APP_INSTALLS , promover um app para celular | APP_INSTALLS | OFFSITE_CONVERSIONS , LINK_CLICKS , REACH e VALUE |
| BRAND_AWARENESS | AD_RECALL_LIFT | REACH |
| CONVERSIONS | OFFSITE_CONVERSIONS | IMPRESSIONS , LINK_CLICKS , POST_ENGAGEMENT , REACH , VALUE , LANDING_PAGE_VIEWS e CONVERSATIONS |
| EVENT_RESPONSES , promover um evento | EVENT_RESPONSES | IMPRESSIONS e REACH |
| EVENT_RESPONSES , promover um post da Página | EVENT_RESPONSES | IMPRESSIONS , POST_ENGAGEMENT e REACH |
| LEAD_GENERATION | LEAD_GENERATION | QUALITY_LEAD , LINK_CLICKS e QUALITY_CALL |
| LINK_CLICKS | LINK_CLICKS | IMPRESSIONS , POST_ENGAGEMENT , REACH e LANDING_PAGE_VIEWS |
| LINK_CLICKS , promover um app de experiências instantâneas | ENGAGED_USERS | APP_INSTALLS , IMPRESSIONS , POST_ENGAGEMENT e REACH |
| LINK_CLICKS , promover um app para celular | LINK_CLICKS | IMPRESSIONS , REACH e OFFSITE_CONVERSIONS |
| MESSAGES | CONVERSATIONS | IMPRESSIONS , POST_ENGAGEMENT , LEAD_GENERATION e LINK_CLICKS |
| PAGE_LIKES | PAGE_LIKES | IMPRESSIONS , POST_ENGAGEMENT e REACH |
| POST_ENGAGEMENT | POST_ENGAGEMENT | IMPRESSIONS , REACH e LINK_CLICKS |
| PRODUCT_CATALOG_SALES | OFFSITE_CONVERSIONS ou LINK_CLICKS | IMPRESSIONS , POST_ENGAGEMENT , REACH , CONVERSATIONS e VALUE |
| REACH | REACH | IMPRESSIONS |
| VIDEO_VIEWS | THRUPLAY |  |

[○](https://developers.facebook.com/docs/marketing-api/bidding/overview#)

## Perguntas frequentes

[Quais são os eventos cobertos por "POST_ENGAGEMENT"?](https://developers.facebook.com/docs/marketing-api/bidding/overview#faq_2333218700033692)

A maioria das ações em um anúncio, incluindo cliques no link, instalações do aplicativo, visualizações do vídeo durante um período determinado, marcações de foto, curtidas, comentários, compartilhamentos e muito mais.
[Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview#faq_2333218700033692)[○](https://developers.facebook.com/docs/marketing-api/bidding/overview#)[○](https://developers.facebook.com/docs/marketing-api/bidding/overview#)Nesta Página[Visão geral dos lances](https://developers.facebook.com/docs/marketing-api/bidding/overview#vis-o-geral-dos-lances)[Configuração de lance](https://developers.facebook.com/docs/marketing-api/bidding/overview#setup)[Metas de otimização](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt)[Validação](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt-goal-validation)[Perguntas frequentes](https://developers.facebook.com/docs/marketing-api/bidding/overview#faq) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ckv6n31V6t_kOmvj2g6BNd1OWKWEZSCUKBMvCvdu9dhq-SQdA0lRPWY3SLQ_aem_OpeNyJayis5wXxfZE50haA&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6O1PBq-JrQbZuplpK8ioiiapS7jQjDAhhpjhpubf3E2flbwNErPlL1q7ufeQ_aem_gXs_uuEPAmeclyg4xmtrZQ&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR44wFhrYGM45LHIHFKoX2hMNgZWmQCz7H4mfvSBjRaRPI_-SZKj2Ht5EIhxAg_aem_AJ7R43uSeQOMciVKuclAQg&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6aCD_Qz6Clc5FNzg5IcDNiwjmv1YTBETDd6BLsDgwvjq_nTh-mtEiQgAAYLQ_aem_2_bW0MuAjrN9TRe84Yg_ow&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6f3j5svkjo3D6k5-l3ANTxMSC-nCeZ1byohbWQ2sYfnFi0EI9NJgOBQPe5hQ_aem_dhm-RJaqIXI_5_YsReMZ1w&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ckv6n31V6t_kOmvj2g6BNd1OWKWEZSCUKBMvCvdu9dhq-SQdA0lRPWY3SLQ_aem_OpeNyJayis5wXxfZE50haA&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR61dj6R708jtizazTl2PriuF17p3GR3eUhsKV7awf6tqnX3PV1L_rLW6jJMUg_aem_ArcbgzAKUtJ5BpitQ3XSBw&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4cJwGfdMJjEVJxtz4jfIuDmOgXdGf3pFoDpqJEezmOhncaa0bvwaczsuN4mA_aem_qX6_wx14jBSGa7IGvB9uRw&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR613a4qB74CxCVvt4eNh7l5E6zBQD7DkmBGA7Zo3rYjGb3hh9qzY7puleOPvA_aem_UcyW1hXZmR8I7QShLffw-g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR613a4qB74CxCVvt4eNh7l5E6zBQD7DkmBGA7Zo3rYjGb3hh9qzY7puleOPvA_aem_UcyW1hXZmR8I7QShLffw-g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4cJwGfdMJjEVJxtz4jfIuDmOgXdGf3pFoDpqJEezmOhncaa0bvwaczsuN4mA_aem_qX6_wx14jBSGa7IGvB9uRw&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qbHyL5CA3Ct2aZ8gY5uL5RRlpu76rkuy5-emwutmRNIKrb0LZC-Ex7rrdgg_aem_2wGvYopfu7WxivyQ7g785g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6aCD_Qz6Clc5FNzg5IcDNiwjmv1YTBETDd6BLsDgwvjq_nTh-mtEiQgAAYLQ_aem_2_bW0MuAjrN9TRe84Yg_ow&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR613a4qB74CxCVvt4eNh7l5E6zBQD7DkmBGA7Zo3rYjGb3hh9qzY7puleOPvA_aem_UcyW1hXZmR8I7QShLffw-g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4cJwGfdMJjEVJxtz4jfIuDmOgXdGf3pFoDpqJEezmOhncaa0bvwaczsuN4mA_aem_qX6_wx14jBSGa7IGvB9uRw&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6O1PBq-JrQbZuplpK8ioiiapS7jQjDAhhpjhpubf3E2flbwNErPlL1q7ufeQ_aem_gXs_uuEPAmeclyg4xmtrZQ&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4qbHyL5CA3Ct2aZ8gY5uL5RRlpu76rkuy5-emwutmRNIKrb0LZC-Ex7rrdgg_aem_2wGvYopfu7WxivyQ7g785g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6aCD_Qz6Clc5FNzg5IcDNiwjmv1YTBETDd6BLsDgwvjq_nTh-mtEiQgAAYLQ_aem_2_bW0MuAjrN9TRe84Yg_ow&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6O1PBq-JrQbZuplpK8ioiiapS7jQjDAhhpjhpubf3E2flbwNErPlL1q7ufeQ_aem_gXs_uuEPAmeclyg4xmtrZQ&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR613a4qB74CxCVvt4eNh7l5E6zBQD7DkmBGA7Zo3rYjGb3hh9qzY7puleOPvA_aem_UcyW1hXZmR8I7QShLffw-g&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7UjpIchmLnUJsMw3YYT64zI-E-LSDyp7WMpCaiJ7STl9u-bksCvYvz5duAUg1FF2DxGVCeG-xNQSmmARTFGo7KaJGtrmPsv4_kNo7tEYAdB3vZZ4T4NsNs9u-qvO3ChbnYoB8RPP-gEG2cYHIgB1PgWow)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão