<!-- Fonte: Direcionamento detalhado - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Direcionamento detalhado


Com a [Pesquisa de direcionamento](https://developers.facebook.com/docs/marketing-api/targeting-search), você pode encontrar um tipo de direcionamento em uma única chamada de API. Já com a API de Direcionamento Detalhado, você pode pesquisar **vários tipos de direcionamento ao mesmo tempo fazendo apenas uma solicitação**. Você também pode obter sugestões com base na sua consulta.


A API tem quatro pontos de extremidade: [Pesquisa](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#search), [Sugestões](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#suggestions), [Navegação](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#browse) e [Validação](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#validation).


A resposta para estes pontos de extremidade contém o seguinte:


| Nome | Descrição |
| --- | --- |
| id Tipo: string | Identificação do público-alvo. |
| name Tipo: string | Nome do público-alvo. |
| audience_size_lower_bound número inteiro | O tamanho mínimo estimado do público-alvo. |
| audience_size_upper_bound número inteiro | O tamanho máximo estimado do público-alvo. |
| path Tipo: matriz de strings | Inclui a categoria e todas as categorias principais que se enquadram no direcionamento. |
| description Tipo: string | Uma breve descrição sobre o público-alvo. |


Se você não fornecer `limit_type`, filtraremos os resultados com menos de 2.000 pessoas em quatro categorias: `work_employers`, `work_positions`, `education_majors`, `education_schools`. Caso contrário, você obterá resultados menos significativos. Quando você usa `limit_type`, filtramos uma dessas quatro categorias e não retornamos tudo.


## Pesquisa


Recupere públicos-alvo para anúncios que correspondam à sua consulta de pesquisa. Você pode fornecer os seguintes parâmetros neste ponto de extremidade:

```
curl -G \
-d "q=harvard" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingsearch
```


| Nome | Descrição |
| --- | --- |
| q Tipo: string | Obrigatório. String de consulta. |
| limit Tipo: número inteiro | Opcional. Número de resultados. |
| limit_type Tipo: string | Opcional. Limite o tipo de público que será recuperado. Por padrão, incluímos todos os tipos. Valores válidos: interests; education_schools; education_majors; work_positions; work_employers; relationship_statuses; college_years; education_statuses; family_statuses; industries; life_events; behaviors; income |
| locale Tipo: string | Opcional. A localidade para mostrar nomes e descrições do público, se disponível. Por padrão, usamos a localidade da conta de anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#)

## Sugestões


Veja públicos adicionais para fazer o direcionamento com base em alguns públicos específicos fornecidos por você.

```
curl -G \
-d "targeting_list=[{'type':'interests','id':6003263791114}]" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingsuggestions
```


Forneça estes parâmetros:


| Nome | Descrição |
| --- | --- |
| targeting_list Tipo: matriz de {'type':'{TYPE}', 'id':{ID}} | Obrigatório. Matriz de pares de {'type':'{TYPE}', 'id':{ID}} como público de entrada para sugestões. |
| limit Tipo: número inteiro | Opcional. Número de resultados. O padrão é 30. O máximo é 45. |
| limit_type Tipo: string | Opcional. Limite o tipo de público que será recuperado. Por padrão, incluímos todos os tipos. Valores válidos: interests; education_schools; education_majors; work_positions; work_employers; relationship_statuses; college_years; education_statuses; family_statuses; industries; life_events; behaviors; income |
| locale Tipo: string | Opcional. A localidade para mostrar nomes e descrições do público. Por padrão, usamos a localidade da conta de anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#)

## Navegação


Obtenha o direcionamento em uma taxonomia estruturada para categorias do Facebook, provedores de dados de terceiros e alguns interesses. Os resultados deste ponto de extremidade aparecem na funcionalidade de navegação no componente da interface do usuário de direcionamento detalhado no Gerenciador de Anúncios.

```
curl -G \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingbrowse
```


Forneça os seguintes parâmetros opcionais:


| Nome | Descrição |
| --- | --- |
| limit_type Tipo: string | Limite o tipo de público que será recuperado. Por padrão, incluímos todos os tipos. |
| locale Tipo: string | A localidade para mostrar nomes e descrições do público. Por padrão, usamos a localidade da conta de anúncios. |

[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#)

## Validação


Verifique se um público é válido para fazer o direcionamento ou não. Isso será útil se você já tiver criado um conjunto de anúncios e quiser verificar se as especificações de direcionamento ainda são válidas. Caso o direcionamento não seja válido, exclua-o das especificações.

```
curl -G \
-d "targeting_list=[{'type':'interests','id':6003283735711}, {'type':'relationship_statuses','id':100}]" \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<API_VERSION>/act_<AD_ACCOUNT_ID>/targetingvalidation
```


Além dos campos de resposta padrão de direcionamento detalhado, este ponto de extremidade também retorna o seguinte:


| Nome | Descrição |
| --- | --- |
| valid Tipo: booleano | Indica se o público-alvo é válido ou não. |


Veja a seguir a lista de parâmetros de entrada:


| Nome | Descrição |
| --- | --- |
| targeting_list Tipo: matriz de {'type':'{TYPE}', 'id':{ID}} | Matriz de pares de {'type':'{TYPE}', 'id':{ID}} para validação. Preferencial. |
| id_list Tipo: matriz de strings | Matriz de identificações para validação. Só terá sucesso se for uma identificação única no nosso banco de dados de público. |
| name_list Tipo: matriz de strings | Matriz de strings para validação. Apenas interesses (não diferencia maiúsculas de minúsculas). |
| locale Tipo: string | Localidade para exibição de nomes e descrições do público. Por padrão, usamos a localidade da conta de anúncios. |


Forneça pelo menos umas destas opções: `targeting_list`, `id_list` e `name_list`.
[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#)[○](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#)Nesta Página[Direcionamento detalhado](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#direcionamento-detalhado)[Pesquisa](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#search)[Sugestões](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#suggestions)[Navegação](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#browse)[Validação](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting#validation) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6cUAYLf0iYlgXtlqxeNEUztVrsVRbffQMMDmsizHiGT-MKFRXGuXiq7lhbgQ_aem_xVdf6jNtMYakhNJUQJYBlQ&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nUrILhL3-L41n8Y3mE040qrwFuJhcVi8W8BDaZgN2SyyvzKjepAHv4GIXtA_aem_7kyp6p9cNS_j19Tr41EQFQ&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6InZSXvtuZvuB_UcKlDOEDARGR5x5jZ0i-D0h_JPCC4QeYIbYUfU7R57toVg_aem_A6jmmo-oQ7-4PvLaAgXo2A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6VVGIMVhETdCZs7JzNqDVx4zcyfxoU4lstXoqHpnSUgcUMJ0sE6GPPZF9gDg_aem_ei9niBF8dlz7p8zO9yyU8A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6VVGIMVhETdCZs7JzNqDVx4zcyfxoU4lstXoqHpnSUgcUMJ0sE6GPPZF9gDg_aem_ei9niBF8dlz7p8zO9yyU8A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Fj_IXPZtQ_QpgEv-EG_bga5-xWmTFvXKnXKSWHL2mf8fox86KPZDUrKiBWA_aem_batbP_VYXuLM7VL-Ghb5cg&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6VVGIMVhETdCZs7JzNqDVx4zcyfxoU4lstXoqHpnSUgcUMJ0sE6GPPZF9gDg_aem_ei9niBF8dlz7p8zO9yyU8A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66Rx4EWAFCaVR_uV1-pUOSm4XqzDD6Y_3DwOJZszKr7tqT0hWwTmegE7f4yA_aem_N8Kx1zbt7kQnzsc8OkxFlw&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6InZSXvtuZvuB_UcKlDOEDARGR5x5jZ0i-D0h_JPCC4QeYIbYUfU7R57toVg_aem_A6jmmo-oQ7-4PvLaAgXo2A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5YkGe1tJxIV9gsqsQgur-cIPeZZwG1BDt3xg2CoKZPBCVaE0-kTKzaiP89sA_aem_kPTc4jZsEHaGbgSoEbnNww&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66Rx4EWAFCaVR_uV1-pUOSm4XqzDD6Y_3DwOJZszKr7tqT0hWwTmegE7f4yA_aem_N8Kx1zbt7kQnzsc8OkxFlw&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66Rx4EWAFCaVR_uV1-pUOSm4XqzDD6Y_3DwOJZszKr7tqT0hWwTmegE7f4yA_aem_N8Kx1zbt7kQnzsc8OkxFlw&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66Rx4EWAFCaVR_uV1-pUOSm4XqzDD6Y_3DwOJZszKr7tqT0hWwTmegE7f4yA_aem_N8Kx1zbt7kQnzsc8OkxFlw&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66Rx4EWAFCaVR_uV1-pUOSm4XqzDD6Y_3DwOJZszKr7tqT0hWwTmegE7f4yA_aem_N8Kx1zbt7kQnzsc8OkxFlw&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nUrILhL3-L41n8Y3mE040qrwFuJhcVi8W8BDaZgN2SyyvzKjepAHv4GIXtA_aem_7kyp6p9cNS_j19Tr41EQFQ&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6VVGIMVhETdCZs7JzNqDVx4zcyfxoU4lstXoqHpnSUgcUMJ0sE6GPPZF9gDg_aem_ei9niBF8dlz7p8zO9yyU8A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6InZSXvtuZvuB_UcKlDOEDARGR5x5jZ0i-D0h_JPCC4QeYIbYUfU7R57toVg_aem_A6jmmo-oQ7-4PvLaAgXo2A&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Fj_IXPZtQ_QpgEv-EG_bga5-xWmTFvXKnXKSWHL2mf8fox86KPZDUrKiBWA_aem_batbP_VYXuLM7VL-Ghb5cg&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR71S_t8q9iZbslhBoaA56ZryHcWx4PJdCGWZZc6cGaPpbGRegMma47RGvVZgQ_aem_RdrJu84E1L4DOZBEo4XC0w&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4wam6kBbXGKRqtZr6ruZuiistJOvc3W447z-VAEcy8UpOSlRUEYCavwNYrVw_aem_IZMGEUIA26UULk7Xp7ojMg&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4qtPW5xodWfl4roIO7ZDQqVJuPIUwwtxmIXo2YMdRzcLq_EaqTpmlQefZHe5dx44ivbjzhbPXp5-jELg2AnUNkWZ5iwuF54j4LEG_7G_c0qtJhDNvxD-gfiGI4x7cANEZcBGbW9ECMv9ALOlJH_knkYKQ)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão