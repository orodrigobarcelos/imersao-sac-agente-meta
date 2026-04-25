<!-- Fonte: Criação de anúncios do Threads - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Criação de anúncios do Threads


Algumas atualizações nos anúncios do Threads podem não estar disponíveis para todos os usuários no momento.


Com a API de Marketing, você pode criar, mensurar e otimizar anúncios no feed principal do Threads. Para criar anúncios:


- [Etapa 1: receber a identificação da conta do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-1)
- [Etapa 2: criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-2)
- [Etapa 3: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-3) — escolha um `placement` que inclua o Threads. A adição do `stream` do Instagram é um pré-requisito para quem quer selecionar o `threads_stream` do Threads como um posicionamento.
- [Etapa 4: fornecer um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-4)
- [Etapa 5: programar a veiculação de anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-5)


### Limitações


- Há um limite de mil caracteres em legendas de anúncios que fazem o direcionamento para o Threads. Se você ultrapassar esse limite, a solicitação de criação será bem-sucedida no Instagram, mas o anúncio não será veiculado no Threads.
- As imagens do Threads devem ter pelo menos 500 pixels de largura.
- Só é possível incluir 30 hashtags por anúncio.


## Etapa 1: receber a identificação da conta do Threads


Você precisa saber a identificação da sua conta do Threads antes de começar a criar anúncios. Há diferentes maneiras de descobrir essa identificação, dependendo do tipo de conta:


- [Conta do Threads conectada ao Instagram:](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-associated-threads-accounts) configure uma conexão do app Threads por meio do fluxo OAuth e [receba a identificação da conta do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/#get-the-instagram-associated-threads-account-id). Salve a identificação retornada para usar nos anúncios.
- [Conta do Threads associada ao Instagram:](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#instagram-backed-threads-accounts)[configure a conta do Threads usando a API](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads#create-an-instagram-backed-threads-account), depois [receba a identificação dessa conta](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/#get-the-instagram-backed-threads-account-id). Salve a identificação retornada para usar nos anúncios.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)

## Etapa 2: criar uma campanha de anúncios


A criação de objetos de anúncio no Threads é feita da mesma forma que no Instagram e no Facebook. Para começar, [crie uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-campaign) e especifique o objetivo.


Os objetivos compatíveis com o Threads variam de acordo com o posicionamento escolhido para o anúncio:


| Posicionamento do anúncio | Objetivos compatíveis |
| --- | --- |
| Anúncios no feed do Threads ( threads_stream ) | OUTCOME_AWARENESS , OUTCOME_TRAFFIC , OUTCOME_ENGAGEMENT , OUTCOME_SALES |

[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)

## Etapa 3: criar um conjunto de anúncios


[Crie um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-set) com as preferências a seguir:


- [Meta de otimização](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt): as opções de meta disponíveis dependem do objetivo definido no nível da campanha. Confira as [regras de validação](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group#objective-validation).
- [Opções de direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference): você pode usar todas as opções de direcionamento padrão para suas campanhas, incluindo [opções de direcionamento básico](https://developers.facebook.com/docs/marketing-api/audiences/reference), [públicos personalizados](https://developers.facebook.com/docs/marketing-api/custom-audience-targeting) e [públicos semelhantes](https://developers.facebook.com/docs/marketing-api/lookalike-audience-targeting).
- [Orçamento](https://developers.facebook.com/docs/marketing-api/bidding/overview/budgets)
- [Evento de cobrança](https://developers.facebook.com/docs/marketing-api/bidding/overview/billing-events): o `billing_event` depende da `optimization_goal` escolhida. Confira as [regras de validação](https://developers.facebook.com/docs/marketing-api/bidding/overview#opt-goal-validation).
- [Programação da veiculação de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling)


### Posicionamento


Para veicular anúncios no Threads, inclua `instagram` e `threads` em `publisher_platforms` no seu conjunto de anúncios. Depois, use o posicionamento `threads_stream` do Threads. Não se esqueça de selecionar também o posicionamento `stream` do Instagram. Se você escolher diversas plataformas, a Meta otimizará a veiculação com base no público-alvo em cada uma delas usando a [otimização de posicionamento](https://developers.facebook.com/docs/marketing-api/audiences/reference/placement-targeting).


### Exemplos


#### Criar um conjunto de anúncios com Threads como posicionamento


```
curl \ -F 'name=Threads Adset' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "publisher_platforms": ["instagram", "threads"], "user_os": ["iOS"] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


#### Criar um conjunto de anúncios com o `threads_stream` do Threads como posicionamento direcionado


```
curl \ -F 'name=Threads Adset' \ -F 'optimization_goal=LINK_CLICKS' \ -F 'billing_event=IMPRESSIONS' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={ "geo_locations": {"countries":["US"]}, "publisher_platforms": ["instagram", "threads"], "instagram_positions": ["stream"], "threads_positions": ["threads_stream"], "user_os": ["iOS"] }' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)

## Etapa 4: fornecer um criativo do anúncio


Para que os criativos sejam usados com um posicionamento do Threads e o posicionamento necessário do Instagram, forneça a [identificação da sua conta do Instagram](https://developers.facebook.com/docs/marketing-api/guides/instagramads/get-started#account-id), a [identificação da sua conta do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-1) e a identificação da sua conta do Facebook.


Quando você [fornece um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad-creative), criamos um post não publicado. Para ver esse post, consulte o feed qualificado para promoção usando a identificação da Página. **As informações da sua Página não aparecem em nenhum lugar no anúncio do Threads.**


Se a conta do Threads estiver associada a uma conta do Instagram no portfólio empresarial (ou seja, nomes de usuário correspondentes) ou for uma conta do Threads associada ao Instagram, será preciso usar essa conta do Instagram.


**Observação:** as empresas com uma conta do Threads associada ao Instagram criada antes de 29 de janeiro de 2026 terão a conta do Threads adicionada automaticamente ao portfólio empresarial com o mesmo acesso e permissões de usuário gerenciadas na conta do Instagram. Os desenvolvedores podem continuar usando as mesmas identificações de contas do Threads associadas ao Instagram que estavam utilizando antes de 29 de janeiro de 2026. As novas contas do Threads criadas após 29 de janeiro de 2026 precisarão ser adicionadas manualmente ao portfólio empresarial e gerenciadas como outros tipos de conta.


O Threads é compatível com a criação de anúncios de imagem, vídeo e imagem em carrossel (use as mesmas etapas para a [criação de anúncios no Instagram](https://developers.facebook.com/docs/instagram/ads-api/reference/media-requirements)). Consulte a seção [Requisitos de mídia](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#media-requirements) para saber mais.


Quando novas configurações de mídia e formatos de anúncios se tornarem compatíveis com o Threads, tanto as campanhas existentes quanto as recém-criadas que os usarem aproveitarão automaticamente seu perfil do Threads ou conta do Instagram para veicular no `threads_stream`, caso esse posicionamento esteja incluído. Você pode analisar e atualizar seus posicionamentos de anúncio quando quiser.


### Hashtags


Só é possível incluir 30 hashtags por anúncio.


### Requisitos de mídia


#### Legendas


Há um limite de mil caracteres em legendas de anúncios que fazem o direcionamento para o Threads. Se você ultrapassar esse limite, a solicitação de criação será bem-sucedida no Instagram, mas o anúncio não será veiculado no Threads. O recomendado é usar de 80 a 160 caracteres.


**Observação**: não é possível usar hashtags e URLs na legenda.


#### Requisitos de imagem


##### Taxa de proporção


Os formatos de 1.91:1 a 9:16 são compatíveis. As imagens com uma proporção maior que 4:5 serão cortadas e centralizadas para 4:5. Imagens com uma proporção de 1.91:1 a 4:5 não serão cortadas ou alteradas.


##### Tamanho


As imagens do Threads devem ter pelo menos 500 pixels de largura.


#### Requisitos de vídeo


##### Taxa de proporção


Os formatos de 1.91:1 a 9:16 são compatíveis. Os vídeos com uma proporção maior que 4:5 serão cortados e centralizados para 4:5. Imagens com uma proporção de 1.91:1 a 4:5 não serão cortadas ou alteradas.


#### Requisitos do carrossel


##### Taxa de proporção para imagens


Os formatos de 1.91:1 a 9:16 são compatíveis. As imagens com uma proporção diferente de 1:1 serão cortadas e centralizadas para 1:1. Imagens com uma proporção de 1:1 não serão cortadas ou alteradas.
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)

## Etapa 5: programar a veiculação de anúncios


[Crie o objeto de anúncio](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad) para vincular o criativo ao conjunto de anúncios.


### Prévia do anúncio


Nos anúncios do Threads, você pode ver estas prévias:


- [Criativos ou anúncios que já existem](https://developers.facebook.com/docs/instagram/ads-api/guides/get-ad-preview#existing)
- [Novos anúncios, antes da inclusão de um criativo](https://developers.facebook.com/docs/instagram/ads-api/guides/get-ad-preview#before-creative)
[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)[○](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#)Nesta Página[Criação de anúncios do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#cria--o-de-an-ncios-do-threads)[Etapa 1: receber a identificação da conta do Threads](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-1)[Etapa 2: criar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-2)[Etapa 3: criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-3)[Posicionamento](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#posicionamento)[Exemplos](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#exemplos)[Etapa 4: fornecer um criativo do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-4)[Hashtags](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#hashtags)[Requisitos de mídia](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#requisitos-de-m-dia)[Etapa 5: programar a veiculação de anúncios](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#step-5)[Prévia do anúncio](https://developers.facebook.com/docs/marketing-api/ad-creative/threads-ads/creation#pr-via-do-an-ncio) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xSf3p-4PW1GWm7qVhw977SZQD685QJL946rSF68Jgec6fTwb5ZtIMv-LbDg_aem_AUjmSVA77Bu4gTqX3GdPOw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZwzpIwXYx__OfpUuGXFsCisATrQUhX_LvQjf2wTHdLfXFjULlmeuONwA2Iw_aem_ZAivUEHZCT9KN99AJPBXfA&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR54ysV2A6wVfZzZASLLtt1-3XSEqW330pA-GB1mwLMDPTZKamnMJjMGInzmdw_aem_GHLeXOY06axpTVfyWliAmw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WAwiXJ4GsO-Xj2q0QQkIKIgINWStI_tWp2miMROoGTYNcA8SSVABCaEzy3A_aem_8pzPmReaq_M8r5IQrq446g&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6pvrjXbWDn3pXz-JtUjBE3CHXrs2lWOuHqs9w7lfhq06uZBQkabTgJ6Pa3gg_aem_p56PhDjbPRb1aGouwGjADQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5aGCDhwfEPl5BSsB9B0qlV2XTCAo19gL1DpVvBOhRi09-P2QvwgzXtygNNlA_aem_C6X_TGh7IpFyGD6DOvYiXQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4WAwiXJ4GsO-Xj2q0QQkIKIgINWStI_tWp2miMROoGTYNcA8SSVABCaEzy3A_aem_8pzPmReaq_M8r5IQrq446g&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xSf3p-4PW1GWm7qVhw977SZQD685QJL946rSF68Jgec6fTwb5ZtIMv-LbDg_aem_AUjmSVA77Bu4gTqX3GdPOw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5QR275Ef5KouFWrriniuh74tuW81ymaijj5FZ2NyHWtX5HpdoU2vCZRyeN4A_aem_ItK3jYI-k2f8gTgi4uPPQw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5aGCDhwfEPl5BSsB9B0qlV2XTCAo19gL1DpVvBOhRi09-P2QvwgzXtygNNlA_aem_C6X_TGh7IpFyGD6DOvYiXQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZwzpIwXYx__OfpUuGXFsCisATrQUhX_LvQjf2wTHdLfXFjULlmeuONwA2Iw_aem_ZAivUEHZCT9KN99AJPBXfA&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR54ysV2A6wVfZzZASLLtt1-3XSEqW330pA-GB1mwLMDPTZKamnMJjMGInzmdw_aem_GHLeXOY06axpTVfyWliAmw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5aGCDhwfEPl5BSsB9B0qlV2XTCAo19gL1DpVvBOhRi09-P2QvwgzXtygNNlA_aem_C6X_TGh7IpFyGD6DOvYiXQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5aGCDhwfEPl5BSsB9B0qlV2XTCAo19gL1DpVvBOhRi09-P2QvwgzXtygNNlA_aem_C6X_TGh7IpFyGD6DOvYiXQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5QR275Ef5KouFWrriniuh74tuW81ymaijj5FZ2NyHWtX5HpdoU2vCZRyeN4A_aem_ItK3jYI-k2f8gTgi4uPPQw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6pvrjXbWDn3pXz-JtUjBE3CHXrs2lWOuHqs9w7lfhq06uZBQkabTgJ6Pa3gg_aem_p56PhDjbPRb1aGouwGjADQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5VfzbAZq_RuvysMqW3-GstK6SZpSyRw7BBCaIkZ74d3Ys_f50nPlJGgiQgqA_aem__bkR4HNtAc6wC8VHFdToMg&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5QR275Ef5KouFWrriniuh74tuW81ymaijj5FZ2NyHWtX5HpdoU2vCZRyeN4A_aem_ItK3jYI-k2f8gTgi4uPPQw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5aGCDhwfEPl5BSsB9B0qlV2XTCAo19gL1DpVvBOhRi09-P2QvwgzXtygNNlA_aem_C6X_TGh7IpFyGD6DOvYiXQ&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4xSf3p-4PW1GWm7qVhw977SZQD685QJL946rSF68Jgec6fTwb5ZtIMv-LbDg_aem_AUjmSVA77Bu4gTqX3GdPOw&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7_c4X5rBaiEZ_6TLghZEqbv-oAp5vQUjm-cKzey3tTRjLA1JaGI4et4VYhJ9oY8tLPltbrHS7r1T75xE677MgJas2bJ4Yy8OVO8vzjSgEJ3N0ycVGCXy2aH6WLJVG8bWRa99CrCo0G8HIaqbHUsmd2-ww)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão