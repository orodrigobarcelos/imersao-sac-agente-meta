<!-- Fonte: Anúncios em vídeo do Facebook - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Anúncios em vídeo do Facebook


## Pré-requisitos


Para publicar um vídeo em uma conta do mercado de anúncios, é preciso ter um [token de acesso](https://developers.facebook.com/docs/facebook-login/access-tokens) e as [permissões](https://developers.facebook.com/docs/permissions/reference) apropriados. Durante os testes, você pode facilmente gerar tokens e conceder permissões ao seu app usando o Explorador da Graph API. Para saber mais, consulte nosso guia [Introdução](https://developers.facebook.com/docs/video-api/getting-started).


Quando seu app estiver pronto para produção, implemente o [Login do Facebook](https://developers.facebook.com/docs/facebook-login) para obter tokens e permissões dos usuários. Para usar este guia, você precisa ter implementado os componentes necessários e seguido com sucesso o guia de introdução.


Quando um usuário puder executar tarefas em uma conta de anúncios, implemente o Login do Facebook para solicitar as seguintes permissões e receber o token de acesso apropriado:


- `ads_read`
- `ads_management`


Aqueles que utilizarem um usuário do sistema empresarial nas solicitações de API deverão estar cientes de que ainda não há compatibilidade com o carregamento de vídeos em contas comerciais.


O usuário do app deve conseguir executar a tarefa `CREATE_CONTENT` na conta de anúncios nas solicitações de API.


### Boas práticas


Ao testar uma chamada de API, você pode incluir o parâmetro `access_token` definido como seu token de acesso. No entanto, quando fizer chamadas seguras do seu app, use as [classes de token de acesso](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#portabletokens).


## Carregar anúncios em vídeo


A publicação de anúncios em vídeo envolve o protocolo "retomável" (não fragmentado).


Apenas o carregamento de vídeos para contas de anúncios é compatível. Ainda não há compatibilidade com o carregamento de vídeos em contas comerciais.


| Etapa | API |
| --- | --- |
| Inicializar | /act_\<PAYMENT_ACCOUNT_ID\>/video_ads?upload_phase=start |
| Fazer upload | rupload.facebook.com/video-ads-upload/ v25.0 /\<VIDEO_ID\> |
| Status | /\<VIDEO_ID\>?fields=status |
| Publicar | /act_\<PAYMENT_ACCOUNT_ID\>/video_ads?upload_phase=finish |


### Especificações de vídeo


| Propriedade | Especificação |
| --- | --- |
| Tipo de arquivo | MP4 (recomendado) |
| Taxa de proporção | 16:9 (paisagem) a 9:16 (retrato) |
| Tamanho máximo do arquivo | O recomendado é até 10 GB. Para arquivos maiores, o processamento e o carregamento poderão ser mais demorados. |
| Largura mínima | 1.200 pixels |
| Resolução | 1280x720 (recomendada) |
| Taxa de quadros | 24 a 60 quadros por segundo |
| Configurações de vídeo | Chroma subsampling de 4:2:0; GOP fechado (2 a 5 segundos); Compressão: H.264, H.265 (VP9, AV1 também são compatíveis); Taxa de quadros fixa; Verificação progressiva |
| Configurações de áudio | Taxa de bits do áudio: mais de 128 kbps; Canais: estéreo; Codec: AAC (baixa complexidade); Taxa de amostragem: 48 kHz |

[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)

## Etapa 1: iniciar a sessão de carregamento


Para iniciar uma sessão de carregamento de vídeo, envie uma solicitação `POST` ao ponto de extremidade `/act_<PAYMENT_ACCOUNT_ID>/video_ads` com o parâmetro `upload_phase` definido como `start`.


#### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \ -F "upload_phase=start" \ -F "access_token=<ACCESS_TOKEN>"
```


Se a solicitação for bem-sucedida, o app receberá uma resposta JSON com o ID do vídeo e o URL do Facebook para carregamento. O ID do vídeo será usado nas etapas subsequentes.


#### Exemplo de resposta


```
{ "video_id": "<VIDEO_ID>", "upload_url": "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>", }
```
[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)

## Etapa 2: carregar um vídeo


O vídeo a ser carregado pode ser um arquivo local no seu dispositivo ou um URL. Se quiser usar um URL, ele deverá ser hospedado em um servidor http/https público, como uma CDN.


### Carregar um arquivo local


Para carregar um arquivo local, envie uma solicitação `POST` ao ponto de extremidade `upload_url` que você recebeu na etapa 1 com os seguintes parâmetros:


- `offset` definido como `0`.
- `file_size` definido como o tamanho total em bytes do vídeo que está sendo carregado.


#### Exemplo de solicitação


```
curl -X POST "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>" \ -H "Authorization: OAuth <ACCESS_TOKEN>" \ -H "offset: 0" \ -H "file_size: 73400320" \ --data-binary "@/path/to/file/my_video_file.mp4"
```


Se a solicitação for bem-sucedida, o app receberá uma resposta JSON com o ID do vídeo e o URL do Facebook para carregamento. O ID do vídeo será usado nas etapas subsequentes.


#### Exemplo de resposta


```
{ "success": true }
```


#### Cabeçalhos


| Nome | Descrição |
| --- | --- |
| authorization | Deve conter OAuth {access-token} . |
| offset | O deslocamento em bytes do primeiro byte que está sendo carregado na solicitação. Geralmente, deve ser definido como "0", a menos que seja necessário retomar um carregamento interrompido. Ao retomar um carregamento interrompido, defina o offset retornado por "/status". |
| file_size | O tamanho total em bytes do vídeo que está sendo carregado. |
| file_url | O URL do vídeo hospedado publicamente. Os protocolos compatíveis são http e https. No momento, não há compatibilidade com outros protocolos nem URLs que exigem autenticação. |


#### Retomar um carregamento interrompido


Para retomar o carregamento interrompido de um vídeo, é possível repetir a solicitação `POST` com `offset` definido como o valor `bytes_transfered` usando um ponto de extremidade `GET``/status`. Você também pode reiniciar o carregamento definindo o deslocamento como `0`. Para fazer isso, primeiro recupere o deslocamento em bytes do carregamento usando o ponto de extremidade de status. Depois, carregue os bytes restantes com o URL de carregamento.


O cabeçalho `offset` deve ser definido como o valor `offset/bytes_transferred` recebido do ponto de extremidade de status ou como `0` para reiniciar o carregamento. Os bytes do arquivo enviado na solicitação subsequente devem começar com o byte em "offset" (base zero).


#### Carregar arquivos hospedados


Este método pode ser usado quando o vídeo a ser carregado está hospedado em um servidor http/https público, como uma CDN.


#### Exemplo de solicitação


```
curl -X POST "https://rupload.facebook.com/video-ads-upload/v25.0/<VIDEO_ID>" \ -H "Authorization: OAuth <ACCESS_TOKEN>" \ -H "file_url: https://some.cdn.url/video.mp4"
```
[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)

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
curl -X GET "https://graph.facebook.com/v25.0/<VIDEO_ID>" \ -H "Authorization: OAuth <ACCESS_TOKEN" \ -d "fields=status"
```


#### Exemplo de resposta


```
{ "status": { "video_status": "processing", // ready, processing, expired, error "uploading_phase": { "status": "in_progress", // not_started, in_progress, complete, error "bytes_transfered": 50002 // bytes received (also 'offset') }, "processing_phase": { "status": "not_started" } "publishing_phase": { "status": "not_started", "publish_status": "publish", "publish_time": 234523452 // publish time (unix) } } }
```
[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)

## Etapa 4: publicar um vídeo na conta de anúncios


Quando você finalizar a sessão de carregamento, codificaremos o vídeo e o publicaremos na conta de anúncios. Para encerrar a sessão de carregamento e publicar o vídeo, envie uma solicitação `POST` ao ponto de extremidade `video_ads` no nó correspondente da conta de anúncios.


- Host: `graph.facebook.com`
- Ponto de extremidade: `/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads`


A resposta será um objeto JSON que indica se a solicitação foi bem-sucedida.


| Campo | Obrigatório | Comentários |
| --- | --- | --- |
| video_id | yes | Valores: {video-id} (conforme retornado na etapa "Iniciar") |
| upload_phase | yes | Valores: finish |


#### Exemplo de solicitação


```
curl -X POST "https://graph.facebook.com/video-ads-upload/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \ -F "upload_phase=finish" \ -F 'video_id=<VIDEO_ID>' \ -F "access_token=<ACCESS_TOKEN>"
```


#### Exemplo de resposta


```
{ "success": true, }
```
[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)

## Obter anúncios em vídeo


Para obter uma lista de todos os vídeos de uma conta de anúncios, envie uma solicitação `GET` ao ponto de extremidade `/act_<PAYMENT_ACCOUNT_ID>/video_ads`, em que `PAYMENT_ACCOUNT_ID` é identificação da conta de pagamento que você quer visualizar.


#### Exemplo de solicitação


```
curl -X GET "https://graph.facebook.com/v25.0/act_<PAYMENT_ACCOUNT_ID>/video_ads" \ -F "access_token=<ACCESS_TOKEN>"
```


#### Exemplo de resposta


```
{ "data": [ { "updated_time": "unix_timestamp", "id": "video_id", } ] }
```


### Filtros (opcional)


| Nome | Descrição |
| --- | --- |
| since | Data/hora de início para consultar reels com um registro de data e hora específico. Formatos permitidos: Registros de data e hora de época, como 1676057525 .; Datas, como dd mmm yyyy (10 jan 2023) , yyyy-mm-dd (2023-01-10) e dd-mmm-yyyy (10-jan-2023) .; Palavras, como today , yesterday e assim por diante. |
| until | Data/hora de término para consultar reels com um registro de data e hora específico. Formatos permitidos: Registros de data e hora de época, como 1676057525 .; Datas, como dd mmm yyyy (10 jan 2023) , yyyy-mm-dd (2023-01-10) e dd-mmm-yyyy (10-jan-2023) .; Palavras, como today , yesterday e assim por diante. |

[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)[○](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#)Nesta Página[Anúncios em vídeo do Facebook](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#an-ncios-em-v-deo-do-facebook)[Pré-requisitos](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#pr--requisitos)[Boas práticas](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#boas-pr-ticas)[Carregar anúncios em vídeo](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#carregar-an-ncios-em-v-deo)[Especificações de vídeo](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#requirements)[Etapa 1: iniciar a sessão de carregamento](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#step-1-initialize-upload-session)[Etapa 2: carregar um vídeo](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#step-2-upload-video)[Carregar um arquivo local](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#carregar-um-arquivo-local)[Etapa 3: recuperar o status da sessão de carregamento (opcional)](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#step-3-retrieve-upload-session-status-optional)[Resposta](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#resposta)[Etapa 4: publicar um vídeo na conta de anúncios](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#step-4-publish-video-to-ad-account)[Obter anúncios em vídeo](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#obter-an-ncios-em-v-deo)[Filtros (opcional)](https://developers.facebook.com/docs/marketing-api/guides/videoads/fbvideoads#filtros--opcional-) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4pOdwmUIo5p_ruQZDvwZS4oIgvXkeilWJqaN99QRHepF3YYOWGHfXmGEOH5g_aem_21RaRioMyk4L3V-2SR09Nw&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yTkulJNAGwg5sK2O_GObQ7NfPht9LhOGtQlGE_XtrOBB4VPrlUW6wtSPu8w_aem_b261oIUUHLK7LVzt-Je51Q&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4pOdwmUIo5p_ruQZDvwZS4oIgvXkeilWJqaN99QRHepF3YYOWGHfXmGEOH5g_aem_21RaRioMyk4L3V-2SR09Nw&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4t1IG4N4zCM6vmYArAPd5ihnCopPXT8bmNUUgWkDvGH-s2O7ddteWYRi2e_Q_aem_TNYFN6AWCFirPNQpZqNBxA&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7OSXlvryURvV2XuFsBjfZBeNrqEFPX7yrkMEWMLlV2sNgrdA1Hopzcrnd-SA_aem_1hBXC4x-tUmwcUuw-4A31g&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR76uzBfm_yPvj8dqaFwnjuBAfu7PbqRsV5ctvVmvG4iAIJplM9P0EJKXWmppw_aem_LE5vwpE7UE05xw756aNSUw&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4t1IG4N4zCM6vmYArAPd5ihnCopPXT8bmNUUgWkDvGH-s2O7ddteWYRi2e_Q_aem_TNYFN6AWCFirPNQpZqNBxA&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7OSXlvryURvV2XuFsBjfZBeNrqEFPX7yrkMEWMLlV2sNgrdA1Hopzcrnd-SA_aem_1hBXC4x-tUmwcUuw-4A31g&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yTkulJNAGwg5sK2O_GObQ7NfPht9LhOGtQlGE_XtrOBB4VPrlUW6wtSPu8w_aem_b261oIUUHLK7LVzt-Je51Q&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR76uzBfm_yPvj8dqaFwnjuBAfu7PbqRsV5ctvVmvG4iAIJplM9P0EJKXWmppw_aem_LE5vwpE7UE05xw756aNSUw&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR703St8TqC3G_bttDZmmwsTwUEWaOpVhAg_AA1-lMWwNtw5-0y2yNIvcZGI7A_aem__smiIGhLgLV0rkJ0G-18uQ&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR59NIVZZ8MhSU184zJHNOgjNYsgnvNZJIWs1PIEgQznheAhfKNOnm9oTeZSWg_aem_bHr70RWq6iSy-t7F0IKTVQ&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR56YYrCDz3KvS6ukoEIOvpB_QIs2S40sIwdFU3W8b31My_0v-KmPBioD0hQmA_aem_3uBuVO7Ybh6jwziWh5RqZQ&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7OSXlvryURvV2XuFsBjfZBeNrqEFPX7yrkMEWMLlV2sNgrdA1Hopzcrnd-SA_aem_1hBXC4x-tUmwcUuw-4A31g&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yTkulJNAGwg5sK2O_GObQ7NfPht9LhOGtQlGE_XtrOBB4VPrlUW6wtSPu8w_aem_b261oIUUHLK7LVzt-Je51Q&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5edGg5HlYrEaMHnmKjRNY2s5BK-Be-2HQSDOkqvJZHpxkhD59UkG4y-pLQJw_aem_UE1s5S3OQc2GDsBx5EOohg&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4lVjYPMO_vgFWVbvvZ26G9uBNxDYsN-LgUfGJNjmeeSiveA-Dp4CbUqDfbag_aem_h-Rej6cSjNfBk4jZZkjTjg&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR76uzBfm_yPvj8dqaFwnjuBAfu7PbqRsV5ctvVmvG4iAIJplM9P0EJKXWmppw_aem_LE5vwpE7UE05xw756aNSUw&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4t1IG4N4zCM6vmYArAPd5ihnCopPXT8bmNUUgWkDvGH-s2O7ddteWYRi2e_Q_aem_TNYFN6AWCFirPNQpZqNBxA&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5yTkulJNAGwg5sK2O_GObQ7NfPht9LhOGtQlGE_XtrOBB4VPrlUW6wtSPu8w_aem_b261oIUUHLK7LVzt-Je51Q&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT4guGJriK7pTcARrfCAfMrHsNgKQZluh_RNKKwi0IGnqri-PJCE-TDYgIvu7XQyT4tx5AytjvjoQZiWp0HapIOxhNyaHNyK1Zfkg89B3FBp8ayJtRvqVpZ9ZKqNT1NThmlwljBzvEfqTgT7Yki-DcqAA3c)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão