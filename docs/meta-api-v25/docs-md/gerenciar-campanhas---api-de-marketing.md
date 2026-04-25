<!-- Fonte: Gerenciar campanhas - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Gerenciamento de campanhas de anúncios


Gerenciar campanhas de anúncios por meio da API de Marketing envolve várias operações importantes: modificar as configurações, bem como pausar, retomar e excluir campanhas.


## Modificar uma campanha de anúncios


Para atualizar uma campanha de anúncios existente, você pode enviar uma solicitação `POST` ao ponto de extremidade `/<CAMPAIGN_ID>`. É possível alterar várias configurações, incluindo o objetivo, o orçamento e os atributos de direcionamento da campanha.


**Exemplo de solicitação da API:**

```
curl -X POST \
  https://graph.facebook.com/v25.0/<CAMPAIGN_ID> \
  -F 'objective=CONVERSIONS' \
  -F 'daily_budget=2000' \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>'
```
[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)

## Pausar uma campanha de anúncios


Interromper temporariamente a veiculação pode ajudar você a reavaliar sua estratégia sem excluir a campanha. Para pausar uma campanha, atualize o status dela para `PAUSED`.


**Exemplo de solicitação da API:**

```
curl -X POST \
  https://graph.facebook.com/v25.0/<CAMPAIGN_ID> \
  -F 'status=PAUSED' \
  -F 'access_token=<ACCESS_TOKEN>'
```


Para retomar a campanha, você pode definir o status de volta para `ACTIVE`.
[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)

## Arquivar uma campanha de anúncios


Se quiser interromper temporariamente uma campanha sem excluí-la, use o recurso de arquivamento. Para fazer isso, envie uma solicitação `POST` ao ponto de extremidade `/<CAMPAIGN_ID>` com o parâmetro de status definido como `ARCHIVED`.


**Exemplo de solicitação da API**

```
curl -X POST \
  https://graph.facebook.com/v25.0/<CAMPAIGN_ID> \
  -F 'status=ARCHIVED \
  -F 'access_token=<ACCESS_TOKEN>'
```


Observe que arquivar uma campanha interromperá a veiculação, que poderá ser facilmente restaurada mudando o status de volta para `ACTIVE`.
[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)

## Excluir uma campanha de anúncios


Quando precisar remover permanentemente uma campanha, envie uma solicitação `DELETE` ao o ponto de extremidade `/<CAMPAIGN_ID>`.


Tenha cuidado ao excluir campanhas, já que essa ação não poderá ser desfeita. Verifique sempre a identificação da campanha antes da exclusão para evitar a perda acidental de dados.


**Exemplo de solicitação da API**

```
curl -X DELETE \
  https://graph.facebook.com/v25.0/<CAMPAIGN_ID> \
  -F 'access_token=<ACCESS_TOKEN>'
```
[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)

## Saiba mais


- [Referência sobre campanha](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group)
- [Como gerenciar o status do seu objeto de anúncio](https://developers.facebook.com/docs/marketing-apis/guides/manage-your-ad-object-status)
- [Solução de problemas](https://developers.facebook.com/docs/marketing-api/troubleshooting)
[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)[←VoltarCreate an Ad](https://developers.facebook.com/docs/marketing-api/get-started/basic-ad-creation/create-an-ad)[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)[○](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#)Nesta Página[Gerenciamento de campanhas de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#gerenciamento-de-campanhas-de-an-ncios)[Modificar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#modificar-uma-campanha-de-an-ncios)[Pausar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#pausar-uma-campanha-de-an-ncios)[Arquivar uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#arquivar-uma-campanha-de-an-ncios)[Excluir uma campanha de anúncios](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#excluir-uma-campanha-de-an-ncios)[Saiba mais](https://developers.facebook.com/docs/marketing-api/get-started/manage-campaigns#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_E2KITUFcceaOyRBt6_2v1_8cEi1qXsIiQtDOSRFHq6kzFSDgKR5NAy2Mqw_aem_0mdAz041hLRYEc00LNndkQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7yilOfhlPJBclPpv9ZSLUXUEVFKj1hX4D_cLKGmJorWQRUS4parLjfufcwGA_aem_6f8hnkHejyRWQjgEG9geig&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7g0cBOOyXLtllSjN6fSp1UAPPci86syUlnRPp9YSRS8ZxKb28JplFhcGK2mA_aem_zS3bHV4cflG_y9k1HteHFg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7yilOfhlPJBclPpv9ZSLUXUEVFKj1hX4D_cLKGmJorWQRUS4parLjfufcwGA_aem_6f8hnkHejyRWQjgEG9geig&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7mDiMRZUu0_D2_roI5d1ltvNf4tM60TRW4wU77n71K9tK5WaAVc1f0y8PVRw_aem_QpxcekMeyUZQ8cn-c2dt3g&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mywrXd6IjR-LpqfyX7FwTMzVMR8SbSyBLkj55DZq-eNEg9aMWgiT-jVPCAA_aem_7KVEFotBTBeiuBoN0uv1tg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mywrXd6IjR-LpqfyX7FwTMzVMR8SbSyBLkj55DZq-eNEg9aMWgiT-jVPCAA_aem_7KVEFotBTBeiuBoN0uv1tg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7qbSDvJvYzirFVrmRa_vOmqMYYwUX48tJZA-AEYIlHttKJGqiN6HqzREH1SQ_aem_EvpqhB92UTp2nTflv5MVoQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_E2KITUFcceaOyRBt6_2v1_8cEi1qXsIiQtDOSRFHq6kzFSDgKR5NAy2Mqw_aem_0mdAz041hLRYEc00LNndkQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7g0cBOOyXLtllSjN6fSp1UAPPci86syUlnRPp9YSRS8ZxKb28JplFhcGK2mA_aem_zS3bHV4cflG_y9k1HteHFg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7CekwOHn_FRQDFFzyZLvOh7q_7TSpdu9XBDgk-duRrk-EjkG34eYDWclh1Fw_aem_FNsAdTqhsQgtfPgLaZml8w&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7dx2tf5wQnMAP7s_UDmaxeVT7dwo5dTyBkTiNkjiuJbZL4G7zo5N-yuyGiJA_aem_PKqoEWBQ6zLKzfPYymOiJw&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mywrXd6IjR-LpqfyX7FwTMzVMR8SbSyBLkj55DZq-eNEg9aMWgiT-jVPCAA_aem_7KVEFotBTBeiuBoN0uv1tg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7qbSDvJvYzirFVrmRa_vOmqMYYwUX48tJZA-AEYIlHttKJGqiN6HqzREH1SQ_aem_EvpqhB92UTp2nTflv5MVoQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7dx2tf5wQnMAP7s_UDmaxeVT7dwo5dTyBkTiNkjiuJbZL4G7zo5N-yuyGiJA_aem_PKqoEWBQ6zLKzfPYymOiJw&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4mywrXd6IjR-LpqfyX7FwTMzVMR8SbSyBLkj55DZq-eNEg9aMWgiT-jVPCAA_aem_7KVEFotBTBeiuBoN0uv1tg&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6_E2KITUFcceaOyRBt6_2v1_8cEi1qXsIiQtDOSRFHq6kzFSDgKR5NAy2Mqw_aem_0mdAz041hLRYEc00LNndkQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7yilOfhlPJBclPpv9ZSLUXUEVFKj1hX4D_cLKGmJorWQRUS4parLjfufcwGA_aem_6f8hnkHejyRWQjgEG9geig&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7qbSDvJvYzirFVrmRa_vOmqMYYwUX48tJZA-AEYIlHttKJGqiN6HqzREH1SQ_aem_EvpqhB92UTp2nTflv5MVoQ&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7dx2tf5wQnMAP7s_UDmaxeVT7dwo5dTyBkTiNkjiuJbZL4G7zo5N-yuyGiJA_aem_PKqoEWBQ6zLKzfPYymOiJw&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7RWG3IbaZhOvN2R4VgX4eTKkhHfYMrH_HSjyaz4rzEAngJj3mbNTVJlMeu5SpP2crsmWzUNvndoYGEEpqC4-ZHGqDWfsbbTv-MsXvoxfnfPy76E9lSN7msbbY_9vqUuzOlRmqKxRtsSkRvXLrY6q8ZaNA)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão