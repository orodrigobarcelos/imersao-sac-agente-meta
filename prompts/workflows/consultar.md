<workflow name="consultar">

<when_to_use>
O usuario quer ver o que tem na conta de anuncios: campanhas criadas, conjuntos de anuncios, anuncios, publicos, imagens, videos, pixels, conversoes ou testes A/B.

Keywords de ativacao: listar, mostrar, consultar, ver, quais, minhas campanhas, meus publicos, status, o que tem, o que tenho, ativas, pausadas, arquivadas, publico, criativo, pixel, conversao, teste AB, imagens, videos
</when_to_use>

<user_mode>
- Iniciante (padrao): perguntar o que o usuario quer consultar, apresentar resultado formatado com explicacoes simples.
- Avancado: aceitar comandos diretos como "lista campanhas ativas" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o que quer ver (ex: "mostra meus publicos"), pular a pergunta e executar direto.
</user_mode>

<steps>

<step number="1" name="O que consultar?">
<question>O que voce gostaria de consultar na sua conta?</question>
<options>
  <option value="campanhas">Campanhas | Ver todas as campanhas criadas, status e objetivo</option>
  <option value="adsets">Conjuntos de anuncios | Ver os publicos e orcamentos dentro de uma campanha</option>
  <option value="ads">Anuncios | Ver os criativos (imagens, textos, videos) que estao rodando</option>
  <option value="publicos">Publicos | Ver publicos personalizados e salvos</option>
  <option value="midias">Midias | Ver videos enviados na conta</option>
  <option value="pixel">Pixel | Ver pixels instalados e status</option>
  <option value="conversoes">Conversoes personalizadas | Ver eventos de conversao configurados</option>
  <option value="testes_ab">Testes A/B | Ver testes em andamento ou finalizados</option>
</options>
</step>

<step number="2" name="Consultas detalhadas">

<branch condition="consulta == campanhas">
<description>Campanhas</description>
<tool_name>get_campaigns</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="status_filter" required="false">Filtrar por status: ACTIVE, PAUSED, ARCHIVED</param>
  <param name="limit" required="false">Numero maximo de campanhas (padrao: 100)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<follow_up_questions>
- "Quer ver todas ou so as ativas?" -- se responder "ativas", usar status_filter=ACTIVE
- "Quer ver detalhes de alguma campanha especifica?" -- se sim, usar get_campaign_details
</follow_up_questions>

<output_template>
Suas campanhas:

| #  | Nome                    | Status  | Objetivo    | Orcamento/dia |
|----|-------------------------|---------|-------------|---------------|
| 1  | Campanha de Vendas      | ATIVA   | Vendas      | R$ 50,00      |
| 2  | Campanha de Leads       | PAUSADA | Leads       | R$ 30,00      |
| 3  | Remarketing             | ATIVA   | Vendas      | R$ 25,00      |

Total: 3 campanhas (2 ativas, 1 pausada)
</output_template>

<translations name="status">
  <translate from="ACTIVE" to="Ativa" />
  <translate from="PAUSED" to="Pausada" />
  <translate from="ARCHIVED" to="Arquivada" />
  <translate from="DELETED" to="Excluida" />
</translations>

<translations name="objectives">
  <translate from="OUTCOME_SALES" to="Vendas" />
  <translate from="OUTCOME_LEADS" to="Leads / Cadastros" />
  <translate from="OUTCOME_TRAFFIC" to="Trafego" />
  <translate from="OUTCOME_ENGAGEMENT" to="Engajamento" />
  <translate from="OUTCOME_AWARENESS" to="Reconhecimento de marca" />
  <translate from="MESSAGES" to="Mensagens" />
  <translate from="APP_INSTALLS" to="Instalacao de app" />
  <translate from="VIDEO_VIEWS" to="Visualizacoes de video" />
</translations>

<detail_view>
<tool_name>get_campaign_details</tool_name>
<parameters>
  <param name="campaign_id" required="true">ID da campanha</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>
Apresentar: nome, status, objetivo, orcamento, data de inicio, data de fim (se houver), estrategia de lance, tipo de compra, special_ad_categories.
</detail_view>
</branch>

<branch condition="consulta == adsets">
<description>Conjuntos de anuncios (adsets)</description>
<tool_name>get_adsets</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="campaign_id" required="false">Filtrar por campanha especifica</param>
  <param name="status_filter" required="false">ACTIVE, PAUSED, ARCHIVED</param>
  <param name="limit" required="false">Numero maximo de resultados (padrao: 100)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<follow_up_questions>
- "De qual campanha voce quer ver os conjuntos?" -- se o usuario tiver mais de uma campanha, perguntar. Caso contrario, buscar todos.
- "Quer ver o publico-alvo detalhado de algum conjunto?" -- se sim, usar get_adset_details
</follow_up_questions>

<output_template>
Conjuntos de anuncios da campanha "[Nome]":

| #  | Nome              | Status | Orcamento/dia | Otimizacao       | Publico resumido          |
|----|-------------------|--------|---------------|------------------|---------------------------|
| 1  | Mulheres 25-44    | ATIVO  | R$ 25,00      | Conversoes       | Feminino, 25-44, SP       |
| 2  | Remarketing site  | ATIVO  | R$ 25,00      | Conversoes       | Visitantes do site 30d    |

Total: 2 conjuntos (2 ativos)
</output_template>

<detail_view>
<tool_name>get_adset_details</tool_name>
<parameters>
  <param name="adset_id" required="true">ID do conjunto de anuncios</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>
Apresentar: nome, status, orcamento, otimizacao, evento de conversao, targeting completo (idade, genero, localizacao, interesses, publicos personalizados, exclusoes), posicionamentos, agendamento.
</detail_view>

<translations name="targeting">
  <translate from="geo_locations.cities" to="Cidades" />
  <translate from="geo_locations.regions" to="Estados" />
  <translate from="geo_locations.countries" to="Paises" />
  <translate from="age_min / age_max" to="Faixa etaria" />
  <translate from="genders" to="Genero (1=Masculino, 2=Feminino, 0=Todos)" />
  <translate from="flexible_spec" to="Interesses e comportamentos" />
  <translate from="custom_audiences" to="Publicos personalizados" />
  <translate from="excluded_custom_audiences" to="Publicos excluidos" />
</translations>
</branch>

<branch condition="consulta == ads">
<description>Anuncios</description>
<tool_name>get_ads</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="campaign_id" required="false">Filtrar por campanha</param>
  <param name="adset_id" required="false">Filtrar por conjunto de anuncios</param>
  <param name="status_filter" required="false">ACTIVE, PAUSED, ARCHIVED</param>
  <param name="limit" required="false">Numero maximo de resultados (padrao: 100)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<follow_up_questions>
- "De qual campanha ou conjunto voce quer ver os anuncios?" -- ajuda a filtrar
- "Quer ver o criativo (imagem/texto) de algum anuncio?" -- se sim, usar get_ad_creatives
</follow_up_questions>

<output_template>
Anuncios da campanha "[Nome]":

| #  | Nome                | Status | Conjunto           |
|----|---------------------|--------|--------------------|
| 1  | Video depoimento    | ATIVO  | Mulheres 25-44     |
| 2  | Carrossel produtos  | ATIVO  | Remarketing site   |
| 3  | Imagem oferta       | PAUSADO| Mulheres 25-44     |

Total: 3 anuncios (2 ativos, 1 pausado)
</output_template>

<detail_view name="criativo">
<tool_name>get_ad_creatives</tool_name>
<parameters>
  <param name="ad_id" required="true">ID do anuncio</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>
Apresentar: texto principal (body/message), titulo, descricao, call to action, link de destino, URL da imagem/video, formato (imagem unica, carrossel, video).
</detail_view>

<detail_view name="imagem">
<tool_name>get_ad_image</tool_name>
<parameters>
  <param name="ad_id" required="true">ID do anuncio</param>
</parameters>
NOTA: A tool recebe o ID do anuncio (nao da imagem). Ela descobre o criativo e a imagem automaticamente.
</detail_view>
</branch>

<branch condition="consulta == publicos">
<description>Publicos personalizados</description>
<tool_name>list_custom_audiences</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="limit" required="false">Numero maximo de resultados (padrao: 100)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<output_template>
Seus publicos personalizados:

| #  | Nome                          | Tipo             | Tamanho aprox. | Status       |
|----|-------------------------------|------------------|----------------|--------------|
| 1  | Engajamento Instagram 365D    | Instagram        | ~5.000         | Pronto       |
| 2  | Visitantes do site 30D        | Website (Pixel)  | ~12.000        | Pronto       |
| 3  | Lista de clientes             | Lista enviada    | ~3.500         | Pronto       |
| 4  | LAL 1% - Compradores BR      | Lookalike        | ~1.200.000     | Pronto       |
| 5  | Engajamento Facebook 90D      | Facebook         | ~8.000         | Muito pequeno|

Total: 5 publicos
</output_template>

<translations name="subtype">
  <translate from="WEBSITE" to="Website (Pixel) -- pessoas que visitaram seu site" />
  <translate from="ENGAGEMENT" to="Engajamento -- pessoas que interagiram com seu conteudo" />
  <translate from="IG_BUSINESS" to="Instagram -- pessoas que interagiram no Instagram" />
  <translate from="CUSTOM" to="Lista enviada -- lista de clientes que voce enviou" />
  <translate from="LOOKALIKE" to="Lookalike (publico semelhante) -- pessoas parecidas com outro publico" />
  <translate from="VIDEO" to="Video -- pessoas que assistiram seus videos" />
  <translate from="OFFLINE" to="Offline -- conversoes offline" />
  <translate from="APP" to="Aplicativo -- usuarios do seu app" />
</translations>

<translations name="delivery_status">
  <translate from="ready" to="Pronto para uso" />
  <translate from="too_small" to="Muito pequeno (precisa de mais pessoas)" />
  <translate from="updating" to="Atualizando" />
  <translate from="expired" to="Expirado" />
</translations>

<note>Incluir o campo approximate_count como tamanho aproximado. Formatar numeros grandes com ponto de milhar.</note>
</branch>

<branch condition="consulta == publicos_salvos">
<description>Publicos salvos</description>
<tool_name>list_saved_audiences</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="limit" required="false">Numero maximo de resultados (padrao: 100)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<output_template>
Seus publicos salvos:

| #  | Nome                     | Targeting resumido                           |
|----|--------------------------|----------------------------------------------|
| 1  | Mulheres SP 25-44        | Feminino, 25-44, Sao Paulo, interesse: moda  |
| 2  | Homens Brasil 18+        | Masculino, 18-65, Brasil                     |

Total: 2 publicos salvos
</output_template>

<note>Resumir o targeting de forma legivel: genero, faixa etaria, localizacao e principais interesses.</note>
</branch>

<branch condition="consulta == midias">
<description>Midias (videos)</description>
<tool_name>get_account_videos</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="limit" required="false">Numero maximo de resultados (padrao: 25)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<output_template>
Videos na conta:

| #  | Titulo / Nome           | Duracao | Data de upload |
|----|-------------------------|---------|----------------|
| 1  | Video depoimento Maria  | 0:45    | 15/03/2026     |
| 2  | Apresentacao produto    | 1:30    | 10/03/2026     |

Total: 2 videos
</output_template>

<formatting>
- Formatar duracao em minutos:segundos.
- Formatar data no padrao brasileiro (DD/MM/AAAA).
</formatting>

<note>NOTA sobre imagens: imagens nao ficam listadas separadamente na conta. Elas estao vinculadas aos criativos dos anuncios. Para ver imagens, consultar os anuncios com get_ad_creatives.</note>
</branch>

<branch condition="consulta == pixel">
<description>Pixels</description>
<tool_name>get_pixels</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<output_template>
Pixels da conta:

| #  | Nome               | ID              | Ultima atividade       |
|----|--------------------|-----------------|------------------------|
| 1  | Pixel Principal    | 123456789012345 | 01/04/2026 as 14:30    |

Total: 1 pixel
</output_template>

<status_messages>
- Se last_fired_time for recente (ultimas 24h): "O pixel esta ativo e recebendo dados normalmente."
- Se last_fired_time for antigo (mais de 7 dias): "O pixel nao recebe dados ha [X] dias. Verifique se ele esta instalado corretamente no seu site."
- Se nao tiver last_fired_time: "O pixel nunca disparou. Ele precisa ser instalado no seu site."
</status_messages>
</branch>

<branch condition="consulta == conversoes">
<description>Conversoes personalizadas</description>
<tool_name>list_custom_conversions</tool_name>

<parameters>
  <param name="account_id" required="true">ID da conta de anuncios (act_XXX)</param>
  <param name="fields" required="false">Campos extras separados por virgula</param>
</parameters>

<output_template>
Conversoes personalizadas:

| #  | Nome                 | Evento base    | Regra URL                    | Valor padrao |
|----|----------------------|----------------|------------------------------|--------------|
| 1  | Compra finalizada    | Purchase       | contem "obrigado"            | R$ 97,00     |
| 2  | Lead formulario      | Lead           | contem "obrigado-cadastro"   | -            |

Total: 2 conversoes configuradas
</output_template>

<note>Traduzir a regra de URL de forma simples: {"url":{"i_contains":"obrigado"}} vira "contem 'obrigado'".</note>
</branch>

<branch condition="consulta == testes_ab">
<description>Testes A/B</description>
<tool_name>list_ab_tests</tool_name>

<parameters>
  <param name="business_id" required="true">ID do business (NAO account_id)</param>
</parameters>

<note>Testes A/B sao criados no nivel do business, nao da conta de anuncios. Usar business_id.</note>

<output_template>
Testes A/B:

| #  | Nome              | Tipo           | Periodo                    | Status      |
|----|-------------------|----------------|----------------------------|-------------|
| 1  | Teste criativo    | Criativo       | 01/03/2026 a 15/03/2026    | Finalizado  |
| 2  | Teste publico     | Publico-alvo   | 20/03/2026 a 03/04/2026    | Em andamento|

Total: 2 testes
</output_template>

<note>Se o teste estiver finalizado, apresentar o resultado: qual variante venceu e por que.</note>
</branch>

</step>

</steps>

<navigation>
Apos apresentar qualquer consulta, oferecer opcoes de aprofundamento:
- Apos listar campanhas: "Quer ver os conjuntos de anuncios de alguma campanha? Ou ver o relatorio de performance?"
- Apos listar conjuntos: "Quer ver os anuncios de algum conjunto? Ou ver o publico-alvo detalhado?"
- Apos listar anuncios: "Quer ver o criativo (imagem/texto) de algum anuncio?"
- Apos listar publicos: "Quer ver em quais conjuntos de anuncios esse publico esta sendo usado?"
- Apos listar pixel: "Quer ver as conversoes personalizadas configuradas?"
Isso cria uma navegacao natural pela estrutura da conta sem o usuario precisar saber os termos tecnicos.
</navigation>

<formatting_rules>
- Moeda: R$ X.XXX,XX (ponto para milhar, virgula para decimal)
- Numeros grandes: X.XXX.XXX (com ponto para milhar)
- Datas: DD/MM/AAAA (padrao brasileiro)
- Duracao de video: M:SS (minutos:segundos)
- Tamanho de publico: ~X.XXX (aproximado, com til)
</formatting_rules>

<tools_used>
- get_campaigns: account_id, status_filter, limit, fields -- listar campanhas da conta
- get_campaign_details: campaign_id, fields -- detalhes de uma campanha especifica
- get_adsets: account_id, campaign_id, status_filter, limit, fields -- listar conjuntos de anuncios
- get_adset_details: adset_id, fields -- detalhes de um conjunto especifico (inclui targeting completo)
- get_ads: account_id, campaign_id, adset_id, status_filter, limit, fields -- listar anuncios
- get_ad_details: ad_id -- detalhes de um anuncio especifico
- get_ad_creatives: ad_id, fields -- ver criativo (texto, imagem, link) de um anuncio
- get_ad_image: ad_id -- ver imagem de um anuncio
- list_custom_audiences: account_id, limit, fields -- listar publicos personalizados e lookalikes
- list_saved_audiences: account_id, limit, fields -- listar publicos salvos com targeting
- get_account_videos: account_id, limit, fields -- listar videos da conta
- get_pixels: account_id, fields -- listar pixels e status de instalacao
- list_custom_conversions: account_id, fields -- listar conversoes personalizadas
- list_ab_tests: business_id -- listar testes A/B
</tools_used>

</workflow>
