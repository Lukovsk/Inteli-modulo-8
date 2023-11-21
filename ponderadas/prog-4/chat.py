import os
from functools import partial
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def send_question(question:str)-> dict:
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"Você é um técnico de manutenção industrial."},
                  {"role":"user","content":question}]
    )

def get_response(response:dict)->str:
    return response["choices"][0]["message"]["content"]

def get_info(question:str,res:str)->str:
    resp = send_question(f"{question}\n\n{res}")
    return get_response(resp)


get_openai = partial(
    get_info,
    question = "Explique sobre essa regra de segurança de maneira sucinta e em apenas 1 parágrafo, sem contextualizar: "
)