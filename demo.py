
# lien vers video : https://www.youtube.com/watch?v=CRDYO3Pu584&ab_channel=Codigo
# https://github.com/JaidedAI/EasyOCR 
# pip3 install easyocr
# lien vers video : https://www.youtube.com/watch?v=2qK2W7ZM4g4&ab_channel=Arthurus
# pip install pyautogui
# pip install keyboard
# # Importation de la bibliotheque permettant d'utiliser les delais
import time
# Importation de la bibliotheque permettant de faire une capture d'écran
import pyautogui
# Importation de la bibliotheque permettant d'utiliser les recherche internet
import webbrowser
# Importation de la bibliotheque permmettant d'effectuer le traitement d'image
import easyocr
from PIL import Image, ImageDraw, ImageFont
import keyboard  # Module pour gérer les entrées clavier

from io import BytesIO
from playwright.sync_api import sync_playwright
import pyautogui
import re

# Ouvrir le lien dans un navigateur web
#webbrowser.open("https://www.snapchat.com/add/naslachiente/dX6SMH4gRGOdtCKqVvUksAAAgZWJpaXBqcW9wAY_5bZPtAY_5bY0rAAAAAA")

webbrowser.open("https://www.laymoon.fr/wp-content/uploads/2024/06/application-carte-2-min-PhotoRoom-4-1.png")

# Attendre 5 secondes pour que la page se charge
time.sleep(5)
fichier = 'img.png'
fichier_test = 'Carte_bancaire_Visa.png'
fichier =fichier_test
print('finish init')


# Initialiser le lecteur OCR
reader = easyocr.Reader(['fr'])
i= 0
nbr_code_carte= [None] * 5
date_expiration = ' '
def process_image():
    #x =  516
    #y = 223
    #width = 451
    #height = 734
    compteur = 0
    x = 700
    y = 400
    width = 400
    height = 250
    # Prendre une capture d'écran
    screen = pyautogui.screenshot(region=(x, y, width, height))
    #screen = pyautogui.screenshot()

    screen.save(fichier)

    # Lire le texte à partir de l'image
    result = reader.readtext(fichier)
    
    # Charger l'image avec PIL
    image_pil = Image.open(fichier)
    draw = ImageDraw.Draw(image_pil)
    font = ImageFont.load_default()  # Utiliser la police par défaut
    
    # Parcourir les résultats et dessiner les rectangles et le texte
    for (haut, droite, bas, gauche), mot, p in result:
        #Affiche les coordoone du mot trouver
        #print(haut, bas, mot)
        #Affiche le mot trouver
        #print(mot)
        #resultats = re.findall(r'\d+', mot)
       # print(resultats)
        if len(mot)==4 and mot.isdigit():
             #print(mot)
             
            compteur = compteur +1
                  #print("La chaîne ne contient que des chiffres.")
                  #print(mot)
            nbr_code_carte[compteur] = mot
            print(nbr_code_carte[compteur])
             
        else :
             #print("La chaîne ne contient pas exactement 4 caractères.Mais voici les caractère lu ")
             #print(mot)
             print('cc')
        if re.match(r'\d{2}/\d{2}', mot):
             date_expiration = mot
             print(f"La chaîne '{date_expiration}' est au format 'dd/mm'.")
             
        

        draw.rectangle([haut[0], haut[1], bas[0], bas[1]], outline=(0, 0, 255))

        # Utiliser textbbox pour obtenir la taille du texte
        bbox = draw.textbbox((0, 0), mot, font=font)
        largeur_texte = bbox[2] - bbox[0]
        hauteur_texte = bbox[3] - bbox[1]

        # Dessiner un rectangle rempli pour le texte
        draw.rectangle([haut[0], bas[1] - hauteur_texte - 10, bas[0], bas[1]], fill=(0, 0, 0))
        # Dessiner le texte
        draw.text((haut[0] + 6, bas[1] - hauteur_texte - 5), mot, fill=(255, 255, 255, 255), font=font)

    # Afficher l'image résultante
    image_pil.show()
    

# Boucle infinie pour traiter les images
while True:
        
        if i ==0 :
             process_image()
             i=1
             print('stop')
    
