import os
import pandas as pd


class AnalisisScrappedData:

    def __init__(self) -> None:
        self.ruta = 'Web_Scrapping/scrapped_csv'
        self.rutas = sorted(os.listdir(self.ruta))


    #En esta funcion vamos a analizar los datos de los csv
    def analize_csv(self):
        print('\nAnalizando los siguientes datos:')
        for csv in self.rutas:
            print(csv)
            self.data_path = self.ruta + '/' + csv
            self.analize(self.data_path)


    #En esta funcion vamos a analizar los datos de un dataframe
    def analize(self, path):
        df = pd.read_csv(path)
        df.drop('Notes', inplace=True, axis=1)
        df.dropna(inplace=True)
        df['id'] = range(len(df))
        print(len(df))
        try: 
            df['Attendance'] = df['Attendance'].str.replace(',', '').astype(float) / 1000
        except:
            pass

        try:
            df.drop('Last 5', inplace=True, axis=1)
        except:
            pass
        #Obtenemos la temporada de cada champions y lo añadimos al nombre del equipo, para diferenciar entre temporadas
        year = path.split('/')[2].split('_')[1].split('.')[0]
        if not df['Squad'].str.contains(year).any():
            df['Squad'] = df['Squad'] + ' ' + year

        df.to_csv(path, index=False)

    
    #Funcion para obtener el dataframe final
    def get_final_data(self):
        dfs = []
        contador = 0
        for csv in self.rutas:
            data_path = self.ruta + '/' + csv
            print(data_path)
            df = pd.read_csv(data_path)
            df['id'] = range(contador, contador + len(df))
            dfs.append(df)
            contador += len(df)
        final_df = pd.concat(dfs)

        final_df.drop(['xG','xGA','xGD','xGD/90'], axis=1, inplace=True)
        final_df['Rk'] = final_df['Rk'].apply(self.get_ucl_rk)
        df_predictions = final_df.tail(32)
        final_df = final_df.iloc[:-32]   
        final_df.to_csv('UEFA_Analisis_CSV/UEFA_Final_Data.csv', index=False)
        df_predictions.to_csv('UEFA_Analisis_CSV/UEFA_Target.csv', index=False)
    

    #Funcion para obtener el ranking de la champions
    def get_ucl_rk(self, standing: str):
        if standing == 'GR':
            return 1
        elif standing == 'R16':
            return 2
        elif standing == 'QF':
            return 3
        elif standing == 'SF':
            return 4
        elif standing == 'F':
            return 5
        else:
            return 6