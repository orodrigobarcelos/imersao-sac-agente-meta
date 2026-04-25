<!-- Fonte: Teste e solução de problemas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Teste e solução de problemas


Use esta API para criar e excluir leads de teste.


## Como usar a ferramenta de teste


Use [esta ferramenta](https://developers.facebook.com/tools/lead-ads-testing) para criar e excluir leads de teste dos seus formulários. **No entanto, não é possível usar a ferramenta no modo de desenvolvimento**.


Você pode criar um lead de teste por formulário. É preciso excluir um lead existente para criar um novo.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)

## Depurar a integração da atualização em tempo real


Use esta ferramenta para testar se a integração com os Webhooks do Facebook foi bem-sucedida. Consulte as etapas a seguir se quiser usar a ferramenta para depurar a integração.


Os leads criados com a ferramenta são orgânicos, sem associação a anúncios. É possível criar somente um lead por formulário. Por isso, se quiser recriar um lead no mesmo formulário, clique em **Excluir lead** primeiro e, depois, crie-o novamente.


- Acesse a [**ferramenta de teste**](https://developers.facebook.com/tools/lead-ads-testing).
 O menu suspenso lista todas as páginas a que você tem acesso de anunciante.


- Selecione uma página no menu suspenso.

- Em **Formulário**, selecione a opção que será usada para criar um lead.

- Clique em **Criar lead** para iniciar o processo de criação. Por padrão, o lead criado contém dados fictícios.

- Clique em **Ver prévia do Formulário** para personalizar os dados enviados.

- Digite os dados desejados no nível do formulário para criar um lead com o conteúdo personalizado.

- Depois de criar o lead, você verá o botão **Acompanhar status**.

- Clique em **Acompanhar status** para ver o status dos leads. Demora alguns segundos para a atualização em tempo real ser disparada no seu ponto de extremidade. Enquanto isso, você verá a atualização com status **pendente**. Clique em **Acompanhar status** até você ver a mudança.



    Ao enviar o lead para seu ponto de extremidade, o campo de status será alterado. Se a atualização em tempo real for disparada, o status será definido como **sucesso**.

 Nesse caso, você também verá a carga na tabela. A carga apresentada é uma cópia do que o Facebook envia ao ponto de extremidade; portanto, você deve visualizar o conteúdo e gerenciar o JSON. Se houver problemas durante o envio da atualização, o status será alterado para **falha**. Nesse caso, a coluna error_code exibirá informações sobre o motivo da falha.


### Teste de lead


Depois de [configurar webhooks para seu app](https://developers.facebook.com/docs/graph-api/webhooks/getting-started), é possível testar os leads usando o botão Testar. O botão aparece no painel de webhooks do app.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)

## Criar leads de teste


Para criar leads de teste, envie uma solicitação `POST` a `/{FORM_ID}/test_leads`.


Para que a solicitação seja bem-sucedida, é necessário atender aos seguintes requisitos:


- Não devem existir outros leads de teste para o formulário de anúncio de lead.
- Você deve ter a [função](https://developers.facebook.com/docs/graph-api/reference/page/roles/) de `Advertiser` ou superior na página de criação do formulário.
- Use o token de acesso à Página na chamada de API.

```
curl \
  -F "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/API_VERSION/FORM_ID/test_leads"
```


É possível personalizar o conteúdo do lead ao passar os seguintes parâmetros:


- `field_data`: um parâmetro de vetor com pares de `name` e `values`.
- `custom_disclaimer_responses`: um parâmetro de vetor com pares de `checkbox_key` e `is_checked`.

```
curl \
  -F "field_data=[{'name': 'favorite_color?', 'values': ['yellow']}, {'name': 'email', 'values': ['test@test.com']}]" \
  -F "custom_disclaimer_responses=[{'checkbox_key': 'my_checkbox', 'is_checked': true}]" \
  -F "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/API_VERSION/FORM_ID/test_leads"
```


Os leads criados a partir das chamadas acima são fictícios e, portanto, não estão associados a nenhum anúncio.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)

## Ler leads de teste


É possível ler os leads de teste associados ao formulário de anúncios de lead fazendo uma chamada `GET` para o ponto de extremidade `{FORM_ID}/test_leads`.

```
curl \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/API_VERSION/FORM_ID/test_leads"
```
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)

## Excluir leads de teste


Se você quiser excluir e reenviar um lead durante o teste da sua integração, faça a seguinte chamada de API:

```
curl -X DELETE \
  -d "access_token=<ACCESS_TOKEN>" \
  "https://graph.facebook.com/<API_VERSION>/<LEAD_ID>"
```


Vale lembrar que apenas o proprietário pode excluir um lead.
[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)[○](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#)Nesta Página[Teste e solução de problemas](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#teste-e-solu--o-de-problemas)[Como usar a ferramenta de teste](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#como-usar-a-ferramenta-de-teste)[Depurar a integração da atualização em tempo real](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#depurar-a-integra--o-da-atualiza--o-em-tempo-real)[Teste de lead](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#teste-de-lead)[Criar leads de teste](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#criar-leads-de-teste)[Ler leads de teste](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#ler-leads-de-teste)[Excluir leads de teste](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting#excluir-leads-de-teste) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7RuEeYCVnM907ov9wwg7mD9hoEb0QsR-oQxfaVBsKT0kixCyiFSVsUx9JXoA_aem_cIicT9cEjw0xAiTSndN9mg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6YJ-WYytOshcz6yovP3duU_7_0ea4ciCYGHTjIsvI9rFRt2tHmkMzIimbXcQ_aem_9zcs8NlRFO9IcKfX5CW53A&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZqQGYw8Mn_a3TgInhrO7JlkjyD1p6jU-tMGbPtht974ogeI2d3BcFyBtOjw_aem_Ssd6VbUJUfwrvUCwD0jOIg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68Lgfd2R6Mxthw--Gz0cuWKz4yzj5105WQ5_YRjGCkjVraTiwqw_2NsNrpVg_aem_vrbPu22QoUBn8qE7aPxnzA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6P1S9eKG6QxFaq8NPVcpuje20a6dnDEMvFZEObsS_IYEPkZYGwJgmiDcD2cw_aem_PnW9r2ELGHKQCdpsXio9aA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7RuEeYCVnM907ov9wwg7mD9hoEb0QsR-oQxfaVBsKT0kixCyiFSVsUx9JXoA_aem_cIicT9cEjw0xAiTSndN9mg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6P1S9eKG6QxFaq8NPVcpuje20a6dnDEMvFZEObsS_IYEPkZYGwJgmiDcD2cw_aem_PnW9r2ELGHKQCdpsXio9aA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7AqIy25mMmLTfHx-RTNLL7qMP31YnFQzgOxdPqpaCubFXwdlPYzSevzgM-0Q_aem_umG-WjOBbtWSGl_NcMPUfw&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68Lgfd2R6Mxthw--Gz0cuWKz4yzj5105WQ5_YRjGCkjVraTiwqw_2NsNrpVg_aem_vrbPu22QoUBn8qE7aPxnzA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6YJ-WYytOshcz6yovP3duU_7_0ea4ciCYGHTjIsvI9rFRt2tHmkMzIimbXcQ_aem_9zcs8NlRFO9IcKfX5CW53A&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68Lgfd2R6Mxthw--Gz0cuWKz4yzj5105WQ5_YRjGCkjVraTiwqw_2NsNrpVg_aem_vrbPu22QoUBn8qE7aPxnzA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZqQGYw8Mn_a3TgInhrO7JlkjyD1p6jU-tMGbPtht974ogeI2d3BcFyBtOjw_aem_Ssd6VbUJUfwrvUCwD0jOIg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7LYQnzW9TisVdpA6ycA_y9csrIbU4Yoc1akdBGv2ajX186KkXZlqexBYNmYQ_aem_Rn1wEAr2UQfuKCMSaIJW7g&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6P1S9eKG6QxFaq8NPVcpuje20a6dnDEMvFZEObsS_IYEPkZYGwJgmiDcD2cw_aem_PnW9r2ELGHKQCdpsXio9aA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZqQGYw8Mn_a3TgInhrO7JlkjyD1p6jU-tMGbPtht974ogeI2d3BcFyBtOjw_aem_Ssd6VbUJUfwrvUCwD0jOIg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6YJ-WYytOshcz6yovP3duU_7_0ea4ciCYGHTjIsvI9rFRt2tHmkMzIimbXcQ_aem_9zcs8NlRFO9IcKfX5CW53A&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7RuEeYCVnM907ov9wwg7mD9hoEb0QsR-oQxfaVBsKT0kixCyiFSVsUx9JXoA_aem_cIicT9cEjw0xAiTSndN9mg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68Lgfd2R6Mxthw--Gz0cuWKz4yzj5105WQ5_YRjGCkjVraTiwqw_2NsNrpVg_aem_vrbPu22QoUBn8qE7aPxnzA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ZqQGYw8Mn_a3TgInhrO7JlkjyD1p6jU-tMGbPtht974ogeI2d3BcFyBtOjw_aem_Ssd6VbUJUfwrvUCwD0jOIg&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR68Lgfd2R6Mxthw--Gz0cuWKz4yzj5105WQ5_YRjGCkjVraTiwqw_2NsNrpVg_aem_vrbPu22QoUBn8qE7aPxnzA&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4_QxvDbn3xgXtJaQtihxvtP6M-aM4Ui68KwMcO3-1UV333H_zfV-F4MZ5G5d-BfLoDQHI6MKBLF1sqVM8ZqFJTfak3BojA-s1H-r_q9KnpgrrHs-xmfDGIKXFs1jjpenev5iaWRAoWsQ2MOuHtpPMj0Ok)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão