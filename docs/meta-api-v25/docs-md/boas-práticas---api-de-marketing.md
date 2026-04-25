<!-- Fonte: Boas práticas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/best-practices -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Boas práticas


## Alterações de anúncio acionando análises de anúncio


Caso faça alguma alteração nos seguintes cenários, o anúncio será acionado para análise:


- Quaisquer alterações no criativo (imagem, texto, link, vídeo, entre outros)
- Quaisquer alterações de direcionamento
- Quaisquer alterações de metas de otimização e eventos de cobrança também podem acionar a análise


**Observação**: as alterações realizadas em valor do lance, orçamento e conjunto de anúncios não afetarão o status da análise.


Além disso, se um anúncio entrar na Análise de anúncios com o status de veiculação “Pausado”, ele permanecerá nesse status ao sair da Análise de anúncios. Caso contrário, o anúncio será considerado ativo e pronto para veiculação.
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Paginação


Para obter dados de resposta da paginação, consulte a [Paginação da Graph API](https://developers.facebook.com/docs/graph-api/results).
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Informações do usuário


Armazene IDs dos usuários, chaves de sessão e identificação da conta de anúncios para facilitar o acesso programático a esses dados e mantê-los juntos. Isso é importante porque as chamadas feitas com o número de identificação da conta de um usuário e a chave de sessão de outro usuário falharão se houver erro de permissão. O armazenamento de dados do usuário precisa ser realizado em conformidade com os [Termos da Plataforma do Facebook](https://developers.facebook.com/terms) e com as [Políticas do Desenvolvedor](https://developers.facebook.com/devpolicy).
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Lances sugeridos


Execute relatórios frequentes das campanhas, uma vez que os lances sugeridos mudam de forma dinâmica em resposta aos concorrentes que usam direcionamentos semelhantes. As sugestões de lance serão atualizadas em algumas horas, dependendo dos lances dos concorrentes.
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Solicitações em lote


Para fazer solicitações múltiplas à API com uma única chamada, consulte:


- [Solicitações múltiplas](https://developers.facebook.com/docs/graph-api/making-multiple-requests)
- [Solicitações em lote](https://developers.facebook.com/docs/reference/ads-api/batch-requests)


Também é possível consultar diversos objetos pelo ID da seguinte forma:

```
https://graph.facebook.com/<API_VERSION>?ids=[id1,id2]
```


Para fazer uma consulta por campo específico:

```
https://graph.facebook.com/<API_VERSION>?ids=[id1,id2]&amp;fields=field1,field2
```
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Verificar alterações de dados com ETags


Para verificar rapidamente se a resposta a uma solicitação foi alterada desde a última vez, consulte:


- [Blog de ETags](https://developers.facebook.com/blog/post/627/)
- [Referência sobre ETags](https://developers.facebook.com/docs/reference/ads-api/etags-reference/)
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Status de arquivado e excluído do objeto


Os objetos de anúncio têm dois tipos de estado de exclusão: arquivado e excluído. É possível consultar objetos arquivados e excluídos com a identificação do objeto. Entretanto, não retornaremos os objetos excluídos se você os solicitar a partir da borda de outro objeto.


É possível arquivar até 5 mil objetos a cada vez. Deve-se passar os objetos de anúncio do estado arquivado para o excluído se não precisar mais carregá-los por meio de bordas. Para saber como os estados funcionam e ver exemplos de chamadas, consulte [Armazenamento de objetos de anúncio](https://developers.facebook.com/docs/ads-api/best-practices/storing_adobjects).
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Visualizar erros


De forma incorreta, as pessoas tentam criar anúncios que não são aceitos. O documento [Códigos de erro](https://developers.facebook.com/docs/reference/ads-api/error-reference) apresenta causas de falhas em chamadas de API. É recomendável exibir o erro aos usuários de alguma maneira para que possam corrigir os anúncios.
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Grupo da comunidade de desenvolvedores de marketing do Facebook


Participe do grupo da [Comunidade de Desenvolvedores de Marketing do Facebook](https://www.facebook.com/groups/pmdcommunity/) para receber notícias e atualizações sobre a API de Marketing. Postamos itens do [blog da API de Marketing](https://developers.facebook.com/ads/blog/) no grupo.
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Teste


O modo sandbox é um ambiente de testes para leitura e gravação de chamadas da API de Marketing sem veiculação dos anúncios. Consulte [Modo sandbox para desenvolvedores](https://developers.facebook.com/ads/blog/post/2016/10/19/sandbox-ad-accounts/)


Experimente fazer chamadas de API com o [Explorador da Graph API](https://developers.facebook.com/tools/explorer). Experimente fazer qualquer chamada à API de Marketing. Veja a [post de blog](https://developers.facebook.com/blog/post/517/). Selecione seu app em `App` e conceda a ele a permissão `ads_management` ou `ads_read` em `extended permissions` quando criar um token de acesso. Use `ads_read` se você precisar de acesso à API de Insights sobre Anúncios apenas para gerar relatórios. Use `ads_management` para ler e atualizar anúncios em uma conta.


Para [desenvolvedores e acesso básico](https://developers.facebook.com/docs/reference/ads-api/access), configure uma lista de contas de anúncios para as quais o app pode fazer chamadas de API. Consulte a [lista de contas](https://developers.facebook.com/docs/reference/ads-api/access#standard_accounts).


Você pode usar o modo sandbox para demonstrar seu app na análise. No entanto, não é possível criar anúncios nem criativos do anúncio no modo sandbox. Por isso, será preciso usar identificações de anúncios e de criativos do anúncio embutidos em código para demonstrar seu uso da API para análise de apps.


### Critérios básicos


- Demonstrar valor além das soluções principais do Facebook, como o [Gerenciador de anúncios do Facebook](https://www.facebook.com/ads/manager/).
- Voltado para os objetivos do negócio, como aumentar as vendas. Os objetivos comerciais do Facebook podem ser encontrados [aqui](https://developers.facebook.com/docs/reference/ads-api/guides/chapter-2-objective-connections).
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)

## Políticas


Entenda as políticas de API. O Facebook tem o direito de auditar sua atividade a qualquer momento:


- **[Termos da Plataforma](https://developers.facebook.com/terms)**
- **[Políticas do Desenvolvedor](https://developers.facebook.com/devpolicy)**
- **[Políticas de Promoção](https://www.facebook.com/page_guidelines.php#promotionsguidelines)**
- **[Política de Uso de Dados](https://www.facebook.com/full_data_use_policy)**
- **[Declaração de Direitos e Responsabilidades](https://www.facebook.com/legal/terms)**
- **[Diretrizes de Publicidade](https://www.facebook.com/ad_guidelines.php)**


Prepare-se para responder rapidamente às mudanças. A maioria das alterações tem [controle de versões](https://developers.facebook.com/docs/reference/ads-api/versions), e as janelas de alteração são de 90 dias contínuos.


Na [Declaração de Direitos e Responsabilidades](https://www.facebook.com/legal/terms), você se responsabiliza financeiramente e operacionalmente pelo app, o conteúdo dele e seu uso da plataforma da Meta e da API de Anúncios. Você deverá gerenciar a estabilidade e os possíveis erros do app.
[○](https://developers.facebook.com/docs/marketing-api/best-practices#)[○](https://developers.facebook.com/docs/marketing-api/best-practices#)Nesta Página[Boas práticas](https://developers.facebook.com/docs/marketing-api/best-practices#boas-pr-ticas)[Alterações de anúncio acionando análises de anúncio](https://developers.facebook.com/docs/marketing-api/best-practices#altera--es-de-an-ncio-acionando-an-lises-de-an-ncio)[Paginação](https://developers.facebook.com/docs/marketing-api/best-practices#paging)[Informações do usuário](https://developers.facebook.com/docs/marketing-api/best-practices#informa--es-do-usu-rio)[Lances sugeridos](https://developers.facebook.com/docs/marketing-api/best-practices#lances-sugeridos)[Solicitações em lote](https://developers.facebook.com/docs/marketing-api/best-practices#solicita--es-em-lote)[Verificar alterações de dados com ETags](https://developers.facebook.com/docs/marketing-api/best-practices#verificar-altera--es-de-dados-com-etags)[Status de arquivado e excluído do objeto](https://developers.facebook.com/docs/marketing-api/best-practices#status-de-arquivado-e-exclu-do-do-objeto)[Visualizar erros](https://developers.facebook.com/docs/marketing-api/best-practices#visualizar-erros)[Grupo da comunidade de desenvolvedores de marketing do Facebook](https://developers.facebook.com/docs/marketing-api/best-practices#grupo-da-comunidade-de-desenvolvedores-de-marketing-do-facebook)[Teste](https://developers.facebook.com/docs/marketing-api/best-practices#testing)[Critérios básicos](https://developers.facebook.com/docs/marketing-api/best-practices#criteria)[Políticas](https://developers.facebook.com/docs/marketing-api/best-practices#policies) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NOntu9mUuPS-I0FTACpvXz9y_8jzsH90fWzkDwNxWc59CY3FVA2fP39rk-A_aem_aH7Pdwx_r509qDs-FsaoFg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58wbLMJeQiiVMQloQPxR0fpGuaBjt7yWjieSebRbVYaf3rad1KiJ6r50DBUQ_aem_VnVDICqmHdUTmODij0eJrA&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6KKCdK7Hw8DyExSVmyuZRQqBGxSl9POadc7aCyE55ae95iGUWE7rCdfwr0mA_aem_oFwinAGEXnBQoZ5T-JiA2g&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NOntu9mUuPS-I0FTACpvXz9y_8jzsH90fWzkDwNxWc59CY3FVA2fP39rk-A_aem_aH7Pdwx_r509qDs-FsaoFg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5QVekKJx3xEsqmeYvxahKA5ak6FkEgBExR5MI2AptJCtfqaXXt938-VrS1lQ_aem_v3idwYTXZFCLVmBkrteDgg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6FuNNC5wKtsMvgFRWJbR-UgFyt-pCRsy_roQpmRaJuK_g3TTKMyu2TOrxqxA_aem_-oVodkFdx6puRA7OxY_O0A&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5QVekKJx3xEsqmeYvxahKA5ak6FkEgBExR5MI2AptJCtfqaXXt938-VrS1lQ_aem_v3idwYTXZFCLVmBkrteDgg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR41vgZJjJSYOx5MmTQWqd-EY75yTo7LlCFxjtgmFhHCxeTDFq0_bY1lnZK61g_aem_8VMwXsvtuVNLxprQfWcpZA&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NOntu9mUuPS-I0FTACpvXz9y_8jzsH90fWzkDwNxWc59CY3FVA2fP39rk-A_aem_aH7Pdwx_r509qDs-FsaoFg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5oiZEZuMe_Li8oocQ2gR56P0uhdmkLYy8_80VoC8Jq60n_g4bBYHaajmY1EA_aem_Jbipd6p3-2kn54yCtRWYDA&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR53aAtojneyeGsCDuoRQoRSiZWXA0SUIOnTgP0NfymFBtql4zMKpAwo646CUQ_aem_V_F7VQlx2wrutuxjO_ZEnQ&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR58wbLMJeQiiVMQloQPxR0fpGuaBjt7yWjieSebRbVYaf3rad1KiJ6r50DBUQ_aem_VnVDICqmHdUTmODij0eJrA&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6VEvZLCiDXOyjNIIl_ui6hjIy4-jTZ1tbqYw3bjwYSlSrafCLPjrN1nhI67A_aem_jyOR5iUGEEFlPNRlx_FJpg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4KNXAuU-CHZDdB2bs-6aEaLmwxZ3XnRxybA_DufNSCxpZ0cEFCKL9p7BOgHw_aem_yRPUhd5xvJdUrygRQnoi5g&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR41vgZJjJSYOx5MmTQWqd-EY75yTo7LlCFxjtgmFhHCxeTDFq0_bY1lnZK61g_aem_8VMwXsvtuVNLxprQfWcpZA&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5QVekKJx3xEsqmeYvxahKA5ak6FkEgBExR5MI2AptJCtfqaXXt938-VrS1lQ_aem_v3idwYTXZFCLVmBkrteDgg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR7NOntu9mUuPS-I0FTACpvXz9y_8jzsH90fWzkDwNxWc59CY3FVA2fP39rk-A_aem_aH7Pdwx_r509qDs-FsaoFg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5QVekKJx3xEsqmeYvxahKA5ak6FkEgBExR5MI2AptJCtfqaXXt938-VrS1lQ_aem_v3idwYTXZFCLVmBkrteDgg&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6FuNNC5wKtsMvgFRWJbR-UgFyt-pCRsy_roQpmRaJuK_g3TTKMyu2TOrxqxA_aem_-oVodkFdx6puRA7OxY_O0A&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6KKCdK7Hw8DyExSVmyuZRQqBGxSl9POadc7aCyE55ae95iGUWE7rCdfwr0mA_aem_oFwinAGEXnBQoZ5T-JiA2g&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5YUgUjE0hUuLfezs8Azyek3BLXJY0XJTgOC16te0-exMscIs47TIak9L7c2a-SgylKimE14kwNzCRt00Ot3aggWPVHE03t3zknpO3_mkdwq6VeR5ilxHseOgVvVDtY1z5V3wvR0ttGphHlWvQ0HSwgbFE)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão