<!-- Fonte: Anúncios com lembrete - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios com lembrete do Instagram


Este documento mostra como usar a API de Marketing para criar anúncios com lembretes do Instagram e anúncios com lembretes.


## Antes de começar


Antes de dar os primeiros passos, você precisa do seguinte:


- A permissão `ads_management`
- Um próximo evento do Instagram criado usando a [Upcoming Event Management API](https://developers.facebook.com/docs/instagram-api/guides/upcoming-events) ou o Gerenciador de Anúncios.


### Limitações


- Se o conjunto de anúncios de um anúncio com lembrete tiver uma data de término, essa data precisa ser posterior à data de início do próximo evento do Instagram do anúncio com lembrete.
- Um anúncio com lembrete deixa de ser veiculado assim que o evento passa.
- Nem todos os objetivos da campanha de anúncios ou metas de otimização do conjunto de anúncios são compatíveis com lembretes. Por exemplo, objetivos da campanha de anúncios e metas de otimização do conjunto de anúncios compatíveis incluem o seguinte: - `objective: OUTCOME_ENGAGEMENT` e `optimization_goal=REMINDERS_SET` - `objective: OUTCOME_ENGAGEMENT` e `optimization_goal=THRUPLAY` - `objective: OUTCOME_AWARENESS` e `optimization_goal=THRUPLAY` - `objective: OUTCOME_AWARENESS` e `optimization_goal=REACH` - `objective: OUTCOME_SALES` e `optimization_goal=OFFSITE_CONVERSIONS`
- Os criativos do anúncio que usam a funcionalidade de lembrete não podem sempre estar associados a diferentes objetivos da campanha de anúncios. Para corrigir isso, crie criativos separados para diferentes objetivos da campanha de anúncios.


## Etapa 1: criar uma campanha de anúncios


O primeiro passo é criar a campanha de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/campaigns`, em que `<AD_ACCOUNT_ID>` é a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `name` (obrigatório)
- `objective` (obrigatório) — **Nota:** nem todos os objetivos da campanha de anúncios são compatíveis com a funcionalidade de lembrete.
- `special_ad_categories` (obrigatório)
- `status` (opcional)


### Solicitação


*Texto formatado para facilitar a leitura. Substitua os espaços reservados pelos seus próprios valores.*

```
curl -X POST "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/campaigns" \
  -H "Content-Type: application/json" \
  -d '{
    "name":"My First Reminder Ads Campaign",
    "objective":""OUTCOME_ENGAGEMENT"",
    "special_ad_categories":""[]"",
  }'
```


### Resposta


Caso ela seja bem-sucedida, o app recebe a resposta JSON a seguir com a identificação da campanha de anúncios criada.

```
{

  "id": "<AD_CAMPAIGN_ID>"
}
```
[○](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#)

## Etapa 2: criar um conjunto de anúncios


Depois, crie seu conjunto de anúncios. Para isso, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adsets`, em que `<AD_ACCOUNT_ID>` é a identificação da sua conta de anúncios da Meta. A solicitação precisa incluir:


- `destination_type` (obrigatório)
- `optimization_goal` (obrigatório) — **Nota:** nem todos os objetivos de otimização do conjunto de anúncios são compatíveis com a funcionalidade de lembrete.
- `instagram_positions` (opcional) — `stream`, `story` e `reels` são alguns posicionamentos compatíveis com anúncios com lembrete. Para mais informações sobre a especificação de posicionamento, consulte [Direcionamento de posicionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting) e [Primeiros passos: Posicionamento](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#targeting) para anúncios do Instagram.


### Solicitação


*Texto formatado para facilitar a leitura. Substitua os espaços reservados pelos seus próprios valores.*

```
curl -X POST "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets" \
  -F 'billing_event=IMPRESSIONS' \
  -F 'campaign_id=<AD_CAMPAIGN_ID>' \
  -F 'daily_budget=1000' \
  -F 'destination_type=ON_REMINDER' \
  -F 'name=Reminder Ads Ad Set' \
  -F 'optimization_goal=REMINDERS_SET' \
  -F 'targeting={
    "geo_locations": { "countries":["US"] },
    "device_platforms": ["mobile"]
  }'
```


### Resposta


Caso ela seja bem-sucedida, o app recebe a resposta JSON a seguir com a identificação do conjunto de anúncios criado.

```
{

  "id": "<AD_SET_ID>"
}
```
[○](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#)

## Passo 3: criar um criativo do anúncio com um evento próximo


Com o criativo, é possível adicionar ativos aos seus anúncios. Para gerar um criativo do anúncio, faça uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/adcreatives`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `asset_feed_spec`: contendo a identificação do próximo evento que você quer associar ao anúncio.
- `object_story_spec`: para anúncios com lembrete, o valor do link precisa ser especificado. Se não quiser que um link apareça no seu anúncio, use o URL falso **https://fb.com/**. O link falso não aparecerá no seu anúncio.


### Solicitação


*Texto formatado para facilitar a leitura. Substitua os espaços reservados pelos seus próprios valores.*

```
curl -X POST "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives" \
    -F 'name=Sample ad creative' \
    -F 'object_story_spec={
        "page_id": "<PAGE_ID>",
        "instagram_user_id": "<IG_USER_ID>",
        "link_data": {
            "call_to_action": {
                "type": "LEARN_MORE"
            },
            "image_hash": "<IMAGE_HASH>",
            "link": "https://fb.com/"
        }
    }' \
    -F 'asset_feed_spec={
        "upcoming_events": [
            {
                "event_id": <EVENT_ID>
                "event_title": "Season Premiere",
                "start_time": "2024-05-11T16:00:00+0000",
            }
        ]
    }' \
    -F 'degrees_of_freedom_spec={
        "creative_features_spec": {
            "standard_enhancements": {
                "action_metadata": {
                    "type": "DEFAULT"
                },
                "enroll_status": "OPT_OUT"
            }
        },
        "degrees_of_freedom_type": "USER_ENROLLED_AUTOFLOW"
    }' \
    -F 'access_token=<ACCESS_TOKEN>'
```


### Resposta


Caso ela seja bem-sucedida, o app recebe a resposta JSON a seguir com a identificação do criativo do anúncio criado.

```
{
  "id": "<AD_CREATIVE_ID>"
}
```
[○](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#)

## Etapa 4: criar um anúncio


Os anúncios permitem que você associe informações do criativo aos seus conjuntos de anúncios. Para criar um anúncio, envie uma solicitação `POST` para o ponto de extremidade `/act_<AD_ACCOUNT_ID>/ads`, sendo `<AD_ACCOUNT_ID>` a identificação da conta de anúncios da Meta. A solicitação precisa incluir:


- `name`: (obrigatório)
- `adset_id`: a identificação do conjunto de anúncios criado. (obrigatório)
- `creative`: um objeto JSON com a identificação do criativo criado. (obrigatório)
- `status`: `PAUSED` para que você possa revisar o anúncio antes da veiculação. (opcional)


### Solicitação


*Texto formatado para facilitar a leitura. Substitua os espaços reservados pelos seus próprios valores.*

```
curl -X POST "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads" \
  -F 'name=Reminder Ad' \
  -F 'adset_id=<AD_SET_ID> \
  -F 'creative={
    "creative_id": "<AD_CREATIVE_ID>"
  }' \
  -F 'status=PAUSED \
  -F 'access_token=<ACCESS_TOKEN>'
```


### Resposta


Caso ela seja bem-sucedida, o app recebe a resposta JSON a seguir com a identificação do anúncio criado.

```
{
  "id": "<AD_ID>"
}
```
[○](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#)[○](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#)Nesta Página[Anúncios com lembrete do Instagram](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#an-ncios-com-lembrete-do-instagram)[Antes de começar](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#antes-de-come-ar)[Limitações](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#limita--es)[Etapa 1: criar uma campanha de anúncios](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#etapa-1--criar-uma-campanha-de-an-ncios)[Solicitação](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#solicita--o)[Resposta](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#resposta)[Etapa 2: criar um conjunto de anúncios](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#etapa-2--criar-um-conjunto-de-an-ncios)[Solicitação](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#solicita--o-2)[Resposta](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#resposta-2)[Passo 3: criar um criativo do anúncio com um evento próximo](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#passo-3--criar-um-criativo-do-an-ncio-com-um-evento-pr-ximo)[Solicitação](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#solicita--o-3)[Resposta](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#resposta-3)[Etapa 4: criar um anúncio](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#etapa-4--criar-um-an-ncio)[Solicitação](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#solicita--o-4)[Resposta](https://developers.facebook.com/docs/instagram/marketing-api/guides/reminder-ads#resposta-4) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JHMlONhKhPDd7XO0HmUFg3UHN7zB4_MlpVCmbpnC5lYNavhdkzA0wQzzLXg_aem_xuVl-bcpIWmXpM24djvAwA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ycn6w6krL-FN8YrYJtv2K1rPl5JehNQGT-6pRPGgDNdIdfed-0MGDIQ31iw_aem_U8he10fPTMAD0TGo68-Leg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4j5dQtupUsXMZh9-l3Zme_xFeF5aIVWk2IC3Z_YMgO5AG1yRwGTyyfL0HIOQ_aem_R9BPMO4dBrd0pSOPP_cu9Q&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ycn6w6krL-FN8YrYJtv2K1rPl5JehNQGT-6pRPGgDNdIdfed-0MGDIQ31iw_aem_U8he10fPTMAD0TGo68-Leg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5eFYm-s44sE9iOmAcEh0u_SRlE9YvRAzdOeHzcUJLLXQFkjUXk32G0ZsZMAw_aem_KdTzxdn2_WlTnp8t9mn01A&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6fY6LNkJReZVQITNJSnxNx5ECSxoL-jKq78ZByE1siK-CmGBKePGHrSAlchQ_aem_CskBa0Y0BsqzpFT8DzXJwg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7-12yLC5XkhdSkIddk5VFTgYSKYQkeO8yy3TIHkJ_aRaNkmb4jLZJ89OfKUw_aem_aGHhrCllUO4FJvMiqq5NMQ&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4j5dQtupUsXMZh9-l3Zme_xFeF5aIVWk2IC3Z_YMgO5AG1yRwGTyyfL0HIOQ_aem_R9BPMO4dBrd0pSOPP_cu9Q&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ULveR47ggLT0Jl-FJEKmiXyUBk7XQJYRwNvVerpjI3-_Ukin0EfT-jp_qlA_aem_3g3z1hBfWqRs8P9KsFIFZA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7-12yLC5XkhdSkIddk5VFTgYSKYQkeO8yy3TIHkJ_aRaNkmb4jLZJ89OfKUw_aem_aGHhrCllUO4FJvMiqq5NMQ&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JHMlONhKhPDd7XO0HmUFg3UHN7zB4_MlpVCmbpnC5lYNavhdkzA0wQzzLXg_aem_xuVl-bcpIWmXpM24djvAwA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JHMlONhKhPDd7XO0HmUFg3UHN7zB4_MlpVCmbpnC5lYNavhdkzA0wQzzLXg_aem_xuVl-bcpIWmXpM24djvAwA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ycn6w6krL-FN8YrYJtv2K1rPl5JehNQGT-6pRPGgDNdIdfed-0MGDIQ31iw_aem_U8he10fPTMAD0TGo68-Leg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6fY6LNkJReZVQITNJSnxNx5ECSxoL-jKq78ZByE1siK-CmGBKePGHrSAlchQ_aem_CskBa0Y0BsqzpFT8DzXJwg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6fY6LNkJReZVQITNJSnxNx5ECSxoL-jKq78ZByE1siK-CmGBKePGHrSAlchQ_aem_CskBa0Y0BsqzpFT8DzXJwg&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NF5kXNy5IggUjgq_H5EGAqagYFOF0WnHTQMQM6bzh2-597XcXpROu7zlocA_aem_URXMVAuIPEB9Ie8D3v1aaQ&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ULveR47ggLT0Jl-FJEKmiXyUBk7XQJYRwNvVerpjI3-_Ukin0EfT-jp_qlA_aem_3g3z1hBfWqRs8P9KsFIFZA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JHMlONhKhPDd7XO0HmUFg3UHN7zB4_MlpVCmbpnC5lYNavhdkzA0wQzzLXg_aem_xuVl-bcpIWmXpM24djvAwA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4j5dQtupUsXMZh9-l3Zme_xFeF5aIVWk2IC3Z_YMgO5AG1yRwGTyyfL0HIOQ_aem_R9BPMO4dBrd0pSOPP_cu9Q&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ULveR47ggLT0Jl-FJEKmiXyUBk7XQJYRwNvVerpjI3-_Ukin0EfT-jp_qlA_aem_3g3z1hBfWqRs8P9KsFIFZA&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7z76mivudXrIvmih88HSh1Yt4P4m6Xg-j-6z80aJO3Ctjp0VxL4QgngZIPFkjQGWtQnfSUJoMtJZQiAZDLLG0JalvE4ZFLc9PlwDuDXWeR_nbY2Tj2sXvHNzv9f0rzZfU6L7aX3gq5koRV4wHWaNA7-0o)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão