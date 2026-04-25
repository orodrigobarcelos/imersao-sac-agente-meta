<!-- Fonte: Configurar contas do Instagram com Páginas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Configurar contas do Instagram com Páginas


Para veicular anúncios no Instagram, você precisa da identificação de uma conta da plataforma. Recomendamos que você acesse essa identificação por meio da [configuração do Gerenciador de Negócios](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager), mas também é possível usar Páginas do Facebook. Você tem duas opções:


- [Contas do Instagram conectadas a Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#via_page): conecte a conta do Instagram a uma Página do Facebook. Essa é uma opção simples para pequenas empresas.
- [Contas do Instagram associadas a Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#pbia): crie uma conta secundária no Instagram associada a uma Página do Facebook.


## Contas do Instagram conectadas a Páginas


Nesta implementação, sua empresa precisa ter uma conta comercial no Instagram. Veja como [configurar uma conta comercial no Instagram](https://www.facebook.com/help/502981923235522). A conta precisa ter uma imagem do perfil e não pode ser uma [conta privada](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F138925576505882&h=AT6Hxo14-iWT2vJbhIk7XYnReETd-OrQTRYxfgNh5RCA5Q1tcg3vOIgxDez65UT0XyOINJ-5jPU-MC2TK_yFW4rpfCuz6B_AQM1TB-IBF-9DHM4bLUCLTEBIn4HyQv24X9IVrRRaAwcWf-ueUraE1Y_kE6IpDQKfILxi6o0V).


Quando a conta do Instagram estiver pronta, conecte-a à Página do Facebook. Consulte [Como conectar ou desconectar uma conta do Instagram da sua Página](https://www.facebook.com/help/1148909221857370). Depois, qualquer pessoa com a função de `advertiser` nessa Página poderá veicular anúncios para a conta.


### Acessar a identificação da conta


Depois de conectar uma conta do Instagram a uma Página, será possível ver a conexão na interface de configurações da Página, mas não visualizar a identificação da conta do Instagram.


Para acessar a identificação da conta do Instagram, faça uma chamada à [API de Contas do Instagram da Página](https://developers.facebook.com/docs/graph-api/reference/page/instagram_accounts/) usando o token de acesso da Página:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "fields=id,username,profile_pic" \
"https://graph.facebook.com/<API_VERSION>/<PAGE_ID>/instagram_accounts"
```


O resultado contém um objeto de conta do Instagram, incluindo campos como `id`, `username` e `profile_pic`. Salve a `id` para usar nos seus anúncios.


### Criar anúncios


Será possível usar qualquer conta de anúncios (seja de propriedade de um indivíduo ou de uma empresa, desde que você tenha acesso) para criar anúncios destinados a contas do Instagram conectadas a uma Página. Existem algumas limitações:


- Nenhuma função é necessária na conta do Instagram, mas você precisa ter pelo menos uma função de `advertiser` na Página relacionada.
- Quando fornecer um criativo do anúncio, informe também `instagram_user_id` e `page_id`. Se a `instagram_user_id` for a identificação da conta do Instagram de uma conta conectada à Página, use a identificação da Página como `page_id`. Não é possível usar uma conta do Instagram conectada à Página com outra Página em um criativo do anúncio.


Uma Página pode ter apenas uma conta do Instagram conectada a ela, assim como uma única [conta do Instagram associada](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#pbia).
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#)

## Contas do Instagram associadas à Páginas


Normalmente, você cria contas do Instagram para veicular anúncios, fazer posts ou comentários usando o perfil e construir sua comunidade de forma orgânica. Alguns anunciantes preferem não criar e manter contas do Instagram para simplificar o processo ou pretendem veicular anúncios e conteúdo orgânico usando contas diferentes na plataforma.


Nesse caso, você pode usar contas do Instagram associadas a uma Página (PBIA, pelas iniciais em inglês). É possível criar essas contas via API e usá-las para exibir anúncios no Instagram. Essa abordagem funciona como se você estivesse veiculando anúncios para uma Página do Facebook, mas criamos uma conta secundária no Instagram para exibir a publicidade.


### Criar a PBIA


Para criar uma conta do Instagram associada a uma Página do Facebook, é preciso ter pelo menos a função de `ADVERTISER` na Página em questão. As funções de `MANAGER` ou `CONTENT_CREATOR` também são aceitas.


Além disso, sua Página não deve ter uma PBIA já configurada. Isso porque cada Página pode ter apenas uma PBIA. Caso você já tenha uma PBIA, use a conta existente. Qualquer pessoa com acesso à Página também poderá acessar a PBIA. [Verifique se uma determinada Página já possui uma PBIA antes de criar uma nova](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#read).


Para criar uma PBIA, envie uma solicitação `POST` para:

```
curl \
-F "access_token=<ACCESS_TOKEN>"\
"https://graph.facebook.com/<API_VERSION>/<PAGE_ID>/page_backed_instagram_accounts"
```


Em caso de sucesso, a operação retornará a identificação da conta do Instagram. Caso uma Página já tenha uma PBIA, a chamada retornará a identificação da conta existente. Salve a identificação para veicular seus anúncios.


### Ler a PBIA


Para verificar se uma Página do Facebook possui uma PBIA, envie uma solicitação `GET`:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "fields=username,profile_pic" \
"https://graph.facebook.com/<API_VERSION>/<PAGE_ID>/page_backed_instagram_accounts"
```


Caso já exista uma PBIA, a operação retornará o objeto da conta do Instagram, conforme [descrito na configuração do Gerenciador de Negócios](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#account_api). O objeto inclui uma `ID` que pode ser usada para veicular anúncios no Instagram.


Se não houver uma PBIA configurada, a API retornará uma resposta vazia.


### Usar a PBIA no criativo do anúncio


Após a criação da PBIA, você poderá usar a identificação como `instagram_user_id` no seu criativo do anúncio, da mesma forma que faz com outros tipos de contas do Instagram.


Não é necessário atribuir nenhuma conta de anúncios à PBIA. Ao fornecer o criativo do anúncio usando uma PBIA, você pode utilizar qualquer conta de anúncios à qual tenha acesso, desde que possua pelo menos a função de `ADVERTISER` na Página associada à PBIA.


A `page_id` do criativo do anúncio precisa corresponder à Página associada a essa PBIA.


Ao usar uma conta de anúncios que não pertence a uma empresa via Gerenciador de Negócios, se a Página tiver uma conta do Instagram conectada a ela, não será possível usar a PBIA dessa Página para criar anúncios. Será preciso usar a conta do Instagram conectada à Página. Caso você crie anúncios para uma conta de anúncios pertencente a uma empresa, essa restrição não será aplicada.


A conta do Instagram tem o mesmo nome e foto do perfil da Página relacionada. Se alguém alterar o nome ou a foto do perfil da Página, atualizaremos automaticamente a conta secundária do Instagram.


**Não é possível acessar essa conta do Instagram para gerenciar posts.** Veja o que fazer para visualizar ou gerenciar os "comentários" e "curtidas" dos seus posts de anúncios:


- Acesse o `instagram_permalink_url`[do seu criativo do anúncio](https://developers.facebook.com/docs/marketing-api/guides/instagramads/ads_management#adpreview). Depois, visualize o post. Não é possível adicionar posts ou comentários com esse perfil da PBIA.
- Use o [Gerenciador de Anúncios](https://business.facebook.com/adsmanager/manage) para ver e excluir comentários no post do anúncio.
- Use a [API de Moderação de Posts de Anúncios do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/post_moderation) para ver e excluir comentários no post do anúncio. Não é possível adicionar posts ou comentários com essa API.
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#)

## Comparação


| Requisitos | Configuração do Gerenciador de Negócios | Conta do Instagram da Página | Conta do Instagram associada à Página |
| --- | --- | --- | --- |
| O anunciante precisa ter uma conta no Instagram | Sim | Sim | Não |
| O anunciante precisa ter o Gerenciador de Negócios configurado | Sim | Não | Não |
| Requer algumas etapas manuais nas interfaces do Facebook | Sim, para reivindicar uma conta do Instagram no Gerenciador de Negócios. | Sim, para reivindicar uma conta do Instagram na Página. | Não |
| É possível adicionar posts (mídia) | Sim, com o app | Sim, com o app | Não |
| É possível comentar como o perfil do Instagram | Sim, com o app ou com as APIs de Marketing . | Sim, com o app ou com as APIs de Marketing . | Não |
| É possível ler ou excluir comentários em posts de anúncios (mídia) usando as APIs . | Sim | Sim | Sim |
| É possível veicular anúncios com uma conta de anúncios de propriedade de um usuário | Não | Sim | Sim |
| É possível veicular anúncios com uma conta de anúncios de propriedade de uma empresa | Sim | Sim | Sim |

[○](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#)

## Connection Objects



Once you create an Instagram account, you cannot use [Connection Objects](https://developers.facebook.com/docs/marketing-api/connectionobjects) to view these accounts. You should use assets under business instead of `connection objects`.


For Instagram accounts, use the following endpoints:


- `{business_id}/instagram_accounts`
- `act_{adaccount_id}/instagram_accounts`
- `{page_id}/instagram_accounts`
 [○](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#)[○](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#)Nesta Página[Configurar contas do Instagram com Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#configurar-contas-do-instagram-com-p-ginas)[Contas do Instagram conectadas a Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#via_page)[Acessar a identificação da conta](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#acessar-a-identifica--o-da-conta)[Criar anúncios](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#criar-an-ncios)[Contas do Instagram associadas à Páginas](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#pbia)[Criar a PBIA](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#pbia_create)[Ler a PBIA](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#read)[Usar a PBIA no criativo do anúncio](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#use-in-creative)[Comparação](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#compara--o)[Connection Objects](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#co) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-Qk7tj0HtWj73w46J9xuNDQhOkw3dQF43GcV_5C61-Hvf3caDBmJi7fuzMg_aem_XaaijVfVpbkKgiDNdELxxQ&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5-Qk7tj0HtWj73w46J9xuNDQhOkw3dQF43GcV_5C61-Hvf3caDBmJi7fuzMg_aem_XaaijVfVpbkKgiDNdELxxQ&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vYqocsgKWGnGYhEqUfOpcLRGscNUI-lKX316v7XT-ABQGbu7qghX5I0PsSA_aem_seZOOjqFXFpY6sAi3rPYdg&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7036bqyeV8FikxueVds7aW61sL2M91EiUG2DJidYVOMqxjwKZJLYCu-zirnw_aem_de7EvQsmR6OsjpcHk99w7g&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BdJxaI_M9SakJEk83AfNpHcICHTc6G79C32ncs-Wqiuztvw-uBzMaHXhgpQ_aem_4KMukXG9M64IE7y91CfX9g&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQg7IGs9vISaUmcf_PxH9V4As3f_u8XqDPRUthjrXFg6bcQUQQrKj9HUBfw_aem_5bWBbraraxjDG_v1bR7FNw&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5OteabntbrP1Kq0MwQh4ftga9c8wM3O3AcOtNVZbKNifrBThu6bEM3vJ6VyQ_aem_60kFYC0k7uFwgr3NXwOLug&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7036bqyeV8FikxueVds7aW61sL2M91EiUG2DJidYVOMqxjwKZJLYCu-zirnw_aem_de7EvQsmR6OsjpcHk99w7g&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BdJxaI_M9SakJEk83AfNpHcICHTc6G79C32ncs-Wqiuztvw-uBzMaHXhgpQ_aem_4KMukXG9M64IE7y91CfX9g&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR42aAkQKbVrLYUHSr6qnEv64mNoIbGC888-0v6lVhtHAS6t0nEBStdaiqVldg_aem_3E0XKw5Uv_Trfhh-VSWnGA&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5OteabntbrP1Kq0MwQh4ftga9c8wM3O3AcOtNVZbKNifrBThu6bEM3vJ6VyQ_aem_60kFYC0k7uFwgr3NXwOLug&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7-eYlVA_mGmwB0Xedt_RbnjroUDTFBfaGA8DFWtFjU0KWKKnsgQO8pVOJN6g_aem_ltAZyOUDejkDRZxH3wEfvg&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UvHuIhNioZxCw62IubAsWe1jkEQeB2SVzhZSXJdFok2kKIeift2pJflMd7Q_aem_ah_MbJxGFXuVgB09h7_yFQ&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jQOneWjAP2qyjaBm7RFHpCsooIExfn_LcdXkO7jqLJ2lNzrMTGyefBXQFiA_aem_q7dXD2ENBT29NxfnIkTBXg&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7jQOneWjAP2qyjaBm7RFHpCsooIExfn_LcdXkO7jqLJ2lNzrMTGyefBXQFiA_aem_q7dXD2ENBT29NxfnIkTBXg&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR42aAkQKbVrLYUHSr6qnEv64mNoIbGC888-0v6lVhtHAS6t0nEBStdaiqVldg_aem_3E0XKw5Uv_Trfhh-VSWnGA&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6BdJxaI_M9SakJEk83AfNpHcICHTc6G79C32ncs-Wqiuztvw-uBzMaHXhgpQ_aem_4KMukXG9M64IE7y91CfX9g&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7vQg7IGs9vISaUmcf_PxH9V4As3f_u8XqDPRUthjrXFg6bcQUQQrKj9HUBfw_aem_5bWBbraraxjDG_v1bR7FNw&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5vYqocsgKWGnGYhEqUfOpcLRGscNUI-lKX316v7XT-ABQGbu7qghX5I0PsSA_aem_seZOOjqFXFpY6sAi3rPYdg&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5OteabntbrP1Kq0MwQh4ftga9c8wM3O3AcOtNVZbKNifrBThu6bEM3vJ6VyQ_aem_60kFYC0k7uFwgr3NXwOLug&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7Q7-RoQIRBrtQ8NpHSs7Sau5KpYKHgUmZNpaEHdC4-Yz54sIk2XTtyWD2s914_wbk430NvjT1ptNQR34Ky4HpQNQ6gsHOO2NAd-jTxBxH6tEgY6sd_tT_S_tH5aQYXP6ZOqWyYdcNAqPtVKIhR0YqAqXc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão