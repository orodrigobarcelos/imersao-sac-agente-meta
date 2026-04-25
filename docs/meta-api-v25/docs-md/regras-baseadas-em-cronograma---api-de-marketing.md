<!-- Fonte: Regras baseadas em cronograma - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/scheduled-based-rules -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Regras baseadas em cronograma


Monitore o status dos seus anúncios com uma periodicidade definida para determinar se cumprem os critérios descritos na [`evaluation_spec`](https://developers.facebook.com/docs/marketing-api/ad-rules/evaluation-spec). Para usar regras baseadas em cronograma, é necessário adicionar outra `schedule_spec`.

```
curl \
-F 'name=Rule 1' \
-F 'evaluation_spec={
    ...
   }' \
-F 'execution_spec={
    ...
   }' \
-F 'schedule_spec={
     "schedule_type": "DAILY"
   }' \

-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


## Especificação de cronograma


A `schedule_spec` de uma regra determina a frequência em que ela deve ser executada. Essa periodicidade é indicada no campo `schedule_type`.


| Tipo de cronograma | Descrição |
| --- | --- |
| DAILY | Executar a regra à meia-noite no fuso horário da conta de anúncios. |
| HOURLY | Executar a regra no início de cada hora. |
| SEMI_HOURLY | Executar a regra a cada meia-hora a partir do início de uma hora. |
| CUSTOM ( Exemplo ) | Executar a regra em períodos personalizados. |


Se `schedule_type` for definido como `CUSTOM`, também será necessário especificar a lista de períodos personalizados ou horários em que a regra deve ser executada.


Na lista `schedule`, cada especificação pode conter uma combinação dos seguintes campos. A única exigência é que ao menos um dos parâmetros `start_minute` e `days` esteja presente em cada especificação.


| Campo | Descrição |
| --- | --- |
| start_minute | Horário, em minutos, após às 12 h. Deve ser um múltiplo de 30 minutos. Quando isso é definido e não há end_minute , essa opção determina o horário exato de execução da regra. Caso contrário, end_minute será usado para determinar uma faixa de tempo para executar a regra. Se essa opção não estiver definida, a regra executará SEMI_HOURLY para cada dia especificado em days . |
| end_minute | Horário, em minutos, após às 12 h. Deve ser múltiplo de 30 minutos e ser posterior a start_minute . Se definida, essa opção usa start_minute para determinar a faixa de tempo para executar a regra. Se end_minute for igual a start_minute , essa opção determinará o horário exato de execução da regra. |
| days | Lista de dias para executar a regra. Cada dia deve conter um valor de 0-6 , em que 0 representa domingo, 1 , representa segunda-feira, e assim por diante, com 6 , por fim, representando sábado. Se essa opção não estiver definida, a regra será executada em todos os 7 dias da semana de acordo com start_minute e end_minute , se houver. |


Para obter mais informações sobre como usar os tipos de cronograma `CUSTOM`, acesse [Cronograma avançado](https://developers.facebook.com/docs/marketing-api/ad-rules-examples/advanced-scheduling).


Veja um exemplo de `evaluation_spec`. Esta regra se aplica a todos os objetos da lista inicial de IDs que, nos últimos 7 dias, tiveram mais de `10000` impressões. Nesse caso, não é necessário usar o filtro `entity_type`, já que definimos uma lista estática de objetos iniciais usando um filtro de `id` sem prefixo.

```
curl \
-F 'name=Rule 1' \
-F 'schedule_spec={
    ...
   }' \
-F 'evaluation_spec={
      "evaluation_type" : "SCHEDULE",
      "filters" : [
       {
         "field": "time_preset",
         "value": "LAST_7_DAYS",
         "operator": "EQUAL"
       },
       {
         "field": "effective_status",
         "value": ["ACTIVE"],
         "operator": "IN"
       },
       {
         "field": "id",
         "value": [101, 102, 103],
         "operator": "IN"
       },
       {
         "field": "impressions",
         "value": 10000,
         "operator": "GREATER_THAN"
       }
     ]
   }' \
-F 'execution_spec={
    ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Veja outro exemplo aqui. Esta regra se aplica a todos os conjuntos de anúncio contidos nas campanhas de anúncio com IDs `101, 102, 103` que usam apenas orçamentos totais e foram criadas para durar menos de 48 horas. Nesse caso, não é preciso usar o filtro `time_preset`, já que não há filtros de insights.

```
curl \
-F 'name=Rule 1' \
-F 'schedule_spec={
    ...
   }' \
-F 'evaluation_spec={
      "evaluation_type" : "SCHEDULE",
      "filters" : [
       {
         "field": "entity_type",
         "value": "ADSET",
         "operator": "EQUAL"
       },
       {
         "field": "campaign.id",
         "value": [101, 102, 103],
         "operator": "IN"
       },
       {
         "field": "budget_reset_period",
         "value": ["LIFETIME"],
         "operator": "IN"
       },
       {
         "field": "hours_since_creation",
         "value": 48,
         "operator": "LESS_THAN"
       },
     ]
   }' \
-F 'execution_spec={
    ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Veja um exemplo de `execution_spec` aqui. Esta regra aumenta em 10% o orçamento de todos os objetos correspondentes, com um limite máximo de 5 execuções. Ou seja, para cada objeto correspondente, um aumento de 10% no orçamento só poderia acontecer no máximo cinco vezes.

```
curl \
-F 'name=Rule 1' \
-F 'schedule_spec={
    ...
   }' \
-F 'evaluation_spec={
    ...
   }' \
-F 'execution_spec={
     "execution_type": "CHANGE_BUDGET",
     "execution_options": [
       {
         "field": "change_spec",
         "value": {
           "amount": 10,
           "unit": "PERCENTAGE"
         },
         "operator": "EQUAL"
       },
       {
         "field": "execution_count_limit",
         "value": 5,
         "operator": "EQUAL"
       }
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Veja outro exemplo aqui. Esta regra pausa todos os objetos correspondentes e envia um e-mail a uma lista de usuários.

```
curl \
-F 'name=Rule 1' \
-F 'schedule_spec={
    ...
   }' \
-F 'evaluation_spec={
    ...
   }' \
-F 'execution_spec={
     "execution_type": "PAUSE",
     "execution_options": [
       {
         "field": "user_ids",
         "value": [1001, 1002],
         "operator": "EQUAL"
       }
     ]
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/scheduled-based-rules#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/scheduled-based-rules#)Nesta Página[Regras baseadas em cronograma](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/scheduled-based-rules#regras-baseadas-em-cronograma)[Especificação de cronograma](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/scheduled-based-rules#especifica--o-de-cronograma) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6wn6Xpa3abJJCoEwDqlf4qRAWdy0QzPjTX3pxMegPjzAopbYvBNhH4PA-9Pg_aem__qKh6ERUKPcIkS0Ad3t08w&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4fSp_sYL3ssDt90FAjFW-jqsX-uIZ6mnMbymcG5yxaGsHAbNe3aFtT4V7y_A_aem_OKYQT5FN2bW-mPj8Jzk-PQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4fSp_sYL3ssDt90FAjFW-jqsX-uIZ6mnMbymcG5yxaGsHAbNe3aFtT4V7y_A_aem_OKYQT5FN2bW-mPj8Jzk-PQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5x3O3rMoT_PVzfN3ROKWq4-tSnEkNgy2j4ItwLibtbxpbSLnzIM66xl7ln1g_aem_4thH77EZkkIwIK5Dq3Umsw&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4fSp_sYL3ssDt90FAjFW-jqsX-uIZ6mnMbymcG5yxaGsHAbNe3aFtT4V7y_A_aem_OKYQT5FN2bW-mPj8Jzk-PQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4fSp_sYL3ssDt90FAjFW-jqsX-uIZ6mnMbymcG5yxaGsHAbNe3aFtT4V7y_A_aem_OKYQT5FN2bW-mPj8Jzk-PQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4fSp_sYL3ssDt90FAjFW-jqsX-uIZ6mnMbymcG5yxaGsHAbNe3aFtT4V7y_A_aem_OKYQT5FN2bW-mPj8Jzk-PQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5ALAZgwA8u3ki046BLpGbF3Iu-JJ1tBhDorayIu-RUQFJSs54k7V4c054lIw_aem_CBNfMB5HPL0U4Mzjx3LVoA&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5dwuQzXwKBIj72-2xYp3P9mTYYQ-Un5Z-iseny0DYSr91gC3PScByXZIC4AA_aem_CDO3Y-2ICnTeLUU3ILVYPg&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR61Es2P5Xahv8Y1pRFadlmKnJ9_Fi2yKZgpgJEwYF_mBxZMC84Auf66nQESBQ_aem_3dL7-7a1T9w7FYY7Kz4hvw&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fGQj_8-kaBKLs0KOi_0HWLf-2etNVlpjTggYyoKczAJVScsWBlVjDY_eNKg_aem__n0Cwm_mjw7JiYZ4CMl7Ww&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5fGQj_8-kaBKLs0KOi_0HWLf-2etNVlpjTggYyoKczAJVScsWBlVjDY_eNKg_aem__n0Cwm_mjw7JiYZ4CMl7Ww&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4HVS9rh0YnlTYYcujnP-SOKsITik18jHYnez--br4GmBRxr1R5-LuOPZb5qA_aem_4TmVfuDDMt8qVdrCTjGwHQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5TeifbKn7Xj4CTEOF0nVzI9Z8kVLcDtWqVKVB61a9AMTJm_-eFcZ4pCCy2Cw_aem_G0JMNoE1RcnnI3pXfDnSRQ&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6wn6Xpa3abJJCoEwDqlf4qRAWdy0QzPjTX3pxMegPjzAopbYvBNhH4PA-9Pg_aem__qKh6ERUKPcIkS0Ad3t08w&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4UfW_h8ZdjmEMvWAv1_X9Sad8DI1TJwLbUCjrqf_liY5jgoDx-neNpPQktjZ3ElvE8q-vFqlwiPOTkH2y30JL3VUZ3OmVME50yBeMR14jtdJmwgoReMuWEgoFVstKKjg35z6xXf7J58ZzLhnz-iEP6HXI)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão