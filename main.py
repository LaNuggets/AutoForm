from connection import *
from send import *
from get_data import *

driver = openUrl()
connection(driver)
    
firstName, lastName, sexe, birthday, pays, adresse, code_postal, ville, mail = chipData()
    
for x in range(len(lastName)):
    resp = input("New candidates ? ")
    if resp == "n":
        break
    driver = sendNames(driver, lastName[x], firstName[x])
    
    already_Exists = input("This candidates already exists ? y or n: ")
    if already_Exists == "n":
        driver = sendAllData(driver,sexe[x], birthday[x], pays[x], adresse[x], code_postal[x], ville[x], mail[x])
    elif already_Exists == "y":
        print("for test")
        driver = sendMail(driver, mail[x])
driver.quit()
