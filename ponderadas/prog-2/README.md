# Atividade 2: Navegação com o turtlebot

## Enunciado

Desenvolva um pacote em ROS com as funcionalidades de mapeamento e navegação utilizando o turtlebot 3 (simulado ou real)

### Padrão de qualidade:

- ✅ Comprovadamente ser capaz de mapear de forma fidedigna um ambiente (simulado ou real);
- ✅ Ser capaz de navegar em um ambiente pré-mapeado de forma programática;
- ✅ Ser capaz de desviar de obstáculos de forma dinâmica (obstáculos não mapeados);
- ✅ O sistema deve ser idempotente. Isso significa, na prática, que mesmo rodando várias vezes o navegador, ele vai passar pelos mesmos pontos (sem tentar inicializar a pose duas vezes);

# Conteúdo

## Estrutura de pastas
<pre><code>prog-2/pacote1/
│
├── launch/
├── pacote1/
└── setup.py</code> </pre>
Onde:
```launch/```: diretório com os launchers

```pacote1/```: diretório com os scripts do meu pacote

```setup.py```: arquivo python com o setup para meu workspace

## Como usar essa aplicação

Para rodar esta aplicação, é necessário, primeiro, fazer todo o setup com o ros e as bibliotecas necessárias. Meu professor fez um tutorial de como fazer tudo isso, aqui o [link](https://rmnicola.github.io/m8-ec-encontros/).

Segundo, clone meu respositório:

<pre> <code> git clone https://github.com/Lukovsk/Inteli-modulo-8.git </code> </pre>

Em seguida, instale meu pacote:

<pre> <code> source /Inteli-modulo-8/ponderadas/prog-2/pacote1/install/setup.bash
ou, se estiver usando zsh:
source /Inteli-modulo-8/ponderadas/prog-2/pacote1/install/setup.zsh</code> </pre>

Agora, você pode rodar os dois launchs.py presentes no diretório launch/. Eles são o ```mapear.launch.py``` e o ```caminhar.launch.py```. 

### Mapear

Rodando o comando

<pre><code>ros2 launch mapear.launch.py</code></pre>

no diretório ```launch/```, abrirá 3 softwares:

- <code>Webots</code>: software responsável por apresentar o turtlebot3 e o mapa dele;
- <code>Rviz</code>: software responsável por mapear;
- <code>Teleop keyboard</code>: script responsável por permitir a movimentação do turtlebot3.

Com isso, você já pode começar a mapear o ambiente. No fim, o seu mapa será salvo dentro do diretório ```/maps``` em launch.

#### Demonstação do mapeamento:

[mapeamento.webm](https://github.com/Lukovsk/Inteli-modulo-8/assets/99260684/5b6a7214-6f24-415f-872e-67043219d783)

### Caminhar

Rodando o comando

<pre><code>ros2 launch caminhar.launch.py</code></pre>

no diretório ```launch/```, abrirá 2 softwares e rodará o meu pacote:

- <code>Webots</code> novamente;
- <code>Rviz</code> com o seu mapa mapeado.
- pacote <code>pacote1</code>, script que fará com que o turtlebot3 passe por 3 pontos (por enquanto) previamente definidos no pacote1

#### Demonstração do turtlebot3 seguindo o caminho:

[caminhando.webm](https://github.com/Lukovsk/Inteli-modulo-8/assets/99260684/edc3b89a-cf1e-4918-9f56-500bf884f4db)

