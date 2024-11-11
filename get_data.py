import pandas as pd

def chipData():
    file = "list.xlsx"
    try:
        df = pd.read_excel(file)
    except Exception:
        print("Je n'ai pas trouvé le fichier excel. je cherche \"list.xlsx\" dans le répairtoire où je suis\n")
    c = df.columns.tolist()
    #columns def
    firstName = df[c[0]]
    lastName = df[c[1]]
    sexe = df[c[2]]
    birthday = df[c[3]]
    pays = df[c[4]]
    adresse = df[c[5]]
    code_postal = df[c[6]]
    ville = df[c[7]]
    mail = df[c[10]]
    #
    return firstName, lastName, sexe, birthday, pays, adresse, code_postal, ville, mail
