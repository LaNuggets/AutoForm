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
    try:
        add_adh = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_btnAddMember")
        add_adh.click()
    except Exception:
        print("Erreur, je n'ai pas trouvé le bouton \"Ajouter un.e adhérent.e\" sur la page \"Gérer les adhérents.es\"\n")
    
    time.sleep(1)
    try:
        prenom_input = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_txtPrenom")
        prenom_input.send_keys(firstName)
    except Exception:
        print("Erreur lors du remplissage du Prénom\n")

    try:
        lastName_input = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_txtNom")
        lastName_input.send_keys(lastName)
    except Exception:
        print("Erreur lors du remplissage du Nom\n")

    try:
        find = driver.find_element(By.ID, "ctl00_ctl00_MasterContent_content_ucCreationPersonne_ucSaisieNomPrenom_btnOk")
        find.click()
    except Exception:
        print("Erreur je n'ai pas trouvé le bouton \"Continuer\" pour ajouter un.e adhérent.e \n")

    return driver

def sendMail(driver, mail):
    try:
        mail_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtEmail")
        mail_input.send_keys(mail)
    except Exception as e:
        print("Erreur lors du remplissage de l'adresse mail")
    return driver

def sendAllData(driver, sexe, birthday, pays, adresse, code_postal, ville, mail):
    try:
        #sexe
        if sexe == "Féminin":
            sexe_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbMme" )
            sexe_input.click()
        elif sexe == "Masculin":
            sexe_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbMr" )
            sexe_input.click()
    except Exception:
        print("Erreur lors de la selection du genre\n")

    try:
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
    except Exception:
        print("Erreur lors du remplissage de la date de naissance\n")

    try:
        #Actualisation (ne sert a rien d'autre)
        maj = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_txtPrenom2")
        maj.click()
        time.sleep(1)
    except Exception:
        print("Erreur lors de l'actualisation\n")

    try:
        #Adresse
        adresse_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtAdresse1")
        adresse_input.send_keys(adresse)
    except Exception:
        print("Erreur lors du remplissage de l'adresse\n")

    try:
        #Pays
        if pays == "99":
            pays_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_rdbNeEnFranceNon")
            pays_input.click()
    except Exception:
        print("Erreur lors de la selection du pays\n")

    try:
        #code Postal
        code_postal_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtCP")
        code_postal_input.send_keys(code_postal)
    except Exception:
        print("Erreur lros du remplissage du code Postal\n")
        
    try:
        #Actualisation (ne sert a rien d'autre)
        maj = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_txtPrenom2")
        maj.click()
        time.sleep(1)
    except Exception:
        print("Erreur lors de l'actualisation\n")

    #ville
    try:
        ville_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_cmbSelectVille")
        select = Select(ville_input)
        
        ville = noAccents(ville)
        select.select_by_visible_text(ville.upper())
    
    except Exception:
        print("Erreur lors de la selection de la ville\n")

        
    try:
        mail_input = driver.find_element(By.ID, "MasterContent_content_ucAdhesion_ucAdhesionFormulaire_ppInformations_ucAdresse_txtEmail")
        mail_input.send_keys(mail)
    except Exception:
        print("Erreur lors du remplissage du mail\n")

    return driver

def noAccents(texte):
    texte_norme = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(char for char in texte_norme if unicodedata.category(char) != 'Mn')
    return texte_sans_accents
