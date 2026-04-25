<!-- Fonte: Direcionamento básico - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Direcionamento básico


Confira o que inclui o direcionamento básico:


- [Dados demográficos e eventos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#demographics)
- [Localização](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#location)
- [Interesses](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#interests)
- [Comportamentos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#behaviors)


Há conjuntos distintos de restrições para os anunciantes que veiculam [anúncios de moradia, emprego, crédito, temas sociais, eleições ou política](https://developers.facebook.com/docs/marketing-api/special-ad-category/) e que estão baseados nos Estados Unidos ou que direcionam anúncios para esse país.


## Dados demográficos e eventos


Receba dados básicos de [demografia](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search#demo) e localização para definir o direcionamento usando a [pesquisa de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search). Depois, especifique as opções no parâmetro `targeting`, que contém atributos do [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset/) para definir quem deve ver o anúncio.


**Observação**: será preciso especificar pelo menos um país no direcionamento, a menos que você use um [público personalizado](https://developers.facebook.com/docs/marketing-api/reference/custom-audience).


### Direcionamento por dados demográficos


```
curl -X POST \ -F 'name=My AdSet' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "industries": [{"id":6009003307783,"name":"Accounting and finance"}], "life_events": [{"id":6003054185372,"name":"Recently Moved"}], "relationship_statuses": [2,4] }' \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Campos


| Nome | Descrição |
| --- | --- |
| genders matriz | Direcionamento baseado em gênero. O padrão é todos. 1 direciona para o gênero masculino, 2 direciona para o gênero feminino. |
| age_min int | Idade mínima. O padrão é 18 anos. Se usado, deve ser 13 ou mais. Se o app tiver configurações personalizadas de restrições de idade, essas informações serão usadas nos anúncios com objetivos APP_INSTALL. Por exemplo, se a idade mínima do app for 18 anos, e você configurar age_min como 13, o direcionamento de anúncios usará a idade mínima do app. |
| age_max int | Idade máxima. Se usado, deve ser 65 ou menos. |
| user_age_unknown booliano | Inclui pessoas de idade desconhecida no WhatsApp. Aplica-se apenas ao posicionamento do Status do WhatsApp A partir de maio de 2026, se o posicionamento do Status do WhatsApp estiver incluído e este campo não estiver definido, o padrão será verdadeiro. Definir como falso permite que as empresas excluam pessoas de idade desconhecida no WhatsApp . A qualquer momento, as empresas poderão cancelar a inclusão de pessoas de idade desconhecida no WhatsApp. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)

## Localização


Pesquise e recupere valores para fazer o direcionamento por localização usando a [pesquisa de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search). Esse direcionamento tem dois parâmetros: `geo_locations` para direcionar por localizações e, opcionalmente, `excluded_geo_locations` para excluir áreas.


Use `country_groups` com `geo_locations` para direcionar para maiores regiões geográficas, como Europa ou América do Norte.


Using `radius` can cause an error, code: 100, subcode 1815946, when targeting multiple locations. We recommend creating an ad for each location or not using `radius` in your call.


### Campos


| Nome | Descrição |
| --- | --- |
| countries matriz | Direcionamento de país. Exige uma matriz de códigos de países. Consulte Pesquisa de direcionamento, Países . Exemplo : 'countries': ['US'] |
| regions matriz | Estado, província ou região. Para ver os valores disponíveis, consulte Pesquisa de direcionamento, Regiões . Limite: 200. Exemplo : 'regions': [{'key':'3847'}] |
| cities matriz | Especifique key , radius e distance_unit . Para key , consulte Pesquisa de direcionamento, Cidades . radius é a distância em torno das cidades, de 10 a 50 milhas ou de 17 a 80 quilômetros. distance_unit é milha ou quilômetro. Limite: 250. Exemplo : 'cities': [{'key':'2430536', 'radius':12, 'distance_unit':'mile'}] |
| zips matriz | Para direcionar por código postal, consulte a API de pesquisa de direcionamento . Limite: 50.000 (antes 2.500) Se você fornecer mais de 2.500 valores, criaremos uma matriz conhecida como location_cluster , que representa um conjunto de códigos postais. Exemplo : 'zips':[{'key':'US:94304'},{'key':'US:00501'}] Para ler um location_cluster e ver as localizações direcionadas: GET /location_cluster_ID |
| places matriz | Forneça um local específico. Limite: 200. Exemplo: "places":[{"key":129672430416115,"name":"SFO", "radius":10, "distance_unit":"mile"}] |
| custom_locations matriz | Disponível para todos os objetivos. Forneça a localização exata em latitude e longitude ou endereço do centro de uma área. Especifique também o raio da sua localização de 0,63 a 50 milhas, ou de 1 a 80 quilômetros. distance_unit é milhas ou quilômetros. O padrão é milha. Limite: 200. Não é possível usar somente a caixa postal com address_string . É preciso fornecer, no mínimo, um endereço físico (rua). Exemplo: 'custom_locations':[{'address_string': '1601 Willow Road, Menlo Park, CA', 'radius': 5},{'latitude': 36, 'longitude': -121.0, 'radius': 5, 'distance_unit': 'kilometer'},] |
| custom_locations.latitude float | Latitude da localização |
| custom_locations.longitude float | Longitude da localização |
| custom_locations.name string | Nome do endereço. Você pode usar com os valores de latitude e longitude para direcionamento por localização geográfica sem fornecer address_string |
| custom_locations.radius float | O raio em torno da latitude/longitude, em milhas, exceto se especificado o contrário em distance_unit . De 0,63 a 50 milhas, ou 1 a 80 quilômetros. |
| custom_locations.distance_unit string | Opcional. kilometer ou mile . O padrão é mile . |
| custom_locations.address_string string | Endereço na latitude/longitude, como 1601 Willow Rd, Menlo Park, CA. Formato sugerido: número nome da rua, cidade, estado/província, país. Excluir códigos postais. |
| geo_markets matriz | Representa códigos geográficos que usam mercados DMA e/ou Comscore. Limite: 2.500. Exemplo: 'geo_markets':[{'key': 'DMA:501', 'name': 'New York'},{'key': COMSCORE_MARKET:2001', 'name': 'New York, NY'}, {'key': 'DMA:543', 'name': 'Springfield-Holyoke'},] |
| electoral_district matriz | Chave para distritos eleitorais. Consulte distritos em Pesquisa de direcionamento, Eleitoral . Exemplo : 'electoral_districts':[{'key':'US:AK00'},{'key':'US:CA01'},{'key':'US:NY14'}] |
| location_types matriz | A matriz ['home', 'recent'] é a única opção disponível. Se nenhuma matriz location_types for fornecida, o padrão será ['home', 'recent'] . recent : pessoas que têm a área selecionada como localização recente, conforme determinado nos dados do dispositivo móvel. Não disponível para excluir localizações.; home : pessoas que têm a "cidade atual" declarada no perfil do Facebook localizada em uma área. O Facebook valida essa declaração usando o IP e informações das localizações de perfis de amigos. |
| country_groups matriz | Regiões geográficas globais e áreas de comércio livre. Consulte Pesquisa de direcionamento, Grupos de países . Forneça a matriz com códigos de grupos de países: worldwide : mundial.; africa : África.; afta : Área de Livre Comércio ASEAN.; android_app_store : apps pagos compatíveis com países na loja de apps Android.; android_free_store : apps gratuitos compatíveis com países na Play Store (Android).; apec : Cooperação Econômica Ásia-Pacífico.; asia : Ásia.; caribbean : Caribe.; central_america : América Central.; cisfta : Área de Livre Comércio da Comunidade de Estados Independentes.; eea : Espaço Econômico Europeu.; emerging_markets : países em mercados emergentes.; europe : Europa.; gcc : Conselho de Cooperação do Golfo.; itunes_app_store : países compatíveis com a App Store (Apple).; mercosur : MERCOSUL.; nafta : Acordo de Livre Comércio da América do Norte.; north_america : América do Norte.; oceania : Oceania.; south_america : América do Sul. Exemplo : 'country_groups': ['asia','mercosur'] |


### Exemplos


#### Direcionamento por país


```
curl -X POST \ -F 'name="My Reach Ad Set"' \ -F 'optimization_goal="REACH"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id="<AD_CAMPAIGN_ID>"' \ -F 'targeting={ "geo_locations": { "countries": [ "US" ] }, "facebook_positions": [ "feed" ] }' \ -F 'status="PAUSED"' \ -F 'promoted_object={ "page_id": "<PAGE_ID>" }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v24.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Direcionamento por localização com exclusões


```
curl -X POST \ -F 'name="My Reach Ad Set"' \ -F 'optimization_goal="REACH"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id="<AD_CAMPAIGN_ID>"' \ -F 'targeting={ "excluded_geo_locations": { "regions": [ { "key": "3847" } ] }, "geo_locations": { "countries": [ "US" ] }, "facebook_positions": [ "feed" ] }' \ -F 'status="PAUSED"' \ -F 'promoted_object={ "page_id": "<PAGE_ID>" }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Direcionamento por código postal


```
curl -X POST \ -F 'name=My AdSet' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations":{ "zips":[{"key":"US:94304"},{"key":"US:00501"}]} }' \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Direcionamento por localizações personalizadas, mercados geográficos e tipos de localização


O código a seguir configura o direcionamento para:


- 5 milhas em torno de 1601 Willow Road, Menlo Park, CA
- 5 quilômetros em torno de latitude: 36, longitude –121,0
- DMAs (501 e 543) e COMSCORE_MARKETS (2001 e 2054)

```
curl -X POST \ -F 'name=My AdSet' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": { "custom_locations": [ {"address_string":"1601 Willow Road, Menlo Park, CA","radius":"5"}, { "latitude": "36", "longitude": "-121.0", "radius": "5", "distance_unit": "kilometer" } ], "geo_markets": [ {"key":"DMA:501","name":"New York"}, {"key":"DMA:543","name":"Springfield-Holyoke"}, {"key":"COMSCORE_MARKET:2001","name":"New York, NY"}, {"key":"COMSCORE_MARKET:2051","name":"New Orleans, LA"} ], "location_types": ["recent","home"] } }' \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Pesquisa e direcionamento


Para direcionar homens entre 20 e 24 anos em um raio de 10 milhas de Menlo Park (CA) ou que moram no Texas ou no Japão:


##### Etapa 1


Primeiro, receba o código de país do Japão:

```
curl -G \ -d 'location_types=["country"]' \ -d 'type=adgeolocation' \ -d 'q=japan' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/search
```


##### Etapa 2


Receba o código de região do Texas:

```
curl -G \ -d 'location_types=["region"]' \ -d 'type=adgeolocation' \ -d 'q=texas' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/search
```


##### Etapa 3


Pesquise o código de cidade de Menlo Park (CA):

```
curl -G \ -d 'location_types=["city"]' \ -d 'type=adgeolocation' \ -d 'q=menlo' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/search
```


##### Etapa 4


Forneça `genders` e idade como `age_min` e `age_max`.


##### Etapa 5


Nossas especificações de direcionamento estão prontas com códigos de país, região e cidade:

```
curl \ -F 'name=My First AdSet' \ -F 'daily_budget=10000' \ -F 'bid_amount=300' \ -F 'billing_event=IMPRESSIONS' \ -F 'optimization_goal=REACH' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'promoted_object={"page_id":"<PAGE_ID>"}' \ -F 'targeting={ "age_max": 24, "age_min": 20, "device_platforms": ["mobile"], "genders": [1], "geo_locations": { "countries": ["JP"], "regions": [{"key":"3886"}], "cities": [ { "key": "2420605", "radius": 10, "distance_unit": "mile" } ] }, "publisher_platforms": ["facebook","audience_network"] }' \ -F 'status=PAUSED' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Direcionamento por várias cidades


Defina `custom_type` como `multi_city` e `country` ou `country_group`, conforme descrito anteriormente.

```
curl \ -F 'name=My AdSet' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": { "custom_locations": [ { "custom_type": "multi_city", "min_population": 500000, "max_population": 1000000, "country": "BR" }, {"custom_type":"multi_city","country_group":"Europe"} ], "location_types": ["recent","home"] } }' \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


##### Parâmetros


| Nome | Descrição |
| --- | --- |
| min_population int | O limite mínimo de população usado na escolha das cidades para direcionamento. |
| max_population int | O limite máximo de população usado na escolha das cidades para direcionamento. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)

## Direcionamento por interesse


Direcionamento com base em interesses na linha do tempo de alguém, Páginas curtidas ou palavras-chave associadas a Páginas ou apps usados por alguém. Consulte [Pesquisa de direcionamento, Interesses](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search#interests).


Para direcionar pessoas interessadas em futebol, primeiro consulte:

```
curl -G \ -d 'type=adinterest' \ -d 'q=soccer' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/search
```


Adicione o interesse por `name` e `id` para uma especificação de direcionamento em que `path` é o caminho desse interesse nas ferramentas para anúncios.

```
curl -X POST \ -F 'name="My First AdSet"' \ -F 'daily_budget=10000' \ -F 'bid_amount=300' \ -F 'billing_event="IMPRESSIONS"' \ -F 'optimization_goal="REACH"' \ -F 'campaign_id="<CAMPAIGN_ID>"' \ -F 'promoted_object={ "page_id": "<PAGE_ID>" }' \ -F 'targeting={ "facebook_positions": [ "feed" ], "geo_locations": { "countries": [ "US" ], "regions": [ { "key": "4081" } ], "cities": [ { "key": 777934, "radius": 10, "distance_unit": "mile" } ] }, "genders": [ 1 ], "age_max": 24, "age_min": 20, "publisher_platforms": [ "facebook", "audience_network" ], "device_platforms": [ "mobile" ], "flexible_spec": [ { "interests": [ { "id": "<INTEREST_ID>", "name": "<INTEREST_NAME>" } ] } ] }' \ -F 'status="PAUSED"' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Este é outro exemplo:

```
curl \ -F 'name=My AdSet' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "interests": [ {"id":6003139266461,"name":"Movies"}, {"id":6003397425735,"name":"Tennis"}, {"id":6003659420716,"name":"Cooking"} ] }' \ -F 'status=ACTIVE' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


### Campos


| Nome | Descrição |
| --- | --- |
| interests matriz | Matriz com os campos id e name (opcional): 'interests':[{id: 6003139266461, 'name': 'Movies'}, {id: 6003139266462}, 6003139266463] |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)

## Direcionamento por comportamento


Direcionamento com base em atividades digitais, dispositivos usados pela pessoa, intenção de compra ou compras anteriores e viagem. Visualize as opções em `Browse`, como "viajantes frequentes". Consulte [Pesquisa de direcionamento, Comportamentos](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search#behaviors).

```
curl -G \ -d 'type=adTargetingCategory' \ -d 'class=behaviors' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/search
```


Adicione o comportamento à especificação `targeting`:

```
curl \ -F 'name=My First AdSet' \ -F 'daily_budget=10000' \ -F 'bid_amount=300' \ -F 'billing_event=IMPRESSIONS' \ -F 'optimization_goal=REACH' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'promoted_object={"page_id":"<PAGE_ID>"}' \ -F 'targeting={ "age_max": 24, "age_min": 20, "behaviors": [{"id":6002714895372,"name":"All frequent travelers"}], "device_platforms": ["mobile"], "genders": [1], "geo_locations": { "countries": ["JP"], "regions": [{"key":"3886"}], "cities": [ { "key": "2420605", "radius": 10, "distance_unit": "mile" } ] }, "interests": [{"id":6003107902433,"name":"Association football (Soccer)"}], "publisher_platforms": ["facebook","audience_network"] }' \ -F 'status=PAUSED' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Outro exemplo:

```
curl -X POST \ -F 'name="My AdSet"' \ -F 'optimization_goal="REACH"' \ -F 'billing_event="IMPRESSIONS"' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id="<CAMPAIGN_ID>"' \ -F 'targeting={ "facebook_positions": [ "feed" ], "geo_locations": { "countries": [ "US" ] }, "behaviors": [ { "id": 6007101597783, "name": "Business Travelers" }, { "id": 6004386044572, "name": "Android Owners (All)" } ] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


## Campos


| Nome | Descrição |
| --- | --- |
| behaviors matriz | Matriz com os campos id e name (opcional): 'behaviors':[{id: 6004386044572, 'name': 'Android Owners (All)'}, {id: 6004386044573}, 6004386044574] |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)

## Saiba mais


- [Pesquisa de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search): consulte as opções de direcionamento para anúncios nativos do Facebook.
- [Direcionamento por público](https://developers.facebook.com/docs/marketing-apis/audiences-api)
- [Categoria de anúncio especial](https://developers.facebook.com/docs/marketing-api/special-ad-category/)


Outro direcionamento:


- [Audience Network](https://developers.facebook.com/docs/reference/ads-api/audience-network): exibe anúncios no Audience Network e amplia o alcance dos seus anúncios com link ou de app.
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#)Nesta Página[Direcionamento básico](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#direcionamento-b-sico)[Dados demográficos e eventos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#demographics)[Direcionamento por dados demográficos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#direcionamento-por-dados-demogr-ficos)[Localização](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#location)[Campos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#campos)[Exemplos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#exemplos)[Direcionamento por interesse](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#interests)[Campos](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#campos-2)[Saiba mais](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_R_OYzP6XARmbREAqxjvYbLtGQSoaP9Szj_XlhUPxhAuelmEkH9SPkCm7AQ_aem_01SQJ1U2HBtn8tAp3wDwWg&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5pJp_B_DMJBw5ryPwGgxGSg-eqRZygiCPKHic3ouBFmwMd6RB7HOuSt8z2NA_aem_UVl5eOckF6XUlvIloRUTCA&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5JIWyZIkQspiPI9PaqkjSMn_5gWF-y-NgndmaHfc-kcEeD5GAynF_GhLt3pg_aem_T7r6XZysV0Rx53DB7XwQqw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4oiVPEpxJKwhNPb3nveuo-YoOFEcQcBYNb-PzrIg7XJx7WSR57_XnnDLZh6A_aem_A7jImXhNeYujwT_q-5kUmw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_R_OYzP6XARmbREAqxjvYbLtGQSoaP9Szj_XlhUPxhAuelmEkH9SPkCm7AQ_aem_01SQJ1U2HBtn8tAp3wDwWg&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7y5Bt8qc5AQD90I3692v-xxs2p1mpF6GVjEIdbIvaTPAuf_yId_TYt7qNjuw_aem_7LRAPkcBRjBsCf9cwX10Fw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_R_OYzP6XARmbREAqxjvYbLtGQSoaP9Szj_XlhUPxhAuelmEkH9SPkCm7AQ_aem_01SQJ1U2HBtn8tAp3wDwWg&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ueMNL7O0eI1TBCzJKHmWhcY6q0zSo_LLFVwdntuJJJ4HKi9kHbVFKPdFZug_aem_sSY1CY-7cySWnDTVTw-Xpg&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5pJp_B_DMJBw5ryPwGgxGSg-eqRZygiCPKHic3ouBFmwMd6RB7HOuSt8z2NA_aem_UVl5eOckF6XUlvIloRUTCA&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5pJp_B_DMJBw5ryPwGgxGSg-eqRZygiCPKHic3ouBFmwMd6RB7HOuSt8z2NA_aem_UVl5eOckF6XUlvIloRUTCA&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vJawd94C5LYtcGl8gXagquHigPNDL-aUqbjddsOrXyWPqRvIMRsZ7R2c-1Q_aem_jt6b-8LPqZlEOe6hvh5T2A&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_R_OYzP6XARmbREAqxjvYbLtGQSoaP9Szj_XlhUPxhAuelmEkH9SPkCm7AQ_aem_01SQJ1U2HBtn8tAp3wDwWg&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5iNME8WAemMu8PoZOmL8GqI1rd05npMnuOiTyIgkxxUNzpqf4Avc-uhBYLHw_aem_Rmh5r_ds8fJWXNRaXT4aEA&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65MYovTeedoO61JsuyhE6nlqbZrmy4SOC2igGKELqDaLY0ofQVjBD6hopRNQ_aem_6F0XE8Tu8viFhEdPU35LBw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5FdbOX8T-1leeZl99rFJA2vmsP4nsmVbdMQpZ7fxZ8WCYLi1nwixS6-U2RmQ_aem_1WQ1q81tL6n_YnbQ0adsIQ&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vJawd94C5LYtcGl8gXagquHigPNDL-aUqbjddsOrXyWPqRvIMRsZ7R2c-1Q_aem_jt6b-8LPqZlEOe6hvh5T2A&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7y5Bt8qc5AQD90I3692v-xxs2p1mpF6GVjEIdbIvaTPAuf_yId_TYt7qNjuw_aem_7LRAPkcBRjBsCf9cwX10Fw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vJawd94C5LYtcGl8gXagquHigPNDL-aUqbjddsOrXyWPqRvIMRsZ7R2c-1Q_aem_jt6b-8LPqZlEOe6hvh5T2A&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5pJp_B_DMJBw5ryPwGgxGSg-eqRZygiCPKHic3ouBFmwMd6RB7HOuSt8z2NA_aem_UVl5eOckF6XUlvIloRUTCA&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65MYovTeedoO61JsuyhE6nlqbZrmy4SOC2igGKELqDaLY0ofQVjBD6hopRNQ_aem_6F0XE8Tu8viFhEdPU35LBw&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6O_Z-bGeQtWdxSbKg1DeSXRdABtD7uP8ao-i65cM_vWQiJvYXLZmM5lxgkSyA3Qt2B4FMUvlTDhsDxWRFhu-_WThXV_UwjkwXykFAEFkFiPWfQqAZGlsomxQdppM5Nn513wFWkvklyoWaFkiGvAqzJ8CM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão