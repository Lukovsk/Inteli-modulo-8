from llm import chain
import gradio as gr

def chatbot(message):
    response = ""
    for s in chain.stream(message):
        print(s.content, end="\n", flush=True)
        response += s.content
    return response

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