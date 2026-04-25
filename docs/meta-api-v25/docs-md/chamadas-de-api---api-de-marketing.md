<!-- Fonte: Chamadas de API - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Chamadas de API


Veja exemplos de chamadas de API para usar o mecanismo de regras de anúncio.


## Ler todas as regras de uma conta


```
curl -G   \
-d 'fields=name,evaluation_spec,execution_spec,status'   \
-d 'access_token=<ACCESS_TOKEN>'   \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Ler uma regra


```
curl -G   \
-d 'fields=name,evaluation_spec,execution_spec,status'   \
-d 'access_token=<ACCESS_TOKEN>'   \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Atualizar uma regra


Para atualizar uma especificação, forneça todos os campos, **incluindo os que permanecerão inalterados**. Confira a seguir um exemplo de atualização do gatilho de regras para cada 1.000 impressões. Não é preciso alterar as especificações para atualizar o status de uma regra.

```
curl \
-F 'evaluation_spec={
      "evaluation_type": ...,
      "trigger" : {
        "type": "STATS_MILESTONE",
        "field": "impressions",
        "value": 1000,
        "operator": "EQUAL"
      },
      "filters": ...
     ]
   }' \
-F 'access_token=<ACCESS_TOKEN>'   \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>
```


Confira a seguir um exemplo de atualização dos filtros para selecionar todos os anúncios que receberam mais de 200 cliques. Outros filtros, como `entity_type` e `time_preset`, devem estar nessa atualização.

```
curl \
-F 'evaluation_spec={
      "evaluation_type": ...,
      "filters" : [
       {
         "field": "clicks",
         "value": 200,
         "operator": "GREATER_THAN",
       },
       {
       ...
     ]
   }' \
-F 'access_token=<ACCESS_TOKEN>'   \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Excluir uma regra


```
curl -X DELETE \
-d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Acessar o histórico de execução de uma regra


Existe um ponto de extremidade para acessar dados históricos das execuções de cada regra. Por padrão, ele fornece dados relevantes, como resultados e ações. Você também pode verificar o estado da regra em cada execução para rastrear edições.

```
curl -G   \
-d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>/history
```


Além disso, esse ponto de extremidade é compatível com três mecanismos de filtragem dos dados: `object_id`, `action` e `hide_no_changes`. É possível filtrar os resultados por `object_id` ou `action` para ver dados relacionados apenas a esse tipo de `object_id` ou `action`.


Você também pode filtrar os resultados usando a sinalização `hide_no_changes` a fim de excluir todas as execuções sem nenhuma alteração. Se quiser restringir ainda mais seus resultados, use uma combinação de filtros.

```
curl -G   \
-d 'object_id=123' \
-d 'action=CHANGED_BID' \
-d 'hide_no_changes=true' \
-d "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>/history
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Acessar o histórico de execução de uma conta


Existe um ponto de extremidade que permite acessar dados históricos agregados para todas as regras da sua conta. Por padrão, ele fornece os mesmos dados relevantes que o [histórico de execução da regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#history), mas também inclui a identificação das regras para cada entrada.


Essas entradas são ordenadas da mais recente para a mais antiga. Além disso, esse ponto de extremidade é compatível com os mesmos mecanismos de filtragem citados acima: `object_id`, `action` e `hide_no_changes`.

```
curl -G   \
-d 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_history
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Ver a prévia de uma regra


Existe um ponto de extremidade para visualizar a avaliação de uma [regra baseada em programação](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/scheduled-based-rules). Quando uma solicitação `POST` é enviada, o ponto de extremidade retorna uma lista de objetos que correspondem a todos os filtros da regra especificados naquele momento.

```
curl \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>/preview
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Executar manualmente uma regra


Existe um ponto de extremidade para executar manualmente uma [regra baseada em programação](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/scheduled-based-rules). Quando uma solicitação `POST` é enviada a ele, ocorre o agendamento imediato da regra para execução.

```
curl \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_RULE_ID>/execute
```


Será possível buscar os resultados no histórico quando a execução da regra for concluída.
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)

## Ler as regras que regem um objeto


Existem pontos de extremidade para ler todas as regras que regem cada anúncio, conjunto de anúncios e campanha. Por padrão, uma regra regerá um objeto se ela fizer referência a ele de modo estático pelo filtro `id` ou dinâmico pelo filtro `entity_type`.


Esse ponto de extremidade também é compatível com o campo `pass_evaluation` opcional. Isso permite que você limite ainda mais a lista de regras, dependendo da correspondência do objeto com os filtros da regra naquele momento. Se `pass_evaluation` for `true`, retornaremos todas as regras que, quando são [visualizadas](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#preview), retornam o objeto. Caso seja `false`, retornaremos todas as regras que não resultam na mesma resposta.

```
curl \
-F 'access_token=<ACCESS_TOKEN>' \
https://graph.facebook.com/<VERSION>/<AD_OBJECT_ID>/adrules_governed
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#)Nesta Página[Chamadas de API](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#chamadas-de-api)[Ler todas as regras de uma conta](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#read-all)[Ler uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#read-rule)[Atualizar uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#atualizar-uma-regra)[Excluir uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#excluir-uma-regra)[Acessar o histórico de execução de uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#history)[Acessar o histórico de execução de uma conta](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#account-history)[Ver a prévia de uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#preview)[Executar manualmente uma regra](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#execute)[Ler as regras que regem um objeto](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/api-calls#govern) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4385DXRSvfvMEV-fp_ySH71XYiCBEugUCe3VdQFOoIhcXu517D-pDzuBlnzw_aem_PlZEL0d6yZxANrgGZOoIUg&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-SvKS0BcG64fLPqZwdQ_P8TdHjhw8RUIgcqmF2xTFe6NOe0wPSm4epmeztQ_aem_baJcKxLTJTAr7eRWIlcXdA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR45YNtOyojBI_qPbyHRGPIPyg8dhusET1D1-1LSbxEDHa10NQ5hZSJQmaeK7w_aem_G0S40ffg393sVNxe2qC-5w&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6KhO1tFcEPAfmWUk5mx263mb96zvVhmqFmwEWDmt2qLgXB0EW1g06awG1h8w_aem_QPuq3sBQZv7UhCpWh1aTDQ&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7FhyuvVLeh9WjecJImbaV1lwTo_NBiso-bXCOR1nfbUMr56axZEvpDUK8MDw_aem_ol2wsVJBoDeDKoDNY6gW5g&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6nZeB4LBc1pYRm-vmvy91B0kbQN8O8cIn_e7DhGimzO8OCZtoYh_wE2U_3Kg_aem_ofUvkyQjIZP2Z4id5uiyRQ&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-SvKS0BcG64fLPqZwdQ_P8TdHjhw8RUIgcqmF2xTFe6NOe0wPSm4epmeztQ_aem_baJcKxLTJTAr7eRWIlcXdA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4385DXRSvfvMEV-fp_ySH71XYiCBEugUCe3VdQFOoIhcXu517D-pDzuBlnzw_aem_PlZEL0d6yZxANrgGZOoIUg&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Is_41gKltaQ_X5YXlKVxnUrDaCCuEn_AH54iUub4asq-ZOnVsErMmKdLdhQ_aem_ld5WeDUouAMLKDwvMlBehA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-SvKS0BcG64fLPqZwdQ_P8TdHjhw8RUIgcqmF2xTFe6NOe0wPSm4epmeztQ_aem_baJcKxLTJTAr7eRWIlcXdA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6KhO1tFcEPAfmWUk5mx263mb96zvVhmqFmwEWDmt2qLgXB0EW1g06awG1h8w_aem_QPuq3sBQZv7UhCpWh1aTDQ&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Is_41gKltaQ_X5YXlKVxnUrDaCCuEn_AH54iUub4asq-ZOnVsErMmKdLdhQ_aem_ld5WeDUouAMLKDwvMlBehA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6KhO1tFcEPAfmWUk5mx263mb96zvVhmqFmwEWDmt2qLgXB0EW1g06awG1h8w_aem_QPuq3sBQZv7UhCpWh1aTDQ&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4385DXRSvfvMEV-fp_ySH71XYiCBEugUCe3VdQFOoIhcXu517D-pDzuBlnzw_aem_PlZEL0d6yZxANrgGZOoIUg&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6-SvKS0BcG64fLPqZwdQ_P8TdHjhw8RUIgcqmF2xTFe6NOe0wPSm4epmeztQ_aem_baJcKxLTJTAr7eRWIlcXdA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eOo9iuKJ6ceHiU2YByKtPVyiE7icNKtqKhKtCNENOLDTT3Hampr2-9UO9Vw_aem_0oVANwPH6TxJOSRvT3GMPA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eOo9iuKJ6ceHiU2YByKtPVyiE7icNKtqKhKtCNENOLDTT3Hampr2-9UO9Vw_aem_0oVANwPH6TxJOSRvT3GMPA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4385DXRSvfvMEV-fp_ySH71XYiCBEugUCe3VdQFOoIhcXu517D-pDzuBlnzw_aem_PlZEL0d6yZxANrgGZOoIUg&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6KhO1tFcEPAfmWUk5mx263mb96zvVhmqFmwEWDmt2qLgXB0EW1g06awG1h8w_aem_QPuq3sBQZv7UhCpWh1aTDQ&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6eOo9iuKJ6ceHiU2YByKtPVyiE7icNKtqKhKtCNENOLDTT3Hampr2-9UO9Vw_aem_0oVANwPH6TxJOSRvT3GMPA&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT64DXplmdAuT9HqxBeImChC6A8T_ftoGmFZkdiFTIy9hsRaLWqUgBAburpaFG-0qESScckzJO6pxacIRt441UNAjQjXrAkR94u1hCnyq8H10ED881iIltKzMmLpXc8zeu-rTfUwzMkLQgQVSYHs4cymO1E)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão