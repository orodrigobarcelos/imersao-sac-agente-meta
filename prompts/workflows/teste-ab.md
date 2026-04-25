<workflow name="teste-ab">

<when_to_use>
Use este workflow quando o usuario quiser:
- Criar um teste A/B para comparar campanhas, conjuntos de anuncios ou criativos
- Saber qual anuncio ou publico funciona melhor
- Ver resultados de um teste A/B em andamento ou finalizado
- Listar testes A/B existentes na conta

Keywords de ativacao: teste AB, teste A/B, split test, comparar, qual funciona melhor, testar criativo, testar publico, testar campanha, qual anuncio e melhor, experimento.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar o que e um teste A/B em linguagem simples, guiar cada etapa com sugestoes, justificar as decisoes. O usuario provavelmente nao sabe o que e um teste A/B.
- Avancado: aceitar parametros diretos como "criar teste AB comparando adset X e adset Y por 7 dias" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja mencionou o que quer (ex: "quero ver resultados do meu teste"), pular para a etapa correspondente.
</user_mode>

<steps>

<step number="1" name="O que o usuario quer fazer">
<question>O que voce gostaria de fazer com testes A/B?</question>
<options>
  <option value="criar">Criar um teste novo -- comparar dois ou mais anuncios, publicos ou campanhas para descobrir qual funciona melhor</option>
  <option value="listar">Ver meus testes -- listar todos os testes A/B da conta</option>
  <option value="resultados">Ver resultados -- ver qual variacao ganhou em um teste especifico</option>
</options>
</step>

<step number="2" name="Criar teste A/B">

<step number="2.1" name="Explicacao para leigos">
Antes de comecar, explicar: "Um teste A/B divide seu publico em grupos iguais e mostra anuncios diferentes para cada grupo. Depois de alguns dias, a Meta analisa qual grupo teve melhores resultados e te diz o vencedor. E como fazer uma degustacao: voce testa duas receitas e ve qual as pessoas preferem."
</step>

<step number="2.2" name="Tipo de teste">
<question>O que voce quer comparar?</question>
<options>
  <option value="SPLIT_TEST" context="publicos">Quero comparar publicos diferentes | Testa conjuntos de anuncios (adsets) com publicos diferentes usando o mesmo anuncio</option>
  <option value="SPLIT_TEST" context="campanhas">Quero comparar campanhas inteiras | Testa campanhas completas com configuracoes diferentes</option>
  <option value="SPLIT_TEST_V2" context="criativos">Quero comparar criativos (imagens, textos, videos) | Testa anuncios diferentes para ver qual criativo performa melhor</option>
</options>
<if_unknown>
Explicar a diferenca:
- SPLIT_TEST: "Ideal para descobrir qual publico ou estrategia funciona melhor. Voce compara conjuntos de anuncios ou campanhas inteiros."
- SPLIT_TEST_V2: "Ideal para descobrir qual imagem, video ou texto chama mais atencao. Voce compara criativos diferentes."
</if_unknown>
</step>

<step number="2.3" name="Obter business_id">
Chamar `me/businesses` para obter o business_id. Se o usuario nao souber qual business usar:

Encontrei [N] business(es) vinculado(s):
1. [nome] (ID: [business_id])
2. [nome] (ID: [business_id])

Qual voce quer usar?

Se so tem um, usar automaticamente.
<fills>business_id: valor obtido da API</fills>
</step>

<step number="2.4" name="Selecionar os elementos para comparar">

Para SPLIT_TEST (comparar adsets ou campanhas):
<question>Voce ja tem os conjuntos de anuncios ou campanhas criados que quer comparar?</question>
<if_unknown>
- Se sim: pedir os IDs. Orientar: "Voce pode consultar suas campanhas e conjuntos com o comando 'listar campanhas' ou 'listar conjuntos de anuncios' se nao souber os IDs."
- Se nao: orientar a criar primeiro usando o workflow de criar campanha.
</if_unknown>

Para SPLIT_TEST_V2 (comparar criativos):
<question>Voce ja tem os anuncios criados que quer comparar?</question>
<if_unknown>
- Se sim: pedir os IDs dos ads.
- Se nao: orientar a criar primeiro usando o workflow de criar criativo.
</if_unknown>
</step>

<step number="2.5" name="Configurar o teste">
<question>Qual nome voce quer dar para esse teste?</question>
<if_unknown>Sugestao: "Teste [tipo] - [descricao curta] - [data]". Exemplo: "Teste Criativo - Video vs Imagem - Abril 2026"</if_unknown>

<question>Por quantos dias voce quer rodar o teste?</question>
<if_unknown>Recomendo no minimo 7 dias para ter dados confiaveis. O ideal e entre 7 e 14 dias.</if_unknown>

Se o usuario escolher menos de 7 dias, alertar: "Testes com menos de 7 dias podem nao ter dados suficientes para determinar um vencedor confiavel. Tem certeza?"

<question>Qual o orcamento diario total do teste? (em reais) -- obrigatorio para SPLIT_TEST_V2</question>
<if_unknown>Esse valor sera dividido igualmente entre as variacoes. Por exemplo, R$ 50/dia com 2 variacoes = R$ 25/dia para cada.</if_unknown>
</step>

<step number="2.6" name="Montar as celulas (grupos)">
Cada teste precisa de no minimo 2 celulas (grupos). Montar o JSON das celulas:

Para SPLIT_TEST com adsets:
```json
[
  {
    "name": "Grupo A - [descricao]",
    "treatment_percentage": 50,
    "adsets": ["ADSET_ID_1"]
  },
  {
    "name": "Grupo B - [descricao]",
    "treatment_percentage": 50,
    "adsets": ["ADSET_ID_2"]
  }
]
```

Para SPLIT_TEST com campaigns:
```json
[
  {
    "name": "Grupo A - [descricao]",
    "treatment_percentage": 50,
    "campaigns": ["CAMPAIGN_ID_1"]
  },
  {
    "name": "Grupo B - [descricao]",
    "treatment_percentage": 50,
    "campaigns": ["CAMPAIGN_ID_2"]
  }
]
```

Para SPLIT_TEST_V2 com ads:
```json
[
  {
    "name": "Grupo A - [descricao]",
    "treatment_percentage": 50,
    "ads": ["AD_ID_1"]
  },
  {
    "name": "Grupo B - [descricao]",
    "treatment_percentage": 50,
    "ads": ["AD_ID_2"]
  }
]
```

IMPORTANTE: A soma dos `treatment_percentage` de todas as celulas deve ser exatamente 100. Com 2 grupos, usar 50/50. Com 3 grupos, usar 34/33/33.
</step>

<step number="2.7" name="Calcular timestamps">
Converter as datas de inicio e fim para Unix timestamp (em segundos).

- start_time: inicio do teste. Recomendado: proximo dia util a partir de amanha. Calcular como Unix timestamp.
- end_time: final do teste. Calcular: start_time + (dias * 86400).

Exemplo para teste de 7 dias comecando amanha:
- start_time: timestamp de amanha as 00:00 no fuso do usuario
- end_time: timestamp de 7 dias depois as 23:59
</step>

<step number="2.8" name="Executar criacao">
<fills>
business_id: ID do business (obtido em 2.3) -- obrigatorio
name: Nome do teste -- obrigatorio
cells: JSON com os grupos (minimo 2) -- obrigatorio
start_time: Unix timestamp de inicio (segundos) -- obrigatorio
end_time: Unix timestamp de fim (segundos) -- obrigatorio
test_type: SPLIT_TEST ou SPLIT_TEST_V2 -- obrigatorio
daily_budget: Orcamento diario em centavos (obrigatorio para SPLIT_TEST_V2) -- condicional
</fills>

NOTA sobre daily_budget: o valor deve ser em centavos. Se o usuario informar R$ 50, enviar 5000.

Apos criar com sucesso, mostrar:

Teste A/B criado com sucesso!

Nome: [nome]
Tipo: [SPLIT_TEST ou SPLIT_TEST_V2]
ID do estudo: [study_id]
Periodo: [data inicio] a [data fim] ([N] dias)
Grupos:
  - [nome grupo A]: [percentual]% do publico
  - [nome grupo B]: [percentual]% do publico

O teste comecara automaticamente na data programada. Voce pode acompanhar os resultados a qualquer momento pedindo "ver resultados do teste".
</step>

</step>

<step number="3" name="Listar testes A/B">
<fills>
business_id: ID do business -- obrigatorio
</fills>

Se o usuario nao souber o business_id, buscar automaticamente com `me/businesses`.

Formato de apresentacao:

Seus testes A/B:

1. [nome] (ID: [study_id])
   Tipo: [SPLIT_TEST / SPLIT_TEST_V2]
   Periodo: [data inicio] a [data fim]
   Status: [em andamento / finalizado / programado]

2. [nome] (ID: [study_id])
   ...

Total: [N] teste(s)

Se nao houver testes: "Voce ainda nao tem testes A/B. Quer criar um agora?"
</step>

<step number="4" name="Ver resultados de um teste A/B">
<fills>
study_id: ID do estudo/teste A/B -- obrigatorio
</fills>

Se o usuario nao souber o study_id, listar primeiro com `list_ab_tests` e perguntar qual teste quer ver.

Formato de apresentacao:

Resultados do Teste A/B: [nome]
Periodo: [data inicio] a [data fim]
Status: [em andamento / finalizado]

Grupo A - [nome]:
  - Gasto: R$ X.XXX,XX
  - Resultados: X [tipo]
  - Custo por resultado: R$ X,XX
  - Impressoes: X.XXX
  - Alcance: X.XXX

Grupo B - [nome]:
  - Gasto: R$ X.XXX,XX
  - Resultados: X [tipo]
  - Custo por resultado: R$ X,XX
  - Impressoes: X.XXX
  - Alcance: X.XXX

---
Vencedor: [nome do grupo vencedor] (custo por resultado X% menor)

Se o teste ainda estiver em andamento: "O teste ainda esta rodando. Os resultados parciais indicam que [grupo X] esta na frente, mas e cedo para conclusoes. Recomendo esperar o teste terminar para decisoes definitivas."

Se o teste finalizou: "O teste terminou e o grupo [X] foi o vencedor. Recomendo usar a estrategia/criativo do grupo vencedor nas suas proximas campanhas."
</step>

</steps>

<auto_fields>
treatment_percentage: calculado automaticamente (50/50 para 2 grupos, 34/33/33 para 3 grupos)
start_time: calculado como Unix timestamp a partir da data informada
end_time: calculado como start_time + (dias * 86400)
daily_budget: convertido de reais para centavos (valor * 100)
</auto_fields>

<validations>
- business_id deve ser obtido via me/businesses antes de criar ou listar testes
- cells deve ter no minimo 2 grupos
- A soma dos treatment_percentage deve ser exatamente 100
- start_time deve ser uma data futura (Unix timestamp em segundos)
- end_time deve ser posterior a start_time
- daily_budget e obrigatorio para SPLIT_TEST_V2 e deve ser em centavos
- IDs de adsets/campaigns/ads nos cells devem ser validos
</validations>

<execution_order>
1. create_ab_test(business_id, name, cells, start_time, end_time, test_type, daily_budget)
2. list_ab_tests(business_id)
3. get_ab_test_results(study_id)
</execution_order>

<error_handling>
<error code="business_not_found" cause="Token sem acesso ao business">Verificar permissoes do token em business_management</error>
<error code="invalid_cells_format" cause="JSON das celulas mal formatado">Verificar que cada celula tem name, treatment_percentage, e adsets/campaigns/ads</error>
<error code="treatment_percentages_not_100" cause="Porcentagens nao somam 100">Ajustar os valores para somar exatamente 100</error>
<error code="minimum_2_cells" cause="Menos de 2 grupos">Adicionar pelo menos 2 grupos para comparar</error>
<error code="invalid_start_time" cause="Timestamp no passado ou formato errado">Usar Unix timestamp em segundos, data futura</error>
<error code="daily_budget_required" cause="Orcamento nao informado para SPLIT_TEST_V2">Para testes de criativo (V2), o orcamento diario e obrigatorio</error>
<error code="entity_not_found" cause="ID invalido nos cells">Verificar os IDs com get_campaigns, get_adsets ou get_ads</error>
<error code="duplicate_study" cause="Teste duplicado com mesmos parametros">Alterar o nome ou os parametros do teste</error>
</error_handling>

<targeting_note>
As tools `search_behaviors` e `search_demographics` sao usadas no workflow de criar campanha (`criar-campanha.md`) na secao de targeting/segmentacao. Elas nao se aplicam diretamente a testes A/B, mas sao uteis na etapa anterior de criar os conjuntos de anuncios que serao comparados no teste.
</targeting_note>

<tools_used>
- create_ab_test: business_id, name, cells, start_time, end_time, test_type, daily_budget
- list_ab_tests: business_id
- get_ab_test_results: study_id
- get_campaigns: account_id (auxiliar)
- get_adsets: account_id ou campaign_id (auxiliar)
- get_ads: account_id ou adset_id (auxiliar)
</tools_used>

</workflow>
