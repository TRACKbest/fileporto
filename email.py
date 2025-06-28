import os
import random
import time
from datetime import datetime

def clear_cache():
    """Nettoyer le cache de Google Play Services"""
    os.system("adb shell pm clear com.google.android.gms")
    os.system("adb shell pm clear com.google.android.gsf")
    time.sleep(2)

def generate_random_name():
    """Générer un prénom aléatoire"""
    first_names = ["Alex", "Jean", "Marie", "Thomas", "Sophie", "Pierre", "Laura", "Nicolas"]
    return random.choice(first_names)

def generate_random_lastname():
    """Générer un nom aléatoire"""
    last_names = ["Dupont", "Martin", "Bernard", "Dubois", "Moreau", "Laurent", "Simon", "Michel"]
    return random.choice(last_names)

def generate_random_birthdate():
    """Générer une date de naissance aléatoire (18-60 ans)"""
    current_year = datetime.now().year
    birth_year = random.randint(current_year - 60, current_year - 18)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    return birth_day, birth_month, birth_year

def create_google_account(email, password):
    """Créer un compte Google avec email et mot de passe spécifiés"""
    # Générer des données aléatoires pour les autres champs
    first_name = generate_random_name()
    last_name = generate_random_lastname()
    day, month, year = generate_random_birthdate()
    
    # Ouvrir les paramètres Android
    os.system("adb shell am start -a android.settings.ADD_ACCOUNT_SETTINGS")
    time.sleep(3)
    
    # Sélectionner Google
    os.system("adb shell input tap 500 500")  # Ajuster les coordonnées
    time.sleep(2)
    
    # Cliquer sur "Créer un compte"
    os.system("adb shell input tap 500 800")  # Ajuster les coordonnées
    time.sleep(2)
    
    # Remplir le formulaire
    # Prénom
    os.system(f"adb shell input text '{first_name}'")
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Nom
    os.system(f"adb shell input text '{last_name}'")
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Date de naissance
    os.system(f"adb shell input text '{day}'")  # Jour
    os.system("adb shell input keyevent 61")  # Tab
    os.system(f"adb shell input text '{month}'")  # Mois
    os.system("adb shell input keyevent 61")  # Tab
    os.system(f"adb shell input text '{year}'")  # Année
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Genre
    os.system("adb shell input keyevent 61")  # Tab
    os.system("adb shell input keyevent 61")  # Tab
    os.system("adb shell input keyevent 66")  # Entrer (Homme)
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Email (celui que vous avez spécifié)
    os.system(f"adb shell input text '{email}'")
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Mot de passe (celui que vous avez spécifié)
    os.system(f"adb shell input text '{password}'")
    os.system("adb shell input keyevent 61")  # Tab
    os.system(f"adb shell input text '{password}'")  # Confirmation
    os.system("adb shell input keyevent 61")  # Tab
    time.sleep(1)
    
    # Passer l'étape du numéro de téléphone
    os.system("adb shell input keyevent 61")  # Tab
    os.system("adb shell input keyevent 61")  # Tab
    os.system("adb shell input keyevent 66")  # Entrer (Passer)
    time.sleep(2)
    
    # Accepter les conditions
    os.system("adb shell input tap 500 1200")  # Ajuster les coordonnées
    os.system("adb shell input keyevent 61")  # Tab
    os.system("adb shell input keyevent 66")  # Entrer
    time.sleep(5)
    
    print(f"Compte créé avec succès: {email}")
    return True

def main():
    print("Script de création de compte Google avec données personnalisées")
    
    # Vérifier la connexion ADB
    if os.system("adb devices") != 0:
        print("Erreur: ADB n'est pas configuré correctement.")
        return
    
    # Demander les informations du compte
    email = input("Entrez l'email pour le compte Google: ")
    password = input("Entrez le mot de passe pour le compte Google: ")
    
    clear_cache()
    try:
        success = create_google_account(email, password)
        if success:
            with open("custom_accounts.txt", "a") as f:
                f.write(f"{email}:{password}\n")
            print("Compte enregistré dans custom_accounts.txt")
    except Exception as e:
        print(f"Erreur lors de la création du compte: {str(e)}")
    
    print("\nProcessus terminé!")

if __name__ == "__main__":
    main()