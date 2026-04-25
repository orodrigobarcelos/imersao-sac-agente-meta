<!-- Fonte: Gerenciar o status do seu objeto de anúncio - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Gerenciar o status do seu objeto de anúncio


A campanha de anúncios, o conjunto de anúncios e os anúncios se enquadram em um dos seguintes tipos de status:


- Live
- Arquivado
- Excluído


Para mais informações, consulte o artigo [Excluído X Arquivado no Blog do desenvolvedor de anúncios](https://developers.facebook.com/ads/blog/post/2014/09/24/deleted-vs-archived/).


## Live


Os objetos de anúncios publicados contêm os seguintes status:


- `ACTIVE`
- `PAUSED`
- `PENDING_REVIEW`
- `CREDIT_CARD_NEEDED`
- `PREAPPROVED`
- `DISABLED`
- `PENDING_PROCESS`
- `WITH_ISSUES`
[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)

## Arquivado


Defina o objeto do anúncio como `ARCHIVED` ao configurar o campo `status` como `ARCHIVED`. Quando um status de objeto for definido como `ARCHIVED`, você poderá continuar a consultar os detalhes e as estatísticas baseadas no ID do objeto. Entretanto, há um máximo de objetos que podem ser arquivados. Então, será necessário respeitar o limite e alterar o status para `DELETED` quando você não precisar mais de um objeto.


Um objeto `ARCHIVED` contém somente dois campos alteráveis: `name` e `status`. Além disso, `status` só pode ser alterado para `DELETED`.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)

## Excluído


Defina o objeto de anúncio como `DELETED`. Isso pode ser feito ao configurar o campo `status` como `DELETED` ou ao enviar um `HTTP DELETE` a esse objeto. Se o status do objeto for definido como `DELETED`, não será possível revertê-lo para `ARCHIVED`.


Se você mantiver o ID do objeto excluído, é possível continuar a recuperar as estatísticas ou os detalhes do objeto consultando o ID do objeto. No entanto, você não pode recuperar os objetos excluídos como um objeto de conexão de um nó ou objeto não excluído. Por exemplo, `<API_VERSION>/<AD_ID>/insights` funciona para um objeto excluído, mas `<API_VERSION>/act_<AD_ACCOUNT_ID>/insights?level=ad` não retorna as estatísticas desse objeto.


Se você excluir um anúncio, ele ainda poderá rastrear impressões, cliques e ações por 28 dias após a data da última veiculação. É possível consultar insights sobre objetos `DELETED` por meio do filtro `ad.effective_status`.


Se você tiver um conjunto com dois anúncios e excluir um deles, as duas consultas a seguir não retornarão os mesmos resultados:

```
https://graph.facebook.com/v25.0/<AD_SET_ID>/insights
https://graph.facebook.com/v25.0/<AD_ID>/insights
```


O conjunto de anúncios retorna as estatísticas dos anúncios excluídos e não excluídos. No entanto, ao consultar anúncios no conjunto de anúncios, você visualiza apenas um anúncio:

```
https://graph.facebook.com/v25.0/<AD_SET_ID>/ads
```


Para evitar esse cenário, você deve excluir os anúncios 28 dias após a última data de veiculação para garantir que as estatísticas não sofram mais alterações. Além disso, você deve armazenar as estatísticas ou os números de identificação desses objetos no seu próprio sistema antes de excluí-los. Esta recomendação é opcional:


- Se o app não mostrar os detalhes das estatísticas ou
- Você não se importa se a soma do detalhamento das estatísticas não corresponde ao objeto principal devido a alguns objetos derivados excluídos.


Exceto `name`, não é possível alterar os campos de um objeto `DELETED`.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)

## Gerenciar status


Normalmente, o status do objeto é gerenciado desta forma:


- Você cria objetos de anúncio, eles são publicados e começam a ser veiculados
- Quando você exclui um objeto, nós o excluímos automaticamente
- Quando você atinge o limite para objetos atingidos, não é mais possível arquivar mais objetos.
- Para reduzir o limite, é necessário mover os objetos excluídos que foram arquivados ao estado `deleted`.


O status dos objetos de anúncio funciona desta maneira para a respectiva hierarquia:


- Se o status de uma campanha estiver definido como `with_issues`, `paused`, `archived`, ou `deleted`, todos os objetos abaixo dela herdarão automaticamente esse status.
- Se você definir uma campanha de anúncios como `deleted`, não será possível recuperar os conjuntos ou anúncios contidos nela sem especificar as identificações correspondentes.
- Caso o status de um anúncio esteja definido como `with_issues`, `paused`, `archived` ou `deleted`, o conjunto de anúncios ou a campanha do anúncio em questão manterá o status original e ficará disponível para recuperação.


Os seguintes limites se aplicam a objetos `ARCHIVED` de uma determinada conta de anúncios:


- 100.000 para campanhas de anúncios
- 100.000 para conjuntos de anúncios
- 100.000 para anúncios


Se você ler as bordas de `archived`, será necessário filtrar especificamente os objetos arquivados, já que não os retornamos por padrão. Caso leia as estatísticas de um objeto de anúncio, incluiremos as estatísticas correspondentes de todos os objetos subordinados, independentemente de ter o status `active`, `archived` ou `deleted`. Portanto, você não precisa do filtro de insighs sobre objetos derivados.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)

## Comparações de status diferentes


Há diferenças entre os objetos com status `ACTIVE` ou `PAUSED` e aqueles com status `ARCHIVED` ou `DELETED`. Estas são as principais diferenças.


| Consulta | Live | Arquivado | Excluído |
| --- | --- | --- | --- |
| Existe no banco de dados | Sim | Sim | Sim |
| Número máximo por conta de anúncio | Com limites | 100.000 | Ilimitado |
| Consulta como bordas sem filtro | Sim | Não | Não |
| Consulta como bordas com filtro de status | Sim para os objetos de status contidos no filtro | Sim se o filtro de status contiver ARCHIVED | Não se o filtro de status não contiver DELETED – se contiver, resultará em erro |
| Consulta pelo próprio número de identificação | Sim | Sim | Sim |
| Estatísticas agregadas em /\<PARENT_OBJECT_ID\>/insights | Sim | Sim | Sim |
| Estatísticas incluídas na lista de resultados de /\<PARENT_OBJECT_ID\>/insights?level=\<OBJECT_LEVEL\> | Sim | Não | Não |
| As estatísticas incluídas na lista de resultados de /\<PARENT_OBJECT_ID\>/insights com filtragem de delivery_info | Sim para os objetos de status contidos no filtro | Sim para os objetos de status contidos no filtro | Não |
| Insights exibidos com /\<OBJECT_ID\>/insights | Sim | Sim | Sim |
| O status pode ser alterado para | Qualquer status válido | DELETED | Não pode ser alterado |


Para definir um anúncio a ser arquivado:

```
curl -X POST \ -d "status=ARCHIVED" \ -d "access_token=<ACCESS_TOKEN>" \ https://graph.facebook.com/v25.0/<AD_ID>
```


Para excluir um anúncio:

```
curl -X POST \ -d "status=DELETED" \ -d "access_token=<ACCESS_TOKEN>" \ https://graph.facebook.com/v25.0/<AD_ID>
```


Para recuperar subobjetos de um objeto publicado, por exemplo, todos os anúncios publicados de uma campanha exceto aqueles com status `ARCHIVED` ou `DELETED`:

```
curl -X GET \ -d 'fields="name"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>/ads
```


Para recuperar os subobjetos `ARCHIVED` de um objeto publicado, por exemplo, todos os anúncios `ARCHIVED` de um conjunto, você precisará do filtro de status:

```
curl -X GET \ -d 'effective_status=[ "ARCHIVED" ]' \ -d 'fields="name"' \ -d 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_CAMPAIGN_ID>/ads
```
[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)[○](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#)Nesta Página[Gerenciar o status do seu objeto de anúncio](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#gerenciar-o-status-do-seu-objeto-de-an-ncio)[Live](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#active)[Arquivado](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#archived)[Excluído](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#deleted)[Gerenciar status](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#how)[Comparações de status diferentes](https://developers.facebook.com/docs/marketing-api/best-practices/manage-your-ad-object-status#comp) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74PR4gqzArdWPJgS024-862njtBHtAiBYcRnflR6Apmcyt8KWSmtZYJNE7Ig_aem_jqqTYg42z1hF_4YQm1Ot7w&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7BJWgRffSu15IRKpx2kfka1Z4vimwyCu_dVP77-xY9ZbcZPRqlSmP32VPI2g_aem_cdW8yY0yn10NU09Y9BPvIg&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR59ohctl6oEOay3aDOtXWK3TVnSMSbKSlzXPDerd1AKH8U6pd0ZKHdk4Rwz9w_aem_5rdirAaRyUfmN04-d8l8yg&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74PR4gqzArdWPJgS024-862njtBHtAiBYcRnflR6Apmcyt8KWSmtZYJNE7Ig_aem_jqqTYg42z1hF_4YQm1Ot7w&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR74PR4gqzArdWPJgS024-862njtBHtAiBYcRnflR6Apmcyt8KWSmtZYJNE7Ig_aem_jqqTYg42z1hF_4YQm1Ot7w&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR59ohctl6oEOay3aDOtXWK3TVnSMSbKSlzXPDerd1AKH8U6pd0ZKHdk4Rwz9w_aem_5rdirAaRyUfmN04-d8l8yg&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5yr2p_eTV2FbqZgeQxvkxtWR2Ni6zEb12MPeZ93Ct3ZUP_3j19BMWRoSYdAA_aem_43oHZm2UNq2kZiVklVv0Nw&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KSwGLT1MOD1H3zast2an3gLGiHLYtaaRvoK-x1AnMLAVvuvGBdrcIboMpUw_aem_SmzkcWoeVYF8oqLpCLTIaA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5yr2p_eTV2FbqZgeQxvkxtWR2Ni6zEb12MPeZ93Ct3ZUP_3j19BMWRoSYdAA_aem_43oHZm2UNq2kZiVklVv0Nw&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5720jvaNfncTSyqufLlObCFZQGjcmQqtNh31xeIFV3TPSGth3n4Af5XWJJfg_aem_BOdsAa-l3Bm7SKFaYCvqnA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4FGiURmTWV8SFLZY0232KnpbvZUAGVgDwG8NRU5vzak0b_DD29SLC517g0EA_aem_fv5LZnHBJ6AFg7E23eBDBA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KSwGLT1MOD1H3zast2an3gLGiHLYtaaRvoK-x1AnMLAVvuvGBdrcIboMpUw_aem_SmzkcWoeVYF8oqLpCLTIaA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR59ohctl6oEOay3aDOtXWK3TVnSMSbKSlzXPDerd1AKH8U6pd0ZKHdk4Rwz9w_aem_5rdirAaRyUfmN04-d8l8yg&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4FGiURmTWV8SFLZY0232KnpbvZUAGVgDwG8NRU5vzak0b_DD29SLC517g0EA_aem_fv5LZnHBJ6AFg7E23eBDBA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7i3cncd1os6uVBOJMoIqg10zT6sxNvHesN2vH2NBijD1p3VYIrVVAsObxrRA_aem_n1gvxHryfz9BFoZS52pvLw&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7BJWgRffSu15IRKpx2kfka1Z4vimwyCu_dVP77-xY9ZbcZPRqlSmP32VPI2g_aem_cdW8yY0yn10NU09Y9BPvIg&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7KSwGLT1MOD1H3zast2an3gLGiHLYtaaRvoK-x1AnMLAVvuvGBdrcIboMpUw_aem_SmzkcWoeVYF8oqLpCLTIaA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6vU-Br5P4uOTN56ahNPdti8bMM-OBLr27Pg9nQoreF1AIFyCUgr2GnuPcbHQ_aem_U3vR3Vz6gyL1l1KagTRDpw&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4FGiURmTWV8SFLZY0232KnpbvZUAGVgDwG8NRU5vzak0b_DD29SLC517g0EA_aem_fv5LZnHBJ6AFg7E23eBDBA&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5yr2p_eTV2FbqZgeQxvkxtWR2Ni6zEb12MPeZ93Ct3ZUP_3j19BMWRoSYdAA_aem_43oHZm2UNq2kZiVklVv0Nw&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6x_KtDgZ9-_cgfJaMHGyIEyxO45JAF9G69fUbg8sYnIZCJPSK8xs_r5GqrhS-oMRB5TaiNzzdtuUGkDgyv23b2K5D_7aUl7dlmyX9u0tSlnxlAORo4EwjL3ur9oKUO8-Rg8l-3fDKaIfLP4xRduc1eDqA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão