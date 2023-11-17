# Atividade 3: Criação de um chatbot simples

## Enunciado

Desenvolva um nó de ROS que seja um chatbot capaz de entender comandos escritos em linguagem natural para interagir com um robô de serviço fictício. O chatbot deve fornecer ao usuário a possibilidade de enviar comandos de posição para o robô de forma simples e intuitiva. Exemplos de comandos:

<pre>Vá para a secretaria
Dirja-se ao laboratório
Me leve para a biblioteca
</pre>

Para cada comando registrado, o sistema deve ser capaz de extrair a intenção do usuário a partir de um dicionário de intenções, filtradas por expressões regulares. A partir daí, um segundo dicionário deve ser usado, capaz de vincular intenções à funções que o robô deve executar. Para essa ponderada, o script em Python não precisa se comunicar com o nav2 e nem com o robô, mas é necessário dar um feedback ao usuário de que a ação foi compreendida e está sendo executada. Por fim, está liberado o uso de frameworks como Chatterbot e NLTK.

### Padrão de qualidade:

O sistema desenvolvido deve:

- ✅ Comprovadamente ser capaz de compreender ao menos uma inteção do usuário: a de mandar o robô para um determinado ponto;
- ✅ Deve haver um dicionário de intenções e a intenção deve ser caputrada através de expressões regulares;
- ✅ Ao menos dois formatos diferentes devem ser considerados para a captura da intenção do usuário (e.g. "Vá para...", "Me leve até...");
- ✅ O script deve contar com um dicionário de ações, relacionando cada intenção com uma função a ser executada pelo robô;
- ✅ O chatbot deve dar feedback ao usuário sobre a compreensão do que foi dito e a ação que será tomada.

# Conteúdo

## Estrutura de pastas
<pre><code>prog-3/ros-workspace/src/chabot/
│
├── chatbot/
└── setup.py</code> </pre>
Onde:

```chatbot/```: diretório com os scripts do meu pacote

```setup.py```: arquivo python com o setup para meu workspace

## Como usar essa aplicação

Para rodar esta aplicação, é necessário, primeiro, fazer todo o setup com o ros e as bibliotecas necessárias. Meu professor fez um tutorial de como fazer tudo isso, aqui o [link](https://rmnicola.github.io/m8-ec-encontros/).

Segundo, clone meu respositório:

<pre> <code>git clone https://github.com/Lukovsk/Inteli-modulo-8.git </code> </pre>

Em seguida, instale meu pacote chatbot:

<pre> <code>source /Inteli-modulo-8/ponderadas/prog-2/pacote1/install/setup.bash # troque para .zsh se necessário</code> </pre>

Agora, você pode rodar os dois nós presentes no pacote. Para isso, em dois terminais diferentes, execute:
<pre><code>ros2 run chatbot output
ros2 run chatbot input</code></pre> 

### Output

Executando

<pre><code>ros2 run chatbot ouput</code></pre>

Um nó será criado e o terminal irá dispor todas as respostas que o chatbot estiver produzindo pelo tópico ```/chatbot```, no qual este nó está inscrito.

### Input

Executando 

<pre><code>ros2 run chatbot input</code></pre>

Um nó será criado e o terminal irá permitir que converse com o chatbot, já que este nó estará publicando no tópico ```/chatbot``` também. Tente pedir para ele ir a algum lugar ou se apresentar.

### Demonstração