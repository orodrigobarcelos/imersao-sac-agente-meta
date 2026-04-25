<!-- Fonte: Autorização - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/get-started/authorization -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Autorização


O processo de autorização verifica os usuários e apps que terão acesso à API de Marketing e concede permissões a eles.


## Funções do app


No painel do seu app, é possível definir funções para você ou para os membros da equipe, como Administrador, Desenvolvedor, Testador, conforme necessário.


**Observação:** dependendo do caso de uso pretendido, talvez seja necessário enviar o app para análise a fim de receber permissões específicas relacionadas ao gerenciamento de anúncios.
[○](https://developers.facebook.com/docs/marketing-api/get-started/authorization#)

## Níveis de acesso, permissões e recursos


Os apps de empresa estão sujeitos a uma camada adicional de autorização da Graph API chamada [níveis de acesso](https://developers.facebook.com/docs/graph-api/overview/access-levels). Durante o processo de [análise](https://developers.facebook.com/docs/app-review), seu app também deverá solicitar permissões e recursos específicos.


Todos os desenvolvedores devem seguir os [Termos da Plataforma](https://developers.facebook.com/terms) e as [Políticas do Desenvolvedor](https://developers.facebook.com/devpolicy) da Meta. **As chamadas em QUALQUER nível de acesso são feitas em relação aos dados de produção.**


### Nível de acesso à API de Marketing e do Acesso Padrão ao Gerenciamento de Anúncios


As permissões e os recursos para apps contam com dois níveis de acesso diferentes: o acesso padrão e o acesso avançado. **Observação:** nesse contexto, o termo "acesso padrão" não está relacionado ao recurso [Acesso Padrão ao Gerenciamento de Anúncios](https://developers.facebook.com/docs/features-reference/ads-management-standard-access). O acesso avançado do Acesso Padrão ao Gerenciamento de Anúncios ainda exige que o app seja aprovado no processo de análise.


#### Mapeamento do acesso à API de Marketing e do Acesso Padrão ao Gerenciamento de Anúncios


| Acesso à API de Marketing | [Acesso Padrão ao Gerenciamento de Anúncios](https://developers.facebook.com/docs/features-reference/ads-management-standard-access) | Ação |
| --- | --- | --- |
| Acesso ao desenvolvimento | Acesso padrão | Por padrão |
| Acesso padrão | Acesso avançado | Solicitar no Painel de Apps |


Para verificar seu nível de acesso atual, navegue até **Painel de Apps** > **Análise do app** > **Permissões e recursos**.


### Permissões e recursos


#### Permissões


As permissões que precisam ser solicitadas mudam de acordo com a API que você quer acessar.


Caso o app gerencie somente sua conta de anúncios, o acesso padrão e as permissões `ads_read` e `ads_management` serão suficientes. Se o app gerenciar contas de anúncios de outras pessoas, será necessário ter acesso avançado e as permissões `ads_read` e/ou `ads_management`. Veja todas as [permissões disponíveis para apps de empresa](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#available-permissions-2).


#### Recursos


Os recursos que devem ser solicitados mudam conforme a maneira como você pretende usar nossas APIs. Se você gerencia anúncios, um recurso comum a ser solicitado é o Acesso Padrão ao Gerenciamento de Anúncios. Veja [todos os recursos disponíveis para apps de empresa](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#available-features-2).


##### Níveis de acesso ao recurso


| Nível de acesso ao recurso | Descrição |
| --- | --- |
| Acesso padrão | O acesso padrão será aprovado automaticamente para todas as permissões e todos os recursos disponíveis para os apps de negócios. Caso você seja iniciante, use essa opção. Você pode criar fluxos de trabalho de ponta a ponta antes de solicitar permissões totais e pode acessar um número ilimitado de contas de anúncios. Algumas chamadas de API não estão disponíveis com o acesso padrão, porque podem pertencer a várias contas ou porque não é possível identificar a conta afetada de modo programático. |
| Acesso avançado | O acesso avançado deve ser aprovado para cada permissão ou recurso por meio do processo de análise do app . Para solicitar o acesso avançado, acesse o Painel de Apps e clique em Análise do app \> Permissões e recursos .; Encontre a permissão ou o recurso que você quer acessar e clique em Solicitar acesso avançado em Ação . É possível selecionar um ou mais recursos. Depois de selecionar suas opções, clique em Continuar a solicitação . Então, uma tela que fornece orientações para o processo de envio será exibida. Após o envio das informações, a Meta responderá com uma mensagem de aprovação ou recusa, com informações adicionais se o app não estiver qualificado para o acesso padrão. Se você tiver aprovação para o acesso avançado, será preciso realizar as seguintes ações para manter esse status: Ter feito ao menos 1.500 chamadas da API de Marketing com sucesso nos últimos 15 dias.; Ter feito chamadas da API de Marketing com uma taxa de erro menor do que 15% nos últimos 15 dias. |


##### Descrição dos níveis de acesso


A tabela abaixo mostra como os níveis de acesso avançado e padrão afetam o recurso Acesso Padrão ao Gerenciamento de Anúncios.


|  | Acesso padrão | Acesso avançado |
| --- | --- | --- |
| Limites de contas | Gerencie um número ilimitado de contas de anúncios. Administradores ou desenvolvedores de apps podem fazer chamadas de API em nome de administradores de contas de anúncios ou anunciantes. | Gerencie um número ilimitado de contas de anúncios se tiver as permissões ads_read ou ads_management da conta de anúncios. |
| Limites de volume | Volumes extremamente limitados por conta de anúncio. Somente para desenvolvimento. Não para apps em produção veiculando para anunciantes publicados. | Volumes ligeiramente limitados por conta de anúncios. |
| Gerenciador de Negócios | Acesso limitado às APIs do Gerenciador de Negócios e de Catálogo . Sem acesso do Gerenciador de Negócios para administrar contas de anúncios, permissões de usuários e Páginas. | Acesso a todas as APIs do Gerenciador de Negócios e de Catálogo . |
| Usuário do sistema | É possível criar um usuário do sistema e um usuário do sistema administrador. | É possível criar 10 usuários do sistema e um usuário do sistema administrador. |
| Criação da Página | Não é possível criar Páginas por meio da API. | Não é possível criar Páginas por meio da API. |


##### Obter acesso avançado


Para obter o acesso avançado do Acesso Padrão ao Gerenciamento de Anúncios, seu app precisa atender a estes requisitos:


- Ter feito ao menos 1.500 chamadas da API de Marketing com sucesso nos últimos 15 dias.
- Ter feito chamadas da API de Marketing com uma taxa de erro menor do que 15% nos últimos 15 dias.


Se estiver gerenciando os anúncios de outra pessoa, use o parâmetro `scope` para solicitar que ela forneça as permissões `ads_management` ou `ads_read`. Seu app obterá acesso quando ela clicar em **Permitir**.

```
https://www.facebook.com/v25.0/dialog/oauth? client_id=<YOUR_APP_ID> &redirect_uri=<YOUR_URL> &scope=ads_management
```


**Observação:** ao preencher o campo `YOUR_URL`, coloque uma `/` à direita (por exemplo, http://www.facebook.com/).


##### Exemplos de caso de uso


| Caso de uso | O que solicitar |
| --- | --- |
| Você quer ler e gerenciar anúncios das próprias contas ou de contas de anúncios para as quais tenha recebido acesso. | Permissão: ads_management; Recurso: Acesso Padrão ao Gerenciamento de Anúncios |
| Você quer ler relatórios de anúncios das próprias contas ou de contas de anúncios para as quais tenha recebido acesso. | Permissão: ads_read; Recurso: Acesso Padrão ao Gerenciamento de Anúncios |
| Você quer obter relatórios de anúncios de um conjunto de clientes, bem como ler e gerenciar anúncios de outro conjunto de clientes. | Permissões: ads_management e ads_read; Recurso: Acesso Padrão ao Gerenciamento de Anúncios |

[○](https://developers.facebook.com/docs/marketing-api/get-started/authorization#)

## Verificação da empresa


A verificação da empresa é um processo que nos permite verificar sua identidade como entidade corporativa, o que será necessário caso o app acesse dados sensíveis. Saiba mais sobre o processo de [verificação da empresa](https://developers.facebook.com/docs/apps/business-verification).
[○](https://developers.facebook.com/docs/marketing-api/get-started/authorization#)

## Saiba mais


- [Permissions Reference for Meta Technologies APIs](https://developers.facebook.com/docs/permissions)
[○](https://developers.facebook.com/docs/marketing-api/get-started/authorization#)[○](https://developers.facebook.com/docs/marketing-api/get-started/authorization#)Nesta Página[Autorização](https://developers.facebook.com/docs/marketing-api/get-started/authorization#autoriza--o)[Funções do app](https://developers.facebook.com/docs/marketing-api/get-started/authorization#fun--es-do-app)[Níveis de acesso, permissões e recursos](https://developers.facebook.com/docs/marketing-api/get-started/authorization#n-veis-de-acesso--permiss-es-e-recursos)[Nível de acesso à API de Marketing e do Acesso Padrão ao Gerenciamento de Anúncios](https://developers.facebook.com/docs/marketing-api/get-started/authorization#n-vel-de-acesso---api-de-marketing-e-do-acesso-padr-o-ao-gerenciamento-de-an-ncios)[Permissões e recursos](https://developers.facebook.com/docs/marketing-api/get-started/authorization#permiss-es-e-recursos)[Verificação da empresa](https://developers.facebook.com/docs/marketing-api/get-started/authorization#verifica--o-da-empresa)[Saiba mais](https://developers.facebook.com/docs/marketing-api/get-started/authorization#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RltJB01vqDB9ZvdRot6xTNwAbzDcSwXkKMlyIW4SEDZRawU0Ceid4GZhO0w_aem_mN-2FAKV1LVauVL1PY3Z6w&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4yFWUqP02fD2zxvSF7fro1KMR5UnPZZSD9dIqiVnqTlcIsNrNwjrwPFxjFcQ_aem_rR31nRc0tfvq2VnP87UXMQ&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5g_nE2CmTk7JiusVfZI7z-HKd-E6XIllqlEqKHZNgULN_3zjqHaJMt6vkitw_aem_2V2GpCeNEpcdVLqI_sZg8g&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6AS6NtYMe-xxxscoVY3Fuh02o6L50lRueX0MiblX5MdTFL6wUWsMPXAnIcKw_aem_jz-etYZVgsrEWGJ_xrMacA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4yFWUqP02fD2zxvSF7fro1KMR5UnPZZSD9dIqiVnqTlcIsNrNwjrwPFxjFcQ_aem_rR31nRc0tfvq2VnP87UXMQ&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6AS6NtYMe-xxxscoVY3Fuh02o6L50lRueX0MiblX5MdTFL6wUWsMPXAnIcKw_aem_jz-etYZVgsrEWGJ_xrMacA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QGvSGC0Il9zdR_S81sbJf-CARVbD3emeVFyPmFYeRQkM_tpBDm7rTxEY9VA_aem_HxXHwgKRc9xP8AIY4lt7pg&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QGvSGC0Il9zdR_S81sbJf-CARVbD3emeVFyPmFYeRQkM_tpBDm7rTxEY9VA_aem_HxXHwgKRc9xP8AIY4lt7pg&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6n2qBnaeGXpk7TZybYAxV5cZSTkl1jK1K-ja7vBMX0fzBZXwOKXYYOjBRbIQ_aem_yvfbi3A7GfPlyF54f5P3Vw&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fObMpujLSvXswsdVlBEtRwomBhiv0tlFsDMm8fLjcoZx8gNbG_60XetfQFw_aem_S-DZj-CcDp4ftmUHSvjVlw&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6AS6NtYMe-xxxscoVY3Fuh02o6L50lRueX0MiblX5MdTFL6wUWsMPXAnIcKw_aem_jz-etYZVgsrEWGJ_xrMacA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RltJB01vqDB9ZvdRot6xTNwAbzDcSwXkKMlyIW4SEDZRawU0Ceid4GZhO0w_aem_mN-2FAKV1LVauVL1PY3Z6w&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-VtaFT2fRSDrM417NQFGWWKnaYb0hOKqyNhrJnVQQIm6gcO1Epeype9jV5w_aem_a6z8qBullZY9eG5WbAmBzA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-VtaFT2fRSDrM417NQFGWWKnaYb0hOKqyNhrJnVQQIm6gcO1Epeype9jV5w_aem_a6z8qBullZY9eG5WbAmBzA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fObMpujLSvXswsdVlBEtRwomBhiv0tlFsDMm8fLjcoZx8gNbG_60XetfQFw_aem_S-DZj-CcDp4ftmUHSvjVlw&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4yFWUqP02fD2zxvSF7fro1KMR5UnPZZSD9dIqiVnqTlcIsNrNwjrwPFxjFcQ_aem_rR31nRc0tfvq2VnP87UXMQ&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6n2qBnaeGXpk7TZybYAxV5cZSTkl1jK1K-ja7vBMX0fzBZXwOKXYYOjBRbIQ_aem_yvfbi3A7GfPlyF54f5P3Vw&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fObMpujLSvXswsdVlBEtRwomBhiv0tlFsDMm8fLjcoZx8gNbG_60XetfQFw_aem_S-DZj-CcDp4ftmUHSvjVlw&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7g6R18fzhhVU9c67R6eE9d3BySjjY8y9hGrlK47F9kEfEgws78FvZJOwY-HQ_aem_hPRwrHd4XBUuOaNF6WX3vA&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RltJB01vqDB9ZvdRot6xTNwAbzDcSwXkKMlyIW4SEDZRawU0Ceid4GZhO0w_aem_mN-2FAKV1LVauVL1PY3Z6w&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6TpTh1VBuiWP8Us6TLzVR8XUBgVEgvB85tfejsJU5qEUftElJherDsUklv29jL6q00HY6Dyj5PpEscbtQc-i6oI7_Nj2H67mQ7chDI92UBxTGXIPCbia4G3DlIwenth7fjvElhG9auT960ZIakWaDmej0)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão