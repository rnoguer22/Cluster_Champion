import pandas as pd
import numpy as np
import os



class MonteCarlo:

    def __init__(self, historical_data_path, current_data_path):
        self.historical_df = pd.read_csv(historical_data_path)
        df = pd.read_csv(current_data_path)
        self.current_df = df[:4]


    #Metodo que calcula la probabilidad con el metodo de Monte Carlo de los equipos
    def simulate_outcomes(self, historical_df, num_simulations=1000):
        historical_df['Pts'] = historical_df['Pts'] / historical_df['Pts'].sum()
        teams = historical_df['Squad'].tolist()
        win_probabilities = historical_df['Pts'].tolist()
        wins = np.zeros(len(teams))
        for _ in range(num_simulations):
            winner_index = np.random.choice(len(teams), p=win_probabilities)
            wins[winner_index] += 1
        win_probabilities = wins / num_simulations
        return win_probabilities


    #Metodo que predice el ganador de la Champions League
    def predict_winner(self, win_probabilities, merged_df):
        winner_index = np.argmax(win_probabilities)
        winner = merged_df.iloc[winner_index]['Squad']
        return winner


     #Metodo que calcula el porcentaje de probabilidad de victoria los equipos y lo guarda en csv
    def predict_champions_winner(self, output_path, num_simulations=1000):
        win_probabilities = self.simulate_outcomes(self.current_df, num_simulations)
        winner = self.predict_winner(win_probabilities, self.current_df)

        #Calculamos el porcentaje de probabilidad de victoria de cada equipo 
        percentages = win_probabilities / np.sum(win_probabilities) * 100
        teams_df = pd.DataFrame({'Squad': self.current_df['Squad'], 'Win Probability (%)': percentages.round(3)})
        teams_df_sorted = teams_df.sort_values(by='Win Probability (%)', ascending=False)

        #Añadimos los equipos que ya estan fuera de la champions, añadiendole la probabilidad de 0
        teams_out = pd.read_csv('./UEFA_Analisis_CSV/UEFA_Target.csv', skiprows=5, header=None, usecols=[2], names=['Squad'])
        teams_out['Win Probability (%)'] = 0
        teams_df_sorted = pd.concat([teams_df_sorted, teams_out], ignore_index=True)

        #Guardamos en csv
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        teams_df_sorted.to_csv(os.path.join(output_path, 'Monte_Carlo_Winner.csv'), index=False)
        print(f'\nThe predicted winner of the Champions League is: {winner}')
        print('csv saved as', os.path.join(output_path, 'Monte_Carlo_Winner.csv'))
        print('\n')
        return teams_df_sorted