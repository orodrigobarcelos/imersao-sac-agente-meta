<workflow name="relatorio-performance">

<when_to_use>
O usuario quer ver resultados, metricas, performance, quanto gastou, quanto vendeu, ROAS, retorno sobre investimento, ou qualquer analise numerica das campanhas.

Keywords de ativacao: relatorio, resultados, performance, metricas, quanto gastei, como esta, analise, gastos, vendas, ROAS, retorno, custo, conversoes, cliques, impressoes, alcance, quanto investi, ta dando resultado, vale a pena, esta funcionando.
</when_to_use>

<user_mode>
- Iniciante (padrao): fazer as perguntas guiadas abaixo, uma por vez, com sugestoes claras. Apresentar resultado formatado e com explicacoes.
- Avancado: aceitar comandos diretos como "relatorio last_7d por campanha com breakdown age,gender" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja informou parametros na mensagem inicial (ex: "como estao minhas campanhas esse mes"), extrair os parametros e pular as perguntas ja respondidas.
</user_mode>

<steps>

<step number="1" name="Periodo">
<question>De qual periodo voce quer ver os resultados?</question>
<options>
  <option value="today">Hoje</option>
  <option value="yesterday">Ontem</option>
  <option value="last_7d">Ultimos 7 dias</option>
  <option value="last_14d">Ultimos 14 dias</option>
  <option value="last_30d">Ultimos 30 dias -- recomendado para ter uma visao geral</option>
  <option value="this_month">Este mes</option>
  <option value="last_month">Mes passado</option>
  <option value="custom">Periodo personalizado -- pedir data de inicio e fim (formato: {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"})</option>
  <option value="maximum">Todo o historico</option>
</options>
<if_unknown>Recomendar "ultimos 30 dias" com a justificativa de que da uma visao geral boa sem pegar dados muito antigos.</if_unknown>

IMPORTANTE: Se o periodo retornar dados vazios (sem gastos), tentar automaticamente com `maximum` e informar ao usuario: "Nao encontrei gastos nos ultimos 30 dias. Busquei todo o historico e encontrei dados de [periodo]."
</step>

<step number="2" name="Nivel de detalhe">
<question>Quer ver um resumo geral ou detalhado por campanha?</question>
<options>
  <option value="campaign">Por campanha -- recomendado, mostra cada campanha separada com seus resultados</option>
  <option value="adset">Por conjunto de anuncios -- mostra qual publico esta performando melhor dentro de cada campanha</option>
  <option value="ad">Por anuncio individual -- mostra qual criativo (imagem/video/texto) esta performando melhor</option>
  <option value="account">Resumo geral da conta -- um unico numero total de tudo</option>
</options>
<if_unknown>Recomendar "por campanha" com a justificativa de que permite ver qual campanha esta trazendo mais resultado.</if_unknown>

Caso especifico: se o usuario perguntar sobre uma campanha especifica (ex: "como esta a campanha de vendas"), buscar primeiro as campanhas com `get_campaigns` para identificar o `campaign_id`, depois chamar `get_insights` com `object_id=campaign_id` e `level=adset` para mostrar os conjuntos dentro dela.
</step>

<step number="3" name="Segmentacao (opcional)">
<question>Quer segmentar os resultados para entender melhor o publico? (opcional)</question>
<options>
  <option value="age,gender">Idade e genero -- descobre qual faixa etaria e genero compra mais</option>
  <option value="publisher_platform,platform_position">Plataforma -- compara resultados entre Facebook, Instagram e Threads</option>
  <option value="country">Pais -- util se anuncia para mais de um pais</option>
  <option value="device_platform">Dispositivo -- compara celular vs computador</option>
  <option value="none">Sem segmentacao -- visao geral simples</option>
</options>
<if_unknown>Recomendar "sem segmentacao" para manter o relatorio simples. Mencionar que pode segmentar depois se quiser se aprofundar.</if_unknown>
</step>

<step number="4" name="Multi-conta (se aplicavel)">
Se o usuario tiver mais de uma conta de anuncios vinculada:

<question>Quer ver de uma conta especifica ou de todas as contas juntas?</question>
<options>
  <option value="single">Uma conta especifica -- usar get_insights</option>
  <option value="all">Todas as contas -- usar bulk_get_insights com a lista de account_ids</option>
</options>

Se o usuario tiver apenas uma conta, pular esta pergunta e usar `get_insights` automaticamente.
</step>

<step number="5" name="Buscar dados">
<fills>
object_id: ID da conta (act_XXX) ou campanha/adset/ad especifico -- obrigatorio
time_range: Preset string ou dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"} -- obrigatorio
fields: Metricas separadas por virgula -- obrigatorio
level: campaign, adset, ad, account -- opcional
breakdown: age,gender / publisher_platform,platform_position / country / device_platform -- opcional
action_breakdowns: action_type, action_destination -- opcional
time_increment: 1 para diario, monthly para mensal, all_days para agregado -- opcional
sort: spend_descending para ordenar por gasto (recomendado) -- opcional
filtering: JSON de filtros, ex: [{"field":"spend","operator":"GREATER_THAN","value":"0"}] -- opcional
limit: Numero maximo de resultados (padrao: 100) -- opcional
</fills>

Fields recomendados (usar como padrao):
impressions,clicks,spend,cpc,cpm,ctr,reach,frequency,actions,action_values,conversions,cost_per_action_type,unique_clicks,purchase_roas

Fields extras para video (incluir quando houver campanhas com video):
video_p25_watched_actions,video_p50_watched_actions,video_p75_watched_actions,video_p95_watched_actions,video_p100_watched_actions,video_thruplay_watched_actions

Para multi-conta, usar bulk_get_insights:
<fills>
account_ids: Lista de IDs ["act_XXX", "act_YYY"] -- obrigatorio
time_range: Mesmo formato do get_insights -- obrigatorio
fields: Mesmo formato do get_insights -- obrigatorio
level: campaign, adset, ad, account -- opcional
</fills>
</step>

<step number="6" name="Apresentar relatorio">

Formato obrigatorio:

Relatorio de Performance -- [Periodo em portugues]

---

1. [Nome da Campanha] (Objetivo: [objetivo em portugues])

   - Valor gasto: R$ X.XXX,XX
   - Resultados: X [tipo de resultado]
   - Custo por resultado: R$ X,XX
   - Impressoes: X.XXX | Alcance: X.XXX | CTR: X,XX%
   - CPC: R$ X,XX | CPM: R$ X,XX | Frequencia: X,X

2. [Nome da Campanha seguinte]
   (mesmo formato)

---

Resumo geral:
- Total gasto: R$ X.XXX,XX
- Total de resultados: X [tipo]
- Custo medio por resultado: R$ X,XX

<result_type_mapping>
Mapeamento de tipo de resultado por objetivo (buscar dentro do campo `actions` o valor correspondente):

| Objetivo da campanha              | Campo em actions                                          | Nome para exibir       |
| Mensagens (MESSAGES)              | onsite_conversion.messaging_conversation_started_7d       | conversas iniciadas    |
| Vendas (OUTCOME_SALES)            | purchase ou offsite_conversion.fb_pixel_purchase          | vendas                 |
| Leads (OUTCOME_LEADS)             | lead ou onsite_conversion.lead_grouped                    | leads                  |
| Trafego (OUTCOME_TRAFFIC)         | link_click                                                | cliques no link        |
| Engajamento (OUTCOME_ENGAGEMENT)  | post_engagement                                           | engajamentos           |
| Reconhecimento (OUTCOME_AWARENESS)| usar reach + impressions dos fields principais            | pessoas alcancadas     |
| Cadastros (LEADGEN_FORMS)         | leadgen.other                                             | cadastros              |
| Instalacao de app (APP_INSTALLS)  | app_install                                               | instalacoes            |
| Visualizacao de video (VIDEO_VIEWS)| video_view                                               | visualizacoes de video |

Se o campo `actions` nao tiver o tipo esperado, verificar todos os action_types disponiveis e usar o mais relevante. Informar ao usuario qual metrica foi usada.
</result_type_mapping>

<roas_display>
ROAS (Retorno sobre investimento):

Quando disponivel no campo `purchase_roas` ou `website_purchase_roas`:
- Exibir como: "ROAS: X,XX (a cada R$1 investido, retornaram R$X,XX)"
- Se o ROAS for menor que 1: alertar que a campanha esta com retorno negativo
- Se o ROAS for maior que 3: destacar como boa performance

Quando disponivel o campo `action_values` com valor de `purchase`:
- Calcular faturamento total
- Exibir: "Faturamento: R$ X.XXX,XX"
- Calcular ROAS manual: faturamento / gasto
</roas_display>

<video_metrics>
Metricas de video (quando aplicavel):

Se houver dados de video, adicionar ao relatorio:
   Metricas de video:
   - Visualizacoes de 25%: X.XXX
   - Visualizacoes de 50%: X.XXX
   - Visualizacoes de 75%: X.XXX
   - Visualizacoes de 95%: X.XXX
   - Visualizacoes completas: X.XXX
   - ThruPlays: X.XXX
</video_metrics>

<threads_insights>
Insights do Threads:

Quando o breakdown inclui `publisher_platform,platform_position`, o Threads aparece como:
- publisher_platform: threads
- platform_position: threads_feed

Apresentar na segmentacao por plataforma como "Threads" ao lado de Facebook e Instagram.
</threads_insights>

<age_gender_breakdown>
Segmentacao por idade e genero:

Quando o breakdown for `age,gender`, apresentar em formato de tabela:

| Faixa etaria | Genero    | Gastos    | Resultados | Custo/resultado |
| 25-34        | Feminino  | R$ XX,XX  | XX         | R$ X,XX         |
| 25-34        | Masculino | R$ XX,XX  | XX         | R$ X,XX         |
| 35-44        | Feminino  | R$ XX,XX  | XX         | R$ X,XX         |

Destaque: a faixa [X-Y] [genero] teve o melhor custo por resultado.
</age_gender_breakdown>

</step>

</steps>

<auto_fields>
fields: impressions,clicks,spend,cpc,cpm,ctr,reach,frequency,actions,action_values,conversions,cost_per_action_type,unique_clicks,purchase_roas (padrao automatico)
sort: spend_descending (padrao recomendado)
time_range: fallback para "maximum" se periodo escolhido retornar dados vazios
</auto_fields>

<formatting_rules>
- Moeda: R$ X.XXX,XX (ponto para milhar, virgula para decimal)
- Porcentagem: X,XX%
- Numeros grandes: X.XXX (com ponto para milhar)
- ROAS: X,XX
- Frequencia: X,X (uma casa decimal)
</formatting_rules>

<interpretation_tips>
Dicas de interpretacao (incluir 1 a 3 ao final do relatorio, quando relevante):

- Frequencia alta (acima de 3): "A frequencia esta em X,X, o que significa que cada pessoa viu seu anuncio X vezes em media. Acima de 3, o publico pode estar saturado. Considere trocar o criativo ou ampliar o publico."
- CTR baixo (abaixo de 1%): "O CTR esta em X,XX%, abaixo da media. Isso pode indicar que o criativo nao esta chamando atencao do publico. Considere testar novas imagens ou textos."
- CTR alto (acima de 3%): "O CTR esta em X,XX%, acima da media. Seu criativo esta gerando bastante interesse."
- CPC alto: comparar com media do nicho se possivel.
- ROAS abaixo de 1: "O ROAS esta em X,XX, o que significa que voce esta gastando mais do que esta faturando com essa campanha."
- ROAS acima de 3: "O ROAS esta em X,XX -- excelente. Para cada R$1 investido, voce esta faturando R$X,XX."
- Sem resultados: "Esta campanha nao registrou [tipo de resultado] no periodo. Verifique se o pixel/conversao esta configurado corretamente ou se o periodo e muito curto."
</interpretation_tips>

<validations>
- object_id e obrigatorio (account_id ou ID especifico de campanha/adset/ad)
- time_range e obrigatorio (preset string ou dict com since/until)
- fields e obrigatorio (usar padrao recomendado se nao especificado)
- Se periodo retornar vazio, tentar automaticamente com "maximum"
- Para campanha especifica, buscar campaign_id via get_campaigns antes de chamar get_insights
</validations>

<execution_order>
1. get_campaigns(account_id) -- auxiliar, se usuario mencionar campanha pelo nome
2. get_insights(object_id, time_range, fields, level, breakdown, action_breakdowns, time_increment, sort, filtering, limit)
3. bulk_get_insights(account_ids, time_range, fields, level) -- para multi-conta
</execution_order>

<error_handling>
<error code="no_data" cause="Periodo sem gastos ou dados">Tentar automaticamente com time_range "maximum" e informar ao usuario</error>
<error code="invalid_time_range" cause="Formato de periodo invalido">Usar preset string (last_7d, last_30d, etc.) ou dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}</error>
<error code="invalid_object_id" cause="ID de conta/campanha/adset/ad invalido">Verificar o ID com get_ad_accounts ou get_campaigns</error>
<error code="permission_denied" cause="Token sem permissao de leitura">Verificar se o token tem permissao ads_read ou ads_management</error>
<error code="rate_limit" cause="Muitas chamadas em sequencia">Aguardar alguns segundos e tentar novamente</error>
</error_handling>

<tools_used>
- get_insights: object_id, time_range, fields, level, breakdown, action_breakdowns, time_increment, sort, filtering, limit
- bulk_get_insights: account_ids, time_range, fields, level
- get_campaigns: account_id (auxiliar para identificar campaign_id pelo nome)
</tools_used>

</workflow>
