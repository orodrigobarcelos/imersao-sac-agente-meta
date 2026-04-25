<workflow name="editar">

<when_to_use>
Use este workflow quando o usuario quiser alterar alguma configuracao de uma campanha, conjunto de anuncios, anuncio ou criativo ja existente. Exemplos:
- Mudar o orcamento de uma campanha
- Pausar ou ativar uma campanha/conjunto/anuncio
- Alterar o publico-alvo de um conjunto de anuncios
- Trocar o texto ou imagem de um anuncio
- Mudar o nome de qualquer elemento
- Ajustar a estrategia de lance

Keywords de ativacao: editar, alterar, mudar, trocar, atualizar, ajustar, modificar, aumentar orcamento, diminuir orcamento, pausar, ativar, desativar, renomear, mudar texto, mudar imagem, mudar publico, mudar lance, edit, update.
</when_to_use>

<user_mode>
- Iniciante (padrao): mostrar valores atuais antes de alterar, explicar impacto de cada mudanca, confirmar antes de executar.
- Avancado: aceitar comandos diretos como "pausa a campanha X" ou "muda orcamento do adset Y para R$50" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o que quer editar (ex: "quero pausar minha campanha de vendas"), identificar o objeto e ir direto para a acao.
</user_mode>

<steps>

<step number="1" name="O que editar?">
<question>O que voce quer editar?</question>
<options>
  <option value="campanha">Campanha | Alterar nome, orcamento, status ou estrategia de lance da campanha</option>
  <option value="adset">Conjunto de anuncios | Alterar publico, orcamento, lance ou otimizacao de um conjunto</option>
  <option value="ad">Anuncio | Alterar nome, status ou trocar o criativo de um anuncio</option>
  <option value="criativo">Criativo | Alterar texto, titulo, descricao, botao ou link de um criativo</option>
</options>
<note>Se o usuario ja mencionou o que quer editar, pular esta pergunta.</note>
</step>

<step number="2" name="Identificar o objeto">

<branch condition="usuario NAO especificou qual objeto">
Listar os objetos disponiveis para o usuario escolher.

<tool_calls>
Para campanha: get_campaigns(account_id, status_filter="ACTIVE,PAUSED")
Para conjunto: get_adsets(account_id, campaign_id="[se informou a campanha]", status_filter="ACTIVE,PAUSED")
Para anuncio: get_ads(account_id, campaign_id="[se informou]", adset_id="[se informou]", status_filter="ACTIVE,PAUSED")
</tool_calls>

Mostrar lista formatada e perguntar qual editar.
</branch>

<branch condition="usuario especificou pelo nome">
Buscar pelo nome e confirmar: "Encontrei '[nome]' (ID: [id]). E esse que voce quer editar?"
</branch>
</step>

<step number="3" name="Edicao por tipo">

<branch condition="tipo == campanha">
<description>Editar campanha</description>
<tools>get_campaign_details + update_campaign</tools>

<substep number="3.1" name="Carregar dados atuais">
<tool_call>get_campaign_details(campaign_id)</tool_call>

<output_template>
Campanha: [nome]
Status: [ATIVA / PAUSADA]
Objetivo: [objetivo em portugues]
Orcamento diario: R$ [valor]
Estrategia de lance: [estrategia]
Limite de gasto: [valor ou "sem limite"]
</output_template>
</substep>

<substep number="3.2" name="O que alterar?">
<question>O que voce quer alterar nessa campanha?</question>
<editable_fields>
  <field name="name" param="name">Nome | Qualquer texto</field>
  <field name="status" param="status">Status | PAUSED ou ACTIVE</field>
  <field name="daily_budget" param="daily_budget">Orcamento diario | Em centavos. Minimo R$20/dia</field>
  <field name="lifetime_budget" param="lifetime_budget">Orcamento vitalicio | Em centavos. Nao pode trocar de daily para lifetime</field>
  <field name="bid_strategy" param="bid_strategy">Estrategia de lance | LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP</field>
  <field name="spend_cap" param="spend_cap">Limite de gasto | Em centavos. Limite total de gasto da campanha</field>
</editable_fields>

<restrictions>
- NAO e possivel trocar de orcamento diario para orcamento vitalicio (ou vice-versa) apos a campanha ser criada.
- NAO e possivel mudar o objetivo da campanha apos a criacao.
- Ao mudar orcamento, o novo valor entra em vigor imediatamente.
</restrictions>
</substep>

<substep number="3.3" name="Confirmacao para ativacao">
<branch condition="status PAUSED -> ACTIVE">
<question>Tem certeza que quer ativar essa campanha? Ela vai comecar a gastar o orcamento imediatamente.</question>
Mostrar o orcamento diario que sera gasto.
</branch>

<branch condition="status ACTIVE -> PAUSED">
Informar: "A campanha sera pausada imediatamente. Anuncios em andamento param de ser exibidos, mas podem levar ate 30 minutos para parar completamente."
</branch>
</substep>

<execution>
<tool_call>
update_campaign(
  campaign_id="[CAMPAIGN_ID]",
  name="[NOVO_NOME]",          // se alterou
  status="[NOVO_STATUS]",      // se alterou
  daily_budget=[NOVO_VALOR],   // se alterou (em centavos)
  bid_strategy="[NOVA_ESTRATEGIA]",  // se alterou
  spend_cap=[NOVO_LIMITE]      // se alterou (em centavos)
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == adset">
<description>Editar conjunto de anuncios</description>
<tools>get_adset_details + update_adset</tools>

<substep number="3.1" name="Carregar dados atuais">
<tool_call>get_adset_details(adset_id)</tool_call>

<output_template>
Conjunto: [nome]
Campanha: [nome da campanha]
Status: [ATIVO / PAUSADO]
Orcamento diario: R$ [valor] (se ABO)
Otimizacao: [optimization_goal em portugues]
Estrategia de lance: [estrategia]
Valor do lance: R$ [valor] (se aplicavel)

Publico-alvo:
- Idade: [min] a [max] anos
- Genero: [genero]
- Localizacao: [locais]
- Interesses: [lista de interesses]
- Publicos personalizados: [lista]
- Exclusoes: [lista]
</output_template>
</substep>

<substep number="3.2" name="O que alterar?">
<question>O que voce quer alterar nesse conjunto?</question>
<editable_fields>
  <field name="name" param="name">Nome | Qualquer texto</field>
  <field name="status" param="status">Status | PAUSED ou ACTIVE</field>
  <field name="daily_budget" param="daily_budget">Orcamento diario | Em centavos. Apenas se a campanha e ABO</field>
  <field name="targeting" param="targeting">Publico-alvo | Pode alterar idade, genero, localizacao, interesses, publicos</field>
  <field name="bid_strategy" param="bid_strategy">Estrategia de lance | LOWEST_COST_WITHOUT_CAP, COST_CAP, BID_CAP</field>
  <field name="bid_amount" param="bid_amount">Valor do lance | Em centavos. So funciona com COST_CAP ou BID_CAP</field>
  <field name="optimization_goal" param="optimization_goal">Objetivo de otimizacao | Pode alterar mas pode impactar performance</field>
  <field name="is_dynamic_creative" param="is_dynamic_creative">Criativo dinamico | true ou false</field>
</editable_fields>

<restrictions>
- NAO e possivel editar o pixel ou evento de conversao apos o adset ser publicado (sair de rascunho).
- Se a campanha usa CBO (orcamento automatico), o orcamento e definido na campanha, nao no adset.
- Alterar o publico-alvo de um adset ativo reinicia a fase de aprendizado da Meta (pode ficar mais caro por alguns dias).
</restrictions>
</substep>

<substep number="3.3" name="Sub-fluxo: Editar publico-alvo">
<condition>usuario quer alterar o targeting</condition>

<process>
1. Mostrar o targeting atual detalhado.
2. Perguntar o que quer mudar (idade, genero, localizacao, interesses, publicos).
3. Se alterar interesses: buscar novos com search_interests(query), validar com validate_interests(interest_ids).
4. Se alterar publicos personalizados: listar com list_custom_audiences(account_id).
5. Montar o novo targeting completo (nao e possivel enviar apenas o campo alterado -- enviar o targeting inteiro).
6. Estimar tamanho do novo publico com estimate_audience_size(account_id, targeting).
</process>

<critical_rule>Ao usar flexible_spec com interesses, SEMPRE incluir targeting_automation.advantage_audience = 0 no targeting (obrigatorio na v25.0).</critical_rule>
</substep>

<execution>
<tool_call>
update_adset(
  adset_id="[ADSET_ID]",
  name="[NOVO_NOME]",           // se alterou
  status="[NOVO_STATUS]",       // se alterou
  daily_budget=[NOVO_VALOR],    // se alterou (em centavos)
  targeting={...},              // se alterou (targeting completo)
  bid_strategy="[NOVA_ESTRATEGIA]",  // se alterou
  bid_amount=[NOVO_VALOR],      // se alterou (em centavos)
  optimization_goal="[NOVO]",   // se alterou
  is_dynamic_creative=[VALOR]   // se alterou
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == ad">
<description>Editar anuncio</description>
<tools>get_ad_details + update_ad</tools>

<substep number="3.1" name="Carregar dados atuais">
<tool_call>get_ad_details(ad_id)</tool_call>

<output_template>
Anuncio: [nome]
Conjunto: [nome do adset]
Campanha: [nome da campanha]
Status: [ATIVO / PAUSADO]
Criativo: [nome ou ID do criativo]
</output_template>
</substep>

<substep number="3.2" name="O que alterar?">
<editable_fields>
  <field name="name" param="name">Nome | Qualquer texto</field>
  <field name="status" param="status">Status | PAUSED ou ACTIVE</field>
  <field name="creative_id" param="creative_id">Criativo | Trocar por outro criativo ja existente</field>
</editable_fields>

<note>Para trocar o criativo: listar criativos disponiveis ou perguntar o creative_id. Se o usuario quer um criativo novo, redirecionar para o workflow de criar criativo.</note>
</substep>

<execution>
<tool_call>
update_ad(
  ad_id="[AD_ID]",
  name="[NOVO_NOME]",         // se alterou
  status="[NOVO_STATUS]",     // se alterou
  creative_id="[NOVO_CREATIVE_ID]"  // se alterou
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == criativo">
<description>Editar criativo</description>
<tools>get_ad_creatives + update_ad_creative</tools>

<substep number="3.1" name="Carregar dados atuais">
<tool_call>get_ad_creatives(ad_id)</tool_call>

<output_template>
Criativo: [nome]
Tipo: [imagem / video / carrossel]

Texto principal: "[message]"
Titulo: "[headline]"
Descricao: "[description]"
Link: [link_url]
Botao: [call_to_action traduzido]
UTM: [url_tags]
Midia: [descricao - imagem HASH, video ID, etc.]
</output_template>
</substep>

<substep number="3.2" name="O que alterar?">
<editable_fields>
  <field name="message" param="message">Texto principal | O texto que aparece acima da imagem/video</field>
  <field name="name" param="name (headline)">Titulo | O texto em negrito abaixo da imagem</field>
  <field name="description" param="description">Descricao | Texto abaixo do titulo</field>
  <field name="call_to_action_type" param="call_to_action_type">Botao de acao | Deve ser compativel com o objetivo</field>
  <field name="link_url" param="link_url">Link | URL de destino</field>
  <field name="url_tags" param="url_tags">UTM tags | Parametros de rastreamento</field>
</editable_fields>

<note>Para trocar a imagem ou video de um criativo, e mais simples criar um novo criativo. A Meta nao permite alterar a midia de um criativo existente com facilidade.</note>
</substep>

<substep number="3.3" name="Mostrar comparacao">
<comparison_template>
Alteracoes:

| Campo          | Valor atual                | Novo valor                  |
|----------------|----------------------------|-----------------------------|
| Texto principal| "Compre agora com 20%..."  | "Aproveite 30% de desconto" |
| Titulo         | "Oferta Especial"          | "Ultima Chance"             |

Confirma as alteracoes? (sim/nao)
</comparison_template>
</substep>

<execution>
<tool_call>
update_ad_creative(
  creative_id="[CREATIVE_ID]",
  message="[NOVO_TEXTO]",              // se alterou
  name="[NOVO_TITULO]",                // se alterou
  description="[NOVA_DESCRICAO]",      // se alterou
  call_to_action_type="[NOVO_CTA]",    // se alterou
  url_tags="[NOVO_UTM]"                // se alterou
)
</tool_call>
</execution>
</branch>

</step>

<step number="4" name="Resultado">
<result_template>
Alteracao realizada com sucesso!

[Tipo]: [nome]
Campos alterados: [lista de campos]

[Se mudou status para ACTIVE]: A campanha/conjunto/anuncio esta ativo e vai comecar a gastar.
[Se mudou status para PAUSED]: A campanha/conjunto/anuncio foi pausado.
[Se mudou orcamento]: O novo orcamento de R$ [valor]/dia entra em vigor imediatamente.
[Se mudou publico]: A Meta vai recalcular o publico. A fase de aprendizado pode reiniciar (performance pode oscilar por 2-3 dias).
</result_template>

<question>Quer fazer mais alguma alteracao?</question>
</step>

</steps>

<auto_fields>
Campos preenchidos automaticamente:
- account_id: Detectado automaticamente da sessao (conta selecionada no login)
- campaign_id: Obtido via get_campaigns ou informado pelo usuario (identificacao da campanha)
- adset_id: Obtido via get_adsets ou informado pelo usuario (identificacao do conjunto)
- ad_id: Obtido via get_ads ou informado pelo usuario (identificacao do anuncio)
- creative_id: Obtido via get_ad_creatives ou informado pelo usuario (identificacao do criativo)
</auto_fields>

<validations>
- O objeto existe e o usuario tem permissao para editar
- Valores de orcamento em centavos (R$50 = 5000)
- Orcamento diario minimo de R$20/dia por adset
- Status valido (ACTIVE ou PAUSED)
- Se alterou targeting com interesses: interesses validados com validate_interests
- Se alterou targeting com interesses: targeting_automation.advantage_audience = 0 incluido
- Se ativar (PAUSED -> ACTIVE): confirmacao do usuario
- Se editar criativo: campos alterados sao editaveis (midia nao e)
- bid_amount informado apenas se bid_strategy for COST_CAP ou BID_CAP
- Nao tentar trocar daily_budget para lifetime_budget (ou vice-versa)
- Nao tentar mudar objective da campanha
</validations>

<error_handling>
<error code="CannotChangeBudgetType" cause="Tentou trocar daily para lifetime">
  Solucao: Informar que nao e possivel alterar o tipo de orcamento apos criacao
</error>
<error code="CannotChangeObjective" cause="Tentou mudar objetivo">
  Solucao: Informar que o objetivo e definido na criacao e nao pode ser alterado. Sugerir criar nova campanha
</error>
<error code="BudgetTooLow" cause="Orcamento abaixo do minimo">
  Solucao: Aumentar para pelo menos R$20/dia
</error>
<error code="LearningPhaseReset" cause="Alteracao significativa no adset">
  Solucao: Informar que e normal e a performance vai estabilizar em 2-3 dias
</error>
<error code="InvalidInterest" cause="Interesse removido pela Meta">
  Solucao: Buscar alternativa com search_interests
</error>
<error code="CannotEditPublishedAdsetPixel" cause="Tentou alterar pixel de adset publicado">
  Solucao: Informar que nao e possivel. Sugerir criar novo adset
</error>
<error code="AdCreativeCannotBeModified" cause="Tentou alterar campo nao editavel do criativo">
  Solucao: Sugerir criar novo criativo
</error>
<error code="ConflictingOptimizationGoals" cause="Adsets com optimization_goals diferentes na mesma campanha CBO">
  Solucao: Todos os adsets devem ter o mesmo optimization_goal em campanhas CBO
</error>
</error_handling>

<tools_used>
- get_campaigns: account_id, status_filter
- get_campaign_details: campaign_id
- update_campaign: campaign_id, name, status, daily_budget, bid_strategy, spend_cap
- get_adsets: account_id, campaign_id, status_filter
- get_adset_details: adset_id
- update_adset: adset_id, name, status, daily_budget, targeting, bid_strategy, bid_amount, optimization_goal
- get_ads: account_id, campaign_id, adset_id, status_filter
- get_ad_details: ad_id
- update_ad: ad_id, name, status, creative_id
- get_ad_creatives: ad_id
- update_ad_creative: creative_id, message, name, description, call_to_action_type, url_tags
- search_interests: query
- validate_interests: interest_ids
- list_custom_audiences: account_id
- estimate_audience_size: account_id, targeting
</tools_used>

</workflow>
