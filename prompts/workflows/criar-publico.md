<workflow name="criar-publico">

<when_to_use>
Use este workflow quando o usuario quiser criar um publico FORA do fluxo de criacao de campanha. Exemplos:
- Criar um publico de remarketing (visitantes do site, engajamento, video)
- Criar um publico a partir de uma lista de clientes
- Criar um publico semelhante (Lookalike) baseado em um publico existente
- Preparar publicos para usar em campanhas futuras

Keywords de ativacao: criar publico, novo publico, publico personalizado, publico semelhante, lookalike, remarketing, lista de clientes, visitantes do site, engajamento, audiencia, audience, custom audience.

NOTA: Se o usuario nunca configurou publicos e quer um setup completo, redirecionar para o workflow de onboarding. Este workflow e para criacao individual e especifica.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar cada tipo de publico em linguagem simples, sugerir o mais adequado para o contexto do usuario, perguntar passo a passo.
- Avancado: aceitar comandos diretos como "cria lookalike 1% do engajamento IG" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o tipo de publico (ex: "quero criar um lookalike"), pular a pergunta de tipo e ir direto para os parametros.
</user_mode>

<steps>

<step number="1" name="Tipo de publico">
<question>Qual tipo de publico voce quer criar?</question>
<if_unknown>
Perguntar: "Voce tem site com pixel instalado? Tem lista de clientes? Tem videos publicados?" e recomendar com base nas respostas:
- Tem pixel ativo: recomendar "Visitantes do site"
- Tem Instagram com engajamento: recomendar "Engajamento Instagram"
- Tem lista de clientes: recomendar "Lista de clientes"
- Ja tem publicos criados e quer escalar: recomendar "Publico semelhante"
</if_unknown>
<options>
  <option value="website">Visitantes do site | Pessoas que visitaram seu site (precisa de pixel instalado) | Website Custom Audience</option>
  <option value="customer_list">Lista de clientes | Enviar uma lista com emails/telefones dos seus clientes | Customer List Audience</option>
  <option value="video_fb">Video do Facebook | Pessoas que assistiram seus videos na pagina do Facebook | Video Custom Audience (page)</option>
  <option value="video_ig">Video do Instagram | Pessoas que assistiram seus videos no Instagram | Video Custom Audience (ig_business)</option>
  <option value="engagement_fb">Engajamento Facebook | Pessoas que interagiram com sua pagina no Facebook | Page Custom Audience</option>
  <option value="engagement_ig">Engajamento Instagram | Pessoas que interagiram com seu perfil no Instagram | Instagram Custom Audience</option>
  <option value="leadform">Formulario de lead | Pessoas que interagiram com seus formularios de cadastro | Leadform Custom Audience</option>
  <option value="lookalike">Publico semelhante | Encontrar pessoas parecidas com um publico que voce ja tem | Lookalike Audience</option>
</options>
</step>

<step number="2" name="Configuracao por tipo">

<branch condition="tipo == website">
<description>Visitantes do site (pixel)</description>
<tool_name>create_website_custom_audience</tool_name>

<substep number="2.1" name="Verificar pixel">
<tool_call>get_pixels(account_id)</tool_call>
<branch condition="NAO tem pixel">"Voce precisa de um pixel instalado no site para criar esse tipo de publico. Quer que eu crie um pixel?" Se sim, chamar create_pixel(account_id, name).</branch>
<branch condition="Tem mais de um pixel">Mostrar lista e perguntar qual usar.</branch>
<branch condition="Tem um pixel">Confirmar automaticamente.</branch>
</substep>

<substep number="2.2" name="Faixa de tempo">
<question>Qual periodo de visitantes voce quer capturar?</question>
<if_unknown>Recomendo 90 dias. Tem um bom volume de pessoas e ainda sao visitantes relativamente recentes.</if_unknown>
<options>
  <option value="30">Ultimos 30 dias | Remarketing quente -- pessoas que visitaram recentemente. Melhor taxa de conversao.</option>
  <option value="60">Ultimos 60 dias | Equilibrio entre volume e recencia.</option>
  <option value="90">Ultimos 90 dias | Bom volume. Recomendado para a maioria dos negocios.</option>
  <option value="180">Ultimos 180 dias | Publico amplo. Bom para lookalike como seed.</option>
</options>
<fills>retention_days: valor escolhido</fills>
</substep>

<substep number="2.3" name="Tipo de visitante">
<question>Quer capturar todos os visitantes ou apenas quem fez uma acao especifica?</question>
<if_unknown>Recomendo 'Todos os visitantes' para comecar. E o publico maior e mais simples.</if_unknown>
<options>
  <option value="all_visitors">Todos os visitantes | Qualquer pessoa que acessou qualquer pagina do site</option>
  <option value="event">Evento especifico | Apenas quem fez uma acao: comprou, cadastrou, adicionou ao carrinho</option>
</options>

<branch condition="rule_type == event">
<question>Qual evento especifico?</question>
<options>
  <option value="PURCHASE">Comprou</option>
  <option value="ADD_TO_CART">Adicionou ao carrinho</option>
  <option value="LEAD">Cadastrou / preencheu formulario</option>
  <option value="CONTENT_VIEW">Viu pagina do produto</option>
  <option value="INITIATED_CHECKOUT">Iniciou checkout</option>
</options>
<fills>custom_event_type: valor escolhido</fills>
</branch>

<fills>rule_type: all_visitors ou event</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>
- Padrao: "Visitantes Site - [X]D" (ex: "Visitantes Site - 90D")
- Se evento especifico: "Visitantes Site - [Evento] - [X]D" (ex: "Visitantes Site - Purchase - 30D")
</default>
<question>Quer usar esse nome ou prefere outro?</question>
</substep>

<execution>
<tool_call>
create_website_custom_audience(
  account_id,
  name="[Nome escolhido]",
  pixel_id="[PIXEL_ID]",
  retention_days=[DIAS],
  rule_type="[all_visitors ou event]",
  custom_event_type="[EVENTO]"  // apenas se rule_type=event
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == customer_list">
<description>Lista de clientes (CSV)</description>
<tool_name>create_customer_list_audience</tool_name>

<substep number="2.1" name="Pedir arquivo">
Informar: "Envie o arquivo CSV com sua lista de clientes pelo chat (clique no icone de anexo). O arquivo deve conter pelo menos uma coluna com email ou telefone."

<format_guide>
Colunas aceitas: email, phone (telefone com DDD e codigo do pais), fn (primeiro nome), ln (sobrenome), ct (cidade), st (estado), zip (CEP), country (pais)
Minimo obrigatorio: email OU phone
Formato do telefone: +5511999998888 (com codigo do pais)
Os dados sao criptografados (hash) antes de serem enviados a Meta. Ninguem ve as informacoes originais.
</format_guide>
</substep>

<substep number="2.2" name="Nome do publico">
<default>"Lista de Clientes - [Nome do negocio]"</default>
<question>Quer usar esse nome ou prefere outro?</question>
</substep>

<execution>
<tool_call>
create_customer_list_audience(
  account_id,
  name="[Nome escolhido]",
  customers=[
    {"email": "...", "phone": "...", "fn": "..."},
    ...
  ]
)
</tool_call>
</execution>

<post_creation>Informar: "O publico foi criado. A Meta vai cruzar seus dados com os usuarios do Facebook/Instagram. Isso pode levar de 30 minutos a 24 horas. Se sua lista tiver menos de 1.000 contatos, o publico pode ficar 'muito pequeno' para usar em anuncios."</post_creation>
</branch>

<branch condition="tipo == video_fb">
<description>Video do Facebook (Page)</description>
<tool_name>create_video_custom_audience</tool_name>

<substep number="2.1" name="Identificar pagina">
<tool_call>get_account_pages(account_id)</tool_call>
- Se tem mais de uma pagina: mostrar lista e perguntar qual usar.
- Se tem uma pagina: confirmar automaticamente.
<saves>page_id</saves>
</substep>

<substep number="2.2" name="Nivel de engajamento">
<question>Qual nivel de engajamento com os videos voce quer capturar?</question>
<if_unknown>Recomendo 75%. Quem assistiu 75% de um video demonstra interesse real no conteudo. E um otimo publico para remarketing.</if_unknown>
<options>
  <option value="video_watched">Assistiu 3 segundos | Qualquer pessoa que viu pelo menos 3 segundos. Publico grande, interesse basico.</option>
  <option value="video_watched_25_percent">Assistiu 25% | Assistiu um quarto do video. Interesse moderado.</option>
  <option value="video_watched_50_percent">Assistiu 50% | Assistiu metade. Bom interesse.</option>
  <option value="video_watched_75_percent">Assistiu 75% | Assistiu a maior parte. Muito engajado. Recomendado para remarketing.</option>
  <option value="video_watched_95_percent">Assistiu 95% | Assistiu quase tudo. Publico pequeno mas altamente interessado.</option>
</options>
<fills>engagement_type: valor escolhido</fills>
</substep>

<substep number="2.3" name="Periodo de retencao">
<question>Por quantos dias voce quer manter essas pessoas no publico?</question>
<if_unknown>Recomendo 365 dias. Videos acumulam visualizacoes ao longo do tempo e voce quer aproveitar todo esse historico.</if_unknown>
<options>
  <option value="30">30 dias</option>
  <option value="60">60 dias</option>
  <option value="90">90 dias</option>
  <option value="180">180 dias</option>
  <option value="365">365 dias</option>
</options>
<fills>retention_days: valor escolhido</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>"Video FB - [%] [X]D" (ex: "Video FB - 75% 365D")</default>
</substep>

<execution>
<tool_call>
create_video_custom_audience(
  account_id,
  name="[Nome escolhido]",
  source_type="page",
  source_id="[PAGE_ID]",
  engagement_type="[TIPO]",
  retention_days=[DIAS]
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == video_ig">
<description>Video do Instagram</description>
<tool_name>create_video_custom_audience</tool_name>

<substep number="2.1" name="Identificar conta do Instagram">
<tool_call>get_account_pages(account_id)</tool_call>
Resolver o instagram_business_account vinculado a pagina.
- Se nao encontrar conta de Instagram: "Nao encontrei um perfil do Instagram vinculado. Para criar esse tipo de publico, voce precisa de um perfil business ou creator do Instagram conectado a uma pagina do Facebook."
- Se encontrar: confirmar o perfil (@username).
<saves>instagram_account_id</saves>
</substep>

<substep number="2.2" name="Nivel de engajamento">
Mesmas opcoes do Video do Facebook (substep 2.2 do tipo video_fb).
<fills>engagement_type: valor escolhido</fills>
</substep>

<substep number="2.3" name="Periodo de retencao">
Mesmas opcoes do Video do Facebook (substep 2.3 do tipo video_fb).
<fills>retention_days: valor escolhido</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>"Video IG - [%] [X]D" (ex: "Video IG - 75% 365D")</default>
</substep>

<execution>
<tool_call>
create_video_custom_audience(
  account_id,
  name="[Nome escolhido]",
  source_type="ig_business",
  source_id="[INSTAGRAM_ACCOUNT_ID]",
  engagement_type="[TIPO]",
  retention_days=[DIAS]
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == engagement_fb">
<description>Engajamento Facebook (Page)</description>
<tool_name>create_page_custom_audience</tool_name>

<substep number="2.1" name="Identificar pagina">
<tool_call>get_account_pages(account_id)</tool_call>
Confirmar a pagina.
<saves>page_id</saves>
</substep>

<substep number="2.2" name="Tipo de engajamento">
<question>Qual tipo de interacao voce quer capturar?</question>
<if_unknown>Recomendo 'Qualquer interacao'. Ele captura todo mundo que engajou com sua pagina de alguma forma.</if_unknown>
<options>
  <option value="page_engaged">Qualquer interacao | Qualquer pessoa que interagiu com sua pagina (curtiu, comentou, compartilhou, clicou). Recomendado.</option>
  <option value="page_visited">Visitou a pagina | Quem visitou o perfil da sua pagina no Facebook.</option>
  <option value="page_messaged">Enviou mensagem | Quem mandou mensagem para sua pagina via Messenger.</option>
  <option value="page_cta_clicked">Clicou no botao de acao | Quem clicou no botao da pagina (ex: "Ligar agora", "Enviar mensagem").</option>
  <option value="page_liked">Curtiu a pagina | Quem curtiu (seguiu) a pagina.</option>
</options>
<fills>engagement_type: valor escolhido</fills>
</substep>

<substep number="2.3" name="Periodo de retencao">
<question>Por quantos dias voce quer manter essas pessoas no publico?</question>
<if_unknown>Recomendo 365 dias para ter o maior volume possivel.</if_unknown>
<options>
  <option value="30">30 dias</option>
  <option value="60">60 dias</option>
  <option value="90">90 dias</option>
  <option value="180">180 dias</option>
  <option value="365">365 dias</option>
</options>
<fills>retention_days: valor escolhido</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>"Engajamento FB - [Tipo] [X]D" (ex: "Engajamento FB - 365D")</default>
</substep>

<execution>
<tool_call>
create_page_custom_audience(
  account_id,
  name="[Nome escolhido]",
  page_id="[PAGE_ID]",
  engagement_type="[TIPO]",
  retention_days=[DIAS]
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == engagement_ig">
<description>Engajamento Instagram</description>
<tool_name>create_instagram_custom_audience</tool_name>

<substep number="2.1" name="Identificar conta do Instagram">
<tool_call>get_account_pages(account_id)</tool_call>
Resolver o instagram_business_account.
<saves>instagram_account_id</saves>
</substep>

<substep number="2.2" name="Tipo de engajamento">
<question>Qual tipo de interacao no Instagram voce quer capturar?</question>
<if_unknown>Recomendo 'Qualquer interacao'. Ele captura todos que engajaram com seu perfil, incluindo quem viu seus stories, curtiu posts, mandou DM, etc.</if_unknown>
<options>
  <option value="ig_business_profile_all">Qualquer interacao | Todo mundo que interagiu com seu perfil de alguma forma. Recomendado.</option>
  <option value="ig_business_profile_engaged">Engajamento com conteudo | Quem curtiu, comentou, salvou ou compartilhou seus posts/reels/stories.</option>
  <option value="ig_business_profile_visit">Visitou o perfil | Quem visitou seu perfil no Instagram.</option>
  <option value="ig_user_messaged_business">Enviou mensagem | Quem mandou DM (mensagem direta) para voce.</option>
  <option value="ig_business_profile_ad_saved">Salvou anuncio/post | Quem salvou um dos seus posts ou anuncios.</option>
  <option value="ig_business_profile_follow">Seguidores atuais | Quem segue seu perfil no Instagram. Sem retencao (tempo real).</option>
</options>
<fills>engagement_type: valor escolhido</fills>
</substep>

<substep number="2.3" name="Periodo de retencao">
<question>Por quantos dias voce quer manter essas pessoas no publico?</question>
<if_unknown>Recomendo 365 dias. Assim voce aproveita todo o engajamento do ultimo ano.</if_unknown>
<options>
  <option value="30">30 dias</option>
  <option value="60">60 dias</option>
  <option value="90">90 dias</option>
  <option value="180">180 dias</option>
  <option value="365">365 dias</option>
  <option value="730">730 dias (maximo para Instagram)</option>
</options>
<fills>retention_days: valor escolhido</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>"Engajamento IG - [Tipo] [X]D" (ex: "Engajamento IG - 365D")</default>
</substep>

<execution>
<tool_call>
create_instagram_custom_audience(
  account_id,
  name="[Nome escolhido]",
  instagram_account_id="[INSTAGRAM_ACCOUNT_ID]",
  engagement_type="[TIPO]",
  retention_days=[DIAS]
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == leadform">
<description>Formulario de lead</description>
<tool_name>create_leadform_custom_audience</tool_name>

<substep number="2.1" name="Identificar pagina e formularios">
Informar: "Esse publico captura pessoas que interagiram com seus formularios de cadastro da Meta (Lead Ads)."
Obter page_id com get_account_pages(account_id). O page_id e obrigatorio.
Opcionalmente, perguntar se quer filtrar por formularios especificos (leadform_ids).
</substep>

<substep number="2.2" name="Tipo de interacao">
<question>Qual tipo de interacao com o formulario voce quer capturar?</question>
<options>
  <option value="lead_generation_submitted">Enviou o formulario | Apenas quem preencheu e enviou (recomendado)</option>
  <option value="lead_generation_opened">Abriu o formulario | Qualquer pessoa que abriu, mesmo sem preencher</option>
  <option value="lead_generation_opened_or_submitted">Abriu ou enviou | Todos que interagiram de alguma forma</option>
</options>
<fills>engagement_type: valor escolhido</fills>
</substep>

<substep number="2.3" name="Nome do publico">
<default>"Leads Form - [Tipo] [X]D"</default>
</substep>

<execution>
<tool_call>
create_leadform_custom_audience(
  account_id,
  name="[Nome escolhido]",
  page_id="[PAGE_ID]",               // obrigatorio
  leadform_ids=["[FORM_ID]"],        // opcional, lista de IDs
  engagement_type="lead_generation_submitted",
  retention_days=[DIAS]
)
</tool_call>
</execution>
</branch>

<branch condition="tipo == lookalike">
<description>Publico semelhante (Lookalike)</description>
<tool_name>create_lookalike_audience</tool_name>

<substep number="2.1" name="Listar publicos existentes">
<tool_call>list_custom_audiences(account_id)</tool_call>

<output_template>
Seus publicos disponiveis para criar semelhante:

| #  | Nome                          | Tipo           | Tamanho aprox. |
|----|-------------------------------|----------------|----------------|
| 1  | Engajamento IG - 365D         | Instagram      | ~5.000         |
| 2  | Visitantes Site - 90D         | Website        | ~12.000        |
| 3  | Lista de Clientes             | Lista enviada  | ~3.500         |

Qual publico voce quer usar como base?
</output_template>

<branch condition="NAO tem publicos">"Voce precisa ter pelo menos um publico personalizado para criar um semelhante. Quer criar um primeiro?"</branch>

<explanation>O publico semelhante usa um publico existente como 'modelo' e encontra pessoas parecidas. Quanto melhor o publico base, melhor sera o semelhante. Os melhores seeds sao: lista de clientes que compraram, engajamento do Instagram, visitantes do site.</explanation>

<saves>origin_audience_id</saves>
</substep>

<substep number="2.2" name="Pais">
<question>Em qual pais voce quer encontrar pessoas semelhantes?</question>
<if_unknown>Para a maioria dos negocios brasileiros, o ideal e Brasil.</if_unknown>
<fills>country (ex: "BR")</fills>
</substep>

<substep number="2.3" name="Percentual">
<question>Qual tamanho do publico semelhante voce quer?</question>
<if_unknown>Recomendo comecar com 1%. E o publico mais parecido com seus clientes e costuma ter o melhor custo por resultado.</if_unknown>
<options>
  <option value="0.01">1% | As pessoas MAIS parecidas com seu publico. Menor e mais preciso. Recomendado para comecar.</option>
  <option value="0.02">2% | Um pouco mais amplo. Bom para escalar quando o 1% estiver saturado.</option>
  <option value="0.05">5% | Bem mais amplo. Maior volume, menor precisao. Use quando os menores estiverem caros.</option>
</options>
<fills>ratio: valor escolhido</fills>
</substep>

<substep number="2.4" name="Nome do publico">
<default>"LAL [%] [Pais] - [Nome do seed]" (ex: "LAL 1% BR - Engajamento IG 365D")</default>
</substep>

<execution>
<tool_call>
create_lookalike_audience(
  account_id,
  name="[Nome escolhido]",
  origin_type="custom_audience",
  origin_audience_id="[SEED_AUDIENCE_ID]",
  country="[PAIS]",
  ratio=[PERCENTUAL]
)
</tool_call>
</execution>

<post_creation>Informar: "O publico semelhante foi criado. Ele leva de 1 a 6 horas para ficar pronto. Voce pode verificar o status com o comando 'listar publicos'."</post_creation>
</branch>

</step>

</steps>

<auto_fields>
Campos preenchidos automaticamente em todos os tipos:
- account_id: Detectado automaticamente da sessao (conta selecionada no login)
- page_id: Obtido via get_account_pages (pagina principal vinculada)
- instagram_account_id: Obtido via get_account_pages / instagram_business_account (perfil IG vinculado a pagina)
- pixel_id: Obtido via get_pixels (pixel ativo da conta)
</auto_fields>

<validations>
- account_id preenchido
- Para website: pixel_id existe e esta ativo (verificar com get_pixels)
- Para video FB: page_id existe (verificar com get_account_pages)
- Para video IG: instagram_account_id existe
- Para engajamento FB: page_id existe
- Para engajamento IG: instagram_account_id existe
- Para lista de clientes: arquivo enviado com pelo menos email ou phone
- Para lookalike: publico seed existe e tem pelo menos 100 membros
- retention_days dentro dos limites (max 180 para website, max 730 para IG, max 365 para demais)
- Nome do publico preenchido e descritivo
</validations>

<error_handling>
<error code="PixelNotFound" cause="Pixel nao existe ou sem acesso">
  Solucao: Criar pixel com create_pixel ou verificar permissoes
</error>
<error code="NoPagesFound" cause="Pagina nao conectada a conta">
  Solucao: Conectar pagina em Business Suite > Configuracoes
</error>
<error code="NoInstagramAccount" cause="Instagram nao vinculado a pagina">
  Solucao: Vincular em Instagram > Configuracoes > Contas vinculadas
</error>
<error code="AudienceLimitReached" cause="Limite de 500 publicos por conta">
  Solucao: Excluir publicos antigos ou inativos
</error>
<error code="SeedAudienceTooSmall" cause="Publico seed tem menos de 100 membros">
  Solucao: Usar outro publico com mais membros ou aguardar crescer
</error>
<error code="CustomerListTooSmall" cause="Lista enviada tem poucos contatos">
  Solucao: Enviar lista com pelo menos 1.000 contatos para melhor resultado
</error>
<error code="InvalidCSVFormat" cause="Arquivo nao esta no formato esperado">
  Solucao: Verificar se as colunas estao corretas (email, phone, fn, ln)
</error>
<error code="RateLimit" cause="Muitas chamadas de API em sequencia">
  Solucao: Aguardar alguns segundos entre as criacoes
</error>
</error_handling>

<tools_used>
- get_pixels: account_id
- create_pixel: account_id, name
- get_account_pages: account_id
- list_custom_audiences: account_id
- create_website_custom_audience: account_id, name, pixel_id, retention_days, rule_type, custom_event_type
- create_customer_list_audience: account_id, name, customers
- create_video_custom_audience: account_id, name, source_type, source_id, engagement_type, retention_days
- create_page_custom_audience: account_id, name, page_id, engagement_type, retention_days
- create_instagram_custom_audience: account_id, name, instagram_account_id, engagement_type, retention_days
- create_leadform_custom_audience: account_id, name, page_id, leadform_ids (opcional), engagement_type, retention_days
- create_lookalike_audience: account_id, name, origin_type, origin_audience_id, country, ratio
</tools_used>

</workflow>
