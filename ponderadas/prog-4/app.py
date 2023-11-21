import gradio as gr
from chat import get_openai

def chatbot(message):
    explanation = get_openai(res=message)
    return explanation

def main():
    iface = gr.Interface(
        fn=chatbot,
        inputs="text",
        outputs="text",
        live=True,
        # placeholder="Digite sua pergunta aqui...",
        title="Bem-vindo ao chat do Júpiter",
        description="Faça uma pergunta para o especialista em normas de seguranças industriais"
    )

    iface.launch()

if __name__ == "__main__":
    main()
