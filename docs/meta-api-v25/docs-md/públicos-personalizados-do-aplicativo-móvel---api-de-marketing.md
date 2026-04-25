<!-- Fonte: Públicos Personalizados do aplicativo móvel - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Públicos Personalizados do aplicativo para celular


Crie públicos com base nas ações das pessoas em seu aplicativo que atendem a seus critérios. Este recurso permite a criação de públicos com base em diferentes critérios. Por exemplo:


- “Passou do nível 8 nos últimos 10 dias”
- “Usou o aplicativo nos últimos 8 dias, mas ainda não fez uma compra”
- “Adicionou um produto ao carrinho, mas não finalizou a compra”


Esta solução usa eventos com nome registrado por meio dos [SDKs do Facebook](https://developers.facebook.com/docs/app-ads/sdk), da [API de Eventos do Aplicativo](https://developers.facebook.com/docs/app-events/) ou dos [Mobile Measurement Partners](https://developers.facebook.com/docs/app-ads/measuring/measurement-partners). Exemplos de eventos a serem registrados incluem “Instalou", “Adicionou ao carrinho", “Comprou" ou “Atingiu um nível”.


### Limitações


- O `subtype` para públicos personalizados de engajamento só tem compatibilidade com vídeo.
- Os Públicos Personalizados do aplicativo para celular de direcionamento de inclusão não têm mais compatibilidade com o ponto de extremidade `POST /{ad-account-id}/adsets` das campanhas da SKAdNetwork para o iOS 14.5.
- Novas campanhas de instalação do aplicativo para o iOS 14.5 não poderão mais usar o direcionamento de conexões do aplicativo.


## Criar um público


Para criar Públicos Personalizados do seu aplicativo para celular, a conta de anúncios precisa aceitar os [Termos de Serviço para Públicos Personalizados](https://www.facebook.com/ads/manage/customaudiences/tos.php) em [Gerenciador de Anúncios](https://business.facebook.com/adsmanager/manage). Veja os requisitos necessários para assinar os termos:


- Você precisa ser um usuário Administrador, Desenvolvedor ou de Informações para a conta de anúncios.
- A conta de anúncios deve estar listada como tal nas [configurações do seu aplicativo](https://developers.facebook.com/apps).


Para criar seu público:

```
curl -X POST \ -F 'name="My Test Website Custom Audience"' \ -F 'rule={ "inclusions": { "operator": "or", "rules": [ { "event_sources": [ { "id": "<APP_ID>", "type": "app" } ], "retention_seconds": 8400, "filter": { "operator": "and", "filters": [ { "field": "event", "operator": "eq", "value": "fb_mobile_purchase" } ] } } ] } }' \ -F 'prefill=1' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/customaudiences
```


Exibe o `id` do público em caso de sucesso. Estes parâmetros são os mais relevantes:


| Nome | Descrição |
| --- | --- |
| name tipo: Cadeia de caracteres | Obrigatório. Nome do Público Personalizado. |
| description tipo: Cadeia de caracteres | Opcional. Descrição do público personalizado. |
| rule tipo: objeto JSON | Opcional. Regra para definir o público. Consulte Regras de público . |


Cada conta de anúncios pode criar no máximo `200` Públicos Personalizados a partir do aplicativo para celular. Faça uma solicitação `POST` para:

```
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/customaudiences
```


Use estes campos:


| Nome | Descrição |
| --- | --- |
| name tipo: cadeia de caracteres | Obrigatório. O nome do seu Público Personalizado. |
| retention_days tipo: número inteiro | Obrigatório. Há quanto tempo alguém está nesse público. O número mínimo é 1 . O número máximo é 180 . Se retention_days for definido como 14 e, no 13º dia, um membro do público acionar um evento do aplicativo que atenda aos seus critérios, o Facebook ampliará o tempo no público por mais 14 dias. Alguém está no público N dias desde que o último evento correspondente foi acionado. |
| rule tipo: objeto JSON | Obrigatório. Regras para definir o público. Consulte Regras de público . |

[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)

## Regras de público


Para determinar quem é adicionado ao Público Personalizado, defina uma regra com base em eventos em seu aplicativo. Uma regra é um objeto JSON com pares de valores chave e pode fazer referência a vários eventos do aplicativo. Você pode definir a regra com base em eventos específicos e seus parâmetros e também em agregação. Consulte [Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules) para saber mais. Veja também:


- [Sintaxe das regras de público](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#audience-rules-syntax)
- [Sintaxe do conjunto de regras](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#rule_set_syntax)
- [Sintaxe da regra de inclusão e exclusão](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#inclusion-exclusion): em `event_sources`, defina `id` como o ID do seu aplicativo e `type` como `app`.
- [Filtros](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#filter)
- [Regras de filtro](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#filter-rules): - Use `'event'` como `field` se o filtro especificar um evento. Os parâmetros que correspondem a Eventos do aplicativo enviados pelo aplicativo (por exemplo, "_appVersion", "_value” e assim por diante). - Se o atributo `field` for definido como `"event"`, o valor deverá ser configurado como um nome de evento. Use a API de Evento do Aplicativo para ver os eventos do aplicativo e parâmetros relatados pelo pixel.
- [Funções de agregação](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules#aggregate): as funções de agregação `"count"`, `"sum"`, `"avg"`, `"min"` e `"max"` estão disponíveis para os Públicos Personalizados do aplicativo para celular.


### Exemplo das regras de Público Personalizado do aplicativo para celular


#### Exemplo de evento padrão


Todas as pessoas que fizeram uma compra no aplicativo para celular nos últimos 30 dias para o ID `55064006` do aplicativo:

```
{
    "inclusions: {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app"
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "fb_mobile_purchase"
                        }
                    ]
                }
            }
        ]
    }
}
```


#### Evento personalizado com exemplo de parâmetros


Todos os usuários que reverteram eventos `“timeOnPanel”` personalizados nos últimos 30 dias para o ID `55064006` do aplicativo:

```
{
    "inclusions: {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app"
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "timeOnPanel"
                        }
                    ]
                }
            }
        ]
    }
}
```


Todos os usuários que reverteram eventos `“timeOnPanel”` personalizados em que o valor do evento é maior que 30, a cor é `“red”` ou `“blue”` e que têm `“banana”` como sobremesa favorita:

```
{
    "inclusions: {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app",
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "timeOnPanel",
                        },
                        {
                            "field": "_value",
                            "operator": ">",
                            "value": 30,
                        },
                        {
                            "field": "color",
                            "operator": "is_any",
                            "value": ["red", "blue"],
                        },
                        {
                            "field": "favoriteDessert",
                            "operator": "contains",
                            "value": "banana",
                        }
                    ]
                }
            }
        ]
    }
}
```


#### Exemplo de agregação


Compradores 20% melhores com base nas compras nos últimos 30 dias:

```
{
    "inclusions: {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app"
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "fb_mobile_purchase"
                        }
                    ]
                }
                "aggregation": {
                    "type": "count",
                    "method": "percentile",
                    "operator": "in_range",
                    "from": 75,
                    "to": 100,
                }
            }
        ]
    }
}
```


#### Exemplo de exclusão


O exemplo a seguir inclui pessoas que adicionaram produtos ao carrinho, mas não finalizaram a compra:

```
{
    "inclusions: {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app"
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "add_to_cart"
                        }
                    ]
                }
            }
        ]
    },
    "exclusions": {
        "operator": "or",
        "rules": [
            {
                "event_sources": [
                    {
                        "id": 55064006,
                        "type": "app"
                    }
                ],
                "retention_seconds: 2592000,
                "filter": {
                    "operator": "and",
                    "filters": [
                        {
                            "field": "event",
                            "operator": "=",
                            "value": "fb_mobile_purchase"
                        }
                    ]
                }
            }
        ]
    }
}
```
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)

## API de Eventos do App


Consulte quais eventos do aplicativo e parâmetros um aplicativo relatou ao Facebook. Você pode usar esses eventos e parâmetros para [criar Públicos Personalizados](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#create) de forma direta. Você precisa de um token de acesso associado ao `app_id` com uma função de administrador, desenvolvedor ou anunciante.


Faça uma solicitação `GET`:

```
https://graph.facebook.com/<API_VERSION>/<APP_ID>/app_event_types
```


A resposta é JSON contendo uma matriz `data` dos dicionários JSON com estes campos:


| Nome | Descrição |
| --- | --- |
| event_name tipo: cadeia de caracteres | Tipo de evento do aplicativo para uso na regra . |
| display_name tipo: cadeia de caracteres | Nome legível do tipo de evento |
| description tipo: cadeia de caracteres | Descrição detalhada do evento padrão |
| parameters tipo: matriz | Matriz de dicionários JSON descrevendo parâmetros desse evento { "parameter_name": "fb_currency", "display_name": "Currency", "description": "Currency for event" } parameter_name : cadeia de caracteres, tipo de parâmetro do aplicativo para uso na regra . display_name : cadeia de caracteres, nome legível do tipo de evento. description : cadeia de caracteres, descrição detalhada do parâmetro, caso ele seja padrão. |


[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)

## Como gerenciar públicos


- Para obter informações sobre públicos, consulte [Público Personalizado, Leitura](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/#read).
- Para atualizar, consulte [Público Personalizado, Atualização](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/#update).
- Para excluir, consulte [Público Personalizado, Exclusão](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/#delete).
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)

## Recursos


- [Aplicativos iOS, Redirecionamento com Eventos do Aplicativo](https://developers.facebook.com/docs/ios/app-events) – retome a interação dos usuários com seu aplicativo iOS.
- [Aplicativos Android, Redirecionamento com Eventos do Aplicativo](https://developers.facebook.com/docs/android/app-events) – redirecione anúncios no seu aplicativo Android.
- [Direcionamento do Público Personalizado](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting/)
- [Direcionamento de semelhantes](https://developers.facebook.com/docs/reference/ads-api/lookalike-audience-targeting)
- [Referência, Especificações de direcionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/)
- [Referência, Anúncios de aplicativo para celular para engajamento](https://developers.facebook.com/docs/reference/ads-api/mobile-app-ads-engagement/)
[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)[○](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#)Nesta Página[Públicos Personalizados do aplicativo para celular](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#p-blicos-personalizados-do-aplicativo-para-celular)[Criar um público](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#create)[Regras de público](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#rules)[Exemplo das regras de Público Personalizado do aplicativo para celular](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#example_rules)[API de Eventos do App](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#app_events_api)[Como gerenciar públicos](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#read)[Recursos](https://developers.facebook.com/docs/marketing-api/audiences/guides/mobile-app-custom-audiences#resources) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HgUVZQUNiZazM6J-sxyNS_UlJVzO0fVuUGKlmpq4nu_sFzdLyqPlVVuXgEQ_aem_DLsgCDYyrUuH551qiIsvrQ&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HgUVZQUNiZazM6J-sxyNS_UlJVzO0fVuUGKlmpq4nu_sFzdLyqPlVVuXgEQ_aem_DLsgCDYyrUuH551qiIsvrQ&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7BQQnTzhWnj3pUmCek2PcEGJ5xRtfTJ3_uiun1Czx012JjCkuleUlMg8D9Wg_aem_D9lUHisIHyN7lgN93ZskAA&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ai5Iihv4NATfE7G0urNKtu-DMsvwlazRXYOv24mYIxussXeEpjGFbEviCHg_aem_GhKKTqY_gfuwXVEZBn7RGw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xUzmvTNr38Iv5aEUb5vi-Xcpf0-PrhkA-xpB0HQ969tRW1o3IDUhRLrl08g_aem_kCnqDCqDgkxfYvNgFVXNhg&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xUzmvTNr38Iv5aEUb5vi-Xcpf0-PrhkA-xpB0HQ969tRW1o3IDUhRLrl08g_aem_kCnqDCqDgkxfYvNgFVXNhg&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR648ZqpEEoq5YgVqobcTXOfdTLPHPDXkAbcNNOI6oAtJf0yOgswF8rVzYkFPg_aem_c1BVhYtFLAFR_SHRSqX1ug&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR747rbCg3t1lZichT-3tdcg6ckgsuB8Wju5C-lMFGm_R2jm4OGFmnWPgOAL1Q_aem_eOnLXHzaNMswefwXElpwRw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IKZxPCUNkHIVhvzblkNpGE9JDsF4b41jcIs-zdOG9Be25pyn_QQQ-HZqbtg_aem_EPvbrymigiOgipdusX1aBg&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HgUVZQUNiZazM6J-sxyNS_UlJVzO0fVuUGKlmpq4nu_sFzdLyqPlVVuXgEQ_aem_DLsgCDYyrUuH551qiIsvrQ&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HgUVZQUNiZazM6J-sxyNS_UlJVzO0fVuUGKlmpq4nu_sFzdLyqPlVVuXgEQ_aem_DLsgCDYyrUuH551qiIsvrQ&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR648ZqpEEoq5YgVqobcTXOfdTLPHPDXkAbcNNOI6oAtJf0yOgswF8rVzYkFPg_aem_c1BVhYtFLAFR_SHRSqX1ug&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7xUzmvTNr38Iv5aEUb5vi-Xcpf0-PrhkA-xpB0HQ969tRW1o3IDUhRLrl08g_aem_kCnqDCqDgkxfYvNgFVXNhg&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7IKZxPCUNkHIVhvzblkNpGE9JDsF4b41jcIs-zdOG9Be25pyn_QQQ-HZqbtg_aem_EPvbrymigiOgipdusX1aBg&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR747rbCg3t1lZichT-3tdcg6ckgsuB8Wju5C-lMFGm_R2jm4OGFmnWPgOAL1Q_aem_eOnLXHzaNMswefwXElpwRw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7K_d7jjGgY-bFKgyBtVlrNIogWoA7k97azL9rpIF0SP5sFIR9PoNG1BlC3Sw_aem_NunrsZLjmiNpDmuymR9eOw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ai5Iihv4NATfE7G0urNKtu-DMsvwlazRXYOv24mYIxussXeEpjGFbEviCHg_aem_GhKKTqY_gfuwXVEZBn7RGw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR648ZqpEEoq5YgVqobcTXOfdTLPHPDXkAbcNNOI6oAtJf0yOgswF8rVzYkFPg_aem_c1BVhYtFLAFR_SHRSqX1ug&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7K_d7jjGgY-bFKgyBtVlrNIogWoA7k97azL9rpIF0SP5sFIR9PoNG1BlC3Sw_aem_NunrsZLjmiNpDmuymR9eOw&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j4BczinukInZ7rkZ87SWQ1Kz9VA_KnqZ76rSDGiii-NpJZPI9HpnH6xM6JQ_aem_FCLhcYlS9Kzt6gEgHSFVXA&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT65K-6ptAi4CMrL7zDU5uEoGjFGjIxirxU3eXWdqTMYMdubtb31gg2kXRpA1broJ-ZZ8FLB-TLUrDRiLMC3oxah6iEmh-MiG4Mrpvz3Sqf4k1-mQRymH0_SQyRrD7NYnC8WqehDe5L1kLhtL9m8e9C-9AQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão