from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

os.system('clear')

def mostrar_menu():
   print("██╗ ██████╗ ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ ")
   print("██║██╔════╝ ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗")
   print("██║██║  ███╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝")
   print("██║██║   ██║██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗")
   print("██║╚██████╔╝██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║")
   print("╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
                                                                           
   print("                                                                       ")
   print("                    Made In Hell                                        ")
   print("                Created by RIP-Network                                 ")
   print("                    Version 1.0                                         ")
   print("")
   print("1. Informacion de un usuario (Free Version)")
   print("2. Informacion de un usuario (Premiun Version)")
   print("3. Bypassear cuenta privada (Premiun Version)")
   print("4. Salir")
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
        browser.quit()

        os.system('clear')

        banner = r'''
    
        ██  ██████  ██ ███    ██      ██ ███████  ██████ ████████  ██████  ██████  
        ██ ██       ██ ████   ██      ██ ██      ██         ██    ██    ██ ██   ██ 
        ██ ██   ███ ██ ██ ██  ██      ██ █████   ██         ██    ██    ██ ██████  
        ██ ██    ██ ██ ██  ██ ██ ██   ██ ██      ██         ██    ██    ██ ██   ██ 
        ██  ██████  ██ ██   ████  █████  ███████  ██████    ██     ██████  ██   ██ 
                                                                           
                       Made In Hell
                    Created by RIP-Network
                                                    
        '''
        print("")
        print("Information about : " + v + " ( Free Version ) ")
        print("//////////////////////////////////////////////////////////////")
        print("Nombre :", frase1)
        print("Publicaciones :", frase2)
        print("Seguidores :", frase3)
        print("Seguidos :", frase4)
        print("Nickname :", frase5)
        print("Descripcion :", frase6)
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
        print("Email or Number :", verify)
        print("Creacion de la Cuenta : *********** ")
        print("Primeros 10 seguidores : ********************** ")
        print("Ultimos 10 seguidores : ********************** ")
        print("Hastags de las publicaciones : **************************** ")
        print("Informacion de ubicacion de las publicaciones : ********************** ")
        print("//////////////////////////////////////////////////////////////")
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
        os.system('clear')
        print("Gracias por usarme.")
        break
    else:
        print("Opción inválida.")

