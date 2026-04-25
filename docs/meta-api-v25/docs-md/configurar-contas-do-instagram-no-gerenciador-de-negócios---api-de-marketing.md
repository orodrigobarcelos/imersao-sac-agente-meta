<!-- Fonte: Configurar contas do Instagram no Gerenciador de Negócios - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Configurar contas do Instagram no Gerenciador de Negócios


Antes de começar a veicular anúncios no Instagram, você precisa da identificação de uma conta da plataforma. Existem vários métodos para isso, mas recomendamos seguir o processo do [Gerenciador de Negócios](https://developers.facebook.com/docs/business-manager-api) descrito neste guia.


O Gerenciador de Negócios oferece uma interface única para você gerenciar sua presença no Instagram. Além de veicular anúncios, é possível adicionar posts não publicitários, responder a comentários como perfil do Instagram e muito mais.


Use este guia para configurar suas contas do Instagram no Gerenciador de Negócios:


- Etapa 1: [crie uma conta comercial no Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#before-you-start).
- Etapa 2: [use o Gerenciador de Negócios para reivindicar a propriedade da sua conta](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#claim_account).
- Etapa 3 (opcional): [se você estiver usando um terceiro para veicular anúncios em nome da sua empresa, atribua o parceiro como uma agência](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#assign_account).
- Etapa 4: [para fins de financiamento, atribua uma ou mais contas de anúncios às suas contas do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#assing_ad_account).
- Etapa 5: é preciso ter a identificação da conta do Instagram para veicular anúncios. [Acesse todas as contas do Instagram associadas a uma empresa para ver essa informação](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#account_api).


## Etapa 1. Criar uma conta comercial no Instagram


Nesta implementação, sua empresa precisa ter uma conta comercial no Instagram. Consulte [Como configurar uma conta comercial no Instagram](https://www.facebook.com/help/502981923235522).
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)

## Etapa 2. Usar o Gerenciador de Negócios para reivindicar contas do Instagram


Para associar uma conta do Instagram a uma empresa, você precisa do nome de usuário e da senha da conta. Consulte [Como adicionar uma conta do Instagram ao Gerenciador de Negócios](https://www.facebook.com/business/help/620548115562686).
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)

## Etapa 3 (opcional). Atribuir uma agência


Se um anunciante tiver uma conta no Instagram e um terceiro quiser veicular anúncios em nome dele, atribua o terceiro como parceiro. No Gerenciador de Negócios, clique em **Atribuir parceiros** e insira a identificação empresarial da agência.


Consulte [Como anunciar em nome de outra empresa no Meta Business Suite ou no Gerenciador de Negócios](https://www.facebook.com/business/help/375950529870841) para saber mais.
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)

## Etapa 4. Atribuir contas de anúncios


Caso você já tenha uma conta no Instagram e use os passos a seguir como referência, saiba que o ponto de extremidade `InstagramUserID` está obsoleto na versão v22.0 e será descontinuado em todas as versões a partir de 21 de abril de 2025. Como alternativa, você pode usar o [ponto de extremidade `IGUserID`](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user) da plataforma do Instagram.


Depois que você tiver acesso a uma conta do Instagram no Gerenciador de Negócios, será possível atribuir uma ou mais contas de anúncios a ela. No Gerenciador de Negócios, selecione sua conta do Instagram, clique em **Adicionar ativos** e escolha as contas de anúncios que você quer associar.


Você também pode usar a API enviando uma solicitação `POST` com `business` e `account_id`. É preciso ser pelo menos um `ADMIN` da empresa.


A conta de anúncios precisa:


- pertencer à empresa ou
- poder ser acessada pela empresa e, ao mesmo tempo, pertencer à empresa proprietária da conta do Instagram.


Por exemplo, caso você receba acesso a uma conta de anúncios e a uma conta do Instagram de um cliente, sua empresa poderá associá-las. Porém, não será possível atribuir uma conta de anúncios pertencente à empresa de um cliente a uma conta do Instagram de propriedade de outra empresa, mesmo que você tenha acesso de administrador a ambas.

```
curl \
-F "access_token=<ACCESS_TOKEN>"\
-F "business=<BUSINESS_ID>"\
-F "account_id=<AD_ACCOUNT_ID>"\
"https://graph.facebook.com/<API_VERSION>/<IG_USER_ID>/authorized_adaccounts"
```


É possível ver quais contas de anúncios de uma determinada empresa estão associadas a uma conta do Instagram. Você precisa fornecer o parâmetro `business` e deve ser pelo menos um `EMPLOYEE` da empresa. Retornaremos apenas contas de anúncios da empresa em questão e aquelas associadas à conta do Instagram fornecida. Se essa conta do Instagram estiver associada a contas de anúncios de outras empresas, não as enviaremos na resposta. Você pode enviar uma solicitação `GET`:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "business=<BUSINESS_ID>"\
"https://graph.facebook.com/<API_VERSION>/<IG_USER_ID>/authorized_adaccounts"
```


Depois de atribuir uma conta de anúncios, todos os usuários da empresa com permissão de veiculação nessa conta poderão veicular anúncios na conta do Instagram associada.
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)

## Etapa 5. Ver as contas associadas


Para ver todas as contas do Instagram que pertencem a uma empresa ou às quais uma empresa tem acesso, faça uma solicitação `GET`:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "fields=username,profile_pic" \
"https://graph.facebook.com/<API_VERSION>/<BUSINESS_ID>/instagram_accounts"
```


O token de acesso é associado a um app. Confira os requisitos para chamar a API:


- É preciso ter um [nível de acesso](https://developers.facebook.com/docs/marketing-api/access)`STANDARD` para o app.
- Ou a empresa que você está consultando deve ser proprietária do app.


Para ver todas as contas do Instagram associadas a uma conta de anúncios, faça uma chamada `GET` para:

```
curl -G \
-d "access_token=<ACCESS_TOKEN>"\
-d "fields=username,profile_pic" \
"https://graph.facebook.com/<API_VERSION>/act_<ADACCOUNT_ID>/instagram_accounts"
```


A resposta das duas chamadas de API anteriores contém uma matriz de contas do Instagram, e cada uma pode incluir os campos a seguir:


| Nome do campo | Descrição |
| --- | --- |
| id tipo: string numérica | É a identificação da conta do Instagram. (Obrigatório para a criação de anúncios) |
| username tipo: string | É o nome de usuário do Instagram. |
| profile_pic tipo: string | É o URL que direciona para a foto do perfil da conta do Instagram. |


Por exemplo:

```
{
  "data": [
    {
      "username": "jaspersmarket",
      "profile_pic": "https://igcdn-photos-a-a.akamaihd.net/hphotos-ak-xaf1/t51.2885-19/11311930_826942667396992_856534255_a.jpg",
      "id": "1023317097692584"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MTM4OTY1MDkwNzkyMTE4NQ==",
      "after": "MTAyMzMxNzA5NzY5MjU4NA=="
    }
  }
}
```


Não é possível conceder permissões diretamente por meio de uma conta do Instagram. Em vez disso, conceda a alguém permissões para a Página ou empresa que está conectada à conta do Instagram. Qualquer pessoa da sua empresa que tenha permissão de veiculação em uma conta de anúncios vinculada a uma conta do Instagram também poderá veicular anúncios para essa conta do Instagram.


Para criar unidades de anúncios, use o token de acesso de um usuário ou [usuário do sistema](https://www.facebook.com/business/help/327596604689624) que pode acessar a conta de anúncios associada.
[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)

## Connection Objects



Once you create an Instagram account, you cannot use [Connection Objects](https://developers.facebook.com/docs/marketing-api/connectionobjects) to view these accounts. You should use assets under business instead of `connection objects`.


For Instagram accounts, use the following endpoints:


- `{business_id}/instagram_accounts`
- `act_{adaccount_id}/instagram_accounts`
- `{page_id}/instagram_accounts`
 [○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)[○](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#)Nesta Página[Configurar contas do Instagram no Gerenciador de Negócios](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#configurar-contas-do-instagram-no-gerenciador-de-neg-cios)[Etapa 1. Criar uma conta comercial no Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#before-you-start)[Etapa 2. Usar o Gerenciador de Negócios para reivindicar contas do Instagram](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#claim_account)[Etapa 3 (opcional). Atribuir uma agência](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#assign_account)[Etapa 4. Atribuir contas de anúncios](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#assing_ad_account)[Etapa 5. Ver as contas associadas](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#account_api)[Connection Objects](https://developers.facebook.com/docs/instagram/ads-api/guides/ig-accounts-with-business-manager#co) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4PG6c2c9bc4eFNm5LscyI3TMbWzExJZzYS6oOCCzjWh2imYJHLtMdsE7a3dQ_aem_XxKgyzl-tLyo9p-JXkLdGg&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GkXCS4rTE6ZqKPC40zlBBVwdGvgdacUM1EKoT7IIFOqr1TCPQxLfRTXMnZg_aem_WE8teRiiEX0nHLUy7o7VHw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7WAad0io9D_D9Iuok2kBlz0niVcZggNNWL2YQmaZC9T7V7Z0zPCrcOdL0I-g_aem_Dln0KqN59SnUZoxy1faCLw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GeoLSg5ltJNdo4mTrbbVDNschhcJ3vTya_T_R8SGTY9iCZGU7mVLtOAtjJg_aem_8mqhfgnULJ1mZ2tUkRRk_g&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6N6PZKeZLNb1hQhtiLIoIokspnZUOnPyb5CxKx9CF6lSQjjAsP1JOqLAzsPA_aem_baaNG8-rBJwZ3qN9_iZ8Rw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7WAad0io9D_D9Iuok2kBlz0niVcZggNNWL2YQmaZC9T7V7Z0zPCrcOdL0I-g_aem_Dln0KqN59SnUZoxy1faCLw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7kZHYV-9M2gFjzVki2CasIrnI64aocWDVJ4GlBvOoyb6QjmM-awC2HhYmh5Q_aem_0PoYTBPBZtXB8J_fI96Miw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GkXCS4rTE6ZqKPC40zlBBVwdGvgdacUM1EKoT7IIFOqr1TCPQxLfRTXMnZg_aem_WE8teRiiEX0nHLUy7o7VHw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GeoLSg5ltJNdo4mTrbbVDNschhcJ3vTya_T_R8SGTY9iCZGU7mVLtOAtjJg_aem_8mqhfgnULJ1mZ2tUkRRk_g&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7WAad0io9D_D9Iuok2kBlz0niVcZggNNWL2YQmaZC9T7V7Z0zPCrcOdL0I-g_aem_Dln0KqN59SnUZoxy1faCLw&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4PG6c2c9bc4eFNm5LscyI3TMbWzExJZzYS6oOCCzjWh2imYJHLtMdsE7a3dQ_aem_XxKgyzl-tLyo9p-JXkLdGg&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GeoLSg5ltJNdo4mTrbbVDNschhcJ3vTya_T_R8SGTY9iCZGU7mVLtOAtjJg_aem_8mqhfgnULJ1mZ2tUkRRk_g&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6GeoLSg5ltJNdo4mTrbbVDNschhcJ3vTya_T_R8SGTY9iCZGU7mVLtOAtjJg_aem_8mqhfgnULJ1mZ2tUkRRk_g&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7DYfJhPDT1_T2LMuOsbwYm82cBVSjezkWh8dMUIfBhBkBq8gX1YYPM4N63gA_aem_CMASkZKRqc_45Y8gEo_kHA&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5j-VlK6WWG_MVZ7jSTNW2OasuavBV3I37qfSsI1Y7qyB7qheVldUDZDJXUKw_aem_hBk845-gKB1BQo9lDZUuxQ&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7iDtcyg92QQOE3Gjo_LlRejGXLCzw0153s4HGte47s9U2l7TTTatdXXPWmmUoi-bwW1M682z9a0pRstc5t6sSeAnHtoboPm8d11GwfbVw4jptd2d8--ABk5lu4RIkJhL0Wuq3Y3oTgJQnqd5IMX-Tte-4)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão