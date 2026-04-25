<!-- Fonte: Perguntas frequentes - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Perguntas frequentes sobre Anúncios de Catálogo Advantage+


A solução [Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/) permite que você promova automaticamente produtos relevantes de um catálogo inteiro em todos os dispositivos usando eventos de app e de pixel para criar públicos de pessoas a serem alcançados. Este documento apresenta as perguntas frequentes sobre Anúncios de Catálogo Advantage+.


## Catálogo de produtos e feed de produtos


#### Q: What are the current product limits on catalog size?



**A:** We recommend breaking larger feeds into smaller ones for faster, parallel upload:


- We currently recommend under 5 million products per feed through the file upload method.
- Limit of 100 MB per feed file via Business Manager.


#### Q: What file formats do you accept?



- File formats accepted are XML and tab delimited CSV, TXT or TSV. [Learn more](https://developers.facebook.com/docs/marketing-api/catalog-setup/catalog-feed-setup#feed-format)
- We also accept files that are compressed: zip, gzip and bz2.


#### Q: My feed is taking too long to upload



- Ensure that there are no network connectivity issues.
- Ensure that your product feed follows the restrictions specified above. [Learn more](https://developers.facebook.com/docs/marketing-api/catalog-setup/catalog-feed-setup#da-commerce)
- To speed up feed upload process, use a compressed feed file. We support zip, gzip and bz2 compression formats.


#### Q: How do I get Google Merchant Center feed to dynamic ads?



- Google Merchant Center feeds can be uploaded directly for dynamic ads.
- Go to the "link" column to make sure it doesn't have Google tracking parameters on it. The parameters may look like this: `URL?utm_campaign=GoogleDynRMKT&utm_medium=display`.


**Note**: To reuse a data feed file from another inventory platform, such as Google or Amazon, Facebook's requirements may be different. Check that your data feed is a CSV, TSV, or XML (RSS/ATOM) file, and has the required columns in our specifications. [Learn more](https://developers.facebook.com/docs/marketing-api/catalog-setup/catalog-feed-setup)


#### Q: How do I troubleshoot my feed upload errors?



- Verify the [upload errors](https://developers.facebook.com/docs/marketing-api/reference/product-feed-upload/errors/). Products with fatal errors are not uploaded; the rest are uploaded.
- Verify the `product_count` in the product catalog after the feed upload has finished. Instructions [here](https://developers.facebook.com/docs/marketing-api/reference/product-catalog#Reading)
- The first line in the field is expected to contain the name of the fields.
- Use the correct delimiter in your feed file. Supported delimiters are TAB (default), PIPE, or TILDE. Ensure the delimiter you use during the upload is the same delimiter as in the feed file.
- Check the **Use quoted fields** option if your feed contains quoted fields.


#### Q: How do I stop a product from running when it is out of stock?



**A:** When products go out of stock, you need to mark it as "out of stock" in your product catalog. Products marked "out of stock" automatically stop serving. Scheduling and fetching the product catalog frequently helps you maintain your stock information easily. See the `availability` field in [Supported Fields](https://developers.facebook.com/docs/marketing-api/catalog-setup/catalog-feed-setup#da-commerce).


#### Q: I'm unable to choose or see a product catalog that my team uploaded.



**A:** Go to **Business Manager** and make sure the user/account has **Product Catalog Admin** permissions.
 [○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)

## Conjunto de produtos e grupo de produtos


#### Q: What's the difference between *product set* and *product group*?



**A:** A *product set* is a collection of product items and product groups within a product catalog defined by a name and a filter or rule that's evaluated dynamically. For example, someone can create a product set with "all things where the brand is Nike and the price is greater than USD 50".


A *product group* describes a collection of variants of a product item. For example, a black iPhone 6 16 GB has the same product group as a white iPhone 6 16 GB, but they have different product items. A product item can have zero (0) or one (1) product group (product groups are optional).


#### Q: Can a product appear in multiple product sets?



**A:** Yes, a product can appear in multiple product sets.


#### Q: Is the exclusion for `Purchase` events done at the product group level or product set level?



**A:** The exclusion for `Purchase` events is done at the product group level if it is available; otherwise, at the product level.
 [○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)

## Configuração e públicos do Pixel da Meta


#### P: Meu pixel não está configurado corretamente.


**R:** Para usar o Pixel da Meta para rastrear eventos externos nas suas páginas de produto e criar um [público para o produto](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-audiences/):


- Coloque um dos [eventos padrão](https://developers.facebook.com/docs/marketing-api/facebook-pixel#standardevents) em páginas selecionadas do seu site com parâmetros padrão.
- Verifique se o pixel está associado corretamente ao seu catálogo de produtos. Veja mais informações [aqui](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-audiences/v2.5#associate).


#### P: Como posso associar o Pixel da Meta ao meu catálogo de produtos?


**R:** Os Anúncios de Catálogo Advantage+ exigem que o Pixel da Meta ou os Eventos do App informem quais produtos estão sendo visualizados, adicionados ao carrinho e comprados no seu site ou app. O ID do produto informado pelo Pixel da Meta (ou pelos eventos do app) deve coincidir EXATAMENTE com a coluna de ID correspondente no seu feed de produtos.


#### P: Quais são os valores permitidos para `content_type` ao configurar o pixel?


**R:** Os valores válidos para `content_type` são `product` ou `product_group`. É importante que o `content_type` corresponda ao tipo de ID incluído no parâmetro `content_ids`. Por exemplo, se `content_type` for `product_group`, os IDs de grupo de produtos devem ser fornecidos em `content_ids`.


#### P: Por que o tamanho do meu público é zero?


**R:** Pode haver alguns motivos pelos quais o tamanho do seu público é zero (0). Para garantir que o público esteja configurado corretamente, siga [estas instruções](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/product-audiences/) e estas diretrizes:


- Certifique-se de que as regras de inclusão e exclusão não entrem em conflito.
- Certifique-se de que o ID do conjunto de produtos pertença ao catálogo de produtos para o qual o Pixel da Meta foi criado.
- Sites com pouco tráfego devem tentar manter a retenção alta para captar público. Os anúncios não serão exibidos se o tamanho do público for inferior a 20.
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)

## Gerenciamento de anúncios


#### P: Qual objetivo preciso configurar para campanhas de Anúncios de Catálogo Advantage+?


**R:** Recomendamos usar o objetivo `PRODUCT_CATALOG_SALES` para campanhas de Anúncios de Catálogo Advantage+.


#### P: Como faço para promover produtos em um determinado conjunto de anúncios?


**R:** Ao criar um conjunto de anúncios, use o campo `promoted_object` para adicionar um ID de conjunto de produtos, que indica que todos os anúncios no conjunto de anúncios promoverão produtos no conjunto de produtos especificado.


#### P: Existe alguma ferramenta que possa ajudar na depuração?


- Instale a [Ferramenta para Pixel da Meta](https://developers.facebook.com/docs/facebook-pixel/pixel-helper). Essa ferramenta pode ajudar você a identificar rapidamente problemas com um pixel que não funciona.
- [Ferramentas de depuração dos Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/debugging-tools/) descreve as ferramentas para depurar problemas com Anúncios de Catálogo Advantage+.
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)

## Saiba mais


- [Sobre os catálogos – Central de Ajuda da Meta para Empresas](https://www.facebook.com/business/help/890714097648074)
- [Sobre os Anúncios de Catálogo Advantage+ da Meta – Central de Ajuda da Meta para Empresas](https://www.facebook.com/business/help/397103717129942)
- [Criar um anúncio de catálogo Advantage+ – Central de Ajuda da Meta para Empresas](https://www.facebook.com/business/help/1132465490107046)
- [Catálogo – Marketing API](https://developers.facebook.com/docs/marketing-api/catalog-setup)
[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)[○](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#)Nesta Página[Perguntas frequentes sobre Anúncios de Catálogo Advantage+](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#perguntas-frequentes-sobre-an-ncios-de-cat-logo-advantage-)[Catálogo de produtos e feed de produtos](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#cat-logo-de-produtos-e-feed-de-produtos)[Conjunto de produtos e grupo de produtos](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#conjunto-de-produtos-e-grupo-de-produtos)[Configuração e públicos do Pixel da Meta](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#configura--o-e-p-blicos-do-pixel-da-meta)[Gerenciamento de anúncios](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#gerenciamento-de-an-ncios)[Saiba mais](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/faq#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4R4nOMoZAoX5KP4Nemag5zEBs5DZG88VreatIS5po1PQVOZVTaTb5n34hebw_aem_m8NaF_F9vLwQMDnRCKUOTQ&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7bnLatJ7-8Sx8AOFCD0S4uuIwvt0qqIYCqrnL6jC8C2c709F5rGO0xBMZ5TQ_aem_NeC8u9ecmDh8mPBjrsgqNA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7STFHgkFfm9THc04997SD_vNwSmmK7Gx5UzPw7CyQr8fdx4jzCYQvTgjbjEA_aem_8j6RSrAb85CP4sp6FzWuxw&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4R4nOMoZAoX5KP4Nemag5zEBs5DZG88VreatIS5po1PQVOZVTaTb5n34hebw_aem_m8NaF_F9vLwQMDnRCKUOTQ&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dkYHFJJD18f8w7Fc_adaLgeu8zb_S8moLH0rM5oeMQxHjj36yiB4ucL76iw_aem_snFsFl8s8TGwnhRD3CZfFA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6onJ5s1uBEE84C-b37oPIKByPN59glkWM9R_dBRS2x04TvGyjRVnWVTGPNcg_aem_o2YyyZlbLxf1aY0j5PJLZg&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7STFHgkFfm9THc04997SD_vNwSmmK7Gx5UzPw7CyQr8fdx4jzCYQvTgjbjEA_aem_8j6RSrAb85CP4sp6FzWuxw&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6s-DpSVdszYlR431ymsylJHvJMsWZKeg6cvChe4RxeJ1rHM_XLYONVqWqBww_aem_Hgq3P_GPxnFXZKnXgwko2Q&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR63iT7pS6Ja3V4YWo6BEUM1EycJFhOVnrc36KLb8IcxoE4V86eUfv64EfBNNg_aem_JDYPY2vf-0Wf_zYFC-dj-w&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4dkYHFJJD18f8w7Fc_adaLgeu8zb_S8moLH0rM5oeMQxHjj36yiB4ucL76iw_aem_snFsFl8s8TGwnhRD3CZfFA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6s-DpSVdszYlR431ymsylJHvJMsWZKeg6cvChe4RxeJ1rHM_XLYONVqWqBww_aem_Hgq3P_GPxnFXZKnXgwko2Q&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7bnLatJ7-8Sx8AOFCD0S4uuIwvt0qqIYCqrnL6jC8C2c709F5rGO0xBMZ5TQ_aem_NeC8u9ecmDh8mPBjrsgqNA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4R4nOMoZAoX5KP4Nemag5zEBs5DZG88VreatIS5po1PQVOZVTaTb5n34hebw_aem_m8NaF_F9vLwQMDnRCKUOTQ&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4R4nOMoZAoX5KP4Nemag5zEBs5DZG88VreatIS5po1PQVOZVTaTb5n34hebw_aem_m8NaF_F9vLwQMDnRCKUOTQ&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6NpCOieliilS18uw6chM26duTQ-GXjjAXEPJBQ7mQYTDwENZZ8xIW948V3Lw_aem_NB2zT1ppRunOucNtNNzrPA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR63iT7pS6Ja3V4YWo6BEUM1EycJFhOVnrc36KLb8IcxoE4V86eUfv64EfBNNg_aem_JDYPY2vf-0Wf_zYFC-dj-w&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR57yqt6aXbYyrXtmW6FAvPW3nUIYUX9IMQwKmje1bhehPlFTYVaWQnH4YdOfg_aem_G7fqqJceLJ6_YO5kqVZdAw&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR63iT7pS6Ja3V4YWo6BEUM1EycJFhOVnrc36KLb8IcxoE4V86eUfv64EfBNNg_aem_JDYPY2vf-0Wf_zYFC-dj-w&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6NpCOieliilS18uw6chM26duTQ-GXjjAXEPJBQ7mQYTDwENZZ8xIW948V3Lw_aem_NB2zT1ppRunOucNtNNzrPA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6NpCOieliilS18uw6chM26duTQ-GXjjAXEPJBQ7mQYTDwENZZ8xIW948V3Lw_aem_NB2zT1ppRunOucNtNNzrPA&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6yT9UoaMYs9lRjbiejToXlvS81VHDsn3jrN9cdpBp99gTx3nNXAB-jveVDPWsN7X3A3Xi-FrjSrVjFXXnv7M-QFf6M6aAYVQUpjcSww8yD5oQszqg9bmxGhFCDkbmtWBSqJ53KGJ2CZ36E8BWXrFseNBM)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão