import pandas as pd
import numpy as np



class MonteCarlo:

    def __init__(self, historical_data_path, current_data_path):
        self.historical_df = pd.read_csv(historical_data_path)
        self.current_df = pd.read_csv(current_data_path)


    def prepare_data(self):
        merged_df = pd.concat([self.historical_df, self.current_df], ignore_index=True)
        merged_df.drop(columns=['id', 'Rk', 'MP', 'Attendance', 'Top Team Scorer', 'Goalkeeper'], inplace=True)
        print(merged_df)
        return merged_df


    def simulate_outcomes(self, historical_df, num_simulations=1000):
        historical_df['Pts'] = historical_df['Pts'] / historical_df['Pts'].sum()

        teams = historical_df['Squad'].tolist()
        win_probabilities = historical_df['Pts'].tolist()

        wins = np.zeros(len(teams))

        for _ in range(num_simulations):
            winner_index = np.random.choice(len(teams), p=win_probabilities)
            wins[winner_index] += 1

        win_probabilities = wins / num_simulations
        print(win_probabilities)
        return win_probabilities



    def predict_winner(self, win_probabilities, merged_df):
        winner_index = np.argmax(win_probabilities)
        winner = merged_df.iloc[winner_index]['Squad']
        return winner


    def predict_champions_winner(self, num_simulations=1000):
        win_probabilities = self.simulate_outcomes(self.current_df, num_simulations)
        winner = self.predict_winner(win_probabilities, self.current_df)
        return winner




# Instanciar la clase MonteCarlo con los DataFrames cargados
mc = MonteCarlo('./UEFA_Analisis_CSV/UEFA_Final_Data.csv', './UEFA_Analisis_CSV/UEFA_Target.csv')

# Realizar la predicción del ganador de la Champions League
winner = mc.predict_champions_winner(num_simulations=1000)

print("Predicted winner of Champions League:", winner)
