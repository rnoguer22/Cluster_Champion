import os
from time import sleep
from Web_Scrapping.lanzador_scrapping import LanzadorScrapping
from Clusters.lanzador_cluster import Lanzador_Cluster
from UEFA_Predictions.lanzador_predict import LanzadorPredict



def limpiar_pantalla():
    import os
    import platform
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def iniciar():
    while True:
        def start():
            limpiar_pantalla()
            print("========================")
            print(" Welcome to the Manager Menu!!! ")
            print("========================")
            print("[1] Web Scrapping")
            print("[2] Clusters ")
            print("[3] Predictions") #Time series, Monte Carlo, Linear Regression with Spark
            print("[4] LangChain")        
            print("[5] IMG Classifier")
            print("[6] Close ")
            print("========================")
            opcion = input("> ")
            limpiar_pantalla()
            return opcion

        opcion = start()

        if opcion == '1':
            lanzador_scrapping = LanzadorScrapping()
            print('========================')
            print(' Choose the web scrapping you want to launch:')
            print('========================')
            print('[1] Update actual Champions League Standings')
            print('[2] Scrap players')
            print('[3] Scrapping playmakers')
            print('[4] Scrapping goalkeepers')
            print('[5] Scrapping Champions League team logos')
            print('[6] Exit')
            print('========================')
            opcion_scrapping = input('> ')
            limpiar_pantalla()
            if opcion_scrapping == '1':
                lanzador_scrapping.lanzar_actualizacion_scrapping()
                lanzador_scrapping.lanzar_analisis_scrapped_data()
            elif opcion_scrapping == '2':
                lanzador_scrapping.lanzar_scrap_players()
            elif opcion_scrapping == '3':
                lanzador_scrapping.lanzar_scrap_pass()
            elif opcion_scrapping == '4':
                lanzador_scrapping.lanzar_scrap_gks()
            elif opcion_scrapping == '5':
                lanzador_scrapping.lanzar_scrap_logos()
            elif opcion_scrapping == '6':
                start()
            else:
                print('Invalid option')
            input('Press Enter to continue...')


        if opcion == '2':
            lanzador_cluster = Lanzador_Cluster()
            print('========================')
            print(' Choose the cluster/syou want to launch:')
            print('========================')
            print('[1] KMeans')
            print('[2] Mean Shift')
            print('[3] Mini Batch')
            print('[4] DBSCAN')
            print('[5] OPTICS')
            print('[6] HDBSCAN')
            print('[7] GMM')
            print('[8] Agglomerative')
            print('[9] All')
            print('[10] Exit')
            print('========================')
            opcion_cluster = input('> ')
            limpiar_pantalla()
            if opcion_cluster == '1':
                lanzador_cluster.lanzar_kmeans()
            elif opcion_cluster == '2':
                lanzador_cluster.lanzar_mean_shift()
            elif opcion_cluster == '3':
                lanzador_cluster.lanzar_minibatch()
            elif opcion_cluster == '4':
                lanzador_cluster.lanzar_dbscan()
            elif opcion_cluster == '5':
                lanzador_cluster.lanzar_optics()
            elif opcion_cluster == '6':
                lanzador_cluster.lanzar_hdbscan()
            elif opcion_cluster == '7':
                lanzador_cluster.lanzar_gmm()
            elif opcion_cluster == '8':
                lanzador_cluster.lanzar_agglomerative()
            elif opcion_cluster == '9':
                lanzador_cluster.launch_all_clusters()
            elif opcion_cluster == '10':
                start()
            else:
                print('Invalid option')
            input('Press Enter to continue...')
            

        if opcion == '3':
            lanzador_predict = LanzadorPredict()
            print('========================')
            print(' Choose the prediction/s you want to launch:')
            print('========================')
            print('[1] Random Forest')
            print('[2] Gradient Boosting')
            print('[3] Autoregressive')
            print('[4] Exponential Smoothing')
            print('[5] ARIMA')
            print('[6] SARIMAX')
            print('[7] Linear Regression')
            print('[8] Monte Carlo')
            print('[9] All')
            print('[10] Exit')
            print('========================')
            opcion_predict = input('> ')
            limpiar_pantalla()
            if opcion_predict == '1':
                print(lanzador_predict.lanzar_randomforest())
            elif opcion_predict == '2':
                print(lanzador_predict.lanzar_gradientboosting())
            elif opcion_predict == '3':
                print(lanzador_predict.lanzar_autoregressive())
            elif opcion_predict == '4':
                print(lanzador_predict.lanzar_exponentialsmoothing())
            elif opcion_predict == '5':
                print(lanzador_predict.lanzar_arima())
            elif opcion_predict == '6':
                print(lanzador_predict.lanzar_sarimax())
            elif opcion_predict == '7':
                print(lanzador_predict.lanzar_linear_regression())
            elif opcion_predict == '8':
                print(lanzador_predict.lanzar_monte_carlo())
            elif opcion_predict == '9':
                print(lanzador_predict.launch_all())
            elif opcion_predict == '10':
                start()
            else:
                print('Invalid option')
            input('Press Enter to continue...')


        if opcion == '4':
            print("Launching LangChain...")
            print('Lanchaing does not work properly :(')
            print('Moyis needs to update it to Llama 3')
            sleep(3)
            start()

        if opcion == '5':
            print('Launching IMG Classifier...')
            print('IMG Classifier does not work properly :(')
            sleep(3)
            start()

        if opcion == '6':
            print('Bye bye!!!')
            sleep(2)
            break