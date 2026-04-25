<!-- Fonte: Programação avançada - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/ad-rules/guides/advanced-scheduling -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Programação avançada


Esse documento fornece exemplos detalhados de `schedule_type` definido como `CUSTOM`.


Conforme mencionado na [documentação principal](https://developers.facebook.com/docs/marketing-api/ad-rules/overview/scheduled-based-rules):


Se `schedule_type` for definido como `CUSTOM`, também será necessário especificar a lista de períodos personalizados em que a regra deve ser executada. Na lista `schedule`, cada especificação individual pode ser composta por uma combinação dos campos a seguir, sendo obrigatória a inclusão de ao menos `start_minute` ou `days` em cada entrada.


| Campo | Descrição |
| --- | --- |
| start_minute | Horário, em minutos, após às 12 h. Deve ser um múltiplo de 30 minutos. Quando isso é definido e não há end_minute , essa opção determina o horário exato de execução da regra. Caso contrário, end_minute será usado para determinar uma faixa de tempo para executar a regra. Se essa opção não estiver definida, a regra será executada SEMI_HOURLY para cada dia especificado em days . |
| end_minute | Horário, em minutos, após às 12 h. Deve ser múltiplo de 30 minutos e ser posterior a start_minute . Se definida, essa opção usa start_minute para determinar a faixa de tempo para executar a regra. Se end_minute for igual a start_minute , essa opção determinará o horário exato de execução da regra. |
| days | Lista de dias para executar a regra. Cada dia deve conter um valor de 0-6 , em que 0 representa domingo, 1 , representa segunda-feira, e assim por diante, com 6 , por fim, representando sábado. Se essa opção não estiver definida, a regra será executada em todos os 7 dias da semana de acordo com start_minute e end_minute , se houver. |


Veja um exemplo de uso da Programação avançada para programar a regra para ser executada todos os dias às 10h. Ao omitir `days`, infere-se que essa especificação de programação será aplicada todos os dias.

```
curl \
-F 'name=Test Advanced Scheduling Rule' \
-F 'schedule_spec={
     "schedule_type": "CUSTOM",
     "schedule": [
       {
         "start_minute": 600,
       }
     ]
   }' \
-F 'evaluation_spec={
     ...
   }' \
-F 'execution_spec={
     ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


## Exemplo


Veja um exemplo de uma regra que é executada a cada 30 minutos somente nos finais de semana. Ao omitir `start_minute`, infere-se que a regra será executada como `SEMI_HOURLY` nos dias especificados.

```
curl \
-F 'name=Test Advanced Scheduling Rule' \
-F 'schedule_spec={
     "schedule_type": "CUSTOM",
     "schedule": [
       {
         "days": [0, 6]
       }
     ]
   }' \
-F 'evaluation_spec={
     ...
   }' \
-F 'execution_spec={
     ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Veja um exemplo de uma regra que é executada somente nas quartas-feiras às 2h. Ao omitir `end_minute`, infere-se que a regra só é executada em um horário específico, em vez de em uma faixa de tempo.

```
curl \
-F 'name=Test Advanced Scheduling Rule' \
-F 'schedule_spec={
     "schedule_type": "CUSTOM",
     "schedule": [
       {
         "start_minute": 120,
         "days": [3]
       }
     ]
   }' \
-F 'evaluation_spec={
     ...
   }' \
-F 'execution_spec={
     ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Cada programação individual é calculada de maneira independente como uma OR com as outras programações. Veja um exemplo de uma regra executada o dia inteiro em dias da semana, mas somente das 12h às 13h nos finais de semana. Como há `end_minute` aqui, a faixa de tempo vai de `start_minute` até `end_minute`.

```
curl \
-F 'name=Test Advanced Scheduling Rule' \
-F 'schedule_spec={
     "schedule_type": "CUSTOM",
     "schedule": [
       {
         "days": [1, 2, 3, 4, 5]
       },
       {
         "start_minute": 720,
         "end_minute": 780,
         "days": [0, 6]
       }
     ]
   }' \
-F 'evaluation_spec={
     ...
   }' \
-F 'execution_spec={
     ...
   }' \
-F "access_token=<ACCESS_TOKEN>" \
https://graph.facebook.com/<VERSION>/<AD_ACCOUNT_ID>/adrules_library
```


Observe que não especificar `days` na segunda programação funcionará de maneira equivalente, pois a primeira especificação inclui a faixa das 12h às 13h em dias de semana.
[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/advanced-scheduling#)[○](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/advanced-scheduling#)Nesta Página[Programação avançada](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/advanced-scheduling#programa--o-avan-ada)[Exemplo](https://developers.facebook.com/docs/marketing-api/ad-rules/guides/advanced-scheduling#exemplo) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_MjpgNvyvJ7fsWkODhNCLd-JOwhA3-5ziLhm5oQeWNb5w3BL25c8A-i-QcA_aem_S7_wInG8EYm2Arze0SUfPQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47e-q-D2SzTdqCxbQmvTmJunpgwbr7wvX60pz2N-Qcq3lvRbMhbSrOrhm4hg_aem_F9vlHr_wgxzuSKopuGWXhQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_MjpgNvyvJ7fsWkODhNCLd-JOwhA3-5ziLhm5oQeWNb5w3BL25c8A-i-QcA_aem_S7_wInG8EYm2Arze0SUfPQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6T-lcxRSBZDWx2qlClGLKc3XKQDi8LjCbaStVMagD2E046BtpCV8TZXIONJQ_aem_RE3kC575rFaWA_iEJx0s1Q&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4rwGXLgaO-blVLNEfEu5TGhh8rovi1NgX-A732Ll8WboVnf8hPv9G5abI1pw_aem_qz-21hykCoeVNatiAHfpGw&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4pG18x_n-Nbr6y6ro-KXYlqxLl0xQMtRUIi_FuFKtx6G0cgg804UcTmi-JAA_aem_bJ1TRtpoNK54i9vPmr5Ang&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uC1epivZAxiZ_IH9anIWkkGFdYhtXh3-PL7yT4CPDe9U-1zykm5kS3O0Nyg_aem_GR5b50Us-z4V_ST7_wl7Ew&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6T-lcxRSBZDWx2qlClGLKc3XKQDi8LjCbaStVMagD2E046BtpCV8TZXIONJQ_aem_RE3kC575rFaWA_iEJx0s1Q&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR47e-q-D2SzTdqCxbQmvTmJunpgwbr7wvX60pz2N-Qcq3lvRbMhbSrOrhm4hg_aem_F9vlHr_wgxzuSKopuGWXhQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Im_0BAAxVWpSDaPNXH2Jq5pdcJR9ex-Ok__rMn85uBk6MctOml6YGk_5PWw_aem_xbT9aPDP14DC-E1oW_wkvA&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6UbBDXSpogQBAEQoy-wpwTINVdWZ1wclSBLYujm53Iy9n7GIA4gEN3enGr1g_aem_r06HukPdTNfDUkl8tTArhQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4rwGXLgaO-blVLNEfEu5TGhh8rovi1NgX-A732Ll8WboVnf8hPv9G5abI1pw_aem_qz-21hykCoeVNatiAHfpGw&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5uC1epivZAxiZ_IH9anIWkkGFdYhtXh3-PL7yT4CPDe9U-1zykm5kS3O0Nyg_aem_GR5b50Us-z4V_ST7_wl7Ew&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4pG18x_n-Nbr6y6ro-KXYlqxLl0xQMtRUIi_FuFKtx6G0cgg804UcTmi-JAA_aem_bJ1TRtpoNK54i9vPmr5Ang&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6T-lcxRSBZDWx2qlClGLKc3XKQDi8LjCbaStVMagD2E046BtpCV8TZXIONJQ_aem_RE3kC575rFaWA_iEJx0s1Q&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6T-lcxRSBZDWx2qlClGLKc3XKQDi8LjCbaStVMagD2E046BtpCV8TZXIONJQ_aem_RE3kC575rFaWA_iEJx0s1Q&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_MjpgNvyvJ7fsWkODhNCLd-JOwhA3-5ziLhm5oQeWNb5w3BL25c8A-i-QcA_aem_S7_wInG8EYm2Arze0SUfPQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4XnMJjOtBySgcue8T1uEI-R39JSqgisBt_KnhklPMYNEOfmWj4lVnnihsBUg_aem_FzvU9Yz139rXR9Bz3JY_uw&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4_MjpgNvyvJ7fsWkODhNCLd-JOwhA3-5ziLhm5oQeWNb5w3BL25c8A-i-QcA_aem_S7_wInG8EYm2Arze0SUfPQ&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6T-lcxRSBZDWx2qlClGLKc3XKQDi8LjCbaStVMagD2E046BtpCV8TZXIONJQ_aem_RE3kC575rFaWA_iEJx0s1Q&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT6DDLVKqKOLGZEXQZ8FDEP-jIVdyJcd2DcFeB332VnI_cpoEPYJgvM5-0AyDZM_cqsnsjCcTWHBmXHKs17VKNOWQY_ShQ8mwljFwVAI8RAICsX2PG3GkFz1zhvKE3tKjxxMR2BQXR8BMSyMkiitgbgO3e8)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão