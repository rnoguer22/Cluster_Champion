import pandas as pd
import os
import matplotlib.pyplot as plt


class Winrate:

    def __init__(self, csv_paths):
        self.csv_paths = csv_paths
    
    
    def combine_data(self):
        dfs = []
        for filename in os.listdir(self.csv_paths):
            if filename.endswith(".csv"):
                df = pd.read_csv(os.path.join(self.csv_paths, filename))
                dfs.append(df)
        combined_df = pd.concat(dfs)
        return combined_df
    

    def calculate_prob(self, combined_df, output_path):
        #Convertimos las predicciones en valores numericos
        score_mapping = {'W': 10, 'F': 7, 'SF': 5, 'QF': 2, 'R16': 1, 'GR': 0}
        combined_df['Score'] = combined_df['Prediction'].map(score_mapping)
        #Hallamos la probabilidad
        team_probabilities = combined_df.groupby(combined_df['Squad'].str[:-10])['Score'].mean().sort_values(ascending=False)
        total_score = team_probabilities.sum()
        team_probabilities_percentage = round((team_probabilities / total_score) * 100, 2)
        #Guardamos en csv
        df_team_prob = pd.DataFrame({'Squad': team_probabilities_percentage.index, 'Prediction': team_probabilities_percentage.values})
        df_team_prob.to_csv(output_path, index=False)
        return df_team_prob


    def plot_prob(self, path, df_prob):
            #Graficamos la probabilidad
            fig, ax = plt.subplots()
            ax.bar(df_prob['Squad'], df_prob['Prediction'])
            ax.set_xlabel('Squad')
            ax.set_ylabel('Winrate (%)')
            plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x
            plt.savefig(path)