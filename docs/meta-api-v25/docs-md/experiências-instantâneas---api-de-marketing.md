<!-- Fonte: Experiências instantâneas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/instant-experiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Experiências instantâneas


As experiências instantâneas são um destino de anúncios de tela cheia e pós-clique carregado quase instantaneamente em anúncios no Feed.


Se você identificar alguma menção de `canvas` na API, será uma referência às experiências instantâneas. Canvas era o nome anterior desse formato.


## Antes de começar


Para criar e gerenciar experiências instantâneas, você precisa do seguinte:


- A [permissão `pages_manage_ads`](https://developers.facebook.com/docs/permissions/reference/pages_manage_ads)
- A [permissão `pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)
- A [permissão `pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
- Capacidade de executar a [tarefa `ADVERTISE`](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) na Página


### Limitações


- Só é possível atualizar uma experiência instantânea não publicada.
- A API de Experiências Instantâneas está disponível para o Instagram de forma limitada.
- Os anúncios das experiências instantâneas não são compatíveis com o Facebook Stories.


## Criar


Para criar uma experiência instantânea, você precisa da identificação de uma Página do Facebook (`PAGE-ID`) e [elementos](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#elements) que queira incluir na experiência, como fotos, botões e texto.

```
curl \
  -F 'background_color=FFFFFF' \
  -F 'body_element_ids=["<CANVAS_PHOTO_ID>"]' \
  -F 'is_hidden=' \
  -F 'is_published=' \
  -F 'name=Canvas Name' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/canvases
```


### Elementos


| Nome | Descrição |
| --- | --- |
| Botão | Um botão dentro da experiência instantânea. O campo button_style é obrigatório. |
| Carrossel | Um carrossel para a experiência instantânea. |
| Rodapé | Um rodapé para a experiência instantânea. |
| Cabeçalho | Um cabeçalho para a experiência instantânea. |
| Foto | Uma foto dentro da experiência instantânea. Forneça a PHOTO-ID de uma foto carregada em uma Página do Facebook . |
| Lista de produtos | Uma lista de produtos para uma experiência instantânea. |
| Conjunto de produtos | O conjunto de produtos de um catálogo de produtos de anúncios de catálogo Advantage+ exibidos em uma experiência instantânea. |
| Localizador de lojas | Um localizador de lojas dentro da experiência instantânea. |
| Texto | O texto e o estilo exibidos dentro da experiência instantânea. |
| Vídeo | Um vídeo dentro da experiência instantânea. Forneça a VIDEO-ID de um vídeo carregado em uma Página do Facebook . |


#### Excluir um elemento


Para fazer a exclusão, envie uma solicitação `DELETE` com a identificação do elemento a ser removido.

```
curl -X DELETE \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CANVAS_ELEMENT_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Obter experiências instantâneas existentes


Para obter informações sobre uma experiência instantânea, você precisa da identificação dela (`CANVAS-ID`).

```
curl -G \
  --data-urlencode 'fields=[
    "body_elements",
    "canvas_link",
    "id",
    "is_hidden",
    "is_published",
    "name"
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CANVAS_ID>
```


### Obter todas as experiências instantâneas de uma Página


Para obter informações sobre todas as experiências instantâneas existentes de uma Página do Facebook, você precisa da identificação da Página (`PAGE-ID`).

```
curl -G \
  --data-urlencode 'fields=[
    "background_color",
    "body_elements",
    "canvas_link",
    "id",
    "is_hidden",
    "is_published",
    "last_editor",
    "name",
    "owner",
    "update_time"
  ]' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<PAGE_ID>/canvases
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Atualizar uma experiência instantânea


Não é possível atualizar uma experiência instantânea já publicada. Além disso, você precisa da identificação correspondente (`CANVAS-ID`) e dos IDs dos elementos para atualização.

```
curl \
  -F 'background_color=FFFFFF' \
  -F 'body_element_ids=["<CANVAS_PHOTO_ID>"]' \
  -F 'is_hidden=' \
  -F 'is_published=' \
  -F 'name=Canvas Name' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CANVAS_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Usar um modelo


É possível usar um modelo como forma rápida de criar uma experiência instantânea para uma meta de negócios específica. O layout de cada modelo é fixo. No entanto, você pode substituir o conteúdo-padrão por imagens, vídeos, produtos, texto e links próprios.


| Nome do modelo da API | ID do modelo | Descrição |
| --- | --- | --- |
| Obter novos clientes | 133471657203838 | Gere conversões com uma página de destino para celular que incentiva a ação. Modelo de aquisição de cliente no Gerenciador de Anúncios. |
| Apresentar sua empresa | 1063217037112304 | Ofereça às pessoas uma maneira envolvente de conhecer melhor sua marca, seu produto ou seu serviço. Modelo de narrativa no Gerenciador de Anúncios. |
| Vender produtos (sem catálogo) | 424787857903852 | Crie uma experiência de compras em dispositivos móveis ao carregar as informações de produto em vez de usar um catálogo. Modelo de venda de produtos (sem catálogo) no Gerenciador de Anúncios. |
| Vender produtos: layout de estilo de vida | 1369752616394017 | Destaque seus produtos em fotos para que as pessoas os explorem na prática. Modelo de lookbook no Gerenciador de Anúncios. |
| Vender produtos: layout de grade | 1932289657009030 | Use seu catálogo de produtos para criar uma experiência que permita às pessoas comprarem diretamente no dispositivo móvel. Modelo de vitrine no Gerenciador de Anúncios. |
| Experiência de AR |  | O modelo de experiência de AR está disponível apenas via Gerenciador de Anúncios. |


### Obter tipos de elemento de um modelo


#### Etapa 1. obter as informações de documento do modelo


Envie uma solicitação `GET` para identificar os elementos necessários a um modelo específico (no exemplo a seguir, **Obter novos clientes**).

```
curl -i -X GET \
 "https://graph.facebook.com/VERSION/133471657203838?fields=document&access_token=ACCESS-TOKEN"
```


#### Exemplo de resposta


```
{
  "document": {
    "name": "Get New Customers",
    "id": "397246414010297"
  },
  "id": "133471657203838"
}
```


#### Etapa 2. obter os tipos de elemento


Use a identificação do campo `document` para obter os elementos disponíveis a um modelo específico.

```
curl -i -X GET \
 "https://graph.facebook.com/VERSION/397246414010297?fields=body_elements&access_token=ACCESS-TOKEN"
```


A lista retornada exibe tipos de elementos disponíveis para uso no modelo **Obter novos clientes**.

```
{
  "body_elements": [
    {
      "name": "Cover Image or Video",
      "element_type": "PHOTO",
      "id": "397271930674412"
    },
    {
      "name": "Text",
      "element_type": "RICH_TEXT",
      "id": "397271920674413"
    },
    {
      "name": "Text",
      "element_type": "RICH_TEXT",
      "id": "397271910674414"
    },
    {
      "name": "Button",
      "element_type": "BUTTON",
      "id": "397271914007747"
    },
    {
      "name": "Carousel",
      "element_type": "CAROUSEL",
      "id": "397271940674411"
    },
    {
      "name": "Text",
      "element_type": "RICH_TEXT",
      "id": "397271917341080"
    },
    {
      "name": "Button",
      "element_type": "BUTTON",
      "id": "397271924007746"
    }
  ],
  "id": "397246414010297"
}
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Publicar


Para publicar seu anúncio de experiência instantânea, envie uma solicitação `POST` à identificação da experiência (`CANVAS-ID`) e defina o campo `is_published` como `true`.

```
curl \
  -F 'is_published=1' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CANVAS_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Gerar um criativo do anúncio


Use o link de uma experiência instantânea existente (`CANVAS-LINK`) para gerar um criativo do anúncio.

```
curl -X POST \
  -F 'image_hash="<IMAGE_HASH>"' \
  -F 'object_story_spec={
       "page_id": "<PAGE_ID>",
       "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<CANVAS_LINK>",
         "name": "Creative message",
         "call_to_action": {
           "type": "LEARN_MORE"
         }
       }
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Assim que o criativo do anúncio estiver pronto, você poderá criar o grupo, o conjunto e a campanha de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Diálogo de anúncios das experiências instantâneas


Use o *diálogo de anúncios de experiências instantâneas* para fornecer as interfaces do usuário para a criação de anúncios de experiências instantâneas do Facebook no seu site. Para mais detalhes sobre o componente de interface do usuário, consulte [Diálogos](https://developers.facebook.com/docs/javascript/reference/FB.ui).


Para configurar o SDK do Facebook para JavaScript, consulte:


- [Guia de início rápido](https://developers.facebook.com/docs/javascript/quickstart)
- [Referência de inicialização](https://developers.facebook.com/docs/javascript/reference/FB.init/)


O SDK para JavaScript depende das permissões do usuário conectado para criar uma experiência instantânea. Se o usuário não tiver as permissões necessárias para criar uma experiência instantânea para a página e a empresa fornecidas, o diálogo exibirá um erro. Para garantir que não ocorram erros, o usuário deve estar na empresa e ter permissões de "criar anúncios" para a página.


Em seguida, acione o diálogo:

```
FB.ui({
  display: 'popup',
  method: 'instant_experiences_builder',
  business_id: '<BUSINESS_ID>',
  page_id: '<PAGE_ID>'
}, function(response) {
  // callback
});
```


É possível fornecer as seguintes configurações para o plugin:


| Nome | Obrigatório | Descrição |
| --- | --- | --- |
| display | Sim | Parâmetro necessário com valor definido de popup . |
| method | Sim | Parâmetro necessário com valor definido de instant_experiences_builder . |
| business_id | Sim | A identificação da empresa. |
| page_id | Sim | A identificação da página a que você deseja associar a experiência instantânea. |
| canvas_id | Não | ID da experiência instantânea que você deseja editar. |


O parâmetro `canvas_id` é opcional e permite que um usuário edite ou visualize uma experiência instantânea existente. **Não** será possível editar experiências instantâneas concluídas. Para visualizar uma experiência instantânea, recomendamos usar o diálogo de experiências instantâneas.


O plugin retorna a seguinte resposta em caso de sucesso:

```
{
  "success": true,
  "id": "CANVAS-ID"
}
```


A identificação retornada é uma experiência instantânea publicada. Você pode usá-la em campanhas de anúncios. Se nenhuma resposta ou uma resposta `undefined` for retornada, isso será uma indicação de que o usuário fechou o diálogo antes de concluir a experiência instantânea. O usuário pode ter salvado a experiência instantânea, mas não a concluiu. Você pode extrair todas as experiências instantâneas pertencentes a uma página por meio da Graph API. Dessa forma, é possível verificar se há experiências inacabadas.
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Ver prévia da experiência instantânea


### API de Prévia do Iframe


Você pode gerar a visualização de uma experiência instantânea fazendo uma chamada da API de prévia que retorna um iframe (assim como na API de prévia do anúncio):

```
curl -X GET \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v18.0/<CANVAS_ID>/preview
```


A API retorna algo semelhante a isto, que pode ser visualizado incorporando o elemento iframe retornado em HTML:

```
{
"data": [
    {
      "body": "<iframe src=\"https://www.facebook.com/ads/canvas/preview?d=AQKELApdJxoVp2f3PHl8-pRtYuAh4-_eDupMDbh-pS9zde_EFxckhYQCXu7NYUi4PhhBA7uskIo2Ys3IjIVNGZiS&t=AQKGOPqGI-NWcv1YKbA\" width=\"405\" height=\"720\" scrolling=\"yes\" style=\"border: none;\"></iframe>"
    }
  ],
  "__www_request_id__": "AQnyr47Qp2r5M-ISqSiMgrw"
}
```


### SDK do Facebook


Você pode usar esse diálogo para fornecer a um usuário do Facebook a prévia de uma experiência instantânea no seu site. Para mais detalhes sobre o componente de interface do usuário, consulte [Diálogos](https://developers.facebook.com/docs/javascript/reference/FB.ui).


Para configurar o SDK do Facebook para JavaScript, consulte:


- [Guia de início rápido](https://developers.facebook.com/docs/javascript/quickstart)
- [Referência de inicialização](https://developers.facebook.com/docs/javascript/reference/FB.init/)


O SDK para JavaScript depende das permissões do usuário conectado para criar uma Experiência Instantânea. Se o usuário não tiver as permissões necessárias para visualizar a experiência instantânea, o diálogo exibirá um erro.


Depois, acione o diálogo de prévia:

```
FB.ui({
  display: 'popup',
  method: 'instant_experiences_preview',
  canvas_id: 'CANVAS-ID'
});
```


É possível fornecer as seguintes configurações para o plugin:


| Nome | Obrigatório | Descrição |
| --- | --- | --- |
| display | Sim | Parâmetro necessário com valor definido de popup . |
| method | Sim | Parâmetro necessário com valor definido de instant_experiences_preview . |
| canvas_id | Sim | ID da experiência instantânea que você deseja visualizar. |

[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Criar públicos para experiências instantâneas


Para criar um público de engajamento, isto é, um público de pessoas que interagiram com uma experiência instantânea, defina o parâmetro `object_id` do campo `rule` como a identificação da experiência instantânea (`CANVAS-ID`) na sua chamada `POST /act_AD-ACCOUNT/customaudiences`.


**Pessoas que abriram a experiência instantânea**

```
curl \
  -F 'name=Instant Experience Engagement Audience' \
  -F 'description=People who opened this Instant Experience' \
  -F 'rule=[{"object_id":"<CANVAS_ID>","event_name":"instant_shopping_document_open"}]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/customaudiences
```


**Pessoas que clicaram em qualquer link na experiência instantânea**

```
curl \
  -F 'name=Instant Experience Engagement Audience' \
  -F 'description=People who clicked any links in this Instant Experience' \
  -F 'rule=[{"object_id":"<CANVAS_ID>","event_name":"instant_shopping_element_click"}]' \
  -F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/act_<AD_ACCOUNT_ID>/customaudiences
```


Para obter mais informações sobre Públicos Personalizados, consulte a [referência Público Personalizado](https://developers.facebook.com/docs/marketing-api/reference/custom-audience).
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Experiências instantâneas e anúncios do Instagram


A implementação de anúncios de experiências instantâneas com o Instagram usa as mesmas chamadas de API utilizadas para esse tipo de anúncio no Facebook. **Observe que há limitações quando você usa o Instagram e as experiências instantâneas**:


- **Posicionamento** – disponível para o Feed do Instagram e o Instagram Stories. Se selecionar o Instagram Stories, você deverá escolhê-lo como posicionamento de anúncios exclusivo.
- **Elementos da experiência instantânea** – totalmente compatíveis com cabeçalhos e conjuntos de produtos.


Oferecemos suporte **parcial** a estes elementos da experiência instantânea no Instagram:


- **Rodapé** – sem `swipe to open` em clientes, será renderizado como `Tap to open`.
- **Carrossel** – sem foto que vincule a outra experiência instantânea; no cliente aparece como um link não clicável. Para fotos e vídeos, sem ajustar à altura e à largura nem inclinar para fazer uma panorâmica; será renderizado como ajustar à largura.
- **Botão** – não é possível vincular a outra experiência instantânea ou à App Store.
- **Texto** – sem suporte à linguagem RTL.
- **Vídeo** – sem vídeo 360.
- **Localizador de lojas** – não é compatível.
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Insights sobre Anúncios


Confira os [Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/) para obter uma visão geral e descrições das métricas disponíveis.
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)

## Veja também


- Guia de anúncios do Facebook: [Especificações de experiências instantâneas](https://www.facebook.com/business/ads-guide/instant-experience)
- Central de Ajuda para Empresas: [Saiba mais sobre as experiências instantâneas](https://www.facebook.com/business/help/183469315334462?id=1633489293397055)
[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)[○](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#)Nesta Página[Experiências instantâneas](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#experi-ncias-instant-neas)[Antes de começar](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#antes-de-come-ar)[Limitações](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#limita--es)[Criar](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#criar)[Elementos](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#elementos)[Obter experiências instantâneas existentes](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#obter-experi-ncias-instant-neas-existentes)[Obter todas as experiências instantâneas de uma Página](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#obter-todas-as-experi-ncias-instant-neas-de-uma-p-gina)[Atualizar uma experiência instantânea](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#atualizar-uma-experi-ncia-instant-nea)[Usar um modelo](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#templates)[Obter tipos de elemento de um modelo](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#obter-tipos-de-elemento-de-um-modelo)[Publicar](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#publish)[Gerar um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#gerar-um-criativo-do-an-ncio)[Diálogo de anúncios das experiências instantâneas](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#canvas-ads-dialog)[Ver prévia da experiência instantânea](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#ver-pr-via-da-experi-ncia-instant-nea)[API de Prévia do Iframe](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#api-de-pr-via-do-iframe)[SDK do Facebook](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#sdk-do-facebook)[Criar públicos para experiências instantâneas](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#criar-p-blicos-para-experi-ncias-instant-neas)[Experiências instantâneas e anúncios do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#experi-ncias-instant-neas-e-an-ncios-do-instagram)[Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#insights)[Veja também](https://developers.facebook.com/docs/marketing-api/guides/instant-experiences#veja-tamb-m) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72hrxb1ItHlXF951ogwxaawzrxJiP81xwCzawcP-0F1tjmQOEckb_UkrV_cg_aem_Q1aTFuZNQswkBb9641cGDg&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6syIiZEwaXMPJB6A-poqYScUd3L_G7Cg937ezSl5K4ZdG11xITXqWxO8f49w_aem_wpBacYGITDSq8n9ZJVSjvQ&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7VRirGIyrhYXhH40bJty8T8odbo4F7a2qIRlO6y7SZunTliUFBmZJDgn_kRg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7VRirGIyrhYXhH40bJty8T8odbo4F7a2qIRlO6y7SZunTliUFBmZJDgn_kRg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4s-7kfVI2jOiNOn_YXhVAQuFGr-pEaxO-JId3PeGOK5h17JA6878_CxZ5X7Q_aem_qck_LN3DvEiKucBkO877-A&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IHRkvjAD9oFjmQdQLVrrll1BXeS7YfkstSCYWHb_i3soY41RmY2T2yR0cPg_aem_w0PzvE2bGkispZgVo9D8fA&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72hrxb1ItHlXF951ogwxaawzrxJiP81xwCzawcP-0F1tjmQOEckb_UkrV_cg_aem_Q1aTFuZNQswkBb9641cGDg&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4NdD4-StG35alnYyi8HlB62EVk9iaFv9V48PUdox_B2oJdrzHkIrxwIjniPA_aem_359qBrR414zdSGEjmPk8sw&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ukzAoc09h6tbzkoIEj00lh81lxwJblmBwPEA5ScUBGKXW_YAILsIS9QZZ5w_aem_D5j78nWWmpE_cBgo-gcC4Q&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ukzAoc09h6tbzkoIEj00lh81lxwJblmBwPEA5ScUBGKXW_YAILsIS9QZZ5w_aem_D5j78nWWmpE_cBgo-gcC4Q&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IHRkvjAD9oFjmQdQLVrrll1BXeS7YfkstSCYWHb_i3soY41RmY2T2yR0cPg_aem_w0PzvE2bGkispZgVo9D8fA&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6N-FMA_3sZA_MrbnAHRUOc51EEna73_nRqeAlyHAFltllvKLJqN4AWxXCrlw_aem_hoiLUwsZpdiRdAuqp-4rDg&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7k-eMMOwSedpiz0SBkt43X-NI-XJPrrrObd3msHcXTwwSNIsEze5nH48tEGQ_aem_wW7-TvCcwO5cvubjjORWIQ&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6N-FMA_3sZA_MrbnAHRUOc51EEna73_nRqeAlyHAFltllvKLJqN4AWxXCrlw_aem_hoiLUwsZpdiRdAuqp-4rDg&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6syIiZEwaXMPJB6A-poqYScUd3L_G7Cg937ezSl5K4ZdG11xITXqWxO8f49w_aem_wpBacYGITDSq8n9ZJVSjvQ&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7VRirGIyrhYXhH40bJty8T8odbo4F7a2qIRlO6y7SZunTliUFBmZJDgn_kRg_aem_ZmFrZWR1bW15MTZieXRlcw&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7k-eMMOwSedpiz0SBkt43X-NI-XJPrrrObd3msHcXTwwSNIsEze5nH48tEGQ_aem_wW7-TvCcwO5cvubjjORWIQ&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72hrxb1ItHlXF951ogwxaawzrxJiP81xwCzawcP-0F1tjmQOEckb_UkrV_cg_aem_Q1aTFuZNQswkBb9641cGDg&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ure0XaaMaTkaG3Hp8nPm4W6sonyFFiYd2TSccO1ZKEaY6-C_Y3I0QwnmXmQ_aem_nwtOE6OOr2XBdgiWxeVuLA&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ure0XaaMaTkaG3Hp8nPm4W6sonyFFiYd2TSccO1ZKEaY6-C_Y3I0QwnmXmQ_aem_nwtOE6OOr2XBdgiWxeVuLA&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6GVpgfuH0iNIhwE_qEOASW3pQvp9x39nmkNdsCqr4DGQk22wdgCASXgBP1zIP9p0GvvacOd5OLtXO97ZsSKJvK2Fh4Rml2YmcgAXd5nZQZZsksy-9atXbh477oy8J4miRwhK-ciMM_iqAKz633jVg9TLc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão