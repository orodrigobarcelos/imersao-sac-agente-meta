<!-- Fonte: Recursos de IA generativa - API de Marketing.html -->
<!-- URL: https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features -->
<!-- API: v25.0 | Data: 2026-03-30 -->

# Comece a usar os recursos de IA generativa na API de Marketing


**Suporte da API para recursos de IA generativa**


Os anunciantes são responsáveis por pré-visualizar os conteúdos de criativos de anúncio gerados por IA antes de publicarem seus anúncios. Veja as instruções para configurar uma prévia.


A Meta não faz nenhuma garantia quanto a completude, confiabilidade e precisão das gerações de texto sugeridas nem quanto aos planos de fundo gerados ou às imagens expandidas. Se você usa a API de marketing para acessar nossos recursos de IA generativa descritos abaixo, os [Termos de IA generativa de criativo do anúncio](https://www.facebook.com/legal/terms/ad_creative_generative_ai_terms) se aplicam, além dos [Termos da Plataforma Meta](https://developers.facebook.com/terms/dfc_platform_terms/).


Este documento mostra como usar recursos de IA generativa para [geração de texto](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#text-generation), [expansão de imagem](https://developers.facebook.com/docs/marketing-api/creative/image-expansion) e [geração de plano de fundo](https://developers.facebook.com/docs/marketing-api/creative/background-generation) para anúncios.


## Antes de começar


É necessário executar as etapas a seguir para configurar suas campanhas de anúncios com os recursos de IA generativa da Meta.


- [Criar uma campanha](https://developers.facebook.com/docs/marketing-apis/get-started/#campaign)
- [Criar um conjunto de anúncios](https://developers.facebook.com/docs/marketing-apis/get-started/#ad-set-budget)
- [Criar o anúncio ou um criativo independente](https://developers.facebook.com/docs/marketing-apis/get-started/#ad-creative)
- [Ver uma prévia do criativo](https://developers.facebook.com/docs/marketing-api/creative#previews)
- [Habilitar o anúncio](https://developers.facebook.com/docs/marketing-apis/get-started/#book-ad)


## Geração de texto


As variações de texto são geradas com IA inspirada no seu texto principal original, nos seus anúncios anteriores ou nos conteúdos da sua Página comercial, para ajudar a fazer sugestões mais relevantes. Adicionar mais opções de texto ao seu anúncio pode ajudar a personalizar seu criativo e a reduzir a fadiga do criativo, o que pode ajudar a aumentar o desempenho. [Saiba mais sobre esse recurso aqui](https://www.facebook.com/business/help/497610041230617).


### Etapa 1: opte por usar a geração de texto ao criar o anúncio


Você pode criar um anúncio através do ponto de extremidade `/ads` ou criar um criativo independente através do ponto de extremidade `/adcreatives`. Optar por usar o recurso aplica-se apenas ao anúncio ou criativo criado na solicitação atual. Em qualquer abordagem, opte por usar o recurso Geração de Texto da seguinte forma:


- Fornecendo um texto principal no campo `message` no `object_story_spec`
- Optando por usar `text_generation`


Veja exemplos de solicitações abaixo:


#### Aceite através do ponto de extremidade `/adcreatives`


```
curl -X POST \
  -F 'name=Text Gen Creative' \
  -F 'object_story_spec={
      "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<URL>",
         "message": "<PRIMARY_TEXT_HERE>",  <--- Primary Text Here
      },
      "page_id": "<PAGE_ID>"
  }' \
  -F 'degrees_of_freedom_spec={
    "creative_features_spec": {
      "text_generation": {
        "enroll_status": "OPT_IN"
      }
    }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


Ou você pode criar um objeto de anúncio com o ponto de extremidade `act_<AD_ACCOUNT_ID>/ads`:


#### Aceite através do ponto de extremidade `/ads`


```
curl \
  -F 'adset_id=<ADSET_ID>' \
  -F 'creative={
    "name": "Text Gen Adgroup",
    "object_story_spec": {
      "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<URL>",
         "message": "<PRIMARY_TEXT_HERE>",  <--- Primary Text Here
      },
      "page_id": "<PAGE_ID>"
    },
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "text_generation": {
          "enroll_status": "OPT_IN"
        }
      }
    }
  }' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Etapa 2: veja uma prévia para Geração de Texto


Quando um anúncio é criado com a opção de usar `text_generation`, o recurso será aplicado apenas ao anúncio atual, e os textos principais gerados serão inseridos na especificação do criativo. Se o recurso tiver sido aceito pelo ponto de extremidade `/ads`, o campo `status` no grupo de anúncios será definido como `PAUSED` por padrão ([consulte a documentação](https://developers.facebook.com/docs/marketing-api/reference/adgroup)). Você pode analisar as sugestões geradas antes, definindo manualmente o status do anúncio como `ACTIVE` para que ele possa ser entregue.


A especificação do criativo contendo sugestões geradas pode ser vista previamente, lendo a `asset_feed_spec` na identificação do criativo ou na identificação do anúncio. Veja o exemplo de solicitação e resposta abaixo:


Comece consultando `asset_feed_spec` do seu criativo do anúncio independente criado na etapa 1.


#### Solicitação


```
// request from creative
curl -X GET -G \
  -d 'fields=asset_feed_spec' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<CREATIVE_ID>

// request from ad
curl -X GET -G \
  -d 'fields=creative{asset_feed_spec,status}' \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_ID>
```


#### Resposta


```
{
  "asset_feed_spec": {
    "bodies": [
      {
        "text": "Buy some cool LED TV at cheap price"
      },
      {
        "text": "Get your dream LED TV at an unbeatable price! Buy now and save big!"
      },
      {
        "text": "Get the best LED TV deals! 📺 Save money and upgrade your entertainment."
      },
      {
        "text": "Get an LED TV at a low cost! Cheap, high-quality options are available."
      },
      {
        "text": "Get LED TVs at affordable prices  ✨  !"
      }
    ],
    "optimization_type": "DEGREES_OF_FREEDOM"
  },
  "id": "<CREATIVE_ID>"
}
```


**Depois que as sugestões tiverem sido analisadas e forem aceitáveis para publicação, vá para a etapa 3, para definir o anúncio como `ACTIVE`. Se alguma das sugestões geradas não for aceitável, [crie um novo anúncio ou criativo](https://developers.facebook.com/docs/marketing-apis/get-started/#ad-creative) sem ativar a Geração de Texto.**


#### Crie o criativo sem ativar a geração de texto


```
curl -X POST \
  -F 'name=Text Gen Creative' \
  -F 'object_story_spec={
      "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<URL>",
         "message": "<PRIMARY_TEXT_HERE>",
      },
      "page_id": "<PAGE_ID>"
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives
```


### Etapa 3: configure o status do grupo de anúncios como `ACTIVE`


Depois de ter verificado as sugestões de texto gerado, você pode definir o `status` do anúncio como `ACTIVE`. Esta etapa precisa ser realizada em ambos os casos:


- Quando um anúncio é ativado para o recurso pelo ponto de extremidade `/ads`
- Se o anúncio for o primeiro a usar um criativo existente com ativação da geração de texto.


#### Solicitação


```
curl \
  -F 'status=ACTIVE' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/<AD_ID>
```
[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)

## Expansão de imagem


Expanda automaticamente sua imagem para caber em mais posicionamentos.


### Etapa 1: crie um anúncio ou criativo que optou pela expansão de imagem


Você pode criar um anúncio através do ponto de extremidade `/ads` ou criar um criativo independente através do ponto de extremidade `/adcreatives`. Em qualquer das abordagens, opte por usar o recurso Expansão de Imagem na especificação do criativo (veja exemplos abaixo).


#### Solicitação


```
// creative example
curl -X POST \
  -F 'name=Image Expansion Creative' \
  -F 'degrees_of_freedom_spec={
    "creative_features_spec": {
      "image_uncrop": {
        "enroll_status": "OPT_IN"
      }
    }
  }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives

// ad example
curl \
  -F 'adset_id=<ADSET_ID>' \
  -F 'creative={
    "name": "Image Expansion Adgroup",
    "object_story_spec": {
      "link_data": {
         "image_hash": "<IMAGE_HASH>",
         "link": "<URL>",
         "message": "You got this.",
      },
      "page_id": "<PAGE_ID>"
    },
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "image_uncrop": {
          "enroll_status": "OPT_IN"
        }
      }
    }
  }' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Etapa 2: veja uma prévia para Expansão de Imagem


Este recurso é aceito para posicionamentos `INSTAGRAM_STANDARD`, `FACEBOOK_REELS_MOBILE`, `INSTAGRAM_REELS`, `MOBILE_FEED_STANDARD`, `INSTGRAM_STORY`. Para ver uma prévia desses posicionamentos, faça uma solicitação `GET` para o ponto de extremidade `/<AD_ID>/previews`.


**Se alguma das imagens geradas não for aceitável, recrie o anúncio ou criativo sem ativar a Expansão de Imagem:**


- Defina o `creative_feature` como `image_uncrop`.
- Solicite a prévia novamente se o `status` for exibido como `pending`.


**Nota:** se um nó `transformation_spec` não for exibido, significa que o criativo não é qualificado para expansão de imagem.


#### Solicitação


`INSTAGRAM_STANDARD`

```
curl -X GET -G \
  -d 'ad_format=INSTAGRAM_STANDARD' \
  -d 'creative_feature=image_uncrop' \
  -d 'access_token=/<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/<AD_ID>/previews
```


`FACEBOOK_REELS_MOBILE`

```
curl -X GET -G \
  -d 'ad_format=FACEBOOK_REELS_MOBILE' \
  -d 'creative_feature=image_uncrop' \
  -d 'access_token=/<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/<AD_ID>/previews
```


#### Resposta


```
{
  "data": [
    {
      "body": "<iframe src='<PREVIEW_URL>'></iframe>",
      "transformation_spec": {
        "image_uncrop": [
          {
            "body": "<iframe src='<PREVIEW_URL>'></iframe>",
            "status": "eligible"
          }
        ]
      }
    }
  ]
}
```


### (Opcional) Prévia direta sem criação de anúncio


Você também pode solicitar uma prévia usando o ponto de extremidade `act_<AD_ACCOUNT_ID>/generatepreviews` sem, de fato, criar um anúncio.


#### Solicitação


`FACEBOOK_REELS_MOBILE`

```
curl -X GET -G \
  -d 'ad_format=FACEBOOK_REELS_MOBILE' \
  -d 'creative_feature=image_uncrop' \
  -d 'creative={
       "object_story_spec": {
         "page_id": "<PAGE_ID>",
          "link_data": {
            "image_hash": "<IMAGE_HASH>",
            "link": "<WEBSITE_LINK>"
          }
        }
     }'
  -d 'access_token=<ACCESS_TOKEN>'
  https://graph.facebook.com/v19.0/act_<AD_ACCOUNT_ID>/generatepreviews
```
[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)

## Geração de plano de fundo


Vamos criar planos de fundo diferentes para imagens de produtos qualificados e apresentar a versão à qual seu público tem maior probabilidade de responder. Esses planos foram criados com base no seu ativo original.


### Etapa 1: crie um anúncio ou criativo com geração de plano de fundo


Atualmente, a geração de plano de fundo funciona apenas com anúncios dinâmicos de produtos ou anúncios de catálogo Advantage+ no feed para celular.


Você pode criar um anúncio através do ponto de extremidade `/ads` ou criar um criativo independente através do ponto de extremidade `/adcreatives`. Em qualquer das abordagens, opte por usar o recurso Geração de Plano de Fundo na especificação do criativo (veja exemplos abaixo).


#### Solicitação


```
// creative example
  curl -X POST \
  -F 'name=Background Gen Creative' \
  -F 'degrees_of_freedom_spec={
    "creative_features_spec": {
      "image_background_gen": {
        "enroll_status": "OPT_IN"
      }
    }
  }' \
  -F 'product_set_id=<PRODUCT_SET_ID>'
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/adcreatives

// ad example
curl \
  -F 'adset_id=<ADSET_ID>' \
  -F 'creative={
    "name": "Background Gen Adgroup",
    "object_story_spec": {
      "page_id": "<PAGE_ID>",
      "template_data": {
        "description": "Description {{product.description}} ",
        "link": "https://www.example.com/",
        "message": "Test {{product.name | titleize}} ",
        "name": "Headline {{product.price}}"
      }
    },
    "product_set_id": "<PRODUCT_SET_ID>",
    "degrees_of_freedom_spec": {
      "creative_features_spec": {
        "image_background_gen": {
          "enroll_status": "OPT_IN"
        }
      }
    }
  }' \
https://graph.facebook.com/v25.0/act_<AD_ACCOUNT_ID>/ads
```


### Etapa 2: veja uma prévia para Geração de Plano de Fundo


Ao optar pelo recurso, criaremos diferentes planos de fundo para imagens de produtos qualificadas e veicularemos a versão à qual seu público tem mais probabilidade de responder. Só é possível optar pelo recurso para o anúncio criado na solicitação atual. Estes planos de fundo são criados com base no seu ativo original, apresentando diferentes cores ou padrões para imagens de produtos elegíveis. Você verá uma prévia estática ou ao vivo do seu plano de fundo gerado, dependendo da elegibilidade do catálogo.


**Se algum dos planos de fundo gerados não for aceitável, crie novamente o anúncio ou criativo sem ativar a Geração de Plano de Fundo.**


- A prévia é atualmente aceita somente no posicionamento `MOBILE_FEED_STANDARD`
- Defina o `creative_feature` como `image_background_gen`
- Se a prévia ao vivo dos produtos do seu catálogo não estiver pronta, uma prévia do estoque será exibida com `status` definido como `PENDING`


#### Solicitação


`MOBILE_FEED_STANDARD`

```
curl -X GET -G \
  -d 'ad_format=MOBILE_FEED_STANDARD' \
  -d 'creative_feature=image_background_gen' \
  -d 'access_token=/<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/<AD_ID>/previews
```


#### Resposta


```
{
  "data": [
    {
      "body": "<iframe src='<PREVIEW_URL>'></iframe>",
      "transformation_spec": {
        "image_background_gen": [
          {
            "body": "<iframe src='<PREVIEW_URL>'></iframe>",
            "status": "eligible" // or one of "pending", "ineligible"
          }
        ]
      }
    }
  ]
}
```


### (Opcional) Prévia direta sem criação de anúncio


Você também pode solicitar uma prévia de um criativo usando o ponto de extremidade `/<AD_CREATIVE_ID>/previews` sem, de fato, criar um anúncio.


#### Solicitação


`MOBILE_FEED_STANDARD`

```
curl -X GET -G \
  -d 'ad_format=MOBILE_FEED_STANDARD' \
  -d 'creative_feature=image_background_gen' \
  -d 'access_token=<ACCESS_TOKEN>'
  https://graph.facebook.com/v19.0/<AD_CREATIVE_ID>/generatepreviews
```


#### Resposta


```
{
  "data": [
    {
      "body": "<iframe src='<PREVIEW_URL>'></iframe>",
      "transformation_spec": {
        "image_background_gen": [
          {
            "body": "<iframe src='<PREVIEW_URL>'></iframe>",
            "status": "eligible" // or one of "pending", "ineligible"
          }
        ]
      }
    }
  ]
}
```
[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)

## Sobre a transparência da IA


Imagens de anúncios criadas ou editadas materialmente com determinados recursos de criativo de IA generativa da Meta disponíveis nas nossas ferramentas de marketing podem incluir informações de IA no menu de três pontos de um anúncio ou ter uma etiqueta de informação de IA ao lado da etiqueta Patrocinado. Consulte [Transparência dos anúncios de IA generativa](https://www.facebook.com/business/help/539137881899016).
[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)

## Saiba mais


- [Criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)
- [Grupo de anúncios](https://developers.facebook.com/docs/marketing-api/reference/adgroup/)
- [Especificação para story do objeto de criativo do anúncio](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-object-story-spec/)
- [Recursos de IA generativa para anúncios](https://www.facebook.com/business/news/generative-ai-features-for-ads-coming-to-all-advertisers)
[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)[○](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#)Nesta Página[Comece a usar os recursos de IA generativa na API de Marketing](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#comece-a-usar-os-recursos-de-ia-generativa-na-api-de-marketing)[Antes de começar](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#antes-de-come-ar)[Geração de texto](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#gera--o-de-texto)[Etapa 1: opte por usar a geração de texto ao criar o anúncio](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-1--opte-por-usar-a-gera--o-de-texto-ao-criar-o-an-ncio)[Etapa 2: veja uma prévia para Geração de Texto](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-2--veja-uma-pr-via-para-gera--o-de-texto)[Etapa 3: configure o status do grupo de anúncios como ACTIVE](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-3--configure-o-status-do-grupo-de-an-ncios-como-active)[Expansão de imagem](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#expans-o-de-imagem)[Etapa 1: crie um anúncio ou criativo que optou pela expansão de imagem](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-1--crie-um-an-ncio-ou-criativo-que-optou-pela-expans-o-de-imagem)[Etapa 2: veja uma prévia para Expansão de Imagem](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-2--veja-uma-pr-via-para-expans-o-de-imagem)[(Opcional) Prévia direta sem criação de anúncio](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#-opcional--pr-via-direta-sem-cria--o-de-an-ncio)[Geração de plano de fundo](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#gera--o-de-plano-de-fundo)[Etapa 1: crie um anúncio ou criativo com geração de plano de fundo](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-1--crie-um-an-ncio-ou-criativo-com-gera--o-de-plano-de-fundo)[Etapa 2: veja uma prévia para Geração de Plano de Fundo](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#etapa-2--veja-uma-pr-via-para-gera--o-de-plano-de-fundo)[(Opcional) Prévia direta sem criação de anúncio](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#-opcional--pr-via-direta-sem-cria--o-de-an-ncio-2)[Sobre a transparência da IA](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#sobre-a-transpar-ncia-da-ia)[Saiba mais](https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features#saiba-mais) react-mount-point-unstable Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Vav8gZRA3Mphd1rsbuM1iHWj77iDpUbpDNzjwJceZHaJWwg6SdiG7ISht4Q_aem_BqI8Hs_ADf66uZX8JbJnJw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zW3LfMXthDn0FqAFUmjB9uu1Yw7MPowsuIxlQWe-6y-NrFtg-ccCouIS5JQ_aem_Kms3GbADCn6FzJrJsq6RFw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l-9EhTrzzZafikC9V8Zibuq5h80zF28r1y4UrWFLYLfJ6113Ifhn4MbXhCQ_aem_zTCfMFyt292FnCvEDPNQyw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66wqQ7pJ14AfCzF4McEb4kAlEwAvB1IfOETa8NyE11I3PCUWLiZyqjXRumgQ_aem_VEtiAPU6GVlXMOXMjYHFLQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ub0-x3qrhC-dZq4aGrfR3L9QrO9xjqrPJqlGfCWXSKVw_I6vjyhaVnv6yAw_aem_wwYBbFlt5NMrTUykWxU_xQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Careers](https://www.facebook.com/careers)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7l-9EhTrzzZafikC9V8Zibuq5h80zF28r1y4UrWFLYLfJ6113Ifhn4MbXhCQ_aem_zTCfMFyt292FnCvEDPNQyw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6v3pvGHKK4NJhw5EvM2_g_gwPgpCXsklYtWzU4sp1ZGbvym6D1mi9HDJ4jXw_aem_lp94KmQFiZ4tzHv6aFAhDg&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6ZXDyTFUlfzdbcsO7ktTpkLIn92K09rBuuW7LDVd9sIokhp0nDPfntTGGHYg_aem_KlLHrir04dqS-AEJIFm9Ug&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ttm-HW0KSezc4T4Ig_Gl-zkmbzNkTDEHK2zkN4fYoFm5S3cHemebpMK1g7A_aem_YYRvBs32S_IDMUD57R3cNA&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zW3LfMXthDn0FqAFUmjB9uu1Yw7MPowsuIxlQWe-6y-NrFtg-ccCouIS5JQ_aem_Kms3GbADCn6FzJrJsq6RFw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR4zW3LfMXthDn0FqAFUmjB9uu1Yw7MPowsuIxlQWe-6y-NrFtg-ccCouIS5JQ_aem_Kms3GbADCn6FzJrJsq6RFw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Vav8gZRA3Mphd1rsbuM1iHWj77iDpUbpDNzjwJceZHaJWwg6SdiG7ISht4Q_aem_BqI8Hs_ADf66uZX8JbJnJw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6v3pvGHKK4NJhw5EvM2_g_gwPgpCXsklYtWzU4sp1ZGbvym6D1mi9HDJ4jXw_aem_lp94KmQFiZ4tzHv6aFAhDg&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7FE1pCqDGgDhbFR9Laj_o8nZxd9QIAkdGcSaQh6JbugZounm8iWt7F1cfreg_aem_Hg2E-a-qTdUyuxout_4TcQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR7ttm-HW0KSezc4T4Ig_Gl-zkmbzNkTDEHK2zkN4fYoFm5S3cHemebpMK1g7A_aem_YYRvBs32S_IDMUD57R3cNA&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)Build with Meta[AI](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.llama.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR66wqQ7pJ14AfCzF4McEb4kAlEwAvB1IfOETa8NyE11I3PCUWLiZyqjXRumgQ_aem_VEtiAPU6GVlXMOXMjYHFLQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Meta Horizon](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fhorizon%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Vav8gZRA3Mphd1rsbuM1iHWj77iDpUbpDNzjwJceZHaJWwg6SdiG7ISht4Q_aem_BqI8Hs_ADf66uZX8JbJnJw&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Social technologies](https://developers.facebook.com/social-technologies/)[Wearables](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fwearables%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6v3pvGHKK4NJhw5EvM2_g_gwPgpCXsklYtWzU4sp1ZGbvym6D1mi9HDJ4jXw_aem_lp94KmQFiZ4tzHv6aFAhDg&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)News[Meta for Developers](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevelopers.meta.com%2Fblog%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR6Ub0-x3qrhC-dZq4aGrfR3L9QrO9xjqrPJqlGfCWXSKVw_I6vjyhaVnv6yAw_aem_wwYBbFlt5NMrTUykWxU_xQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Blog](https://developers.facebook.com/blog/)[Success stories](https://developers.facebook.com/success-stories/)Support[Developer Support](https://developers.facebook.com/support/)[Bug tool](https://developers.facebook.com/support/bugs/)[Platform status](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAYnJpZBExczI3SHZlNGdvMmlHblBZYnNydGMGYXBwX2lkATAAAR5p4eAoiv0-7SBeG8QLTv_3WxXa6qTiIaMeoRI0wo1meBHQ_nE5hp7IVeqNwg_aem_yW4w2JDXZg7GkNh9Sq5MXQ&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Developer community forum](https://www.facebook.com/groups/fbdevelopers/)[Report an incident](https://developers.facebook.com/incident/report/)About us[About](https://l.facebook.com/l.php?u=https%3A%2F%2Fabout.fb.com%2F&h=AT7XNxIaAYPsF5escexXqnWM_jTYg-EcBrxshQvOM6yal_PmbrItAq98fmotRYl_T3j1jw1JBY239oHU3f9V5nfiholM4csE8ZjMfI55mhW7Gv7_dAfpjca0zEH1S8Ge89e0rZhAzvP8V9gS48e5mXXRHKc)[Careers](https://www.facebook.com/careers)Terms and policies[Responsible platform initiatives](https://developers.facebook.com/products/responsible-platform-initiatives/)[Platform terms](https://developers.facebook.com/terms/dfc_platform_terms/)[Developer policies](https://developers.facebook.com/devpolicy/)[Privacy policy](https://www.facebook.com/about/privacy)[Cookies](https://www.facebook.com/help/cookies)English (US) react-mount-point-unstable Este documento foi útil?SimNão