<!-- Fonte: Moderação de posts - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Moderação de posts


Cada [criativo de anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative) com `instagram_user_id` cria um post de stream do Instagram para a conta com essa identificação. Use a API para acessar o post, adicionar e excluir comentários, além de verificar os comentários dos visualizadores.


Para moderar seus posts:


- [Por meio da Graph API do Instagram, usando `effective_instagram_media_id`](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#post-mod-gapi)


No momento, não é possível recuperar mídias e comentários com restrição de idade por meio da Graph API. Para fazer isso, use a [abordagem da Graph API do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#post-mod-gapi).


Saiba mais sobre as [restrições para esse recurso](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#comments-restrictions).


### Comentários orgânicos em relação a não orgânicos


A moderação de posts do Instagram também envolve lidar com comentários deixados pelos usuários. Existem dois tipos de comentários: orgânicos e não orgânicos. Comentários orgânicos são feitos na mídia orgânica do Instagram. Comentários não orgânicos são feitos em mídias de anúncios. [Saiba mais sobre os comentários do Instagram](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).


Ao usar a mídia representada por `effective_instagram_media_id`, você terá acesso apenas aos comentários não orgânicos dos seus posts. Para ver os comentários orgânicos, use a mídia representada por `source_instagram_media_id`. Quando tiver o número de identificação associado, use a [Graph API](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#post-mod-gapi) para acessar comentários orgânicos.


## Usar a API de Marketing para receber informações sobre a mídia


Os criativos do anúncio com `instagram_user_id` têm dois campos: `instagram_permalink_url` e `effective_instagram_media_id`.


Com o campo `instagram_permalink_url`, você pode receber um URL para o post correspondente do Instagram e ver as interações dos usuários com o post do anúncio. Como você vê esse post em um site em vez do app para celular do Instagram, não é exatamente o que os visualizadores do seu anúncio veem. Ele não exibe a identificação "Patrocinado" nem uma chamada para ação, e não mostra anúncios em carrossel com várias imagens.


Para acessar o `instagram_permalink_url` e o `effective_instagram_media_id` de um criativo do anúncio:

```
curl -G \ -d "access_token=<ACCESS_TOKEN>"\ -d "fields=instagram_permalink_url,effective_instagram_media_id"\ "https://graph.facebook.com/v25.0/<AD_CREATIVE_ID>"
```


Com o `effective_instagram_media_id`, envie uma solicitação `GET` para receber todos os [comentários](https://developers.facebook.com/docs/graph-api/reference/instagram-comment/) de um post:

```
curl -G \ -d "access_token=<ACCESS_TOKEN>"\ -d "fields=id,message,instagram_user"\ "https://graph.facebook.com/v25.0/<EFFECTIVE_INSTAGRAM_MEDIA_ID>/comments"
```


A resposta inclui apenas comentários não orgânicos:

```
{
  "data": [
    {
      "id": "1234",
      "text": "Where can I get it?"
    }
    {
      "id": "5678",
      "text": "This is nice.",

    }
  ],
  "paging": {
    ...
  }
}
```
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#)

## Usar a Graph API do Instagram para comentários


É necessário ter permissões adicionais para usar a Graph API do Instagram no gerenciamento de comentários em anúncios do Instagram. Para saber mais, [veja as seções sobre permissões](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments).


Consulte a documentação abaixo para ver as seguintes instruções:


- [Como criar um novo comentário](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments#create)
- [Como ler um comentário](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#read)
- [Como atualizar, ocultar e reexibir comentários](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#update)
- [Como excluir um comentário](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#delete)
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#)

## Limitações


- A moderação de posts **não está disponível para stories do Instagram**. Os stories não são posts abertos para comentários.
- Os recursos de moderação de comentários não funcionam com anúncios de catálogo Advantage+. No criativo do anúncio, o campo `effective_instagram_media_id` não funciona com o [modelo de criativo para anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/guides/instagramads/ad_creative#dynamic).
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#)[○](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#)Nesta Página[Moderação de posts](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#modera--o-de-posts)[Usar a API de Marketing para receber informações sobre a mídia](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#post-mod-mapi)[Usar a Graph API do Instagram para comentários](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#post-mod-gapi)[Limitações](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation#comments-restrictions) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dQZoWTKwbKdE5EfqDTK_yF5xjfnhsf5T6g7kmAyinTLwX4hydqgSyGOz7qw_aem_hn7Q4dPMOrm2i0SOfYlr0g&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DUTlXHr6X4elN-TwCuN2rQxYbb4oca36bEpi8rruOYJ5zf_VdI5rfFJZtnw_aem_LNodSA-aL5LTws6hRM2-jQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR78a-xi8f64D-gBxTYKkGUVq8qWD4WiDOfTbRcF3YjPO5YA3edGQqmgzM8g-Q_aem_H47ci-XzZDt6Je_KEk8ccg&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DUTlXHr6X4elN-TwCuN2rQxYbb4oca36bEpi8rruOYJ5zf_VdI5rfFJZtnw_aem_LNodSA-aL5LTws6hRM2-jQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7_PrZa8LRT_UqB_-i367VwJY-tBQHIWbLyBU2opt0w-bgnOOlHFBbvNc83kw_aem_3LZhUvqTP-lM1FM_YLdtcQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR78a-xi8f64D-gBxTYKkGUVq8qWD4WiDOfTbRcF3YjPO5YA3edGQqmgzM8g-Q_aem_H47ci-XzZDt6Je_KEk8ccg&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DUTlXHr6X4elN-TwCuN2rQxYbb4oca36bEpi8rruOYJ5zf_VdI5rfFJZtnw_aem_LNodSA-aL5LTws6hRM2-jQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dQZoWTKwbKdE5EfqDTK_yF5xjfnhsf5T6g7kmAyinTLwX4hydqgSyGOz7qw_aem_hn7Q4dPMOrm2i0SOfYlr0g&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7_PrZa8LRT_UqB_-i367VwJY-tBQHIWbLyBU2opt0w-bgnOOlHFBbvNc83kw_aem_3LZhUvqTP-lM1FM_YLdtcQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DUTlXHr6X4elN-TwCuN2rQxYbb4oca36bEpi8rruOYJ5zf_VdI5rfFJZtnw_aem_LNodSA-aL5LTws6hRM2-jQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5b0_eHtuY8ge3JAlCNN8Er5j0XVVmOtm00SPF9yLdWla2__bVH7A2tIbHkdg_aem_gakKcRL3adssk0Ir9HP0eg&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4ZHUfBdlj4p5uE7kuq8pbhNb3FMR7Lq7UzIT6B0GfugaIXLUUJ8KsSiQyB9w_aem_iLYAGK_G3SNXIZPXTM0s_Q&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dQZoWTKwbKdE5EfqDTK_yF5xjfnhsf5T6g7kmAyinTLwX4hydqgSyGOz7qw_aem_hn7Q4dPMOrm2i0SOfYlr0g&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yGt4YaRduNZzth-KMQXktPwk1pjn2ELE7PIUvWIKkdy36DybjQVSYOSR3rw_aem_VhLTK6MR_sNMsa4XuO5pbA&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7194RgVdXmt8RI1gQrdrwGRpkWDciyk4pAy1VG5nVkGixdCmFu39l5KOUMTQ_aem_SpdssdJh-ymssDaIQ2qeJQ&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Y0CIAteyXjXXougjpckHrbwbCHkTO999z7F3s8jVWAORMpXHGW8rHX4qimWGziGTTC4LCxNs-8nZjiEz6XVQFfLRF_1DO6-X7fB6Lkka9PIJXB4I_3K2MkHPpJxOwDQiEJ7ZzrpxpAPz2LKgtnaDY4UI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão