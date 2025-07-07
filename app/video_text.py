main_text = """
A partir das criações geradas, implementamos diversas abordagens para a tentativa de criação de vídeos correspondentes, inspirados nos clipes originais das músicas.

### Ferramentas Utilizadas
- [Sora](https://sora.chatgpt.com): Ferramenta para criação e modificação do modelo/partes do cenário.
- [Vocal Remover](https://vocalremover.org/): Ferramenta para isolamento das faixas vocais das músicas.
- [Hedra](https://hedra.com/): Ferramenta para geração de vídeo sincronizado com os vocais das músicas.

Ajustes finos foram feitos com softwares de edição de imagem com o Photoshop e sincronização feita com o Capcut.
"""

first_approach = """
**Primeira abordagem: apenas modelo com descrição do vídeo**

Nesta primeira tentativa, o vídeo foi gerado unicamente a partir de uma descrição textual simples e de um modelo, apenas da face do personagem. A ideia era observar como as ferramentas de geração se comportariam com inputs mínimos, confiando apenas na interpretação da IA. O resultado, no entanto, foi pouco expressivo: o personagem gerado era inconsistente com o modelo enviado, sem identidade clara, e os movimentos pareciam aleatórios ou genéricos. O vídeo carecia de coesão visual e narrativa, o que o tornava difícil de associar à música ou ao artista pretendido.
"""

second_approach = """
**Segunda abordagem: fornecimento de modelo e fundo gerado**

Na segunda tentativa, passamos a fornecer tanto o modelo visual do personagem quanto um fundo gerado artificialmente, buscando compor cenas mais próximas de um videoclipe, tendo como planejamento uma sincronização labial em uma fase posterior. Apesar da melhora visual em relação à primeira abordagem, os movimentos do personagem se tornaram errádicos e podia se notar uma inconsistência de movimentos e expressões faciais do personagem, o que dificultou expressivamente a tentativa de utilização dos vídeos gerados para sincronização labial.
"""

third_approach = """
**Terceira abordagem: geração com Hedra, imagem e áudio integrados**

Por fim, utilizamos o Hedra como solução integrada: isolamos os vocais da música, geramos uma imagem inicial personalizada com base no modelo do artista e aplicamos ajustes visuais finos. Com esses elementos combinados, o Hedra foi capaz de gerar um vídeo sincronizado com a faixa vocal, oferecendo expressões mais naturais e movimentos labiais significativamente mais alinhados à performance. Esta abordagem resultou no vídeo mais convincente entre as tentativas, tanto visual quanto musicalmente, principalmente após a sincronização com a versão da música com as faixas instrumentais posteriormente.
"""

generated_videos = [
    {
        "title": "Primeira Tentativa - Apenas modelo com descrição do vídeo",
        "tag": "Vídeo gerado por descrição pura e sem modelo de corpo inteiro",
        "video": "./assets/videos/test2.mp4",
    },
    {
        "title": "Segunda Tentativa - Fornecimento do modelo e também",
        "tag": "Vídeo gerado a partir de modelo e fundo gerados",
        "video": "./assets/videos/test1.mp4",
    },
    {
        "title": "Terceira abordagem - Hedra",
        "tag": "Vídeo gerado com Hedra a partir do isolamento vocal e imagem inicial com modelo gerado e ajustes finos feitos e sincronização com a versão da música gerada",
        "video": "./assets/videos/inutilismo_espresso_ready_alt.mp4",
    },
    {
        "title": "Terceira abordagem - Hedra: Geração de imagem mais autônoma",
        "tag": "Vídeo gerado com Hedra a partir do isolamento vocal e imagem inicial gerada majoritariamente pelo Sora a partir de uma captura de tela do clipe original, com pequenos ajustes feitos e sincronização com a versão da música gerada",
        "video": "./assets/videos/too-sweet_synced.mp4",
    }
]

tries_text = """
Apesar de conseguirmos bons resultados, também houveram gerações que, por fatores de isolamento de áudio ou ritmo de música, dificultaram a criação de uma mídia final convincente. Seguem abaixo exemplos preliminares destes casos.
"""

generated_tries = [
    {
        "title": "Exemplo onde vocais em camadas afetaram a habilidade de sincronização labial da ferramenta",
        "tag": "Million Dollar Baby, Tommy Richman",
        "video": "./assets/videos/tommy-richman_synced.mp4",
    },
    {
        "title": "Exemplo onde vídeo causou pequena distorção no cenário com a movimentação do personagem",
        "tag": "Cruel Summer, Taylor Swift",
        "video": "./assets/videos/cruel-summer_synced.mp4",
    },
        {
        "title": "Exemplo onde vocais, apesar de terem sido altamente modificados durante a transformação da música, foram utilizados de forma eficiente para a sincronização labial",
        "tag": "To bem, Jovem Dionisio",
        "video": "./assets/videos/to-bem_synced.mp4",
    }
]