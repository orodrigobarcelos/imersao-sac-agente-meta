<!-- Fonte: Anúncios no Threads - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios no Threads


Algumas atualizações nos anúncios do Threads podem não estar disponíveis para todos os usuários no momento.


Para veicular anúncios no Threads, você precisa da identificação de uma conta do app. Há duas maneiras de fazer isso:


- [Conta do Threads associada ao Instagram:](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-associated-threads-accounts) uma conta do Threads tem uma conta do Instagram associada com um nome de usuário correspondente no mesmo portfólio empresarial. - **Observação:** as empresas com uma conta do Threads associada ao Instagram criada antes de 29 de janeiro de 2026 terão a conta do Threads adicionada automaticamente ao portfólio empresarial com o mesmo acesso e permissões de usuário gerenciadas na conta do Instagram. Os desenvolvedores podem continuar usando as mesmas identificações de contas do Threads associadas ao Instagram que estavam utilizando antes de 29 de janeiro de 2026. As novas contas do Threads criadas após 29 de janeiro de 2026 precisarão ser adicionadas manualmente ao portfólio empresarial e gerenciadas como outros tipos de conta.
- [Conta do Threads associada ao Instagram:](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-backed-threads-accounts) uma conta do Instagram veicula anúncios em nome de uma conta do Threads criada para essa finalidade.


Verifique se a sua conta do Instagram tem a configuração correta para [veicular anúncios do Instagram.](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account)


### Limitações


- Não é possível veicular anúncios no Threads sem uma conta do Instagram associada ou uma conta do Threads associada ao Instagram. Além disso, não é possível veicular anúncios no Threads se a conta do Instagram associada não puder veicular anúncios no Instagram.
- Você precisa ter pelo menos a função de anunciante na [Página vinculada à sua conta do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account#via_page). As funções de gerenciador e criador de conteúdo também são aceitas. Ou é preciso que a conta do Instagram esteja [conectada a uma conta comercial](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#claim_account) na qual você tenha as funções apropriadas.
- Uma conta do Instagram pode ter um link apenas para uma conta do Threads ([conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-associated-threads-accounts)) no portfólio empresarial, bem como apenas uma [conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-backed-threads-accounts). Verifique se uma conta do Instagram tem uma [conta do Threads associada a ela](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#get-the-instagram-associated-threads-account-id) ou uma [conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#get-the-instagram-backed-threads-account-id) antes de tentar criar uma nova. Se já houver, use a conta existente do tipo desejado.
- Como decidimos manter um volume baixo de anúncios no Threads à medida que fazemos testes e descobertas, esperamos que a veiculação de anúncios também seja baixa. Caso sua campanha seja veiculada no Threads, você verá isso nos relatórios de detalhamento por posicionamento.
- Ao criar anúncios no Threads, só é possível usar imagens e vídeos como formato de mídia.
- Não é possível criar anúncios usando um post existente do Threads.


## Contas do Threads conectadas ao Instagram


### Permissões


Para fazer chamadas de API com uma conta do Threads associada ao Instagram, você precisará de um token de acesso de usuário com as seguintes permissões:


- `instagram_basic`
- `threads_business_basic`
- `pages_read_engagement`


Caso uma função tenha sido concedida ao usuário do app por meio do Gerenciador de Negócios na Página conectada à conta profissional do Instagram do usuário, seu app também precisará de uma destas permissões:


- `ads_management`
- `ads_read`


**Observação:** qualquer pessoa com acesso à criação de anúncios no Instagram a partir da conta do Instagram pode criar anúncios do Threads usando a conta do Threads associada ao Instagram.


### Antes de começar


Confira os requisitos:


- Uma empresa com a configuração correta para [identidades de anunciante em anúncios do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/pages-ig-account).
- Uma conta do Instagram com uma imagem de perfil que não seja uma [conta privada](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F138925576505882&h=AT6_6-eyOROjro5Zf1DXPGyV32GmbWFjtu93AUOeToQQgEridvpwUUVHYPTJuWs_dj6aeXdfmaUGgcChS0gTOc7iTfSn78IKoBneckB4ndhX-ZZxcKUbxOpDIeLGuTcpkFrw0Taqg5YlJP-lqKqNpav9wy8) e que tenha as permissões de anunciante apropriadas (consulte [Como conectar minha Página do Facebook e minha conta do Instagram?](https://www.facebook.com/help/1148909221857370)).
- Uma conta do Threads tem uma conta do Instagram associada com um nome de usuário correspondente no mesmo portfólio empresarial. Para configurar isso, siga as [instruções para portfólio empresarial do Threads](https://www.facebook.com/business/help/1888797071720635). As empresas com uma conta do Threads associada ao Instagram criada antes de 29 de janeiro de 2026 terão a conta do Threads adicionada automaticamente ao portfólio empresarial com o mesmo acesso e permissões de usuário gerenciadas na conta do Instagram. As novas contas do Threads criadas após 29 de janeiro de 2026 precisarão ser adicionadas manualmente ao portfólio empresarial e gerenciadas como outros tipos de conta.


### Como receber a identificação da conta do Threads associada ao Instagram


Depois de conectar uma conta do Threads a uma conta válida do Instagram, você pode chamar o [ponto de extremidade `/<IG_USER_ID>/connected_threads_user`](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/connected_threads_user) para receber a identificação da conta.


#### Exemplo de solicitação


```
curl -G \ -d "access_token=<ACCESS_TOKEN>"\ -d "fields=threads_user_id" \ "https://graph.facebook.com/v25.0/<IG_USER_ID>/connected_threads_user"
```


O resultado deve ser um objeto de conta do Threads contendo apenas o `threads_user_id`. Salve o `threads_user_id` para usar nos seus anúncios.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#)

## Contas do Threads associadas ao Instagram


Se não tiver um perfil no Threads, você ainda poderá criar e veicular anúncios na plataforma usando uma conta do Threads associada ao Instagram.


Essas contas são criadas com a API e funcionam como se você estivesse veiculando anúncios *para* uma conta do Threads. Entretanto, uma conta de modelo do Threads é criada especificamente para veicular esses anúncios.


As contas do Threads criadas dessa maneira não poderão ser usadas para gerenciar posts.


### Como criar uma conta do Threads associada ao Instagram


Você pode criar uma conta do Threads associada ao Instagram enviando uma solicitação `POST` ao [ponto de extremidade `/<IG_USER_ID>/instagram_backed_threads_user`](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user#edges).


#### Exemplo de solicitação


```
curl \ -F "access_token=<ACCESS_TOKEN>"\ "https://graph.facebook.com/v25.0/<IG_USER_ID>/instagram_backed_threads_user"
```


Caso a operação seja bem-sucedida, ela retornará a identificação da conta do Threads. Se uma conta do Instagram já tiver uma conta do Threads associada à plataforma, a chamada retornará a identificação dessa conta do Threads. Salve a identificação retornada para veicular seus anúncios.


### Como obter a identificação da conta do Threads associada ao Instagram


Para verificar se uma conta do Instagram tem uma conta do Threads vinculada, envie uma solicitação `GET` ao ponto de extremidade `/<IG_USER_ID>/instagram_backed_threads_user`.


#### Exemplo de solicitação


```
curl -G \ -d "access_token=<ACCESS_TOKEN>"\ -d "fields=threads_user_id" \ "https://graph.facebook.com/v25.0/<IG_USER_ID>/instagram_backed_threads_user"
```


Se já houver uma conta, a operação retornará um objeto de conta do Threads. O objeto inclui um `threads_user_id` que pode ser usado para veicular anúncios no Threads. Se não houver uma conta do Threads associada ao Instagram já configurada, a API retornará uma resposta vazia.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#)

## Criativos de anúncio com contas do Threads


### Como usar contas do Threads associadas ao Instagram em anúncios


Você pode usar qualquer conta de anúncios, seja de propriedade de um indivíduo ou de uma empresa (desde que tenha acesso), para criar anúncios em contas do Threads conectadas ao Instagram.


Ao criar um criativo do anúncio, forneça `threads_user_id` e `instagram_user_id`. O `instagram_user_id` do criativo do anúncio deve corresponder à conta do Instagram associada a essa conta do Threads e ter o mesmo nome de usuário do portfólio empresarial. As empresas com uma conta do Threads associada ao Instagram criada antes de 29 de janeiro de 2026 terão a conta do Threads adicionada automaticamente ao portfólio empresarial com o mesmo acesso e permissões de usuário gerenciadas na conta do Instagram. Os desenvolvedores podem continuar usando as mesmas identificações de contas do Threads associadas ao Instagram que estavam utilizando antes de 29 de janeiro de 2026. As novas contas do Threads criadas após 29 de janeiro de 2026 precisarão ser adicionadas manualmente ao portfólio empresarial e gerenciadas como outros tipos de conta.


### Como usar contas do Threads associadas ao Instagram em anúncios


Não é necessário atribuir contas de anúncios à conta do Threads associada ao Instagram. Ao fornecer um criativo do anúncio usando uma conta do Threads associada ao Instagram, você poderá usar quaisquer contas de anúncios às quais tem acesso.


Quando uma conta do Threads associada ao Instagram for criada, você poderá usar a identificação dessa conta como o `threads_user_id` no criativo do anúncio, assim como faz com outros tipos de contas do Instagram. O `instagram_user_id` do criativo do anúncio deve corresponder à conta do Instagram associada a essa conta do Threads vinculada ao Instagram.


### Exemplos


Enquanto o `instagram_user_id` precisa ser incluído no campo `object_story_spec`, o `threads_user_id` pode ser incluído no campo `object_story_spec` ou em um nível superior da chamada de API.


#### Incluído no campo `object_story_spec`


```
curl -X POST \ -F { "name": "test", "object_story_spec": { "link_data": { "link": "<LINK_URL>", "call_to_action": { "type": "WATCH_MORE", "value": {} }, "message": "<MESSAGE_TEXT>", "image_hash": "<IMAGE_HASH>" }, "instagram_user_id": "<IG_USER_ID>", "threads_user_id": "<THREADS_USER_ID>", "page_id": "<PAGE_ID>" } } \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


#### Incluído em um nível superior


```
curl -X POST \ - F { "name": "test", "object_story_spec": { "link_data": { "link": "<LINK_URL>", "call_to_action": { "type": "WATCH_MORE", "value": {} }, "message": "<MESSAGE_TEXT>", "image_hash": "<IMAGE_HASH>" }, "instagram_user_id": "<IG_USER_ID>", "page_id": "<PAGE_ID>" }, "threads_user_id": "<THREADS_USER_ID>" } \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#)

## Próximas etapas


- [Criação de anúncios do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation)
- [Anúncios em carrossel do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation/carousel-ads)
- [Insights sobre anúncios do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/insights)
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#)Nesta Página[Anúncios no Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#an-ncios-no-threads)[Contas do Threads conectadas ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#contas-do-threads-conectadas-ao-instagram)[Permissões](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#permiss-es)[Antes de começar](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#antes-de-come-ar)[Como receber a identificação da conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#como-receber-a-identifica--o-da-conta-do-threads-associada-ao-instagram)[Contas do Threads associadas ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#contas-do-threads-associadas-ao-instagram)[Como criar uma conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#como-criar-uma-conta-do-threads-associada-ao-instagram)[Como obter a identificação da conta do Threads associada ao Instagram](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#como-obter-a-identifica--o-da-conta-do-threads-associada-ao-instagram)[Criativos de anúncio com contas do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#criativos-de-an-ncio-com-contas-do-threads)[Como usar contas do Threads associadas ao Instagram em anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#como-usar-contas-do-threads-associadas-ao-instagram-em-an-ncios)[Exemplos](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#exemplos)[Próximas etapas](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#pr-ximas-etapas) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75OphNWN3U4sBXtqQHYJNwzmturRNySul7H1yr09S4bDvilQn57rhxgJQsrQ_aem_MKv4dxg3DY4l4ENYVdPTmA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rXByD9AF892Ncyv9Yr1SAygedOXyhgtYLiG7Rwej8aPIzvngu52H5UVJ60w_aem_VGha_3Bk9ou1klRb9xIiEA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR551hpexdYEOWI-v2P-cvNWzSmc277jrquZV9OWz4KbYR_H7Iue8ah-EwoT1g_aem_LWOOfoYEqxdSUosh1x3URA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OEW2dGRO85eHi1OyW2HrzQLmqzZ4MgIPX78_7_WJUTQPLFrndhmtrD8Yp9A_aem_4Wp99CzXZafVgvJxSiBRCg&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-Jg9EpxKjvxUj0ALXLwh-kq1fpbsRcyvnKBxQhUJTSXRyGdso6cxxv6L6aw_aem_B7DD0HiHWIPmHEnDPehLvw&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OEW2dGRO85eHi1OyW2HrzQLmqzZ4MgIPX78_7_WJUTQPLFrndhmtrD8Yp9A_aem_4Wp99CzXZafVgvJxSiBRCg&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6OEW2dGRO85eHi1OyW2HrzQLmqzZ4MgIPX78_7_WJUTQPLFrndhmtrD8Yp9A_aem_4Wp99CzXZafVgvJxSiBRCg&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rXByD9AF892Ncyv9Yr1SAygedOXyhgtYLiG7Rwej8aPIzvngu52H5UVJ60w_aem_VGha_3Bk9ou1klRb9xIiEA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GkLooNZLCTSBGEZPXsh58S7LgXEHZmXVOfvMlCysl2izpK9xCa1lA-x_F3g_aem_5gas8Mq9ZFTLza07kPBrIg&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rXByD9AF892Ncyv9Yr1SAygedOXyhgtYLiG7Rwej8aPIzvngu52H5UVJ60w_aem_VGha_3Bk9ou1klRb9xIiEA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-Jg9EpxKjvxUj0ALXLwh-kq1fpbsRcyvnKBxQhUJTSXRyGdso6cxxv6L6aw_aem_B7DD0HiHWIPmHEnDPehLvw&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mW3ELzfX1GqjT3j-Zsx2P6aewhjS3YFJe0I0oaZRvr7ExlzsZ4t26Njg0YQ_aem__5GdLBRo3R86G7U6qxkfgA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mW3ELzfX1GqjT3j-Zsx2P6aewhjS3YFJe0I0oaZRvr7ExlzsZ4t26Njg0YQ_aem__5GdLBRo3R86G7U6qxkfgA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rXByD9AF892Ncyv9Yr1SAygedOXyhgtYLiG7Rwej8aPIzvngu52H5UVJ60w_aem_VGha_3Bk9ou1klRb9xIiEA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR75OphNWN3U4sBXtqQHYJNwzmturRNySul7H1yr09S4bDvilQn57rhxgJQsrQ_aem_MKv4dxg3DY4l4ENYVdPTmA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7F9pkvqH4AR9FCRKEKdu9CNeStGyvo6MHUabZRduK182gaZb2aPx23-zYfrQ_aem_MIrcFmhevWv2goUNEmT6xw&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR551hpexdYEOWI-v2P-cvNWzSmc277jrquZV9OWz4KbYR_H7Iue8ah-EwoT1g_aem_LWOOfoYEqxdSUosh1x3URA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rXByD9AF892Ncyv9Yr1SAygedOXyhgtYLiG7Rwej8aPIzvngu52H5UVJ60w_aem_VGha_3Bk9ou1klRb9xIiEA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-Jg9EpxKjvxUj0ALXLwh-kq1fpbsRcyvnKBxQhUJTSXRyGdso6cxxv6L6aw_aem_B7DD0HiHWIPmHEnDPehLvw&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mW3ELzfX1GqjT3j-Zsx2P6aewhjS3YFJe0I0oaZRvr7ExlzsZ4t26Njg0YQ_aem__5GdLBRo3R86G7U6qxkfgA&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KoAlc5xbD8-MV69tH2iAdVbqLJYmx_SID4sBQlVu2Oc4mnF_plWEh8NS3ybzKZ0pg4wMskMitLhj2BfMwov807H4GhonCKmld1SUlDRubhKL4jwJbky7D9bmnGPPo6aZSLfSHDwT4cPzIpqwYh4K9vcw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão