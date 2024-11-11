import time
import unicodedata
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def sendNames(driver, lastName, firstName):
    add_adh = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_btnAddMember")
    add_adh.click()
    
    time.sleep(1)
    
    prenom_input = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_txtPrenom")
    prenom_input.send_keys(firstName)

    lastName_input = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_txtNom")
    lastName_input.send_keys(lastName)

    find = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_btnOk")
    find.click()
    return driver

def sendMail(driver, mail):
    mail_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtEmail")
    mail_input.send_keys(mail)
    return driver

def sendAllData(driver, sexe, birthday, pays, adresse, code_postal, ville, mail):
    #sexe
    if sexe == "Féminin":
        sexe_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbMme" )
        sexe_input.click()
    elif sexe == "Masculin":
        sexe_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbMr" )
        sexe_input.click()

    #Date de naissance 
    birthday_obj = datetime.strptime(birthday, "%Y-%m-%d")
    
    birthday_form = birthday_obj.strftime("%d-%m-%Y")

    time.sleep(1)
    birthday_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_txtNaissance")
    birthday_input.click()

    birthday_input.send_keys(Keys.HOME)
    time.sleep(1)
    
    action = ActionChains(driver)

    for char in birthday_form:
        action.send_keys(char)
        action.pause(0.1)
    action.perform()

    #Actualisation (ne sert a rien d'autre)
    maj = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_txtPrenom2")
    maj.click()
    time.sleep(1)
    
    #Adresse
    adresse_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtAdresse1")
    adresse_input.send_keys(adresse)

    #Pays
    if pays == "99":
        pays_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbNeEnFranceNon")
        pays_input.click()
        
    #code Postal
    code_postal_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtCP")
    code_postal_input.send_keys(code_postal)

    #Actualisation (ne sert a rien d'autre)
    maj = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_txtPrenom2")
    maj.click()
    time.sleep(1)

    #ville
    try:
        ville_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_cmbSelectVille")
        select = Select(ville_input)
        
        ville = noAccents(ville)
        select.select_by_visible_text(ville.upper())
    
    except Exception as e:
        print(f"Error : {e}")

    mail_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtEmail")
    mail_input.send_keys(mail)

    return driver

def noAccents(texte):
    texte_norme = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(char for char in texte_norme if unicodedata.category(char) != 'Mn')
    return texte_sans_accents
