<workflow name="upload-midia">

<when_to_use>
Use este workflow quando o usuario quiser:
- Enviar uma imagem para usar em anuncios depois
- Enviar um video para usar em anuncios depois
- Subir midia para a conta de anuncios sem criar criativo imediatamente
- Preparar arquivos de midia para campanhas futuras

Keywords de ativacao: upload, enviar imagem, enviar video, subir foto, subir video, carregar imagem, carregar video, enviar arquivo, mandar imagem, mandar video, midia.
</when_to_use>

<user_mode>
- Iniciante (padrao): explicar o processo de upload, orientar sobre formatos e tamanhos recomendados, guiar passo a passo.
- Avancado: aceitar comandos diretos como "upload imagem na conta act_XXX" e executar sem perguntas intermediarias.
- Deteccao automatica: se o usuario ja enviou um arquivo pelo chat, identificar automaticamente se e imagem ou video e prosseguir.
</user_mode>

<steps>

<step number="1" name="Tipo de midia">
<question>Voce quer enviar uma imagem ou um video?</question>
<options>
  <option value="imagem">Imagem -- foto ou arte para usar em anuncios (JPG, PNG)</option>
  <option value="video">Video -- video para usar em anuncios (MP4)</option>
</options>
<if_unknown>Se o usuario ja enviou o arquivo pelo chat, detectar automaticamente pelo tipo e pular esta pergunta.</if_unknown>
</step>

<step number="2" name="Upload de imagem">

<step number="2.1" name="Orientacao de formato">
Antes de pedir o arquivo, orientar:

Para melhores resultados, sua imagem deve seguir estas recomendacoes:

Formatos aceitos: JPG, PNG
Tamanhos recomendados:
  - Feed (quadrado): 1080 x 1080 pixels
  - Feed (vertical): 1080 x 1350 pixels -- recomendado, ocupa mais espaco na tela
  - Stories/Reels: 1080 x 1920 pixels
  - Tamanho maximo: 30 MB

Dicas:
  - Use imagens com pouco texto (a Meta penaliza imagens com muito texto)
  - Cores vibrantes e alto contraste chamam mais atencao
  - Rostos humanos geram mais engajamento
</step>

<step number="2.2" name="Solicitar o arquivo">
Pedir: "Envie a imagem pelo chat clicando no icone de anexo (clipe de papel) na barra de mensagem."

NOTA TECNICA: O upload real e feito pelo frontend via endpoint `/api/mcp/upload`. O LLM deve instruir o usuario a anexar o arquivo pelo icone de clipe no chat. O frontend detecta o arquivo e faz o upload automaticamente.
</step>

<step number="2.3" name="Executar upload de imagem">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
</fills>

O arquivo e enviado automaticamente pelo frontend junto com a chamada da tool.

Apos upload com sucesso, mostrar:

Imagem enviada com sucesso!

Hash da imagem: [image_hash]

Guarde esse hash! Voce vai precisar dele para criar anuncios com essa imagem.
Quando for criar um criativo, informe esse hash e eu uso automaticamente.

Guardar: image_hash (para referencia futura na conversa)
</step>

</step>

<step number="3" name="Upload de video">

<step number="3.1" name="Orientacao de formato">
Antes de pedir o arquivo, orientar:

Para melhores resultados, seu video deve seguir estas recomendacoes:

Formato aceito: MP4
Tamanhos recomendados:
  - Feed (quadrado): 1080 x 1080 pixels (1:1)
  - Feed (vertical): 1080 x 1350 pixels (4:5)
  - Stories/Reels (vertical): 1080 x 1920 pixels (9:16) -- recomendado para Reels
  - Tamanho maximo: 4 GB (recomendado: ate 1 GB para upload mais rapido)

Duracao:
  - Feed: ate 240 minutos (recomendado: 15 a 60 segundos)
  - Stories: ate 60 segundos (recomendado: 15 segundos)
  - Reels: ate 90 segundos (recomendado: 15 a 30 segundos)

Dicas:
  - Os 3 primeiros segundos sao os mais importantes -- capture a atencao imediatamente
  - Inclua legendas (muitas pessoas assistem sem som)
  - Videos curtos (ate 15 segundos) costumam ter melhor custo por resultado
</step>

<step number="3.2" name="Solicitar o arquivo">
Pedir: "Envie o video pelo chat clicando no icone de anexo (clipe de papel) na barra de mensagem."

NOTA TECNICA: O upload real e feito pelo frontend via endpoint `/api/mcp/upload` usando upload chunked (resumable). Para videos grandes, o frontend divide o arquivo em partes e envia de forma progressiva. O LLM deve instruir o usuario a anexar o arquivo pelo icone de clipe no chat.
</step>

<step number="3.3" name="Informacoes opcionais">
<question>Quer dar um titulo para o video? (opcional)</question>
<if_unknown>Um titulo descritivo ajuda a organizar seus videos na conta. Exemplo: 'Video Produto X - Lancamento Abril'</if_unknown>

<question>Quer adicionar uma descricao? (opcional)</question>
</step>

<step number="3.4" name="Executar upload de video">
<fills>
account_id: ID da conta de anuncios (act_XXX) -- obrigatorio
title: Titulo do video -- opcional
description: Descricao do video -- opcional
</fills>

O arquivo e enviado automaticamente pelo frontend junto com a chamada da tool.

Apos upload com sucesso, mostrar:

Video enviado com sucesso!

ID do video: [video_id]
Titulo: [titulo ou "sem titulo"]

Guarde esse ID! Voce vai precisar dele para criar anuncios com esse video.
Quando for criar um criativo, informe esse ID e eu uso automaticamente.

NOTA: O video pode levar alguns minutos para ser processado pela Meta.
Enquanto processa, voce ja pode usar o ID para criar criativos.

Guardar: video_id (para referencia futura na conversa)
</step>

</step>

<step number="4" name="Proximo passo">
Apos o upload, sugerir:

"Midia enviada! O que voce quer fazer agora?"
<options>
  <option value="criar_criativo">Criar um criativo -- usar essa midia para criar um anuncio (workflow criar-criativo)</option>
  <option value="outra_midia">Enviar outra midia -- continuar fazendo uploads</option>
  <option value="voltar">Voltar ao inicio -- fazer outra coisa</option>
</options>
</step>

</steps>

<auto_fields>
account_id: mantido da selecao de conta do usuario
image_hash: retornado automaticamente apos upload de imagem (guardar para uso futuro)
video_id: retornado automaticamente apos upload de video (guardar para uso futuro)
</auto_fields>

<validations>
- account_id e obrigatorio para qualquer upload
- Imagens: formatos aceitos JPG, PNG; tamanho maximo 30 MB
- Videos: formato aceito MP4; tamanho maximo 4 GB
- Verificar se o arquivo foi anexado antes de tentar upload
- Token deve ter permissao ads_management
</validations>

<execution_order>
1. upload_ad_image(account_id) -- para imagens
2. upload_ad_video(account_id, title, description) -- para videos
</execution_order>

<error_handling>
<error code="file_too_large" cause="Arquivo excede o limite de tamanho">Imagens: max 30 MB. Videos: max 4 GB. Reduzir o tamanho do arquivo</error>
<error code="invalid_file_format" cause="Formato nao suportado">Imagens: usar JPG ou PNG. Videos: usar MP4</error>
<error code="upload_failed" cause="Erro de conexao durante upload">Tentar novamente. Para videos grandes, o upload chunked retoma de onde parou</error>
<error code="account_not_found" cause="account_id invalido">Verificar o ID da conta com get_ad_accounts</error>
<error code="permission_denied" cause="Token sem permissao de upload">Verificar se o token tem permissao ads_management</error>
<error code="video_processing_failed" cause="Video com codec nao suportado">Converter o video para H.264 (MP4) e tentar novamente</error>
<error code="image_hash_not_returned" cause="Erro interno no processamento">Tentar o upload novamente</error>
</error_handling>

<tools_used>
- upload_ad_image: account_id
- upload_ad_video: account_id, title, description
</tools_used>

</workflow>
