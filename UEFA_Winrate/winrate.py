import pandas as pd
import os


class Winrate:

    def __init__(self, csv_paths):
        self.csv_paths = csv_paths
    
    
    def combine_data(self, output_path):
        dfs = []
        for filename in os.listdir(self.csv_paths):
            if filename.endswith(".csv"):
                df = pd.read_csv(os.path.join(self.csv_paths, filename))
                dfs.append(df)

        combined_df = pd.concat(dfs, index=False)
        combined_df.to_csv(output_path, index=False)
        return combined_df
    