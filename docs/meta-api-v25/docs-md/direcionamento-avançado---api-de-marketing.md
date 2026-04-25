<!-- Fonte: Direcionamento avançado - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Direcionamento avançado


O direcionamento avançado abrange:


- [dispositivos móveis](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#mobile) e [posicionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting);
- [direcionamento demográfico avançado](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#demographic); - [educação e local de trabalho](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#education-and-workplace);
- [públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#custom_audiences);
- [locais](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#locales);
- [alcance de pessoas interessadas em cidades e regiões selecionadas](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#reach-people-interested-in-selected-cities-and-regions).
- [direcionamento por categoria ampla](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#broadcategories);
- [expansão do direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion);
- [direcionamento flexível](https://developers.facebook.com/docs/marketing-api/audiences/reference/flexible-targeting).


É possível usar combinações das opções avançadas de direcionamento nos seus [públicos personalizados](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/) e semelhantes. Por padrão, o Facebook usa `ORs` para fazer combinações. Saiba mais sobre [direcionamento básico ou principal](https://developers.facebook.com/docs/marketing-api/buying-api/targeting).


Caso você use `flexible_spec`, também será preciso fornecer um dos seguintes dados em `targeting`:


- `geo_locations` (campo de direcionamento geográfico por país, região, cidade, código postal)
- `custom_audiences`
- `product_audience_specs`
- `dynamic_audience_ids`


### Limitações


- Haverá conjuntos distintos de restrições para os anunciantes que veicularem anúncios de moradia, emprego e crédito que estiverem baseados nos Estados Unidos ou que veicularem anúncios direcionados a esse país. Consulte [**Categoria de anúncio especial**](https://developers.facebook.com/docs/marketing-api/special-ad-category/).
- Consulte nosso [guia sobre restrições de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-restrictions) para ver mais limitações.


## Dispositivos móveis


Esta seção é útil para [anúncios de instalação de app para celular](https://developers.facebook.com/docs/reference/ads-api/mobile-app-ads).

```
curl -X POST \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "user_device": ["Galaxy S6","One m9"],
    "user_os": ["android"]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Você pode combinar categorias, como iPod OU iPad OU iPhone.


**Uma categoria não exclui a outra**. Ao selecionar iOS, você direcionará para todos os dispositivos que usam esse sistema operacional, incluindo iPhone e iPod, mesmo se não especificar `user_device`.


**Para anúncios com o objetivo de reconhecimento da marca**, não será possível direcionar com base no tipo de dispositivo móvel, como celulares comuns ou aparelhos Samsung, nem com base no número de versão do iOS. Só é possível escolher Android, iOS ou todos os celulares.


### Campos disponíveis


| Campo | Descrição |
| --- | --- |
| user_os tipo: matriz | Obrigatório. Um ou mais valores da tabela de opções de sistema operacional abaixo. Os valores possíveis estão na API de Pesquisa de Direcionamento com type=adTargetingCategory e class=user_os . Você não pode direcionar anúncios para a versão mínima de uma plataforma na outra plataforma. Contudo, você pode direcionar anúncios às duas plataformas sem especificar as versões mínimas delas. Valores válidos: - ['iOS', 'Android'] - ['iOS'] - ['Android_ver_4.2_and_above'] - ['iOS_ver_8.0_to_9.0'] Valores inválidos: - ['Android', 'iOS_ver_8.0_and_above'] - ['iOS', 'Android_ver_4.0_and_above'] |
| user_device tipo: matriz | Opcional. Os dispositivos devem corresponder ao valor em user_os . Veja os valores possíveis na API de Pesquisa de Direcionamento com type=adTargetingCategory e class=user_device . |
| excluded_user_device tipo: matriz | Opcional. Dispositivos que serão excluídos. Os dispositivos devem corresponder ao valor em user_os . Veja os valores possíveis na API de Pesquisa de Direcionamento com type=adTargetingCategory e class=user_device . |
| wireless_carrier tipo: matriz | Opcional. O valor permitido é Wifi . Direcionado aos usuários de dispositivos móveis que estão conectados a redes Wi-Fi. |


### Opções de sistema operacional


| Campo | Descrição |
| --- | --- |
| iOS tipo: cadeia de caracteres | Dispositivos com iOS, entre eles iPhone, iPad e iPod. |
| iOS_ver_x.x_and_above tipo: cadeia de caracteres | Dispositivos com iOS que executam a versão x.x e superior do sistema operacional. Opções : 2.0, 3.0, 4.0, 4.3, 5.0, 6.0, 7.0, 8.0 e 9.0. Exemplo : iOS_ver_4.0_and_above Para anúncios de apps da Meta: Os conjuntos de anúncios da SKAdNetwork e de Mensuração de Eventos Agregados da Meta são compatíveis somente com versões no intervalo iOS_ver_14.0_and_above .; Os conjuntos de anúncios da SKAdNetwork ou de Mensuração de Eventos Agregados da Meta são compatíveis somente com versões no intervalo iOS_ver_2.0_to_14.4 . |
| iOS_ver_x.x_to y.y tipo: cadeia de caracteres | Dispositivos com iOS que executam as versões x.x a y.y do sistema operacional. Opções : 2.0, 3.0, 4.0, 4.3, 5.0, 6.0, 7.0, 8.0 e 9.0. Exemplo : iOS_ver_8.0_to_9.0 , em que x.x deve ser menor que y.y. |
| Android tipo: cadeia de caracteres | Dispositivos com Android |
| Android_ver_x.x_and_above tipo: cadeia de caracteres | Dispositivos com Android que executam a versão x.x e superior. Opções : 2.0, 2.1, 2.2, 2.3, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2, 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1 e 8.0. Exemplo : Android_ver_4.0_and_above |
| Android_ver_x.x_to y.y tipo: cadeia de caracteres | Dispositivos com Android que executam as versões x.x a y.y. Opções : 2.0, 2.1, 2.2, 2.3, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2, 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1 e 8.0. Exemplo : Android_ver_4.2_to_8.0 , em que x.x. deve ser menor que y.y. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Direcionamento demográfico avançado


Direcionamento com base em relacionamentos, educação, finanças e acontecimentos.


### Exemplos


Primeiro, consulte `life_events`:

```
curl -G \
  -d 'type=adTargetingCategory' \
  -d 'class=life_events' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/search
```


Adicione os resultados a `targeting_spec`:

```
curl -X POST \
  -F 'name="My First AdSet"' \
  -F 'daily_budget=10000' \
  -F 'bid_amount=300' \
  -F 'billing_event="IMPRESSIONS"' \
  -F 'optimization_goal="REACH"' \
  -F 'campaign_id="<AD_CAMPAIGN_ID>"' \
  -F 'promoted_object={
       "page_id": "<PAGE_ID>"
     }' \
  -F 'targeting={
       "facebook_positions": [
         "feed"
       ],
       "age_max": 24,
       "age_min": 20,
       "behaviors": [
         {
           "id": 6002714895372,
           "name": "All travelers"
         }
       ],
       "device_platforms": [
         "mobile"
       ],
       "genders": [
         1
       ],
       "geo_locations": {
         "countries": [
           "US"
         ],
         "regions": [
           {
             "key": "4081"
           }
         ],
         "cities": [
           {
             "key": 777934,
             "radius": 10,
             "distance_unit": "mile"
           }
         ]
       },
       "interests": [
         {
           "id": "<INTEREST_ID>",
           "name": "<INTEREST_NAME>"
         }
       ],
       "life_events": [
         {
           "id": 6002714398172,
           "name": "Newlywed (1 year)"
         }
       ],
       "publisher_platforms": [
         "facebook",
         "audience_network"
       ]
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Agora direcionamos:


- Localização – Japão, Estados Unidos (raio de 10 milhas de Menlo Park, Califórnia) ou Estados Unidos (Texas)
- Idade – de 20 a 24 anos
- Gênero – masculino
- Interesses – futebol
- Comportamentos – apenas viajantes frequentes
- Acontecimento – recém-casados (um ano)
- Propriedade da residência – locatários


Este é outro exemplo de direcionamento por localização, dados demográficos, status de relacionamento e interesses:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "age_max": 43,
    "age_min": 18,
    "genders": [1],
    "geo_locations": {
      "regions": [{"key":"3847"}],
      "cities": [
        {
          "key": "2430536",
          "radius": 12,
          "distance_unit": "mile"
        }
      ]
    },
    "interests": [{"id":6003139266461,"name":"Movies"}],
    "relationship_statuses": [
      2,
      3,
      4
    ]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


### Opções possíveis


| Nome | Descrição |
| --- | --- |
| relationship_statuses tipo: matriz | Matriz de números inteiros que representam o status de relacionamento. 1 – solteiro(a) 2 – em um relacionamento 3 – casado(a) 4 – noivo(a) 6 – não especificado Padrão : ALL se você especificar "Null" (Nulo) ou não informar um valor. Restrições : não use 0 . |
| life_events tipo: matriz | Matriz de objetos com o campo "id" e o campo opcional "name": [{'id': 123, 'name': 'foo'}, {'id': 456}, 789] |
| industries tipo: matriz | Matriz de objetos com o campo "id" e o campo opcional "name". |
| income tipo: matriz | Matriz de objetos com o campo "id" e o campo opcional "name". |
| family_statuses tipo: matriz | Matriz de objetos com o campo "id" e o campo opcional "name". |


### Trabalho e educação


Use a [API de Pesquisa de Direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search#demo) para todas as opções.


| Nome | Descrição |
| --- | --- |
| education_schools tipo: matriz | Escolas, faculdades e instituições. Limite : 200 instituições de ensino. Exemplo : [{id: 105930651606, 'name': 'Harvard University'}, {id: 105930651607}, 105930651608] |
| education_statuses tipo: matriz | Matriz de números inteiros para o direcionamento com base no nível de escolaridade. 1 – HIGH_SCHOOL (Ensino Médio) 2 – UNDERGRAD (graduação incompleta) 3 – ALUM (ex-estudante) 4 – HIGH_SCHOOL_GRAD (Ensino Médio completo) 5 – SOME_COLLEGE (faculdade não especificada) 6 – ASSOCIATE_DEGREE (diploma de associado) 7 – IN_GRAD_SCHOOL (pós-graduação incompleta) 8 – SOME_GRAD_SCHOOL (pós-graduação não especificada) 9 – MASTER_DEGREE (mestrado completo) 10 – PROFESSIONAL_DEGREE (diploma profissional) 11 – DOCTORATE_DEGREE (doutorado completo) 12 UNSPECIFIED (não especificado) 13 – SOME_HIGH_SCHOOL (instituição de Ensino Médio não especificada) |
| college_years tipo: matriz | Matriz de números inteiros. Formatura na faculdade. Limite : o primeiro ano permitido é 1980. |
| education_majors tipo: matriz | Graduações. Exemplo : [{'id': 123, 'name': 'Computer Science'}, {'id': 456}, 789] Limite : 200 |
| work_employers tipo: matriz | Empresa, organização ou local de trabalho. Exemplo : [{'id':'50431654','name':'Microsoft'}, {'id':50431655}, 50431656] Limite : 200 |
| work_positions tipo: matriz | Cargo informado pelo usuário. Exemplo : [{'id':105763692790962, 'name':'Contractor'}, {'id':105763692790963}, 105763692790964] Limite : 200 |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Públicos personalizados


Crie um [público personalizado](https://developers.facebook.com/docs/marketing-api/reference/custom-audience) e adicione usuários. Você pode usar o público para fazer o direcionamento, seja para inclusão ou exclusão. Inclua até 500 públicos personalizados em `custom_audiences` e 500 em `excluded_custom_audiences`.


O campo `excluded_custom_audiences` em targeting_specs não é o mesmo que `excluded_custom_audiences` no público personalizado `APP_COMBINATION`.


| Campo | Descrição |
| --- | --- |
| custom_audiences tipo: matriz | Matriz de identificações ou objetos de público. Somente no campo 'id' : [123, 456] ou [{'id': 123}, {'id': 456}] |
| excluded_custom_audiences tipo: matriz | Matriz de identificações ou objetos de público. Somente no campo 'id' : [123, 456] ou [{'id': 123}, {'id': 456}] |


```
targeting:{
     "geo_locations":{
       "countries":["US"],
     },
     "age_min":25,
     "age_max":40,
     "custom_audiences":[{"id":6004192254512}]}
     "excluded_custom_audiences":
       [{"id":6004192252847}],
 }
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Localidades


Insira um direcionamento detalhado na localidade:


| Campo | Descrição |
| --- | --- |
| locales tipo: matriz | Consulte a seção Localidades em Pesquisa de direcionamento . Índices na submatriz "locales". Direcione o anúncio a contas da Central de Contas com idioma diferente do idioma comum para a localização. Forneça um ID para o idioma, como 5 para "alemão". Limite: 50. Confira o mapeamento de "localidades" virtuais para conjuntos de idiomas na seção sobre localidades em Pesquisa de direcionamento com type=adlocale . |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Como alcançar pessoas interessadas em cidades e regiões selecionadas


Esse recurso expande o direcionamento por localização, permitindo que anunciantes alcancem pessoas que demonstraram interesse ou intenção de viajar e fazer compras nas cidades e regiões que você selecionou, dentro do mesmo país.


- Para aceitar, defina o parâmetro `geo` dentro de `individual_setting` em `targeting_automation` como `1`.
- Para recusar, defina o parâmetro `geo` dentro de `individual_setting` em `targeting_automation` como `0`.

```
"targeting": { "age_range": [25, 35], "geo_locations": { "countries": ["GB"], "cities": [{"key":"2430536", "radius":12, "distance_unit":"mile"}] }, "targeting_automation": { "individual_setting": { "geo": 1 } } }
```


#### Limitações


Esse recurso funciona quando você selecionou cidades ou regiões no seu direcionamento por localização (ou seja, o campo `geo_locations`).


#### Exemplo de solicitação


```
curl -X POST \ -F 'name="advantage audience test"' \ -F 'is_autobid="true"' \ -F 'daily_budget="100"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'campaign_id="<CAMPAIGN_ID>"' \ -F 'targeting={ "age_range": [25,35], "geo_locations": { "cities": [{"key":"2430536","radius":12,"distance_unit":"mile"}] }, "targeting_automation": {"individual_setting": {"geo": 1 } }}' \ -F 'access_token="<ACCESS_TOKEN>"' \ https://facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Para mais informações sobre o recurso, veja [Como alcançar pessoas interessadas nas cidades e regiões selecionadas](https://www.facebook.com/business/help/726389026372510).
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Habilitar sugestões de idade e gênero


No momento, este recurso está disponível para anunciantes selecionados. Nos próximos meses, ele será lançado para todos os anunciantes.


Para usar idade ou gênero como sugestões, configure o parâmetro `individual_setting` no campo `targeting_automation`. Essa configuração também será retornada ao recuperar o conjunto de anúncios, se existir no adset.


#### Limitações


- Esse recurso só está disponível nos objetivos `OUTCOME_SALES` e `APP_INSTALLS`.
- Se você habilitar as sugestões de idade e gênero, os anúncios serão mostrados além dessas configurações quando isso for melhorar o desempenho dos anúncios.


### Idade como sugestão


Defina o parâmetro `age` dentro de `individual_setting` em `targeting_automation` como `1`. Depois, inclua o campo `age_range` na especificação do público.


#### Exemplo de solicitação


```
{ "geo_locations": { "countries": [ "US" ] }, "age_min": 18, "age_range": [25, 35], "targeting_automation": { "individual_setting": { "age": 1 } } }
```


### Gênero como sugestão


Defina o parâmetro `gender` dentro de `individual_setting` em `targeting_automation` como `1`.


#### Exemplo de solicitação


```
{ "geo_locations": { "countries": [ "US" ] }, "age_min": 21, "genders":[1], "targeting_automation": { "individual_setting": { "gender": 1 } } }
```


### Criar conjunto de anúncios com sugestões


#### Exemplo de solicitação


```
curl -X POST \ -F 'name="advantage audience test"' \ -F 'is_autobid="true"' \ -F 'daily_budget="100"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'campaign_id="<CAMPAIGN_ID>"' \ -F 'promoted_object={"pixel_id": "<PIXEL_ID>","custom_event_type": "PURCHASE"}' \ -F 'targeting={ "age_min": 18, "age_range": [25,35], "genders":[1], "geo_locations": { "countries": ["US"] }, "targeting_automation": {"individual_setting": {"age": 1, "gender": 1 } }}' \ -F 'access_token="<ACCESS_TOKEN>"' \ https://facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Exemplo de resposta


```
{ "id": "<AD_SET_ID>", }
```


### Recuperar conjunto de anúncios com sugestões


#### Exemplo de solicitação


```
curl -X GET \ -d 'fields="targeting"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_SET_ID>/
```


#### Exemplo de resposta


```
{ "targeting": { "age_max": 65, "age_min": 19, "age_range": [ 25, 35 ], "genders": [ 1 ], "geo_locations": { "countries": [ "US" ], "location_types": [ "home", "recent" ] }, "targeting_relaxation_types": { "lookalike": 0, "custom_audience": 0 }, "targeting_automation": { "advantage_audience": 0, "individual_setting": { "age": 1, "gender": 1 } } }, "id": "<AD_SET_ID>", }
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Direcionamento por categoria ampla personalizada


Use categorias amplas para fazer um direcionamento personalizado criado ou permitido especificamente para sua conta. Para incluir as categorias "culinária" e "proprietário de pequena empresa":

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "user_adclusters": [
      {"id":6002714885172,"name":"Cooking"},
      {"id":6002714898572,"name":"Small Business Owners"}
    ]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Para fazer o direcionamento de acordo com uma categoria ampla, a localização e os dados demográficos:

```
curl \
  -F 'name=My AdSet' \
  -F 'optimization_goal=REACH' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'bid_amount=2' \
  -F 'daily_budget=1000' \
  -F 'campaign_id=<CAMPAIGN_ID>' \
  -F 'targeting={
    "geo_locations": {"countries":["US"]},
    "relationship_statuses": [2],
    "user_adclusters": [{"id":6002714886772,"name":"Food & Dining"}]
  }' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


A seguinte opção está disponível:


| Nome | Descrição |
| --- | --- |
| user_adclusters tipo: matriz | Matriz de pares de nomes de identificação com clusters de categorias amplas . Veja as informações abaixo sobre como recuperar categorias amplas. Limite: 50 pares de nomes e identificações. |


Para consultar esse direcionamento por conta de anúncios, faça uma solicitação `HTTP GET`:

```
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/broadtargetingcategories
```


A resposta é uma matriz de pares chave-valor JSON.


| Nome | Descrição |
| --- | --- |
| id Tipo: longo | O ID da categoria ampla é usado para a especificação de direcionamento do anúncio. |
| name tipo: cadeia de caracteres | Nome da categoria ampla. |
| parent_category tipo: cadeia de caracteres | Categoria principal da categoria ampla. |
| size_lower_bound tipo: int | Tamanho mínimo do público da categoria ampla. |
| size_upper_bound tipo: int | Tamanho máximo do público da categoria ampla. |
| type tipo: int | 6 = categoria ampla. |
| type_name tipo: cadeia de caracteres | Categoria ampla. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)

## Recursos


- [Pesquisa de direcionamento](https://developers.facebook.com/docs/reference/ads-api/get-autocomplete-data/)
- [Reach Estimate](https://developers.facebook.com/docs/marketing-api/reference/reach-estimate/)
- [Targeting Description](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-description)
- [Custom Audience](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/)
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#)Nesta Página[Direcionamento avançado](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#direcionamento-avan-ado)[Dispositivos móveis](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#dispositivos-m-veis)[Campos disponíveis](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#campos-dispon-veis)[Opções de sistema operacional](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#op--es-de-sistema-operacional)[Direcionamento demográfico avançado](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#demographic)[Exemplos](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#exemplos)[Opções possíveis](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#op--es-poss-veis)[Trabalho e educação](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#education-and-workplace)[Públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#custom_audiences)[Localidades](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#localidades)[Como alcançar pessoas interessadas em cidades e regiões selecionadas](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#como-alcan-ar-pessoas-interessadas-em-cidades-e-regi-es-selecionadas)[Habilitar sugestões de idade e gênero](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#habilitar-sugest-es-de-idade-e-g-nero)[Idade como sugestão](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#idade-como-sugest-o)[Gênero como sugestão](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#g-nero-como-sugest-o)[Criar conjunto de anúncios com sugestões](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#criar-conjunto-de-an-ncios-com-sugest-es)[Recuperar conjunto de anúncios com sugestões](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#recuperar-conjunto-de-an-ncios-com-sugest-es)[Direcionamento por categoria ampla personalizada](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#broadcategories)[Recursos](https://developers.facebook.com/docs/marketing-api/audiences/reference/advanced-targeting#recursos) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7PEfyMfzQ05HqDTmS6G3bfMXKIyG_Ptrefxg6riwoMDldE_7vzebiQwvUkoQ_aem_1DSPrmkBM55VelITQir41g&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rsIwPJYk4wd874k_yFtd302KO4m-TCCZJGlV769ZQ-bcfXXPab5sKo0JNrw_aem_r7jrGMjnM0VUtf6rasWH0w&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rsIwPJYk4wd874k_yFtd302KO4m-TCCZJGlV769ZQ-bcfXXPab5sKo0JNrw_aem_r7jrGMjnM0VUtf6rasWH0w&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-Rl-MYUicohM-q7_Lmj6kEEtfwMMVXyrndQY2LDN2d0ZHDVGawEb-WCqd0g_aem_suHA_olncRWVbF9vUmhPew&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-Rl-MYUicohM-q7_Lmj6kEEtfwMMVXyrndQY2LDN2d0ZHDVGawEb-WCqd0g_aem_suHA_olncRWVbF9vUmhPew&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7S6y85ltBJdkq09bMV31dqOWQwWYHNnScP_1tAsQqf18s2CrySDKRavTYNLA_aem_e3zqUYyikmiylrKlZEdafw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-Rl-MYUicohM-q7_Lmj6kEEtfwMMVXyrndQY2LDN2d0ZHDVGawEb-WCqd0g_aem_suHA_olncRWVbF9vUmhPew&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Aa8YFUB2vz-hkJ9Ibsn3YZtEAbznxczV8GAC7HwmcjdBl3eFE2IgTdn0wug_aem_E6WdHnagHSNP5byidCmNow&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rsIwPJYk4wd874k_yFtd302KO4m-TCCZJGlV769ZQ-bcfXXPab5sKo0JNrw_aem_r7jrGMjnM0VUtf6rasWH0w&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR40nB86i4DZZBaK45SOfsCP92Fvh_PKdYYN2op-u1y02e3_WImQ7EHzks8NQA_aem_Y7R3ekMXhOH6k6xMI-EO2w&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7S6y85ltBJdkq09bMV31dqOWQwWYHNnScP_1tAsQqf18s2CrySDKRavTYNLA_aem_e3zqUYyikmiylrKlZEdafw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4YEEdinoF8mWS7CgiWzB0EKdtGBapASR1emyenmY1wimtWv955TsYiq2Ig-g_aem_sJofa3Umk7PqIkDuP0c5cw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Zgu9h5orJHZfsuRmpWXAfn-vigApgyPLz0eLwWHdm7ing7RhTq22CbU6YJA_aem_e9Z5kg06l61fIbGK9yJEnw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Lv4Ohl3kXUee_gJN1oIqodJU2HZBR2ebaFoHMbsr-6_P225coDIBfl6UQSA_aem_OcBz2iHIiDi1uASX_6VaEw&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4M4Em1UgKJowY_a1H-r2I1fNYLLDW_hDmo7fb_vNN4CdkYt0Sglxj8GkdxFtDjpC9LmlmF6VE50vsV7kWR7KbkbXUVZ9x7q9YWFuSxonodmI6-Ut84K15JWZkRFex4-ClrnAFmXqUUd-tfmJ58D9GI8Mo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão