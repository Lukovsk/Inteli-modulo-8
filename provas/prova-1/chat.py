#! /bin/env python3

import re

"""
- Intenção A: Pergunta sobre como atualizar as informações de pagamento.
  - Perguntas relacionadas: "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"
"""

"""
- Intenção B: Pergunta sobre como acompanhar o status do pedido.
  - Perguntas relacionadas: "Onde vejo o status do meu pedido?", "Como faço para rastrear meu pedido?", "Quero saber onde está meu pedido, como faço?", "Status de entrega, como consultar?"
"""


intentions = {
    "payment": [
        r"(.*atualizar*.)|\b(.*mudar*.)"
    ],
    "status": [
        r"(?:(?:[Ss]tatus)|(.*[Oo]nde*.)|(.*pedido*.))"
        ],
    "exit": [
        r"\b(?:[Ss]air)"
    ]
}

actions = {
    "payment": lambda _: f"Você pode atualizá-lo assim.",
    "status": lambda _: f"Você pode acompanhar o status do seu pedido lá.",
    "exit": lambda _: exit()
}


def process_command(command:str):
    for intention, patternts in intentions.items():
        for pattern in patternts:
            match = re.match(pattern, command, re.IGNORECASE)
            if match:
                return actions[intention](match.group(len(match.groups())))


def main(args=None):
    
    while True:
        command = input("Como posso te ajudar? \n")
        print(process_command(command))

if __name__ == '__main__':
    main()