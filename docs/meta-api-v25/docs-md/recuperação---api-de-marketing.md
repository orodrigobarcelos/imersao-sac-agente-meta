<!-- Fonte: Recuperação - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Como recuperar leads


É possível recuperar leads com [Webhooks](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks) ou [leitura em lote](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#bulk-read).


## Antes de começar


Para ler campos de anúncios específicos, como `ad_id` ou `campaign_id`, você precisará do seguinte:


- Um token de acesso do usuário ou da Página solicitado por alguém com permissão para anunciar na conta de anúncios e [na Página](https://developers.facebook.com/docs/pages/overview#tasks)
- A [Permissão `ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)
- A [permissão `pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_management)
- A [permissão `pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
- A [permissão `pages_manage_metadata`](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata) (caso você use webhooks)


Para recuperar todos os dados de lead e de nível de anúncio, você precisará do seguinte:


- Um token de acesso do usuário ou da Página solicitado por alguém com permissão para anunciar na conta de anúncios e [na Página](https://developers.facebook.com/docs/pages/overview#tasks)
- A [permissão `ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)
- A [permissão `leads_retrieval`](https://developers.facebook.com/docs/permissions/reference/leads_retrieval)
- A [Permissão `pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
- A [Permissão `pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_management)
- A [permissão `pages_manage_ads`](https://developers.facebook.com/docs/permissions/reference/pages_manage_ads)


**Observação:** caso o administrador da Página nunca tenha personalizado leads nem concedido permissão de acesso com o Gerenciador de Acesso a Leads, todos os administradores da Página terão permissão de acesso a leads. Um administrador básico da Página pode ou não ter permissão de acesso a leads. Isso depende dos administradores da empresa, que podem personalizar essa permissão.


## Limites de volume


O limite de volume é 200 x 24 multiplicado pelo número de leads criados nos últimos 90 dias para uma Página do Facebook. Caso você ultrapasse esse limite de chamadas em um período de 24 horas, sua solicitação retornará um erro.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)

## Filtrar por intervalo de datas


Envie uma solicitação `GET` ao ponto de extremidade `/ads/lead_gen/export_csv/` em que os formatos de data sejam registros de data e hora `POSIX` ou `UNIX`.

```
curl -i -X GET "https://www.facebook.com/ads/lead_gen/export_csv/
    ?id=<FORM_ID>
    &type=form
    &from_date=1482698431
    &to_date=1482784831"
```


#### Atenção


- Caso `from_date` não esteja definido ou seja um valor anterior ao horário de criação do formulário, esse horário será usado.
- Caso `to_date` não esteja definido ou seja posterior ao horário atual, usaremos esse horário.
- Em caso de uma entrada sem identificação do anúncio ou IDs de grupo de anúncio no TSV, as possíveis causas são as seguintes: - O lead foi gerado pelo alcance orgânico. Nesse caso, `is_organic` no TSV exibirá `1`. Caso contrário, o valor será `0`. - O lead pode ter sido enviado de uma prévia do anúncio. - A pessoa que está solicitando leads não tem privilégios de anunciante na conta de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)

## Webhooks


Obtenha atualizações em tempo real sobre anúncios de lead.


### Etapa 1: introdução


Consulte o [guia de introdução a Webhooks](https://developers.facebook.com/docs/graph-api/webhooks/getting-started) para configurar seu ponto de extremidade e webhook.


### Etapa 2: obter um token de acesso à Página de longa duração


Gere um único [token de Página de longa duração](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing/#get-a-long-lived-page-access-token) para continuar a buscar dados sem se preocupar com a expiração.


### Etapa 3: instalar o seu app na Página


Consulte o nosso [guia de Webhooks para Páginas](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-pages#install-app) e saiba como instalar o seu app em uma Página.


### Resposta do webhook


Quando você cria a geração de leads, seu app recebe a seguinte resposta de webhook:

```
array(
  "object" => "page",
  "entry" => array(
    "0" => array(
      "id" => 153125381133,
      "time" => 1438292065,
      "changes" => array(
        "0" => array(
          "field" => "leadgen",
          "value" => array(
            "leadgen_id" => 123123123123,
            "page_id" => 123123123,
            "form_id" => 12312312312,
            "adgroup_id" => 12312312312,
            "ad_id" => 12312312312,
            "created_time" => 1440120384
          )
        ),
        "1" => array(
          "field" => "leadgen",
          "value" => array(
            "leadgen_id" => 123123123124,
            "page_id" => 123123123,
            "form_id" => 12312312312,
            "adgroup_id" => 12312312312,
            "ad_id" => 12312312312,
            "created_time" => 1440120384
          )
        )
      )
    )
  )
)
```


Você pode usar `leadgen_id` para recuperar dados associados ao lead:

```
curl -X GET \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<LEAD_ID>
```


Se o processo for bem-sucedido, o app receberá a seguinte resposta:

```
{
  "created_time": "2015-02-28T08:49:14+0000",
  "id": "<LEAD_ID>",
  "ad_id": "<AD_ID>",
  "form_id": "<FORM_ID>",
  "field_data": [{
    "name": "car_make",
    "values": [
      "Honda"
    ]
  },
  {
    "name": "full_name",
    "values": [
      "Joe Example"
    ]
  },
  {
    "name": "email",
    "values": [
      "joe@example.com"
    ]
  },
  {
    "name": "selected_dealer",
    "values": [
      "99213450"
    ]
  }],
	...
}
```


### Saiba mais


- Para auxiliar a migração dos dados de anúncios de lead para as ferramentas de gestão de relacionamento do cliente (CRM, pelas iniciais em inglês), muitas delas fornecem atualizações em tempo real. Consulte as [integrações de CRM disponíveis](https://www.facebook.com/business/help/908902042493104?__mref=message_bubble).
- O ping para as atualizações em tempo real é estruturado da seguinte forma. Saiba mais sobre [atualizações em tempo real no blog](https://developers.facebook.com/ads/blog/post/2014/12/11/real-time-updates-for-page-conversions/).
- Em caso de sucesso, os pings em tempo real ocorrerão nos eventos com um atraso de no máximo alguns minutos. Veja [como solucionar problemas de integrações em tempo real](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/).


Veja um exemplo de implementação no nosso [repositório no GitHub](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Flead-ads-webhook-sample&h=AT7XLAQ5yr9btp5NEjv-4_5KjfO0Hqs5ZJ9fOybuC4nD7CurYmQeQydCIht0nLEwR0KVh9OXh5vJnlKXZmthXrWm4y573MSwEmmQS_yCW9z_z5Vjco15-60fzpWUi67MM7x4nxGEQFYmAchyimQhYqfUzXE).
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)

## Leitura em lote


A permissão `leads_retrieval` é necessária para ler os leads.


Há `leads` no grupo de anúncios e em nós do formulário. Isso retorna todos os dados associados aos respectivos objetos. Como é possível reutilizar um formulário em diversos anúncios, **ele pode conter muito mais leads do que um anúncio**.


Para fazer a leitura em lote por anúncio:

```
curl -X GET \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>/leads
```


Para fazer a leitura por formulário:

```
curl -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  -d 'fields=created_time,id,ad_id,form_id,field_data' \
  https://graph.facebook.com/<API_VERSION>/<FORM_ID>/leads
```


A resposta:

```
{
  "data": [
    {
      "created_time": "2018-02-28T08:49:14+0000",
      "id": "<LEAD_ID>",
      "ad_id": "<AD_ID>",
      "form_id": "<FORM_ID>",
      "field_data": [
        {
          "name": "car_make",
          "values": [
            "Honda"
          ]
        },
        {
          "name": "full_name",
          "values": [
            "Joe Example"
          ]
        },
        {
          "name": "email",
          "values": [
            "joe@example.com"
          ]
        },
      ],
      ...
    }
  ],
  "paging": {
    "cursors": {
      "before": "OTc2Nz3M8MTgyMzU1NDMy",
      "after": "OTcxNjcyOTg8ANTI4NzE4"
    }
  }
}
```


### Como ler um valor de pergunta do localizador de lojas


Uma pergunta do localizador de lojas não é diferente de nenhuma outra. Além disso, esse tipo de pergunta terá o ID do campo que será mapeado durante a criação do formulário. As perguntas do localizador de lojas serão enviadas de modo semelhante a outras perguntas. O valor informado virá do **número da loja** da localização selecionada.


Por exemplo, digamos que você tenha uma pergunta do localizador de lojas em que `selected_dealer` é o ID do campo. Para buscar os leads em lote, faça a seguinte chamada:

```
curl -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  -d 'fields=created_time,id,ad_id,form_id,field_data' \
  https://graph.facebook.com/<API_VERSION>/<FORM_ID>/leads
```


A resposta:

```
{
  "data": [
    {
      "created_time": "2018-02-28T08:49:14+0000",
      "id": "<LEAD_ID>",
      "ad_id": "<AD_ID>",
      "form_id": "<FORM_ID>",
      "field_data": [
        {
          "name": "car_make",
          "values": [
            "Honda"
          ]
        },
        {
          "name": "full_name",
          "values": [
            "Joe Example"
          ]
        },
        {
          "name": "email",
          "values": [
            "joe@example.com"
          ]
        },
        {
          "name": "selected_dealer",
          "values": [
            "99213450"
          ]
        }
      ],
      ...
    }
  ],
  "paging": {
    "cursors": {
      "before": "OTc2Nz3M8MTgyMzU1NDMy",
      "after": "OTcxNjcyOTg8ANTI4NzE4"
    }
  }
}
```


### Como ler respostas de avisos legais personalizados


`field_data` não contém as respostas às caixas de seleção opcionais de avisos legais personalizados que seriam marcadas pelo usuário. Use o campo `custom_disclaimer_responses` para recuperar as respostas.

```
curl -X GET \
"https://graph.facebook.com/<API_VERSION>/<LEADGEN_ID>?
fields=custom_disclaimer_responses"
```


Resposta:

```
{
  "custom_disclaimer_responses": [
    {
      "checkbox_key": "optional_1",
      "is_checked": "1"
    },
    {
      "checkbox_key": "optional_2",
      "is_checked": ""
    }
  ],
  "id": "1231231231"
}
```


### Como filtrar leads


O exemplo a seguir filtra leads com base em registros de data e hora. Os registros de data e hora devem estar no formato Unix.

```
curl -X GET \ -d 'filtering=[ { "field": "time_created", "operator": "GREATER_THAN", "value": 1761945743 } ]' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_ID>/leads
```


O `operator` tem um dos valores a seguir.


| Operador | Significado |
| --- | --- |
| LESS_THAN | Filtra valores menores que o registro de data e hora. |
| GREATER_THAN | Filtra valores maiores que o registro de data e hora. |
| GREATER_THAN_OR_EQUAL | Filtra valores maiores ou iguais ao registro de data e hora. |
|  |  |


### Geração de tokens


Caso o formulário tenha IDs de campos personalizados, os campos e valores especificados serão retornados.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)

## Recursos


- Plataforma do Marketplace: [Leads relacionados a veículos](https://developers.facebook.com/docs/marketplace/vehicles/retrieving-leads)
- Gerenciador de Acesso a Leads: consulte os artigos [Sobre o Gerenciador de Acesso a Leads](https://www.facebook.com/business/help/1440176552713521?id=735435806665862) e [Atribuir ou remover permissões no Gerenciador de Acesso a Leads](https://www.facebook.com/business/help/540596413257598?id=735435806665862) na Central de Ajuda.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#)Nesta Página[Como recuperar leads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#como-recuperar-leads)[Antes de começar](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#antes-de-come-ar)[Limites de volume](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#rate)[Filtrar por intervalo de datas](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#filtering)[Webhooks](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks)[Etapa 1: introdução](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#etapa-1--introdu--o)[Etapa 2: obter um token de acesso à Página de longa duração](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#etapa-2--obter-um-token-de-acesso---p-gina-de-longa-dura--o)[Etapa 3: instalar o seu app na Página](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#etapa-3--instalar-o-seu-app-na-p-gina)[Resposta do webhook](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#resposta-do-webhook)[Saiba mais](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#saiba-mais)[Leitura em lote](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#bulk-read)[Como ler um valor de pergunta do localizador de lojas](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#como-ler-um-valor-de-pergunta-do-localizador-de-lojas)[Como ler respostas de avisos legais personalizados](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#como-ler-respostas-de-avisos-legais-personalizados)[Como filtrar leads](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#como-filtrar-leads)[Geração de tokens](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#tokenization)[Recursos](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#recursos) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7p78DZAMuoIxaT27f0OkmgQzaGFXhu4BpODKEeXR1j3mKLYXeYxA0ZpkkIkw_aem_VNgU2YbRHtF2j__iSBYs3Q&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6zf3_OPFCKxN00dFb6yoTlFlaurfxmu22FJ06qHA-MS9DxkKxxYfe0F9civQ_aem_v-m_lDhTLsAxN0YRvL-iWA&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DzsolRHQR4bVx-F17zZSJquQKNSVHS7vsmbf0dtFqdegzt-OAfccp2dV8-g_aem_X79fTmPIawjPnEKMnuytcQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ZhBcgPeY-SYiAP7FGG9kM_Yp8tlecloo-wb4_juZDqFk3DcqxoUHvOJk04Q_aem_b41PjrLWoN8VMyKu9UV7sQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ZhBcgPeY-SYiAP7FGG9kM_Yp8tlecloo-wb4_juZDqFk3DcqxoUHvOJk04Q_aem_b41PjrLWoN8VMyKu9UV7sQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DzsolRHQR4bVx-F17zZSJquQKNSVHS7vsmbf0dtFqdegzt-OAfccp2dV8-g_aem_X79fTmPIawjPnEKMnuytcQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DzsolRHQR4bVx-F17zZSJquQKNSVHS7vsmbf0dtFqdegzt-OAfccp2dV8-g_aem_X79fTmPIawjPnEKMnuytcQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6DzsolRHQR4bVx-F17zZSJquQKNSVHS7vsmbf0dtFqdegzt-OAfccp2dV8-g_aem_X79fTmPIawjPnEKMnuytcQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5AwHq3J8G7cIUNsqTbZtLoG1Y5JwqCFq7hlnq4zmE1a9W7TNq5BbN1XXG1Cw_aem_jkvGGiv-ZPmKfcu-WgIFZA&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4U35Fb_esPCYsr4BxjS5CQ5iIdgztm-96YpgqIe12387OSeLIRT3mmo2ML7w_aem_iFQMhqgru93JvlgsSPFNTg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4U35Fb_esPCYsr4BxjS5CQ5iIdgztm-96YpgqIe12387OSeLIRT3mmo2ML7w_aem_iFQMhqgru93JvlgsSPFNTg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ZhBcgPeY-SYiAP7FGG9kM_Yp8tlecloo-wb4_juZDqFk3DcqxoUHvOJk04Q_aem_b41PjrLWoN8VMyKu9UV7sQ&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7p78DZAMuoIxaT27f0OkmgQzaGFXhu4BpODKEeXR1j3mKLYXeYxA0ZpkkIkw_aem_VNgU2YbRHtF2j__iSBYs3Q&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7UqrYq62HNWLlko5JFOl5atEmWaqYi5K3SgX8MqyWZQVOJP6qdiv7Oaqr1JA_aem_hNsnFCauHHz1ukwlGJEl1w&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ztDdchIalofqQDFtvLONXxZba6zzegxv6_FcBds4FM9a2u5vPl0404yxRXA_aem_ee2ouZHNKHuyrun-_HcbRg&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT51iMdcfrag6CKbTtLBKxJ6CpRjGmZ7KSqT5oyGgGF3HCOwlu10M6Qp6P_PtYDWa7EEJ4mAPjTXB_FqIZXs4ltitdUafd2NMgocjGS9LfpMffNJfxzdlo9N1qFPFS4HT43mEQP-6XUGIAKKQkCsjHW2Fjk)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão