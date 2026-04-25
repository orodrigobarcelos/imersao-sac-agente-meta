<!-- Fonte: Moderação de respostas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Moderação de respostas a anúncios do Threads


Com a moderação de respostas, você pode gerenciar a conversa nos anúncios do Threads lendo respostas, ocultando conteúdo inadequado e adicionando suas próprias respostas. Para ver informações gerais sobre publicidade no Threads, consulte a [visão geral de anúncios do Threads](https://developers.facebook.com/docs/threads/threads-ads/).


### Limitações


- Apenas respostas diretas à mídia do anúncio são compatíveis para busca e resposta. As respostas aninhadas (respostas a respostas) não estão disponíveis por meio de nenhuma dessas operações.
- Somente respostas de texto podem ser adicionadas. Não há compatibilidade com respostas de imagem, vídeo e carrossel.
- Os tipos de anúncios compatíveis incluem anúncios de imagem única, anúncios de vídeo único, anúncios em carrossel, anúncios de personalização de ativos por posicionamento, posts estáticos e posts existentes.
- Entre os tipos de anúncios não compatíveis estão anúncios de catálogo Advantage+ e posts turbinados, assim como anúncios criados por contas do Threads associadas ao Instagram ou a uma Página.


## Antes de começar


Você precisará do seguinte:


- Um app da Meta com o produto API de Marketing habilitado
- Uma conta de anúncios com um anúncio ativo do Threads
- Um anúncio de um dos tipos compatíveis (veja [Limitações](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#limitations))


### Permissões


Estas permissões são obrigatórias para a conta de anúncios que possui o anúncio:


- `ads_read`: para leitura de mídia e respostas do anúncio
- `ads_management`: para ocultar e adicionar respostas
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)

## Recuperar a mídia de um anúncio do Threads


Para recuperar a mídia e os metadados associados de um anúncio do Threads, envie uma solicitação `GET` ao ponto de extremidade `/{media-id}` com um parâmetro `fields` separado por vírgulas para especificar quais campos devem ser retornados.


### Campos


| Nome | Descrição |
| --- | --- |
| id string | Identificação de mídia do Threads. |
| caption string | O texto associado à mídia. |
| like_count inteiro | É o número de curtidas na mídia. |
| username string | O nome de usuário do proprietário da mídia. |
| reply_count inteiro | Para respostas, o número de respostas diretas. Para mídias principais, o número total de respostas aninhadas. |
| share_count inteiro | O número de compartilhamentos. |
| quote_count inteiro | É o número de citações. |
| repost_count inteiro | É o número de reposts. |
| hide_status string | O status de ocultação da resposta. Valores: HUSHED e UNHUSHED . |
| timestamp string | O horário em que a mídia foi criada, no formato ISO 8601. |
| media_url string | O URL da CDN para a imagem ou o vídeo da mídia. |
| media_type string | O tipo de mídia. Valores: IMAGE , VIDEO , CAROUSEL . |
| gif_url string | O URL da CDN de um GIF anexado, se disponível. |
| owner_profile_pic string | A URL da CDN para a foto de perfil do dono. |
| is_owner_verified Booleano | Indica se a conta do proprietário da mídia foi verificada. |


### Exemplo de solicitação


```
curl -X GET "https://graph.facebook.com/v24.0/<MEDIA_ID>/?fields=id,caption,like_count,username,reply_count,hide_status,timestamp,media_type&access_token=<ACCESS_TOKEN>"
```


### Exemplo de resposta


```
{
  "id": "18106042978723008",
  "caption": "Check out our latest product!",
  "like_count": 42,
  "username": "mybrand",
  "reply_count": 5,
  "hide_status": "UNHUSHED",
  "timestamp": "2025-11-18T23:52:47+0000",
  "media_type": "IMAGE"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)

## Recuperar respostas a anúncios do Threads


Para recuperar as respostas diretas a uma mídia de anúncio do Threads, envie uma solicitação `GET` ao ponto de extremidade `/{media-id}/replies`, com um parâmetro `fields` separado por vírgulas para especificar quais campos devem ser retornados.


### Campos


| Nome | Descrição |
| --- | --- |
| id string | Identificação de mídia do Threads. |
| caption string | O texto associado à resposta. |
| like_count inteiro | É o número de curtidas na resposta. |
| username string | É o nome de usuário do autor da resposta. |
| reply_count inteiro | O número de respostas diretas a esta resposta. |
| share_count inteiro | O número de compartilhamentos. |
| quote_count inteiro | É o número de citações. |
| repost_count inteiro | É o número de reposts. |
| hide_status string | O status de ocultação da resposta. Valores: HUSHED e UNHUSHED . |
| timestamp string | O horário em que a resposta foi criada, no formato ISO 8601. |
| media_url string | O URL da CDN para a imagem ou o vídeo de mídia da resposta, se disponível. |
| media_type string | O tipo de mídia. Valores: IMAGE , VIDEO , CAROUSEL . |
| gif_url string | O URL da CDN de um GIF anexado, se disponível. |
| owner_profile_pic string | O URL da CDN para a foto do perfil do autor da resposta. |
| is_owner_verified Booleano | Indica se a conta do autor da resposta foi verificada. |


### Exemplo de solicitação


```
curl -X GET "https://graph.facebook.com/v24.0/<MEDIA_ID>/replies?fields=id,caption,username,like_count,hide_status,timestamp&access_token=<ACCESS_TOKEN>"
```


### Exemplo de resposta


```
{
  "data": [
    {
      "id": "18106042978723009",
      "caption": "Love this!",
      "username": "user123",
      "like_count": 3,
      "hide_status": "UNHUSHED",
      "timestamp": "2025-11-19T01:15:22+0000"
    },
    {
      "id": "18106042978723010",
      "caption": "Where can I buy this?",
      "username": "user456",
      "like_count": 1,
      "hide_status": "UNHUSHED",
      "timestamp": "2025-11-19T02:30:45+0000"
    }
  ]
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)

## Ocultar ou reexibir respostas em um anúncio do Threads


Para ocultar ou reexibir uma resposta no seu anúncio do Threads, envie uma solicitação `POST` ao ponto de extremidade `/{reply-id}/manage_reply`. Quando você oculta uma resposta, ela é removida da visualização pública, mas não é excluída.


**Observação:** o app precisa ter a permissão `ads_management` para usar o ponto de extremidade.


### Parâmetros


| Nome | Descrição |
| --- | --- |
| hide Booleano | Obrigatório. Defina como true para ocultar a resposta ou false para reexibi-la. |


### Campos de resposta


| Nome | Descrição |
| --- | --- |
| success Booleano | Retorna true se a resposta foi ocultada/reexibida com sucesso. |


### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/v24.0/<REPLY_ID>/manage_reply" \ -H "Authorization: Bearer <ACCESS_TOKEN>" \ -d "hide=true"
```


### Exemplo de resposta


```
{
  "success": true
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)

## Adicionar respostas a um anúncio do Threads


Para adicionar uma resposta de texto ao seu anúncio do Threads, envie uma solicitação `POST` para o ponto de extremidade `/{reply-id}/add_reply`. Apenas respostas de texto são compatíveis.


**Observação:** o app precisa ter a permissão `ads_management` para usar o ponto de extremidade.


### Parâmetros


| Nome | Descrição |
| --- | --- |
| text string | Obrigatório. É o conteúdo de texto da sua resposta. |


### Campos de resposta


| Nome | Descrição |
| --- | --- |
| id string | O ID da resposta recém-criada. |


### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/v24.0/<REPLY_ID>/add_reply" \ -H "Authorization: Bearer <ACCESS_TOKEN>" \ -d "text=Agradecemos seu interesse! Confira nosso site para ver mais informações."
```


### Exemplo de resposta


```
{
  "id": "18106042978723011"
}
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)

## Saiba mais


- [Visão geral dos anúncios do Threads](https://developers.facebook.com/docs/threads/threads-ads/)
- [Registro de alterações da API do Threads](https://developers.facebook.com/docs/threads/changelog/)
- [Permissões da API de Marketing](https://developers.facebook.com/docs/marketing-api/overview/authorization/)
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#)Nesta Página[Moderação de respostas a anúncios do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#modera--o-de-respostas-a-an-ncios-do-threads)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#antes-de-come-ar)[Permissões](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#permiss-es)[Recuperar a mídia de um anúncio do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#recuperar-a-m-dia-de-um-an-ncio-do-threads)[Campos](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#campos)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-solicita--o)[Exemplo de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-resposta)[Recuperar respostas a anúncios do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#recuperar-respostas-a-an-ncios-do-threads)[Campos](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#campos-2)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-solicita--o-2)[Exemplo de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-resposta-2)[Ocultar ou reexibir respostas em um anúncio do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#ocultar-ou-reexibir-respostas-em-um-an-ncio-do-threads)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#par-metros)[Campos de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#campos-de-resposta)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-solicita--o-3)[Exemplo de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-resposta-3)[Adicionar respostas a um anúncio do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#adicionar-respostas-a-um-an-ncio-do-threads)[Parâmetros](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#par-metros-2)[Campos de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#campos-de-resposta-2)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-solicita--o-4)[Exemplo de resposta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#exemplo-de-resposta-4)[Saiba mais](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/reply-moderation#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vbnJRmxcrdMn-3AmNtJ0j1cqqq9K7eBUGPxxgucDNQU71iT_3IlM9E3U4jw_aem_zWNQu4Rh_j7Iis2-MzFLmw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR78TYbMBNAstngvhBKwBshAvZsjk_nysIYT8koRoiVGrXqS0t8SvRfjNI1drA_aem_AgfJcqIbGdAIMtimFmOzdg&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mSssUzMduJpqWJ9ffeadtlllfYL9z_ICIETaYuTMRYzcaHwOtVql-jPdoww_aem_xpZai9WmrYGHISWJMY9Qog&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5g04Fp_AZ-xHJdZZa3dgbqfFeMbQEgdlpgcq0zQ9eaeDs2Rv74MskXoMy4og_aem_-p-FnJfDTfFJacK67k1FVw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QLQS_R6QdBg4Nee401RMBZCeoD_yyGHTh8WIi8l5VFcQH_Y-Sk8SZEiNCEg_aem_qmdzBMuOXxZStJBxULfwUg&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5g04Fp_AZ-xHJdZZa3dgbqfFeMbQEgdlpgcq0zQ9eaeDs2Rv74MskXoMy4og_aem_-p-FnJfDTfFJacK67k1FVw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mSssUzMduJpqWJ9ffeadtlllfYL9z_ICIETaYuTMRYzcaHwOtVql-jPdoww_aem_xpZai9WmrYGHISWJMY9Qog&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7kn4RS_oHEOot3tEsXFVO5Wcgnev5VdvKz5UOhHj7drnx-6FrnBElL67804g_aem_jtJIOuF1VFgHjskQ0mV__A&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7kn4RS_oHEOot3tEsXFVO5Wcgnev5VdvKz5UOhHj7drnx-6FrnBElL67804g_aem_jtJIOuF1VFgHjskQ0mV__A&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5x5JHQZY_5JR2EMBmFoXOxIDqPQBW9aUFTb14jm4-KOlXG_GBdVqxoZblJJg_aem__GUjv2CdtncLaKlLE59qFA&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vbnJRmxcrdMn-3AmNtJ0j1cqqq9K7eBUGPxxgucDNQU71iT_3IlM9E3U4jw_aem_zWNQu4Rh_j7Iis2-MzFLmw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QLQS_R6QdBg4Nee401RMBZCeoD_yyGHTh8WIi8l5VFcQH_Y-Sk8SZEiNCEg_aem_qmdzBMuOXxZStJBxULfwUg&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mSssUzMduJpqWJ9ffeadtlllfYL9z_ICIETaYuTMRYzcaHwOtVql-jPdoww_aem_xpZai9WmrYGHISWJMY9Qog&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vbnJRmxcrdMn-3AmNtJ0j1cqqq9K7eBUGPxxgucDNQU71iT_3IlM9E3U4jw_aem_zWNQu4Rh_j7Iis2-MzFLmw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5g04Fp_AZ-xHJdZZa3dgbqfFeMbQEgdlpgcq0zQ9eaeDs2Rv74MskXoMy4og_aem_-p-FnJfDTfFJacK67k1FVw&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DHG98QjaN9EqTYag3CfCk8QHq07ygthfgYAp-gXryMnX9u-R9Ac0h2PtjKA_aem_3UN-v_aFoD3JnSdCLeNCZA&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR50D36JAZrtfVb0RPl2Ik-ydehu56bewGxsXBlxHBArxXK3YoNW-RyU2Y6Ykg_aem_Kj6t9Kp4tQFQthBwFG7NYg&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mSssUzMduJpqWJ9ffeadtlllfYL9z_ICIETaYuTMRYzcaHwOtVql-jPdoww_aem_xpZai9WmrYGHISWJMY9Qog&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mSssUzMduJpqWJ9ffeadtlllfYL9z_ICIETaYuTMRYzcaHwOtVql-jPdoww_aem_xpZai9WmrYGHISWJMY9Qog&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QLQS_R6QdBg4Nee401RMBZCeoD_yyGHTh8WIi8l5VFcQH_Y-Sk8SZEiNCEg_aem_qmdzBMuOXxZStJBxULfwUg&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4xHvxMODRRp-WwniL0ASxYex44TdlvaDiazMqhUBZcFDYrh-qx0BnEonJWaf0xEV2jtVlbgSLWvshNl3lzEuRdH49UYJR9SFkFxwzFdTFLsHl8IRUEZ-XcwU9eOgl0CA9jPqKAcS4vC6qNhVlNxlgnEHc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão