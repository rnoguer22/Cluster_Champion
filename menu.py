import os
from Ejercicio1.lanzador1 import main1
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
            main2()

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