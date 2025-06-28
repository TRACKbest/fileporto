import os
import random
import time
from datetime import datetime

def clear_cache():
    """Nettoyer le cache via Termux"""
    os.system("pm clear com.google.android.gms")
    os.system("pm clear com.google.android.gsf")
    time.sleep(2)

def generate_random_name():
    first_names = ["Alex", "Jean", "Marie", "Thomas"]
    return random.choice(first_names)

def generate_random_lastname():
    last_names = ["Dupont", "Martin", "Bernard"]
    return random.choice(last_names)

def create_account(email, password):
    try:
        # Ouvrir les paramètres de création de compte
        os.system("am start -a android.settings.ADD_ACCOUNT_SETTINGS")
        time.sleep(3)
        
        # Ces commandes simulent les touches (ajustez selon votre appareil)
        os.system("input keyevent 20 20 66")  # Sélectionne Google
        time.sleep(2)
        
        # Remplissage automatique
        first_name = generate_random_name()
        last_name = generate_random_lastname()
        
        os.system(f"input text '{first_name}'")
        os.system("input keyevent 61")  # Tab
        os.system(f"input text '{last_name}'")
        os.system("input keyevent 61")  # Tab
        
        # Date de naissance aléatoire
        os.system("input text '01'")  # Jour
        os.system("input keyevent 61")  # Tab
        os.system("input text '01'")  # Mois
        os.system("input keyevent 61")  # Tab
        os.system("input text '1990'")  # Année
        os.system("input keyevent 61")  # Tab
        
        # Email et mot de passe
        os.system(f"input text '{email}'")
        os.system("input keyevent 61")  # Tab
        os.system(f"input text '{password}'")
        os.system("input keyevent 61")  # Tab
        os.system(f"input text '{password}'")  # Confirmation
        
        # Fin du processus
        os.system("input keyevent 61 61 66")  # Passer la vérification
        time.sleep(2)
        os.system("input tap 500 1200")  # Accepter les conditions
        
        print(f"Compte créé : {email}")
        return True
        
    except Exception as e:
        print(f"Erreur : {str(e)}")
        return False

if __name__ == "__main__":
    email = input("Entrez l'email : ")
    password = input("Entrez le mot de passe : ")
    
    clear_cache()
    if create_account(email, password):
        with open("accounts.txt", "a") as f:
            f.write(f"{email}:{password}\n")
        print("Compte enregistré !")
