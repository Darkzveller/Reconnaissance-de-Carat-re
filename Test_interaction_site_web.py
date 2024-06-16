#Coucou batard
from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ldlc.com/")
    page.click(".icon.icon-user")
    page.fill("#Email", "dzvellox@gmail.com")
    page.wait_for_timeout(3000)
    page.fill(".input-group input", "Dark2008@")
    page.wait_for_timeout(4000)
    page.wait_for_selector(".button")
    page.click("form button.button")
    page.wait_for_timeout(2000)
    page.click(".icon.icon-basket")
    page.wait_for_timeout(1500)
    page.click(".maxi.color2.noMarg")

    motifs_trouves = "1234 5678 9012 3456"
    motif_compose ="11/22"
    #prenon
    Card_Holder = "nasdas"
    motif_cvv = "234"
    




    
    #a refaire cette partir puisque system de payment ne marche pas
    page.wait_for_load_state("networkidle")  # Attendre que la page soit chargée
    time.sleep(2)
    for x in range (1,3):
        page.keyboard.press("End")
        print('scrolling', x) 
    time.sleep(5)
    page.mouse.click(508, 592)

    #page.wait_for_selector(".sdpx-hosted-cardNumber")  # Attendre que l'élément soit présent
    #page.click(".sdpx-hosted-cardNumber")  # Cliquer sur l'élément
    #page.fill(".sdpx-hosted-cardNumber", motifs_trouves)  # Remplir le champ

    
#   #page.wait_for_selector("#sdpx-hosted-cardExpiryDate")
    #page.fill("#sdpx-hosted-cardExpiryDate", motif_compose)
#
    page.wait_for_selector("#CardHolder")
    page.fill("#CardHolder", "nasdas")
#
    time.sleep(5)
    print('iiiiiiiiiiiiiiiiiiiiiiiiIIIIIIIIIIIiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
#Je ne trouve pas els coordonnées de la case
    #for d in range(0,900):
    #    page.mouse.click(d, 592)
    #    print(d)
    #    time.sleep(0.1)
    #print('iiiiiiiiiiiiiiiiiiiiiiiiIIIIIIIIIIIiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    #page.wait_for_selector("#sdpx-hosted-cardCvc")
    #print('iiiiiiiiiiiiiiiiiiiiiiiiIIIIIIIIIIIiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    #page.fill("#sdpx-hosted-cardCvc", "456" )
    #print('iiiiiiiiiiiiiiiiiiiiiiiiIIIIIIIIIIIiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

    time.sleep(100)
    page.screenshot(path="example.png")
    page.wait_for_timeout(20000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
