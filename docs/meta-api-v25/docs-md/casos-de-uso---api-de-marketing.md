<!-- Fonte: Casos de uso - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/get-started/use-cases -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Casos de uso da API de Marketing


Este documento ensina a personalizar um ou mais dos seguintes casos de uso da API de Marketing que você adicionou ao seu app no [processo de criação do app](https://developers.facebook.com/docs/development/create-an-app/):


- **Capturar e gerenciar leads de anúncios com a API de Marketing**
- **Criar e gerenciar anúncios com a API de Marketing**
- **Mensurar dados de desempenho de anúncios com a API de Marketing**


Os produtos a seguir foram adicionados automaticamente ao app:


- [Login do Facebook para Empresas](https://developers.facebook.com/docs/facebook-login/facebook-login-for-business/) – Autentique os usuários e crie uma configuração para solicitar aos usuários as permissões e os ativos de negócios necessários para que o app funcione corretamente.
- [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-ad-accounts) – Assine as alterações e receba atualizações em tempo real sem fazer chamadas de API.


### Permissões e recursos de casos de uso da API de Marketing


A tabela a seguir mostra as permissões e os recursos disponíveis em cada caso de uso da API de Marketing.


| Recurso ou permissão | Uso da API de Marketing | Ações permitidas |
| --- | --- | --- |
| Acesso Padrão ao Gerenciamento de Anúncios | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. Pode solicitar um limite maior de volume da API de Marketing para qualquer caso de uso* |
| Acesso ao Perfil do Usuário de Ativo de Negócios | Opcional para todos os casos de uso. | Pode ser adicionado a qualquer caso de uso. |
| ads_management | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. |
| ads_read | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. |
| business_management | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. |
| catalog_management | Opcional para criar e gerenciar anúncios. Não está disponível para capturar e gerenciar leads de anúncios. Não está disponível para mensurar o desempenho de anúncios. | Pode ser adicionado para criar e gerenciar anúncios. Não pode ser adicionado para capturar e gerenciar leads de anúncios. Não pode ser adicionado para mensurar o desempenho de anúncios. |
| email | Opcional para todos os casos de uso. | Pode ser adicionado a qualquer caso de uso. |
| leads_retrieval | Obrigatório para capturar e gerenciar leads de anúncios . Não está disponível para criar e gerenciar anúncios. Não está disponível para mensurar o desempenho de anúncios. | Não pode ser removido para capturar e gerenciar leads de anúncios . Não pode ser adicionado para criar e gerenciar anúncios. Não pode ser adicionado para mensurar o desempenho de anúncios. |
| page_manage_ads | Obrigatório para capturar e gerenciar leads de anúncios . Opcional para criar e gerenciar anúncios. Não está disponível para mensurar o desempenho de anúncios. | Não pode ser removido para capturar e gerenciar leads de anúncios . Opcional para criar e gerenciar anúncios. Não pode ser adicionado para mensurar o desempenho de anúncios. |
| page_manage_metadata | Não está disponível para criar e gerenciar anúncios. Opcional para capturar e gerenciar leads de anúncios. Não está disponível para mensurar o desempenho de anúncios. | Não está disponível para criar e gerenciar anúncios. Opcional para capturar e gerenciar leads de anúncios. Não está disponível para mensurar o desempenho de anúncios. |
| pages_read_engagement | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. |
| pages_show_list | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. |
| public_profile | Obrigatório para todos os casos de uso . | Cannot be removed for any use case. Pode aumentar o acesso para qualquer caso de uso.** |
| threads_business_basic | Opcional para criar e gerenciar anúncios. Não está disponível para mensurar o desempenho de anúncios. Não está disponível para capturar e gerenciar leads de anúncios. | Pode ser adicionado para criar e gerenciar anúncios. Não pode ser adicionado para capturar e gerenciar leads de anúncios. Não pode ser adicionado para mensurar o desempenho de anúncios. |


***Solicitar um limite maior de volume da API de Marketing**: para aproveitar um limite de volume mais alto e um número ilimitado de contas de anúncios com o Acesso Padrão ao Gerenciamento de Anúncios, é necessário receber aprovação por meio da análise do app, além de passar por revisões anuais para manter os benefícios. Selecione "Solicitar" para adicionar o Acesso Padrão ao Gerenciamento de Anúncios ao envio para a análise do app. [Saiba mais sobre o Acesso Padrão ao Gerenciamento de Anúncios](https://developers.facebook.com/docs/features-reference/ads-management-standard-access/).


****Aumentar o acesso a este privilégio afetará outros casos de uso**: este privilégio faz parte de mais de um caso de uso no app. Todas as alterações feitas nesse acesso afetarão os casos de uso listados abaixo. Essa alteração pode exigir novos requisitos e processos de análise.
[○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)

## Personalizar caso de uso


### Permissões e recursos


- Caso ainda não esteja na página **Casos de uso** no painel, clique em **Casos de uso**, ou no ícone de lápis, no menu à esquerda.
- Clique em um caso de uso para visualizar os respectivos recursos e permissões disponíveis (obrigatórios e opcionais).
- Clique no botão **Adicionar** à direita de cada permissão ou recurso a ser adicionado. Durante o desenvolvimento, é possível retornar e remover o recurso ou a permissão, caso você perceba que não será usado pelo app.
- Há ações adicionais disponíveis para determinados recursos ou permissões. - Se quiser solicitar um limite de volume mais alto para o recurso Acesso Padrão ao Gerenciamento de Anúncios, clique no botão **Ações** e selecione **Solicitar um limite maior**. - Se estiver com tudo pronto para enviar o app para análise, prossiga para a seção [Análise do app](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#app-review). Caso contrário, clique em **Casos de uso**, ou no ícone de lápis, no menu à esquerda para continuar personalizando os casos de uso. - Para expandir o acesso à permissão `public_profile`, permita que o app atenda a usuários sem função nele ou na empresa conectada a ele clicando no botão **Aumentar o acesso**. - Durante o desenvolvimento, é possível retornar e remover o limite de volume mais alto ou o acesso expandido à permissão `public_profile`, caso você perceba que não será usado pelo app.


### Início rápido


O início rápido da API de Marketing oferece uma experiência prática e guiada de criação de código, orientando você pelo processo de criação de um app em minutos.


- Clique em **Início rápido** no menu esquerdo.
- Clique em **Criar uma campanha de anúncios** a fim de gerar códigos de amostra para criar uma campanha de anúncios.
- Clique em **Avançar** para gerar códigos de amostra usando o [SDK de Negócios da Meta](https://developers.facebook.com/docs/business-sdk/).
- Selecione uma linguagem de código no menu suspenso e clique em **Avançar**.
- Clique em **Criar conta de anúncios de sandbox**. Uma conta de anúncios de sandbox permite que você teste a criação de anúncios e a geração de relatórios por meio da API de Marketing do Facebook de forma gratuita. Essas contas de anúncio não precisam de forma de pagamento, e os anúncios criados não são veiculados. Também é possível criar relatórios com dados fictícios de desempenho de anúncios.
- Na notificação pop-up, adicione as informações necessárias e clique em **Criar**. Depois de selecionar a Página do Facebook, marque a caixa de seleção antes de clicar em criar. 1. A página deve atualizar para mostrar seu sandbox. Clique em **Avançar**.
- Clique em **Gerar token de acesso**.
- Na notificação pop-up, selecione as permissões para associar ao seu token de acesso e clique em **Obter token**. O token é válido por 2 meses. Clique em **Avançar**.
- Um código de amostra com seu token de acesso, sua identificação da conta de anúncios e sua identificação do app é gerado para você criar uma campanha de anúncios. É possível: - **Baixar código de amostra** para adicionar ao seu app - **Usar o Explorador da Graph API** para testar o código na ferramenta de teste da Meta - **Usar o Postman** para testar o código - **Ver mais exemplos** no GitHub
- Clique em **Avançar** para ver as etapas para **executar o código de amostra baixado**.


### Ferramentas


- Clique em **Ferramentas** no menu à esquerda para: - Gerar novos tokens de acesso - Atualizar seu sandbox de conta de anúncio - [Leia a documentação para desenvolvedores da API de Marketing](https://developers.facebook.com/docs/marketing-api/)


### Configurações


Clique em **Configurações** no menu à esquerda e:


- Conecte um portfólio empresarial ao seu app, altere o portfólio atualmente conectado ou inicie o processo de verificação da empresa. É possível adicionar um portfólio empresarial não verificado, mas ele deverá passar pelo processo de verificação antes que você possa veicular anúncios. - Se você não tiver um portfólio empresarial ou quiser criar um novo, clique em **Criar nova conta**.
- [Leia a documentação para desenvolvedores da API de Marketing](https://developers.facebook.com/docs/marketing-api/).
- Confira o [**nível de acesso da API de Anúncios**](https://developers.facebook.com/docs/marketing-api/get-started/authorization/).
- Habilite a [atualização automática da versão da API de Marketing](https://developers.facebook.com/docs/marketing-api/versions/) para atualizar automaticamente as chamadas de API de versões obsoletas da API de Marketing.


### Webhooks (opcional)


A maioria dos desenvolvedores da Meta usa webhooks para receber notificações em tempo real e reduzir o número de chamadas de API, diminuindo assim a chance de atingir a limitação de volume. Os webhooks são adicionados automaticamente, mas são opcionais.


Veja o que fazer para receber webhooks da Meta:


- [Crie um ponto de extremidade](https://developers.facebook.com/docs/marketing-api/get-started/docs/graph-api/webhooks/getting-started) no seu servidor para receber e processar essas notificações HTTP.
- [Envie uma solicitação `POST` para seu app assinar](https://developers.facebook.com/docs/marketing-api/get-started/docs/graph-api/webhooks/getting-started/webhooks-for-ad-account) os webhooks.
- Configure webhooks no painel do app (a etapa listada nesta seção).


Se quiser configurar webhooks para seu caso de uso no painel do app, siga as etapas descritas aqui. Para seguir estas etapas, presumimos que você já tenha acessado o painel **Casos de uso > Personalizar > Personalizar caso de uso** e selecionado a opção **Webhooks** no menu.


- **Selecione o produto**: no menu suspenso, selecione os ativos, como Página e conta de anúncios, sobre os quais você quer receber notificações.
- Adicione seu **URL de retorno de chamada**, isto é, o ponto de extremidade que você criou para receber webhooks.
- Adicione o **token de verificação** que será usado pela Meta como parte da verificação do URL de retorno de chamada.
- É possível adicionar a autenticação do cliente ao processo de verificação ao alterar **TLS em comum** de "Não" para **Sim** (opcional).


**Observação**: para receber notificações de webhook, o app deve estar publicado. Não é preciso passar pela análise do app para usar webhooks.


### Update a use case



If, at any point during development, you want to update a use case, you can return to the dashboard, click **Use cases** (pencil icon) in the left-side menu and click **Customize**.
 [○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)

Se estiver implementando o [Login do Facebook para Empresas](https://developers.facebook.com/docs/facebook-login/facebook-login-for-business/) no app, siga as etapas abaixo.


### Configurações


- Clique em **Login do Facebook para Empresas** no menu à esquerda no Painel de Apps.
- Selecione **Configurações**.
- Adicione o **URI de redirecionamento** e clique em **Verificar URI** para validá-lo.
- Personalize as **Configurações de OAuth do cliente**.
- Adicione o **URL de retorno de chamada de desautorização**.
- Adicione o **URL de solicitação de exclusão de dados**.
- Clique em **Salvar alterações**.


### Início rápido


Use o início rápido para adicionar o Login do Facebook ao seu app.


- Clique em **Início rápido**.
- Selecione e personalize cada plataforma para o app.
- Adicione o **botão Entrar do Facebook** ao app.


### Configurações


Com o recurso opcional Login do Facebook para Empresas, é possível criar várias configurações e apresentá-las a diferentes conjuntos de usuários. Nas configurações, é possível escolher:


- O tipo de login para mostrar aos usuários do app.
- O tipo de token de acesso que deseja solicitar aos clientes da sua empresa (um token de acesso do usuário ou token de acesso do usuário do sistema) e a expiração do token. - Se você escolher token de acesso do usuário, os usuários do app farão login usando a conta pessoal do Facebook. - Se escolher token de acesso do usuário do sistema, os usuários do app serão solicitados a fazer login usando um portfólio empresarial. Isso só será necessário se a configuração precisar de acesso contínuo aos ativos de negócios, como Páginas do Facebook, contas de anúncios ou contas do Instagram.
- Os ativos de negócios que você quer solicitar dos clientes.
- As permissões que os usuários do app precisam conceder.


## Become a tech provider (optional)



Become a Tech Provider if this app will be for clients or other business portfolios.


- Click **Become a Tech Provider**. You will need to: - [Verify your business](https://developers.facebook.com/docs/marketing-api/get-started/docs/development/release/business-verification/) - Verify that your business is [allowed to access another business portfolio's data](https://developers.facebook.com/docs/development/release/access-verification/) - [Complete App Review](https://developers.facebook.com/docs/resp-plat-initiatives/individual-processes/app-review/)
- Click **Yes, I'm a Tech Provider**.


You will be redirected to **Dashboard** which will display **App customization and requirements**. You will see the status for each customization and requirement with the status for each item instead of your app's rate limit usage. Each item must be completed before you can publish your app. When each item is complete the circle icon will be filled in.


- **Add and customize use cases** – Clicking on a use case takes you to **Use cases > Customize > Customize use case** for that use case where you can update the use case or add more use cases.
- [**Prepare and submit for App Review**](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#review). - **Review and complete testing requirements** will take you to **Review > Testing**. - **Business Verification** will take you to **Review > Verification**. - [**App Review**](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#review) will take you to **Review > App Review**.
- [**Publish your app**](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#publish)
 [○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)

## App Review



**Apps that require App Review** – If your app will access data your don't own or manage, it requires App Review before your app users can grant access.


- In the left side menu go to **Review > App Review**. Click the **Edit** button to start your submission. You will see a list of all permissions and features you are requesting, with links to the documentation for each.
- **Complete App Settings** – Click the arrow to the right to add [app settings](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/basic-settings/) such as app icon, privacy policy URL, and app category. **This step must be complete before continuing.**
- **Complete app verification** – For each platform on which your app is available, provide all the necessary details for how a Meta reviewer can log in to your app. - Provide detailed, step-by-step instructions on how a reviewer can test your integration and how you are using the requested permissions or features. Include any testing credentials required to access your integration.
- **How will your app use the advanced access for each permission?** – For each feature and permission your app needs, click the arrow to the right to: - Provide a detailed description of how your app uses that specific permission or feature requested, how it adds value for a person using your app, and why it's necessary for app functionality. - Upload a screen recording that demonstrates how your app will use this permission or feature so Meta reviewers can confirm it is used correctly and does not violate Meta policies. [Learn more.](https://developers.facebook.com/docs/marketing-api/get-started/docs/app-review/submission-guide/screen-recordings/) - Agree that any data your app receives through the permission or feature will be used in accordance with its allowed usage.
- Click the **Submit for Review** button in the lower-right.
 [○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)

## Publicar (opcional)


Só será preciso publicar seu app se ele acessar dados que você não possui ou gerencia ou se ele usar um produto que exija a publicação, como webhooks.


Para publicar um app, você precisará adicionar as configurações necessárias. Além disso, é possível incluir configurações opcionais. Você pode atualizar essas configurações a qualquer momento durante o processo de desenvolvimento.


Também é possível ver o **ID** e a **chave secreta** do app.


### Configurações básicas


**Etapa 1.** Para publicar o app, selecione **Publicar** no menu do lado direito.


**Etapa 2.** Clique em **Ir para as configurações do app** à direita da opção **URL da Política de Privacidade**. Isso levará você para **Configurações do app > Básico**.


**Etapa 3.** Caso ainda não tenha feito isso, adicione as seguintes configurações necessárias:


- **Ícone do app**
- **Categoria**
- **URL da Política de Privacidade**
- **Exclusão de dados do usuário**


Você também pode atualizar as informações de contato da plataforma e do encarregado da proteção dos dados do seu app.


**Etapa 4.** Clique em **Salvar alterações**.


**Etapa 5.** Se você não tiver configurações avançadas para adicionar ou atualizar, clique em **Publicar** no menu do lado direito.


**Etapa 6.** Quando estiver tudo pronto, clique no botão **Publicar** no canto inferior direito.


### Configurações avançadas


**Etapa 1.** Clique em **Configurações do app > Avançado** para atualizar estas configurações:


- Autenticação do app
- Baixar identificadores de usuário
- Restrições do app
- Segurança
- Gerenciador de domínios
- Página do app
- Contas de anúncios
- Lista de permissão do gatekeeper de testador
- Lista de permissão para redirecionamento de compartilhamentos


**Etapa 2.** Clique em **Salvar alterações**.


**Etapa 3.** Clique em **Publicar** no menu do lado direito.


**Etapa 4.** Quando estiver tudo pronto, clique no botão **Publicar** no canto inferior direito.
[○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)

## Veja também


Consulte os seguintes documentos para saber mais sobre o processo de desenvolvimento de apps:


- [Desenvolvimento de apps](https://developers.facebook.com/docs/development)
- [Análise do App](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)
- [Verificação da empresa](https://developers.facebook.com/docs/development/release/business-verification)
- [API de Marketing](https://developers.facebook.com/docs/marketing-apis)
[○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)[○](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#)Nesta Página[Casos de uso da API de Marketing](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#casos-de-uso-da-api-de-marketing)[Personalizar caso de uso](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#customize)[Permissões e recursos](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#permiss-es-e-recursos)[Início rápido](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#in-cio-r-pido)[Ferramentas](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#ferramentas)[Configurações](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#configura--es)[Webhooks (opcional)](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#webhooks--opcional-)[Update a use case](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#update-a-use-case)[Become a tech provider (optional)](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#become-a-tech-provider--optional-)[App Review](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#review)[Publicar (opcional)](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#publicar--opcional-)[Configurações básicas](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#configura--es-b-sicas)[Configurações avançadas](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#configura--es-avan-adas)[Veja também](https://developers.facebook.com/docs/marketing-api/get-started/use-cases#veja-tamb-m) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kShMOvvmVTNKsWYgdl0oPMAhpszmD8TUGcXuteMAM_al3AzytskknUtt36Q_aem_rqJz2mIhevI0Rr2NRMsOVw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kShMOvvmVTNKsWYgdl0oPMAhpszmD8TUGcXuteMAM_al3AzytskknUtt36Q_aem_rqJz2mIhevI0Rr2NRMsOVw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR740auvxs6x91DiIjahRgHvomIEEvzK9psHHZlv3YLKzS-ssp7Tw4vAUchGfg_aem_U5i_ueoC7GtL5qbBOWa9dg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kShMOvvmVTNKsWYgdl0oPMAhpszmD8TUGcXuteMAM_al3AzytskknUtt36Q_aem_rqJz2mIhevI0Rr2NRMsOVw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kShMOvvmVTNKsWYgdl0oPMAhpszmD8TUGcXuteMAM_al3AzytskknUtt36Q_aem_rqJz2mIhevI0Rr2NRMsOVw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62NS-dhnCdITrOjxRdOx6VPQm_BEEcX8Y_ZcH0QpiBdntDLgVYYkP-CMdTRA_aem_QuuHyuaVicIwZJxZkTdnzg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6tNkG1ryDB-GEETsFtnobhuAcnJo5zS4s9iJExziN1uxQtQforFa8UryzTkQ_aem_dlZ0IMmhfOA67o0ta-Wj0A&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR740auvxs6x91DiIjahRgHvomIEEvzK9psHHZlv3YLKzS-ssp7Tw4vAUchGfg_aem_U5i_ueoC7GtL5qbBOWa9dg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6QPVYKmWrNXzhlo02peOAlAM4JqDSIhLTYunGqehb7PnOHwwGcAJCGfvnG1w_aem_ipN8_RsDEFUJTj7LpBgKNg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62XgZZocoSfiSfcIgTPIwlIPnwDkAN_EtGca-ONpdrzpEH5iLyv7SJiquhYg_aem_2lYJ9_UN_SUk7mRwwJDHkg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62XgZZocoSfiSfcIgTPIwlIPnwDkAN_EtGca-ONpdrzpEH5iLyv7SJiquhYg_aem_2lYJ9_UN_SUk7mRwwJDHkg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7b5Iix_0j-oMb8ZdX_jArDZykoNN5_QCPUX3NdpUpbDGXGLthC_4QE17QL6A_aem_48wP8OJIbFesjN_nvetKrg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6k8Yu9JP_QFbtSoHp5NjPovKSDJJNO31-_HzX5TWQGzGFkLgptBYUFEGieWg_aem_KSqjOgBVgBtyb3Gj8fAejw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7b5Iix_0j-oMb8ZdX_jArDZykoNN5_QCPUX3NdpUpbDGXGLthC_4QE17QL6A_aem_48wP8OJIbFesjN_nvetKrg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6k8Yu9JP_QFbtSoHp5NjPovKSDJJNO31-_HzX5TWQGzGFkLgptBYUFEGieWg_aem_KSqjOgBVgBtyb3Gj8fAejw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4kShMOvvmVTNKsWYgdl0oPMAhpszmD8TUGcXuteMAM_al3AzytskknUtt36Q_aem_rqJz2mIhevI0Rr2NRMsOVw&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dTK70byTK3g3rXHt6dklvBRfE6JOoukKKlRRvXaTHsXcq4Ii3HjmWU5iqBg_aem_tTtdFiyPXNUxvrksFgWQ7w&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6dTK70byTK3g3rXHt6dklvBRfE6JOoukKKlRRvXaTHsXcq4Ii3HjmWU5iqBg_aem_tTtdFiyPXNUxvrksFgWQ7w&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR62XgZZocoSfiSfcIgTPIwlIPnwDkAN_EtGca-ONpdrzpEH5iLyv7SJiquhYg_aem_2lYJ9_UN_SUk7mRwwJDHkg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR740auvxs6x91DiIjahRgHvomIEEvzK9psHHZlv3YLKzS-ssp7Tw4vAUchGfg_aem_U5i_ueoC7GtL5qbBOWa9dg&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5HnmK6hfced5WD1mpC-nnbkbP1l2SGOudI0S8K8P1y7z5BnGHFsLAGULhJFC8--EYI1B1WYQJyyf-X5TZ7po64p9XnCyMBYAzNg9mTZWpmjge6DuwZCUElEacxRqMhsz6OPx3QNK6EaZI4jP8xjXOeF8A)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão