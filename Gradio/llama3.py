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


with gr.Blocks() as demo:
    gr.Markdown('''
    # Hola Mundo
    Estamos realizando pruebas con gradio
    ''')
    input_text = gr.Textbox(lines=7, label="Input Text")
    output_text = gr.Textbox(lines=7, label="Output Text")

    gr.ChatInterface(predict)

demo.launch() 