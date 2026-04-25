<!-- Fonte: Criar público - Criativo do anúncio.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Criar um público para imóveis


A partir do lançamento da **versão 15.0 da API de Marketing**, não será mais possível criar públicos de anúncio especial. Consulte [Públicos de anúncio especial](https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category#special-ad-audiences) para saber mais informações.


Crie um público para imóveis:


- [Etapa 1: configurar sinais de usuários de eventos para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#events)
- [Etapa 2: associar sinais de usuários ao catálogo](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#associate-signals-to-catalog)
- [Etapa 3: criar um grupo de origens de eventos para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#create-event-source-group)
- [Etapa 4: criar públicos para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#create-audiences)


## Etapa 1: configurar sinais de usuários de eventos para imóveis


Estes são nomes de eventos predefinidos que você pode enviar do seu site ou app e que permitem medir o desempenho das campanhas, além de capturar a intenção dos públicos. Consulte [Configuração do Pixel do Facebook](https://developers.facebook.com/docs/marketing-api/audiences-api/pixel).


Anúncios imobiliários exigem estes eventos padrão do pixel do seu site e app para celular:


| Evento de pixel | Evento do app | Nível do requisito | Descrição |
| --- | --- | --- | --- |
| Search | fb_mobile_search | ◉ | Alguém pesquisou nos classificados de propriedades |
| ViewContent | fb_mobile_content_view | ◉ | Alguém visualizou um cadastro específico |
| InitiateCheckout | fb_mobile_initiated_ checkout | ◉ | Alguém salvou, curtiu ou demonstrou interesse especial em um cadastro |
| Purchase | fb_mobile_purchase | ◉ | Alguém entrou em contato com um corretor sobre um cadastro |


- ◉ **Obrigatório**: os anúncios não funcionarão sem esses parâmetros.
- ◎ **Recomendado**: não é estritamente necessário, mas permite melhores recomendações e mais opções de direcionamento para os seus anúncios. Forneça o máximo possível.
- ◯ **Não obrigatório**: não é obrigatório e pode ser ignorado.


Por exemplo, para relatar um evento de Pesquisa de um cadastro usando o pixel do Facebook ou eventos do app, coloque este código na sua página de resultados da pesquisa:

```
<!-- Facebook Pixel Code -->
```

```
Bundle parameters = new Bundle();
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_TYPE, "home_listing");
parameters.putString(AppEventsConstants.EVENT_PARAM_CONTENT_ID, "[\"1234\", \"2345\", \"3456\", \"4567\"]"); // top search results

// we must prefix all travel-specific parameters with fb_
parameters.putString("fb_city", "New York City"); // Required for Search event
parameters.putString("fb_region", "New York"); // region is the state for the US. Required for Search event
parameters.putString("fb_country", "US"); // Required for Search event

logger.logEvent(
  AppEventsConstants.EVENT_NAME_SEARCHED,
  parameters
);
```

```
[FBSDKAppEvents logEvent:FBSDKAppEventNameSearched
  parameters:@{
    FBSDKAppEventParameterNameContentType : @"home_listing",
    FBSDKAppEventParameterNameContentID : @"[\"1234\", \"2345\", \"3456\", \"4567\"]", // top search results
		// we must prefix all travel-specific parameters with fb_
		@"fb_city" : @"New York City", //Required for Search event
	  @"fb_region" : @"New York", // region is the state for the US. Required for Search event
	  @"fb_country" : @"US", // Required for Search event
  }
];
```


Depois de determinar os eventos que serão inicializados, forneça os parâmetros de cada evento.
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)

## Parâmetros dos eventos


A tabela abaixo mostra os parâmetros recomendados e obrigatórios.


| Parâmetro do pixel | Parâmetro de dispositivos móveis | Nível do requisito |
| --- | --- | --- |
| content_ids | fb_content_id | ◉ |
| content_type | fb_content_type | ◯ |
| lease_start_date |  | ◎ |
| lease_end_date |  | ◎ |
| preferred_baths_range |  | ◎ |
| preferred_beds_range |  | ◎ |
| preferred_price_range |  | ◎ |
| currency | fb_currency | ◎ |
| property_type |  | ◎ |
| listing_type |  | ◎ |
| availability |  | ◎ |
| city | fb_city | ◎ |
| neighborhood |  | ◎ |
| region | fb_region | ◎ |
| country | fb_country | ◎ |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)

## Detalhes do parâmetro


| Nome do parâmetro | Tipo de dados | Descrição |
| --- | --- | --- |
| availability | string | O valor deve ser available_soon , for_rent , for_sale , off_market , recently_sold ou sale_pending . |
| city | string | Forneça a cidade de interesse do usuário, por exemplo, 'Menlo Park' |
| content_ids | string ou string[] | Qualquer ID do seu catálogo de cadastro. Por exemplo, para o evento ViewContent , envie o ID do item visualizado ou, para Search , envie uma matriz de IDs para os principais resultados: ['1234', '2345', '3456', '4567'] |
| content_type | string ou string[] | Por exemplo: 'home_listing' ['home_listing', 'product'] ['home_listing', 'hotel'] |
| country | string | Direcione para o seu país de interesse, como 'United States' |
| currency | string | Especificado usando o formado de moeda da norma ISO 4217: 'USD' |
| lease_start_date | string | Nos permite recomendar propriedades com base na sua disponibilidade de data (usando available_dates_price_config no catálogo) e melhorar a experiência de destino do usuário (usando tags de modelo). Especificado usando o formato de data da norma ISO 8601: 'YYYY-MM-DD' (por exemplo, 2018-01-01 ). |
| lease_end_date | string | Especificado usando o formato de data da norma ISO 8601: 'YYYY-MM-DD' (por exemplo, '2018-02-01' ). |
| listing_type | string | O valor deve ser for_rent_by_agent , for_rent_by_owner , for_sale_by_agent , for_sale_by_owner , foreclosed , new_construction ou new_listing . |
| neighborhood | string | Bairro de interesse: 'Menlo Oaks' |
| preferred_baths_range | [int (mínimo) , int (máximo) ] | Número de banheiros selecionados em um intervalo: [1, 2] |
| preferred_beds_range | [int (mínimo) , int (máximo) ] | Número de quartos selecionados em um intervalo: [1, 2] |
| preferred_price_range | [float (mínimo) , float (máximo) ] | Faixa de preço: [1000.99, 2000.99] |
| property_type | string | Deve ser apartment , condo , house , land , manufactured , other ou townhouse . |
| region | string | Estado, distrito ou região de interesse: 'California' |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)

## Etapa 2: associar sinais de usuários ao catálogo de cadastros


Associe as origens dos eventos a cada um dos seus catálogos de classificados. Consulte [Página de catálogo do Gerenciador de Negócios](https://business.facebook.com/settings/product-catalogs/). Para selecionar o pixel e o app por meio da API que envia eventos, faça uma chamada `HTTP POST`:

```
curl \
  -F '0=
```


Especifique estes parâmetros:


| Nome do campo | Tipo de dados | Descrição |
| --- | --- | --- |
| external_event_sources (obrigatório) | int[] | Lista de IDs do app e do pixel que serão associados ao catálogo. |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)

## Etapa 3: criar e compartilhar grupos de origens de eventos para imóveis


Para criar um público, o administrador da sua empresa deve criar um grupo de origens de eventos. Ele reúne todas as suas origens que enviam sinais de interesse no cadastro. Como fazer uma chamada `HTTP POST`:

```
curl \
  -F 'name=My Real Estate Company Events' \
  -F 'event_sources=['
```


Depois, compartilhe o grupo de origens de eventos com todas as contas de anúncios que vão veicular anúncios aos públicos gerados por essas origens de eventos. Como fazer uma chamada `HTTP POST`:

```
curl \
  -F 'accounts=['
```
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)

## Etapa 4: criar públicos


Nesse momento, você tem sinais de pixels ou eventos de app configurados e associados a um [grupo de origens de eventos](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#create-event-source-group) e seu catálogo imobiliário. Para direcionar os classificados às pessoas interessadas nos seus cadastros, crie um público dinâmico. Inclua ou exclua pessoas do público de acordo com os sinais de intenção. Você também pode aplicar mais filtros baseados em regras para personalizar o público da mesma forma que nos Públicos Personalizados do site. Consulte [Públicos Personalizados](https://developers.facebook.com/docs/marketing-api/audiences-api/websites).


Para configurar um novo público, faça uma chamada `HTTP POST` para `/act_<AD_ACCOUNT_ID>/customaudiences`.


### Parâmetros necessários


| Nome do campo | Tipo de dados | Descrição |
| --- | --- | --- |
| name | string | Nome do público. |
| subtype | enum {CLAIM} | Tipo de público personalizado. Deve ser definido como CLAIM . |
| claim_objective | enum {HOME_LISTING} | Objetivo do público. Deve ser definido como HOME_LISTING . |
| event_source_group | id | Grupo de origens de eventos para criar um público. |
| inclusions | object[] | Matriz de objetos JSON. Relacione cada sinal de intenção que torna alguém qualificado para este público. |
| inclusões: event (obrigatório) | enum { Search, ViewContent, InitiateCheckout, Purchase } | Nome do evento de um sinal. Usado para inclusão em um público: {'event': 'Search', …} . |
| inclusões: retention (obrigatório) | object | Tempo mínimo e máximo desde que o evento foi recebido. Determine se o evento será considerado para inclusão. Exemplo: {…, 'retention': {'min_seconds': 0, 'max_seconds': 259200}, …} . A retenção mínima deve ser de 4 horas. |
| inclusões: count | operadores JSON | Número de vezes que o evento foi acionado. Você pode usar operadores de comparação numéricos e de igualdade, como {…'count': {'lte': 3}, …} . |


### Parâmetros opcionais


| Nome do campo | Tipo de dados | Descrição |
| --- | --- | --- |
| content_type | enum {HOME_LISTING} | Tipos de sinal usados para criar este público. |
| description | string | Descrição do público. |
| exclusions | object[] | Matriz de objetos JSON listando cada sinal de intenção que exclui alguém deste público. |
| exclusões: event (obrigatório) | enum { Search, ViewContent, InitiateCheckout, Purchase } | Nome do evento de um sinal usado para exclusão: {'event': 'Search', …} . |
| exclusões: retention (obrigatório) | object | Tempo mínimo e máximo desde que o evento foi recebido. Determina se o evento é considerado para exclusão, por exemplo, {…, 'retention': {'min_seconds': 0, 'max_seconds': 259200}, …} . A retenção mínima deve ser de 4 horas. |
| rule | object | Regra de público a partir de Públicos Personalizados de sites. Filtre o fluxo de eventos por essas regras antes de processar qualquer inclusions e exclusions . Veja a lista de campos específicos disponíveis. Você pode usar esses campos com qualquer operador JSON padrão para Regras de público . |
| regra: home_listing_set_id (obrigatório) | object | ID do conjunto de classificados: {'eq': '1234'}} |


Por exemplo, para criar um público composto por pessoas que visualizaram ou compraram nos últimos 14 dias:

```
curl \
  -F 'name=Viewed or Purchased Last 14 days' \
  -F 'subtype=CLAIM' \
  -F 'claim_objective=HOME_LISTING' \
  -F 'content_type=HOME_LISTING' \
  -F 'event_source_group=
```
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#)Nesta Página[Criar um público para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#criar-um-p-blico-para-im-veis)[Etapa 1: configurar sinais de usuários de eventos para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#events)[Parâmetros dos eventos](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#par-metros-dos-eventos)[Detalhes do parâmetro](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#detalhes-do-par-metro)[Etapa 2: associar sinais de usuários ao catálogo de cadastros](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#associate-signals-to-catalog)[Etapa 3: criar e compartilhar grupos de origens de eventos para imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#create-event-source-group)[Etapa 4: criar públicos](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#create-audiences)[Parâmetros necessários](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#par-metros-necess-rios)[Parâmetros opcionais](https://developers.facebook.com/docs/marketing-api/real-estate-ads/audience#par-metros-opcionais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7tTeo11_GrNjxLuwUuemfUy253-zB5mqNviQ3cNMGLZAYB-jmK8-oF6LXIqA_aem_3d5k4VS7ppaj0VFYoO6Zlw&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7NqMrJQfn10Xfv-NCdmd42OT06HhHj4JQ24PwKebmEtS0oQ0fesz5CTnUF9A_aem_B-qiOJN3fsxrMtOOIiP2kg&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7tTeo11_GrNjxLuwUuemfUy253-zB5mqNviQ3cNMGLZAYB-jmK8-oF6LXIqA_aem_3d5k4VS7ppaj0VFYoO6Zlw&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OA04nY8sbUiWRnVBshAtqXTdJW8X7f7fNwMyBeGAOPdUZmK1CXrrjj02S1g_aem_FpSo33zPyLXgYp51U0ZZEA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6M-NSjA2zSQMvu7cGn_QeWdtx2cwBQVj0EVwXpxaphoW8PXfzOUam5q3H8XQ_aem_Ot5mED6HhD6ziue_z3Rh_w&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7tTeo11_GrNjxLuwUuemfUy253-zB5mqNviQ3cNMGLZAYB-jmK8-oF6LXIqA_aem_3d5k4VS7ppaj0VFYoO6Zlw&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7oyPdMo6uY4cJfx09nZ45gBtl0X_dx3OMHh6gmuIdHjR2b0g-zgE72d7IMmw_aem_BnZHJrLvb59M0yqJWTi-zA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5wHjj8icYVkPN9Yn7FrsaL5-cbPV2_rbjZ9ba-LvZxgOPXAAE6ofcQSljRSg_aem_q801iX7FeauGXCUsjwwSeQ&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5CCeo4HUh6kfnUDRrgRdtYuJnFY0fzX5gG5IDpbpqcihfL2aT6Nh1HocHGLQ_aem_Lhhn34BBaMujvckVqbqU-A&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6M-NSjA2zSQMvu7cGn_QeWdtx2cwBQVj0EVwXpxaphoW8PXfzOUam5q3H8XQ_aem_Ot5mED6HhD6ziue_z3Rh_w&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OA04nY8sbUiWRnVBshAtqXTdJW8X7f7fNwMyBeGAOPdUZmK1CXrrjj02S1g_aem_FpSo33zPyLXgYp51U0ZZEA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7oyPdMo6uY4cJfx09nZ45gBtl0X_dx3OMHh6gmuIdHjR2b0g-zgE72d7IMmw_aem_BnZHJrLvb59M0yqJWTi-zA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7oyPdMo6uY4cJfx09nZ45gBtl0X_dx3OMHh6gmuIdHjR2b0g-zgE72d7IMmw_aem_BnZHJrLvb59M0yqJWTi-zA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7NqMrJQfn10Xfv-NCdmd42OT06HhHj4JQ24PwKebmEtS0oQ0fesz5CTnUF9A_aem_B-qiOJN3fsxrMtOOIiP2kg&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7oyPdMo6uY4cJfx09nZ45gBtl0X_dx3OMHh6gmuIdHjR2b0g-zgE72d7IMmw_aem_BnZHJrLvb59M0yqJWTi-zA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7oyPdMo6uY4cJfx09nZ45gBtl0X_dx3OMHh6gmuIdHjR2b0g-zgE72d7IMmw_aem_BnZHJrLvb59M0yqJWTi-zA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OA04nY8sbUiWRnVBshAtqXTdJW8X7f7fNwMyBeGAOPdUZmK1CXrrjj02S1g_aem_FpSo33zPyLXgYp51U0ZZEA&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5CCeo4HUh6kfnUDRrgRdtYuJnFY0fzX5gG5IDpbpqcihfL2aT6Nh1HocHGLQ_aem_Lhhn34BBaMujvckVqbqU-A&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4y5ykvqJPPoJzsQxjLpn6NAVEPeQ8WFb8wbvTe4O5aB5jwvMcTqUHbmoq_dw_aem_5rcQy1-TooKhAGBcYq0ozw&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6M-NSjA2zSQMvu7cGn_QeWdtx2cwBQVj0EVwXpxaphoW8PXfzOUam5q3H8XQ_aem_Ot5mED6HhD6ziue_z3Rh_w&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4R02YGj90UUUfUy0vB4jxlufNlb_HNBDgDn1lQ0cwigQEd2e7GEFI2fM13zsRyaFtxPAyiNz9m0EFTUWjHlqnHuWPOG3VtqPrZffLPz6WQ3LKuZo8WIKMW4F-nsAKqBnYEsjXPOEH_ouAR8OgbN_W-q3s)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão