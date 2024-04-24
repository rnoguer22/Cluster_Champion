import os
from Clusters.lanzador_cluster import Lanzador_Cluster
from Ejercicio2.lanzador2 import main2
from Ejercicio3.lanzador3 import main3
from Ejercicio3.lanzador3 import main4
from Ejercicio3.lanzador3 import main5



def limpiar_pantalla():
    import os
    import platform
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def iniciar():
    while True:
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

        if opcion == '1':
            main1()

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
            else:
                print('Invalid option')
            input("\nPress ENTER to continue...")
            


        if opcion == '3':
            main3()

        if opcion == '4':
            main4()

        if opcion == '5':
            main5()

        if opcion == '6':
            print("Bye bye!!!\n")
            break
    
        input("\nPress ENTER to continue...")

        limpiar_pantalla()