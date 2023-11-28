# Atividade 5: Construção de um chatbot com LLM e RAG

## Enunciado

Utilizando um LLM (local ou API externa), crie um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema ainda deve ser capaz de contextualizar suas respostas a partir do seguinte documento:

[Workshop rules and safety considerations](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety)

Exemplo de prompt:

<pre><code>Who is allowed to operate a lathe? What protective gear should be used to do it?</code></pre>

Resposta:

<pre><code>Based on the given context, it is not mentioned who is allowed to operate a lathe. However, it is stated that tools other than the router and trimmer can be used by students who have been inducted into the workshop and tested in their capability to use them. 
The protective gear that should be used when operating a lathe is not explicitly mentioned in the given context.</code></pre>

### Padrão de qualidade

O sistema desenvolvido deve:

- ✅ Utilizar o langchain para criar a interface com o modelo de LLM utilizado (pode ser openAI ou modelos do huggingface/ollama);
- ✅ Criar uma interface gráfica simples para o chatbot;
- ✅ Responder de forma concisa aos prompts do usuário;
- ✅ O sistema deve considerar como contexto o arquivo/documento/página fornecida no enunciado da atividade.

# Conteúdo

## Estrutura de pastas
<pre><code>prog-5/
│
├── data/
├── flagged/
├── llm.py
├── main.py
└── requirements.txt</code> </pre>
Onde:

```data/```: diretório que possui o pdf que dá contexto ao chatbot;

```flagged/```: diretório que possui qualquer chat salvo pelo gradio;

```llm.py```: script auxiliar que faz as requisições para o openai e define o llm;

```main.py```: script responsável por ativar a aplicação;

```requirements.txt```: arquivo com as dependências necessárias para a execução da aplicação.

## Como usar essa aplicação

Para rodar essa aplicação, primeiro você precisa da chave da API do openai. Essa chave pode ser retirada [aqui](https://platform.openai.com/api-keys).

Segundo, clone este respositório:

<pre> <code>git clone https://github.com/Lukovsk/Inteli-modulo-8.git </code> </pre>

Em seguida, neste diretório, instale as dependências necessárias:

<pre> <code>python -m pip install -r requirements.txt</code> </pre>

Agora, basta executar o arquivo ```main.py```:

<pre><code>python main.py</code></pre> 

### Demonstração

[af823e10-1a5d-4509-9f1f-d90646c584f2.webm](https://github.com/Lukovsk/Inteli-modulo-8/assets/99260684/f33b7f0f-ee81-49af-bcf3-7af7e5e3cc80)

