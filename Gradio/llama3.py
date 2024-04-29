import requests
import os
import gradio as gr
import pandas as pd



class Gradio_GUI():

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.models = self.get_models(csv_path)
    

    def get_models(self, csv_path):
        #Obtenemos la lista de nombres de archivos en el directorio
        archivos = os.listdir(csv_path)
        models = []
        for model in archivos:
            if model.startswith('Monte'):
                models.append(model.split("_")[0] + "_" + model.split("_")[1])
            else:
                models.append(model.split("_")[0])
        models.sort()
        return models


    def llama3_predict(self, prompt):
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


    def selection(self, model):
        if model.startswith('Monte'):
            model = 'Monte_Carlo_Winner.csv'
        else:
            model += '_Predictions.csv'
        df = pd.read_csv(os.path.join(self.csv_path, model))
        return df

    def select_cluster(self, cluster_sel, comb):
        centroid_clusters = ['kmeans', 'mean-shift', 'minibatch']
        density_clusters = ['dbscan', 'hdbscan', 'optics']
        distribution_clusters = 'gmm'
        hierarchical_clusters = 'agglomerative'

        if cluster_sel in centroid_clusters:
            path = f'./Clusters/CentroidClustering/img/{cluster_sel}/{cluster_sel}-{comb}.png'
        elif cluster_sel in density_clusters:
            path = f'./Clusters/DensityClustering/img/{cluster_sel}/{cluster_sel}-{comb}.png'
        elif cluster_sel == distribution_clusters:
            path = f'./Clusters/DistributionClustering/img/{cluster_sel}/{cluster_sel}-{comb}.png'
        elif cluster_sel == hierarchical_clusters:
            path = f'./Clusters/HierarchicalClustering/img/{cluster_sel}/{cluster_sel}-{comb}.png'
        else:
            print('Error')
        return path
    


    def launch_gradio_gui(self):
        with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
            gr.Markdown('''
            <h1 style="text-align: left">
            Champions League Analysis with Llama3
            </h1>
            ''')
            with gr.Tabs():

                with gr.TabItem('Clusters'):
                    cluster_type = ['kmeans', 'mean-shift', 'minibatch', 'dbscan', 'hdbscan', 'optics', 'gmm', 'agglomerative']
                    cluster_comb = ['GF-Pts', 'GF-GD', 'GF-Attendance', 'GD-Pts', 'GD-Attendance']
                    with gr.Row():
                        with gr.Column():
                            dropdown_cluster_type = gr.Dropdown(choices=cluster_type, value=cluster_type[0], label="Choose the cluster to launch:")
                            dropdown_cluster_comb = gr.Dropdown(choices=cluster_comb, value=cluster_comb[0], label="Choose the combination of data for the cluster:")
                            gr.Markdown('<br><br><br><br><br><br>') 
                            text_button = gr.Button("Generate")
                        cluster_img = gr.Image(height=445)
                    text_button.click(self.select_cluster, inputs=[dropdown_cluster_type, dropdown_cluster_comb], outputs=cluster_img)

                with gr.TabItem('Predictions'):
                    with gr.Row():
                        with gr.Column():
                            dropdown = gr.Dropdown(choices=self.models, value=self.models[0], label="Choose the time series model to visualize the prediction:")
                            text_button = gr.Button("Generate")
                        output_df = gr.DataFrame()
                    text_button.click(self.selection, inputs=dropdown, outputs=output_df)

                with gr.TabItem('ChatBot'):
                    gr.Markdown('''
                        ### To make the chatbot work, you need to:
                        - Have Ollama installed and running in your computer (run ollama from the command line with: ollama serve)
                        - Install llama3 in your local machine      
                    ''')
                    gr.ChatInterface(self.llama3_predict, fill_height=True)

        demo.launch(inbrowser=True) 