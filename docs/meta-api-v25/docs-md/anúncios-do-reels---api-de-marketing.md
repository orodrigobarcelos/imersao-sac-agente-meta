<!-- Fonte: Anúncios do Reels - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/creative/reels-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios do Reels


Crie um anúncio da Meta com foco nos posicionamentos de Reels disponíveis e aprenda as boas práticas para operações de anúncios.


## Pré-requisitos


- Ter criado anteriormente um app do Facebook
- Ter familiaridade com APIs de Marketing e ter o Login do Facebook habilitado


Se você não atende a esses pré-requisitos, consulte nossa [documentação para desenvolvedores](https://developers.facebook.com/docs/marketing-apis/get-started).


### Teste no sandbox


A Meta oferece um ambiente de teste, que não veicula anúncios, mas permite:


- Adicionar a API de Marketing como um produto no seu app da Meta na seção Ferramentas para criar e editar anúncios usando nossas APIs sem incorrer em custos
- Criar uma conta de anúncios para usar a API de Marketing


Leia nossas [boas práticas para testes](https://developers.facebook.com/docs/marketing-api/best-practices/#testing).
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 1: acessar o ativo


Um [token de acesso](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/) é uma string opaca que identifica um usuário, um app ou uma Página. Esse identificador pode ser usado pelo app para fazer chamadas da Graph API. É possível ver quando ele expira e por qual app ele foi gerado. As chamadas da API de Marketing em apps da Meta precisam incluir um token de acesso.


Obtenha um token de acesso com as permissões necessárias:


- `ads_management`: faz alterações nas contas de anúncios selecionadas
- `ads_read`: lê os dados de anúncios
- `read_insights`: lê insights de desempenho


Use tokens de acesso ao sistema pois eles têm prazos de validade mais longos.


### Camada adicional de autorização


É necessário criar um app de empresa para acessar os pontos de extremidade da API de Marketing. Os apps de empresa estão sujeitos a uma camada adicional de autorização da Graph API chamada de níveis de acesso. Durante o processo de análise, seu app também deverá solicitar permissões e recursos específicos. Conclua a verificação da empresa se você pretende disponibilizar o app para usuários que não tenham função no app ou na empresa relacionada.


Se o app estiver gerenciando contas de anúncios de outras pessoas, você precisará de:


- `ads_read` com acesso avançado


e/ou


- `ads_management` com acesso avançado
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 2: obter a conta de anúncios


Obtenha a(s) conta(s) de anúncios dos seus anunciantes e permita que eles selecionem uma para criação de anúncios.


Você pode ver todas as contas de anúncios às quais a empresa tem acesso por meio da API de Gerenciamento de Anúncios, que retorna todas as contas de anúncios de uma empresa. Observe que você precisará da permissão `business_management` no nível de app e usuário. Consulte as [APIs de Gerenciamento de Ativos de Negócios](https://developers.facebook.com/docs/marketing-api/business-asset-management).


#### Exemplo de chamada


```
curl -G \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<BUSINESS_ID>/owned_ad_accounts"
```
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 3: criar uma campanha


A campanha é o nível mais alto da estrutura organizacional da conta de anúncios e deve representar um objetivo único para o anunciante. Estes objetos contêm seu objetivo de publicidade e um ou mais conjuntos de anúncios. Isso ajuda você a otimizar e a medir os resultados para cada objetivo de publicidade. Saiba mais sobre como criar, ler, atualizar e excluir uma campanha [aqui](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group).


#### Exemplo de chamada


```
curl -X POST \
  -F 'name="My campaign"' \
  -F 'objective="OUTCOME_TRAFFIC"' \
  -F 'status="PAUSED"' \
  -F 'special_ad_categories=[]' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns
```
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 4: definir o direcionamento


Para permitir que os anunciantes alcancem grupos específicos, especifique estes parâmetros nas suas solicitações de API:


- Dados demográficos (idade, gênero, localização)
- interesses
- comportamentos


Com isso, seu anúncio alcançará clientes em potencial [que tenham maior probabilidade de se interessar](https://developers.facebook.com/docs/marketing-api/audiences/reference/basic-targeting/) pelos seus produtos ou serviços.


#### Exemplo de chamada


```
curl -X POST \
  -F 'access_token=YOUR_ACCESS_TOKEN' \
  -F 'name=My Custom Audience' \
  -F 'subtype=CUSTOM' \
  -F 'description=People who live in New York, aged 25-40, interested in technology' \
  -F 'customer_file_source=USER_PROVIDED_ONLY' \
  -F 'targeting_spec={
        "geo_locations": {
          "countries": ["US"],
          "regions": [{"key": "4081"}]  # New York region key
        },
        "age_min": 25,
        "age_max": 40,
        "interests": [{"id": "6003139266461", "name": "Technology"}]
      }' \
  https://graph.facebook.com/v25.0/act_YOUR_AD_ACCOUNT_ID/customaudiences
```
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 5: criar um conjunto de anúncios


Conjuntos de anúncios podem conter um ou mais anúncios. Os anúncios contidos em um conjunto devem ter o mesmo direcionamento, orçamento, a mesma cobrança, meta de otimização e duração.


Você pode definir o orçamento, a programação, o direcionamento, a estratégia de lance e as opções de posicionamento. Os conjuntos de anúncios permitem ajustar como e onde os anúncios são veiculados para segmentos de público específicos, otimizando o desempenho e alcançando objetivos de marketing.


Principais parâmetros:


- Critérios para direcionamento de público
- Orçamentos diários ou vitalícios
- Opções de programação para controlar quando os anúncios serão exibidos


Veja mais detalhes [aqui](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign).


Você pode escolher um posicionamento manual que inclua anúncios do Instagram e do Facebook Reels ou usar os posicionamentos automáticos. Se você não especificar um determinado campo de posicionamento, todas as posições-padrão possíveis serão consideradas para esse campo.


#### Exemplo de chamada


```
curl -X POST \
  -F 'access_token=YOUR_ACCESS_TOKEN' \
  -F 'name=Reels Ad Set' \
  -F 'campaign_id=YOUR_CAMPAIGN_ID' \
  -F 'daily_budget=5000' \
  -F 'billing_event=IMPRESSIONS' \
  -F 'optimization_goal=REACH' \
  -F 'start_time=2024-07-10T10:00:00-0700' \
  -F 'end_time=2024-07-20T10:00:00-0700' \
  -F 'targeting={"geo_locations":{"countries":["US"]},"age_min":18,"age_max":65}' \
  -F 'promoted_object={"page_id":"YOUR_PAGE_ID"}' \
  -F 'status=PAUSED' \
  -F 'instagram_user_id=<IG_USER_ID>' \
  -F 'publisher_platforms=["instagram"]' \
  -F 'instagram_positions=["reels"]' \
  https://graph.facebook.com/v25.0/act_YOUR_AD_ACCOUNT_ID/adsets
```


### Direcionamento de posicionamentos: posições disponíveis no Reels, objetivos compatíveis e objetivos de otimização


| `publisher_platforms` | `facebook_position` ou `instagram position` | Objetivos compatíveis | `optimization_goal` |
| --- | --- | --- | --- |
| ` instagram ` | reels , profile_reels | `OUTCOME_APP_PROMOTION` | LINK_CLICKS OFFSITE_CONVERSIONS APP_INSTALLS |
| ` instagram ` | reels , profile_reels | ` OUTCOME_AWARENESS` | REACH IMPRESSIONS AD_RECALL_LIFT THRUPLAY |
| ` instagram ` | reels , profile_reels | ` OUTCOME_LEADS` | OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS LINK_CLICKS REACH IMPRESSIONS LEAD_GENERATION QUALITY_LEAD |
| ` instagram ` | reels , profile_reels | `OUTCOME_TRAFFIC` | LINK_CLICKS LANDING_PAGE_VIEWS REACH CONVERSATIONS IMPRESSIONS VISIT_INSTAGRAM_PROFILE |
| ` instagram ` | reels , profile_reels | `OUTCOME_ENGAGEMENT` | CONVERSATIONS LINK_CLICKS THRUPLAY POST_ENGAGEMENT REACH IMPRESSIONS REMINDERS_SET OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS |
| ` instagram ` | reels , profile_reels | OUTCOME_SALES | OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS LINK_CLICKS REACH IMPRESSIONS CONVERSATIONS |
| `facebook` | `facebook_reels` | OUTCOME_APP_PROMOTION | LINK_CLICKS OFFSITE_CONVERSIONS APP_INSTALLS |
| `facebook` | `facebook_reels` | OUTCOME_AWARENESS | REACH IMPRESSIONS AD_RECALL_LIFT THRUPLAY TWO_SECOND_CONTINUOUS_VIDEO_VIEWS |
| `facebook` | `facebook_reels` | OUTCOME_LEADS | OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS LINK_CLICKS REACH IMPRESSIONS LEAD_GENERATION QUALITY_LEAD |
| `facebook` | `facebook_reels` | OUTCOME_TRAFFIC | LINK_CLICKS LANDING_PAGE_VIEWS REACH CONVERSATIONS IMPRESSIONS QUALITY_CALL |
| `facebook` | `facebook_reels` | OUTCOME_ENGAGEMENT | CONVERSATIONS LINK_CLICKS THRUPLAY TWO_SECOND_CONTINUOUS_VIDEO_VIEWS POST_ENGAGEMENT REACH IMPRESSIONS EVENT_RESPONSES QUALITY_CALL OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS PAGE_LIKES |
| `facebook` | `facebook_reels` | OUTCOME_SALES | OFFSITE_CONVERSIONS LANDING_PAGE_VIEWS LINK_CLICKS REACH IMPRESSIONS CONVERSATIONS QUALITY_CALL |


### Limitações


| Combinação de objetivo compatível + `optimization_goal` | Qualificado para Reels do Facebook? | Qualificado para Reels do Instagram? |
| --- | --- | --- |
| OUTCOME_AWARENESS + TWO_SECOND_CONTINUOUS_VIDEO_VIEWS | ✅ | ❌ |
| OUTCOME_TRAFFIC + VISIT_INSTAGRAM_PROFILE | ❌ | ✅ |
| OUTCOME_TRAFFIC + QUALITY_CALL | ✅ | ❌ |
| OUTCOME_ENGAGEMENT + TWO_SECOND_CONTINUOUS_VIDEO_VIEWS | ✅ | ❌ |
| OUTCOME_ENGAGEMENT + EVENT_RESPONSES | ✅ | ❌ |
| OUTCOME_ENGAGEMENT + REMINDERS_SET | ❌ | ✅ |
| OUTCOME_ENGAGEMENT + QUALITY_CALL | ✅ | ❌ |
| OUTCOME_ENGAGEMENT + PAGE_LIKES | ✅ | ❌ |
| OUTCOME_SALES + QUALITY_CALL | ✅ | ❌ |

[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 6: selecionar o criativo


Os criativos são os componentes visuais e textuais do anúncio e são compatíveis com os seguintes formatos de anúncio:


- Imagens
- Vídeos
- Carrosséis
- Designs de anúncios personalizados


Automatize os elementos de design e otimize o desempenho usando nosso [processo criativo](https://developers.facebook.com/docs/marketing-api/reference/ad-creative).


### Reutilize um reel existente como criativo do anúncio


Os usuários podem fornecer um novo ativo ou reaproveitar um reel existente na sua conta do Instagram como criativo do anúncio.


Você pode criar anúncios a partir de Reels orgânicos existentes do Instagram ou do Facebook que sejam elegíveis para serem promovidos, desde que preencham estas condições:


- Tenham menos de 90 segundos
- Tenham uma taxa de proporção vertical em tela cheia (9:16)
- Não tenham música com direitos autorais, GIFs, figurinhas interativas ou filtros de câmera de terceiros
- Não tenham sido compartilhados no Facebook


Para reutilizar um reel orgânico do Instagram como criativo do anúncio em uma nova campanha de anúncios:


- Obtenha a identificação da conta comercial do Instagram, que precisa estar conectada a uma Página do Facebook - `GET/{ad_account_id}/connected_instagram_accounts`**ou** - `GET/{business_id}/instagram_business_accounts`
- Encontre o reel que deseja promover - `GET/{ig-business-account-user-id}/media`
- Forneça o criativo do anúncio - Em vez de indicar `instagram_actor_id` na especificação do criativo, defina `instagram_user_id` como a identificação do usuário do Instagram - Especifique `source_instagram_media_id` como identificação de mídia - Opcionalmente, atualize `call_to_action` para sua promoção


[Utilize o campo `boost_eligibility_info`](https://developers.facebook.com/docs/instagram/ads-api/guides/use-posts-as-ads/) como um modo conveniente de verificar se uma mídia pode ser turbinada como anúncio e `boost_ads_list` para acompanhar informações anteriores de anúncios turbinados.


#### Exemplo de chamada


```
curl -i -X POST \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT>/adcreatives?object_id=<PAGE_ID>
&instagram_user_id=<IG_USER_ID>
&source_instagram_media_id=<IG_ORGANIC_MEDIA_ID>
&call_to_action="{'type':'LEARN_MORE','value':{'link': '<YOUR_LINK>'}}"
&access_token=<API_ACCESS_TOKEN>
```


### Caixa de ferramentas criativas de IA generativa


Você pode [automatizar a geração de elementos de anúncios diversos e envolventes](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features/), como imagens, vídeos e texto. Essas ferramentas baseadas em IA ajudam a otimizar o desempenho dos anúncios, adaptando o conteúdo às preferências do público e aumentando a variedade dos criativos. A criação de anúncios resultará em maior engajamento e campanhas melhores.
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 7: ver uma prévia do anúncio


[Veja uma prévia do anúncio](https://developers.facebook.com/docs/marketing-api/generatepreview/v21.0) nos formatos Facebook Reels e Instagram Reels tabulados abaixo usando:


- A identificação do anúncio
- A identificação do criativo do anúncio
- A especificação do criativo do anúncio


| PLATAFORMA DE PUBLICAÇÃO | Formato do anúncio |
| --- | --- |
| Facebook | DESKTOP_FEED_STANDARD , FACEBOOK_STORY_MOBILE , INSTANT_ARTICLE_STANDARD , INSTREAM_VIDEO_DESKTOP , INSTREAM_VIDEO_MOBILE , MARKETPLACE_DESKTOP , MARKETPLACE_MOBILE , MOBILE_FEED_BASIC , MOBILE_FEED_STANDARD , RIGHT_COLUMN_STANDARD , SUGGESTED_VIDEO_DESKTOP , SUGGESTED_VIDEO_MOBILE , WATCH_FEED_MOBILE , FACEBOOK_REELS_BANNER , FACEBOOK_REELS_BANNER_DESKTOP , FACEBOOK_REELS_MOBILE , FACEBOOK_REELS_POSTLOOP , FACEBOOK_REELS_STICKER , FACEBOOK_STORY_STICKER_MOBILE , WATCH_FEED_HOME |
| Instagram | INSTAGRAM_STANDARD , INSTAGRAM_STORY , INSTAGRAM_EXPLORE_CONTEXTUAL , INSTAGRAM_EXPLORE_IMMERSIVE , INSTAGRAM_EXPLORE_GRID_HOME , INSTAGRAM_FEED_WEB , INSTAGRAM_FEED_WEB_M_SITE , INSTAGRAM_PROFILE_FEED , INSTAGRAM_REELS , INSTAGRAM_REELS_OVERLAY , INSTAGRAM_SEARCH_CHAIN , INSTAGRAM_SEARCH_GRID , INSTAGRAM_STORY_CAMERA_TRAY , INSTAGRAM_STORY_WEB , INSTAGRAM_STORY_WEB_M_SITE |


#### Exemplo de chamada


```
curl -X POST \
  'https://graph.facebook.com/v25.0/act_{ad_account_id}/adpreviews' \
  -F 'access_token={your_access_token}' \
  -F 'creative={
        "object_story_spec": {
            "instagram_user_id": "<IG_USER_ID>",
            "video_data": {
                "video_id": "{video_id}",
                "title": "Check out our new product!",
                "description": "Exciting new features and benefits.",
                "call_to_action": {
                    "type": "LEARN_MORE",
                    "value": {
                        "link": "https://www.example.com/product"
                    }
                }
            }
        }
    }' \
  -F 'ad_format=INSTAGRAM_REELS'
```
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 8: programar a veiculação dos anúncios


Para [reservar um anúncio](https://developers.facebook.com/docs/marketing-api/reference/adgroup) usando a API de Marketing, crie um objeto de grupo de anúncios e vincule seu objeto do conjunto de anúncios ao criativo do anúncio. Use `/act_{ad_account_id}/ads` para enviar seu objeto de anúncio e valide a resposta para confirmar que a reserva foi bem-sucedida. Essa etapa finaliza a configuração do seu anúncio, deixando-o pronto para veiculação com base nas configurações fornecidas.


#### Exemplo de chamada


```
curl -X POST \
  -F 'name="My Ad"' \
  -F 'adset_id="<AD_SET_ID>"' \
  -F 'creative={
       "creative_id": "<CREATIVE_ID>"
     }' \
  -F 'status="PAUSED"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Etapa 9: analisar o desempenho


Use a [API de Insights](https://developers.facebook.com/docs/marketing-api/insights/) para obter métricas da conta de anúncios para anúncios:


- `act_<AD_ACCOUNT_ID>/insights`
- `<CAMPAIGN_ID>/insights`
- `<ADSET_ID>/insights`
- `<AD_ID>/insights`


Se você estiver veiculando uma campanha no Instagram e no Facebook, adicione `breakdowns=publisher_platform` para visualizar as estatísticas de posicionamento do Facebook e do Instagram separadamente, conforme o exemplo de chamada abaixo. Ao detalhar insights por nível de posicionamento, será possível ver o desempenho dos anúncios pelos posicionamentos dos Facebook e Instagram Reels.


#### Exemplo de chamada


```
curl -X GET \
  'https://graph.facebook.com/v25.0/{ad_account_id}/insights' \
  -F 'access_token={your_access_token}' \
  -F 'level=campaign' \
  -F 'fields=campaign_name,impressions,clicks,spend' \
  -F 'breakdowns=publisher_platform,platform_position' \
  -F 'filtering=[{"field":"platform_position","operator":"IN","value":["instagram_reels"]}]' \
  -F 'time_range={"since":"2024-06-01","until":"2024-06-30"}'
```


### Considerações importantes


#### Novos objetivos compatíveis com validação de objetivo de experiências com anúncios orientados para resultados (ODAX, na sigla em inglês)


- `OUTCOME_APP_PROMOTION`
- `OUTCOME_AWARENESS`
- `OUTCOME_ENGAGEMENT`
- `OUTCOME_LEADS`
- `OUTCOME_SALES`
- `OUTCOME_TRAFFIC`


### Limites de volume


A API de Marketing tem a própria [lógica de limitação de volume](https://developers.facebook.com/docs/marketing-apis/rate-limiting/) e está excluída de todos os limites de volume da Graph API. O recurso que afeta a cota de limitação de volume da API de Marketing é o Acesso Padrão ao Gerenciamento de Anúncios. Por padrão, você obtém **Acesso Padrão** quando adiciona o produto da API de Marketing ao seu Painel de Apps, que fornece acesso de desenvolvedor à API de Marketing. Para aumentar a cota de limitação de volume, atualize para **acesso avançado**.


### Noções básicas sobre criativos


Anúncios no Reels transformam a atenção em ação, turbinando resultados. Quando criados da maneira certa, são ainda mais eficazes.


**1. Crie no formato 9:16 para deixar seu vídeo cativante:** Reels é um formato imersivo em tela cheia. Para ajudar seu criativo a se encaixar aqui, considere começar com um vídeo e redimensioná-lo para 9:16.


**2. Crie nas zonas de segurança para que sua mensagem fique clara:** trabalhe dentro das zonas de segurança para que suas sobreposições de figurinha de texto, chamadas para ação ou mensagens principais não sejam obscurecidas pela interface do usuário do Reels. Mantenha 35% da parte inferior do criativo em 9:16 sem textos, logotipos e outros elementos importantes.


**3. Utilize o som para deixar seu vídeo mais divertido:** áudio, seja música, sobreposição de voz ou efeitos sonoros, é um grande impulsionador de engajamento e entretenimento no Reels.
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)

## Mídia dinâmica com vídeo de produto do catálogo


Use o vídeo de produto do catálogo nos posicionamentos do Reels para melhorar seu catálogo e a experiência de anúncios. Com a mídia dinâmica, você pode veicular ativos de vídeo do seu catálogo juntamente com as imagens de produtos existentes nas suas campanhas de anúncios de catálogo Advantage+. A mídia dinâmica permite que você estenda seu alcance para o Instagram Reels e Facebook Reels. Além disso, consolida várias campanhas de vídeo em uma única campanha de anúncios dinâmicos. Você pode usar anúncios de mídia dinâmica em diferentes posicionamentos, mas nosso foco é usar anúncios de mídia dinâmica nos posicionamentos do Reels aqui.


Os anúncios de mídia dinâmica mostrarão imagens ou vídeos dos itens do seu catálogo com base no que cada pessoa que visualizar seu anúncio provavelmente achará interessante. A mídia dinâmica usa automação e classificação de produtos para fornecer não apenas os produtos mais relevantes, mas também os ativos com maior desempenho para públicos em todos os posicionamentos.


### Por que usar vídeos de produtos do catálogo?


Os vídeos de produtos do catálogo são aceitos em todos os verticais do catálogo, e os anúncios de mídia dinâmica estão abertos a todos os anunciantes. O vídeo de produtos do catálogo é uma boa opção para anunciantes que gostariam de melhorar as suas [campanhas de anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/get-started) com criativos de vídeo mais inspiradores.


### Requisitos


Para criar anúncios de mídia dinâmica que são veiculados no Reels, você precisará de um catálogo de produtos com produtos existentes e pelo menos um vídeo para cada item do produto em um formato URL de vídeo para download. Para obter mais informações, veja [Mídia dinâmica](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/dynamic-media/).


### Etapa 1: [configure](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/dynamic-media/#add-videos-to-your-catalog) o catálogo de vídeos de produtos do catálogo


- Certifique-se de que pelo menos um vídeo por produto tenha uma taxa de proporção de 9:16 para ter o melhor desempenho no Reels - Os anúncios de mídia dinâmica selecionarão automaticamente um vídeo 9:16 para os posicionamentos do Reels - Se um vídeo 9:16 não estiver disponível, o primeiro vídeo será usado
- Certifique-se de que os vídeos fornecidos para o seu catálogo estejam hospedados em URLs para download
- O áudio é bem-vindo e pode ter um impacto positivo no seu anúncio, mas não é necessário
- Você pode adicionar tags aos vídeos do seu catálogo para serem usadas `preferred_video_tags` no anúncio


### Etapa 2: crie uma campanha de anúncios compatível com posicionamentos do Reels e anúncios de catálogo Advantage+


- [Criação de campanha do Reels](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started/#campaign)
- [Criação de campanha de anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/get-started#step-1--create-an-ad-campaign) - Certifique-se de que o objetivo da sua campanha de anúncios seja `OUTCOME_SALES`, `LINK_CLICKS`, `APP_INSTALLS` ou `CONVERSIONS`


### Etapa 3: crie um conjunto de anúncios direcionando os posicionamentos do Reels com um conjunto de produtos


- [Criação de conjunto de anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/get-started#adset)
- [Criação de conjunto de anúncios de posicionamento do Reels](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started/#adset)
- Defina uma meta de otimização que se alinhe ao seu objetivo no nível da campanha e respeite as nossas [regras de validação](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt-goal-validation)
- Defina as opções adequadas de direcionamento, orçamento, evento de cobrança e programação
- Certifique-se de que `publisher_platforms` esteja definido como `["instagram","facebook"]`, e que `facebook_positions` e `instagram_positions` estejam definidos como reels
- Defina seu `product_set_id` desejado no `promoted_object` para seu conjunto de anúncios a fim de promover produtos a partir desse conjunto de produtos


### Etapa 4: [crie um anúncio de mídia dinâmica](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/dynamic-media/#create-ads-with-dynamic-media)


- Certifique-se de que esteja criando um anúncio em carrossel ou um anúncio em formato de vídeo único. Anúncios de coleção com vídeos de produtos do catálogo ainda não são aceitos nos posicionamentos do Reels. Os anúncios em carrossel contêm uma série de produtos diferentes de um conjunto. O vídeo único mostrará um produto de cada vez do conjunto de produtos especificado
- [Mais informações sobre vídeos de produtos de catálogo](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/dynamic-media/faq)
[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)[○](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#)Nesta Página[Anúncios do Reels](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#an-ncios-do-reels)[Pré-requisitos](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#pr--requisitos)[Teste no sandbox](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#sandbox)[Etapa 1: acessar o ativo](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#step1)[Camada adicional de autorização](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#camada-adicional-de-autoriza--o)[Etapa 2: obter a conta de anúncios](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-2--obter-a-conta-de-an-ncios)[Etapa 3: criar uma campanha](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-3--criar-uma-campanha)[Etapa 4: definir o direcionamento](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-4--definir-o-direcionamento)[Etapa 5: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-5--criar-um-conjunto-de-an-ncios)[Direcionamento de posicionamentos: posições disponíveis no Reels, objetivos compatíveis e objetivos de otimização](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#direcionamento-de-posicionamentos--posi--es-dispon-veis-no-reels--objetivos-compat-veis-e-objetivos-de-otimiza--o)[Limitações](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#limita--es)[Etapa 6: selecionar o criativo](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-6--selecionar-o-criativo)[Reutilize um reel existente como criativo do anúncio](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#reutilize-um-reel-existente-como-criativo-do-an-ncio)[Caixa de ferramentas criativas de IA generativa](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#caixa-de-ferramentas-criativas-de-ia-generativa)[Etapa 7: ver uma prévia do anúncio](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-7--ver-uma-pr-via-do-an-ncio)[Etapa 8: programar a veiculação dos anúncios](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-8--programar-a-veicula--o-dos-an-ncios)[Etapa 9: analisar o desempenho](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-9--analisar-o-desempenho)[Considerações importantes](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#considera--es-importantes)[Limites de volume](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#limites-de-volume)[Noções básicas sobre criativos](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#no--es-b-sicas-sobre-criativos)[Mídia dinâmica com vídeo de produto do catálogo](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#m-dia-din-mica-com-v-deo-de-produto-do-cat-logo)[Por que usar vídeos de produtos do catálogo?](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#por-que-usar-v-deos-de-produtos-do-cat-logo-)[Requisitos](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#requisitos)[Etapa 1: configure o catálogo de vídeos de produtos do catálogo](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-1--configure-o-cat-logo-de-v-deos-de-produtos-do-cat-logo)[Etapa 2: crie uma campanha de anúncios compatível com posicionamentos do Reels e anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-2--crie-uma-campanha-de-an-ncios-compat-vel-com-posicionamentos-do-reels-e-an-ncios-de-cat-logo-advantage-)[Etapa 3: crie um conjunto de anúncios direcionando os posicionamentos do Reels com um conjunto de produtos](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-3--crie-um-conjunto-de-an-ncios-direcionando-os-posicionamentos-do-reels-com-um-conjunto-de-produtos)[Etapa 4: crie um anúncio de mídia dinâmica](https://developers.facebook.com/docs/marketing-api/creative/reels-ads#etapa-4--crie-um-an-ncio-de-m-dia-din-mica) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4D82Frde3ONaorU-qnYpmGiF_bENBum24T05uNIMkr-vKPQB8ExhDICO9ILQ_aem_pfsNz8ki4ZBUFo83Wi-vSA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ZU1nRX4hmghGA3nviwN80KTohVeTfp3PElKLymToeCtl03hpP28J_Nfs2pA_aem_e-xilen2ygxV4SOk7XPhGw&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sXQ6I4ObZOZWbQSJ1BfRNErJ9WjDGpjgnXKOApsz1TPoYO0jton7r9eGWMw_aem_BJwhZNI5BdbfHinsiHp1-Q&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Mk-EraPUlw6HaB_YyAgFk4sRk9GFrtwDBdB1KPfXUBvzTsRigC8eJ0ovo_w_aem_3R062o_eaY-FriZ4Jnx6_g&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uFixweZOFXmM9jswHPwm1bX_WmYZnVz0iFl6NaWSQvr9VMIEgFS0p2kvUBw_aem_LMcfL46kOslT7_YaxgtudA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xsxElanDjUACIwaNBoDJ696blz_XQ3uffjQqsjlznVNWhCCwlhLqWQJl4FA_aem_-2mvkTL69Q0OCKhdgS1brQ&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4g6H5frGjXmVrcrS8YGUS4HTvXM2Sb00zWA4UampSPe1qUgKbcNS0KNJTK5A_aem_Q84w5RzM66I5W1LEnX6rJg&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4D82Frde3ONaorU-qnYpmGiF_bENBum24T05uNIMkr-vKPQB8ExhDICO9ILQ_aem_pfsNz8ki4ZBUFo83Wi-vSA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sXQ6I4ObZOZWbQSJ1BfRNErJ9WjDGpjgnXKOApsz1TPoYO0jton7r9eGWMw_aem_BJwhZNI5BdbfHinsiHp1-Q&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4D82Frde3ONaorU-qnYpmGiF_bENBum24T05uNIMkr-vKPQB8ExhDICO9ILQ_aem_pfsNz8ki4ZBUFo83Wi-vSA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xsxElanDjUACIwaNBoDJ696blz_XQ3uffjQqsjlznVNWhCCwlhLqWQJl4FA_aem_-2mvkTL69Q0OCKhdgS1brQ&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5xsxElanDjUACIwaNBoDJ696blz_XQ3uffjQqsjlznVNWhCCwlhLqWQJl4FA_aem_-2mvkTL69Q0OCKhdgS1brQ&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uFixweZOFXmM9jswHPwm1bX_WmYZnVz0iFl6NaWSQvr9VMIEgFS0p2kvUBw_aem_LMcfL46kOslT7_YaxgtudA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4g6H5frGjXmVrcrS8YGUS4HTvXM2Sb00zWA4UampSPe1qUgKbcNS0KNJTK5A_aem_Q84w5RzM66I5W1LEnX6rJg&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6oheVbysnW_VtCpHP98GmxLfaM9q2llBp4bnZvpni2zp66XZKok3OyH4z48Q_aem_MhO2uuQJNN-pw_PRh6xnhQ&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uFixweZOFXmM9jswHPwm1bX_WmYZnVz0iFl6NaWSQvr9VMIEgFS0p2kvUBw_aem_LMcfL46kOslT7_YaxgtudA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4g6H5frGjXmVrcrS8YGUS4HTvXM2Sb00zWA4UampSPe1qUgKbcNS0KNJTK5A_aem_Q84w5RzM66I5W1LEnX6rJg&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ZU1nRX4hmghGA3nviwN80KTohVeTfp3PElKLymToeCtl03hpP28J_Nfs2pA_aem_e-xilen2ygxV4SOk7XPhGw&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sXQ6I4ObZOZWbQSJ1BfRNErJ9WjDGpjgnXKOApsz1TPoYO0jton7r9eGWMw_aem_BJwhZNI5BdbfHinsiHp1-Q&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uFixweZOFXmM9jswHPwm1bX_WmYZnVz0iFl6NaWSQvr9VMIEgFS0p2kvUBw_aem_LMcfL46kOslT7_YaxgtudA&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6B7HCBU9-5trWi17SwHBKyFl-N7uu93XIMvT_B7uqXUb3s-pGJd7icG8PmsIZgESEy_WyRh4tU54syVs364As0XrUnFhHPdGh0FefHE3a7_OY1KVNPtKM1L4omUqB4R716IOSxEoo4i5Io9Gqf9NiGV3E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão