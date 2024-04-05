import pandas as pd
import numpy as np

class MonteCarlo:
    def __init__(self, historical_data, current_data):
        self.historical_data = historical_data
        self.current_data = current_data

    def prepare_data(self):
        historical_df = pd.read_csv(pd.compat.StringIO(self.historical_data))
        current_df = pd.read_csv(pd.compat.StringIO(self.current_data))
        merged_df = pd.concat([historical_df, current_df], ignore_index=True)
        merged_df.drop(columns=['id', 'Rk', 'MP', 'Attendance', 'Top Team Scorer', 'Goalkeeper'], inplace=True)
        return merged_df

    def simulate_outcomes(self, merged_df, num_simulations=1000):
        num_teams = merged_df.shape[0]
        wins = np.zeros(num_teams)

        for _ in range(num_simulations):
            winner_index = np.random.randint(num_teams)
            wins[winner_index] += 1

        win_probabilities = wins / num_simulations
        return win_probabilities

    def predict_winner(self, win_probabilities, merged_df):
        winner_index = np.argmax(win_probabilities)
        winner = merged_df.iloc[winner_index]['Squad']
        return winner

    def predict_champions_winner(self, num_simulations=1000):
        merged_df = self.prepare_data()
        win_probabilities = self.simulate_outcomes(merged_df, num_simulations)
        winner = self.predict_winner(win_probabilities, merged_df)
        return winner


# Cargar datos históricos y actuales desde archivos CSV
historical_data_df = pd.read_csv('ruta/historical_data.csv')
current_data_df = pd.read_csv('ruta/current_data.csv')

# Instanciar la clase MonteCarlo con los DataFrames cargados
mc = MonteCarlo(historical_data_df, current_data_df)

# Realizar la predicción del ganador de la Champions League
winner = mc.predict_champions_winner(num_simulations=1000)

print("Predicted winner of Champions League:", winner)
