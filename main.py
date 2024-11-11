from connection import *
from send import *
from get_data import *
import os

driver = openUrl()
connection(driver)
    
firstName, lastName, sexe, birthday, pays, adresse, code_postal, ville, mail = chipData()
    
for x in range(len(lastName)):
    os.system('cls' if os.name == 'nt' else 'clear')
    resp = input("Voulez vous entrer un.e nouveau.elle adhérent.e ? Allez sur la page \"Gérer les Adhérents.es\" et tapez y ou n:  ")
    if resp == "n":
        break
    driver = sendNames(driver, lastName[x], firstName[x])
    
    already_Exists = input("Cette adhérent.e exist t'il déjà ? Allez sur la Fiche de l'adhérent.e et tapez y ou n: ")
    if already_Exists == "n":
        driver = sendAllData(driver,sexe[x], birthday[x], pays[x], adresse[x], code_postal[x], ville[x], mail[x])
    elif already_Exists == "y":
        driver = sendMail(driver, mail[x])
driver.quit()
