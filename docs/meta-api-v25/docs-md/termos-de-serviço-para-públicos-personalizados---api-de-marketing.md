<!-- Fonte: Termos de Serviço para públicos personalizados - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Termos de Serviço para públicos personalizados


Os [públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences-api) estão disponíveis para empresas que anunciam no Facebook. Essas empresas podem ter uma ou mais contas de anúncios e um ou mais usuários. Para usar os públicos personalizados, os usuários da empresa devem primeiro assinar nossos contratos de Termos de Serviço. Isso inclui [usuários do sistema](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser).


Os Termos de Serviço para públicos personalizados precisam ser aceitos pelo usuário e pela empresa. Para fazer isso, a empresa deve ter pelo menos uma conta de anúncios. O usuário será solicitado a assinar nossos contratos quando acessar uma das contas de anúncios da empresa. Para saber em nome de quem está assinando os contratos, o usuário precisa conhecer o status da conta de anúncios:


| Status da conta de anúncios | Com que partes os Termos de Serviço estão relacionados | Exemplo |
| --- | --- | --- |
| Pertencente a uma empresa. | Empresa proprietária da conta de anúncios. | Cenário : a empresa 1 é proprietária da conta de anúncios Alfa. Um usuário acessa a conta de anúncios Alfa e aceita os Termos de Serviço. Resultado : o usuário aceita os Termos de Serviço para a empresa 1. |
| Pertencente a uma empresa. Atua em nome de uma empresa diferente. | Empresa em nome da qual a conta está atuando. Para assinar os contratos da empresa original, o usuário deve mudar para uma conta de anúncios que não atue "em nome de". | Cenário : a empresa 1 é proprietária da conta de anúncios Alfa. A conta de anúncios Alfa está configurada para atuar em nome da empresa 2. Um usuário acessa a conta de anúncios Alfa e aceita os Termos de Serviço. Resultado : o usuário aceita os Termos de Serviço para a empresa 2. |
| Pertencente a uma empresa. Compartilhada com uma empresa diferente. | Empresa proprietária da conta de anúncios. Se a outra empresa quiser usar o público personalizado, o usuário precisará mudar para uma conta de anúncios que pertença a ela. | Cenário : a empresa 1 é proprietária da conta de anúncios Alfa. A empresa 1 compartilha a conta de anúncios Alfa com a empresa 2. Um usuário acessa a conta de anúncios Alfa e aceita os Termos de Serviço. Resultado : o usuário aceita os Termos de Serviço para a empresa 1. |


Esse usuário precisa ter uma função na conta de anúncios para poder assinar nossos contratos. Depois que um usuário aceitar os Termos de Serviço de uma empresa em uma das respectivas contas de anúncios, ele poderá gerenciar o **público personalizado a partir de um arquivo de cliente** em todas as contas de anúncios pertencentes a essa empresa.


A API não permitirá a criação nem a alteração de públicos personalizados até que os Termos de Serviço sejam aceitos. Se o contrato não for assinado, dispararemos erros quando você tentar criar ou editar um público personalizado a partir de um arquivo de cliente e quando tentar modificar a seção de segmentação ou o público salvo, caso incluam um público personalizado.


Encontre o link dos Termos de Serviço para públicos personalizados da sua empresa em `https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`. O campo de identificação da empresa é gerado automaticamente.


## Tipos de público personalizado qualificados


Depois que você assinar nossos Termos de Serviço, as contas de anúncios da sua empresa poderão usar os seguintes tipos de público personalizado:


| Público Personalizado | Subtipo | Parâmetro is_value_based |
| --- | --- | --- |
| Público personalizado a partir de um arquivo de cliente | CUSTOM | Não é necessário |
| Público personalizado baseado em valor | CUSTOM | 1 |
| Público personalizado de mensuração | MEASUREMENT | Não é necessário |


Caso você não queira usar públicos personalizados com subtipo `CUSTOM` ou `MEASUREMENT`, será preciso assinar os Termos de Serviço dos níveis da conta de anúncios.


## Usuários do sistema


Para que um usuário do sistema opere com um público personalizado a partir de um arquivo de cliente em uma empresa, um usuário que não seja do sistema precisará aceitar os Termos de Serviço para públicos personalizados dessa empresa. A confirmação do aceite deverá ser feita em uma conta de anúncios de propriedade da empresa em questão. Para exceções, consulte a tabela acima.


Caso um usuário que não seja do sistema já tenha aceitado os Termos de Serviço para públicos personalizados em uma conta de anúncios com um relacionamento do tipo "Em nome de", os usuários do sistema poderão operar em nome dessa outra empresa. No entanto, os usuários do sistema não poderão operar na empresa original. O usuário que não é do sistema poderá acessar diferentes contas de anúncios na empresa proprietária e aceitar os Termos de Serviço para que os usuários do sistema possam operar.


Para confirmar se um usuário do sistema tem permissão para operar com um público personalizado a partir de um arquivo de cliente, você pode verificar o status dos Termos de Serviço de uma das contas de anúncios da empresa. Isso poderá ser feito desde que a conta de anúncios não seja do tipo "Em nome de" nem tenha sido compartilhada com outra empresa. No nível da conta de anúncios, é possível ver todos os Termos de Serviço assinados para a empresa proprietária da conta.


## Verificar a assinatura


Você pode verificar se uma empresa assinou os Termos de Serviço para públicos personalizados fazendo uma chamada `GET` para uma conta de anúncios que pertence a essa empresa. A conta de anúncios não pode ser do tipo "Em nome de" nem pode ter sido compartilhada com outra empresa. A chamada `GET` é:

```
GET act_<AD_ACCOUNT_ID>?fields=tos_accepted
```


Um exemplo de resposta é semelhante a:

```
{
  "tos_accepted": {
    "custom_audience_tos": 1 // this means the terms were signed
  },
  "id": "act_<AD_ACCOUNT>"
}
```


**Observação**: você também receberá `custom_audience_tos: 1` para uma conta de anúncios com um relacionamento do tipo "Em nome de". Porém, esses termos são assinados para a empresa em nome da qual a conta de anúncios atua.


Na conta de anúncios, você também verificar se um usuário específico assinou os Termos de Serviço. Para isso, faça uma chamada `GET` e inclua o token de acesso do usuário:

```
GET act_<AD_ACCOUNT_ID>?fields=user_tos_accepted
```


Um exemplo de resposta com a confirmação de aceite dos `custom_audience_tos` é semelhante a:

```
{
  "user_tos_accepted": {
    "custom_audience_tos": 1
  },
  "id": "act_<AD_ACCOUNT_ID>",
  "__fb_trace_id__": "EKjdfdfeOt0k"
}
```


Isso é válido apenas para usuários que não são do sistema.
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service#)Nesta Página[Termos de Serviço para públicos personalizados](https://developers.facebook.com/docs/marketing-api/audiences/reference/custom-audience-terms-of-service#termos-de-servi-o-para-p-blicos-personalizados) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_l1oIxHfbN3SpLKX_263JtSmIPPSIUY4MNpnHZ_PD36Cdn5w-uUqKfN0TEQ_aem_mEYDF1K0HpNi9nnfGaw8Qg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR521LLINtYLo0t7iTrS2JpzKGme4bW_eEJ2mJcdfPHVC8b7PB94y_HYmE9pgg_aem_XrMn7cj1WNSTJit6Du85hw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR521LLINtYLo0t7iTrS2JpzKGme4bW_eEJ2mJcdfPHVC8b7PB94y_HYmE9pgg_aem_XrMn7cj1WNSTJit6Du85hw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6rMTsegP887O3KKHWAj43wL_Le4m3a4mASvGku0xl-99kZTy66sRw6smQXFA_aem_C4f9HYWhEM3dabJBMdbxmA&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NZhpduVEdV0FFH5yyqlqxglJUAz2GGKjAD_yU7UeY2bXY1POr1CjmAhZaEQ_aem_WEoQhKCR2rm3yV2CB20J5g&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_l1oIxHfbN3SpLKX_263JtSmIPPSIUY4MNpnHZ_PD36Cdn5w-uUqKfN0TEQ_aem_mEYDF1K0HpNi9nnfGaw8Qg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6U4dx-3njAUg0aIfugF0xbWYi32gexiYYSsDm5C_adKpkAYI0q70K7sd3Iww_aem_MXyTnjvSzEbNNNVfDACKwg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NZhpduVEdV0FFH5yyqlqxglJUAz2GGKjAD_yU7UeY2bXY1POr1CjmAhZaEQ_aem_WEoQhKCR2rm3yV2CB20J5g&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR521LLINtYLo0t7iTrS2JpzKGme4bW_eEJ2mJcdfPHVC8b7PB94y_HYmE9pgg_aem_XrMn7cj1WNSTJit6Du85hw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RLJW1AK5Oi0OCmCymiUocKbIkSdRwicMe4_sYPrTbRBA20lQZccusQqc6gg_aem_GUzxcuW1B5mukvkJpVlRjw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR58fduAu7T1rgqPScGqhk8EE-sWnWKXPwdIVgu0Zp8TP1WuPfGHYKzcTp3GGQ_aem_vGLcbgQJ_KzgjjU7zZY-Pw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_l1oIxHfbN3SpLKX_263JtSmIPPSIUY4MNpnHZ_PD36Cdn5w-uUqKfN0TEQ_aem_mEYDF1K0HpNi9nnfGaw8Qg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RLJW1AK5Oi0OCmCymiUocKbIkSdRwicMe4_sYPrTbRBA20lQZccusQqc6gg_aem_GUzxcuW1B5mukvkJpVlRjw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR521LLINtYLo0t7iTrS2JpzKGme4bW_eEJ2mJcdfPHVC8b7PB94y_HYmE9pgg_aem_XrMn7cj1WNSTJit6Du85hw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5gGKKyPzhPu523pQQXsMsA_lmmX7j1t5wocELriJ9_8pZ3cZtV8YJRME3UkA_aem_sMcWlxGS3zxuXAUB8Lj1og&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6U4dx-3njAUg0aIfugF0xbWYi32gexiYYSsDm5C_adKpkAYI0q70K7sd3Iww_aem_MXyTnjvSzEbNNNVfDACKwg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5gGKKyPzhPu523pQQXsMsA_lmmX7j1t5wocELriJ9_8pZ3cZtV8YJRME3UkA_aem_sMcWlxGS3zxuXAUB8Lj1og&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5NZhpduVEdV0FFH5yyqlqxglJUAz2GGKjAD_yU7UeY2bXY1POr1CjmAhZaEQ_aem_WEoQhKCR2rm3yV2CB20J5g&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_l1oIxHfbN3SpLKX_263JtSmIPPSIUY4MNpnHZ_PD36Cdn5w-uUqKfN0TEQ_aem_mEYDF1K0HpNi9nnfGaw8Qg&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4RLJW1AK5Oi0OCmCymiUocKbIkSdRwicMe4_sYPrTbRBA20lQZccusQqc6gg_aem_GUzxcuW1B5mukvkJpVlRjw&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6L6qwApohMceZITlxV6ugqxDYNfXSVXd_mVd-7aMNthpJX0CwsqiLYjMenpC2S1UP0ZOY9OQa6B4znQ3FSevwTwQTW2cBV15-s1trinrE9Xmp1SPLsxDmA8GxPTKlXFikJWwUZNSAp8_dl8wd7kxAyltM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão