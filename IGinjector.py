from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'


os.system('clear')

def mostrar_menu():
   print(rojo+"                       #################################################################################   "+cierre)
   print(rojo+"                       #                                                                               #    "+cierre)
   print(rojo+"                       #   ██╗ ██████╗ ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗  #   "+cierre)
   print(rojo+"                       #   ██║██╔════╝ ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗ #   "+cierre)
   print(rojo+"                       #   ██║██║  ███╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝ #   "+cierre)
   print(rojo+"                       #   ██║██║   ██║██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗ #    "+cierre)
   print(rojo+"                       #   ██║╚██████╔╝██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║ #    "+cierre)
   print(rojo+"                       #   ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ #    "+cierre)
   print(rojo+"                       #################################################################################")                                                                        
   print("                                                                          ")
   print(rojo+"                                                        💥 Made In Hell 💥                                      "+cierre)
   print(rojo+"                                                    ☠ Created by RIP-Network ☠                                "+cierre)
   print(rojo+"                                                         ✓ Version 2.5 ✓                                       "+cierre)
   print("")
   print(rojo+"           [ADVERTENCIA] Es posible que la herramienta haga 3 scaneos luego no funcione, dejela reposar. [ADVERTENCIA]")
   print("")
   print("")
   print(rojo+"                        [*] 1. Informacion de un usuario"+cierre + rojo+" (Free Version)"+cierre)
   print("")
   print(rojo+"                        [*] 2. Informacion de un usuario"+cierre + rojo+" (Premiun Version)"+cierre)
   print("")
   print(rojo+"                        [*] 3. Bypassear cuenta privada"+cierre + rojo+" (Premiun Version)"+cierre)
   print("")
   print(rojo+"                        [*] 4. Buscar nuevas actualizaciones                                                                          ")
   print("")
   print(rojo+"                        [*] 5. Salir")
   print("")
   print("")

opcion = 0

while opcion != 3:
    mostrar_menu()
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:

        print("")
        v=input("Usuario de Instagram : ")
        print("")

        url = f"https://www.instagram.com/{v}"
        url2 = f"https://www.instagram.com/accounts/password/reset/"


        browser = webdriver.Chrome()
        browser.get(url2)
        sleep(4)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click
        sleep(3)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input').send_keys(v)
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[5]/div').click
        sleep(2)
        c=input("Pulse enter cuando acepte el capcha y continue.")
        sleep(4)
        elemento = browser.find_element_by_xpath('/html/body/div[1]/section/main/div[2]/div/div/div/div[2]/div/div')
        verify = elemento.text
        browser.quit()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        sleep(4)

        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/div[1]/a/h2')
        frase1 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button')
        frase2 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
        frase3 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button')
        frase4 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/div/span')
        frase5 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/h1')
        frase6 = elemento.text
        elemento = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/a/div')
        frase7 = elemento.text
        browser.quit()

        os.system('clear')

        print(rojo+"                       #################################################################################   "+cierre)
        print(rojo+"                       #                                                                               #    "+cierre)
        print(rojo+"                       #   ██╗ ██████╗ ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗  #   "+cierre)
        print(rojo+"                       #   ██║██╔════╝ ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗ #   "+cierre)
        print(rojo+"                       #   ██║██║  ███╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝ #   "+cierre)
        print(rojo+"                       #   ██║██║   ██║██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗ #    "+cierre)
        print(rojo+"                       #   ██║╚██████╔╝██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║ #    "+cierre)
        print(rojo+"                       #   ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ #    "+cierre)
        print(rojo+"                       #################################################################################")                                                                        


        print("")
        print("Information about : " + v + " ( Free Version ) ")
        print("//////////////////////////////////////////////////////////////")
        print("Nombre :", frase1)
        print("Publicaciones :", frase2)
        print("Seguidores :", frase3)
        print("Seguidos :", frase4)
        print("Nickname :", frase5)
        print("Descripcion :", frase6)
        print("Enlaces :", frase7)
        print("Email :", verify)
        print("//////////////////////////////////////////////////////////////")
        print("")
        print("")
        print("Information about : " + v + " ( Premiun Version ) ")
        print("//////////////////////////////////////////////////////////////")
        print("URL de la Foto de Perfil : ********************** ")
        print("Nombre :", frase1)
        print("Publicaciones :", frase2)
        print("Seguidores :", frase3)
        print("Seguidos :", frase4)
        print("Nickname :", frase5)
        print("Descripcion :", frase6)
        print("Enlaces :", frase7)
        print("Email or Number :", verify)
        print("Creacion de la Cuenta : *********** ")
        print("Primeros 10 seguidores : ********************** ")
        print("Ultimos 10 seguidores : ********************** ")
        print("Hastags de las publicaciones : **************************** ")
        print("Informacion de ubicacion de las publicaciones : ********************** ")
        print("//////////////////////////////////////////////////////////////")
        print("")
        break

    elif opcion == 2:
        print("")
        print("Deberas pedir la version premiun.")
        print("")
        print("t.me/@RIPNetwork")
        sleep(8)
    elif opcion == 3:
        print("")
        print("Deberas pedir la version premiun.")
        print("")
        print("t.me/@RIPNetwork")
        sleep(8)
    elif opcion == 4:
        print("")
        print("Deberas pedir la version premiun.")
        print("")
        print("t.me/@RIPNetwork")
        sleep(8)
    elif opcion == 5:
        os.system('clear')
        print(rojo+"                       #################################################################################   "+cierre)
        print(rojo+"                       #                                                                               #    "+cierre)
        print(rojo+"                       #   ██╗ ██████╗ ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗  #   "+cierre)
        print(rojo+"                       #   ██║██╔════╝ ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗ #   "+cierre)
        print(rojo+"                       #   ██║██║  ███╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝ #   "+cierre)
        print(rojo+"                       #   ██║██║   ██║██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗ #    "+cierre)
        print(rojo+"                       #   ██║╚██████╔╝██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║ #    "+cierre)
        print(rojo+"                       #   ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ #    "+cierre)
        print(rojo+"                       #################################################################################")                                                                        

        print("                                                 Sigueme en mis redes sociales !")
        print("")
        print("                                           YT : https://youtube.com/@RIP-Network")
        print("                                           YT : https://youtube.com/@RIPNetwork ")
        print("                                           GH : https://github.com/RIP-Network  ")
        print("                                           IG : https://instagram.com/ripnetworkyt  ")
        break
    else:
        os.system('clear')
        print("Opción inválida.")
        sleep(5)
        os.system('clear')
