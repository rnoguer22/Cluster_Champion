import requests
import gradio as gr
from llama3 import llama3

def predict(message, history):
    history_llama3_format = []
    for human, assistant in history:
        history_llama3_format.append({"from": "user", "message": human})
        history_llama3_format.append({"from": "assistant", "message": assistant})
    history_llama3_format.append({"from": "user", "message": message})
  
    response = llama3(message)
    #response = requests.post("https://api.llama.ai/chat", json={"messages": history_llama3_format})
    '''partial_message = ""
    for item in response["messages"]:
        if item["from"] == "assistant":
            partial_message += item["message"]
    return partial_message'''
    return response

gr.ChatInterface(predict).launch()
