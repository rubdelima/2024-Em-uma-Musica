# Main Text

main_text = """
> "Bom, fim de ano chegou. É hora da gente olhar pra trás. E relembrar de tudo o que aconteceu. Mas como seria o ano de 20XX em uma música?"

Se assim como eu você também sentiu a falta dessa frase em algum ano, bem vindo! Mas um certo grupo da classe de Criatividade Computacional se juntou e se perguntou, "e se déssemos continuidade a esse projeto, mas utilizando AI"?

E então nos juntamos e criamos uma coleção de como seria o ano de 2024 em uma música, utilizando o RVC, e ferramentas de edição e criação de vídeo e imagens com Inteligência Artificial, explorando ao máximo a nossa criatividade e dos modelos, para gerar uma coleção de músicas na voz do Lucas.

O Resultado? Pois bem, algumas não saíram como queríamos, mas em outras tivemos um bom resultado, convido todos a escutarem e tentar imaginar como seria o ano de 2024 em uma música.

### Ferramentas Utilizadas
- [RVC-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI): Ferramenta para treinamento do Modelo de Voz e Substituição de Fala
"""

# Relatory Text

music_generation_p1 = """
## 2.1 Geração/Alteração de Voz

Como falamos na introdução, nosso foco era primeiramente criar as músicas antes dos vídeos, para isso, dividimos em duas etapas, geração da voz e geração da melodia. Primeiramente para a geração da melodia, utilizamos o RVC, que é uma das ferramentas mais utilizadas para a substituição de voz.

Para isso, utilizamos o [RVCWebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/tree/main) executando de forma local, coletamos os áudios dos 5 vídeos das últimas retrospectivas (2019, 2020, 2021, 2022, 2023), e utilizamos o demucs, uma biblioteca do python, para separar a parte vocal da parte instrumental. Utilizando uma RTX 4050 Mobile, treinamos um modelo por 50 épocas, o que demorou algumas longas horas de treinamento, e mais algumas horas para o treinamento de 10 épocas dos índices.

Verificamos que algumas músicas tinham vocais diversos, (como "tô bem" de Jovem Dionísio e "Die With a Smile" de Lady Gaba com participação de Bruno Mars), o que poderia gerar um dificuldade para o modelo distinguir as diferentes vozes, por isso, utilizamos o [Pyannote - Speaker Diarization](https://huggingface.co/pyannote/speaker-diarization), um modelo disponível no huggingface para fazer a distinção entre diferentes. Porém o output que tivemos foi que ele não conseguiu separar diferentes fontes de vozes, algumas separações contavam com arquivos com mais de um fonte de voz e a outra com o mesmo vocal de outro arquivo, porém como uma configuração co chorus, por exemplo. Embora haja uma hipóteses, que a divisão poderia nos ajudar a testar os modelos, isso impactaria bastante no tempo total para criar as músicas, dessa forma optamos por utilizar apenas o audio separado via demucs.

Tivemos sim um resultado positivo em algumas músicas, principalmente em músicas que há apenas uma voz, pois em  músicas onde há mais de um locutor ou sobreposição de voz com oitavas diferentes. Em geral, os áudios possui uma cara de robotizados, talvez isso se reflita pelo modelo ou a qualidade dos dados utilizados para o treinamento, embora tivemos mais de 1h de voz para treinar o modelo, utilizamos um algoritmo para separar a voz do audio original, e nessa separação algumas características da voz podem ser perdidas ficando robotizadas, o que pode ter impactado na qualidade das features e pesos do modelo.

Abaixo tem alguns exemplos do áudio original, áudio com remoção de instrumental e audios com a substituição de voz. Nota-se uma leve vantagem (embora ainda sim robotizada) no cenário que o uso do separador de vocal não foi utilizado.
"""

music_generation_p1_items = [
    {
        "title": "The Weeknd - Dancing in The Flames",
        "tag" : "Audio Original",
        "audio" : "./assets/audios/vocals-dancing.flac",
    },
    {
        "title" : "Lvcas(RVC) - Dancing in The Flames",
        "tag" : "Audio Substituído",
        "audio" : "./assets/audios/rvc-dancing.wav",
    },
    {
        "title" : "Benson Boone - Beautiful Things",
        "tag" : "Audio Original com Remoção de Instrumental",
        "audio" : "./assets/audios/vocals-beautiful-things.wav",
    },
    {
        "title" : "Lvcas(RVC) - Beautiful Things",
        "tag" : "Audio Substituído",
        "audio" : "./assets/audios/rvc-beautiful-things.wav",
    }
]

music_generation_p2 = """
O modelo não interpreta como vozes diferentes e tenta, como na música "tô bem" de Jovem Dionísio, a qual há várias locutores com audio sobrepostos, e tonalidades diferente. Bem como a música "Please Please Please" de Sabrina Carpenter, na qual há um vocal que acompanha a voz dela, e o modelo não interpreta como vozes distintas e tenta substituir as duas simultaneamente, e como as vozes estão em tonalidades diferentes (mesmo tendo o mesmo timbre), o modelo não acerta a nota. Observe nos exemplos abaixo:
"""

music_generation_p2_items = [
    {
        "title": "Jovem Dionísio - to bem",
        "tag" : "Audio Original",
        "audio" : "./assets/audios/vocals-to-bem.wav",
    },
    {
        "title" : "Lvcas(RVC) - to bem",
        "tag" : "Audio Substituído",
        "audio" : "./assets/audios/rvc-to-bem.wav",
    },
    {
        "title": "Sabrina Carpenter - Please Please Please",
        "tag" : "Audio Original",
        "audio" : "./assets/audios/vocals-please.wav",
    },
    {
        "title": "Lvcas(RVC) - Please Please Please",
        "tag" : "Audio Substituído",
        "audio" : "./assets/audios/rvc-please.wav",
    }
]

music_generation_p3 = """
## 2.2 Geração de Melodia
Para a geração da melodia, testamos o [MusicGen Melody](https://huggingface.co/facebook/musicgen-melody), um modelo de geração de música da Meta, que gera músicas com base em um prompt e que possui como parâmetro de entrada um audio, o qual ele irá extrair as características para aplicar o estilo informado no prompt. Exploramos outros modelos, porém apenas esse realmente demostrou uma troca de estilo e manteu características da música original. Porém, a sua saída era descompassada em relação à música original, não sendo possível juntar com o áudio gerado com o RVC.
Abaixo temos um exemplo da saída de uma entrada desse modelos, é a música Dancing in The Flames do The Weeknd, com o prompt 
"""

music_generation_p3_items = [
    {
        "title": "The Weeknd - Dancing in The Flames",
        "tag" : "Audio Original",
        "audio" : "./assets/audios/dancing-instrumental.flac",
    },
    {
        "title": "MusicGen Melody - Dancing in The Flames - Power Metal",
        "tag": "Audio Gerado - Power Metal",
        "audio": "./assets/audios/dancing-power-metal.wav",
    },
    {
        "title": "MusicGen Melody - Dancing in The Flames - Hard Rock",
        "tag": "Audio Gerado - Hard Rock",
        "audio": "./assets/audios/dancing-hard-rock.wav",
    }
]

music_generation_p4 = """
Por fim, tentamos, também, utilizar algum modelo de Geração de Músicas, nossa ideia era por a letra da música e estilo, descrever um pouco a música original, e depois substitui a voz gerada com o RVC, porém, nos sites que tentamos, eles identificavam que a letra original já era de uma música, então se recusavam a gerar a música. Dessa forma, desistimos dessa etapa, pois hoje, ainda não existe alguma ferramenta que possa realizar a troca de estilo musical sem perdas na composição da música original.
"""