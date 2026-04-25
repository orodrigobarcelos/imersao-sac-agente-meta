<!-- Fonte: Anúncios de imóveis – introdução  - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios de imóveis – introdução


As empresas de comércio precisam passar pelo processo de [verificação](https://developers.facebook.com/docs/marketplace/realestate/business-verification) para publicar classificados de imóveis.


**Etapa 1: criar um [catálogo de classificados de imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#create-home-listing-catalog)**.


**Etapa 2: [configurar os classificados e definir preços](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#setup-home-listing-and-pricing)**.


**Etapa 3: [escolher opções de atualização](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#update-options)**.


**Etapa 4: [filtrar o catálogo no conjunto de classificados](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#filter-to-home-listing-set)**.


**Etapa 5: [enviar conversões offline](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#send-offline-conversions)** (opcional)


**Etapa 6: criar um [público para os imóveis](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-real-estate/audience)**. Diferentemente do que acontece com os classificados de imóveis publicados pelos usuários, para integrações de parceiros, os leads são enviados por meio de um formulário, e não pela conversa do Messenger. Saiba mais sobre como [recuperar leads para comércio](https://developers.facebook.com/docs/marketplace/realestate/leads).


**Etapa 7: [criar e veicular anúncios](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-real-estate/ads-management) para seus classificados de imóveis**.


**Etapa 8: obter informações de veiculação para ver como as pessoas no Facebook interagem com seus anúncios**. Consulte a referência sobre [insights de anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/).


**Etapa 9: usar ferramentas de depuração para diagnosticar e resolver problemas**. Consulte [Ferramentas de depuração dos Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/debugging-tools).


## Etapa 1: criar um catálogo de classificados de imóveis


### Anúncios de catálogo Advantage+


Seu catálogo deve conter uma lista de imóveis que você deseja anunciar. Consulte a [referência sobre catálogo](https://developers.facebook.com/docs/marketing-api/reference/product-catalog).


Se você quiser criar um catálogo de classificados de imóveis para anúncios de catálogo Advantage+, defina `vertical` como `home_listings`:

```
curl \
  -F 'name=Home Listing Catalog Name' \
  -F 'vertical=home_listings' \
  -F 'access_token=<ACCESS TOKEN>' \
  https://graph.facebook.com/<API_VERSION>
```


Para usar a API de catálogo, você precisa ter o [nível de acesso adequado à API de Marketing](https://developers.facebook.com/docs/marketing-api/access#limits) e aceitar os [Termos de Serviço](https://business.facebook.com/legal/product_catalog_terms/) criando seu primeiro catálogo por meio do [Gerenciador de Negócios](https://business.facebook.com/).


### Comércio


Veja instruções sobre como criar um catálogo para comércio na documentação a respeito da [plataforma Marketplace](https://developers.facebook.com/docs/marketplace/realestate/uploading-listings#create-a-real-estate-catalog-with-the-product-catalog-ui).
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)

## Etapa 2: configurar os classificados e definir preços


Os classificados contêm informações sobre as propriedades, como ID do imóvel anunciado, nome, disponibilidade, descrição, endereço, número de quartos, quantidade de banheiros e assim por diante. Sua empresa pode carregar ou buscar um conjunto de classificados de imóveis. Um item do classificado é um imóvel único exibido no seu site ou app.


### Formatos de feed compatíveis


Você pode ter um feed único para todos os imóveis do catálogo ou vários feeds nos quais cada feed representa os imóveis de um país, de uma imobiliária ou de um corretor.


**Para anúncios de catálogo Advantage+**, é preciso fornecer o feed de classificados em um destes formatos:


| Formato do arquivo | Descrição | Arquivo de exemplo |
| --- | --- | --- |
| XML | Normalmente gerado por sistemas de provedores de feed automatizados. Um nó XML \<listings\> raiz abrange um conjunto de nós \<listing\> , em que cada nó representa um classificado de imóvel. O arquivo deve iniciar por uma tag de declaração \<?xml válida. | Baixar |
| CSV, TSV | A primeira linha deve listar os nomes de campo escolhidos na ordem em que os valores serão fornecidos. As linhas seguintes mostram os valores correspondentes para cada classificado de imóvel. Os campos aninhados ou com vários valores, como "image", podem ser representados por valores codificados em JSON ou por um conjunto de colunas de texto simples e sem formatação, rotuladas com a sintaxe de caminho JSON, como image[0].url , image[0].tag[0] , image[0].tag[1] . | Baixar (CSV) |


**Para comércio**, é preciso fornecer o feed de classificados em formato **XML**:


| Formato do arquivo | Descrição |
| --- | --- |
| XML | Normalmente gerado por sistemas de provedores de feed automatizados. Um nó XML \<listings\> raiz abrange um conjunto de nós \<listing\> , em que cada nó representa um classificado de imóvel. O arquivo deve iniciar por uma tag de declaração \<?xml válida. |
| CSV, TSV, JSON | Estes formatos não são aceitos no momento. |


Nosso analisador de feeds detecta automaticamente as codificações de texto `UTF8`, `UTF16` ou `UTF32` e usa `LATIN1` quando há uma sequência de bytes inesperada.


#### Exemplo de feed em XML


```
<?xml version="1.0" encoding="UTF-8"?>
<listings>
    <title>example.com Feed</title>
    <link rel="self" href="http://www.example.com"/>
    <listing>
        <home_listing_id>12345678</home_listing_id>
        <name>1 Hacker Way, Menlo Park, CA 94025</name>
        <availability>for_rent</availability>
        <description>An amazing listing</description>
        <address format="simple">
            <component name="addr1">1 Hacker Way</component>
            <component name="city">Menlo Park</component>
            <component name="region">California</component>
            <component name="country">United States</component>
            <component name="postal_code">94025</component>
        </address>
        <latitude>1.11414</latitude>
        <longitude>-1.835003</longitude>
        <neighborhood>Menlo Oaks</neighborhood>
        <image>
            <url>http://example.com/12345678-1.jpg</url>
        </image>
        <image>
            <url>http://example.com/12345678-2.jpg</url>
        </image>
        <image>
            <url>http://example.com/12345678-3.jpg</url>
        </image>
        <listing_type>for_rent_by_agent</listing_type>
        <num_baths>6</num_baths>
        <num_beds>5</num_beds>
        <num_units>1</num_units>
        <price>110000 USD</price>
        <property_type>house</property_type>
        <url>http://www.example.com/link_to_listing</url>
        <year_built>2007</year_built>
    </listing>
</listings>
```


### Campos compatíveis – Classificados de imóveis


Os campos compatíveis a seguir foram desenvolvidos para itens que você adiciona ao seu catálogo de produtos. Para ver uma lista completa dos campos compatíveis, consulte a [referência de classificados de imóveis](https://developers.facebook.com/docs/marketing-api/reference/home-listing/).


Para catálogos localizados, consulte os [campos compatíveis com classificados de imóveis](https://developers.facebook.com/docs/marketing-api/catalog/reference#loc-cat-home).


Nosso analisador de feeds detecta automaticamente as codificações de texto `UTF8`, `UTF16` ou `UTF32` e usa `LATIN1` quando há uma sequência de bytes inesperada. Embora o texto referente aos valores dos campos possa ser inserido em qualquer idioma, os nomes dos campos precisam ser fornecidos exatamente conforme descrito abaixo, em inglês.


| Nome e tipo de campo | Descrição |
| --- | --- |
| home_listing_id tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O ID único do classificado de imóvel (apartamento/condomínio), que deve ser o mais detalhado possível. Exemplo: FB_home_1234 |
| home_listing_group_id tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. A identificação única do edifício ou do apartamento. Deve ser único por grupo. |
| name tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O título do classificado de imóvel. Exemplo: Modern Eichler in Green Oaks |
| availability tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. Disponibilidade atual do classificado de imóvel. Valores aceitos: for_sale , for_rent , sale_pending , recently_sold , off_market , available_soon . Para comércio, "for_rent" é o único valor aceito. |
| address tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O endereço do imóvel que deve levar à localização da propriedade. Consulte os parâmetros do objeto Address . 1 Hacker Way |
| address.city tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. A cidade onde o imóvel está localizado. Consulte os parâmetros do objeto Address . Exemplo: Menlo Park |
| address.region tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O estado, o condado, a região ou a província do imóvel. Consulte os parâmetros do objeto Address . Exemplo: Menlo Park |
| address.country tipo: objeto | Obrigatório para anúncios de catálogo Advantage+ e comércio. O país onde o imóvel está localizado. Consulte os parâmetros do objeto Address . Exemplo: United States |
| address.postal_code tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O país onde o imóvel está localizado. Consulte os parâmetros do objeto Address . Exemplo: United States |
| latitude tipo: float | Obrigatório para anúncios de catálogo Advantage+ e comércio. A latitude do classificado. Exemplo: 37.484100 |
| longitude tipo: float | Obrigatório para anúncios de catálogo Advantage+ e comércio. A longitude do classificado. Exemplo: -122.148252 |
| neighborhood tipo: string | Obrigatório para anúncios de catálogo Advantage+. Opcional, mas recomendado para comércio. Máximo de bairros permitidos: 20 Bairro do classificado onde o imóvel está localizado. É possível incluir vários bairros. Se houver mais de um bairro, inclua colunas adicionais para cada tipo e use a sintaxe de caminho JSON nos nomes das colunas para indicar o número de bairros. Exemplo: neighborhood[0]; neighborhood[1] |
| price tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O preço da venda ou do aluguer do imóvel. Formate o preço como o custo, seguido pelo código de moeda ISO de 3 dígitos (https://en.wikipedia.org/wiki/ISO_4217?fbclid=IwAR0_xYfUmL3kIUA6sMeEaFAzbJa4MLeMiPDPrftFSX6wkKiTXxPinC-5j70"), incluindo um espaço entre o custo e a moeda. Exemplo: 13,999 USD |
| image tipo: objeto | Obrigatório para anúncios de catálogo Advantage+ e comércio. Número máximo de imagens: 20 Tamanho máximo: 4 MB O URL da imagem usado no seu anúncio. Para as taxas de proporção quadradas (1:1) no formato do anúncio em carrossel, a imagem deve ser de 600 x 600.; Para anúncios com imagem única, ela deve ser de pelo menos 1.200 x 630 pixels.; Para comércio : a primeira imagem é exibida no feed comercial como a foto da capa. Exemplo: image[0].url , image[0].tag[0] Consulte os parâmetros do objeto Image . |
| url tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. Link para a página do classificado do imóvel. Deve ser um URL válido. Consulte os parâmetros do objeto Image . Exemplo: http://www.realestate.com |
| description tipo: string | Opcional para anúncios de catálogo Advantage+. Obrigatório para comércio. Número máximo de caracteres: 5.000 A descrição do imóvel. Exemplo: Beautiful 3BD home available in Belmont |
| num_beds tipo: float | Opcional para anúncios de catálogo Advantage+. Obrigatório para comércio. O número total de quartos. Pode ser 0 para apartamentos do tipo "studio". Exemplo: 2 |
| num_baths tipo: float | Opcional para anúncios de catálogo Advantage+. O número total de banheiros. Para comércio, deve ser pelo menos 1 . |
| num_rooms tipo: float | Não aplicável a anúncios de catálogo Advantage+. Obrigatório para comércio. O número total de quartos do imóvel. |
| property_type tipo: string | Opcional para anúncios de catálogo Advantage+. O tipo de propriedade. Valores aceitos para anúncios de catálogo Advantage+: apartment , condo , house , land , manufactured , other , townhouse . Valores aceitos para comércio: apartment , builder_floor , condo , house , house_in_condominium , house_in_villa , loft , penthouse , studio , townhouse , other . |
| listing_type tipo: string | Opcional para anúncios de catálogo Advantage+. O tipo de classificado do imóvel. Valores aceitos para anúncios de catálogo Advantage+: for_rent_by_agent , for_rent_by_owner , for_sale_by_agent , for_sale_by_owner , foreclosed , new_construction , new_listing . Valores aceitos para comércio: for_rent_by_agent , for_rent_by_owner . |
| area_size tipo: número inteiro | Não aplicável a anúncios de catálogo Advantage+. Obrigatório para comércio. A área ou o espaço da planta baixa do imóvel. |
| area_unit tipo: string | Não aplicável a anúncios de catálogo Advantage+. Obrigatório para comércio. As unidades (pés ou metros quadrados) do valor da área útil do imóvel. Valores aceitos: sq_ft , sq_m . |
| ac_type tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. O tipo de sistema de ar condicionado. Valores aceitos: central , other , none . |
| furnish_type tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. O tipo de mobília disponível no imóvel. Valores aceitos: furnished , semi-furnished , unfurnished . |
| heating_type tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. O tipo de sistema de aquecimento instalado no imóvel. Valores aceitos: central , gas , electric , radiator , other , none . |
| laundry_type tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. O tipo de lavanderia disponível. Valores aceitos: in_unit , in_building , other , none . |
| num_units tipo: número inteiro | Opcional para anúncios de catálogo Advantage+ e comércio. O número total de unidades (apartamentos/condomínios) disponíveis para aluguel. Exemplo: 0 |
| parking_type tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. O tipo de estacionamento disponível no imóvel. Valores aceitos: garage , street , off-street , other , none . |
| partner_verification tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. Indica se a empresa parceira verificou o classificado. Valores aceitos: verified , none . |
| year_built tipo: string | O ano de construção do imóvel, usando o formato AAAA (ano de quatro dígitos). Exemplo: 1994 |
| pet_policy tipo: string | Não aplicável a anúncios de catálogo Advantage+. Opcional para comércio. Indica se animais de estimação são permitidos no imóvel: cat , dog , all , none . |
| available_dates_price_config tipo: objeto | Uma lista com datas disponíveis e preços de um classificado. Quando você fornece os valores, o Facebook pode recomendar classificados com base nas datas disponíveis e mostrar dinamicamente o preço associado no seu anúncio. Consulte os parâmetros do objeto Available Dates . |
| applink tipo: objeto | O link do app para o classificado. |
| status Tipo: string | Controla se um item está ativo ou foi arquivado no seu catálogo. Apenas itens ativos podem ser vistos por pessoas nos seus anúncios, lojas ou outros canais. Valores compatíveis: active , archived . Os itens estão ativos por padrão. Saiba mais sobre como arquivar itens . Exemplo: active Observação : algumas plataformas parceiras como a Shopify podem sincronizar itens ao seu catálogo com um status chamado staging . Ele se comporta da mesma forma que archived . Esse campo era chamado anteriormente de visibility . Apesar da compatibilidade do antigo nome desse campo, recomendamos que você use o novo nome. |


### Campos obrigatórios específicos do país – Somente para comércio


[Acesse a documentação da plataforma Marketplace e confira os campos obrigatórios específicos do país para comércio.](https://developers.facebook.com/docs/marketplace/realestate/uploading-listings#country_specific)


### Parâmetros do objeto Image


| Nome e tipo de campo | Descrição |
| --- | --- |
| url tipo: string | Obrigatório para anúncios de catálogo Advantage+ e comércio. O URL da imagem de origem. Siga estas especificações de imagem: Todas as imagens precisam estar em formato JPG, GIF ou PNG.; Para anúncios em carrossel e em coleções: as imagens são exibidas no formato quadrado (1:1). O tamanho mínimo da imagem é 500 x 500 px. Recomendamos 1.024 x 1.024 px para garantir melhor qualidade.; Para anúncios de imagem única: a imagem é exibida na taxa de proporção 1.91:1. O tamanho mínimo da imagem é 500 x 500 px. Recomendamos 1.200 x 628 px para garantir melhor qualidade. |
| tag tipo: string | Opcional para anúncios de catálogo Advantage+ e comércio. A tag anexada à imagem que mostra o que aparece na figura. É possível associar diversas tags a uma imagem. Exemplos: Fitness Center e Swimming Pool INSTAGRAM_STANDARD_PREFERRED – permite que os anunciantes marquem uma imagem específica no próprio feed como a imagem-padrão a ser usada no Instagram. A tag diferencia letras maiúsculas de minúsculas. |


### Parâmetros do objeto Address


| Nome e tipo de campo | Descrição |
| --- | --- |
| addr1 tipo: string | Obrigatório . O endereço do imóvel. Exemplo: 675 El Camino Real |
| city tipo: string | Obrigatório . A cidade onde o hotel está localizado. Exemplo: Palo Alto |
| region tipo: string | Obrigatório . O estado, o condado, a região ou a província onde o imóvel está localizado. Exemplo: California |
| country tipo: string | Obrigatório . O país do imóvel. Exemplo: United States |
| postal_code tipo: string | O código postal ou o CEP do imóvel. Obrigatório , a menos que o país não tenha um sistema de código postal. Exemplos: 94125 , NW1 3FG |


### Configuração de preços e datas disponíveis


Com `available_dates_price_config`, você pode fornecer a disponibilidade e os preços de cada imóvel para um intervalo de datas específico. Quando você inclui um período neste campo, o Facebook considera essa disponibilidade nas nossas recomendações de produtos e tenta mostrar classificados disponíveis para as datas pesquisadas no seu site. Como alternativa, se você incluir preços, também poderemos mostrar valores específicos para datas no criativo do seu anúncio. **Para habilitar esse recurso, será preciso enviar ao Facebook `lease_start_date` e `lease_end_date` nos seus [eventos de pixel](https://developers.facebook.com/docs/marketing-api/dynamic-ads-for-real-estate/audience).**


#### Parâmetros do objeto Available Dates


| Nome e tipo de campo | Descrição |
| --- | --- |
| start_date tipo: string | Opcional quando end_date é fornecido. O início do intervalo de datas disponíveis no formato ISO-8601 (incluindo a data inicial). Se você fornecer apenas start_date , end_date será definido como um ano a partir dessa data por padrão. Exemplo: YYYY-MM-DD , como 2018-01-01 . |
| end_date tipo: string | Opcional quando start_date é fornecido. O término do intervalo de datas disponíveis no formato ISO-8601 (excluindo a data final). Se você fornecer apenas end_date , start_date será definido como a data atual por padrão. Exemplo: YYYY-MM-DD , como 2018-02-01 . |
| rate tipo: string | Um número inteiro que representa o preço do classificado no período escolhido. Exemplo: 10000 se o classificado tiver o preço de $100.00 USD . |
| currency tipo: string | Obrigatório quando rate é fornecido. O código de moeda nos padrões ISO-4217 . Exemplo: USD , GBP e assim por diante. |
| interval tipo: string | O tempo da estadia para a taxa especificada. Valores aceitos: nightly , weekly , monthly , sale . |


Confira abaixo um exemplo que mostra a disponibilidade de um classificado e como ele aparece em JSON:

```
"available_dates_price_config": [
    {
        // available until 11/01 at $150/night
        "end_date": "2018-11-01",
        "rate": "15000",
        "currency": "USD",
        "interval": "nightly",
    },
    {
        // available from 11/01 - 12/01 at $200/night
        "start_date": "2018-11-01",
        "end_date": "2018-12-01",
        "rate": "20000",
        "currency": "USD",
        "interval": "nightly",
    },
    {
        // available from 11/01 onward at $500/week
        "start_date": "2018-11-01",
        "rate": "50000",
        "currency": "USD",
        "interval": "weekly",
    },
]
```


### Deep links de produtos


[Forneça deep links](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-deep-links/) no seu feed seguindo a especificação do [App Links](https://developers.facebook.com/docs/applinks). As informações de deep link no feed têm prioridade sobre as que o Facebook coleta com metadados de App Links no nosso rastreador da web.


Não será necessário especificar esses dados se você já tiver informações de deep link do App Links. O Facebook usa as informações do App Links para exibir o deep link certo. Para exibir deep links nos seus anúncios, consulte a documentação sobre os [modelos de anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/ads-management/#adtemplate).
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)

## Etapa 3: escolher opções de atualização


### Anúncios de catálogo Advantage+


**Para anúncios de catálogo Advantage+**, você pode atualizar as informações do classificado de imóvel no catálogo das seguintes maneiras com carregamento direto. Consulte a [referência sobre feed de carregamento direto](https://developers.facebook.com/docs/marketing-api/reference/product-feed/uploads/).


**Exemplo**: você pode fazer um carregamento único manualmente:

```
curl \
  -F "url=http://www.example.com/sample_feed.xml" \
  -F "access_token=
```


### Comércio


**Para comércio**, você pode atualizar as informações do classificado de imóvel no catálogo configurando um carregamento de feed recorrente (programado) e atualizando seu feed. No Marketplace, é altamente recomendável usar a opção Set a Schedule.


#### Configurar uma programação para carregar o feed de dados do catálogo


- Acesse o [**Gerenciador de Comércio**](https://www.facebook.com/products).
- Clique em **Data Sources**.
- Clique em **Add Data Source**.
- Clique em **Use Data Feeds** e em **Next**.
- Clique em **Set a schedule**.
- Escolha com que frequência você quer que o Facebook verifique se há atualizações no seu feed de dados: **Daily**, **Hourly** e **Weekly**. Se você escolher **Hourly** ou **Weekly**, também será possível especificar quando o carregamento programado deve se repetir.
- Digite o URL direto para o feed. Você pode incluir URLs que usam HTTP, HTTPS, FTP ou SFTP. Observação: o URL deve apontar diretamente para o arquivo do feed de dados; caso contrário, o carregamento pode falhar.
- (Opcional) Digite o nome de usuário e a senha do provedor do feed de dados. Isso é diferente do nome de usuário e da senha que você usa para acessar sua conta de anúncios do Facebook.
- Insira um nome para o feed de dados.
- Escolha o tipo de moeda para o feed de dados. O tipo de moeda será usado caso você não tenha especificado essa informação no arquivo de feed de dados.
- Clique em **Avançar**.
- Revise seu arquivo de feed de dados para identificar possíveis erros. Se houver colunas obrigatórias em branco no seu arquivo ou colunas que o Facebook não reconhece, será possível mapear as opções apropriadas [**aqui**](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#setup-home-listing-and-pricing). Todas as colunas mapeadas aqui são salvas para futuros carregamentos do feeds de dados.
- Clique em **Avançar**.


#### Carregar um feed em vários idiomas


Para comércio, oferecemos compatibilidade com uma experiência multilíngue. Ao adicionar um feed de idioma secundário a um catálogo, você pode criar outro feed com o segundo idioma desse catálogo único. As informações nos feeds secundários substituem o idioma padrão quando o público relevante vê seus classificados.


**Esse recurso é aplicável apenas a países parceiros específicos. Entre em contato com seu representante do Facebook para conferir a disponibilidade no seu mercado.**


- Crie um catálogo com um feed de dados para seu país e idioma padrão.
- Crie um arquivo XML apenas com o ID do classificado (**home_listing_id**) e outros campos que precisam ser traduzidos para o idioma local, como nome, descrição ou campos adicionais. Para substituir as informações, o **home_listing_id** deve corresponder aos IDs no feed de dados do catálogo original.
- Inclua o feed de informações adicionais do Gerenciador de Comércio. *Inclua o feed adicional do Gerenciador de Comércio em Add Home Listing Information e Add Language Information.*
- Confirme as 2 fontes de dados dentro do mesmo catálogo.
[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)

## Etapa 4: filtrar o catálogo no conjunto de classificados


Este é um grupo de itens em um catálogo que você divulga nos seus anúncios de catálogo Advantage+. Cada catálogo de classificados pode ter diversos conjuntos de classificados.

```
curl \
  -F "name=test set" \
  -F 'filter={"availability":{"eq":"for_sale"}}' \
  -F "access_token=" \
  https://graph.facebook.com/
```


O `filter` acima é formado pelos seguintes operadores e dados:


| Operadores | Tipo de filtro |
| --- | --- |
| i_contains | Contém substring (não diferencia maiúsculas de minúsculas) |
| i_not_contains | Não contém substring (não diferencia maiúsculas de minúsculas) |
| contains | Contém substring (diferencia maiúsculas de minúsculas) |
| not_contains | Não contém substring (diferencia maiúsculas de minúsculas) |
| eq | Igual a (não diferencia maiúsculas de minúsculas) |
| neq | Diferente de (não diferencia maiúsculas de minúsculas) |
| lt | Menor que (somente campos numéricos) |
| lte | Menor que ou igual a (somente campos numéricos) |
| gt | Maior que (somente campos numéricos) |
| gte | Maior que ou igual a (somente campos numéricos) |


| Dados | Dados do filtro |
| --- | --- |
| availability | A disponibilidade do classificado. Exemplo: for_sale |
| listing_type | O tipo de classificado. Exemplo: for_sale_by_agent |
| property_type | O tipo de imóvel. Exemplo: house |
| price | O preço do classificado. |
| name | Nome |
| city | Cidade |
| country | País |
| region | A região ou o estado. |
| postal_code | CEP |
| num_beds | Quantidade de camas |
| num_baths | Quantidade de banheiros |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)

## Etapa 5: enviar conversões offline


É possível enviar eventos de conversão offline e ver quantos clientes visualizaram ou clicaram em anúncios do Facebook e classificados comerciais antes da conversão. Para isso, use a [API de Conversões Offline](https://developers.facebook.com/docs/marketing-api/offline-conversions) e adicione os campos a seguir na [etapa **4. Carregamento de eventos offline**](https://developers.facebook.com/docs/marketing-api/offline-conversions#requirements).


### Chaves de correspondência


As chaves de correspondência comparam uma conversão a um usuário.


| Chave | Descrição |
| --- | --- |
| email | Endereços de email Hash |
| phone | Números de telefone Hash |
| fn | Nome Hash |
| ln | Sobrenome Hash |
| madid | Identificador de anunciante da Apple ou ID de publicidade do Android Hash |
| zip | Códigos postais Hash |
| ct | Cidade Hash |
| st | Estado Hash |
| country | País Hash |
| dob | Data de nascimento (formato DD) Hash |
| doby | Data de nascimento (formato AAAA) Hash |
| gen | Gênero Hash |
| age | Idade Hash |
| lead_id | IDs de leads do Marketplace |


### Dados personalizados


Os dados personalizados comparam uma conversão a um revendedor.


| Campo | Descrição |
| --- | --- |
| content_ids | home_listing_id do carregamento do catálogo. |
| content_type | Defina como home_listing . |


### Detalhes do evento


Os detalhes do evento descrevem o evento de conversão offline que ocorreu. A frequência de carregamento é diária, em até 48 horas após o evento.


| Campo | Descrição |
| --- | --- |
| event_name | Obrigatório Enumeração do tipo de evento: ViewContent Search AddToCart AddToWishlist Lead = ligação ou outro lead qualificado CompleteRegistration = configuração de horas marcadas InitiateCheckout = visita à agência AddPaymentInfo = visualização do imóvel Purchase = contrato assinado Other |
| event_time | Obrigatório . A hora do evento. |
| value | Obrigatório . O valor do aluguel. Definido como 0 para eventos que não forem de aluguel. |
| currency | Obrigatório . O código da moeda. |

[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)[○](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#)Nesta Página[Anúncios de imóveis – introdução](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#an-ncios-de-im-veis---introdu--o)[Etapa 1: criar um catálogo de classificados de imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#create-home-listing-catalog)[Anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#an-ncios-de-cat-logo-advantage-)[Comércio](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#com-rcio)[Etapa 2: configurar os classificados e definir preços](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#setup-home-listing-and-pricing)[Formatos de feed compatíveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#supported-feed-format)[Campos compatíveis – Classificados de imóveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#home-listing-fields)[Campos obrigatórios específicos do país – Somente para comércio](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#country_specific)[Parâmetros do objeto Image](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#image-object)[Parâmetros do objeto Address](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#address-object)[Configuração de preços e datas disponíveis](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#available_dates-object)[Deep links de produtos](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#deep-links-de-produtos)[Etapa 3: escolher opções de atualização](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#update-options)[Anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#an-ncios-de-cat-logo-advantage--2)[Comércio](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#com-rcio-2)[Etapa 4: filtrar o catálogo no conjunto de classificados](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#filter-to-home-listing-set)[Etapa 5: enviar conversões offline](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#send-offline-conversions)[Chaves de correspondência](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#chaves-de-correspond-ncia)[Dados personalizados](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#dados-personalizados)[Detalhes do evento](https://developers.facebook.com/docs/marketing-api/real-estate-ads/get-started#detalhes-do-evento) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7AcMjodL7IAUtF0w7ZhucZXgDodK54YSXAGsr1BmOsKplbb8C-75EA4J8bYQ_aem_Zik7mvYfO18QhL0MAvB7sA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7AcMjodL7IAUtF0w7ZhucZXgDodK54YSXAGsr1BmOsKplbb8C-75EA4J8bYQ_aem_Zik7mvYfO18QhL0MAvB7sA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-YutWv0E9-6oS0z8rxaZtKhfeV5Fwp93JUNgq2wKrJyQ31Du7O7OzjoIIrA_aem_pK_TOM5Y8JrKYasTOuXlZQ&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5IEH784bAbDcuHupz_kUWnwvKx7Y4VsLYR0Vw87vpz8UY4I-K01ghQdjKn5Q_aem_3ERan8-3-oM3gsfvp4iBhw&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR71ayyTVBquyiwSZSGmhgQwWyky52SdJ-VdJRINkEdJGNw-F6jivEVjF2Nxcw_aem_lxAw5HdJIIOpJOdlEz8yLA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ZvxdxzjYjuLBpyPOxT51oWn5JIpteo7ISo_qegV8wXiOiXoA1XtHdCvZ5zg_aem_qPO08QafY-GUYP5xzmIGUA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GAyHFM3RN8QzexLUm3V8ZrM_1c5YbxC-mcNC8l3SyKxOv4u3nsY4JZHfEYQ_aem_XkexLhRA5kRCTPbSMB819g&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7AcMjodL7IAUtF0w7ZhucZXgDodK54YSXAGsr1BmOsKplbb8C-75EA4J8bYQ_aem_Zik7mvYfO18QhL0MAvB7sA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR473WuzHHA3V6n4LdbgsOhlK_A9OgvNWHBuTq_Ldmg9E_T3d04PieClZyF4yQ_aem__glce8_KPYTQxSymFqYpVA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5IEH784bAbDcuHupz_kUWnwvKx7Y4VsLYR0Vw87vpz8UY4I-K01ghQdjKn5Q_aem_3ERan8-3-oM3gsfvp4iBhw&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4oijiXCM1ikW_Ar1QOUsvQ3NPdKISN8T0mYdvTGEpnzGw6eqzIYk9KV1funQ_aem_aPaf-eE5aeqzAfEbLVtaSQ&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GAyHFM3RN8QzexLUm3V8ZrM_1c5YbxC-mcNC8l3SyKxOv4u3nsY4JZHfEYQ_aem_XkexLhRA5kRCTPbSMB819g&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jPtQq9sblM3YnvqLpdvFB0gxqyv8JxJEJQFnrW5EhBv0uyjbuzSY22t5XzQ_aem_8VecsUgqPiFoK24L3eHSZw&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR473WuzHHA3V6n4LdbgsOhlK_A9OgvNWHBuTq_Ldmg9E_T3d04PieClZyF4yQ_aem__glce8_KPYTQxSymFqYpVA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GAyHFM3RN8QzexLUm3V8ZrM_1c5YbxC-mcNC8l3SyKxOv4u3nsY4JZHfEYQ_aem_XkexLhRA5kRCTPbSMB819g&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-YutWv0E9-6oS0z8rxaZtKhfeV5Fwp93JUNgq2wKrJyQ31Du7O7OzjoIIrA_aem_pK_TOM5Y8JrKYasTOuXlZQ&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jPtQq9sblM3YnvqLpdvFB0gxqyv8JxJEJQFnrW5EhBv0uyjbuzSY22t5XzQ_aem_8VecsUgqPiFoK24L3eHSZw&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7AcMjodL7IAUtF0w7ZhucZXgDodK54YSXAGsr1BmOsKplbb8C-75EA4J8bYQ_aem_Zik7mvYfO18QhL0MAvB7sA&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-YutWv0E9-6oS0z8rxaZtKhfeV5Fwp93JUNgq2wKrJyQ31Du7O7OzjoIIrA_aem_pK_TOM5Y8JrKYasTOuXlZQ&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5GAyHFM3RN8QzexLUm3V8ZrM_1c5YbxC-mcNC8l3SyKxOv4u3nsY4JZHfEYQ_aem_XkexLhRA5kRCTPbSMB819g&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5xlid5llUq04cteriJ2ZtxYGFqX8FUrvfXEzIPdlEsy-ASvQsFq1LEuJ-czEdie5Zgrk_Xv4wkxYnI6SgdqaqGv2mqse38mKCaxVeaLJxvJihGkB3tcW0ltE6zIcd5kJ_K0Ix1htyL4A4WIhP1-XiNSLM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão