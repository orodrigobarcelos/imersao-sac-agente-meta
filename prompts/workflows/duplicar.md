<workflow name="duplicar">

<when_to_use>
Use este workflow quando o usuario quiser duplicar (copiar) uma campanha, conjunto de anuncios, anuncio ou criativo existente. Exemplos:
- Criar uma copia de uma campanha para testar outro orcamento
- Duplicar um conjunto de anuncios para outra campanha
- Copiar um anuncio para outro conjunto
- Duplicar um criativo com textos diferentes para teste A/B
- Replicar uma campanha que deu certo com pequenas alteracoes

Keywords de ativacao: duplicar, copiar, clonar, replicar, fazer copia, duplicata, igual, mesmo anuncio, mesma campanha, teste AB, variacao, duplicate, copy, clone.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar o que a duplicacao faz, mostrar mapa original vs copia, confirmar antes de executar.
- Avancado: aceitar comandos diretos como "duplica campanha X com orcamento de R$100" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o que quer duplicar (ex: "quero copiar minha campanha de vendas"), identificar o objeto e ir direto para as opcoes.
</user_mode>

<steps>

<step number="1" name="O que duplicar?">
<question>O que voce quer duplicar?</question>
<options>
  <option value="campanha">Campanha | Copia a campanha inteira com todos os conjuntos e anuncios dentro dela</option>
  <option value="adset">Conjunto de anuncios | Copia um conjunto (publico + configuracoes) para a mesma ou outra campanha</option>
  <option value="ad">Anuncio | Copia um anuncio para o mesmo ou outro conjunto</option>
  <option value="criativo">Criativo | Copia um criativo com textos diferentes (otimo para teste A/B de copy)</option>
</options>
<note>Se o usuario ja mencionou o que quer duplicar, pular esta pergunta.</note>
</step>

<step number="2" name="Identificar o objeto original">

<branch condition="usuario NAO especificou qual objeto">
Listar os objetos disponiveis para o usuario escolher.

<tool_calls>
Para campanha: get_campaigns(account_id, status_filter="ACTIVE,PAUSED")
Para conjunto: get_adsets(account_id, campaign_id="[se informou a campanha]", status_filter="ACTIVE,PAUSED")
Para anuncio: get_ads(account_id, campaign_id="[se informou]", adset_id="[se informou]", status_filter="ACTIVE,PAUSED")
Para criativo: get_ad_creatives(ad_id="[se informou o anuncio]")
</tool_calls>

Mostrar lista formatada e perguntar qual duplicar.
</branch>

<branch condition="usuario especificou pelo nome">
Buscar pelo nome e confirmar: "Encontrei '[nome]' (ID: [id]). E esse que voce quer duplicar?"
</branch>
</step>

<step number="3" name="Duplicacao por tipo">

<branch condition="tipo == campanha">
<description>Duplicar campanha</description>
<tool_name>duplicate_campaign</tool_name>

<substep number="3.1" name="Carregar dados da campanha original">
<tool_call>get_campaign_details(campaign_id)</tool_call>

<output_template>
Campanha original:
- Nome: [nome]
- Objetivo: [objetivo]
- Orcamento: R$ [valor]/dia
- Status: [status]
- Conjuntos de anuncios: [N]
- Anuncios: [N total]
</output_template>
</substep>

<substep number="3.2" name="Opcoes de duplicacao">

<question name="sufixo">Qual sufixo voce quer adicionar ao nome da copia?</question>
<default>
Padrao: " - Copia"
Exemplo: "Campanha de Vendas" vira "Campanha de Vendas - Copia"
Ou sugerir com data: " - Copia Abr/2026"
</default>

<question name="escopo">Voce quer duplicar tudo (campanha + conjuntos + anuncios) ou apenas a estrutura da campanha vazia?</question>
<options>
  <option value="tudo">Tudo | include_adsets=true, include_ads=true (recomendado)</option>
  <option value="apenas_campanha">Apenas campanha | include_adsets=false, include_ads=false</option>
  <option value="campanha_e_conjuntos">Campanha + conjuntos sem anuncios | include_adsets=true, include_ads=false</option>
</options>

<question name="orcamento">Quer manter o mesmo orcamento (R$ [valor]/dia) ou alterar?</question>
<note>Se alterar: pedir novo valor.</note>

<question name="status">A copia deve comecar pausada ou ativa?</question>
<if_unknown>Recomendo PAUSADA para voce revisar antes de ativar.</if_unknown>
<default>PAUSED</default>

</substep>

<execution>
<tool_call>
duplicate_campaign(
  campaign_id="[CAMPAIGN_ID]",
  account_id="[ACCOUNT_ID]",
  name_suffix="[SUFIXO]",
  include_adsets=true,
  include_ads=true,
  new_daily_budget=[NOVO_ORCAMENTO],  // em centavos, opcional
  new_status="PAUSED"
)
</tool_call>
<saves>novo campaign_id</saves>
</execution>

<result_template>
Duplicacao concluida!

MAPA: Original -> Copia
==============================

Campanha:
  [Nome original] (ID: [id]) -> [Nome copia] (ID: [novo_id])

Conjuntos de anuncios:
  [Adset 1 original] (ID: [id]) -> [Adset 1 copia] (ID: [novo_id])
  [Adset 2 original] (ID: [id]) -> [Adset 2 copia] (ID: [novo_id])

Anuncios:
  [Ad 1 original] (ID: [id]) -> [Ad 1 copia] (ID: [novo_id])
  [Ad 2 original] (ID: [id]) -> [Ad 2 copia] (ID: [novo_id])
  [Ad 3 original] (ID: [id]) -> [Ad 3 copia] (ID: [novo_id])

Status: PAUSADA
Orcamento: R$ [valor]/dia

Quer ativar a campanha copiada agora?
</result_template>
</branch>

<branch condition="tipo == adset">
<description>Duplicar conjunto de anuncios</description>
<tool_name>duplicate_adset</tool_name>

<substep number="3.1" name="Carregar dados do conjunto original">
<tool_call>get_adset_details(adset_id)</tool_call>

<output_template>
Conjunto original:
- Nome: [nome]
- Campanha: [nome da campanha]
- Publico: [resumo do targeting]
- Orcamento: R$ [valor]/dia (se ABO)
- Otimizacao: [optimization_goal]
- Anuncios: [N]
</output_template>
</substep>

<substep number="3.2" name="Opcoes de duplicacao">

<question name="destino">Quer manter a copia na mesma campanha ou mover para outra?</question>
<options>
  <option value="mesma">Mesma campanha | Nao informar target_campaign_id</option>
  <option value="outra">Outra campanha | Listar campanhas com get_campaigns e perguntar qual. Guardar: target_campaign_id</option>
</options>
<note>Se mover para outra: verificar se o objetivo da campanha destino e compativel com o optimization_goal do adset.</note>

<question name="sufixo">Qual sufixo?</question>
<default>" - Copia"</default>

<question name="publico">Quer alterar o publico da copia?</question>
<note>Se sim: coletar novo targeting (mesma logica do workflow editar).</note>

<question name="orcamento">Quer alterar o orcamento?</question>
<note>Se sim: pedir novo valor.</note>

<question name="status">Status da copia</question>
<default>PAUSED</default>

</substep>

<execution>
<tool_call>
duplicate_adset(
  adset_id="[ADSET_ID]",
  account_id="[ACCOUNT_ID]",
  name_suffix="[SUFIXO]",
  target_campaign_id="[CAMPAIGN_ID]",  // opcional
  new_daily_budget=[NOVO_ORCAMENTO],    // opcional, em centavos
  new_targeting='{"geo_locations":{"countries":["BR"]}}',  // opcional, STRING JSON
  new_status="PAUSED"
)
</tool_call>
</execution>

<result_template>
Conjunto duplicado com sucesso!

Original: [nome original] (ID: [id])
Copia: [nome copia] (ID: [novo_id])
Campanha: [nome da campanha destino]
Status: PAUSADO

[Se incluiu anuncios]: Anuncios copiados: [N]
</result_template>
</branch>

<branch condition="tipo == ad">
<description>Duplicar anuncio</description>
<tool_name>duplicate_ad</tool_name>

<substep number="3.1" name="Carregar dados do anuncio original">
<tool_call>get_ad_details(ad_id)</tool_call>

<output_template>
Anuncio original:
- Nome: [nome]
- Conjunto: [nome do adset]
- Campanha: [nome da campanha]
- Criativo: [nome/ID do criativo]
- Status: [status]
</output_template>
</substep>

<substep number="3.2" name="Opcoes de duplicacao">

<question name="destino">Quer manter a copia no mesmo conjunto ou mover para outro?</question>
<options>
  <option value="mesmo">Mesmo conjunto | Nao informar target_adset_id</option>
  <option value="outro">Outro conjunto | Listar adsets e perguntar qual. Guardar: target_adset_id</option>
</options>

<question name="sufixo">Sufixo do nome</question>
<default>" - Copia"</default>

<question name="status">Status da copia</question>
<default>PAUSED</default>

</substep>

<execution>
<tool_call>
duplicate_ad(
  ad_id="[AD_ID]",
  account_id="[ACCOUNT_ID]",
  name_suffix="[SUFIXO]",
  target_adset_id="[ADSET_ID]",  // opcional
  new_status="PAUSED"
)
</tool_call>
</execution>

<result_template>
Anuncio duplicado com sucesso!

Original: [nome original] (ID: [id])
Copia: [nome copia] (ID: [novo_id])
Conjunto: [nome do adset destino]
Status: PAUSADO
</result_template>
</branch>

<branch condition="tipo == criativo">
<description>Duplicar criativo</description>
<tool_name>duplicate_creative</tool_name>

<substep number="3.1" name="Carregar dados do criativo original">
<tool_call>get_ad_creatives(ad_id)</tool_call>

<output_template>
Criativo original:
- Nome: [nome]
- Tipo: [imagem / video / carrossel]
- Texto principal: "[message]"
- Titulo: "[headline]"
- Descricao: "[description]"
- Link: [link_url]
- Botao: [CTA]
</output_template>
</substep>

<substep number="3.2" name="O que alterar na copia?">
Informar: "Duplicar um criativo e otimo para teste A/B. Voce cria uma copia com um texto ou titulo diferente para ver qual performa melhor."

<question>O que voce quer alterar na copia?</question>
<editable_fields>
  <field name="message">Texto principal | O texto acima da imagem/video</field>
  <field name="headline">Titulo | O texto em negrito abaixo da imagem</field>
  <field name="description">Descricao | Texto abaixo do titulo</field>
  <field name="call_to_action_type">Botao de acao (CTA) | O botao do anuncio</field>
  <field name="link_url">Link | URL de destino</field>
</editable_fields>

<note>Se nao quiser alterar nada: criar copia identica (util para usar em outro adset).</note>
</substep>

<substep number="3.3" name="Mostrar comparacao">
<comparison_template>
Comparacao: Original vs Copia

| Campo           | Original                     | Copia                         |
|-----------------|------------------------------|-------------------------------|
| Texto principal | "Compre agora com 20%..."    | "Ultima chance: 30% OFF"      |
| Titulo          | "Oferta Especial"            | "So Hoje"                     |
| Descricao       | (igual)                      | (igual)                       |
| Link            | (igual)                      | (igual)                       |
| Botao           | (igual)                      | (igual)                       |

Confirma a duplicacao? (sim/nao)
</comparison_template>
</substep>

<execution>
<tool_call>
duplicate_creative(
  creative_id="[CREATIVE_ID]",
  account_id="[ACCOUNT_ID]",
  name_suffix=" - Copia",
  new_message="[NOVO_TEXTO]",            // opcional
  new_headline="[NOVO_TITULO]",          // opcional
  new_description="[NOVA_DESCRICAO]",    // opcional
  new_cta_type="[NOVO_CTA]",            // opcional (LEARN_MORE, SHOP_NOW, etc)
  new_link_url="[NOVO_LINK]"            // opcional
)
</tool_call>
</execution>

<result_template>
Criativo duplicado com sucesso!

Original: [nome original] (ID: [id])
Copia: [nome copia] (ID: [novo_id])

Para usar esse criativo em um teste A/B:
1. Crie um novo anuncio (ad) no mesmo conjunto (adset) usando esse criativo
2. A Meta vai automaticamente distribuir impressoes entre os dois anuncios
3. Apos 3-7 dias, compare os resultados no relatorio de performance

Quer criar um anuncio com esse criativo agora?
</result_template>
</branch>

</step>

</steps>

<auto_fields>
Campos preenchidos automaticamente em todos os tipos:
- account_id: Detectado automaticamente da sessao (conta selecionada no login)
- name_suffix: " - Copia" (padrao, sufixo adicionado ao nome original)
- new_status: PAUSED (padrao, seguranca: revisar antes de ativar)
</auto_fields>

<validations>
- O objeto original existe e o usuario tem permissao
- account_id preenchido
- Se mover adset para outra campanha: objetivo compativel
- Se mover anuncio para outro adset: adset pertence a mesma conta
- Se alterar orcamento: valor em centavos, minimo R$20/dia
- Se alterar targeting: interesses validados (se aplicavel)
- Se duplicar criativo com alteracoes: campos alterados sao validos
- Status da copia definido (padrao PAUSED)
- Nome da copia definido (original + sufixo)
</validations>

<error_handling>
<error code="CampaignNotFound" cause="Campanha nao existe ou sem acesso">
  Solucao: Verificar ID e permissoes
</error>
<error code="IncompatibleObjective" cause="Adset movido para campanha com objetivo diferente">
  Solucao: Mover para campanha com mesmo objetivo ou criar nova campanha
</error>
<error code="BudgetTooLow" cause="Orcamento da copia abaixo do minimo">
  Solucao: Aumentar para pelo menos R$20/dia
</error>
<error code="AudienceLimitReached" cause="Conta com limite de 500 publicos">
  Solucao: Excluir publicos antigos antes de duplicar
</error>
<error code="RateLimit" cause="Muitas duplicacoes em sequencia">
  Solucao: Aguardar alguns segundos entre duplicacoes
</error>
<error code="CreativeLimitReached" cause="Limite de criativos por conta">
  Solucao: Excluir criativos antigos nao utilizados
</error>
<error code="CannotDuplicateDeleted" cause="Tentou duplicar objeto excluido">
  Solucao: Verificar status do objeto original
</error>
<error code="AdsetOptimizationConflict" cause="Adsets com optimization_goals diferentes em campanha CBO">
  Solucao: Garantir que o adset duplicado tem o mesmo optimization_goal dos demais
</error>
</error_handling>

<tools_used>
- get_campaigns: account_id, status_filter
- get_campaign_details: campaign_id
- duplicate_campaign: campaign_id, account_id, name_suffix, include_adsets, include_ads, new_daily_budget, new_status
- get_adsets: account_id, campaign_id, status_filter
- get_adset_details: adset_id
- duplicate_adset: adset_id, account_id, name_suffix, target_campaign_id, new_daily_budget, new_targeting, new_status
- get_ads: account_id, campaign_id, adset_id, status_filter
- get_ad_details: ad_id
- duplicate_ad: ad_id, account_id, name_suffix, target_adset_id, new_status
- get_ad_creatives: ad_id
- duplicate_creative: creative_id, account_id, name_suffix, new_message, new_headline, new_description, new_cta_type, new_link_url
- update_campaign: campaign_id, status="ACTIVE"
- search_interests: query
- validate_interests: interest_ids
</tools_used>

</workflow>
