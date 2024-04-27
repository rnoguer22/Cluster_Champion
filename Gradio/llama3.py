import requests
import os
import gradio as gr
import pandas as pd


# Obtener lista de nombres de archivos en el directorio
archivos = os.listdir("./UEFA_Predictions/csv/")

models = []
for model in archivos:
    if model.startswith('Monte'):
        models.append(model.split("_")[0] + "_" + model.split("_")[1])
    else:
        models.append(model.split("_")[0])

models.sort()



def predict(prompt, history):
    data = {
        "model": "llama3",
        "messages": [
            {
              "role": "user",
              "content": prompt
            }
        ],
        "stream": False
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    url = "http://localhost:11434/api/chat"
    response = requests.post(url, headers=headers, json=data)
    return(response.json()['message']['content'])

def selection(model):
    model += '_Predictions.csv'
    df = pd.read_csv(f'./UEFA_Predictions/csv/{model}')
    return df


with gr.Blocks() as demo:
    gr.Markdown('''
    # Hola Mundo
    
    ## [Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)
                
    Estamos realizando pruebas con gradio
    ''')
    with gr.Tabs():

        with gr.TabItem('Predictions'):
            dropdown = gr.Dropdown(choices=models, label="Choose the model to launch:")
            output_text = gr.Textbox(lines=2, label="Output Text", visible=False)
            text_button = gr.Button("Send")
            text_button.click(selection, inputs=dropdown, outputs=gr.DataFrame())

        with gr.TabItem('ChatBot'):
            gr.ChatInterface(predict)

demo.launch() 