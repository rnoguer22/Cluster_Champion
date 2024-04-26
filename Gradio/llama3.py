import requests
import gradio as gr

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

def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    gr.Markdown('''
    # Hola Mundo
    
    ## [Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)
                
    Estamos realizando pruebas con gradio
    ''')
    with gr.Tabs():
        with gr.TabItem('Prueba'):
            input_text = gr.Textbox(lines=2, label="Input Text")
            output_text = gr.Textbox(lines=2, label="Output Text")
            text_button = gr.Button("Enviar")
            text_button.click(greet, inputs=input_text, outputs=output_text)
        with gr.TabItem('ChatBot'):
            gr.ChatInterface(predict)

demo.launch() 