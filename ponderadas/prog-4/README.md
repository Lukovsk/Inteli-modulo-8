# Atividade 4: Construção de um chatbot com LLM

## Enunciado

Utilizando um LLM (local ou API externa), crie um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado.

Exemplo de prompt:

<code><pre>Quais EPIs são necessários para operar um torno mecânico?</pre></code>


### Padrão de qualidade:

O sistema desenvolvido deve:

- Utilizar o langchain para criar a interface com o modelo de LLM utilizado (pode ser openAI ou modelos do huggingface/ollama);
- Utilizar o gradio para criar uma interface gráfica simples para o chatbot;
- Responder de forma concisa aos prompts do usuário. Para isso, deve-se criar um prompt de sistema que contextualiza todas as respostas do modelo utilizado.

# Conteúdo

## Estrutura de pastas
<pre><code>prog-4/
│
├── app.py
├── chat.py
└── requirements.txt</code> </pre>
Onde:

```app.py```: script responsável por ativar a aplicação;

```chat.py```: script auxiliar que faz as requisições para o openai;

```requirements.txt```: arquivo com as dependências necessárias.

## Como usar essa aplicação

Para rodar essa aplicação, primeiro você precisa da chave da API do openai. Essa chave pode ser retirada [aqui](https://platform.openai.com/api-keys)

Segundo, clone este respositório:

<pre> <code>git clone https://github.com/Lukovsk/Inteli-modulo-8.git </code> </pre>

Em seguida, neste diretório, instale as dependências necessárias:

<pre> <code>python -m pip install -r requirements.txt</code> </pre>

Agora, basta executar o arquivo ```app.py```:

<pre><code>python app.py</code></pre> 

### Demonstração



