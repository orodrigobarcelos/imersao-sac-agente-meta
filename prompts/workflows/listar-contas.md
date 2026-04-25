<workflow name="listar-selecionar-conta">

<when_to_use>
Use este workflow quando:
- E o primeiro acesso do usuario e ele precisa selecionar uma conta
- O usuario quer ver quais contas de anuncio tem disponiveis
- O usuario quer trocar de conta de anuncios
- O usuario quer ver detalhes de uma conta especifica (saldo, moeda, status)
- O usuario quer saber quais recursos estao configurados na conta (pixel, paginas, Instagram)

Keywords de ativacao: minhas contas, listar contas, qual conta, selecionar conta, trocar conta, ver conta, conta de anuncios, saldo, moeda, status da conta, primeira vez, comecar.
</when_to_use>

<user_mode>
- Iniciante (padrao): apresentar as contas de forma clara com explicacao de cada campo, guiar a selecao e mostrar o que tem configurado na conta escolhida.
- Avancado: listar contas de forma resumida e aceitar selecao direta por ID.
- Deteccao automatica: se o usuario ja informou o account_id ou nome da conta, pular para os detalhes.
</user_mode>

<steps>

<step number="1" name="Listar contas de anuncios">
Nenhum parametro necessario (busca todas as contas acessiveis pelo token).

Formato de apresentacao:

Suas contas de anuncios:

| # | Nome | ID | Status | Moeda |
|---|------|-----|--------|-------|
| 1 | [nome] | act_XXXXXXX | Ativa | BRL (Real) |
| 2 | [nome] | act_XXXXXXX | Desativada | USD (Dolar) |

Total: [N] conta(s)

<status_mapping>
Mapeamento de status para portugues:
| Codigo | Status em portugues |
| 1      | Ativa |
| 2      | Desativada |
| 3      | Nao publicavel |
| 7      | Analise pendente |
| 8      | Em analise |
| 9      | Em periodo de carencia |
| 100    | Fechada |
| 101    | Qualquer conta ativa |
| 201    | Qualquer conta fechada |
</status_mapping>

Se so tem uma conta, sugerir automaticamente: "Encontrei uma unica conta: '[nome]'. Vou usar essa, certo?"

Se tem varias contas: "Qual conta voce quer usar? Informe o numero ou o ID."

Se nao encontrar contas: "Nao encontrei contas de anuncios vinculadas ao seu token. Verifique se o token foi gerado com a permissao ads_management e se voce tem acesso a pelo menos uma conta no Gerenciador de Anuncios."

<fills>account_id: valor selecionado pelo usuario</fills>
</step>

<step number="2" name="Ver detalhes da conta selecionada">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

Formato de apresentacao:

Detalhes da conta: [nome]

- ID: [account_id]
- Status: [status em portugues]
- Moeda: [currency] ([nome da moeda])
- Fuso horario: [timezone_name]
- Saldo disponivel: [balance formatado na moeda da conta]
- Gasto total: [amount_spent formatado na moeda da conta]

Se a conta nao estiver ativa (status diferente de 1), alertar: "Esta conta nao esta ativa (status: [status]). Voce pode ter restricoes para criar campanhas. Verifique no Gerenciador de Anuncios da Meta se ha alguma pendencia."
</step>

<step number="3" name="Verificar recursos da conta">
Apos mostrar os detalhes, verificar automaticamente os recursos disponiveis na conta.

<step number="3.1" name="Verificar pixels">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

Mostrar:
Pixels configurados:
- [nome] (ID: [pixel_id]) -- Ultimo disparo: [data ou "nunca"]

Se nao tem pixel: "Nenhum pixel configurado. O pixel e importante para rastrear acoes no seu site (vendas, cadastros). Voce pode criar um depois com o comando 'configurar pixel'."
</step>

<step number="3.2" name="Verificar paginas e Instagram">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

Mostrar:
Paginas conectadas:

1. [nome da pagina] (ID: [page_id])
   Instagram vinculado: @[username] (ID: [ig_id]) - [N] seguidores

2. [nome da pagina] (ID: [page_id])
   Instagram vinculado: nenhum

Se nao tem paginas: "Nenhuma pagina conectada a essa conta. Voce precisa de pelo menos uma Pagina do Facebook para criar anuncios. Conecte uma em Business Suite > Configuracoes > Contas > Paginas."

Se tem pagina mas nao tem Instagram: "Sua pagina nao tem um Instagram vinculado. Para anunciar no Instagram, vincule sua conta em Instagram > Configuracoes > Contas vinculadas > Facebook."
</step>

</step>

<step number="4" name="Resumo da conta">
Apresentar um resumo consolidado:

Resumo da conta: [nome]

Conta: [account_id] - [status]
Moeda: [currency]
Saldo: [balance]

Recursos disponiveis:
- Pixel: [sim (nome) / nao configurado]
- Paginas: [N] conectada(s)
- Instagram: [sim (@username) / nao vinculado]
</step>

<step number="5" name="Proximo passo">
Encerrar com sugestoes baseadas no que foi encontrado:

Se tem pagina e pixel: "Conta selecionada e pronta! Voce ja tem pixel e pagina configurados. O que quer fazer?"
- Configurar publicos (onboarding)
- Criar sua primeira campanha
- Ver relatorios de performance

Se tem pagina mas nao tem pixel: "Conta selecionada! Voce tem pagina mas nao tem pixel. Recomendo:"
- Configurar pixel primeiro (para rastrear acoes no site)
- Criar uma campanha de trafego ou mensagens (nao precisa de pixel)

Se nao tem pagina: "Conta selecionada, mas voce precisa conectar uma Pagina do Facebook antes de criar anuncios. Faca isso em Business Suite > Configuracoes > Contas > Paginas."
</step>

</steps>

<auto_fields>
account_id: selecionado automaticamente se o usuario tiver apenas uma conta
status: traduzido automaticamente do codigo numerico para portugues
</auto_fields>

<validations>
- Token deve ter permissao ads_management para listar contas
- account_id deve comecar com "act_" seguido de numeros
- Verificar se a conta esta ativa (status = 1) antes de sugerir criacao de campanhas
- Verificar existencia de pixel e paginas antes de sugerir proximos passos
</validations>

<execution_order>
1. get_ad_accounts() -- listar todas as contas
2. get_account_info(account_id) -- detalhes da conta selecionada
3. get_pixels(account_id) -- verificar pixels
4. get_account_pages(account_id) -- verificar paginas e Instagram
5. search_pages_by_name(account_id, search_term) -- auxiliar, buscar pagina por nome
</execution_order>

<error_handling>
<error code="no_ad_accounts_found" cause="Token sem acesso a contas de anuncio">Verificar se o token foi gerado com permissao ads_management e se o usuario tem acesso a pelo menos uma conta</error>
<error code="invalid_account_id" cause="account_id com formato errado">O ID deve comecar com "act_" seguido de numeros. Exemplo: act_123456789</error>
<error code="account_disabled" cause="Conta desativada pela Meta">Verificar no Gerenciador de Anuncios se ha restricoes ou violacoes de politica</error>
<error code="permission_denied" cause="Token sem permissao suficiente">Gerar novo token com permissoes ads_management e pages_read_engagement</error>
<error code="no_pages_found" cause="Nenhuma pagina vinculada">Conectar uma Pagina do Facebook a conta de anuncios no Business Suite</error>
<error code="rate_limit_exceeded" cause="Muitas chamadas em sequencia">Aguardar alguns segundos e tentar novamente</error>
</error_handling>

<tools_used>
- get_ad_accounts: (nenhum parametro)
- get_account_info: account_id
- get_pixels: account_id
- get_account_pages: account_id
- search_pages_by_name: account_id, search_term
</tools_used>

</workflow>
