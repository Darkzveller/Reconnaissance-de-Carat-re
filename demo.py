# lien vers video : https://www.youtube.com/watch?v=CRDYO3Pu584&ab_channel=Codigo
# https://github.com/JaidedAI/EasyOCR 
# pip3 install easyocr
# lien vers video : https://www.youtube.com/watch?v=2qK2W7ZM4g4&ab_channel=Arthurus
# pip install pyautogui

# Importation de la bibliotheque permettant d'utiliser les delais
import time
# Importation de la bibliotheque permettant de faire une capture d'écran
import pyautogui
# Importation de la bibliotheque permettant d'utiliser les recherche internet
import webbrowser
# Importation de la bibliotheque permmettant d'effectuer le traitement d'image
import easyocr
from PIL import Image, ImageDraw, ImageFont

# Ouvrir le lien dans un navigateur web
webbrowser.open("https://www.snapchat.com/add/naslachiente/dX6SMH4gRGOdtCKqVvUksAAAgZWJpaXBqcW9wAY_5bZPtAY_5bY0rAAAAAA")
# Attendre 15 secondes pour que la page se charge
time.sleep(15)


fichier = 'img.png'
# effectue la capture d'écran
screen = pyautogui.screenshot()
# Enregistrer la capture d'écran
screen.save(fichier)

# Initialiser le lecteur OCR
reader = easyocr.Reader(['fr'])

# Lire le texte à partir de l'image
result = reader.readtext(fichier)

# Charger l'image avec PIL
image_pil = Image.open(fichier)
draw = ImageDraw.Draw(image_pil)
font = ImageFont.load_default()  # Utiliser la police par défaut

for (haut, droite, bas, gauche), mot, p in result:
    print(mot)
    #print(haut, bas, mot)
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
