<!-- Fonte: Teste A_B - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/split-testing -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Teste A/B


Teste diferentes estratégias publicitárias com públicos mutuamente exclusivos para identificar a que apresenta melhor desempenho. A API automatiza a divisão de públicos, garante que não haja sobreposição entre os grupos e ajuda a testar diferentes variáveis. Teste o impacto dos diversos tipos de público, técnicas de otimização de veiculação, posicionamentos de anúncios, criativos de anúncios, orçamentos e muito mais. Você ou seu parceiro de marketing podem criar, iniciar e analisar os resultados dos testes em um único local. Consulte a [referência Estudo de anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-study/).


## Diretrizes


- **Defina KPIs** com seu parceiro de marketing ou equipe interna antes de criar o teste.
- **Nível de confiança**: determine o nível antes de criar um teste. Os testes com alcance mais abrangente, programações mais longas ou orçamentos mais elevados tendem a produzir resultados estatisticamente mais significativos.
- **Selecione apenas uma variável por teste.** Dessa maneira, é possível determinar a causa mais provável da diferença de desempenho.
- **Tamanhos de teste comparáveis**: ao testar métricas de volume, como o número de conversões, é necessário fazer escala dos resultados e dos tamanhos de público para que ambos os tamanhos de teste sejam comparáveis.


## Restrições de testes


- Máximo de estudos simultâneos por anunciante: 100
- Máximo de células por estudo: 150
- Máximo de entidades de anúncio por célula: 100


### Teste de variável


*Recomendamos testar somente uma variável por vez, embora seja possível testar diversos tipos de variável.* Isso preserva a integridade científica do teste e ajuda a identificar a diferença específica que gera um melhor desempenho.


Por exemplo, considere um teste com os conjuntos de anúncios A e B. Se A usar conversões como método de otimização da veiculação *e* posicionamentos automáticos, e B aplicar cliques no link para a otimização da veiculação *e* posicionamentos personalizados, não será possível determinar se os métodos de otimização ou os posicionamentos diferentes provocaram um desempenho melhor.


Nesse exemplo, se os dois conjuntos de anúncios usarem conversões para otimização de veiculação, mas tiverem posicionamentos diferentes, você saberá que a estratégia de posicionamento foi responsável pelas diferenças de desempenho.


Para configurar o teste no nível do conjunto de anúncios:

```
curl \
-F 'name="new study"' \
-F 'description="test audience"' \
-F 'start_time=1478387569' \
-F 'end_time=1479597169' \
-F 'type=SPLIT_TEST' \
-F 'cells=[{name:"Group A",treatment_percentage:50,adsets:[<AD_SET_ID>]},{name:"Group B",treatment_percentage:50,adsets:[<AD_SET_ID>]}]' \
-F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/<API_VERSION>/<BUSINESS_ID>/ad_studies
```


### Como testar estratégias


É possível testar duas ou mais estratégias, uma em relação à outra. Por exemplo, os anúncios com o objetivo de conversões têm um impacto maior sobre seu marketing de resposta direta do que o objetivo de visitas ao site? Para configurar o teste no nível da campanha:

```
curl \
-F 'name="new study"' \
-F 'description="campaign comparison"' \
-F 'start_time=1478387569' \
-F 'end_time=1479597169' \
-F 'type=SPLIT_TEST' \
-F 'cells=[{name:"Group A",treatment_percentage:50,campaigns:[<CAMPAIGN_ID>]},{name:"Group B",treatment_percentage:50,campaigns:[<CAMPAIGN_ID>]}]' \
-F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/<API_VERSION>/<BUSINESS_ID>/ad_studies
```


### Teste de criativo


Os testes de criativo ajudam você a explorar e avaliar diferentes criativos por meio da execução de um teste A/B controlado em duas a cinco células de tratamento. Use o ponto de extremidade dos estudos de anúncios de empresas para publicar um teste de criativo de várias células e atribuir um anúncio (variante de criativo) por célula.


Para aceitar um teste de criativo, inclua o campo `creative_test_config` na sua solicitação. Use para definir o orçamento do teste configurando `daily_budget` ou `lifetime_budget_percentage`.


#### Campos


Inclua estes campos em uma solicitação POST de teste de criativo.


##### Campos obrigatórios


- `name`: nome do estudo (string).
- `type`: deve ser `SPLIT_TEST_V2`.
- `creative_test_config`: obrigatório para ativar o teste do criativo e definir o orçamento. - Forneça `daily_budget` ou `lifetime_budget_percentage`.
- `cells`: matriz de duas a cinco células: - `name`: nome da célula (string). - `treatment_percentage`: porcentagem em número inteiro para a célula. Todas as células devem somar no máximo 100. - `ads`: matriz contendo exatamente uma identificação do anúncio (string) para essa célula (uma variante de criativo por célula).
- `start_time`: hora de início do estudo (registro de data e hora Unix, segundos).
- `end_time`: hora de término do estudo (registro de data e hora Unix, segundos).
- `cooldown_start_time`: precisa corresponder a `start_time` (registro de data e hora Unix, segundos).
- `observation_end_time`: precisa corresponder a `end_time` (registro de data e hora Unix, segundos).


##### Campos opcionais


- `description`: descrição do estudo (string).


#### Exemplo de solicitação


```
curl \
-F 'name="Spring Promo Creative test"' \
-F 'description="Measures performance between two creative concepts for the Spring Promo campaign: a static image ad vs a short video ad"' \
-F 'type=SPLIT_TEST_V2' \
-F 'cells=[{name:"group a",treatment_percentage:50, ads:["<AD_ID>"]},{name:"group b",treatment_percentage:50,ads:["<AD_ID>"]}]' \
-F 'creative_test_config={"daily_budget":15000}' \
-F 'start_time=1773957600' \
-F 'cooldown_start_time=1773957600' \
-F 'end_time=1774562400' \
-F 'observation_end_time=1774562400' \
-F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v<API_VERSION>/<BUSINESS_ID>/ad_studies
```


### Avaliar os testes


Para determinar o teste de melhor desempenho, escolha uma estratégia ou variável que alcance a **métrica de eficiência** mais alta com base no seu objetivo da campanha. Por exemplo, para testar o objetivo de conversões, o conjunto de anúncios que alcançar o **menor custo por ação (CPA) terá o melhor desempenho**.


Evite avaliar testes com tamanhos de grupos assimétricos ou tamanhos de público significativamente diferentes. Nesse caso, aumente o tamanho e os resultados de uma das partes, para que ela seja comparável em relação aos outros testes. Caso seu orçamento não seja proporcional ao tamanho do grupo de teste, considere o volume de resultados, além da eficiência.


Você deve também usar um modelo de atribuição que faça sentido para o negócio e estar em conformidade com ele, antes de iniciar um teste A/B. Se for necessário reavaliar seu modelo de atribuição atual, contate seu representante do Facebook e solicite a realização de um estudo de incrementalidade. Isso poderá mostrar o verdadeiro impacto causal dos seus esforços de marketing da marca e de conversão.


### Orçamento


Você pode usar orçamentos personalizados com os testes A/B e optar por testar vários orçamentos, uns em relação aos outros. No entanto, o orçamento afeta diretamente o alcance nos grupos de teste. Se os grupos de teste apresentarem grandes diferenças de alcance ou tamanho de público, aumente o orçamento para melhorar os resultados e tornar o teste comparável.
[○](https://developers.facebook.com/docs/marketing-api/guides/split-testing#)Nesta Página[Teste A/B](https://developers.facebook.com/docs/marketing-api/guides/split-testing#teste-a-b) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65EkcxeRjXjj-hep0UG3MabmABmF0SiF15xdBMGqpHPDe-ztYVzCcIAU4Prw_aem_V0toe5AXviaqX38astcQhA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6K6F17X6GWsJhZUvv54xMbp01vDfcLyzu9yzD9JctTZ4g4N2gqzeelxStD8g_aem_pA3bDcQlDAtznge_OPw5WQ&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68FH8vd7-7lBnaN_Amzc4VRNSPNHQ6trfXNQfHQD_-2fgm_l59rMh49kMB2w_aem_hoJ5Z-g5xELOD3ijBa7RSA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5T0biA4izUgb3FHTH9Tcl9sycEoGTqk5TtfjbZuxD38_a7fVvWYvXL9dPbhA_aem_67mB3PD18n6OUeIfVe4-Bw&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ofx5dyD-_n52W22V1mDxG66GqQf6IBmQZKGxyTJtXd5CU1S3Ub4PW9LAN4g_aem_brnhM49BUXwXrmM5Kbawmw&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69F_2tbqjxf4e9AiS-kjq5BGjfUL126pnDXMw7L1UA-C0aE8TEaF7ACNQ8hQ_aem_fAj8FvR0EWGnUKrURmFznw&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7JHG4_kBy-V_wsh3GcCv6N9Ugxv4kbqq8E6fd6zvyXTPKdS17EQH9iOhClOA_aem_kTZnJFLT0Q_atmeQdcMPtg&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65EkcxeRjXjj-hep0UG3MabmABmF0SiF15xdBMGqpHPDe-ztYVzCcIAU4Prw_aem_V0toe5AXviaqX38astcQhA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4lDtMZ6fwoRsrzK7jVoUGomyZtp8rl-4KodGYWPoM1XKh72ZfFq94lGaEkZQ_aem_sYtRdvhDLf5YwOBegTaZcA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5T0biA4izUgb3FHTH9Tcl9sycEoGTqk5TtfjbZuxD38_a7fVvWYvXL9dPbhA_aem_67mB3PD18n6OUeIfVe4-Bw&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6K6F17X6GWsJhZUvv54xMbp01vDfcLyzu9yzD9JctTZ4g4N2gqzeelxStD8g_aem_pA3bDcQlDAtznge_OPw5WQ&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68FH8vd7-7lBnaN_Amzc4VRNSPNHQ6trfXNQfHQD_-2fgm_l59rMh49kMB2w_aem_hoJ5Z-g5xELOD3ijBa7RSA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6EHeshjkThNXyAxmSp9VPElE-9kq8YL5f72544fHcajcyq0TM719dlBytE_Q_aem_u4peVnFZsl65rnMA60koWQ&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6EHeshjkThNXyAxmSp9VPElE-9kq8YL5f72544fHcajcyq0TM719dlBytE_Q_aem_u4peVnFZsl65rnMA60koWQ&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65EkcxeRjXjj-hep0UG3MabmABmF0SiF15xdBMGqpHPDe-ztYVzCcIAU4Prw_aem_V0toe5AXviaqX38astcQhA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6XSGJvysisprfjhTL-LV9kzIRPP5emFZrNnulAOCmyyKnsTG-oazsBsYPQkQ_aem_q5FTvrdGvPmNOp24-kIoUg&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69F_2tbqjxf4e9AiS-kjq5BGjfUL126pnDXMw7L1UA-C0aE8TEaF7ACNQ8hQ_aem_fAj8FvR0EWGnUKrURmFznw&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4lDtMZ6fwoRsrzK7jVoUGomyZtp8rl-4KodGYWPoM1XKh72ZfFq94lGaEkZQ_aem_sYtRdvhDLf5YwOBegTaZcA&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7JHG4_kBy-V_wsh3GcCv6N9Ugxv4kbqq8E6fd6zvyXTPKdS17EQH9iOhClOA_aem_kTZnJFLT0Q_atmeQdcMPtg&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6EHeshjkThNXyAxmSp9VPElE-9kq8YL5f72544fHcajcyq0TM719dlBytE_Q_aem_u4peVnFZsl65rnMA60koWQ&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7u2bU37GsG45ZN97BJ_NxRurTNI57CeYmWTAGulZNQsUVa39DlOzFvZ6wf1vu_a_onGTwWQmBoUQV_fjt7TAp9SsljN3H5f1XDWN2FnZNNo9BuhAkQrQ2x623R_VwDTAPNpV2VuGgz4_kJuSBlztHxicI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão