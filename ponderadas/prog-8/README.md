# Atividade 8: Tradutor de áudio

## Enunciado

Crie uma ferramenta de terminal capaz de receber como argumento o caminho para um arquivo de áudio contendo a fala de uma pessoa. Após ler o arquivo fornecido, a sua aplicação deve ser capaz de transformar o áudio em texto corretamente, usar esse texto gerado para alimentar um tradutor de texto (e.g. transforma um texto do português para o inglês) e, por fim, transforma o texto traduzido em áudio novamente e reproduz para o usuário.

### Padrão de qualidade:

- ✅ A aplicação desenvolvida deve ter uma interface de usuário capaz de receber um arquivo de áudio (sugere-se o uso do terminal por simplicidade, mas pode utilizar opções mais robustas);
- ✅ O sistema deve comprovadamente ser capaz de transformar o arquivo de áudio em texto, sendo capaz de traduzir o exemplo demonstrado sem falhas;
- ✅ O sistema deve comprovadamente ser capaz de traduzir o texto fornecido para a língua de sua escolha (e.g. português, inglês, japonês);
- ✅ O sistema deve comprovadamente ser capaz de sintetizar a frase traduzida, criando um áudio que o usuário pode ouvir com a resposta final.

#z Conteúdo

## Estrutura de pastas
<pre><code>prog-8/
│
├── inputs/
├── outputs/
├── requirements.txt
└── main.py</code> </pre>
Onde:

```inputs/```: diretório com áudios em português;

```outputs/```: diretório com os áudios que o sistema criou da frase traduzida;

```requirements.txt```: arquivo de texto com as dependências necessárias para executar a aplicação;

```main.py```: arquivo python com a classe que faz a transcrição, a tradução e a reprodução do áudio, além da instância dessa classe e sua implementação.

## Como usar essa aplicação

Para rodar esta aplicação, é necessário instalar as dependências executando (preferencialmente em um ambiente virtual):

<pre><code>pyhon -m pip install -r requirements.txt</code></pre>

Em seguida, rode o arquivo ```main.py``` passando como argumento pelo terminal algum áudio de input em português:

<pre><code>python main.py caminho-do-audio.wav</code></pre>

No próprio terminal, pode-se ver a trascrição do áudio, além da sua tradução para inglês. Na pasta ```outputs/``` estará um novo áudio em inglês que é a reprodução da tradução do áudio em português.

### Output


### Demonstração do turtlebot3 seguindo o caminho:


