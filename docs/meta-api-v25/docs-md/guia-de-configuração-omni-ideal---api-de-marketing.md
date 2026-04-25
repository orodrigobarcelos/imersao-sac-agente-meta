<!-- Fonte: Guia de configuração omni ideal - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Guia de configuração técnica omni: boas práticas e requisitos


## Configuração de eventos


Uma configuração de evento ideal permite a coleta de dados de alta qualidade, o que é essencial para o desempenho do sistema de anúncios. Estes dados de alta qualidade ajudam a definir e apresentar anúncios com precisão, o que pode levar a um melhor engajamento, taxas de conversão mais elevadas e, em última análise, a um melhor retorno sobre o investimento.


## Parâmetros obrigatórios/recomendados


A lista consiste em todos os parâmetros de dados de evento obrigatórios/recomendados e outros parâmetros de dados que os anunciantes precisam passar para a Meta via API de Conversões/Pixel da Meta a fim de usá-los na otimização da veiculação e da atribuição de anúncios.


#### Parâmetros dos eventos


- Nome do evento
- Hora do evento
- Client_user_agent (apenas web)
- Action_source
- Event_source_url (apenas web)
- Dados personalizados (altamente recomendados para anúncios dinâmicos) - IDs de conteúdo - Tipo de conteúdo - Conteúdo - Quantidade - Moeda (obrigatório para eventos de compra) - Valor (obrigatório para eventos de compra)


#### Parâmetros de informações do cliente


- Email
- Número de telefone
- Nome
- Sobrenome
- Endereço IP (apenas web)
- Agente do usuário (apenas web)
- Fbc (apenas web)
- Fbp (apenas web)


**Nota**: [encontre aqui](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters) uma lista completa de parâmetros de informações do cliente e requisitos de hash.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Qualidade da correspondência de eventos e taxas de correspondência


### Pontuações de qualidade da correspondência de eventos (apenas eventos da web)


As pontuações de qualidade da correspondência de eventos (EMQ, pelas iniciais em inglês) são uma métrica usada para avaliar a eficácia da integração da API de Conversões de um anunciante na correspondência de eventos com os usuários da Meta. As pontuações variam de 1 a 10, com pontuações mais altas indicando uma correspondência mais eficaz. Alguns dos parâmetros de informações PII com maior ponderação são:


- Email
- Número de telefone
- Endereço IP
- Agente do usuário
- FBP
- FBC
- Nome
- Sobrenome


### Pontuação de qualidade dos dados offline


A pontuação de qualidade dos dados offline (ODQ, pelas iniciais em inglês) avalia o quanto seus eventos offline estão alinhados com os requisitos de publicidade da Meta, com foco na cobertura dos eventos para melhorar o desempenho e a precisão da mensuração.


#### Como a qualidade dos dados offline é calculada


Para calcular a pontuação de qualidade dos dados offline, consideramos fatores como atualização, frequência e atribuição dos dados:


- **Frequência:** é o número de dias, nos últimos 14 dias, em que o evento esteve presente nas partições (ou seja, em que eventos offline foram enviados para a Meta).
- **Atualização:** é o tempo médio entre a ocorrência e o envio do evento nos últimos 28 dias.
- **Cobertura das chaves de correspondência**: é o número de eventos que contêm determinadas quantidades de chaves de correspondência fortes (como email, telefone ou ID do dispositivo em anúncios para dispositivos móveis) dividido pelo número total de eventos nos últimos 28 dias.
- **Volume de eventos offline**: é o número de compras de produtos nos últimos 28 dias que tiveram pelo menos um anúncio vinculado ao ID da fonte de dados nesse mesmo período.
- **Comportamento offline semelhante ao online**: é a proporção de compras na loja física que são enviadas logo após a impressão, refletindo um comportamento típico de transações online.
- **Valores de compra válidos**: são os valores de compras válidos (compras com preço superior a zero) em relação ao total de eventos nos últimos 28 dias.
- **Divisão de carrinho**: os eventos de compra não devem ser divididos em vários eventos (a melhor opção é incluir vários itens em um único evento de compra). A mensuração é feita pela relação entre itens e compras nos últimos 2 dias.
- **Atribuição**: indica se os anúncios rastreiam automaticamente eventos offline para a geração de relatórios.
- **Precisão**: indica se você envia dados offline sem erros ou inconsistências (observação: **não envie**[dados do site como um evento offline](https://www.facebook.com/legal/technology_terms)).


Esses fatores, ponderados de forma diferente, são combinados em uma pontuação de até 10.


#### O que a pontuação significa


- **Pontuação alta (8 a 10)**: indica correspondência forte, identificação eficaz do usuário e melhor atribuição de anúncios.
- **Pontuação média (4 a 7)**: indica correspondências parciais, sugerindo que há espaço para melhorias.
- **Pontuação baixa (0 a 3)**: indica correspondência fraca, com a maioria dos eventos offline não enviados para a Meta, o que reduz a qualidade dos dados e a atribuição dos anúncios.


### Como verificar as pontuações de EMQ e ODQ:


Acesse **Gerenciador de Eventos** > **Selecione ID do Pixel** > **Selecione o nome do evento** > **Visualizar detalhes** >**Qualidade do evento**


Como alternativa ao Gerenciador de Eventos, você pode utilizar a [Integration Quality API](https://developers.facebook.com/docs/marketing-api/conversions-api/integration-quality-api) para verificar as pontuações de EMQ. Para saber mais sobre esta API e como maximizar a EMQ, consulte nossa [documentação aqui](https://developers.facebook.com/docs/marketing-api/conversions-api/integration-quality-api).


### Benefícios da qualidade dos dados offline


Melhorar a qualidade dos dados offline é fundamental para aprimorar seus anúncios omnichannel, otimizados para vendas online e na loja.


#### O valor da qualidade dos dados offline na habilitação de anúncios omnichannel


Focar na qualidade dos dados offline é essencial para sua estratégia de publicidade omnichannel:


- **Desempenho de anúncio aprimorado**: uma pontuação alta garante dados precisos e atualizados para um direcionamento eficaz em todos os canais.
- **Mensuração precisa**: pontuações robustas possibilitam uma atribuição precisa das conversões offline, o que é fundamental para entender o impacto dos anúncios e aprimorar estratégias.
- **Campanhas otimizadas**: uma pontuação igual ou superior a 8,5 permite o uso eficaz de anúncios omnichannel, garantindo o alcance do público adequado no momento certo.


#### Exemplo: melhorar a qualidade dos dados offline no varejo


Um varejista com uma pontuação 6 de 10 pode garantir melhorias implementando estas medidas:


- **Aumentar a frequência do envio de dados**: carregue dados com mais regularidade.
- **Melhorar a precisão dos dados**: reduza erros e inconsistências.
- **Aprimorar a atribuição**: forneça todas as chaves de correspondência recomendadas para maximizar a precisão da mensuração de conversões offline.


Trabalhar nessas áreas pode aumentar a pontuação, gerando melhores resultados de publicidade, como mais compras e um direcionamento mais eficiente.


A Meta fornece recomendações personalizadas no Gerenciador de Eventos para ajudar a melhorar a pontuação de qualidade dos seus dados offline.


### Melhorar a qualidade dos dados offline


Para melhorar sua métrica de qualidade dos dados offline:


- Carregue novos dados regularmente para garantir precisão no direcionamento e na mensuração. - Carregue dados diariamente. - Confira se os dados de transações offline não estão desatualizados (com mais de 3 dias).
- Implemente processos robustos de validação de dados para minimizar erros e inconsistências. - Envie os preços de compra corretos (por exemplo, sem valores zero ou negativos). - Evite vincular identificações de conjuntos de dados incorretas a campanhas omni. Observação: use apenas uma fonte de sinal offline para a otimização de campanhas omni. Para fins de mensuração (nível do rastreamento de anúncios), o anunciante pode vincular várias fontes de sinal offline, mas não para a otimização no nível do conjunto de anúncios.
- Habilite o [rastreamento automático de eventos offline](https://www.facebook.com/business/help/1480558938621580) para atribuir com precisão as conversões offline.
- Monitore seus procedimentos de coleta e processamento de dados para manter dados de alta qualidade.
- Analise regularmente a qualidade dos seus dados offline no Gerenciador de Eventos e siga as recomendações personalizadas para melhorar essa pontuação.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Nível de atualidade dos dados


Priorize o compartilhamento de eventos em tempo real para uma melhor otimização da campanha. Verifique se há pouco ou nenhum atraso desde a ocorrência dos seus eventos até seu compartilhamento com a Meta. Isto vai ajudar a:


- Veicular anúncios com otimização superior graças a dados em tempo real para atualizar os seus públicos
- Ver os resultados de uma campanha de anúncios mais perto do tempo real no Gerenciador de Anúncios da Meta.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Eventos do site


Para eventos da web, é essencial transmitir dados em tempo real para proporcionar o desempenho ideal. O Pixel da Meta e a API de Conversões são os métodos mais eficazes para enviar dados de eventos em tempo real.


Para avaliar seu status atual, navegue até **Gerenciador de Eventos** > **ID do Pixel** > **Nome do evento** > **Visualizar detalhes** > **Nível de atualidade dos dados** > **Site**

[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Eventos offline


Para eventos offline, recomendamos enviar dados com a maior frequência possível, pois isso ajudaria nossos algoritmos a impulsionar o desempenho em tempo real/quase real. A recomendação é retornar dados offline pelo menos uma vez ao dia e, de preferência, a cada hora. Para avaliar seu status atual, navegue até **Gerenciador de Eventos** > **ID do Pixel** > **Nome do evento** > **Visualizar detalhes** > **Nível de atualidade dos dados** > **Atividade offline**.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Desduplicação


O Pixel da Meta e a API de Conversões permitem compartilhar eventos padrão e personalizados conosco para poder medir e otimizar o desempenho dos anúncios. O pixel permite o compartilhamento de eventos da web por meio de um navegador. Já a API de Conversões permite o compartilhamento de eventos da web diretamente do seu servidor.


Se você conectar a atividade do site usando tanto o pixel quanto a API de Conversões, poderemos receber os mesmos eventos do navegador e do servidor. Se identificarmos que os eventos são idênticos e redundantes, poderemos manter um e descartar o resto. Isso se chama desduplicação.


É altamente recomendado incluir parâmetros de desduplicação com seus eventos para garantir que nossos sistemas possam identificar e processar eventos com precisão apenas uma vez. Isto é crucial para fins de atribuição e mensuração precisas.


#### Eventos da web


Ao enviar eventos redundantes usando o Pixel da Meta e a API de Conversões,**assegure-se de que ambos os eventos usem o event_name idêntico e que event_id ou uma combinação de external_id e fbp estejam incluídos**. Recomendamos incluir todos esses parâmetros para ajudar a Meta a desduplicar os eventos apropriadamente e reduzir a incidência de relatórios duplos para eventos idênticos. **A janela máxima de desduplicação é de 48 horas**.


#### Eventos offline


Ao contrário da desduplicação configurada nos eventos da API de Conversões e Pixel da Meta, **os eventos offline só podem ser desduplicados em relação a outros eventos offline**. Damos suporte a dois métodos de desduplicação:


- Baseado em `order_id`
- baseado no usuário


A desduplicação usa a combinação dos campos: `dataset_id`, `event_time`, `event_name`, `item_number` e o campo `order_id` ou informações do usuário como o "campo-chave" baseado no método da carga do evento específico.


A desduplicação padrão usa order_id com uma combinação dos campos acima. Se order_id não estiver presente na carga, a lógica de desduplicação baseada no usuário será usada. **A janela de desduplicação máxima é de 7 dias.** Saiba mais sobre a desduplicação de eventos offline no nosso [site de documentação do desenvolvedor](https://developers.facebook.com/docs/marketing-api/conversions-api/offline-events).


**Recomendamos não dividir seu pedido em vários eventos em vez de enviar um evento para representar o pedido todo**.


Por exemplo, quando houver dois pedidos com `event_time` idêntico, `event_name` tendo o mesmo `order_id` ou o mesmo conjunto de Parâmetros de Informações do Cliente sem `order_id`, eles serão considerados eventos duplicados e usaremos o primeiro evento. O método de desduplicação baseado no usuário só funciona com os mesmos campos de Parâmetros de Informações do Cliente nas duas cargas.


Outra forma de maximizar a taxa de captura de PII é no seu armazenamento. Ao enviar transações por email que capturam PII (incluindo recibos), você pode aumentar o volume de eventos para impulsionar a otimização do desempenho nas plataformas da Meta.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Qualidade do evento


A qualidade do evento mede a correção dos parâmetros nos eventos recebidos de fontes de eventos ligadas a um catálogo. A baixa qualidade do evento afeta a taxa de correspondência, a disponibilidade e pode resultar em fases de aprendizagem mais longas, além de otimização da campanha abaixo do ideal. Observe que é altamente recomendado que estes parâmetros sejam retornados através de eventos da web e offline.


Alguns dos parâmetros importantes que precisam ser aprovados são:


**1. Identificações de conteúdo**


Informar à Meta a identificação de conteúdo especifico de um produto ou grupo de produtos. A identificação de conteúdo deve corresponder exatamente à identificação do produto ou do grupo de produtos para esse item do seu catálogo, dependendo de qual content_type você inseriu. A correspondência indica que se trata do mesmo produto ou grupo do seu catálogo. Exemplo: ['123','456']


**2. Conteúdo (maneira recomendada de enviar detalhes do conteúdo)**


Informar à Meta a identificação do conteúdo específico, que precisa corresponder ao número de identificação do item no seu catálogo. Se você usar conteúdo no seu parâmetro, também deverá incluir o seguinte em um subobjeto: a identificação ou as identificações dos produtos e a quantidade (número de itens adicionados ao carrinho ou comprados).


Exemplo: [{id: '123', quantity: 2}, {id: '456', quantity: 1}]. Esta é maneira que recomendamos para repassar as informações.


**3. Tipo de conteúdo**


Deve ser definido como `product` ou `product_group`:


- Use `product` se as chaves enviadas por você representarem produtos. As chaves enviadas podem ser `content_ids` ou conteúdo.
- Use `product_group` se as chaves enviadas por você em `content_ids` representarem grupos de produtos. Os grupos de produtos são usados para diferenciar produtos idênticos que apresentam variações, como cor, material, tamanho ou estampa.


**4. Moeda**


Obrigatório para eventos de compra. É a moeda para o valor especificado, se aplicável. A moeda deve ser um código [ISO 4217](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_4217%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR0CtnCe-QMMDrf9cqJOE8TBny7cnfG3kcPFkq-uOJTkO2U3W-vEtW84ZFI_aem_bXCd0DS25QdidMvS9zGFdQ&h=AT4FrzrXtmOl73-ORTa_B0ZI4AyPZDfGQeMrzZauWSJbmPgUAd6alWZkZCJOhE3KVPhr6IBYomafZg7OSAS1KxhUb1kZzgfS01AIRCXi9d9-gSvXxu0EN5EEOJgxzDMYPcJcwG2kBaMgfAsVGO3CEthznqc) válido de três dígitos.


**5. Valor**


Obrigatório para eventos de compra. Um valor numérico associado ao evento. Certifique-se de que esse valor seja >= 0.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Configuração do catálogo


Um catálogo é um contêiner com informações sobre os itens que os anunciantes desejam anunciar ou vender no Facebook e no Instagram. Os catálogos são um bloco fundamental de vários dos nossos produtos disponíveis, incluindo (mas não limitado a):


- Campanhas de compras Advantage+
- Anúncios Colaborativos
- Anúncios de coleção
- Anúncios em carrossel
- Lojas


Para garantir uma configuração de qualidade para seu catálogo de anúncios omnichannel, certifique-se de que as seguintes áreas estejam cobertas e sejam ideais:


### Taxas de correspondência do catálogo


Uma correspondência de catálogo ocorre quando um evento é associado a um produto. A taxa de sucesso disso é conhecida como taxa de correspondência do catálogo. As taxas de correspondência ideais do catálogo são > 90%


#### Eventos do site


Para verificar as taxas de correspondência do catálogo para eventos da web, acesse **Gerenciador de Comércio** > **Selecionar Catálogo** > **Eventos** > **Selecionar fonte de dados** (conjunto de dados ou app).


#### Eventos offline


Os eventos offline devem ser integrados através da API (o carregamento manual está disponível, mas para usar o Beta de Anúncios Omnichannel, CAPI ou OCAPI é necessária a integração).


- Frequência de carregamento: - Carregue dados diariamente, pelo menos 12 vezes nos últimos 14 dias. - Confira se os dados de transações offline não estão desatualizados (com mais de 3 dias).
- Os dados de eventos offline precisam ser transmitidos nos últimos 14 dias, qualificando a conta para anúncios omnichannel.
- Evite dividir sua integração de eventos offline garantindo que você passe todos os itens da mesma transação que a mesma linha/cesta. Isso garante a precisão da mensuração do valor médio dos pedidos e do custo por compra.


### Conectando o catálogo com o conjunto de dados


Verifique se a fonte de dados (conjunto de dados/app) está corretamente vinculada ao catálogo. Se não estiver, siga as etapas abaixo para estabelecer uma conexão entre o conjunto de dados/app e o catálogo.


- Acessar o Gerenciador de Comércio
- Selecione eventos.
- Clique em **Gerenciar conexões**.
- Selecione a identificação do conjunto de dados/app.
- Clique em **Salvar**.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Habilitando o rastreamento automático para o conjunto de dados


O rastreamento automático do conjunto de dados permite que *qualquer campanha futura* nessa conta de anúncios seja automaticamente rastreada através do conjunto de dados. Isso é importante para a atribuição da campanha. Para habilitar o rastreamento automático, [siga estas etapas](https://www.facebook.com/business/help/1480558938621580).


Para adicionar o rastreamento de conjunto de dados às campanhas existentes, acesse a configuração do anúncio e habilite o rastreamento dentro das especificações de rastreamento.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Público omni


Público omni é uma solução de direcionamento especial que permite aos anunciantes criar públicos com base na atividade do usuário em vários canais.


Por exemplo, se um anunciante quiser criar um público de pessoas que visualizaram um produto no site e depois foram à loja comprar, é possível usar este tipo de público.


### Boas práticas e requisitos


[Taxas de correspondência](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#match-rates): as taxas de correspondência de evento são cruciais para determinar o tamanho do público. É essencial ter taxas de correspondência altas para eventos offline e pontuações de EMQ ideais para eventos da web a fim de garantir um público com tamanho adequado.


[Atualização dos dados](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#data-freshness): como os públicos omni são criados com base nas ações do usuário que acontecem nos canais, receber dados com menos atraso tornaria o público mais recente e preciso.
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)

## Saiba mais


- [Parâmetros de informações do cliente da API de Conversões](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters)
- [Como enviar eventos offline usando a API de Conversões](https://developers.facebook.com/docs/marketing-api/conversions-api/offline-events)
- [Ativar o rastreamento automático para conjuntos de eventos offline no Gerenciador de Eventos da Meta](https://www.facebook.com/business/help/1480558938621580)
- [Integration Quality API](https://developers.facebook.com/docs/marketing-api/conversions-api/integration-quality-api)
[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)[○](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#)Nesta Página[Guia de configuração técnica omni: boas práticas e requisitos](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#guia-de-configura--o-t-cnica-omni--boas-pr-ticas-e-requisitos)[Configuração de eventos](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#configura--o-de-eventos)[Parâmetros obrigatórios/recomendados](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#par-metros-obrigat-rios-recomendados)[Qualidade da correspondência de eventos e taxas de correspondência](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#match-rates)[Pontuações de qualidade da correspondência de eventos (apenas eventos da web)](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#pontua--es-de-qualidade-da-correspond-ncia-de-eventos--apenas-eventos-da-web-)[Pontuação de qualidade dos dados offline](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#pontua--o-de-qualidade-dos-dados-offline)[Como verificar as pontuações de EMQ e ODQ:](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#como-verificar-as-pontua--es-de-emq-e-odq-)[Benefícios da qualidade dos dados offline](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#benef-cios-da-qualidade-dos-dados-offline)[Melhorar a qualidade dos dados offline](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#melhorar-a-qualidade-dos-dados-offline)[Nível de atualidade dos dados](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#data-freshness)[Eventos do site](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#eventos-do-site)[Eventos offline](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#eventos-offline)[Desduplicação](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#desduplica--o)[Qualidade do evento](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#qualidade-do-evento)[Configuração do catálogo](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#configura--o-do-cat-logo)[Taxas de correspondência do catálogo](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#taxas-de-correspond-ncia-do-cat-logo)[Conectando o catálogo com o conjunto de dados](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#conectando-o-cat-logo-com-o-conjunto-de-dados)[Habilitando o rastreamento automático para o conjunto de dados](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#habilitando-o-rastreamento-autom-tico-para-o-conjunto-de-dados)[Público omni](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#p-blico-omni)[Boas práticas e requisitos](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#boas-pr-ticas-e-requisitos)[Saiba mais](https://developers.facebook.com/docs/marketing-api/best-practices/omni-optimal-setup-guide#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR65Eyxzu80Dj7ZEhEPc7Ggq6JomvtQ_oY-p--FwlIBi-cZEiXh3_KVDSls4sA_aem_3baEZ-uCJ1fBAPcuC3YNfA&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR53RjbslRvDfrTEksuILJYE3x55bpldbX-1pV14rH0FObTaZnNVEONyobzDig_aem_z82tAcy8fyEdx7iOeDqg5g&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR75hncCjXPBHTlFv7Ks3st1eisBmZ-bDw1n7Ckk75kVfRQTpeLHo7ntzNM9WQ_aem_66swT1AsuBpi5dYIWkeuTw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR65Eyxzu80Dj7ZEhEPc7Ggq6JomvtQ_oY-p--FwlIBi-cZEiXh3_KVDSls4sA_aem_3baEZ-uCJ1fBAPcuC3YNfA&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gmmYtdVoO9QnmK9xPT1SL2QCx3B4gFL8kexpIIf596YlxKondm8Egi_RAsw_aem_lZzVjVU3iEm1GN7BFC0d3w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7qoQPz7M4i7QLPKm6ZhHENZP7-rSRR-dVTnx0IqgGChWGzK017JMX43mSSvA_aem_qHASxcKkMbpuMPbihMYf0w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5lWZ6XbtJXZCvX6nuGtRJDPzfi2-vYcuXg47VKkm-BMCLQ-7uNRBDIZJpLKw_aem_j5KTJGtQ9cWOxGHrKMm7cQ&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6iAOirCPICDc-Hk9IVSPcNMYxhfKsG3rtCAmFuCEHIYPpP4b5nezN62dyl1w_aem_80XTiAjKI1vbVnNE3eIXTg&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR53RjbslRvDfrTEksuILJYE3x55bpldbX-1pV14rH0FObTaZnNVEONyobzDig_aem_z82tAcy8fyEdx7iOeDqg5g&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR75hncCjXPBHTlFv7Ks3st1eisBmZ-bDw1n7Ckk75kVfRQTpeLHo7ntzNM9WQ_aem_66swT1AsuBpi5dYIWkeuTw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7qoQPz7M4i7QLPKm6ZhHENZP7-rSRR-dVTnx0IqgGChWGzK017JMX43mSSvA_aem_qHASxcKkMbpuMPbihMYf0w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5lWZ6XbtJXZCvX6nuGtRJDPzfi2-vYcuXg47VKkm-BMCLQ-7uNRBDIZJpLKw_aem_j5KTJGtQ9cWOxGHrKMm7cQ&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gmmYtdVoO9QnmK9xPT1SL2QCx3B4gFL8kexpIIf596YlxKondm8Egi_RAsw_aem_lZzVjVU3iEm1GN7BFC0d3w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7G50-h624woWSNTW3nJ2qmakqyNBfYKVNN1aYDyRZ4ydvnLUXPmIh92yqNwg_aem_gEZbp8XAh9hU2OvOv3cSPw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gmmYtdVoO9QnmK9xPT1SL2QCx3B4gFL8kexpIIf596YlxKondm8Egi_RAsw_aem_lZzVjVU3iEm1GN7BFC0d3w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5gmmYtdVoO9QnmK9xPT1SL2QCx3B4gFL8kexpIIf596YlxKondm8Egi_RAsw_aem_lZzVjVU3iEm1GN7BFC0d3w&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR75hncCjXPBHTlFv7Ks3st1eisBmZ-bDw1n7Ckk75kVfRQTpeLHo7ntzNM9WQ_aem_66swT1AsuBpi5dYIWkeuTw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR75hncCjXPBHTlFv7Ks3st1eisBmZ-bDw1n7Ckk75kVfRQTpeLHo7ntzNM9WQ_aem_66swT1AsuBpi5dYIWkeuTw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR65Eyxzu80Dj7ZEhEPc7Ggq6JomvtQ_oY-p--FwlIBi-cZEiXh3_KVDSls4sA_aem_3baEZ-uCJ1fBAPcuC3YNfA&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR75hncCjXPBHTlFv7Ks3st1eisBmZ-bDw1n7Ckk75kVfRQTpeLHo7ntzNM9WQ_aem_66swT1AsuBpi5dYIWkeuTw&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5KURkTYv21i65kA82Av7_YzByycB2AHAO0U4PiEmqU_eJye15pnFXXI-MFPT3rvsdBFxA-4RVlMnnA_lJQsvtQBL_yujxMqaqAWMohNHupwwtwXzDJ2B7P6jb9Pz6ce8zqH4etQHTBKpEBz5VeNGVCPLw)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão