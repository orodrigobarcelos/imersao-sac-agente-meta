<workflow name="criar-campanha">

<when_to_use>
Use este workflow sempre que o usuario quiser:
- Criar uma campanha de anuncios
- Anunciar um produto ou servico
- Vender pelo Instagram ou Facebook
- Gerar leads ou cadastros
- Receber mensagens no WhatsApp, Messenger ou Instagram
- Atrair visitantes para o site
- Promover um video
- Aumentar o engajamento em posts
- Aumentar o reconhecimento da marca

Keywords de ativacao: criar campanha, anunciar, vender, promover, gerar leads, gerar cadastros, quero anunciar, fazer anuncio, trafego pago, campanha nova, impulsionar.
</when_to_use>

<user_mode>
Detectar automaticamente o nivel do usuario com base no historico de conversas ou perguntar:
- Iniciante (padrao): perguntar tudo passo a passo, oferecer sugestoes com justificativa para cada decisao, usar linguagem simples sem termos tecnicos.
- Avancado: aceitar comandos diretos com parametros, perguntar apenas o que falta, usar terminologia tecnica.
</user_mode>

<steps>

<step number="1" name="Objetivo da campanha">
<question>O que voce quer alcancar com essa campanha?</question>
<if_unknown>Para a maioria dos negocios que estao comecando, recomendo 'Atrair visitantes pro site' (Trafego). E mais simples, mais barato e ajuda a aquecer o pixel para campanhas de vendas no futuro.</if_unknown>
<options>
  <option value="OUTCOME_SALES / OFFSITE_CONVERSIONS">Vender pelo site (e-commerce, loja virtual) | Requer pixel</option>
  <option value="OUTCOME_SALES / CONVERSATIONS">Vender por mensagem (WhatsApp/Messenger/DM) | Requer page_id</option>
  <option value="OUTCOME_LEADS / OFFSITE_CONVERSIONS">Gerar leads/cadastros pelo site | Requer pixel</option>
  <option value="OUTCOME_LEADS / LEAD_GENERATION">Gerar leads por formulario da Meta | Requer page_id + permissoes</option>
  <option value="OUTCOME_TRAFFIC / CONVERSATIONS">Receber mensagens (WhatsApp/Messenger/DM) | Requer page_id</option>
  <option value="OUTCOME_TRAFFIC / LINK_CLICKS ou LANDING_PAGE_VIEWS">Atrair visitantes pro site | Sem pixel obrigatorio</option>
  <option value="OUTCOME_ENGAGEMENT / THRUPLAY">Mais visualizacoes em video | Requer page_id</option>
  <option value="OUTCOME_ENGAGEMENT / POST_ENGAGEMENT">Mais engajamento em posts | Requer page_id</option>
  <option value="OUTCOME_ENGAGEMENT / CONVERSATIONS">Engajamento via mensagens | Requer page_id</option>
  <option value="OUTCOME_ENGAGEMENT / REACH">Mais alcance (via engajamento) | Sem requisitos especiais</option>
  <option value="OUTCOME_AWARENESS / REACH">Mais alcance/reconhecimento | Sem requisitos especiais</option>
</options>
<fills>objective: valor mapeado, optimization_goal: valor mapeado</fills>
</step>

<step number="2" name="Configuracoes especificas do objetivo">

<branch condition="objective == OUTCOME_SALES AND optimization_goal == OFFSITE_CONVERSIONS">
<description>Vendas pelo site</description>

<substep number="2.1" name="Verificar pixel">
Chamar get_pixels(account_id).
- Se NAO tem pixel: "Voce precisa de um pixel instalado no site para rastrear vendas. Quer que eu crie um?" Se sim, chamar create_pixel(account_id, name).
- Se tem pixel: mostrar nome e ID, confirmar qual usar.
</substep>

<substep number="2.2" name="Acao no site">
<question>Qual acao voce quer que as pessoas facam no seu site?</question>
<if_unknown>Se voce esta comecando e seu pixel e novo, recomendo 'Ver pagina do produto'. Assim a Meta aprende quem sao seus visitantes antes de otimizar para compras.</if_unknown>
<options>
  <option value="PURCHASE">Comprar | Recomendado para e-commerce</option>
  <option value="LEAD">Cadastrar / preencher formulario | Para servicos</option>
  <option value="ADD_TO_CART">Adicionar ao carrinho | Para e-commerce com funil</option>
  <option value="CONTENT_VIEW">Ver pagina do produto | Recomendado para aquecer pixel novo</option>
  <option value="INITIATED_CHECKOUT">Iniciar checkout</option>
  <option value="COMPLETE_REGISTRATION">Cadastro completo</option>
</options>
<fills>custom_event_type: valor escolhido</fills>
</substep>

<auto_fields>
optimization_goal: OFFSITE_CONVERSIONS
billing_event: IMPRESSIONS
promoted_object: {"pixel_id": "PIXEL_ID", "custom_event_type": "EVENTO_ESCOLHIDO"}
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_SALES AND optimization_goal == CONVERSATIONS">
<description>Vendas por mensagem</description>

<substep number="2.1" name="Canal de mensagens">
<question>Por onde voce quer receber as mensagens dos clientes?</question>
<if_unknown>Messenger e a opcao mais simples para comecar. WhatsApp exige configuracao extra do Business Platform API.</if_unknown>
<options>
  <option value="WHATSAPP">WhatsApp | Requer WhatsApp Business Platform API</option>
  <option value="MESSENGER">Messenger (Facebook)</option>
  <option value="INSTAGRAM_DIRECT">Instagram Direct</option>
</options>
<fills>destination_type: valor escolhido</fills>
</substep>

<substep number="2.2" name="Pagina do Facebook">
Obter page_id: chamar get_account_pages(account_id) para listar TODAS as paginas, depois fazer match pelo nome informado pelo usuario. NAO usar search_pages_by_name como primeiro recurso.
</substep>

<auto_fields>
optimization_goal: CONVERSATIONS
billing_event: IMPRESSIONS
destination_type: DESTINO_ESCOLHIDO
promoted_object: {"page_id": "PAGE_ID"}
</auto_fields>

<creative_fields>
- Para Messenger: link_url = "https://m.me/PAGE_ID", call_to_action_type = "MESSAGE_PAGE", app_destination = "MESSENGER"
- Para Instagram Direct: link_url = "https://ig.me/m/USERNAME", call_to_action_type = "MESSAGE_PAGE", app_destination = "INSTAGRAM_DIRECT"
- Para WhatsApp: call_to_action_type = "WHATSAPP_MESSAGE", app_destination = "WHATSAPP"
</creative_fields>
</branch>

<branch condition="objective == OUTCOME_LEADS AND optimization_goal == OFFSITE_CONVERSIONS">
<description>Leads pelo site</description>

<substep number="2.1" name="Verificar pixel">
Chamar get_pixels(account_id).
- Se NAO tem pixel: "Voce precisa de um pixel instalado no site para rastrear cadastros. Quer que eu crie um?"
</substep>

<substep number="2.2" name="Tipo de cadastro">
<question>Qual tipo de cadastro voce quer rastrear?</question>
<options>
  <option value="LEAD">Lead / formulario preenchido</option>
  <option value="COMPLETE_REGISTRATION">Cadastro completo</option>
</options>
</substep>

<auto_fields>
optimization_goal: OFFSITE_CONVERSIONS
billing_event: IMPRESSIONS
promoted_object: {"pixel_id": "PIXEL_ID", "custom_event_type": "LEAD"}
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_LEADS AND optimization_goal == LEAD_GENERATION">
<description>Leads por formulario da Meta</description>

<substep number="2.1" name="Pagina do Facebook">
Obter page_id: chamar get_account_pages(account_id) para listar TODAS as paginas, depois fazer match pelo nome informado pelo usuario. NAO usar search_pages_by_name como primeiro recurso.
</substep>

<substep number="2.2" name="Informar sobre formulario">
Informar: "Vou criar um formulario dentro da Meta. Quando alguem clicar no anuncio, o formulario aparece sem sair do Facebook/Instagram."
</substep>

<substep number="2.3" name="Verificar permissoes">
O token precisa de pages_manage_metadata, leads_retrieval e pages_manage_ads. Se faltar, orientar o usuario.
</substep>

<substep number="2.4" name="Verificar TOS">
"O administrador da pagina precisa aceitar os termos de servico de Lead Ads em: https://www.facebook.com/ads/leadgen/tos/?page_id=PAGE_ID (aceitar como perfil pessoal, nao como pagina)."
</substep>

<substep number="2.5" name="Criar formulario">
Perguntar quais campos quer no formulario:
- Padrao: Nome completo, Email, Telefone.
- Opcoes adicionais: Cidade, Estado, CEP, Data de nascimento, pergunta personalizada.
- URL da politica de privacidade (obrigatorio).
- URL de agradecimento apos envio.
- Chamar create_lead_form(page_id, name, questions, privacy_policy_url, follow_up_action_url).
</substep>

<auto_fields>
optimization_goal: LEAD_GENERATION
billing_event: IMPRESSIONS
destination_type: ON_AD
promoted_object: {"page_id": "PAGE_ID"}
</auto_fields>

<creative_fields>
call_to_action_type: SIGN_UP (ou SUBSCRIBE, APPLY_NOW conforme contexto)
Incluir lead_gen_form_id no call_to_action value.
</creative_fields>
</branch>

<branch condition="objective == OUTCOME_TRAFFIC AND optimization_goal == LINK_CLICKS ou LANDING_PAGE_VIEWS">
<description>Visitantes no site</description>

<substep number="2.1" name="Tipo de otimizacao">
<question>Voce quer otimizar para cliques no link ou para visualizacoes de pagina?</question>
<if_unknown>Para comecar, recomendo 'Cliques no link'. E mais barato e voce nao precisa de pixel. Depois, quando tiver mais dados, pode mudar para 'Visualizacoes de pagina'.</if_unknown>
<options>
  <option value="LINK_CLICKS">Cliques no link | Mais volume, custo menor, recomendado para comecar</option>
  <option value="LANDING_PAGE_VIEWS">Visualizacoes de pagina | So conta quem carregou a pagina, mais qualidade mas precisa de pixel</option>
</options>
</substep>

<auto_fields>
optimization_goal: LINK_CLICKS ou LANDING_PAGE_VIEWS
billing_event: IMPRESSIONS
promoted_object: nenhum obrigatorio (opcional: pixel_id se disponivel)
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_TRAFFIC AND optimization_goal == CONVERSATIONS">
<description>Mensagens via trafego</description>
Mesmo fluxo de OUTCOME_SALES + CONVERSATIONS, com:
- objective: OUTCOME_TRAFFIC
- optimization_goal: CONVERSATIONS
</branch>

<branch condition="objective == OUTCOME_ENGAGEMENT AND optimization_goal == THRUPLAY">
<description>Visualizacoes de video</description>

<substep number="2.1" name="Pagina do Facebook">
Obter page_id: chamar get_account_pages(account_id).
</substep>

<substep number="2.2" name="Video">
<question>Qual video voce quer promover?</question>
Se nao tem video, orientar sobre formatos.
</substep>

<auto_fields>
optimization_goal: THRUPLAY
billing_event: IMPRESSIONS
destination_type: ON_VIDEO
promoted_object: {"page_id": "PAGE_ID"}
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_ENGAGEMENT AND optimization_goal == POST_ENGAGEMENT">
<description>Engajamento em posts</description>

<substep number="2.1" name="Pagina do Facebook">
Obter page_id: chamar get_account_pages(account_id).
</substep>

<auto_fields>
optimization_goal: POST_ENGAGEMENT
billing_event: IMPRESSIONS
destination_type: ON_POST
promoted_object: {"page_id": "PAGE_ID"}
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_ENGAGEMENT AND optimization_goal == CONVERSATIONS">
<description>Mensagens via engajamento</description>
Mesmo fluxo de OUTCOME_SALES + CONVERSATIONS, com:
- objective: OUTCOME_ENGAGEMENT
- optimization_goal: CONVERSATIONS
- destination_type: MESSENGER ou INSTAGRAM_DIRECT
- promoted_object: {"page_id": "PAGE_ID"}
</branch>

<branch condition="objective == OUTCOME_ENGAGEMENT AND optimization_goal == REACH">
<description>Alcance via engajamento</description>

<auto_fields>
optimization_goal: REACH
billing_event: IMPRESSIONS
Sem promoted_object obrigatorio
</auto_fields>
</branch>

<branch condition="objective == OUTCOME_AWARENESS">
<description>Alcance/Reconhecimento</description>

<substep number="2.1" name="Tipo de otimizacao">
<question>Voce quer otimizar para alcance (pessoas unicas que veem o anuncio) ou impressoes (total de vezes que o anuncio aparece)?</question>
<if_unknown>Recomendo 'Alcance'. Assim a Meta mostra seu anuncio para o maior numero de pessoas diferentes possiveis.</if_unknown>
<options>
  <option value="REACH">Alcance | Recomendado para a maioria</option>
  <option value="IMPRESSIONS">Impressoes</option>
</options>
</substep>

<auto_fields>
optimization_goal: REACH ou IMPRESSIONS
billing_event: IMPRESSIONS
</auto_fields>
</branch>

</step>

<step number="3" name="Nome da campanha">
<question>Qual nome voce quer dar para essa campanha?</question>
<if_unknown>Sugerir padrao: "[Objetivo] - [Produto/Servico] - [Mes/Ano]". Exemplo: "Trafego - Curso de Ingles - Abr/2026"</if_unknown>
<fills>name: valor informado pelo usuario</fills>
</step>

<step number="4" name="Orcamento">
<question>Quanto voce quer investir por dia nessa campanha?</question>
<if_unknown>Para comecar, recomendo entre R$30 e R$50 por dia. Com menos de R$20, a Meta nao consegue otimizar bem os anuncios. Se voce tem urgencia ou um lancamento, pode comecar com R$100 a R$200 por dia e depois reduzir. O valor e em reais. Eu converto automaticamente para centavos na API.</if_unknown>
<fills>daily_budget: valor em centavos (R$50 = 5000)</fills>
</step>

<step number="5" name="Modo de orcamento (Budget Mode)">
<question>Voce quer que a Meta distribua o orcamento automaticamente entre os conjuntos de anuncios (recomendado) ou prefere controlar manualmente quanto cada conjunto recebe?</question>
<if_unknown>Para quem esta comecando, recomendo automatico (CBO). A Meta e muito boa em identificar qual publico gera mais resultado e coloca mais dinheiro la.</if_unknown>
<options>
  <option value="CBO">Automatico (Advantage Campaign Budget) | Orcamento definido na campanha, Meta distribui entre adsets automaticamente, bid_strategy: LOWEST_COST_WITHOUT_CAP</option>
  <option value="ABO">Manual | Orcamento definido em cada adset, dividir orcamento igualmente entre os adsets criados</option>
</options>
<fills>budget_mode: CBO ou ABO</fills>
</step>

<step number="5.1" name="Agendamento (opcional)">
<question>Quer que a campanha comece imediatamente quando for ativada ou prefere agendar pra uma data futura?</question>
<if_unknown>Recomendo comecar imediatamente. Voce pode pausar a qualquer momento se precisar.</if_unknown>
<options>
  <option value="imediato">Imediatamente (padrao) | Nao passar start_time (comeca quando ativar)</option>
  <option value="agendar">Agendar | Perguntar data e hora de inicio. Converter para ISO 8601 (ex: "2026-04-15T00:00:00-0300"). Passar como start_time no create_adset.</option>
</options>
<note>Se o usuario quiser data de fim, perguntar e passar end_time. NOTA: end_time obriga o uso de lifetime_budget em vez de daily_budget.</note>
<fills>start_time: ISO 8601 (se agendado), end_time: ISO 8601 (se informado)</fills>
</step>

<step number="6" name="Publico-alvo (MULTIPLOS ADSETS)">

<critical_rule>Cada tipo de publico vai em um adset separado. Isso permite que a Meta otimize o orcamento entre tipos de publico diferentes.</critical_rule>

<substep number="6.1" name="Verificar publicos existentes e criar LAL">
<critical_rule>OBRIGATORIO: Chamar list_custom_audiences(account_id) ANTES de sugerir qualquer estrutura de adsets. NAO pule esta etapa.</critical_rule>
Chamar list_custom_audiences(account_id) para listar publicos ja criados (personalizados e semelhantes/lookalike).
- Se TEM publicos: incluir os publicos personalizados e semelhantes como adsets separados na sugestao de estrutura. Cada tipo de publico existente (lookalike, engajamento IG, engajamento FB, video, site) vira um adset.
- Se NAO tem publicos: sugerir executar o workflow de onboarding primeiro OU criar publicos inline.
A estrutura de adsets deve SEMPRE considerar os publicos existentes na conta, nao apenas interesses e publico aberto.

<lookalike_creation>
APOS listar os publicos, verificar se ja existem publicos semelhantes (Lookalike/LAL).
Se NAO existir LAL para os publicos personalizados de maior janela, SUGERIR criar:
- "Voce ainda nao tem publicos semelhantes (Lookalike). Quer que eu crie? Eles encontram pessoas parecidas com quem ja interagiu com voce — sao otimos para prospectar novos clientes."

Se o usuario aceitar, criar 1 LAL 1% BR para CADA tipo de publico personalizado que existir (usar o de maior janela):
<tool_call>create_lookalike_audience(account_id, name="LAL 1% BR - [Nome do publico seed]", origin_type="custom_audience", origin_audience_id="[ID do publico de maior janela]", country="BR", ratio=0.01)</tool_call>

Seeds recomendados (criar 1 LAL para cada que existir):
- Visitantes Site - 180D (se existir publico de website)
- Engajamento FB - 365D (se existir publico de pagina)
- Engajamento IG - 365D (se existir publico de Instagram)
- Video FB - 75% 365D (se existir publico de video FB)
- Video IG - 75% 365D (se existir publico de video IG)

Se ja existem LAL, pular esta etapa e seguir para a estrutura de adsets.
</lookalike_creation>
</substep>

<substep number="6.2" name="Estrutura de adsets por tipo de publico">
<critical_rule>A sugestao de adsets DEVE incluir os publicos personalizados e semelhantes que existem na conta (retornados por list_custom_audiences no step 6.1). NAO sugira apenas "publico aberto + interesses + lookalike" se a conta tem publicos de engajamento, video ou site. Cada TIPO de publico existente deve virar um adset separado.</critical_rule>

Organizar os publicos em adsets separados. Incluir TODOS os tipos que existirem na conta:

<adset_structure>
  <adset name="Adset 1 - Lookalike 1%" type="Publico semelhante (Lookalike)" priority="alta">Pessoas similares aos seus clientes. Melhor custo por resultado. Usar o LAL 1% (menor e mais preciso).</adset>
  <adset name="Adset 2 - Engajamento IG" type="Publico personalizado de Instagram" priority="alta">Pessoas que ja interagiram com seu Instagram. Usar o de 365D (maior volume). SO INCLUIR se existir na list_custom_audiences.</adset>
  <adset name="Adset 3 - Engajamento FB" type="Publico personalizado de Facebook" priority="alta">Pessoas que ja interagiram com sua pagina no Facebook. Usar o de 365D. SO INCLUIR se existir na list_custom_audiences.</adset>
  <adset name="Adset 4 - Video" type="Publico personalizado de video" priority="media">Pessoas que assistiram seus videos (usar 75% 365D). SO INCLUIR se existir na list_custom_audiences.</adset>
  <adset name="Adset 5 - Visitantes Site" type="Publico personalizado de site" priority="media">Pessoas que visitaram seu site (usar 180D). SO INCLUIR se existir na list_custom_audiences e se o pixel tem dados.</adset>
  <adset name="Adset 6 - Interesses" type="Direcionamento detalhado" priority="alta">Pessoas com interesses especificos. Todos os interesses juntos num unico adset. Minimo 3 interesses.</adset>
</adset_structure>

<critical_rule>NAO criar um adset por interesse. Agrupar todos os interesses num unico adset.</critical_rule>
<critical_rule>Se a conta tem publicos personalizados (engajamento IG, FB, video, site), eles DEVEM aparecer na sugestao de adsets. Esses publicos sao quentes (remarketing) e normalmente performam melhor que publico frio.</critical_rule>
</substep>

<substep number="6.3" name="Perguntas de targeting por adset">
Para CADA adset, perguntar:

<targeting_question name="Faixa de idade">
<question>Qual faixa de idade do seu publico?</question>
<if_unknown>Para a maioria dos negocios, 25 a 55 anos funciona bem. Se seu produto e para jovens, use 18 a 35.</if_unknown>
<fills>age_min, age_max</fills>
</targeting_question>

<targeting_question name="Genero">
<question>Genero: homens, mulheres ou ambos?</question>
<if_unknown>Ambos, e deixe a Meta descobrir quem converte mais.</if_unknown>
<fills>genders: [1] = masculino, [2] = feminino, [1,2] = ambos, omitir = todos</fills>
</targeting_question>

<targeting_question name="Localizacao">
<question>Localizacao: qual regiao do Brasil (ou outro pais)?</question>
<if_unknown>Brasil inteiro.</if_unknown>
<fills>geo_locations.countries (ex: ["BR"]). Para localizacoes especificas, usar search_geo_locations(query) para buscar regioes/cidades.</fills>
</targeting_question>
</substep>

<substep number="6.4" name="Para adset de interesses">
<question>Quais interesses descrevem seu publico? Por exemplo: fitness, marketing digital, moda...</question>

<critical_rule>MINIMO 3 interesses validos por adset de interesses. Se o usuario informar apenas 1 tema (ex: "IA"), voce DEVE buscar pelo menos 3-5 termos relacionados automaticamente. Exemplo: se o tema e "IA", buscar "inteligencia artificial", "machine learning", "tecnologia", "automacao", "marketing digital". Faca MULTIPLAS chamadas a search_interests com termos variados ate conseguir pelo menos 3 validos.</critical_rule>

<additional_targeting>
Alem de interesses, tambem e possivel segmentar por:
- Comportamentos: usar search_behaviors() (retorna lista completa, filtrar localmente) -- ex: viajantes frequentes, donos de iPhone, compradores online
- Demografia: usar search_demographics(demographic_class="life_events") -- ex: recem-casados, pais com filhos pequenos. Classes disponiveis: demographics, life_events, industries, income, family_statuses, education_statuses, work_employers, work_positions
</additional_targeting>

<process>
1. Identificar o tema do usuario e gerar pelo menos 5 termos de busca relacionados.
2. Buscar interesses com search_interests(query) para CADA termo separadamente. NAO busque todos de uma vez.
3. Buscar comportamentos com search_behaviors(query) se o usuario mencionar habitos ou comportamentos.
4. Buscar demograficos com search_demographics(query) se o usuario mencionar eventos de vida ou perfil profissional.
5. Validar com validate_interests(interest_ids=[...]). Se algum for invalido, buscar alternativas.
6. Se ficou com menos de 3 interesses validos, usar get_interest_suggestions(interest_list) para obter sugestoes adicionais.
7. Estimar tamanho com estimate_audience_size(account_id, targeting={...}).
8. Agrupar TODOS os interesses, comportamentos e demograficos num unico adset usando flexible_spec.
</process>

<targeting_example>
{
  "age_min": 25,
  "age_max": 55,
  "genders": [1, 2],
  "geo_locations": {"countries": ["BR"]},
  "flexible_spec": [
    {
      "interests": [
        {"id": "6003127206524", "name": "Marketing digital"},
        {"id": "6003384241848", "name": "Empreendedorismo"}
      ]
    }
  ],
  "targeting_automation": {"advantage_audience": 0}
}
</targeting_example>

<critical_rule>SEMPRE incluir targeting_automation.advantage_audience = 0 no targeting de TODOS os adsets (com interesses, com custom audiences, ou publico aberto). Isso e obrigatorio na v25.0 para manter controle de idade e evitar erros da API.</critical_rule>
</substep>

<substep number="6.5" name="Para adset de publico personalizado">
Usar os publicos do list_custom_audiences. Targeting:
<targeting_example>
{
  "age_min": 18,
  "age_max": 65,
  "geo_locations": {"countries": ["BR"]},
  "custom_audiences": [{"id": "AUDIENCE_ID"}],
  "targeting_automation": {"advantage_audience": 0}
}
</targeting_example>
</substep>

<substep number="6.6" name="Para adset de lookalike">
Usar os publicos lookalike do list_custom_audiences. Targeting:
<targeting_example>
{
  "age_min": 25,
  "age_max": 55,
  "geo_locations": {"countries": ["BR"]},
  "custom_audiences": [{"id": "LOOKALIKE_AUDIENCE_ID"}],
  "targeting_automation": {"advantage_audience": 0}
}
</targeting_example>
</substep>

<substep number="6.7" name="Para adset de publico aberto (sem interesses nem custom audiences)">
Targeting sem interesses nem publicos personalizados. A Meta otimiza sozinha.
<targeting_example>
{
  "age_min": 25,
  "age_max": 55,
  "geo_locations": {"countries": ["BR"]},
  "targeting_automation": {"advantage_audience": 0}
}
</targeting_example>
<critical_rule>OBRIGATORIO incluir targeting_automation.advantage_audience = 0 mesmo sem interesses. Sem isso, a Meta ativa Advantage+ automaticamente e rejeita age_max menor que 65.</critical_rule>
</substep>

</step>

<step number="7" name="Criativo (imagens, videos, textos)">
<question>Voce tem imagem ou video pronto para o anuncio?</question>

<substep number="7.1" name="Se tem midia">
<critical_rule>Assim que o usuario enviar uma imagem ou video no chat, faca upload IMEDIATAMENTE com upload_ad_image ou upload_ad_video. NAO espere ate o step 10 para fazer upload. O arquivo pendente pode ser perdido se nao for processado logo. Guarde o image_hash ou video_id retornado para usar na criacao do criativo.</critical_rule>
- Pedir para enviar pelo chat (upload de arquivo).
- Formatos aceitos para imagem: JPG, PNG (recomendado 1080x1080 ou 1080x1350).
- Formatos aceitos para video: MP4 (recomendado ate 15 segundos, max 240 minutos).
- Tambem aceita URL publica de imagem ou video.
</substep>

<substep number="7.2" name="Se nao tem midia">
Orientar: "Voce precisa de pelo menos uma imagem ou video para criar o anuncio. Recomendacoes:"
- Imagem quadrada: 1080 x 1080 pixels (funciona em todos os posicionamentos)
- Imagem retrato: 1080 x 1350 pixels (melhor para Stories e Reels)
- Video: ate 15 segundos, formato vertical (9:16) para Stories/Reels ou quadrado (1:1) para feed
</substep>

<substep number="7.3" name="Textos do anuncio">
<critical_rule>NUNCA crie criativos sem antes mostrar os textos ao usuario e receber aprovacao. Se o usuario nao forneceu os textos, sugira opcoes e ESPERE a aprovacao antes de prosseguir. Pergunte um campo por vez.</critical_rule>

<text_field name="message" label="Texto principal do anuncio">
<question>Qual o texto principal do anuncio?</question>
<if_unknown>Sugerir 3 opcoes e perguntar qual o usuario prefere (ou se quer editar). ESPERAR resposta antes de continuar.</if_unknown>
<note>Limite recomendado: 125 caracteres para nao ser cortado.</note>
</text_field>

<text_field name="headline" label="Titulo/headline">
<question>Qual o titulo/headline?</question>
<if_unknown>Sugerir 3 opcoes e ESPERAR aprovacao.</if_unknown>
<note>Limite: 40 caracteres.</note>
</text_field>

<text_field name="description" label="Descricao (opcional)">
<question>Qual a descricao?</question>
<if_unknown>Sugerir opcao e ESPERAR aprovacao.</if_unknown>
<note>Aparece abaixo do titulo em alguns posicionamentos. Limite: 125 caracteres.</note>
</text_field>

<text_field name="link_url" label="Link do site/produto">
<question>Qual o link do site/produto?</question>
<note>Obrigatorio para objetivos de site. Para mensagens, preenchido automaticamente (m.me/, ig.me/).</note>
</text_field>

<text_field name="call_to_action_type" label="Botao de acao">
<question>Qual botao de acao?</question>
<options>
  <option value="SHOP_NOW">Vendas</option>
  <option value="SIGN_UP">Leads (SIGN_UP, APPLY_NOW)</option>
  <option value="LEARN_MORE">Trafego</option>
  <option value="MESSAGE_PAGE">Mensagens (MESSAGE_PAGE, WHATSAPP_MESSAGE)</option>
  <option value="WATCH_MORE">Video</option>
  <option value="LEARN_MORE">Engajamento</option>
</options>
</text_field>

<text_field name="url_tags" label="Parametros UTM para rastreamento">
<critical_rule>UTMs sao AUTOMATICOS. NAO pergunte ao usuario. Inclua SEMPRE o valor padrao abaixo em TODOS os criativos. Mostrar no resumo final que UTMs foram incluidos.</critical_rule>
<default>utm_source={{placement}}&amp;utm_medium=meta_ads&amp;utm_campaign={{campaign.name}}&amp;utm_content={{ad.name}}</default>
</text_field>

</substep>

<substep number="7.4" name="Pagina e Instagram Actor">
<critical_rule>Para resolver page_id e instagram_actor_id, SEMPRE use get_account_pages(account_id) primeiro para listar TODAS as paginas conectadas a conta. Depois faca o match pelo nome que o usuario informou. NAO use search_pages_by_name como primeiro recurso — ele pode falhar se o nome nao for exato. Use search_pages_by_name apenas como fallback se get_account_pages nao encontrar.</critical_rule>
- Obter page_id e instagram_actor_id da lista retornada por get_account_pages.
- Se o usuario informou um nome de pagina, buscar na lista pelo nome mais proximo.
- Necessario para que o anuncio apareca no Instagram com o perfil correto.
</substep>

</step>

<step number="8" name="Anuncios (variacoes)">
<critical_rule>Minimo 3, maximo 6 anuncios por conjunto.</critical_rule>
<critical_rule>Os anuncios sao IGUAIS entre todos os adsets (mesmos criativos replicados).</critical_rule>

<question>Quantas variacoes de anuncio voce quer criar? Recomendo pelo menos 3 para a Meta testar qual funciona melhor.</question>

<options>
  <option value="textos_diferentes">3 variacoes com textos diferentes e mesma imagem</option>
  <option value="imagens_diferentes">3 variacoes com imagens diferentes e mesmo texto</option>
  <option value="combinacao">Combinacao de ambos</option>
</options>

<fills>Para cada variacao, coletar: message, headline, description, imagem/video.</fills>
</step>

<step number="9" name="Resumo antes de executar">
Mostrar resumo completo e pedir confirmacao:

<summary_template>
RESUMO DA CAMPANHA
==================

Campanha: [nome]
Objetivo: [objetivo em linguagem simples]
Orcamento: R$[valor]/dia
Modo de orcamento: [CBO ou ABO]
Status inicial: PAUSADO (voce ativa quando estiver pronto)

CONJUNTOS DE ANUNCIOS ([N] conjuntos):

  1. [Nome do adset]
     Publico: [descricao do publico]
     Idade: [X] a [Y] anos
     Genero: [genero]
     Local: [localizacao]
     [Se ABO: Orcamento: R$[valor]/dia]

  2. [Nome do adset]
     ...

ANUNCIOS ([N] anuncios, replicados em todos os conjuntos):

  1. [Nome do anuncio]
     Texto: [texto resumido]
     Titulo: [headline]
     Midia: [imagem/video]
     Link: [url]
     Botao: [CTA]
     UTMs: incluidos automaticamente

  2. [Nome do anuncio]
     ...

Total de ads que serao criados: [N anuncios x N adsets]

Confirma a criacao? (sim/nao)
</summary_template>
</step>

<step number="10" name="Execucao">
<critical_rule>Executar na seguinte ordem. NAO prosseguir se alguma etapa falhar.</critical_rule>

<substep number="10.1" name="Criar campanha">
<tool_call>
create_campaign(
  account_id,
  name,
  objective,
  budget_mode,         // "CBO" ou "ABO"
  status="PAUSED",
  special_ad_categories=[],
  daily_budget,        // apenas se CBO (em centavos)
  bid_strategy="LOWEST_COST_WITHOUT_CAP"
)
</tool_call>
<saves>campaign_id</saves>
</substep>

<substep number="10.2" name="Criar adsets (um por tipo de publico)">
Para CADA adset:
<tool_call>
create_adset(
  account_id,
  campaign_id,
  name,
  optimization_goal,
  billing_event="IMPRESSIONS",
  status="PAUSED",
  daily_budget,         // apenas se ABO (em centavos)
  targeting,            // targeting especifico do publico
  promoted_object,      // conforme objetivo
  destination_type      // se aplicavel
)
</tool_call>
<saves>lista de adset_ids</saves>
</substep>

<substep number="10.3" name="Upload de midia (uma unica vez)">
Para cada imagem:
<tool_call>
upload_ad_image(
  account_id,
  image_url="URL" ou file="base64..."
)
</tool_call>
<saves>image_hash</saves>

Para cada video:
<tool_call>
upload_ad_video(
  account_id,
  file_url="URL" ou file="base64...",
  title
)
</tool_call>
<saves>video_id</saves>
</substep>

<substep number="10.4" name="Criar criativos (uma unica vez)">
Para cada variacao de anuncio:
<tool_call>
create_ad_creative(
  account_id,
  name,
  image_hash ou video_id,
  page_id,
  link_url,
  message,
  headline,
  description,
  call_to_action_type,
  instagram_actor_id,
  url_tags
)
</tool_call>
<saves>lista de creative_ids</saves>
</substep>

<substep number="10.5" name="Criar ads (criativos x adsets)">
Para CADA adset, para CADA criativo:
<tool_call>
create_ad(
  account_id,
  name="[Nome criativo] - [Nome adset]",
  adset_id,
  creative_id,
  status="PAUSED"
)
</tool_call>
</substep>

<substep number="10.6" name="Resultado">
Mostrar resultado:
- IDs de tudo que foi criado (campanha, adsets, criativos, ads)
- Link para o Gerenciador de Anuncios
- Perguntar: "Tudo foi criado como PAUSADO. Quer que eu ative a campanha agora?"

Se sim, chamar update_campaign(campaign_id, status="ACTIVE").
</substep>

</step>

</steps>

<auto_fields>
Campos preenchidos automaticamente em todos os cenarios:
- status: PAUSED (seguranca: sempre confirmar antes de ativar)
- billing_event: IMPRESSIONS (padrao da Meta, recomendado para todos os objetivos)
- bid_strategy: LOWEST_COST_WITHOUT_CAP (lances automaticos, melhor custo por resultado)
- special_ad_categories: [] (lista vazia, a menos que seja emprego, imoveis, credito ou politica)
</auto_fields>

<advantage_audience_rules>
REGRAS CRITICAS sobre targeting_automation.advantage_audience na API v25.0:

1. SEMPRE incluir targeting_automation no targeting de TODOS os adsets.
2. Para adsets com flexible_spec (interesses): targeting_automation.advantage_audience = 0 (DESLIGA Advantage+). Isso permite controle total de idade, genero e interesses.
3. Para adsets com custom_audiences (publicos personalizados, lookalike): targeting_automation.advantage_audience = 0 (DESLIGA Advantage+). Queremos que a Meta use APENAS esses publicos.
4. Para adset de "publico aberto" (sem interesses nem custom_audiences): targeting_automation.advantage_audience = 0 tambem. Nao usar Advantage+ porque ele impede controle de idade (age_max nao pode ser menor que 65 com Advantage+ ativo).

RESUMO: SEMPRE usar targeting_automation.advantage_audience = 0 em TODOS os adsets. Isso garante controle total de idade/genero e evita erros da API.
</advantage_audience_rules>

<validations>
- pixel_id preenchido para objetivos de site (OFFSITE_CONVERSIONS, LANDING_PAGE_VIEWS com pixel)
- page_id preenchido para mensagens, formularios e engajamento
- link_url preenchido para criativos de site
- daily_budget > 0 (em centavos)
- Pelo menos 1 publico configurado
- Pelo menos 3 anuncios (variacoes de criativo)
- Interesses validados com validate_interests (se usar interesses)
- instagram_actor_id preenchido para aparecer no Instagram
- Para LEAD_GENERATION: TOS aceitos e permissoes verificadas
</validations>

<execution_order>
1. create_campaign(account_id, name, objective, budget_mode, status="PAUSED", daily_budget, bid_strategy)
2. create_adset(account_id, campaign_id, name, optimization_goal, billing_event, targeting, promoted_object, destination_type, daily_budget)
3. upload_ad_image(account_id, image_url) ou upload_ad_video(account_id, file_url, title)
4. create_ad_creative(account_id, name, image_hash/video_id, page_id, link_url, message, headline, description, call_to_action_type, instagram_actor_id, url_tags)
5. create_ad(account_id, name, adset_id, creative_id, status="PAUSED")
6. update_campaign(campaign_id, status="ACTIVE") -- apenas se o usuario confirmar ativacao
</execution_order>

<error_handling>
<error code="InvalidInterest" cause="Interesse removido pela Meta">
  Solucao: Usar search_interests para encontrar alternativa
</error>
<error code="1815089" cause="Lead Ads TOS nao aceitos">
  Solucao: Aceitar em facebook.com/ads/leadgen/tos/?page_id=PAGE_ID como perfil pessoal
</error>
<error code="1885760" cause="Optimization goals conflitantes em CBO">
  Solucao: Criar campanha separada para cada optimization_goal
</error>
<error code="2446886" cause="WhatsApp Business Platform nao configurado">
  Solucao: Configurar em business.facebook.com > WhatsApp Accounts
</error>
<error code="PixelNotFound" cause="Pixel nao existe ou nao tem acesso">
  Solucao: Criar pixel com create_pixel ou verificar permissoes
</error>
<error code="PageNotFound" cause="Pagina nao conectada a conta">
  Solucao: Verificar com get_account_pages
</error>
<error code="BudgetTooLow" cause="Orcamento muito baixo">
  Solucao: Aumentar para pelo menos R$20/dia por adset
</error>
</error_handling>

<tools_used>
- get_pixels: account_id
- create_pixel: account_id, name
- get_account_pages: account_id
- list_custom_audiences: account_id
- search_interests: query
- validate_interests: interest_ids
- get_interest_suggestions: interest_list
- estimate_audience_size: account_id, targeting
- search_behaviors: query
- search_demographics: query
- search_geo_locations: query
- create_campaign: account_id, name, objective, budget_mode, daily_budget, bid_strategy
- create_adset: account_id, campaign_id, name, optimization_goal, billing_event, targeting, promoted_object, destination_type, daily_budget
- upload_ad_image: account_id, image_url ou file
- upload_ad_video: account_id, file_url ou file, title
- create_ad_creative: account_id, image_hash/video_id, page_id, link_url, message, headline, description, call_to_action_type, instagram_actor_id, url_tags
- create_lead_form: page_id, name, questions, privacy_policy_url, follow_up_action_url
- create_ad: account_id, name, adset_id, creative_id, status
- update_campaign: campaign_id, status="ACTIVE"
</tools_used>

</workflow>
