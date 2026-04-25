<!-- Fonte: Requisitos de mídia - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Requisitos de mídia


Se você usar imagens ou vídeos que não atendem aos requisitos abaixo, a validação do anúncio não será bem-sucedida durante a criação do criativo do anúncio.


## Anúncios para o Feed e o Explorar do Instagram


### Legendas


Há um limite de 2.200 caracteres para legendas de anúncios direcionados apenas para o Instagram, e um erro é retornado quando há uma tentativa de criar esse anúncio. Se um anúncio direcionado ao Instagram e ao Facebook exceder esse limite, a solicitação de criação de um anúncio será bem-sucedida, mas ele não será veiculado no Instagram.


### Requisitos de imagem e vídeo


#### Proporção de tela


A proporção de tela recomendada para imagem e vídeo para streaming do Instagram é de 1:1. Recomendamos o uso de vídeos e imagens quadradas para aproveitar toda a área de exibição em dispositivos móveis. O streaming do Instagram também é compatível com imagens e vídeos com:


- Proporção de tela de 1.91:1
- Proporção de tela de 4:5
- Qualquer proporção de tela entre 1.91:1 e 4:5


#### Tamanho


Exigimos que todas as imagens e vídeos tenham pelo menos 600 px de largura, independentemente do posicionamento do anúncio. No entanto, os números recomendados para imagens podem mudar por posicionamento:


| Posicionamento | Recomendação de tamanho da imagem |
| --- | --- |
| Instagram | 640 px de largura ou maior |
| Facebook | 1080 px por 1080 px ou maior |


Se você executar [anúncios de catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads), as imagens de produtos especificadas em [feeds de produtos](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-catalog#setup-product-feed) devem ter pelo menos 600 px, tanto em largura como em altura.


#### Duração do vídeo


Os vídeos precisam ter entre 3 e 60 segundos. Um vídeo é reproduzido num loop infinito no Instagram, mas apenas uma vez no Facebook.


#### Miniatura de vídeo


`video_data` requer uma imagem em miniatura. Essa imagem deve ter a mesma proporção do vídeo, com uma largura de pelo menos 600 px.


#### Tamanho do arquivo de vídeo


O tamanho do arquivo de vídeo não pode ser superior a 2.3 GB. Depois de carregado no Facebook e comprimido, ele não pode ser maior do que um limite interno. Para ver se o arquivo de vídeo funciona como anúncio do Instagram, carregue-o primeiro e use esta chamada de API para verificar o valor booliano `is_instagram_eligible`:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "fields=is_instagram_eligible"\
"https://graph.facebook.com/<API_VERSION>/<VIDEO_ID>"
```


A resposta terá esta aparência se o vídeo não estiver qualificado:

```
{
  "is_instagram_eligible": false,
  "id": "<VIDEO_ID>"
}
```


#### Cortes


Os vídeos não podem ser cortados, mas as imagens podem. As informações a seguir são válidas somente para imagens.


O comportamento de corte depende de você enviar uma especificação de corte. Para posicionamentos do Facebook, você também pode usar [`use_flexible_image_aspect_ratio`](https://developers.facebook.com/ads/blog/post/2019/03/26/flexible-image-link-ads).


Se você fornecer uma especificação de corte 100x100 em `link_data`:


- Usamos isso para cortes de posicionamentos no Instagram e no Facebook.
- Se a imagem for maior que 1.91:1, o Instagram cortará o anúncio para 1.91:1.


Se você não fornecer uma especificação de corte:


- Se a imagem for maior que 4:5 sem uma especificação de corte, o Instagram a cortará para 4:5.


#### Corte e tamanho


Mais detalhes sobre cortes e recomendações de tamanho de acordo com o posicionamento escolhido.


Para o Instagram:


| Mídia | Com especificações de corte 100x100 | Sem especificações de corte 100x100 |
| --- | --- | --- |
| Imagem 1:1 | Após o corte, pelo menos 600x600 px | Pelo menos 600x600 px |
| Imagem 4:5 | Após o corte, pelo menos 600x600 px | Pelo menos 600x750 px |
| Imagem 1.91:1 | Após o corte, pelo menos 600x600 px | Pelo menos 600x315 px |
| Proporção da imagem entre 4:5 e 1.91:1 | Após o corte, pelo menos 600x600 px | Pelo menos 600 px de largura |
| Proporção da imagem entre 1:1 e 1.91:1 | Após o corte, pelo menos 600x600 px | Pelo menos 600 px de largura |
| Proporção da imagem entre 4:5 e 1.91:1 | Após o corte, pelo menos 600x600 px | Com object_story_spec , corte central para 1.91:1, se a imagem for mais larga do que isso, ou 4:5 se for mais alta do que isso. Após o corte, a largura deve ser de pelo menos 600 px. Com object_story_id para um post existente, não é válida. |


Para o Facebook:


| Mídia | Nenhuma especificação de corte, e use_flexible_image_aspect_ratio definido como falso. | Nenhuma especificação de corte, e use_flexible_image_aspect_ratio definido como verdadeiro, ou não definido. (comportamento padrão) | Com especificações de corte 100x100 |
| --- | --- | --- | --- |
| Imagem 1:1 | Corte central de 1.91:1 realizado automaticamente. Após o corte, pelo menos 600x315 px | Pelo menos 600x600 px | Após o corte, pelo menos 600x600 px |
| Imagem 4:5 | Corte central de 1.91:1 realizado automaticamente. Após o corte, pelo menos 600x315 px | Corte central de 1:1 realizado automaticamente. Após o corte, pelo menos 600x600 px | Após o corte, pelo menos 600x600 px |
| Imagem 1.91:1 | Pelo menos 600x315 px | Pelo menos 600x315 px | Após o corte, pelo menos 600x600 px |
| Proporção da imagem entre 4:5 e 1.91:1 | Corte central de 1.91:1 realizado automaticamente. Após o corte, pelo menos 600x315 px | Corte central de 1:1 realizado automaticamente. Após o corte, pelo menos 600x600 px | Após o corte, pelo menos 600x600 px |
| Proporção da imagem entre 1:1 e 1.91:1 | Corte central de 1.91:1 realizado automaticamente. Após o corte, pelo menos 600x315 px | Pelo menos 600 px de largura | Após o corte, pelo menos 600x600 px |
| Proporção da imagem entre 4:5 e 1.91:1 | Corte central de 1.91:1 realizado automaticamente. Após o corte, pelo menos 600x315 px | Corte central de 1.91:1, se a imagem for mais larga do que isso, ou 1:1 se for mais alta do que isso. Após o corte, a largura deve ser de pelo menos 600 px. | Após o corte, pelo menos 600x600 px |


#### Imagens adicionais


Normalmente, entregamos a imagem padrão especificada por `image_url`, mas você pode veicular `additonal_image_urls` se definir `additional_image_index` no criativo do modelo de anúncio. Para ver uma prévia dos anúncios de catálogo Advantage+ com o `additional_image_index`, passe todas as `object_story_spec` para o ponto de extremidade `/generatepreviews`. Você não pode passar apenas `object_story_id`.


Se um produto tiver uma imagem pequena demais para o Instagram, a criação de anúncios não terá erros, mas o anúncio não será veiculado pelo anúncios de catálogo Advantage+ do Instagram.
[○](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#)

## Anúncios de story do Instagram


### Requisitos de imagem e vídeo


#### Proporção de tela


Para o Instagram Stories, recomendamos uma proporção de imagem e vídeo de 9:16. O Instagram Stories também é compatível com imagens e vídeos com:


- Modo paisagem de 1.91:1
- Modo retrato de 4:5
- Qualquer proporção de tela em 1.91:1 e 4:5


Para anúncios em carrossel no Instagram Stories, confira a seção [Anúncios em carrossel do Instagram](https://developers.facebook.com/docs/instagram/ads-api/reference/?locale=en_US#Stories-carousel).


#### Tamanho


A largura mínima da imagem ou do vídeo é de 600 px.


#### Cortes


Os vídeos não podem ser cortados, por isso, forneça vídeos entre 1.91:1 e 4:5 ou 9:16 e mais.


As imagens podem ser cortadas. Você pode usar especificações de corte de imagens para anúncios no Instagram Stories usando chaves de corte 90x160, 100x100 e 191x100:


- Se uma imagem for maior do que 1.91:1 e você não fornecer especificações de corte, a imagem será cortada para 1.91:1.
- Se uma proporção de imagem estiver entre 4:5 e 9:16, e você não fornecer uma especificação de corte, a imagem será cortada para 4:5.
[○](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#)

## Recursos


- Guia de anúncios: [Anúncios de imagem no feed](https://www.facebook.com/business/ads-guide/image/instagram-feed)
- Guia de anúncios: [Anúncios de imagem no story](https://www.facebook.com/business/ads-guide/image/instagram-story)
- Guia de anúncios: [Anúncios de imagem no Explorar](https://www.facebook.com/business/ads-guide/image/instagram-explore)
- Guia de anúncios: [Anúncios de vídeo no feed](https://www.facebook.com/business/ads-guide/video/instagram-feed)
- Guia de anúncios: [Anúncios de vídeo no story](https://www.facebook.com/business/ads-guide/video/instagram-story)
- Guia de anúncios: [Anúncios de vídeo no Explorar](https://www.facebook.com/business/ads-guide/video/instagram-explore)
- [Boas práticas: tamanhos de imagem](https://developers.facebook.com/docs/sharing/best-practices#images)
[○](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#)[○](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#)Nesta Página[Requisitos de mídia](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#requisitos-de-m-dia)[Anúncios para o Feed e o Explorar do Instagram](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#an-ncios-para-o-feed-e-o-explorar-do-instagram)[Legendas](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#legendas)[Requisitos de imagem e vídeo](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#requisitos-de-imagem-e-v-deo)[Anúncios de story do Instagram](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#an-ncios-de-story-do-instagram)[Requisitos de imagem e vídeo](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#requisitos-de-imagem-e-v-deo-2)[Recursos](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements#recursos) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7r4TgNAX0u7CVpfxhj_lye_5JzLtz-bHMkMwyQI_tPL459D8D7Ml-g-ArFKg_aem_bBWI2CPBWRERmmnU_TLt2Q&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45tWxnWf899C4o_GN6jHonzUwJ3yef0k2V08e4gRit8puANlF1er0FwEl0gQ_aem_wEOs3E4Oa6pcqqC6sGsssA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45tWxnWf899C4o_GN6jHonzUwJ3yef0k2V08e4gRit8puANlF1er0FwEl0gQ_aem_wEOs3E4Oa6pcqqC6sGsssA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XpNEw04_GO53uzofJgDDGaHWhUcEppjXTkc82E0KwCyxjS67LF4563cMUwg_aem_IlUu_BoalqX5G73OFhgGFA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7RwFzY0rwYNXK121xK89qTquEKGZrXO1taLA3lOHwbDGTYBW2Rjk2H5izqxA_aem_SZKMpaLO8epGh7FT7ALf4w&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7cgGSz2oFblYx0WlnfjDEn5RmHdT8edgyQL-6cx-xh6OeK_Gk7iUv_LnGCBA_aem_-zjD7NTOzURw3xKnSv3RGg&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XpNEw04_GO53uzofJgDDGaHWhUcEppjXTkc82E0KwCyxjS67LF4563cMUwg_aem_IlUu_BoalqX5G73OFhgGFA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XpNEw04_GO53uzofJgDDGaHWhUcEppjXTkc82E0KwCyxjS67LF4563cMUwg_aem_IlUu_BoalqX5G73OFhgGFA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR63eJQdoGj1SVroWqOwqI1S08KaJ_-HJ6RXIKAp5oiGgls6zMuIiIdblT1qTw_aem_JVXt_cZ2prD2TUVFsCU-Hg&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4q4WwYYLl2CgZM2X5xVOChTjH5-FeULKbPH9rOya_Fqq1fXtH_m8iAWXHJfA_aem_zFKuGv2DG3jydNsrTtP-mw&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7cgGSz2oFblYx0WlnfjDEn5RmHdT8edgyQL-6cx-xh6OeK_Gk7iUv_LnGCBA_aem_-zjD7NTOzURw3xKnSv3RGg&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR63eJQdoGj1SVroWqOwqI1S08KaJ_-HJ6RXIKAp5oiGgls6zMuIiIdblT1qTw_aem_JVXt_cZ2prD2TUVFsCU-Hg&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4GF3GqrO-VjQHWG30uoqOjsO3N-R9mvgDNF7Ad9EexyUFplcTNtwc8ELGzIw_aem_oSXdn0ZwAK4k7dnKfRM6fQ&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XpNEw04_GO53uzofJgDDGaHWhUcEppjXTkc82E0KwCyxjS67LF4563cMUwg_aem_IlUu_BoalqX5G73OFhgGFA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4GF3GqrO-VjQHWG30uoqOjsO3N-R9mvgDNF7Ad9EexyUFplcTNtwc8ELGzIw_aem_oSXdn0ZwAK4k7dnKfRM6fQ&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7RwFzY0rwYNXK121xK89qTquEKGZrXO1taLA3lOHwbDGTYBW2Rjk2H5izqxA_aem_SZKMpaLO8epGh7FT7ALf4w&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4q4WwYYLl2CgZM2X5xVOChTjH5-FeULKbPH9rOya_Fqq1fXtH_m8iAWXHJfA_aem_zFKuGv2DG3jydNsrTtP-mw&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75i6UBiQ_2K_XqYAdxazwCScTEtDH5hzNvOA0GJvZrwNzEEH-jERcRSAEc7g_aem_2AErYQ0oWrNGz-HwQyqdmg&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45tWxnWf899C4o_GN6jHonzUwJ3yef0k2V08e4gRit8puANlF1er0FwEl0gQ_aem_wEOs3E4Oa6pcqqC6sGsssA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XpNEw04_GO53uzofJgDDGaHWhUcEppjXTkc82E0KwCyxjS67LF4563cMUwg_aem_IlUu_BoalqX5G73OFhgGFA&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6Q4fhXpIvTj1DciVYNOdt6zqTAq-QpWIK_WpUizeYI9O1Pv2NkMp_NvKzGuNqtDw1ctFI5CVIVqAWw_hEyQ_Jg8UzLueDYNBqWnarxJ17U3hNocM6LtzAJX4FGjEVJ_kbb1iys9ykSzvCR4G6KZyGojR0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão