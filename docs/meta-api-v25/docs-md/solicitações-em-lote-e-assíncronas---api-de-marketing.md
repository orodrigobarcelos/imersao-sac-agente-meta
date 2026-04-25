<!-- Fonte: Solicitações em lote e assíncronas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/asyncrequests -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Solicitações em lote e assíncronas


Use solicitações assíncronas para criar anúncios e enviar diversas solicitações de anúncio sem necessidade de bloqueio. Especifique uma URL para chamada após a conclusão das solicitações ou verifique o status da solicitação. Veja a [referência sobre anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/#create).


A forma mais eficaz de gerenciar anúncios é por meio de [solicitações em lote](https://developers.facebook.com/docs/reference/api/batch/). Use essa informação para desempenhar algumas das solicitações mais comuns.


## Solicitações assíncronas


Por exemplo, obtenha o status do conjunto de solicitações assíncronas:

```
curl -G \
  -d 'fields=name,success_count,error_count,is_completed' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_SET_ID>
```


Isso retorna o status geral do conjunto de solicitações assíncronas como um objeto JSON. Nem todos os campos aparecem por padrão. Se você quiser que a consulta inclua campos não padrão, especifique esses campos em `fields`, como `fields=id,owner_id,name,total_count,success_count,error_count,is_completed`.


| Nome | Descrição |
| --- | --- |
| id tipo: número inteiro | Exibido por padrão. O id do conjunto atual de solicitações assíncronas. |
| owner_id tipo: número inteiro | Exibido por padrão. A qual objeto pertence esse conjunto de solicitações assíncronas. Para solicitações assíncronas de anúncios, owner_id será a identificação da conta. |
| name tipo: cadeia de caracteres | Exibido por padrão. O nome desse conjunto de solicitações assíncronas. |
| is_completed tipo: booliano | Exibido por padrão. As solicitações assíncronas desse conjunto foram concluídas. |
| total_count tipo: número inteiro | Não exibido por padrão. O total de solicitações desse conjunto. |
| initial_count tipo: número inteiro | Não exibido por padrão. O número de solicitações ainda não exibidas. |
| in_progress_count tipo: número inteiro | Não exibido por padrão. O número de solicitações em andamento. |
| success_count tipo: número inteiro | Não exibido por padrão. O número de solicitações concluídas com sucesso. |
| error_count tipo: número inteiro | Não exibido por padrão. O número de solicitações concluídas com falha. |
| canceled_count tipo: número inteiro | Não exibido por padrão. O número de solicitações canceladas pelo usuário. |
| notification_uri tipo: cadeia de caracteres | Não exibido por padrão. O URI de notificação desse conjunto de solicitações assíncronas. |
| notification_mode tipo: cadeia de caracteres | Não exibido por padrão. O modo de recebimento de notificações. Os valores válidos incluem o seguinte: OFF – sem notificações; ON_COMPLETE – enviar notificação quando todo o conjunto for concluído |


Depois de obter o status geral do conjunto de solicitações assíncronas, verifique os detalhes de cada solicitação:

```
curl -G \
  -d 'fields=id,status' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_SET_ID>/requests
```


Isso retorna o status e os detalhes de cada solicitação do conjunto de solicitações assíncronas. Para a criação de anúncio assíncrona, faça uma solicitação para cada anúncio. O parâmetro status é usado para filtrar solicitações por status e pode ser uma combinação dos valores a seguir:


- `initial` – não processado ainda.
- `in_progress` – solicitação em processamento.
- `success` – solicitação concluída com sucesso.
- `error` – solicitação concluída com falha
- `canceled` – solicitação cancelada pelo usuário.


A resposta é uma matriz JSON com campos-padrão. Para incluir campos não padrão, especifique o campo em `fields`, como `fields=id,scope_object_id,status,result,input,async_request_set`.


| Nome | Descrição |
| --- | --- |
| id tipo: número inteiro | Exibido por padrão. O ID da solicitação assíncrona. |
| scope_object_id tipo: número inteiro | Exibido por padrão. O ID principal do objeto criado pela solicitação. Se você criar um anúncio, esta será a identificação do conjunto desse novo anúncio. |
| status tipo: cadeia de caracteres | Exibido por padrão. O status dessa solicitação assíncrona. Opções: Initial – não processado ainda.; In_progress – solicitação em processamento.; Success – solicitação concluída com sucesso.; Error – solicitação concluída com falha; Canceled – solicitação cancelada pelo usuário |
| result tipo: matriz | Não exibido por padrão. Se a solicitação for finalizada, ela exibirá o resultado da solicitação. Quando há sucesso, o resultado é igual a uma solicitação não assíncrona. Por exemplo, se você criar um anúncio, o resultado para cada solicitação é a identificação do novo anúncio. Em caso de erro, será matriz do seguinte: error_code – código de erro retornado; error_message – mensagem de erro |
| input tipo: objeto | Não exibido por padrão. A entrada original dessa solicitação assíncrona. Se você criar um anúncio, a entrada será adgroup_spec . |
| async_request_set tipo: objeto | Não exibido por padrão. O conjunto de solicitações assíncronas que contém essa solicitação em particular. |


### Obter detalhes da solicitação


Para obter os detalhes de uma solicitação assíncrona, faça a seguinte chamada:

```
curl -G \
  -d 'fields=id,status' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_SET_ID>/requests
```


Isso retorna um objeto JSON com os campos listados acima.


### Listar os conjuntos de solicitações de uma conta


É possível criar diversos conjuntos de solicitações assíncronas de anúncio. Para consultar todos os conjuntos desse tipo de uma conta de anúncios:

```
curl -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/asyncadrequestsets
```


Isso retorna uma matriz JSON de objetos do conjunto de solicitações assíncronas. Cada objeto é igual ao especificado na [seção conjunto de solicitações assíncronas](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/asyncadrequests). Você pode filtrar os resultados com `is_completed`. Se `is_completed=true`, somente os conjuntos de solicitações assíncronas concluídos serão exibidos.


### Listar as solicitações de um conjunto de anúncios


Você pode fazer uma chamada assíncrona para criar anúncios em conjuntos diferentes. Para ver o status de cada conjunto de anúncios, obtenha todas as solicitações de criação de anúncio de um conjunto:

```
curl -G \
  -d 'fields=id,status' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_SET_ID>/asyncadrequests
```


Isso retorna uma matriz JSON de objetos de solicitação assíncrona. Os campos de status, filtros e solicitações assíncronas são iguais à API `https://graph.facebook.com/&lt;API_VERSION>/&lt;REQUEST_SET_ID>/requests`.


### Atualizar conjuntos de solicitações


É possível alterar `name`, `notification_uri` e `notification_mode` de um conjunto de solicitações assíncronas.

```
curl \
  -F 'name=New Name' \
  -F 'notification_mode=OFF' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_SET_ID>
```


O retorno será `true` se a atualização for bem-sucedida. A alteração de `notification_uri` e `notification_mode` só pode ser feita antes do envio da notificação.


### Cancelar solicitação


É possível cancelar uma solicitação assíncrona, mas isso só pode ser feito se a solicitação ainda não tiver sido processada.

```
curl -X DELETE \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_ID>
```


O retorno será `true` se o cancelamento for bem-sucedido. Também é possível cancelar solicitações ainda não processadas no conjunto de solicitações assíncronas:

```
curl -X DELETE \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<REQUEST_SET_ID>
```


O retorno será `true` se o cancelamento for bem-sucedido.


### Exemplos de solicitações assíncronas


Obter o status de uma solicitação assíncrona específica:

```
//pretty=true for command line readable output
curl -G \
-d "id=6012384857989" \
-d "pretty=true" \
-d "access_token=_____" \
"https://graph.facebook.com/v25.0/"
```


Valores de retorno:

```
{
   "id": "6012384857989",
   "owner_id": 12345,
   "name": "testasyncset",
   "is_completed": true
}
```


Obter os resultados de solicitações:

```
curl -G \
-d "id=6012384857989" \
-d "pretty=true" \
-d "fields=result" \
-d "access_token=_____" \
"https://graph.facebook.com/v25.0/requests"
```


Retorna:

```
{
   "data": [
      {
         "result": {
            "id": "6012384860989"
         },
         "id": "6012384858389"
      },
      {
         "result": {
            "id": "6012384858789"
         },
         "id": "6012384858189"
      }
   ],
   "paging": {
      "cursors": {
         "after": "___",
         "before": "___"
      }
   }
}
```


Obter a lista dos conjuntos de solicitações de uma conta de anúncios:

```
curl -G \
-d "is_completed=1" \
-d "pretty=true" \
-d "access_token=___" \
"https://graph.facebook.com/v25.0/act_71597454/asyncadrequestsets"
```


Retorna:

```
{
   "data": [
      {
         "id": "6012384253789",
         "owner_id": 71597454,
         "name": "testasyncset",
         "is_completed": true
      },
   ],
   "paging": {
      "cursors": {
         "after": "___",
         "before": "___"
      }
   }
}
```


Obter uma lista das solicitações de uma campanha:

```
curl -G \
-d "status=SUCCESS,ERROR" \
-d "pretty=true" \
-d "access_token=___" \
"https://graph.facebook.com/v25.0/6008248529789/asyncadrequests"
```


Valores de retorno:

```
{
   "data": [
      {
         "id": "6012384951789",
         "scope_object_id": 6008248529789,
         "status": "SUCCESS"
      },
   ],
   "paging": {
      "cursors": {
         "after": "___",
         "before": "___"
      }
   }
}
```
[○](https://developers.facebook.com/docs/marketing-api/asyncrequests#)

## Solicitações em lote


Com [solicitações em lote](https://developers.facebook.com/docs/reference/api/batch/), combine um número de chamadas da Graph API a uma solicitação HTTP. A API de Marketing dividiu essa solicitação em solicitações menores. Isso faz com que as [solicitações em lote](https://developers.facebook.com/docs/reference/api/batch/) sejam a maneira mais eficiente de interagir com a API de Marketing. Para incrementar essa eficiência, é possível realizar solicitações em lote paralelas usando tópicos de processamento separados.


Cada [solicitação em lote](https://developers.facebook.com/docs/reference/api/batch/) pode conter um máximo de 50 solicitações. Para a criação de [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup/), é preciso ter 10 ou menos [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/) por lote.


Solicitações em lote para [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/), [criativos de anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative/) e [conjuntos de anúncio](https://developers.facebook.com/docs/reference/ads-api/adset/) são semelhantes e por isso não são discutidas separadamente aqui. Para mais informações, consulte [solicitações em lote da Graph API](https://developers.facebook.com/docs/reference/api/batch/) e [ETags](https://developers.facebook.com/docs/reference/ads-api/etags-reference/).


### Criar anúncios


É possível fornecer o criativo e outros objetos de anúncio em uma solicitação em lote. Por exemplo: você pode criar três [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/) usando um [criativo de anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative/) e três [especificações de direcionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/) diferentes. Primeiro, defina o [criativo do anúncio](https://developers.facebook.com/docs/reference/ads-api/adcreative/). Depois, consulte-o ao criar cada [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup/):

```
curl -F 'access_token=______'
  -F 'test1=@./test1.jpg'
  -F 'batch=[
             {
              "method": "POST",
              "name": "create_adimage",
              "relative_url": "<API_VERSION>/act_187687683/adimages",
              "attached_files": "test1"
             },
             {
              "method": "POST",
              "name": "create_creative",
              "relative_url": "<API_VERSION>/act_187687683/adcreatives",
              "attached_files": "test1",
              "body": "name=sample creative&object_story_spec={\"link_data\": {\"image_hash\": \"{result=create_adimage:$.images.*.hash}\", \"link\": \"https://www.test12345.com\", \"message\": \"this is a sample message\"}, \"page_id\":\"12345678\"}&degrees_of_freedom_spec={\"creative_features_spec\": {\"standard_enhancements\": {\"enroll_status\": \"OPT_OUT\"}}}"
             },
             {
              "method": "POST",
              "relative_url": "<API_VERSION>/act_187687683/ads",
              "body": "adset_id=6004163746239&redownload=1&status=PAUSED&optimization_goal=REACH&billing_event=IMPRESSIONS&&creative={\"creative_id\":\"{result=create_creative:$.id}\"}&targeting={\"countries\":[\"US\"]}&name=test1"
             },
             {
              "method": "POST",
              "relative_url": "<API_VERSION>/act_187687683/ads",
              "body": "adset_id=6004163746239&redownload=1&status=PAUSED&optimization_goal=REACH&billing_event=IMPRESSIONS&&creative={\"creative_id\":\"{result=create_creative:$.id}\"}&targeting={\"countries\":[\"US\"]}&name=test2"
             },
             {
              "method": "POST",
              "relative_url": "<API_VERSION>/act_187687683/ads",
              "body": "adset_id=6004163746239&redownload=1&status=PAUSED&optimization_goal=REACH&billing_event=IMPRESSIONS&&creative={\"creative_id\":\"{result=create_creative:$.id}\"}&targeting={\"countries\":[\"US\"]}&name=test3"
             }
            ]' https://graph.facebook.com/
```


A resposta inclui códigos individuais de resposta para cada solicitação e a resposta-padrão da Graph API. Para mais detalhes, veja [Como fazer várias solicitações de API](https://developers.facebook.com/docs/graph-api/making-multiple-requests).


O processo de [solicitação em lote](https://developers.facebook.com/docs/reference/api/batch/) usa o [formato de expressão JSONPath](https://l.facebook.com/l.php?u=https%3A%2F%2Fcode.google.com%2Fp%2Fjsonpath%2F&h=AT52biqLUhVMNHrScuJupxFDHLc99LBX8P0xMaEx1KPBlERRx02q5fX9DEIX2nCejuIeZj-ASOfN3LapN7ZV6al_kz-X8NVBvwV-R3dlOESjgfH5pc3dyiC95EmpHXD51WqQDhcDjORyBrjO1mrZV5f_Jd0) como referência a solicitações anteriores.


### Atualizar anúncios


É possível atualizar anúncios por meio de solicitações em lote. Para atualizar lances em três [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/):

```
curl -F 'access_token=____'
  -F 'batch=[
             {
              "method": "POST",
              "relative_url": "<API_VERSION>/6004251715639",
              "body": "redownload=1&name=new name"
             },
             {
              "method": "POST",
              "relative_url": <API_VERSION>/v6004251716039",
              "body": "redownload=1&name=new name"
             },
             {
              "method": "POST",
              "relative_url": "<API_VERSION>/6004251715839",
              "body": "redownload=1&name=new name"
             }
            ]' https://graph.facebook.com
```


Se incluir `redownload=1` na URL relativa, você obterá os detalhes completos do anúncio, incluindo a identificação. Isso ajuda a identificar quais anúncios foram atualizados.


Para atualizar o criativo do anúncio, especifique todo o criativo ou forneça uma nova identificação correspondente. Isso acontece porque os [criativos de anúncios](https://developers.facebook.com/docs/reference/ads-api/adcreative/) não podem ser editados depois que forem criados, exceto pelo nome e status de execução.


### Ler anúncios


Se você tiver uma grande quantidade de [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/), divida a solicitação em várias dentro de uma [solicitação em lote](https://developers.facebook.com/docs/reference/api/batch/):

```
curl -F 'access_token=____'
  -F 'batch=[
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/?ids=6003356308839,6004164369439&fields=<comma separated list of fields>"
             },
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/6003356307839/ads&fields=<comma separated list of fields>"
             },
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/act_187687683/ads?adset_ids=[6003356307839, 6004164259439]&fields=<comma separated list of fields>"
             }
            ]' https://graph.facebook.com
```


`6003356308839` e `6004164369439` são identificações do [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup/), ao passo que `6003356307839` e `6004164259439` são identificações do [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset/).


### Insights sobre Anúncios


Se você tiver uma grande quantidade de [Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/insights/), divida a solicitação em várias dentro de uma [solicitação em lote](https://developers.facebook.com/docs/reference/api/batch/):

```
curl -F 'access_token=____'
  -F 'batch=[
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/act_19643108/insights?filtering=[{field:'ad.id',operator:'IN',value:[6003356308839,6004164369439]}]"
             },
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/6003356308839/insights"
             },
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/act_187687683/insights?filtering=[{field:'adset.id',operator:'IN',value:[6003356307839, 6004164259439]}]"
             }
            ]' https://graph.facebook.com
```


No exemplo, `6003356308839` e `6004164369439` são identificações do [anúncio](https://developers.facebook.com/docs/reference/ads-api/adgroup/), ao passo que `6003356307839` e `6004164259439` são identificações do [conjunto de anúncios](https://developers.facebook.com/docs/reference/ads-api/adset/).


Em [contas de anúncio](https://developers.facebook.com/docs/reference/ads-api/adaccount/) com um grande número de [anúncios](https://developers.facebook.com/docs/reference/ads-api/adgroup/), o uso de `act_<account_ID>/adgroupstats` não é recomendado, pois pode causar o encerramento da solicitação.


### Solicitações em lote para estimativa de alcance


É possível solicitar até 50 [estimativas de alcance](https://developers.facebook.com/docs/reference/ads-api/reachestimate/) em uma única [solicitação em lote](https://developers.facebook.com/docs/reference/api/batch/). No exemplo a seguir, a estimativa de alcance é solicitada para duas [especificações de direcionamento](https://developers.facebook.com/docs/reference/ads-api/targeting-specs/) diferentes:

```
curl -F 'access_token=____'
  -F 'batch=[
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/act_600335/reachestimate?targeting_spec={'geo_locations': {'countries':['US']}}"
             },
             {
              "method": "GET",
              "relative_url": "<API_VERSION>/act_600335/reachestimate?targeting_spec={'geo_locations': {'countries':['FR']}}"
             }
            ]' https://graph.facebook.com
```
[○](https://developers.facebook.com/docs/marketing-api/asyncrequests#)

## API em Lote


A API em lote permite fazer solicitações em lote e enviá-las de maneira assíncrona. Agrupe várias chamadas da Graph API em uma única solicitação HTTP e as execute de forma assíncrona sem a necessidade de bloquear. Você pode também especificar dependências entre operações relacionadas.


O Facebook processa cada operação independente de maneira paralela e as operações dependentes de forma sequencial. Cada chamada de API pode ter até 1.000 solicitações.


### Fazer uma chamada da API em lote


Para fazer uma chamada da API em Lote:

```
curl \
-F "access_token=___" \
-F "name=asyncbatchreqs" \
-F "adbatch=<an array of requests>"\
"https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/async_batch_requests"
```


Forneça uma matriz de solicitações `HTTP POST` como matrizes `JSON`. Cada solicitação tem o seguinte:


- `name`
- `relative_url` - porção da URL após graph.facebook.com
- `body`


A API retorna um ID que você usa para consultar o progresso das solicitações.


Por exemplo, crie uma campanha com um conjunto de anúncios no formato JSONPath para incluir as solicitações anteriores:

```
curl \
-F "access_token=___" \
-F "name=batchapiexample" \
-F "adbatch=[
  {
    'name': 'create-campaign',
    'relative_url': 'act_123456/campaigns',
    'body': 'name%3DTest+Campaign%26objective%3DLINK_CLICKS%26status%3DPAUSED%26buying_type%3DAUCTION',
  },
  {
    'name': 'create-adset',
    'relative_url': 'act_123456/adsets',
    'body': 'targeting%3D%7B%22geo_locations%22%3A%7B%22countries%22%3A%5B%22US%22%5D%7D%7D%26daily_budget%3D5000%26campaign_id%3D%7Bresult%3Dcreate-campaign%3A%24.id%7D%26bid_amount%3D2%26name%3DFirst%2BAd%2BSet%20Test%26billing_event%3DLINK_CLICKS',
  },
]" \
https://graph.facebook.com/<API_VERSION>/act_123456/async_batch_requests
```


Para obter o status de um conjunto de solicitações:

```
curl –G \
-d "access_token=___" \
-d "fields=<comma separated list of fields>" \
"https://graph.facebook.com/v25.0/<REQUEST_SET_ID>"
```


Isso retorna o status geral do conjunto de solicitações assíncronas como objetos JSON. Nem todos os campos são retornados por padrão. Para incluí-los, especifique `fields`, por exemplo, `fields=id,owner_id,name,total_count,success_count,error_count,is_completed`.


| Nome | Descrição |
| --- | --- |
| id tipo: número inteiro | Exibido por padrão. O id do conjunto atual de solicitações assíncronas. |
| owner_id tipo: número inteiro | Exibido por padrão. O objeto ao qual pertence o conjunto de solicitações assíncronas. Se você criar anúncios, owner_id será a identificação da conta de anúncios. |
| name tipo: cadeia de caracteres | Exibido por padrão. O nome desse conjunto de solicitações assíncronas. |
| is_completed tipo: booliano | Exibido por padrão. Todas as solicitações assíncronas no conjunto foram concluídas. |
| total_count tipo: número inteiro | Não exibido por padrão. O total de solicitações nesse conjunto de solicitações. |
| initial_count tipo: número inteiro | Não exibido por padrão. O número de solicitações ainda não exibidas. |
| in_progress_count tipo: número inteiro | Não exibido por padrão. O número de solicitações em andamento. |
| success_count tipo: número inteiro | Não exibido por padrão. O número de solicitações concluídas com sucesso. |
| error_count tipo: número inteiro | Não exibido por padrão. O número de solicitações concluídas com falha. |
| canceled_count tipo: número inteiro | Não exibido por padrão. O número de solicitações canceladas pelo usuário. |
| notification_uri tipo: cadeia de caracteres | Não exibido por padrão. O URI de notificação desse conjunto de solicitações assíncronas. |
| notification_mode tipo: cadeia de caracteres | Não exibido por padrão. Os modos de recebimento de notificações. Valores válidos: OFF – sem notificações; ON_COMPLETE – enviar notificação quando todo o conjunto for concluído |
| notification_result tipo: cadeia de caracteres | Não exibido por padrão. O resultado do envio da notificação. |
| notification_status tipo: cadeia de caracteres | Não exibido por padrão. Status da notificação: not_sent , sending ou sent . |


Depois de obter o status geral, verifique os detalhes de cada solicitação:

```
curl –G \
-d "access_token=___" \
-d "fields=<comma separated list of fields>" \
"https://graph.facebook.com/v25.0/<REQUEST_SET_ID>/requests"
```


Isso retorna detalhes como uma matriz JSON. Para incluir campos não padrão, especifique o campo em `fields`, como `fields=id,scope_object_id,status,result,input,async_request_set`.


| Nome | Descrição |
| --- | --- |
| id tipo: número inteiro | Exibido por padrão. O ID da solicitação assíncrona. |
| scope_object_id tipo: número inteiro | Exibido por padrão. O ID principal do objeto criado pela solicitação. Se você criar anúncios, esta será a identificação do conjunto desse novo anúncio. |
| status tipo: cadeia de caracteres | Exibido por padrão. Status dessa solicitação assíncrona: Initial – não processado ainda.; In_progress – solicitação em processamento.; Success – solicitação concluída com sucesso; Error – solicitação concluída com falha; Canceled – solicitação cancelada pelo usuário |
| result tipo: matriz | Não exibido por padrão. Se a solicitação for concluída, o resultado é exibido. Para obter sucesso, o resultado é igual à API não assíncrona. Por exemplo, se você criar um anúncio, o resultado será uma nova identificação do anúncio. Em caso de erro: error_code – código de erro retornado; error_message – mensagem de erro |
| input tipo: objeto | Não exibido por padrão. A entrada original dessa solicitação. Se você criar um anúncio, a entrada será adgroup_spec . |
| async_request_set tipo: objeto | Não exibido por padrão. O conjunto de solicitações assíncronas que contém essa solicitação. |


### Listar solicitações da API em lote de uma conta de anúncios


É possível criar diversos conjuntos de solicitações da API em lote. Para consultar todos os conjuntos de solicitações de uma conta de anúncios:

```
curl –G \
-d "access_token=___" \
"https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/async_requests"
```
[○](https://developers.facebook.com/docs/marketing-api/asyncrequests#)

## ETags


A API de Marketing é compatível com [Etags](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FProtocols%2Frfc2616%2Frfc2616-sec14.html%23sec14.19&h=AT5nKL_6B3HTuOP79voQTki_qNMl9ajxZW00WDSknkvW4fubDhqCilfSzqg8q-riaEJW6pdvr6mptHXMyailIjowFTvppHnpiqr0Mnf177GOQKX9o-t8UzuW-9b100YOwGbPkPX1vUrpdsGEeN-U5PB26tM). Isso ajuda você a saber se houve alteração nos dados consultados desde a última verificação. Como funciona:


- Quando você faz uma chamada, o cabeçalho da resposta inclui uma ETag cujo valor é o hash dos dados retornados na chamada de API. Salve o valor dessa ETag para uso na próxima etapa.
- Na próxima vez que você fizer essa chamada de API, inclua o cabeçalho da solicitação **If-None-Match** com o valor salvo da ETag.
- Se não houver alteração nos dados, o código de status da resposta será `304 – Not Modified` e nenhum dado será retornado.
- Se os dados foram alterados desde a última consulta, eles serão retornados normalmente com uma nova ETag. Salve o novo valor da ETag para uso em chamadas futuras.


As ETags ajudam a reduzir o tráfego de dados, mas o `If-None-Match GET` ainda deduz o limite de volume para seu app.


A ETag é calculada usando toda a resposta da chamada de API, incluindo a formatação. O formato da resposta pode ser afetado pela cadeia de caracteres do agente do usuário. Por isso, mantenha o agente do usuário consistente entre chamadas feitas a partir do mesmo cliente.


### Exemplos de ETags


Para verificar se houve alteração nas contas de anúncios do usuário.


**Etapa 1**: determinar a ETag dos dados atuais

```
curl -i "https://graph.beta.facebook.com/me/adaccounts?access_token=___"
```


A resposta será a seguinte:

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Type: text/javascript; charset=UTF-8
ETag: "7776cdb01f44354af8bfa4db0c56eebcb1378975"
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Pragma: no-cache
X-FB-Rev: 495685
X-FB-Server: 10.30.149.204
X-FB-Debug: CWbHcogdwUE8saMv6ML+8FacXFrE8ufhjjwxU2dQWaA=
X-Cnection: close
Date: Mon, 16 Jan 2012 12:07:44 GMT
Content-Length: 3273

{"data":[{"id":"act.......
```


No exemplo, a ETag é `"7776cdb01f44354af8bfa4db0c56eebcb1378975"`. Vale lembrar que esse valor inclui aspas (`"`).


**Etapa 2**: determinar se houve alterações nos dados

```
curl -i -H "If-None-Match: \"7776cdb01f44354af8bfa4db0c56eebcb1378975\"" "https://graph.beta.facebook.com/me/adaccounts?access_token=___"
```


Se não houver alteração, a resposta será a seguinte:

```
HTTP/1.1 304 Not Modified
Access-Control-Allow-Origin: *
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Type: text/javascript; charset=UTF-8
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Pragma: no-cache
X-FB-Rev: 495685
X-FB-Server: 10.30.177.190
X-FB-Debug: ImBhat3k07Nez5FvuS2lPWU0U2xxmxD4B3k9ua4Sk7Q=
X-Cnection: close
Date: Mon, 16 Jan 2012 12:09:17 GMT
Content-Length: 0
```


Observe a resposta `304 Not Modified`. Se houvesse alteração nos dados, uma resposta normal de API teria sido retornada.


Um exemplo de lote para verificar se houve alteração nos anúncios do usuário.


**Etapa 1**: determinar a ETag dos dados atuais

```
curl -i "curl -F 'access_token=___' -F 'batch=[
  {"method":"GET", "relative_url": "?ids=6003356308839,6004164369439" },
  {"method":"GET", "relative_url": "act_12345678/ads?campaign_ids=[6003356307839, 6004164259439]"}]'
 https://graph.facebook.com"
```


A resposta terá valores de ETag como no exemplo a seguir:

```
...{"name":"ETag","value":"\"21d371640127490b2ed0387e8af3f0f8c9eff012\""}...
...{"name":"ETag","value":"\"410e53bb257f116e8716e4ebcc76df1c567b87f4\""}...
```


Neste exemplo, as ETags são `"21d371640127490b2ed0387e8af3f0f8c9eff012"` e `"410e53bb257f116e8716e4ebcc76df1c567b87f4"`. Vale lembrar que esse valor inclui aspas (`"`).


**Etapa 2**: determinar se houve alterações nos dados

```
curl -F 'access_token=___' -F 'batch=[
  {"method":"GET", "headers":["If-None-Match: \"21d371640127490b2ed0387e8af3f0f8c9eff012\""], "relative_url": "?ids=6003356308839,6004164369439" },
  {"method":"GET",  "headers":["If-None-Match: \"410e53bb257f116e8716e4ebcc76df1c567b87f4\""], "relative_url": "act_12345678/ads?campaign_ids=[6003356307839, 6004164259439]"}]'
https://graph.facebook.com
```


Se não houver alteração, a resposta será a seguinte:

```
[{
    "code": 304,
    .
    .
    .
    "body": null
},
{
    "code": 304,
    .
    .
    .
    "body": null
}]
```


Observe a resposta `304 Not Modified`. Se houver alteração nos dados, retornaremos uma resposta normal de API.
[○](https://developers.facebook.com/docs/marketing-api/asyncrequests#)[○](https://developers.facebook.com/docs/marketing-api/asyncrequests#)Nesta Página[Solicitações em lote e assíncronas](https://developers.facebook.com/docs/marketing-api/asyncrequests#solicita--es-em-lote-e-ass-ncronas)[Solicitações assíncronas](https://developers.facebook.com/docs/marketing-api/asyncrequests#aoverview)[Obter detalhes da solicitação](https://developers.facebook.com/docs/marketing-api/asyncrequests#obter-detalhes-da-solicita--o)[Listar os conjuntos de solicitações de uma conta](https://developers.facebook.com/docs/marketing-api/asyncrequests#listar-os-conjuntos-de-solicita--es-de-uma-conta)[Listar as solicitações de um conjunto de anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#listar-as-solicita--es-de-um-conjunto-de-an-ncios)[Atualizar conjuntos de solicitações](https://developers.facebook.com/docs/marketing-api/asyncrequests#atualizar-conjuntos-de-solicita--es)[Cancelar solicitação](https://developers.facebook.com/docs/marketing-api/asyncrequests#cancelar-solicita--o)[Exemplos de solicitações assíncronas](https://developers.facebook.com/docs/marketing-api/asyncrequests#examples)[Solicitações em lote](https://developers.facebook.com/docs/marketing-api/asyncrequests#boverview)[Criar anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#adgroup)[Atualizar anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#atualizar-an-ncios)[Ler anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#ler-an-ncios)[Insights sobre Anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#adinsights)[Solicitações em lote para estimativa de alcance](https://developers.facebook.com/docs/marketing-api/asyncrequests#solicita--es-em-lote-para-estimativa-de-alcance)[API em Lote](https://developers.facebook.com/docs/marketing-api/asyncrequests#batchapioverview)[Fazer uma chamada da API em lote](https://developers.facebook.com/docs/marketing-api/asyncrequests#fazer-uma-chamada-da-api-em-lote)[Listar solicitações da API em lote de uma conta de anúncios](https://developers.facebook.com/docs/marketing-api/asyncrequests#listar-solicita--es-da-api-em-lote-de-uma-conta-de-an-ncios)[ETags](https://developers.facebook.com/docs/marketing-api/asyncrequests#etags)[Exemplos de ETags](https://developers.facebook.com/docs/marketing-api/asyncrequests#etag) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63Prc6JnMc2ujUR_oe8hwD59RZdD1ahqU72AW9uUQsUJ-ED-IJeHbxnFv-kw_aem_CvhkNWRCSl_KpJh8B82bdg&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR79DfuVRkpmbqTpN8vRRD2tD0Abc2VIfvn9G7gb2T5nJ0eq7R0Z-gjKoVgLsg_aem_20pb5XY0Ys3FOYsT_pd-6Q&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4srDHHDxkx1OPj9aS8rkCJf9k2Sdmeait_thfuxAnkTyB9MvG62nCpyfvN8Q_aem_JuwJC7E8BjLhJ3ToE0m7Hw&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR424pQDveuv7q2CkZZm1TkWjmyDT5tD81dOFMWfEDwSLMKBjP_KNLS2pnw4eA_aem_SyutJWE186TERyxpSgxgSA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-b7njXvI-xi5GG3ImnjLnWOT3S89uJf2tHxU0M__BxPpDzWT7veJ7CmpNgg_aem_YIxFrK5L8pikhnu6pLPxmA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR61OmxV00Z-hVRh476VDCovF3JetsZ393bWxcrcUbLSl6dGDpqXSFNZQm5_9Q_aem_pLrqj18tuk2-veo-uLtr3g&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Ftaz6onIoEDvEdUFvioWZT0Q6GMfj4yT7BOZ1o1W_ENv1gHS3_F-ACDewug_aem_8WlaKr1KpIL4QxWAcvJ2VQ&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-b7njXvI-xi5GG3ImnjLnWOT3S89uJf2tHxU0M__BxPpDzWT7veJ7CmpNgg_aem_YIxFrK5L8pikhnu6pLPxmA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-b7njXvI-xi5GG3ImnjLnWOT3S89uJf2tHxU0M__BxPpDzWT7veJ7CmpNgg_aem_YIxFrK5L8pikhnu6pLPxmA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR61OmxV00Z-hVRh476VDCovF3JetsZ393bWxcrcUbLSl6dGDpqXSFNZQm5_9Q_aem_pLrqj18tuk2-veo-uLtr3g&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR61OmxV00Z-hVRh476VDCovF3JetsZ393bWxcrcUbLSl6dGDpqXSFNZQm5_9Q_aem_pLrqj18tuk2-veo-uLtr3g&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR5Ftaz6onIoEDvEdUFvioWZT0Q6GMfj4yT7BOZ1o1W_ENv1gHS3_F-ACDewug_aem_8WlaKr1KpIL4QxWAcvJ2VQ&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6egQY2SG19wcusRSI7uJoD9ZLRtgm7PUUObt2CKu92SLbxOaD4Y0vH6x9M2g_aem_D9z_ALpm5oIM5T8Zh8SY2w&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR424pQDveuv7q2CkZZm1TkWjmyDT5tD81dOFMWfEDwSLMKBjP_KNLS2pnw4eA_aem_SyutJWE186TERyxpSgxgSA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR79DfuVRkpmbqTpN8vRRD2tD0Abc2VIfvn9G7gb2T5nJ0eq7R0Z-gjKoVgLsg_aem_20pb5XY0Ys3FOYsT_pd-6Q&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR61OmxV00Z-hVRh476VDCovF3JetsZ393bWxcrcUbLSl6dGDpqXSFNZQm5_9Q_aem_pLrqj18tuk2-veo-uLtr3g&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR63Prc6JnMc2ujUR_oe8hwD59RZdD1ahqU72AW9uUQsUJ-ED-IJeHbxnFv-kw_aem_CvhkNWRCSl_KpJh8B82bdg&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6egQY2SG19wcusRSI7uJoD9ZLRtgm7PUUObt2CKu92SLbxOaD4Y0vH6x9M2g_aem_D9z_ALpm5oIM5T8Zh8SY2w&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR6-b7njXvI-xi5GG3ImnjLnWOT3S89uJf2tHxU0M__BxPpDzWT7veJ7CmpNgg_aem_YIxFrK5L8pikhnu6pLPxmA&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExM0lLMlA1bUZmZDh1ZW1PZ3NydGMGYXBwX2lkATAAAR4srDHHDxkx1OPj9aS8rkCJf9k2Sdmeait_thfuxAnkTyB9MvG62nCpyfvN8Q_aem_JuwJC7E8BjLhJ3ToE0m7Hw&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT5aWx03VQy5BgvrfIIWHRBTg1tcYaBrnHu3acgp_WHXsO5YZy5ooHlH_iP8ja2TdANpxCEsGdBVaZ_Jg5rL8-R8Oc_abS5Zin8k9eAC6DEJLam592Sh6uSxFHyQ613zT9ZKa1YkoND6YFid4DbCa-8mvsA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão