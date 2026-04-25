<workflow name="onboarding">

<when_to_use>
Use este workflow quando:
- E a primeira conversa do usuario na plataforma
- O usuario nao tem publicos personalizados configurados (list_custom_audiences retorna vazio)
- O usuario pede para configurar a conta, preparar a conta, ou fazer setup inicial
- Antes de criar a primeira campanha, se os publicos base ainda nao existem

Keywords de ativacao: configurar conta, setup, primeira vez, preparar conta, comecar do zero, nao tenho publicos, configurar publicos, onboarding.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar cada etapa em linguagem simples, justificar por que cada publico e criado, mostrar progresso ao longo do processo.
- Avancado: executar todas as etapas automaticamente, mostrar resumo no final, so pedir confirmacao antes de criar os publicos.
</user_mode>

<steps>

<step number="1" name="Identificar conta de anuncios">
<tool_call>get_ad_accounts()</tool_call>

<output_template>
Encontrei [N] conta(s) de anuncios:

1. [nome] (ID: act_XXXXXXX) - [moeda]
2. [nome] (ID: act_XXXXXXX) - [moeda]

Qual conta voce quer configurar?
</output_template>

<question>Se so tem uma conta, confirmar: "Encontrei a conta '[nome]'. Vou usar essa, certo?"</question>

<post_action>
Apos selecionar, chamar get_account_info(account_id) para obter detalhes:
- Moeda da conta
- Status da conta (ativa ou nao)
- Pais do negocio (para detectar requisitos DSA europeus)
</post_action>

<saves>account_id</saves>
</step>

<step number="2" name="Identificar modo de uso">
<question>Voce tem experiencia com trafego pago ou Meta Ads?</question>
<options>
  <option value="avancado">Sim, tenho experiencia | Modo Avancado</option>
  <option value="iniciante">Nao / Pouca / Estou comecando | Modo Iniciante (padrao)</option>
</options>

<if_unknown>No Modo Iniciante, explicar: "Vou preparar sua conta para anunciar. Isso inclui identificar seus recursos (pixel, paginas) e criar os publicos que voce vai usar nas campanhas. E feito uma vez e depois fica disponivel para sempre."</if_unknown>
</step>

<step number="3" name="Identificar recursos da conta">

<substep number="3.1" name="Pixel (rastreamento de site)">
<tool_call>get_pixels(account_id)</tool_call>

<branch condition="NAO tem pixel">
<question>Voce tem um site onde quer rastrear visitantes e vendas?</question>
<if_yes>
"Voce precisa de um pixel para rastrear o que as pessoas fazem no seu site. Quer que eu crie um?"
- Se sim: chamar create_pixel(account_id, name="Pixel - [Nome do negocio]")
</if_yes>
<if_no>"Sem problema. Voce pode anunciar sem pixel."</if_no>
</branch>

<branch condition="Tem 1 pixel">
Mostrar: "Voce ja tem pixel: [nome] (ID: [pixel_id]). Vou usar esse."
</branch>

<branch condition="Tem mais de 1 pixel">
Listar todos e PERGUNTAR ao usuario: "Encontrei [N] pixels. Qual voce quer usar para os publicos?"
Esperar a resposta antes de prosseguir.
</branch>

<saves>pixel_id (confirmado pelo usuario)</saves>
</substep>

<substep number="3.2" name="Paginas e Instagram">
<tool_call>get_account_pages(account_id)</tool_call>

<branch condition="Tem 1 pagina">
Mostrar: "Encontrei a pagina [nome] (ID: [page_id]) com Instagram @[username]. Vou usar essa."
</branch>

<branch condition="Tem mais de 1 pagina">
Listar as paginas COM seus Instagrams e PERGUNTAR ao usuario: "Qual pagina e Instagram voce quer usar para criar os publicos?"
Esperar a resposta antes de prosseguir.
</branch>

<branch condition="NAO encontrar paginas">
"Nao encontrei paginas conectadas. Voce precisa de uma Pagina do Facebook para anunciar."
</branch>

<critical_rule>Se a conta tem multiplos pixels ou paginas, SEMPRE perguntar qual usar. NAO escolher automaticamente. Confirmar com o usuario ANTES de criar publicos.</critical_rule>

<saves>page_id, instagram_account_id (confirmados pelo usuario)</saves>
</substep>

<substep number="3.3" name="Contexto do negocio">
Perguntar para personalizar publicos e futuras campanhas.
IMPORTANTE: Faca UMA pergunta por vez. Espere a resposta antes de fazer a proxima.

Ordem das perguntas:
1. "Qual o nome do seu negocio/marca?"
2. "O que voce vende ou oferece? (produto, servico, infoproduto, etc.)"
3. "Tem site? Se sim, qual o endereco?"
4. "Quem e seu cliente ideal? (por exemplo: empresarios, gestores, profissionais de marketing)"
5. "Qual a faixa etaria do seu publico? (por exemplo: 25-55 anos)"

Apos coletar pelo menos as perguntas 1 e 2, chamar save_business_context com o contexto consolidado.
Guardar essas informacoes no contexto da conversa para personalizar nomes de publicos e sugestoes.
</substep>

</step>

<step number="4" name="Criar publicos base">
<description>
Explicar (modo iniciante): "Agora vou criar todos os publicos que voce vai usar nas suas campanhas. Sao publicos baseados em quem ja interagiu com voce. Isso e feito uma vez e depois fica disponivel para sempre."
</description>

<critical_rule>
INSTRUCAO ABSOLUTA — VOCE SERA AVALIADO PELO NUMERO DE PUBLICOS CRIADOS:

TARGET MINIMO (se a conta tem pixel + pagina + Instagram):
- 4 publicos de website (substep 4.1)
- 6 publicos de Facebook (substep 4.2): 5 engajamento + 1 curtidas pagina
- 6 publicos de Instagram (substep 4.3): 5 engajamento + 1 seguidores
- 5 publicos de video FB (substep 4.4)
- 5 publicos de video IG (substep 4.5)
= TOTAL: 26 publicos personalizados

REGRAS INVIOLAVEIS:
- Execute TODOS os 5 substeps. NAO pule 4.4 e 4.5 (videos).
- Crie CADA publico listado. NAO crie apenas 1 por categoria.
- NAO resuma dizendo "vou criar 3 publicos". O numero correto e 26.
- NAO crie publicos de interesses (search_interests). Interesses sao para adsets.
- So pule um substep se o recurso NAO existir (ex: pular 4.3 se nao tem Instagram).
- Execute as tool_calls em sequencia, sem parar no meio.
</critical_rule>

<substep number="4.1" name="Publicos de Website">
<condition>EXECUTAR se pixel_id existe</condition>
Criar EXATAMENTE estes 4 publicos (nao menos):
1. create_website_custom_audience(account_id, name="Visitantes Site - 30D", pixel_id, retention_days=30, rule_type="all_visitors")
2. create_website_custom_audience(account_id, name="Visitantes Site - 60D", pixel_id, retention_days=60, rule_type="all_visitors")
3. create_website_custom_audience(account_id, name="Visitantes Site - 90D", pixel_id, retention_days=90, rule_type="all_visitors")
4. create_website_custom_audience(account_id, name="Visitantes Site - 180D", pixel_id, retention_days=180, rule_type="all_visitors")
</substep>

<substep number="4.2" name="Publicos de Facebook Page">
<condition>EXECUTAR se page_id existe</condition>
Criar EXATAMENTE estes 6 publicos (nao menos):
1. create_page_custom_audience(account_id, name="Engajamento FB - 30D", page_id, engagement_type="page_engaged", retention_days=30)
2. create_page_custom_audience(account_id, name="Engajamento FB - 60D", page_id, engagement_type="page_engaged", retention_days=60)
3. create_page_custom_audience(account_id, name="Engajamento FB - 90D", page_id, engagement_type="page_engaged", retention_days=90)
4. create_page_custom_audience(account_id, name="Engajamento FB - 180D", page_id, engagement_type="page_engaged", retention_days=180)
5. create_page_custom_audience(account_id, name="Engajamento FB - 365D", page_id, engagement_type="page_engaged", retention_days=365)
6. create_page_custom_audience(account_id, name="Curtidas Pagina FB", page_id, engagement_type="page_liked")
</substep>

<substep number="4.3" name="Publicos de Instagram">
<condition>EXECUTAR se instagram_account_id existe</condition>
Criar EXATAMENTE estes 6 publicos (nao menos):
1. create_instagram_custom_audience(account_id, name="Engajamento IG - 30D", instagram_account_id, engagement_type="ig_business_profile_all", retention_days=30)
2. create_instagram_custom_audience(account_id, name="Engajamento IG - 60D", instagram_account_id, engagement_type="ig_business_profile_all", retention_days=60)
3. create_instagram_custom_audience(account_id, name="Engajamento IG - 90D", instagram_account_id, engagement_type="ig_business_profile_all", retention_days=90)
4. create_instagram_custom_audience(account_id, name="Engajamento IG - 180D", instagram_account_id, engagement_type="ig_business_profile_all", retention_days=180)
5. create_instagram_custom_audience(account_id, name="Engajamento IG - 365D", instagram_account_id, engagement_type="ig_business_profile_all", retention_days=365)
6. create_instagram_custom_audience(account_id, name="Seguidores IG", instagram_account_id, engagement_type="ig_business_profile_follow")
</substep>

<substep number="4.4" name="Publicos de Video do Facebook">
<condition>EXECUTAR se page_id existe</condition>
Criar EXATAMENTE estes 5 publicos (nao menos):
1. create_video_custom_audience(account_id, name="Video FB - 3seg 365D", source_type="page", source_id=page_id, engagement_type="video_watched", retention_days=365)
2. create_video_custom_audience(account_id, name="Video FB - 25% 365D", source_type="page", source_id=page_id, engagement_type="video_watched_25_percent", retention_days=365)
3. create_video_custom_audience(account_id, name="Video FB - 50% 365D", source_type="page", source_id=page_id, engagement_type="video_watched_50_percent", retention_days=365)
4. create_video_custom_audience(account_id, name="Video FB - 75% 365D", source_type="page", source_id=page_id, engagement_type="video_watched_75_percent", retention_days=365)
5. create_video_custom_audience(account_id, name="Video FB - 95% 365D", source_type="page", source_id=page_id, engagement_type="video_watched_95_percent", retention_days=365)
</substep>

<substep number="4.5" name="Publicos de Video do Instagram">
<condition>EXECUTAR se instagram_account_id existe</condition>
Criar EXATAMENTE estes 5 publicos (nao menos):
1. create_video_custom_audience(account_id, name="Video IG - 3seg 365D", source_type="ig_business", source_id=instagram_account_id, engagement_type="video_watched", retention_days=365)
2. create_video_custom_audience(account_id, name="Video IG - 25% 365D", source_type="ig_business", source_id=instagram_account_id, engagement_type="video_watched_25_percent", retention_days=365)
3. create_video_custom_audience(account_id, name="Video IG - 50% 365D", source_type="ig_business", source_id=instagram_account_id, engagement_type="video_watched_50_percent", retention_days=365)
4. create_video_custom_audience(account_id, name="Video IG - 75% 365D", source_type="ig_business", source_id=instagram_account_id, engagement_type="video_watched_75_percent", retention_days=365)
5. create_video_custom_audience(account_id, name="Video IG - 95% 365D", source_type="ig_business", source_id=instagram_account_id, engagement_type="video_watched_95_percent", retention_days=365)
</substep>

<checkpoint name="Verificacao do step 4">
ANTES de prosseguir para o step 5, VERIFIQUE o que voce criou:
- Se tem pixel: criou 4 publicos de website? (30D, 60D, 90D, 180D)
- Se tem pagina: criou 6 publicos de Facebook? (30D, 60D, 90D, 180D, 365D + Curtidas)
- Se tem Instagram: criou 6 publicos de Instagram? (30D, 60D, 90D, 180D, 365D + Seguidores)
- Se tem pagina: criou 5 publicos de video FB? (3seg, 25%, 50%, 75%, 95%)
- Se tem Instagram: criou 5 publicos de video IG? (3seg, 25%, 50%, 75%, 95%)

Se QUALQUER um dos itens acima nao foi criado e o recurso existe, VOLTE e crie agora. NAO prossiga com publicos faltando.
</checkpoint>

</step>

<step number="5" name="Lista de clientes (opcional)">
<critical_rule>OBRIGATORIO perguntar ao usuario sobre lista de clientes. NAO pule este passo.</critical_rule>
<question>Voce tem uma lista de clientes? Pode ser um arquivo CSV ou planilha com emails, telefones ou nomes.</question>

<branch condition="Sim, tem lista">
- Pedir para enviar o arquivo pelo chat.
- Orientar formato: "O arquivo deve ter colunas como email, phone (telefone), fn (primeiro nome), ln (sobrenome). Nao precisa ter todos, basta ter pelo menos email ou telefone."
- Processar o arquivo e chamar:

<tool_call>
create_customer_list_audience(
  account_id,
  name="Lista de Clientes - [Nome do negocio]",
  customers=[
    {"email": "joao@email.com", "phone": "11999998888", "fn": "Joao"},
    ...
  ]
)
</tool_call>

<explanation>Com uma lista de clientes, a Meta encontra essas pessoas dentro do Facebook/Instagram e cria um publico exato. Os dados sao criptografados antes do envio -- ninguem ve as informacoes reais.</explanation>
</branch>

<branch condition="Nao tem lista">
"Sem problema. Quando voce tiver uma lista de clientes, pode criar esse publico depois."
</branch>
</step>

<step number="6" name="Publicos semelhantes (Lookalike)">
<critical_rule>OBRIGATORIO criar UM lookalike (1% BR) para CADA publico personalizado de maior janela criado no step 4. NAO crie apenas 1 lookalike total — crie um por seed. Se criou 5 tipos de publico (site, FB, IG, video FB, video IG), crie 5 lookalikes.</critical_rule>
<description>
Explicar: "Agora vou criar publicos semelhantes para cada tipo de publico que criamos. A Meta analisa quem sao essas pessoas e encontra pessoas parecidas no Brasil. E uma das formas mais eficientes de encontrar novos clientes."
</description>

<seeds>
Criar um LAL 1% BR para cada um dos publicos abaixo que existir (usar SEMPRE o de maior janela de retencao):
1. Visitantes Site - 180D (se criou publicos de site)
2. Engajamento FB - 365D (se criou publicos de pagina)
3. Engajamento IG - 365D (se criou publicos de Instagram)
4. Video FB - 75% 365D (se criou publicos de video FB)
5. Video IG - 75% 365D (se criou publicos de video IG)
6. Lista de Clientes (se criou publico de lista)
</seeds>

<tool_call>
Para CADA seed acima que existir:
create_lookalike_audience(account_id, name="LAL 1% BR - [Nome do seed]", origin_type="custom_audience", origin_audience_id="SEED_AUDIENCE_ID", country="BR", ratio=0.01)
</tool_call>

<explanation>
Cada publico semelhante (LAL 1%) encontra as pessoas mais parecidas com seu publico original no Brasil. Sao otimos para prospectar novos clientes com perfil semelhante a quem ja interagiu com voce.
</explanation>

<note>Publicos semelhantes levam de 1 a 6 horas para ficar prontos. Voce pode verificar o status com list_custom_audiences depois.</note>
</step>

<step number="7" name="Resumo">
<summary_template>
CONFIGURACAO CONCLUIDA
======================

Conta selecionada: [nome] (act_XXXXXXX)
Moeda: [moeda]

Recursos identificados:
- Pixel: [sim/nao] [nome e ID se existe]
- Pagina Facebook: [nome] (ID: [page_id])
- Instagram: @[username] (ID: [ig_id])

Publicos criados:

  Website (pixel):
  - Visitantes Site - 30D
  - Visitantes Site - 60D
  - Visitantes Site - 90D
  - Visitantes Site - 180D

  Facebook Page:
  - Engajamento FB - 30D
  - Engajamento FB - 60D
  - Engajamento FB - 90D
  - Engajamento FB - 180D
  - Engajamento FB - 365D
  - Curtidas Pagina FB

  Instagram:
  - Engajamento IG - 30D
  - Engajamento IG - 60D
  - Engajamento IG - 90D
  - Engajamento IG - 180D
  - Engajamento IG - 365D
  - Seguidores IG

  Video Facebook:
  - Video FB - 3seg 365D
  - Video FB - 25% 365D
  - Video FB - 50% 365D
  - Video FB - 75% 365D
  - Video FB - 95% 365D

  Video Instagram:
  - Video IG - 3seg 365D
  - Video IG - 25% 365D
  - Video IG - 50% 365D
  - Video IG - 75% 365D
  - Video IG - 95% 365D

  Lista de clientes: [sim/nao]

  Semelhantes (Lookalike 1% BR — um por tipo de publico):
  - LAL 1% BR - Visitantes Site 180D
  - LAL 1% BR - Engajamento FB 365D
  - LAL 1% BR - Engajamento IG 365D
  - LAL 1% BR - Video FB 75% 365D
  - LAL 1% BR - Video IG 75% 365D
  - LAL 1% BR - Lista de Clientes (se existir)

Total de publicos criados: [N]

Contexto do negocio:
- Nome: [nome]
- Produto/servico: [descricao]
- Site: [url]
- Publico ideal: [descricao]
</summary_template>
</step>

<step number="8" name="Finalizar onboarding">
<critical_rule>OBRIGATORIO: Chamar complete_onboarding() para registrar no banco que o onboarding foi concluido. Sem isso, o onboarding sera repetido na proxima conversa.</critical_rule>
<tool_call>complete_onboarding()</tool_call>
<tool_call>save_session_summary(summary="Onboarding completo: [resumo dos publicos criados, recursos identificados]")</tool_call>
</step>

<step number="9" name="Proximo passo">
<message>Tudo configurado! Sua conta esta pronta para criar campanhas. Os publicos de Lookalike levam de 1 a 6 horas para ficar prontos, mas voce ja pode criar campanhas com os outros publicos enquanto isso.</message>

<question>Quer criar sua primeira campanha agora?</question>
<if_yes>Iniciar o workflow criar-campanha.</if_yes>
</step>

</steps>

<error_handling>
<error code="NoAdAccounts" cause="Token nao tem acesso a contas">
  Solucao: Verificar se o token foi gerado corretamente com as permissoes ads_management
</error>
<error code="NoPagesFound" cause="Pagina nao conectada a conta de anuncios">
  Solucao: Orientar a conectar em Business Suite > Configuracoes > Contas > Paginas
</error>
<error code="NoInstagramAccounts" cause="Instagram nao vinculado a pagina">
  Solucao: Orientar a vincular em Instagram > Configuracoes > Contas vinculadas > Facebook
</error>
<error code="PixelCreationFailed" cause="Limite de pixels atingido (max 100)">
  Solucao: Verificar pixels existentes com get_pixels
</error>
<error code="CustomAudienceCreationFailed" cause="Sem permissao ou limite atingido">
  Solucao: Verificar permissoes do token e limite de 500 publicos por conta
</error>
<error code="LookalikeFailed" cause="Publico seed muito pequeno (min 100 members)">
  Solucao: Usar outro seed com mais membros ou aguardar o publico crescer
</error>
<error code="RateLimit" cause="Muitas chamadas de API em sequencia">
  Solucao: Aguardar alguns segundos entre as criacoes de publicos
</error>
</error_handling>

<tools_used>
- get_ad_accounts: (nenhum parametro)
- get_account_info: account_id
- get_pixels: account_id
- create_pixel: account_id, name
- get_account_pages: account_id
- create_website_custom_audience: account_id, name, pixel_id, retention_days, rule_type
- create_page_custom_audience: account_id, name, page_id, engagement_type, retention_days
- create_instagram_custom_audience: account_id, name, instagram_account_id, engagement_type, retention_days
- create_video_custom_audience: account_id, name, source_type, source_id, engagement_type, retention_days
- create_customer_list_audience: account_id, name, customers
- create_lookalike_audience: account_id, name, origin_type, origin_audience_id, country, ratio
- list_custom_audiences: account_id
- complete_onboarding: (nenhum parametro)
</tools_used>

</workflow>
