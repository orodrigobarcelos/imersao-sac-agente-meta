<workflow name="configurar-pixel-conversoes">

<when_to_use>
Use este workflow quando o usuario quiser:
- Criar ou ver pixels de rastreamento
- Instalar o pixel no site
- Criar conversoes personalizadas (rastrear acoes especificas no site)
- Ver ou deletar conversoes existentes
- Configurar rastreamento de vendas, leads ou cadastros

Keywords de ativacao: pixel, conversao, rastrear, rastreamento, instalar pixel, codigo do pixel, configurar pixel, conversao personalizada, evento de conversao, rastrear compras, rastrear vendas, rastrear leads.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar o que e pixel e conversao em linguagem simples, guiar cada etapa com exemplos praticos. O usuario provavelmente nao sabe o que e um pixel.
- Avancado: aceitar comandos diretos como "criar pixel na conta act_XXX" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o que quer (ex: "preciso do codigo do meu pixel"), pular para a etapa correspondente.
</user_mode>

<steps>

<step number="1" name="O que o usuario quer fazer">
<question>O que voce gostaria de configurar?</question>
<options>
  <option value="criar_pixel">Criar pixel -- instalar um codigo no seu site para rastrear visitantes e acoes</option>
  <option value="ver_pixels">Ver meus pixels -- listar pixels existentes e obter o codigo de instalacao</option>
  <option value="criar_conversao">Criar conversao personalizada -- definir uma acao especifica para rastrear (compra, cadastro, etc.)</option>
  <option value="ver_conversoes">Ver minhas conversoes -- listar conversoes personalizadas configuradas</option>
  <option value="deletar_conversao">Deletar conversao -- remover uma conversao personalizada</option>
</options>
</step>

<step number="2" name="Criar pixel">

<step number="2.1" name="Explicacao para leigos">
Explicar: "O pixel e um codigo JavaScript invisivel que voce instala no seu site. Ele rastreia o que as pessoas fazem: quais paginas visitam, se adicionam ao carrinho, se compram. Com esses dados, a Meta consegue otimizar seus anuncios e encontrar as pessoas certas."
</step>

<step number="2.2" name="Verificar pixels existentes">
Antes de criar, chamar `get_pixels(account_id)` para verificar se ja existe um pixel.

Se ja tem pixel: "Voce ja tem um pixel configurado: [nome] (ID: [pixel_id]). Cada conta pode ter no maximo 100 pixels. Quer criar um novo mesmo assim ou quer ver o codigo do pixel existente?"

Se nao tem pixel: prosseguir para criacao.
</step>

<step number="2.3" name="Criar o pixel">
<question>Qual nome voce quer dar para o pixel?</question>
<if_unknown>Use o nome do seu site ou negocio. Exemplo: 'Pixel - Minha Loja'</if_unknown>
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
name: Nome do pixel -- obrigatorio
</fills>

Apos criar com sucesso, o retorno inclui o campo `code` com o codigo JavaScript do pixel.

Mostrar:

Pixel criado com sucesso!

Nome: [nome]
ID: [pixel_id]

Codigo de instalacao (copie e cole no seu site):
---
[codigo JavaScript do pixel]
---

IMPORTANTE: Pixel nao pode ser deletado via API. Uma vez criado, ele fica permanente na conta.
</step>

<step number="2.4" name="Orientacao de instalacao">
Explicar como instalar de acordo com a plataforma:

Como instalar o pixel:

O codigo acima deve ser colado no &lt;head&gt; de todas as paginas do seu site.

Por plataforma:
- WordPress: Instale o plugin "Meta Pixel" ou cole no tema em Aparencia > Editor de Temas > header.php
- Shopify: Va em Configuracoes > Aplicativos e canais de vendas > Meta > Configurar
- Wix: Va em Marketing > Integracoes de marketing > Pixel do Facebook
- Google Tag Manager: Crie uma tag HTML personalizada e cole o codigo
- Outro: Cole o codigo antes do &lt;/head&gt; em todas as paginas

Apos instalar, pode levar ate 24 horas para comecar a registrar dados.
Voce pode verificar se esta funcionando com a extensao "Meta Pixel Helper" no Chrome.
</step>

</step>

<step number="3" name="Listar pixels">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

Formato de apresentacao:

Seus pixels:

1. [nome] (ID: [pixel_id])
   Ultimo disparo: [last_fired_time ou "Nunca disparou"]
   Codigo JS: [mostrar o campo code se disponivel]

2. [nome] (ID: [pixel_id])
   ...

Total: [N] pixel(s)

Se algum pixel nunca disparou (last_fired_time vazio ou ausente): "Este pixel nunca recebeu dados. Verifique se o codigo foi instalado corretamente no seu site."

Se nao tem pixels: "Voce ainda nao tem pixels configurados. Quer criar um agora?"
</step>

<step number="4" name="Criar conversao personalizada">

<step number="4.1" name="Explicacao para leigos">
Explicar: "Uma conversao personalizada e uma regra que voce cria para rastrear acoes especificas no seu site. Por exemplo: quando alguem chega na pagina '/obrigado', isso conta como uma compra. A Meta usa esses dados para otimizar seus anuncios e mostrar para pessoas que tem mais chance de fazer a mesma acao."
</step>

<step number="4.2" name="Verificar pre-requisitos">
Chamar `get_pixels(account_id)` para verificar se existe pelo menos um pixel. Conversoes personalizadas precisam de um pixel como fonte de eventos.

Se nao tem pixel: "Para criar uma conversao personalizada, voce precisa de um pixel instalado primeiro. Quer criar um pixel agora?"
</step>

<step number="4.3" name="Coletar informacoes">

<question>Qual nome voce quer dar para essa conversao?</question>
<if_unknown>Use algo descritivo. Exemplo: 'Compra no Site', 'Cadastro Newsletter', 'Visualizou Produto'</if_unknown>

<question>Qual acao voce quer rastrear?</question>
<options>
  <option value="PURCHASE">Compra / Venda | Quando alguem compra algo</option>
  <option value="LEAD">Cadastro / Lead | Quando alguem se cadastra ou preenche formulario</option>
  <option value="COMPLETE_REGISTRATION">Registro / Criacao de conta | Quando alguem cria uma conta</option>
  <option value="ADD_TO_CART">Adicionar ao carrinho | Quando alguem adiciona produto ao carrinho</option>
  <option value="INITIATE_CHECKOUT">Iniciar checkout | Quando alguem comeca o processo de pagamento</option>
  <option value="VIEW_CONTENT">Visualizar conteudo | Quando alguem ve uma pagina especifica</option>
  <option value="SEARCH">Pesquisa | Quando alguem faz uma busca no site</option>
  <option value="ADD_TO_WISHLIST">Adicionar a lista de desejos | Quando alguem salva um produto</option>
  <option value="CONTACT">Contato | Quando alguem entra em contato</option>
</options>
<if_unknown>Para a maioria dos negocios, 'Compra' (PURCHASE) ou 'Cadastro' (LEAD) sao as conversoes mais importantes.</if_unknown>

<question>Em qual pagina do seu site essa acao acontece? (a URL da pagina de confirmacao)</question>
<if_unknown>Se apos a compra o cliente vai para 'meusite.com/obrigado', informe 'obrigado'.</if_unknown>

Montar a regra:
- Se o usuario informar uma palavra ou trecho: {"url":{"i_contains":"[trecho]"}}
- Se informar uma URL exata: {"url":{"eq":"[url completa]"}}

<question>Quanto vale em media cada conversao? (opcional, em reais)</question>
<if_unknown>Se voce sabe que cada venda vale em media R$ 100, informe aqui. Isso ajuda a Meta a calcular o retorno sobre o investimento (ROAS).</if_unknown>

<question>Quer adicionar uma descricao? (opcional)</question>
</step>

<step number="4.4" name="Criar a conversao">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
name: Nome da conversao -- obrigatorio
pixel_id: ID do pixel (campo event_source_id) -- obrigatorio
event_name: Nome do evento (PURCHASE, LEAD, etc.) -- obrigatorio
rule_url: JSON com a regra de URL -- obrigatorio
default_conversion_value: Valor monetario padrao da conversao -- opcional
description: Descricao da conversao -- opcional
</fills>

Apos criar com sucesso, mostrar:

Conversao personalizada criada com sucesso!

Nome: [nome]
ID: [custom_conversion_id]
Evento: [event_name em portugues]
Regra: Quando a URL [contem/e igual a] "[trecho]"
Valor padrao: R$ [valor] (ou "nao definido")
Pixel vinculado: [pixel_id]

Essa conversao ja esta ativa e comecara a registrar dados automaticamente quando alguem acessar a pagina configurada.
Voce pode usa-la como objetivo de otimizacao ao criar campanhas de vendas ou leads.
</step>

</step>

<step number="5" name="Listar conversoes personalizadas">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

Formato de apresentacao:

Suas conversoes personalizadas:

1. [nome] (ID: [custom_conversion_id])
   Evento: [event_name]
   Regra: [regra de URL]
   Valor padrao: R$ [valor] ou "nao definido"
   Pixel: [pixel_id]

2. [nome] (ID: [custom_conversion_id])
   ...

Total: [N] conversao(oes)

Se nao tem conversoes: "Voce ainda nao tem conversoes personalizadas. Quer criar uma agora?"
</step>

<step number="6" name="Deletar conversao personalizada">

<step number="6.1" name="Listar conversoes para selecao">
Primeiro, chamar `list_custom_conversions(account_id)` para mostrar as conversoes disponiveis.
</step>

<step number="6.2" name="Confirmar exclusao">
IMPORTANTE: Sempre confirmar antes de deletar.

Perguntar: "Tem certeza que deseja deletar a conversao '[nome]' (ID: [id])? Essa acao e irreversivel e todos os dados historicos dessa conversao serao perdidos."
</step>

<step number="6.3" name="Executar exclusao">
<fills>
custom_conversion_id: ID da conversao personalizada -- obrigatorio
</fills>

Apos deletar com sucesso:
"Conversao '[nome]' deletada com sucesso. Se alguma campanha usava essa conversao como objetivo, voce precisara atualizar o objetivo da campanha."
</step>

</step>

</steps>

<auto_fields>
pixel_id: obtido automaticamente via get_pixels ao criar conversao personalizada (usado como event_source_id)
account_id: mantido da selecao de conta do usuario
rule_url: montado automaticamente a partir do trecho de URL informado pelo usuario
</auto_fields>

<validations>
- Verificar se ja existe pixel antes de criar um novo (get_pixels)
- Verificar se existe pelo menos um pixel antes de criar conversao personalizada
- event_name deve ser um dos valores validos (PURCHASE, LEAD, COMPLETE_REGISTRATION, ADD_TO_CART, INITIATE_CHECKOUT, VIEW_CONTENT, SEARCH, ADD_TO_WISHLIST, CONTACT)
- rule_url deve estar em formato JSON valido: {"url":{"i_contains":"trecho"}} ou {"url":{"eq":"url_completa"}}
- Sempre confirmar antes de deletar conversao (acao irreversivel)
- Pixel nao pode ser deletado via API (alertar o usuario)
</validations>

<execution_order>
1. get_pixels(account_id) -- verificar pixels existentes
2. create_pixel(account_id, name) -- criar pixel se necessario
3. get_pixels(account_id) -- obter pixel_id para conversao
4. create_custom_conversion(account_id, name, pixel_id, event_name, rule_url, default_conversion_value, description)
5. list_custom_conversions(account_id) -- listar conversoes
6. delete_custom_conversion(custom_conversion_id) -- deletar conversao
</execution_order>

<error_handling>
<error code="pixel_creation_failed" cause="Limite de 100 pixels por conta atingido">Verificar pixels existentes com get_pixels e reutilizar um existente</error>
<error code="pixel_cannot_be_deleted" cause="Pixel nao pode ser removido via API">Pixels sao permanentes. Pode ser desativado no Gerenciador de Eventos</error>
<error code="no_pixel_found" cause="Conta sem pixel para criar conversao">Criar um pixel primeiro antes de criar conversoes</error>
<error code="invalid_rule_format" cause="JSON da regra de URL mal formatado">Verificar formato: {"url":{"i_contains":"trecho"}}</error>
<error code="custom_conversion_limit" cause="Limite de conversoes na conta atingido">Cada conta tem um limite de conversoes personalizadas. Deletar conversoes nao usadas</error>
<error code="permission_denied" cause="Token sem permissao para gerenciar pixels">Verificar se o token tem permissao ads_management</error>
<error code="event_source_not_found" cause="pixel_id invalido">Verificar o ID do pixel com get_pixels</error>
</error_handling>

<tools_used>
- create_pixel: account_id, name
- get_pixels: account_id
- create_custom_conversion: account_id, name, pixel_id (event_source_id), event_name, rule_url, default_conversion_value, description
- list_custom_conversions: account_id
- delete_custom_conversion: custom_conversion_id
</tools_used>

</workflow>
