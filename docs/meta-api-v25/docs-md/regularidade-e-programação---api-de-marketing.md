<!-- Fonte: Regularidade e programação - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Regularidade e programação


Determina como o orçamento dos seus anúncios é gasto ao longo do tempo. Ela oferece uma concorrência uniforme no leilão de anúncios do Facebook entre todos os anunciantes a cada dia, além de alocar automaticamente os orçamentos para diferentes anúncios. A regularidade funciona da mesma maneira para anúncios criados com a API e para ferramentas do Facebook. Consulte [Veiculação e regularidade na Central de Ajuda de Anúncios](https://www.facebook.com/business/help/1037425549606837).


É possível definir três opções de regularidade em `pacing_type` ao criar ou atualizar um [conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign). Com a regularidade padrão, incluímos seu anúncio em todos os leilões relevantes e ajustamos o lance ao longo do dia para gerar a veiculação ideal e regular em relação ao seu objetivo e orçamento. Essa é a regularidade padrão.


Para redefini-la:

```
curl \ -F 'pacing_type=["standard"]' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_SET_ID>
```


A **veiculação acelerada** remove todos os ajustes de regularidade do lance. Incluímos seu anúncio em todos os leilões elegíveis com o lance máximo. Você pode alcançar uma veiculação máxima com orçamento e custo especificados. Isso resulta em veiculações irregulares ao longo do dia. Dessa forma, o orçamento do seu conjunto de anúncios pode se esgotar antes do fim do dia. Para criar um conjunto de anúncios com **veiculação acelerada**:

```
curl \ -F 'name=Ad Set without pacing' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'pacing_type=["no_pacing"]' \ -F 'bid_amount=2' \ -F 'daily_budget=1000' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={"geo_locations":{"countries":["US"]}}' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


É possível desabilitar a regularidade para estes casos:


- Anunciar vendas relâmpago ou promoções por tempo limitado.
- Veicular anúncios em eventos ao vivo, como partidas esportivas e debates eleitorais.
- Maximizar a veiculação durante períodos importantes do ano, como a época de festas de fim de ano ou de volta às aulas.


Não use essa opção nas seguintes situações:


- Seu anúncio apresenta veiculação abaixo do esperado porque o lance foi muito baixo ou o direcionamento foi muito restritivo. Nesses casos, já removemos a regularidade do orçamento, então, a veiculação acelerada não ajudará.


Consulte a [referência Opções de regularidade do conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/adset/pacing).


Você também pode definir o pacing_type como `day_parting` para ter um controle mais preciso da programação de anúncios. Veja `"Ad Scheduling"`.


## Programação de anúncios


Especifique os dias da semana e as horas do dia para a veiculação do seu conjunto de anúncios em `adset_schedule`. A programação se aplica a todos os grupos de anúncios do conjunto de anúncios. Consulte [Programação de anúncios em nosso blog](https://developers.facebook.com/ads/blog/post/2014/08/13/ad-scheduling). `adset_schedule` é uma matriz de objetos JSON. Cada objeto representa uma programação para um único dia. Por exemplo:

```
curl \ -F 'name=Ad Set with scheduling' \ -F 'optimization_goal=REACH' \ -F 'billing_event=IMPRESSIONS' \ -F 'pacing_type=["day_parting"]' \ -F 'lifetime_budget=100000' \ -F 'end_time=2018-02-06T04:45:17+0000' \ -F 'adset_schedule=[ { "start_minute": 540, "end_minute": 720, "days": [ 1, 2, 3, 4, 5 ] } ]' \ -F 'bid_amount=2' \ -F 'campaign_id=<CAMPAIGN_ID>' \ -F 'targeting={"geo_locations":{"countries":["US"]}}' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adsets
```


Para atualizar a **programação de anúncios**:

```
curl \ -F 'lifetime_budget=100000' \ -F 'end_time=2016-07-21T20:42:08+0000' \ -F 'pacing_type=["day_parting"]' \ -F 'adset_schedule=[ { "start_minute": 720, "end_minute": 840, "days": [ 1, 2, 3, 4, 5 ] } ]' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_SET_ID>
```


Para desativar a **programação de anúncios**:

```
curl \ -F 'pacing_type=["standard"]' \ -F 'adset_schedule=[]' \ -F 'access_token=<ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_SET_ID>
```


Para obter informações sobre a **programação de anúncios**:

```
curl -X GET \ -d 'fields="adset_schedule"' \ -d 'access_token=<=ACCESS_TOKEN>' \ https://graph.facebook.com/v25.0/<AD_SET_ID>
```


Cada matriz deve ter:


| Nome do campo | Descrição |
| --- | --- |
| start_minute tipo: int | Minuto do dia com base 0. Quando a programação inicia |
| end_minute tipo: int | Minuto do dia com base 0. Quando a programação termina |
| days Tipo: matriz de números inteiros | Dias de programação ativa. Valores válidos: 0 a 6, em que 0 corresponde a domingo, 1 a segunda-feira e 6 a sábado. |
| timezone_type Opcional | Se o valor é "user", o fuso horário do visualizador. Se o valor é "advertizer", o fuso horário da conta. |


`start_minute` e `end_minute` devem representar horas inteiras e ter pelo menos uma hora de diferença. Para [alcance e frequência](https://developers.facebook.com/docs/marketing-api/reachandfrequency/), as partes do dia devem ter no mínimo 4 horas. Por exemplo:

```
[{'start_minute':540,'end_minute':720,'days':[1,2,3,4,5]},{'start_minute':180, 'end_minute':360,'days':[0,6]}]
```


Aplicam-se estas restrições:


- Use a programação de anúncios somente com orçamentos totais.
- A programação se aplica ao fuso horário do público-alvo dos anúncios de um conjunto, **não da conta de anúncios**. Se o fuso horário da sua conta de anúncios for o horário do Leste dos EUA, mas seus anúncios forem direcionados para pessoas na Califórnia (horário do Pacífico), seus anúncios programados para veiculação entre as 18h e 21h serão exibidos para as pessoas na Califórnia entre as 18h e 21h no horário do Pacífico, e não no horário da sua conta.
[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#)

## Perguntas frequentes

[My ads are not pacing correctly, what do I do?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2232425777087535)

For under-delivery, your bid price might be too low or your audience too narrow. Your bid should be in the suggested bid range so your ads win auctions and get placement. With competitive target audiences, you may need to bid above the suggested bid range. Or your targeting is too narrow.


If we over-deliver your ad, you might have a very large audience that quickly exhausts budget. If you believe that is not the case, contact us at [Facebook Advertising Help](https://www.facebook.com/business/help).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2232425777087535)[Is pacing at the ad set or ad campaign level?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_290777248538550)

If you're using campaign budget optimization, budget pacing is at the campaign level. Otherwise, budget pacing is done at the ad set level.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_290777248538550)[When I change my budget, will it impact pacing?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2222627511146465)

When you change budget, our systems have to learn the new optimal bid which takes time. During this time, your bids are not optimal and we can't maximize ROI. Therefore you should not change bid and budget **frequently**.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2222627511146465)[When should I change bid or budget?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_644281972666201)

If you have to change these parameters, limit yourself to 2-3 times a day and only the early part of the day. This impacts pacing less than changing it often or later in a day.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_644281972666201)[What about campaigns that run only a day or shorter?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_849734268694368)

Facebook optimizes pacing within a day, so this is not a problem.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_849734268694368)[I have ads with 'billing_event' as 'IMPRESSIONS' and I switched 'billing_event' to 'LINK_CLICKS'. Will this affect pacing?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2130174283732193)

Pacing may change. Since you switch from view-based billing to click-based billing, we re-adjust pacing.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2130174283732193)[I don't see 'max_bid' for different bid types, where is it?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2117755961607050)

Max bid is `bid_amount` of an ad set you specify regardless of its optimization goal.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_2117755961607050)[How does day parting and pacing work together?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_703725050030787)

With ad scheduling, you schedule hours in a day and days in a week when your ads display to a target audience. You can have your ads display when they are most relevant to an audience. Pacing takes this schedule into account to calculate your effective, optimal bid. See [ad scheduling](https://developers.facebook.com/docs/marketing-api/adset/pacing#ad-scheduling).
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_703725050030787)[How does Facebook spend ad set budgets over partial days?](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_304277833835641)

From April 9th, 2014, we change the way budgets are spent on partial days at the beginning and end of ad set schedules. For ad sets with daily budgets, we adjust the first and last day spend based on the number of hours we have to deliver ads on those days. For example, if your ad set starts at 6PM, we try to deliver only 25% of daily budget between 6 PM and midnight.
 [Link permanente](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq_304277833835641)[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#)[○](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#)Nesta Página[Regularidade e programação](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#regularidade-e-programa--o)[Programação de anúncios](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#ad-scheduling)[Perguntas frequentes](https://developers.facebook.com/docs/marketing-api/bidding/overview/pacing-and-scheduling#faq) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JUiBEQKD125Po97K_7dzw3kqB2GmsXBXzEGI2dPLOryZWH9h_fPbHebKRlQ_aem_9FJnPspm7R-B-rYLe1pSjw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65zC1iH5NT6IYkCugRlBLK0S1WQgS4uc24XOMNe8CifNolLidCvMIJYAL_Jg_aem_YbG-sS33ysa4Vw5Li_XIHw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7pDSymXjMCUtRwt_XleQzgku3WbJvkzTWcXXL5RWQvKhpomp1VUwFsSS7YeQ_aem_FEgzxW_bH0KxbPNppwFrsQ&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jtEGmR0KMvvVf2QnTh-v9hy_Pqd41LehJ8WPM-udWloFOxcYNPcvTvdDZHA_aem_5aMGxhR4va8ghnWishoKfg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6sEA2VbFTqx2TaEjNL09kitIKVi9IZzKFcd02twFwZU5TeKdAu_IGqN9jvkw_aem_tMMyRAGfiET01ESCtsSDFQ&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR65zC1iH5NT6IYkCugRlBLK0S1WQgS4uc24XOMNe8CifNolLidCvMIJYAL_Jg_aem_YbG-sS33ysa4Vw5Li_XIHw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_Zuc4hkB9claJHzYT23Nj4IjrFDfzy3dSc_UtB0k7BvL0jbn61TDr0_PqQg_aem_01vjj0M3a77cSD7VoA2ytw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tlks9vUVfQv4HRz5vmdNFywYOGfWrJU1YR4iJXqO8LY0OTqEIKjrKp17ROg_aem_0spLV4dxVB9FvRNcXHLIvg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jtEGmR0KMvvVf2QnTh-v9hy_Pqd41LehJ8WPM-udWloFOxcYNPcvTvdDZHA_aem_5aMGxhR4va8ghnWishoKfg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6JUiBEQKD125Po97K_7dzw3kqB2GmsXBXzEGI2dPLOryZWH9h_fPbHebKRlQ_aem_9FJnPspm7R-B-rYLe1pSjw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72v74YCyCjIpCWx4ifVDaTbZlHJePFFbuZTn892jCW7u1n21gq-GHy8ep-FA_aem_eVfX-MZp5-3tW1xKvaGhRA&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_Zuc4hkB9claJHzYT23Nj4IjrFDfzy3dSc_UtB0k7BvL0jbn61TDr0_PqQg_aem_01vjj0M3a77cSD7VoA2ytw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR72v74YCyCjIpCWx4ifVDaTbZlHJePFFbuZTn892jCW7u1n21gq-GHy8ep-FA_aem_eVfX-MZp5-3tW1xKvaGhRA&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TMjkhPw3JrucOjEbReUqzgLCppzbTgr7vPzxtDqUy9gXs_NIobXZs4gNUlQ_aem_1PdIVeOZE6VLHjcGfPuQTg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_Zuc4hkB9claJHzYT23Nj4IjrFDfzy3dSc_UtB0k7BvL0jbn61TDr0_PqQg_aem_01vjj0M3a77cSD7VoA2ytw&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ztynxgrpjYMWD2fqsDupXIu2ZYfVTxznz4eQi18LWKbZgzf7X5HqHrUpeTw_aem_ZrrlziBsFrOUe1QDY_rWfA&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ztynxgrpjYMWD2fqsDupXIu2ZYfVTxznz4eQi18LWKbZgzf7X5HqHrUpeTw_aem_ZrrlziBsFrOUe1QDY_rWfA&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tlks9vUVfQv4HRz5vmdNFywYOGfWrJU1YR4iJXqO8LY0OTqEIKjrKp17ROg_aem_0spLV4dxVB9FvRNcXHLIvg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4jtEGmR0KMvvVf2QnTh-v9hy_Pqd41LehJ8WPM-udWloFOxcYNPcvTvdDZHA_aem_5aMGxhR4va8ghnWishoKfg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5Tlks9vUVfQv4HRz5vmdNFywYOGfWrJU1YR4iJXqO8LY0OTqEIKjrKp17ROg_aem_0spLV4dxVB9FvRNcXHLIvg&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6335-ytEvTw1jpKtrDS7uqKgrzrt5xJggzIitLyEkeDvEWQ7ewVt7Tq8D4THA53tMbPLO7zqorgrfJCX8kwkemK0kMYYmCbLeY4YXgdHPBhO0IBMT5GvMIVrld6Vu0Jwc-KkFEckpgeYM-NzEh6EPG5Vo)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão