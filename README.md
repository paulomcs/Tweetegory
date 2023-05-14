# Tweets Clustering
O Tweets Clustering é um projeto de Inteligência Aritificial cujo objetivo é entender o comportamento do agrupamento desse tipo de texto. Adotamaos a representação TF-IDF e utilizamos o algoritmo K-Means para a clusterização.


## Base de Dados
Foi utilizada uma base de 2600 tweets do dia 10/05/2023.

Páginas Selecionadas:
- Notícias:CNN Brasil, Estadão, Jovem Pan News, Folha de São Paulo, O Antagonista e Globo News
- Esportes: TNT Sports Brasil, ESPN Brasil, Globo Esporte, Sportv, NBA Brasil e UOL Esporte
- Entretenimento: Omelete, Adoro Cinema, Cine POP e Série Maníacos

A quantidade de tweets de cada categoria foi definida da seguinte forma:
- 150 tweets de cada página de Notícia
- 150 tweets de cada página de Esportes
- 200 tweets de cada página de Entretenimento

A base de tweets processados está no arquivo "tweets_Todos_processados.txt"

## Resultado das Clusterização
Foi adotado o número de clusters igual a 5, que formaram-se da seguinte forma:

### Geral
Um grupo formado por cerca de 2050 tweets que continha termos de todas as áreas (Notícias, Esportes e Entretenimento)

### Rita Lett
Um grupo formado por certa de 200 tweets que comentaram sobre o falecimento da artista Rita Lee

### PL da Fake News
Um grupo formado por certa de 150 tweets que continha termos como: PL, Fake News, STF e Bolsonaro

### Temporada
Um grupo formado por certa de 150 tweets que continha o termo "temporada", seja ele do ramo do esporte ou do entretenimento

### Real Madrid x Manchester City
Um grupo formado por certa de 100 tweets que continha termos relacionados ao jogo da semi-final da Champions League


Link do Colab: 
https://colab.research.google.com/drive/1sB9ArBfenFcKyEttmmHI1rOSAPI6aQJC?usp=sharing

Link da Páginas com os Vìdeos de Apresentação:
https://drive.google.com/drive/folders/1gcdjXD5AMCo8y2EEC9yi_RnAiZITCLAY?usp=sharing
