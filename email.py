import os
import random
import time
import json
from datetime import datetime

def clear_cache():
    """Nettoyer le cache via Termux"""
    os.system("termux-notification -t 'Nettoyage en cours'")
    os.system("pm clear com.google.android.gms")
    os.system("pm clear com.google.android.gsf")
    time.sleep(2)

def generate_random_details():
    """Générer des données aléatoires"""
    first_names = ["Alex", "Jean", "Marie", "Thomas"]
    last_names = ["Dupont", "Martin", "Bernard", "Dubois"]
    return {
        'first_name': random.choice(first_names),
        'last_name': random.choice(last_names),
        'day': random.randint(1, 28),
        'month': random.randint(1, 12),
        'year': random.randint(1980, 2000)
    }

def simulate_swipe(duration=500):
    """Simuler un swipe"""
    os.system(f"termux-sensor -s accelerometer -d 100 -n 1")
    time.sleep(duration/1000)

def create_account(email, password):
    try:
        details = generate_random_details()
        
        # Ouvrir les paramètres
        os.system("termux-toast 'Ouvrir les paramètres manuellement'")
        input("Ouvrez manuellement Paramètres > Comptes > Ajouter un compte Google. Appuyez sur Entrée quand c'est fait...")
        
        # Remplir le formulaire
        os.system(f"termux-dialog text -t 'Prénom' -i '{details['first_name']}'")
        simulate_swipe()
        
        os.system(f"termux-dialog text -t 'Nom' -i '{details['last_name']}'")
        simulate_swipe()
        
        # Date de naissance
        os.system(f"termux-dialog text -t 'Jour' -i '{details['day']}'")
        simulate_swipe()
        os.system(f"termux-dialog text -t 'Mois' -i '{details['month']}'")
        simulate_swipe()
        os.system(f"termux-dialog text -t 'Année' -i '{details['year']}'")
        simulate_swipe()
        
        # Email et mot de passe
        os.system(f"termux-dialog text -t 'Email' -i '{email}'")
        simulate_swipe()
        os.system(f"termux-dialog text -t 'Mot de passe' -i '{password}'")
        simulate_swipe()
        os.system(f"termux-dialog text -t 'Confirmer mot de passe' -i '{password}'")
        
        # Fin du processus
        os.system("termux-toast 'Completez manuellement les dernières étapes'")
        print(f"Compte créé : {email}")
        return True
        
    except Exception as e:
        print(f"Erreur : {str(e)}")
        return False

if __name__ == "__main__":
    # Installer les dépendances Termux-API si nécessaire
    if not os.path.exists("/data/data/com.termux/files/usr/bin/termux-api"):
        print("Veuillez installer Termux-API depuis le Play Store")
        print("Puis exécutez: pkg install termux-api")
        exit()

    email = input("Entrez l'email : ")
    password = input("Entrez le mot de passe : ")
    
    clear_cache()
    if create_account(email, password):
        with open("accounts.txt", "a") as f:
            f.write(f"{email}:{password}\n")
        print("Compte enregistré dans accounts.txt")
