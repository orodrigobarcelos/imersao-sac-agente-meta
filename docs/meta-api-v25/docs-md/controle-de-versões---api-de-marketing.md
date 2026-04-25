<!-- Fonte: Controle de versões - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/overview/versioning -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Controle de versões


A versão atual da API de Marketing é `v25.0`.


A plataforma do Facebook tem um modelo de [controle de versões](https://developers.facebook.com/docs/apps/versions) principal e um ampliado. Com o controle de versões da API de Marketing, todas as alterações importantes serão lançadas em uma nova versão. As diversas versões das APIs de Marketing ou dos SDKs podem coexistir com funcionalidades diferentes em cada versão.


Os desenvolvedores devem saber com antecedência quando uma API de Marketing ou um SDK sofrerá alterações. Embora haja uma janela de 90 dias para adotar as alterações, a escolha de como e quando passar para a nova versão é sua.


## Cronograma de versões


Quando uma nova versão da API de Marketing é lançada, mantemos a compatibilidade com a versão anterior por pelo menos 90 dias. Isso significa que você terá esse período de carência para atualizar sua versão. Durante esses 90 dias, você poderá fazer chamadas para a versão atual e a obsoleta. Depois desse prazo, será necessário atualizar para a nova versão. Ao término do período de carência, a versão obsoleta deixará de funcionar. Depois que uma versão ficar indisponível, as chamadas feitas para ela poderão falhar ou ser atualizadas para a próxima versão disponível.


Por exemplo, a API de Marketing v17.0 foi lançada em 23 de maio de 2023, e a v16.0 expirou em 6 de fevereiro de 2024, fornecendo ao menos 90 dias para fazer a atualização para a nova versão.


Veja um exemplo de cronograma. Talvez não lancemos uma nova versão no final do período de carência de 90 dias da versão anterior. No exemplo, a v16.0 fica obsoleta um pouco antes do lançamento da v18.0:


No caso dos SDKs, uma versão está sempre disponível no estado atual como um pacote para download. Depois do fim de vida útil, o SDK continuará se baseando nas APIs de Marketing ou em métodos que não funcionam mais; por isso, presuma que ele não funcionará mais no fim de vida útil.
[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)

## Como fazer solicitações de controle de versões


Todos os pontos de extremidade da API de Marketing estão disponíveis por meio de um caminho com controle de versões. Pré-anexe o identificador de versão no início do caminho da solicitação. Por exemplo:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/me/adaccounts"
```


Isso funciona para todas as versões, neste formato geral:

```
https://graph.facebook.com/v{n}/{request-path}
```


Nele, `n` é a versão necessária. Confira a lista completa das versões disponíveis no [Registro de alterações](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog). Todas as [referências da API de Marketing](https://developers.facebook.com/docs/ads-api/) fornecem informações por versão.
[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)

## Migrações


As migrações são somente para casos especiais, nos quais as alterações que precisam ser feitas não podem entrar no controle de versões. Normalmente, isso ocorrerá se o modelo de dados básicos tiver sido alterado. Migrações aplicam-se a todas as versões.


As migrações que ainda estão em andamento aparecem listadas na nossa [página de migrações](https://developers.facebook.com/docs/apps/migrations). As migrações têm uma janela de pelo menos 90 dias, durante a qual você deverá migrar o app. Uma vez iniciada a janela, o comportamento pós-migração se tornará o padrão para os novos apps. Depois, quando a janela de migração tiver sido concluída, o comportamento pré-migração não estará mais disponível.


### Como gerenciar migrações por meio da Graph API


As migrações podem ser gerenciadas por meio do [campo de migrações do nó `/app`](https://developers.facebook.com/docs/graph-api/reference/app#migrations):


É possível [fazer uma chamada de atualização na borda](https://developers.facebook.com/docs/graph-api/reference/app#migrations) para ativar e desativar migrações.


### Como gerenciar migrações por meio do Painel de Apps


Você pode ativar e desativar as migrações disponíveis no [Painel de Apps](https://developers.facebook.com/apps), em **Configurações** > **Migrações**. Vale ressaltar que a lista de migrações pode não ser a mesma da imagem abaixo, já que as migrações disponíveis são específicas para cada app, em momentos diferentes. Caso você veja uma migração `Use Graph API v2.0 by default`, ela será para Graph API somente, não para a API de Marketing.


### Ativação temporária de migrações no lado do cliente


Em vez de ativar a migração pelo Painel de Apps ou pela API de Marketing, é possível adicionar uma sinalização especial definindo a migração para chamadas da API de Marketing. A sinalização é chamada de `migrations_override` e exige que você defina um blob JSON que descreva as migrações a serem ativadas ou desativadas. Por exemplo, se fosse fazer uma chamada bruta, você poderia passar:

```
http://graph.facebook.com/path?
  migrations_override={"migration1":true, "migration2":false}
```


Com isso, é possível fazer chamadas à nova API de Marketing por meio de atualizações do cliente, em vez de fazer todos atualizarem para fazer chamadas a ela ao mesmo tempo. Isso também é útil para depuração.


Você pode encontrar os nomes dessas migrações no nó [`/app` mencionado acima](https://developers.facebook.com/docs/marketing-api/overview/versioning#manage-migrations-via-graph-api).
[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)

## Atualização automática da versão


Devido à rápida rotatividade das versões da API de Marketing, que mudam aproximadamente a cada quatro meses, estamos simplificando o processo de atualização. A partir de maio de 2024, habilitaremos o recurso de atualização automática da versão para os pontos de extremidade da API de Marketing que não são afetados entre as versões. Isso significa que, entre uma versão prestes a ficar obsoleta e a próxima disponível, se nenhum ponto de extremidade for afetado, a plataforma atualizará a chamada para a versão a ser lançada, em vez de gerar uma falha na solicitação diretamente. Essa mudança foi pensada para garantir uma experiência mais tranquila e eficiente com a API.


Por exemplo, no dia 14 de maio de 2024, a v17.0 ficará obsoleta. De acordo com o [registro de alterações da v18.0](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/version18.0), os seguintes pontos de extremidade serão afetados:


- `POST /act_{ad-account-id}/reachfrequencypredictions`
- `GET /act_{ad-account-id}/reachestimate`
- `GET /act_{ad-account-id}/delivery_estimate`
- `POST /act_{ad-account-id}/adsets`
- `POST /{adset-id}`
- `POST /act_{ad-account-id}/saved_audiences`
- `POST /{saved-audience-id}`
- `POST /act_{ad-account-id}/credit_cards`


Caso seu app faça uma chamada `POST /{adset-id}` com a v17.0 depois que ela ficar obsoleta no dia 14 de maio de 2024, essa solicitação da API falhará, já que a atualização automática não se aplica aos pontos de extremidade afetados pela próxima versão disponível (v18.0).


Se o app fizer uma chamada `GET /{ad-account-id}/insights` com a v17.0 depois que ela ficar obsoleta, a plataforma atualizará sua solicitação para a próxima versão disponível (v18.0).


**Observação**: caso seu app já esteja fazendo chamadas com versões posteriores à v17.0, nada mudará na data em que a versão ficar obsoleta.


Para verificar os pontos de extremidade afetados em cada versão, consulte o [registro de alterações da API de Marketing](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog).
[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)

## Perguntas frequentes


### Cronograma de versões

[What if I don't specify a version for the Marketing API?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_427988163217772)

We refer to this as an **unversioned** call. Unversioned calls are invalid and will fail when made against Marketing API endpoints.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_427988163217772)[Can I make calls to versions older than the current version?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_292743143916083)

You can call the version of the Marketing API that was the latest available when the app was created, as long as it has not been deprecated. It can also make calls to any newer, undeprecated versions launched after the app is created.


Starting May 14, 2024, if a deprecated version is provided, the platform may upgrade selected endpoints to the next available version instead of failing the request. To learn more about the behavior, refer to [Marketing API Auto-version upgrade](https://developers.facebook.com/docs/marketing-api/overview/versioning#version-auto-upgrade).


For example:


- If your app was created before the launch of v17.0, while v16.0 was available, then it will be able to make calls to v16.0 until the expiration date of that version. After v16.0 has been deprecated, calls to v16.0 will fail.
- If your app was created after v17.0 was released, it will be able to make calls to v17.0 until the expiration date of that version, and any subsequent versions (v18.0, etc) until their expiration dates. After v17.0 has been deprecated, calls to v17.0 will fail.
- Your app will not be able to make calls to v16.0, since 1) that was before your app was created and 2) that version is deprecated and calls to v16.0 may fail or be upgraded to the next available version.


If an app was not used - to make any Marketing API calls or requests - after being created, it will not have the ability to use those versions if any newer version is launched. Here's another example to explain this:


- If your app was created while v16.0 was the latest version available, but not used until after v17.0 had launched, it will only be to use v17.0, and not v16.0.
- If your app was created while v16.0 was the latest version available, and then used before v17.0 had launched, it will still be able to use v16.0 even after the launch of v17.0.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_292743143916083)[How is this different from Platform API versioning?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_1089302298789612)

There are a few differences between how Marketing API and the rest of Graph API. For the details on Platform API versioning, see [Graph API, Versioning](https://developers.facebook.com/docs/apps/versions).


- Marketing API is versioned on a 90-day deprecation schedule, whereas Platform API has core and extended APIs with a 2 year guarantee for core APIs.
- Marketing API does not support unversioned calls. If you do not specify a working version in your call, it fails.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_1089302298789612)

### Como fazer solicitações de controle de versões

[How is this different than migrations?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_799762958198668)

With migrations, you set migration on or off in App Dashboard, as described in the [Migrations](https://developers.facebook.com/docs/marketing-api/overview/versioning#migrations) section. With versioning, we are making Marketing API functionality more transparent by moving the setting into the endpoint:

```
https://graph.facebook.com/v{n}/{request-path}
```


You can know what behavior to expect out without having to manually visit your app's migration panel.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_799762958198668)

### Atualização automática da versão

[Does the upgrade only apply to the version to be deprecated and the next available version?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_3545761025675240)

The upgrade will apply on any deprecated version to the next available version. This means hypothetically if your app is making calls to v15.0 after v16.0 is deprecated, the call will also be upgraded to v17.0 if the endpoint is not listed as affected endpoint on both v16.0 and v17.0.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_3545761025675240)[Does this mean developers don't need to do anything during version deprecation?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_2254842978219172)

No. We highly encourage developers to perform version upgrades before a version gets deprecated for the following reasons


- You may still need to manually upgrade endpoints being impacted by next version.
- You might want to upgrade to newer versions to benefit from new features instead of the lowest available version.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_2254842978219172)[How can I find out which endpoints will not be auto-upgraded?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_968773524857672)

You can look up affected endpoints from [Marketing API Changelog](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_968773524857672)[How can I opt-out of this behavior?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_2322796654576360)

You can disable the version auto-upgrade via the **Marketing API Version** setting under **Marketing API App Product Page** > **Settings**.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_2322796654576360)[Can I check if any specific API call has been auto-upgraded?](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_328062030285054)

If an API call targets a version that has been deprecated and has been automatically upgraded, an API response header is included for any call that has been auto-upgraded.


Example notification header

```
X-Ad-Api-Version-Warning: 'X-Ad-Api-Version-Warning: 'The call has been auto-upgraded to vXXX as vXXX has been deprecated''
```
[Link permanente](https://developers.facebook.com/docs/marketing-api/overview/versioning#faq_328062030285054)[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)[○](https://developers.facebook.com/docs/marketing-api/overview/versioning#)Nesta Página[Controle de versões](https://developers.facebook.com/docs/marketing-api/overview/versioning#controle-de-vers-es)[Cronograma de versões](https://developers.facebook.com/docs/marketing-api/overview/versioning#cronograma-de-vers-es)[Como fazer solicitações de controle de versões](https://developers.facebook.com/docs/marketing-api/overview/versioning#como-fazer-solicita--es-de-controle-de-vers-es)[Migrações](https://developers.facebook.com/docs/marketing-api/overview/versioning#migra--es)[Como gerenciar migrações por meio da Graph API](https://developers.facebook.com/docs/marketing-api/overview/versioning#como-gerenciar-migra--es-por-meio-da-graph-api)[Como gerenciar migrações por meio do Painel de Apps](https://developers.facebook.com/docs/marketing-api/overview/versioning#como-gerenciar-migra--es-por-meio-do-painel-de-apps)[Ativação temporária de migrações no lado do cliente](https://developers.facebook.com/docs/marketing-api/overview/versioning#ativa--o-tempor-ria-de-migra--es-no-lado-do-cliente)[Atualização automática da versão](https://developers.facebook.com/docs/marketing-api/overview/versioning#atualiza--o-autom-tica-da-vers-o)[Perguntas frequentes](https://developers.facebook.com/docs/marketing-api/overview/versioning#perguntas-frequentes)[Cronograma de versões](https://developers.facebook.com/docs/marketing-api/overview/versioning#cronograma-de-vers-es-2)[Como fazer solicitações de controle de versões](https://developers.facebook.com/docs/marketing-api/overview/versioning#como-fazer-solicita--es-de-controle-de-vers-es-2)[Atualização automática da versão](https://developers.facebook.com/docs/marketing-api/overview/versioning#atualiza--o-autom-tica-da-vers-o-2) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR69VBtqfWUeS6-qO_H3FZ36CUaL_8rd6oD4S8qVswbycKhUeZMVpa0VYjnp4w_aem_huU0UxDM1SaP__bYLuw8Dg&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Areqc4gwav0HulC1FIRmNpJmU5N6rKiSssCfjsElBtWfvOn0NayVwfXQsjg_aem_X0n4Uj7JVPIzV7DexzXjGQ&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR55bYxnNnWd3SgGJYSZcm0t9wGfxnWFGHsbo8F7qgxLM99CLhQRQ7hQC5WTXA_aem_3_i7gA4ec6cDdfs8Vr_Plg&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5HPHfLIlVpHnGJ0DkldOSWVHCIdfYxkm35MsCQg-lDdYuA_5jNJPb_iv8YEg_aem_OVSgUWQlWML62Ml21iO5oA&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR55bYxnNnWd3SgGJYSZcm0t9wGfxnWFGHsbo8F7qgxLM99CLhQRQ7hQC5WTXA_aem_3_i7gA4ec6cDdfs8Vr_Plg&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7QIwIaWipwV7zZHeXyajWqLsXjjwTEbulrItZp4dX3UKelWhVIqN3p2DDvdQ_aem_TUYEwuSgqxkyMYmwUtyVaQ&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR55bYxnNnWd3SgGJYSZcm0t9wGfxnWFGHsbo8F7qgxLM99CLhQRQ7hQC5WTXA_aem_3_i7gA4ec6cDdfs8Vr_Plg&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR71YJ60rhuIkGVIkABW_v5qS818D_V-SiWGGGNwj0_n6ZcUs0Xltgn_hp62bg_aem_XHENy1q-UHkI7oR2LMNRLA&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR71YJ60rhuIkGVIkABW_v5qS818D_V-SiWGGGNwj0_n6ZcUs0Xltgn_hp62bg_aem_XHENy1q-UHkI7oR2LMNRLA&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5HPHfLIlVpHnGJ0DkldOSWVHCIdfYxkm35MsCQg-lDdYuA_5jNJPb_iv8YEg_aem_OVSgUWQlWML62Ml21iO5oA&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5HPHfLIlVpHnGJ0DkldOSWVHCIdfYxkm35MsCQg-lDdYuA_5jNJPb_iv8YEg_aem_OVSgUWQlWML62Ml21iO5oA&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Areqc4gwav0HulC1FIRmNpJmU5N6rKiSssCfjsElBtWfvOn0NayVwfXQsjg_aem_X0n4Uj7JVPIzV7DexzXjGQ&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6j9k20PHNRyRIlxM6Gyt5leuCawHnJxqyjYftsy1wFucYn9RYWles2pSyEIg_aem_7s31FPEYkBmkd9SN-APWIg&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Areqc4gwav0HulC1FIRmNpJmU5N6rKiSssCfjsElBtWfvOn0NayVwfXQsjg_aem_X0n4Uj7JVPIzV7DexzXjGQ&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mnjHtMuOJ9-MyGd4oK-Am6lsV8YiynuAEQFeYKSP25EVgLNEGRbXZRifTsg_aem_ig71NPxqZ_Hyu2GyiPGT2Q&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5191Ga7QZHb02HNXWioXrmYSY-jlxil66L3340m74jF0YQHARUbG7KugDAxkQGz0RFaivtu0PWC0Pzf483bAAlQVRobTbkV30l4Www_rfvraIsTMeWOf-dm1EWUlH6qxGiVzKw6TBu_p8ARvNSX4A0lx8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão