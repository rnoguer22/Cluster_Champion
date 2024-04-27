import requests
import os
import gradio as gr


# Obtener lista de nombres de archivos en el directorio
archivos = os.listdir("./UEFA_Predictions/csv/")

models = []
for model in archivos:
    if model[0].islower():
        model = model.capitalize()
    if model.startswith('Monte'):
        models.append('Monte Carlo')
    elif model.startswith('Linear'):
        models.append('Linear Regression')
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

def selection(option):
    return f"{option} selected"


with gr.Blocks() as demo:
    gr.Markdown('''
    # Hola Mundo
    
    ## [Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)
                
    Estamos realizando pruebas con gradio
    ''')
    with gr.Tabs():
        with gr.TabItem('Predicciones'):
            dropdown = gr.Dropdown(choices=models, label="Seleccione el modelo que desea utilizar")
            output_text = gr.Textbox(lines=2, label="Output Text")
            text_button = gr.Button("Enviar")
            text_button.click(selection, inputs=dropdown, outputs=output_text)
        with gr.TabItem('ChatBot'):
            gr.ChatInterface(predict)

demo.launch() 