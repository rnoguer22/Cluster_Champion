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
    if model.startswith('Monte'):
        model = 'Monte_Carlo_Winner.csv'
    else:
        model += '_Predictions.csv'
    df = pd.read_csv(f'./UEFA_Predictions/csv/{model}')
    return df

def select_cluster(cluster_sel, comb):
    centroid_clusters = ['kmeans', 'mean-shift', 'minibatch']

    if cluster_sel in centroid_clusters:
        path = f'./Clusters/CentroidClustering/img/{cluster_sel}/{cluster_sel}-{comb}.png'
    
    return path
    


with gr.Blocks() as demo:
    gr.Markdown('''
    # Hola Mundo
    
    ## [Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)
                
    Estamos realizando pruebas con gradio
    ''')
    with gr.Tabs():

        with gr.TabItem('Clusters'):
            cluster_type = ['kmeans', 'mean-shift', 'minibatch', 'DBSCAN', 'HDBSCAN', 'OPTICS', 'GMM', 'Agglomerative']
            cluster_comb = ['GF-Pts', 'GF-GD', 'GF-Attendance', 'GD-Pts', 'GD-Attendance']
            dropdown_cluster_type = gr.Dropdown(choices=cluster_type, label="Choose the cluster to launch:")
            dropdown_cluster_comb = gr.Dropdown(choices=cluster_comb, label="Choose the combination of data for the cluster:")
            text_button = gr.Button("Send")
            text_button.click(select_cluster, inputs=[dropdown_cluster_type, dropdown_cluster_comb], outputs=gr.Image())

        with gr.TabItem('Predictions'):
            dropdown = gr.Dropdown(choices=models, label="Choose the model to launch:")
            text_button = gr.Button("Send")
            output_df = gr.DataFrame()
            text_button.click(selection, inputs=dropdown, outputs=output_df)

        with gr.TabItem('ChatBot'):
            gr.ChatInterface(predict)

demo.launch() 