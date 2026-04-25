<!-- Fonte: Visão geral dos públicos  - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/overview -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Visão geral dos públicos


O direcionamento de público ajuda a exibir seus anúncios para as pessoas que interessam a você. Há duas abordagens gerais possíveis para a criação de um público-alvo:


- **Específica**: você define um conjunto relativamente rigoroso de parâmetros, e nós criamos um público com base nessas definições. Essa abordagem inclui públicos personalizados, semelhantes e dinâmicos.
- **Ampla**: você usa nosso sistema de veiculação para encontrar as melhores pessoas a quem exibir seu anúncio. Forneça restrições básicas, como dados demográficos ou localização, para que possamos exibir os anúncios às pessoas que atendem a esses atributos.


Este documento fornece uma visão geral das opções de direcionamento de público oferecidas pela API de Marketing.


## Públicos personalizados


Beginning September 2, 2025, we will start to roll out more proactive restrictions on custom audiences that may suggest information not permitted under our terms. For example, any custom audience or lookalike audience suggesting specific health conditions (e.g., "arthritis", "diabetes") or financial status (e.g., "credit score", "high income") will be flagged and prevented from being used to run ad campaigns.


**What these restrictions mean for your campaigns:**


- You won't be able to use flagged custom audiences when creating new campaigns.
- If you have an active campaign using flagged custom audiences, you should edit or pause it and choose a different audience to avoid performance and delivery issues.


**For API developers:**


- Beginning September 2, 2025, `operation_statu`s will return `471` to signal if your custom audiences have been flagged.


More information on this update and how to resolve flagged custom audiences can be found [here](https://www.facebook.com/business/help/1055828013359808).


A opção de público personalizado permite que você crie seu próprio público a partir de um conjunto de fontes diferentes, incluindo listas de clientes, tráfego do site ou do app e engajamento no Facebook.


Alguns casos podem exigir a criação de [regras](https://developers.facebook.com/docs/marketing-api/audiences/overview/audience-rules) para determinar se uma pessoa deve ser adicionada ao seu público personalizado.


### Permissões


É preciso receber a permissão [`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management/) para criar e atualizar públicos personalizados.


### Tipos de público personalizado


#### [Públicos personalizados a partir de um arquivo de cliente](https://developers.facebook.com/docs/marketing-api/audiences-api)


Crie públicos personalizados para direcionamento a partir de informações dos clientes. Isso inclui endereço de email, telefone, nome, data de nascimento, gênero, localização, [número de identificação do usuário do app](https://developers.facebook.com/docs/graph-api/reference/user), [número de identificação do usuário no escopo da Página](https://developers.facebook.com/docs/app-events/bots-for-messenger), Identificador de Anunciante da Apple ou [ID de publicidade do Android](https://l.facebook.com/l.php?u=https%3A%2F%2Fdeveloper.android.com%2Fgoogle%2Fplay-services%2Fid.html&h=AT7CSWUW6qeel7KcKZSPSt8K2JLrJhUU4VGegiLP4eOpC68RYTnr-SPmyY6CizYNVGHnjlSz16OlDwSROobGGplY9JDAkOQwvZRD60r4DcRuFvGjxaUKTw1p1gEVnW-M3Np-Pz2LD3HeKQ1IQ64oKGep7nw).


#### [Públicos personalizados de engajamento](https://developers.facebook.com/docs/marketing-api/audiences-api/engagement)


Crie públicos com base nas pessoas que interagiram com seu conteúdo no Facebook ou no Instagram. No momento, os tipos de público compatíveis incluem Página, perfil comercial do Instagram, anúncio de lead e anúncio de experiências instantâneas.


#### [Públicos personalizados de app para celular](https://developers.facebook.com/docs/marketing-api/audiences-api/mobile-apps)


Crie públicos com base nas ações das pessoas no app que atendem aos seus critérios. Essa solução usa eventos registrados com nome por meio dos [SDKs do Facebook](https://developers.facebook.com/docs/app-ads/sdk), da [API de Eventos do App](https://developers.facebook.com/docs/app-events) ou dos [Parceiros de Métricas para Aplicativos](https://developers.facebook.com/docs/app-ads/measuring/measurement-partners).


#### [Públicos personalizados do site](https://developers.facebook.com/docs/marketing-api/audiences-api/websites)


Crie públicos personalizados de usuários que acessaram seu site ou realizaram ações específicas nele usando o [pixel do Facebook](https://developers.facebook.com/docs/facebook-pixel), a [API de Tag](https://developers.facebook.com/docs/ads-for-websites/tag-api) do JavaScript e as regras de público. Depois de criar um público personalizado com dados do site, faça referência a ele para direcionar o anúncio como você faria com o tipo padrão de [público personalizado](https://developers.facebook.com/docs/reference/ads-api/custom-audience-targeting).


#### [Públicos personalizados offline](https://developers.facebook.com/docs/marketing-api/audiences-api/offline)


Agrupe as pessoas que visitaram sua loja, ligaram para seu atendimento ao cliente ou realizaram ações offline e direcione anúncios do Facebook para elas. Os públicos personalizados de conversões offline são baseados em eventos de conversão carregados em um conjunto de eventos offline.


#### [Públicos dinâmicos](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-audiences)


Os públicos dinâmicos permitem que você exiba anúncios às pessoas com base nas intenções de compra em todos os dispositivos. É possível coletar sinais da intenção do usuário em apps para celular e sites e usar esses dados para criar um público de clientes em potencial para direcionamento.


#### [Públicos semelhantes](https://developers.facebook.com/docs/marketing-api/audiences/guides/lookalike-audiences)


Exiba anúncios a pessoas parecidas com seus clientes já estabelecidos. Os públicos semelhantes usam vários conjuntos de pessoas como "sementes". Depois, o Facebook cria um público com pessoas semelhantes. Use semelhantes para qualquer objetivo da empresa: direcionamento de pessoas parecidas com seus clientes para fins de aquisição de fãs, registro no site, compras fora do Facebook, resgates de cupom ou apenas para impulsionar o reconhecimento de uma marca.


### Como compartilhar um público personalizado


Você pode optar por compartilhar seu público personalizado com outra empresa, como um parceiro que gerencia e veicula seus anúncios. Para isso, você deve usar APIs e requisitos específicos. Saiba mais sobre [Funções entre empresas](https://developers.facebook.com/docs/marketing-api/businessmanager/business-to-business).


### Como excluir públicos personalizados


Para todos os anunciantes: a partir de 8 de junho de 2021, o status "Público a expirar" será aplicado automaticamente quando um público ficar inativo por mais de dois anos. Em outras palavras, se um público não for usado em um conjunto de anúncios ativo por mais de dois anos, ele será sinalizado automaticamente como um "Público a expirar". Além disso, quando o público for programado para exclusão, o campo `delete_time` será marcado com o tempo estimado para que isso aconteça (ou seja, 90 dias a partir do momento da sinalização).


Depois disso, você poderá excluir proativamente o público ou usá-lo em um conjunto de anúncios ativo para evitar a exclusão. É possível ver quais dos seus públicos estão na fase de expiração a qualquer momento. Para isso, use os filtros nos campos `operation_status` ou `delete_time`.


Especificamente para [públicos personalizados da lista de clientes](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences), você precisará fornecer as instruções antes de realizarmos qualquer ação. Assim que um público for sinalizado e movido para o estágio "Público prestes a expirar", você poderá usá-lo em um conjunto de anúncios ativos, e isso será entendido como uma instrução para que ele seja retido. Caso você decida não usar o público, isso será considerado uma instrução para que ele seja excluído.


#### Público personalizado


[**Ponto de extremidade:**`GET /{CUSTOM_AUDIENCE_ID}`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience)


O campo `operation_status` de públicos personalizados agora tem uma opção de status `EXPIRING` que será adicionada a públicos que não tiverem sido usados em um conjunto de anúncios ativo nos últimos 2 anos. Quando um público for marcado como "prestes a expirar", o campo `delete_time` indicará a data de exclusão.


**Exemplo de resposta**

```
delete_time: 1620543600 // Unix time in secs for 9 May 2021
operation_status: {
  “status”: 100
  “description”: "If an audience hasn't been used in an active ad set for over 2 years, it will begin to expire. Expiring audiences that remain unused for 90 days will be deleted."
}
```


#### Conta de anúncios


[**Ponto de extremidade:**`GET /act_{AD_ACCOUNT_ID]/customaudiences`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/customaudiences)


Agora você pode filtrar públicos personalizados para ver quais têm o `operation_status` de `EXPIRING` ou quais têm um campo `delete_time` indicando que o público será excluído em breve. Esses novos filtros retornarão as identificações dos públicos.


**Exemplos de solicitação**

```
GET /act_217284683/customaudiences?filtering=[{"field":"delete_time","operator":"GREATER_THAN","value":0}]&fields=["name", "operation_status","delete_time"]

GET /act_217284683/customaudiences?filtering=[{"field":"operation_status.code","operator":"IN","value":[100]}]&fields=["name", "operation_status","delete_time"]']
```


**Ponto de extremidade:**`GET /act_{AD_ACCOUNT_ID}/saved_audiences`


Agora você pode filtrar públicos salvos por `delete_time` para ver quais serão excluídos em breve. Esse filtro retornará as identificações dos públicos.


**Exemplo de solicitação**

```
GET /act_217284683/saved_audiences?filtering=[{"field":"delete_time","operator":"GREATER_THAN","value":0}]
```


#### Públicos salvos


[**Ponto de extremidade:**`GET /{SAVED_AUDIENCE_ID}`](https://developers.facebook.com/docs/marketing-api/reference/saved-audience)


O campo `operation_status` para públicos salvos agora tem uma opção de status `EXPIRING` que será adicionada a públicos que não tiverem sido usados em um conjunto de anúncios ativo nos últimos 2 anos. Quando um público for marcado como "prestes a expirar", o campo `delete_time` indicará a data de exclusão.


**Exemplo de resposta**

```
delete_time: 1620543600 // Unix time in secs for 9 May 2021
operation_status: {
  "status": 100
  "description": "If an audience hasn't been used in an active ad set for over 2 years, it will begin to expire. Expiring audiences that remain unused for 90 days will be deleted."
}
```


#### Perguntas frequentes

[Which audiences will be impacted by this change?](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_834753803829558)

Any Custom Audience, Lookalike Audience, or Saved Audience which has not been used in any active ad sets in over two years will be included in this update. **Note:** This is a rolling change going forward.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_834753803829558)[Is there any action I can take to prevent my flagged audiences from being deleted on the planned deletion date?](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_2904555683152585)

If you do not wish for the identified audiences to be deleted, you will be required to include the audiences marked as “Expiring Audience” in an active ad set prior to the deletion date shown in the `delete_time` field, which is 90 days after the audience is flagged, to keep it from being deleted.


For [Customer List Custom Audiences](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences), specifically, you will need to provide us with your instructions by either using the flagged audience in an active ad set, which we will consider an instruction to retain the audience, or by deciding not to use the flagged audience in an active ad set, which we will consider an instruction to delete the audience.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_2904555683152585)[When does the system automatically delete an audience?](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_1999620396847212)

The system will automatically delete the audience that has had an `EXPIRING` status for more than 90 days.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/audiences/overview#faq_1999620396847212)[○](https://developers.facebook.com/docs/marketing-api/audiences/overview#)

## Direcionamento


As especificações de direcionamento são atributos do [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset) que definem quem vê o anúncio. O direcionamento básico ou principal inclui o seguinte:


- [Dados demográficos e eventos](https://developers.facebook.com/docs/marketing-api/buying-api/targeting#demographics)
- [Localização](https://developers.facebook.com/docs/marketing-api/buying-api/targeting#location)
- [Interesses](https://developers.facebook.com/docs/marketing-api/buying-api/targeting#interests)
- [Comportamentos](https://developers.facebook.com/docs/marketing-api/buying-api/targeting#behaviors)


Normalmente, você consulta dados para definir o direcionamento a partir de uma [pesquisa de direcionamento](https://developers.facebook.com/docs/reference/ads-api/get-autocomplete-data). Depois, define as opções nas [especificações de direcionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs). Você precisará especificar pelo menos um país no direcionamento, exceto se usar [públicos personalizados](https://developers.facebook.com/docs/marketing-api/custom-audience-targeting).


Haverá conjuntos distintos de restrições para os anunciantes que veicularem anúncios de moradia, emprego e crédito que estiverem baseados nos Estados Unidos ou que veicularem anúncios direcionados a esse país. Consulte [**Categorias de anúncio especial**](https://developers.facebook.com/docs/marketing-api/special-ad-category/).
[○](https://developers.facebook.com/docs/marketing-api/audiences/overview#)

## Veja também


- [Sobre públicos personalizados](https://www.facebook.com/business/help/744354708981227?id=2469097953376494)
- [Sobre os públicos semelhantes](https://www.facebook.com/business/help/164749007013531?id=401668390442328)
[○](https://developers.facebook.com/docs/marketing-api/audiences/overview#)[○](https://developers.facebook.com/docs/marketing-api/audiences/overview#)Nesta Página[Visão geral dos públicos](https://developers.facebook.com/docs/marketing-api/audiences/overview#vis-o-geral-dos-p-blicos)[Públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences/overview#p-blicos-personalizados)[Permissões](https://developers.facebook.com/docs/marketing-api/audiences/overview#permiss-es)[Tipos de público personalizado](https://developers.facebook.com/docs/marketing-api/audiences/overview#tipos-de-p-blico-personalizado)[Como compartilhar um público personalizado](https://developers.facebook.com/docs/marketing-api/audiences/overview#como-compartilhar-um-p-blico-personalizado)[Como excluir públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences/overview#custom-audiences-deletion)[Direcionamento](https://developers.facebook.com/docs/marketing-api/audiences/overview#direcionamento)[Veja também](https://developers.facebook.com/docs/marketing-api/audiences/overview#veja-tamb-m) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5BCxyJExGSNtLY15CwQV2lR-0Si0CIlcSSc1GzDrtP883NQAuq0LeBDIJkxw_aem_PiWougUP_LmEEzxNyIntkw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wz_x_XN2FyJxLrxZaJd5-TGBFhCUPP69FuDEtb6mtXUrM3pZst8zoDyfApA_aem_QkPMaqWCe7J5XrWWDiLSSQ&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7I0Bu1gMuW-OrVagGZ-YJqaLxl_fy8G4BvOO8yFyZ2WYjJ5iH2GYOf8d9tnQ_aem_vnUZEnQ1xSdMQI-yXK8G9Q&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Bnkr_2X7VfbzEzcKaAceNHSvoO_w4Z7PNCbxuAk5LfdF_RRpC-WraUXNxoA_aem_9AiTnPpMUKFzNYwC4jy6Zg&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6WMIhuQ3ubUaW_WdJK1sNjVa-rUfC-DF42W25UXE1_XN4xgtDHm9plBuWNNg_aem_n18HODXSNnTPSEGBK8BTLw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e3ATXDezny6XBc-mNy_Y3T1yCP7b95szqU6c8ktb767iqf7Fs3cT94ADDcQ_aem_-m8-4ZS8jdr2jIt4JVQ62g&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7e3ATXDezny6XBc-mNy_Y3T1yCP7b95szqU6c8ktb767iqf7Fs3cT94ADDcQ_aem_-m8-4ZS8jdr2jIt4JVQ62g&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7wz_x_XN2FyJxLrxZaJd5-TGBFhCUPP69FuDEtb6mtXUrM3pZst8zoDyfApA_aem_QkPMaqWCe7J5XrWWDiLSSQ&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Bnkr_2X7VfbzEzcKaAceNHSvoO_w4Z7PNCbxuAk5LfdF_RRpC-WraUXNxoA_aem_9AiTnPpMUKFzNYwC4jy6Zg&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mxzIVHtz0FDYMB3ZuZpVu9oCBLeZXE_2MRSz4a19bteNo3lq2dAOHCG2UeQ_aem_0F1jkJ0ir0VG0492KtvpEw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7I0Bu1gMuW-OrVagGZ-YJqaLxl_fy8G4BvOO8yFyZ2WYjJ5iH2GYOf8d9tnQ_aem_vnUZEnQ1xSdMQI-yXK8G9Q&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Bnkr_2X7VfbzEzcKaAceNHSvoO_w4Z7PNCbxuAk5LfdF_RRpC-WraUXNxoA_aem_9AiTnPpMUKFzNYwC4jy6Zg&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4FqMqNvrJMLDHc0PEKiSwKgCP86YN9axL8y8fOW-H23QmtwgEudu-qQ8ZEOQ_aem_trV3pJalKi0owzB99xbhLA&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mxzIVHtz0FDYMB3ZuZpVu9oCBLeZXE_2MRSz4a19bteNo3lq2dAOHCG2UeQ_aem_0F1jkJ0ir0VG0492KtvpEw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7XwJeYHcjhL5E6CGOHXj81UtwAjZLvS1wXcR5Fnjllenj-SijCOTBQOkHLEg_aem_YjvUVyxyDA2YGRzQthM1uw&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7opOSA8W5-zRkmjnrl51WteieJ9L1AEQn-R33_VQk0TTG2RA81fj8sTeeGUl0K8cxbDjtiVp--7tsIbR1zIvBLB6-iVkB5DI-XP3mkXjKVPg5Xt5JRy_yq2Kzh8UcCzXoNejFcYMWLHvOFbB7fk2wcYGw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão