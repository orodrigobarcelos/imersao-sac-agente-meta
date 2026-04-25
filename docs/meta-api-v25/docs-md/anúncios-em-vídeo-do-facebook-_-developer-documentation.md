<!-- Fonte: Anúncios em vídeo do Facebook _ Developer Documentation.html -->
<!-- URL: https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads/fbvideoads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios em vídeo do Facebook

Updated: Dec 17, 2025

## Pré-requisitos

Para publicar um vídeo em uma conta do mercado de anúncios, é preciso ter um [token de acesso](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens) e as [permissões](https://developers.facebook.com/docs/permissions/reference) apropriados. Durante os testes, você pode facilmente gerar tokens e conceder permissões ao seu app usando o Explorador da Graph API. Para saber mais, consulte nosso guia [Introdução](https://developers.facebook.com/docs/video-api/getting-started).Quando seu app estiver pronto para produção, implemente o [Login do Facebook](https://developers.facebook.com/documentation/facebook-login) para obter tokens e permissões dos usuários. Para usar este guia, você precisa ter implementado os componentes necessários e seguido com sucesso o guia de introdução.Quando um usuário puder executar tarefas em uma conta de anúncios, implemente o Login do Facebook para solicitar as seguintes permissões e receber o token de acesso apropriado:

- `ads_read`
- `ads_management`
Aqueles que utilizarem um usuário do sistema empresarial nas solicitações de API deverão estar cientes de que ainda não há compatibilidade com o carregamento de vídeos em contas comerciais.O usuário do app deve conseguir executar a tarefa `CREATE_CONTENT` na conta de anúncios nas solicitações de API.

### Boas práticas


Ao testar uma chamada de API, você pode incluir o parâmetro `access_token` definido como seu token de acesso. No entanto, ao fazer chamadas seguras do seu app, use a classe de [token de acesso.](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#portabletokens)

## Carregar anúncios em vídeo

A publicação de anúncios em vídeo envolve o protocolo "retomável" (não fragmentado).Apenas o carregamento de vídeos para contas de anúncios é compatível. Ainda não há compatibilidade com o carregamento de vídeos em contas comerciais.

| Etapa | API |
| --- | --- |
| Inicializar | /act_\<PAYMENT_ACCOUNT_ID\>/video_ads?upload_phase=start |
| Fazer upload | rupload.facebook.com/video-ads-upload/v25.0/\<VIDEO_ID\> |
| Status | /\<VIDEO_ID\>?fields=status |
| Publicar | /act_\<PAYMENT_ACCOUNT_ID\>/video_ads?upload_phase=finish |


### Especificações de vídeo


| Propriedade | Especificação |
| --- | --- |
| Tipo de arquivo | MP4 (recomendado) |
| Taxa de proporção | 16:9 (paisagem) a 9:16 (retrato) |
| Tamanho máximo do arquivo | O recomendado é até 10 GB. Para arquivos maiores, o processamento e o carregamento poderão ser mais demorados. |
| Largura mínima | 1.200 pixels |
| Resolução | 1280 x 720 (recomendado) |
| Taxa de quadros | 24 a 60 quadros por segundo |
| Configurações de vídeo | Chroma subsampling de 4:2:0 GOP fechado (2 a 5 segundos) Compressão: H.264, H.265 (VP9, AV1 também são compatíveis) Taxa de quadros fixa Verificação progressiva |
| Configurações de áudio | Taxa de bits do áudio: mais de 128 kbps Canais: estéreo Codec: AAC (baixa complexidade) Taxa de amostragem: 48 kHz |


## Etapa 1: iniciar a sessão de carregamento

Para iniciar uma sessão de carregamento de vídeo, envie uma solicitação `POST` ao ponto de extremidade `/act_<PAYMENT_ACCOUNT_ID>/video_ads` com o parâmetro `upload_phase` definido como `start`.

#### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \
  -F "upload_phase=start" \
  -F "access_token=<ACCESS_TOKEN>"
```
Se a solicitação for bem-sucedida, o app receberá uma resposta JSON com o ID do vídeo e o URL do Facebook para carregamento. O ID do vídeo será usado nas etapas subsequentes.

#### Exemplo de resposta


```
{
  "video_id": "<VIDEO_ID>",
  "upload_url": "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>",
}
```


## Etapa 2: carregar um vídeo

O vídeo a ser carregado pode ser um arquivo local no seu dispositivo ou um URL. Se quiser usar um URL, ele deverá ser hospedado em um servidor http/https público, como uma CDN.

### Carregar um arquivo local

Para carregar um arquivo local, envie uma solicitação `POST` ao ponto de extremidade `upload_url` que você recebeu na etapa 1 com os seguintes parâmetros:

- `offset` definido como `0`.
- `file_size` definido como o tamanho total em bytes do vídeo que está sendo carregado.


#### Exemplo de solicitação


```
curl -X POST "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>" \
  -H "Authorization: OAuth <ACCESS_TOKEN>" \
  -H "offset: 0" \
  -H "file_size: 73400320" \
  --data-binary "@/path/to/file/my_video_file.mp4"
```
Se a solicitação for bem-sucedida, o app receberá uma resposta JSON com o ID do vídeo e o URL do Facebook para carregamento. O ID do vídeo será usado nas etapas subsequentes.

#### Exemplo de resposta


```
{    "success": true}
```


#### Cabeçalhos


| Nome | Descrição |
| --- | --- |
| authorization | Deve conter OAuth {access-token} . |
| offset | O deslocamento em bytes do primeiro byte que está sendo carregado na solicitação. Geralmente, deve ser definido como "0", a menos que seja necessário retomar um carregamento interrompido. Ao retomar um carregamento interrompido, defina o offset retornado por "/status". |
| file_size | O tamanho total em bytes do vídeo que está sendo carregado. |
| file_url | O URL do vídeo hospedado publicamente. Os protocolos compatíveis são http e https. No momento, não há compatibilidade com outros protocolos nem URLs que exigem autenticação. |


#### Retomar um carregamento interrompido

Para retomar o carregamento interrompido de um vídeo, é possível repetir a solicitação `POST` com `offset` definido como o valor `bytes_transfered` usando um ponto de extremidade `GET``/status`. Você também pode reiniciar o carregamento definindo o deslocamento como `0`. Para fazer isso, primeiro recupere o deslocamento em bytes do carregamento usando o ponto de extremidade de status. Depois, carregue os bytes restantes com o URL de carregamento.O cabeçalho `offset` deve ser definido como o valor `offset/bytes_transferred` recebido do ponto de extremidade de status ou como `0` para reiniciar o carregamento. Os bytes do arquivo enviado na solicitação subsequente devem começar com o byte em "offset" (base zero).

#### Carregar arquivos hospedados

Este método pode ser usado quando o vídeo a ser carregado está hospedado em um servidor http/https público, como uma CDN.

#### Exemplo de solicitação


```
curl -X POST "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>" \
  -H "Authorization: OAuth <ACCESS_TOKEN>" \
  -H "file_url: https://some.cdn.url/video.mp4"
```


## Etapa 3: recuperar o status da sessão de carregamento (opcional)

Você pode recuperar o status de uma operação de publicação enviando uma solicitação `GET` ao campo `status` no vídeo.

- Host: `graph.facebook.com`
- Ponto de extremidade: `/v25.0/<VIDEO_ID>?fields=status`


### Resposta

A resposta será um objeto JSON que inclui um campo de status. O campo de status terá os seguintes campos aninhados:

| Nome | Descrição |
| --- | --- |
| video_status | O status geral do carregamento e do processamento. |
| uploading_phase | Esta estrutura contém informações sobre o progresso na fase de carregamento. O campo bytes_transferred pode ser usado com o ponto de extremidade de carregamento para retomar um processo interrompido. |
| processing_phase | Esta estrutura contém informações sobre o progresso na fase de processamento. A fase envolve a geração de codificações de mídias alternativas, miniaturas e outros ativos necessários para publicação. |
| publishing_phase | Esta estrutura contém informações sobre o progresso na fase de publicação. A fase envolve adicionar o vídeo à conta de anúncios. |


#### Exemplo de solicitação


```
curl -X GET "https://graph.facebook.com/v25.0/<VIDEO_ID>" \
  -H "Authorization: OAuth <ACCESS_TOKEN" \
  -d "fields=status"
```


#### Exemplo de resposta


```
{  "status": {    "video_status": "processing", // ready, processing, expired, error    "uploading_phase": {      "status": "in_progress", // not_started, in_progress, complete, error      "bytes_transfered": 50002  // bytes received (also 'offset')    },    "processing_phase": {      "status": "not_started"    }    "publishing_phase": {      "status": "not_started",      "publish_status": "publish",      "publish_time": 234523452 // publish time (unix)    }  }}
```


## Etapa 4: publicar um vídeo na conta de anúncios

Quando você finalizar a sessão de carregamento, codificaremos o vídeo e o publicaremos na conta de anúncios. Para encerrar a sessão de carregamento e publicar o vídeo, envie uma solicitação `POST` ao ponto de extremidade `video_ads` no nó correspondente da conta de anúncios.

- Host: `graph.facebook.com`
- Ponto de extremidade: `/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads`
A resposta será um objeto JSON que indica se a solicitação foi bem-sucedida.

| Campo | Obrigatório. | Comentários |
| --- | --- | --- |
| video_id | yes | Valores: {video-id} (conforme retornado na etapa "Iniciar") |
| upload_phase | yes | Valores: finish |


#### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/video-ads-upload/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \
  -F "upload_phase=finish" \
  -F 'video_id=<VIDEO_ID>' \
  -F "access_token=<ACCESS_TOKEN>"
```


#### Exemplo de resposta


```
{  "success": true,}
```


## Obter anúncios em vídeo

Para obter uma lista de todos os vídeos de uma conta de anúncios, envie uma solicitação `GET` ao ponto de extremidade `/act_<PAYMENT_ACCOUNT_ID>/video_ads`, em que `PAYMENT_ACCOUNT_ID ` é identificação da conta de pagamento que você quer visualizar.

#### Exemplo de solicitação


```
curl -X GET "https://graph.facebook.com/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \
  -F "access_token=<ACCESS_TOKEN>"
```


#### Exemplo de resposta


```
{  "data": [    {      "updated_time": "unix_timestamp",      "id": "video_id",    }  ]}
```


### Filtros (opcional)


| Nome | Descrição |
| --- | --- |
| since | Data/hora de início para consultar reels com um registro de data e hora específico. Formatos permitidos: Registros de data e hora de época, como 1676057525 . Datas, como dd mmm yyyy (10 jan 2023) , yyyy-mm-dd (2023-01-10) e dd-mmm-yyyy (10-jan-2023) . Palavras, como today , yesterday e assim por diante. |
| until | Data/hora de término para consultar reels com um registro de data e hora específico. Formatos permitidos: Registros de data e hora de época, como 1676057525 . Datas, como dd mmm yyyy (10 jan 2023) , yyyy-mm-dd (2023-01-10) e dd-mmm-yyyy (10-jan-2023) . Palavras, como today , yesterday e assim por diante. |

Did you find this page helpful?ON THIS PAGEPré-requisitosBoas práticasCarregar anúncios em vídeoEspecificações de vídeoEtapa 1: iniciar a sessão de carregamentoExemplo de solicitaçãoExemplo de respostaEtapa 2: carregar um vídeoCarregar um arquivo localExemplo de solicitaçãoExemplo de respostaCabeçalhosRetomar um carregamento interrompidoCarregar arquivos hospedadosExemplo de solicitaçãoEtapa 3: recuperar o status da sessão de carregamento (opcional)RespostaExemplo de solicitaçãoExemplo de respostaEtapa 4: publicar um vídeo na conta de anúnciosExemplo de solicitaçãoExemplo de respostaObter anúncios em vídeoExemplo de solicitaçãoExemplo de respostaFiltros (opcional)$$Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7DxDNGNP_kPqh8qDwDShz34GPaEajJdILcv-Qe70dUbGRbjzrlQFCcTcbd0w_aem_7XrmYQOiKzHfg04YAcxpTQ&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4oKdcrf2eFB4y7RAUGKE_MZF4X-xvB0v1ogYiRHejsKH7XIgy-sb0T4IPGIg_aem_0ohoIK46bpxJhrpPCvu21w&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4MMfKvF3odzMAF0f_3GIfikJ6vWXsAikVjvphiS3ULX4M86mMPUZIuhfxniA_aem_T1Q2JwJlLWaQl0P56NqTQw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4lIvfXL9VVtot-YQnUf_A8EnC6Q-P-OgX8hIgnqhLKc-crNBj6HEfLUTTafg_aem_QnSmCiYjr-PVRlhvsMlfrA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR6tbc1z7VZOs-4a-vsSj2VPkGn9yfdU3sjPJhqm8d2fAVW6-VYmh_rgK2maNA_aem_xPEkZSWDNeW5uEyaFmSQRg&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4WvxHgqzHac7S5cIoM2nFlCM4Bhp7M_He5gDNUqmRVuq6n6WtN52qIctqgEg_aem_4Qabpg1iZcLCTPVnEstNRw&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7slo6xf-1sF006L6mRfzGsMa9LWnk6nSjk1rdjfuhGbBUiYYURpo_8gX-mlA_aem_6CigqZTvfN91ojvCp3sAZA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR438CwgrohlEFtZyOscZEl-Bgv6s16drVfLGVaTFmcKy2EIqGw3i9YjbSAK6w_aem_9nvxYd0XC6c7qh20yLy6-A&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExR2dOUzRCUkZHNkJrRWtyeXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR5smhevpPXCItu9x5ziJhxNzHA8a5Oak9w41VL_6z3dv_Jx19Iv3IyyYAFx1w_aem_756qEHuNj-VX47JBBqs8fA&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4W3b-X7xVL--_jgPCPwc6VCLnh2VkUnyd8XUz71DzwCFhJgr5ArJETG2-ztEDn3FD8n3EO2sBnflv9w1tf3Cl5Ng9BDMIfa--k9yoM30z5a_CXCx4rBjzL45jR-jWWY7uwXjvkC9I)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)/$/$/$/$/$/$/$/$