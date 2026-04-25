<!-- Fonte: Marketing mix modeling - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Detalhamento de marketing mix modeling na API de Insights


O detalhamento de marketing mix modeling na API de Insights é uma opção de autoatendimento para extração de dados que pode ser usada para exportar dados de anúncios da Meta de forma rápida e fácil sem passar por um dos nossos Parceiros de Marketing Science nem por agências de terceiros e Parceiros de Métricas para Aplicativos.


As chamadas de API são integradas na API de Insights usando o parâmetro `breakdowns=mmm`. **Observação:** não é possível combinar essa opção com diferentes `breakdowns` nem `action_breakdowns`.


As respostas contêm métricas e detalhamentos semelhantes aos resultados da exportação de dados de marketing mix modeling na interface Relatórios de Anúncios. Os dados de marketing mix modeling estão disponíveis apenas no nível do conjunto de anúncios (equivalente ao parâmetro `level=adset`). No momento, as métricas compatíveis com dados de marketing mix modeling são `impressions` e `spend`. **Observação:**`spend` é uma métrica estimada. Consulte [API de Insights, Métricas obsoletas e estimadas](https://developers.facebook.com/docs/marketing-api/insights/estimated-in-development#estimated) para ver mais informações.


### Permissões


Você precisará das seguintes permissões para sua conta de anúncios:


- `ads_read`


## Consultas de exportação assíncronas (preferenciais)


Executar uma consulta de exportação assíncrona usando o parâmetro `export_format=csv` resulta em um arquivo baixado com nomes de colunas que correspondem aos nomes no Gerenciador de Anúncios.


**Observação:** o `time_increment` pode ser definido para 1 dia (ou seja, `1`), Caso contrário, `all_time` será usado por padrão.


### Exemplo de solicitação


```
curl GET \ -F "access_token=<ACCESS_TOKEN>" \ -F "breakdowns=mmm" \ -F “export_format=csv” \ -F "time_increment=1" \ "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights
```
[○](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#)

## Recuperação dos dados de marketing mix modeling


Envie uma chamada de API `GET` para o ponto de extremidade `/insights` com `breakdowns=mmm`.

```
curl GET \ -F "access_token=<ACCESS_TOKEN>" \ -F "breakdowns=mmm" \ "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights"
```


**Observação:** a API de Insights usa valores-padrão para parâmetros não especificados na chamada. Recomendamos usar os parâmetros `time_range` e `date_preset`. Para ampliar ainda mais o detalhamento da resposta, use `time_increment`.


### Exemplo de solicitação


Recuperação dos dados de modelagem diária de marketing mix da última semana:

```
curl GET \ -F "access_token=<ACCESS_TOKEN>" \ -F "breakdowns=mmm" \ -F "date_preset=last_7d" \ -F "time_increment=1” \ "https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/insights"
```


Para saber mais sobre a API de Insights e entender como integrar a API de Marketing, consulte [Guia de início rápido da API de Insights](https://developers.facebook.com/docs/marketing-api/insights).
[○](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#)

## Perguntas sobre o Gerenciador de Negócios


Um caso de uso comum é recuperar dados de marketing mix modeling para um único Gerenciador de Negócios. Essa operação não é diretamente compatível porque a API de Insights funciona para contas de anúncios e níveis inferiores.


Para baixar dados de um Gerenciador de Negócios, primeiro você precisa consultar as contas de anúncios disponíveis com os pontos de extremidade `/owned_ad_accounts` e `/client_ad_accounts`. Depois, itere as identificações de contas de anúncios individuais retornadas para consultar os dados de marketing mix modeling de cada conta.


### Exemplos de solicitação


Usar `/owned_ad_accounts`

```
curl GET \
  -F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<BUSINESS_ID>/owned_ad_accounts"
```


Usar `/client_ad_accounts`

```
curl GET \
  -F "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/v25.0/<BUSINESS_ID>/client_ad_accounts"
```
[○](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#)

## Limites e boas práticas


O detalhamento dos dados de marketing mix modeling gera uma resposta grande, com um número significativo de registros. Isso pode fazer com que suas solicitações expirem durante o cálculo.​ Para resolver esse problema, diminua o tamanho da solicitação usando os parâmetros `time_range` e `filtering` e consulte o tempo total em seções. Para saber mais, leia [Limites e boas práticas da API de Insights](https://developers.facebook.com/docs/marketing-api/insights/best-practices).


Apenas um `filtering` específico compatível para consultar os dados de marketing mix modeling. Somente as combinações de operadores listadas abaixo são permitidas para cada campo. Qualquer outro uso de `filtering` retornará um erro.


| Campo | Operadores permitidos |
| --- | --- |
| campaign.id | IN , NOT_IN |
| campaign.name | CONTAIN , NOT_CONTAIN |
| adset.id | IN , NOT_IN |
| adset.name | CONTAIN , NOT_CONTAIN |
| country | IN |
| region | IN |
| dma | IN |
| device_platform | IN |
| publisher_platform | IN |
| platform_position | IN |


Recomendamos o uso da exportação de dados de marketing mix modeling na interface Relatórios de Anúncios para gerar dados históricos caso a API não seja necessária.


Como alternativa, você pode usar o fluxo de trabalhos assíncronos da API de Insights. Isso cria um trabalho que calcula os dados de forma assíncrona. O ponto de extremidade responderá com o `id` de uma execução de relatório de anúncios, que você poderá usar para consultar o status do trabalho e recuperar os dados computados. **Observação:** algumas solicitações podem expirar, mesmo como um trabalho assíncrono. Para saber mais, consulte [Trabalhos assíncronos da API de Insights](https://developers.facebook.com/docs/marketing-api/insights/best-practices#asynchronous).


Você pode encontrar mapeamentos e ordenação de cabeçalhos de coluna um pouco diferentes da exportação de dados de marketing mix modeling na interface Relatórios de Anúncios. Você também tem total flexibilidade para combinar os dados-padrão do detalhamento de marketing mix modeling com outras tabelas consultadas a partir da API.


| Índice da coluna | Tipo padrão de cabeçalhos de coluna do detalhamento de marketing mix modeling |
| --- | --- |
| 0 | account_id |
| 1 | campaign_id |
| 2 | adset_id |
| 3 | date_start |
| 4 | date_stop |
| 5 | impressions |
| 6 | spend |
| 7 | country |
| 8 | region |
| 9 | dma |
| 10 | device_platform |
| 11 | platform_position |
| 12 | publisher_platform |
| 13 | creative_media_type |

[○](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#)[○](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#)Nesta Página[Detalhamento de marketing mix modeling na API de Insights](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#detalhamento-de-marketing-mix-modeling-na-api-de-insights)[Consultas de exportação assíncronas (preferenciais)](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#consultas-de-exporta--o-ass-ncronas--preferenciais-)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#exemplo-de-solicita--o)[Recuperação dos dados de marketing mix modeling](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#recupera--o-dos-dados-de-marketing-mix-modeling)[Exemplo de solicitação](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#exemplo-de-solicita--o-2)[Perguntas sobre o Gerenciador de Negócios](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#perguntas-sobre-o-gerenciador-de-neg-cios)[Exemplos de solicitação](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#exemplos-de-solicita--o)[Limites e boas práticas](https://developers.facebook.com/docs/marketing-api/insights/marketing-mix-modeling#limites-e-boas-pr-ticas) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XV51eCzfAo6hIRz6sLwAwZ4W12qcvZoven9RoV4sIsnfB4IfcZB-FZ-4SFg_aem_R0NdhcBD0-EKyVdPHnT0kw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66uyB7j8u8HqhKIH7Gs7IAlkmncBuojLbia6sxPWF5f59_kXwFvubNgqvP1g_aem_beL3vgh7zBjk8g9eREKVvw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7D9q28hd_aEz-pr92-aiI3AxE8Z9pqcpG-EEyn6dLGOwHemhEDI0GqxhvYpQ_aem_u-0VuUzajgyOlf1v--Fwhg&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LuKbaTu-oN7SVseBL00sJ-HFCPfC7QlHe9JjqMYDtyNO125o_G29YzSXPrg_aem_I8JfMebDVYmPmmKZah5oKQ&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nOyKjqW6VhVj9CA9W_3W790-ehpBsztvP688_KZ74FFpYDZU2N3QTeczbnQ_aem_4uJAo27dLPdbbkmEyQv_Uw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7D9q28hd_aEz-pr92-aiI3AxE8Z9pqcpG-EEyn6dLGOwHemhEDI0GqxhvYpQ_aem_u-0VuUzajgyOlf1v--Fwhg&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LuKbaTu-oN7SVseBL00sJ-HFCPfC7QlHe9JjqMYDtyNO125o_G29YzSXPrg_aem_I8JfMebDVYmPmmKZah5oKQ&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66uyB7j8u8HqhKIH7Gs7IAlkmncBuojLbia6sxPWF5f59_kXwFvubNgqvP1g_aem_beL3vgh7zBjk8g9eREKVvw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-PFf8QIpcg8Jc4im0jCFgkOw9wer65kY1cemPRmvRBP9gxuAklrsFrtH1-w_aem_wNhwv0443Nda25naxFSA9A&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4LuKbaTu-oN7SVseBL00sJ-HFCPfC7QlHe9JjqMYDtyNO125o_G29YzSXPrg_aem_I8JfMebDVYmPmmKZah5oKQ&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67C_rL1UjneV7ghOtD4sAqgTE7QggNFr9hTB1VWqHXSzUgWIFquUyrDn2oow_aem_ghPM1ykZr6xY99cKfOQlrg&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nOyKjqW6VhVj9CA9W_3W790-ehpBsztvP688_KZ74FFpYDZU2N3QTeczbnQ_aem_4uJAo27dLPdbbkmEyQv_Uw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR67C_rL1UjneV7ghOtD4sAqgTE7QggNFr9hTB1VWqHXSzUgWIFquUyrDn2oow_aem_ghPM1ykZr6xY99cKfOQlrg&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4-PFf8QIpcg8Jc4im0jCFgkOw9wer65kY1cemPRmvRBP9gxuAklrsFrtH1-w_aem_wNhwv0443Nda25naxFSA9A&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Q_tFwk_DF2lIK_MZCLWojky6fBeSTqVQVkxVKDA-bQ7SaRMHD4ZjhVrAGUQ_aem_wvkSw6XmmsTgjYvDc1K8dQ&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7D9q28hd_aEz-pr92-aiI3AxE8Z9pqcpG-EEyn6dLGOwHemhEDI0GqxhvYpQ_aem_u-0VuUzajgyOlf1v--Fwhg&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66uyB7j8u8HqhKIH7Gs7IAlkmncBuojLbia6sxPWF5f59_kXwFvubNgqvP1g_aem_beL3vgh7zBjk8g9eREKVvw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66uyB7j8u8HqhKIH7Gs7IAlkmncBuojLbia6sxPWF5f59_kXwFvubNgqvP1g_aem_beL3vgh7zBjk8g9eREKVvw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66uyB7j8u8HqhKIH7Gs7IAlkmncBuojLbia6sxPWF5f59_kXwFvubNgqvP1g_aem_beL3vgh7zBjk8g9eREKVvw&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4Q_tFwk_DF2lIK_MZCLWojky6fBeSTqVQVkxVKDA-bQ7SaRMHD4ZjhVrAGUQ_aem_wvkSw6XmmsTgjYvDc1K8dQ&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5DffSUMQNUpDQhhQoNfr_0Ek7kIB6Iy3q2FFruu2JYfH3HZzClC1iXKbwuyGxzx0Nk_1C_hRGiRDWA64lKfqmGrs3iOs0pODGSuWr9HtbPaspiPn4KksAcciIcPrK3QoDlLBkMGSe2oRtrILzEgH3lfc4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão