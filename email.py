import os
import random
import time
import re
import shutil
from datetime import datetime

# --- Couleurs terminal ---
class Colors:
    INFO = "\033[94m"
    OK = "\033[92m"
    WARN = "\033[93m"
    ERR = "\033[91m"
    RESET = "\033[0m"

# --- Outils ---
def run_cmd(command, delay=0.5):
    os.system(command)
    time.sleep(delay)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_strong_password(password):
    return len(password) >= 6

# --- Vérification fiable de termux-api ---
def check_termux_api():
    if shutil.which("termux-api") is None and shutil.which("termux-toast") is None:
        print(f"{Colors.ERR}❌ termux-api non détecté.{Colors.RESET}")
        print("Assure-toi d’avoir :")
        print("1. Installé le package Termux-API :")
        print("   → pkg install termux-api")
        print("2. Installé l’application Termux:API depuis F-Droid :")
        print("   → https://f-droid.org/packages/com.termux.api/")
        exit()
    else:
        print(f"{Colors.OK}✅ Termux API détecté avec succès.{Colors.RESET}")

# --- Nettoyage ---
def clear_cache():
    print(f"{Colors.INFO}Nettoyage du cache...{Colors.RESET}")
    run_cmd("termux-notification -t 'Nettoyage du cache en cours'")
    run_cmd("pm clear com.google.android.gms")
    run_cmd("pm clear com.google.android.gsf")
    print(f"{Colors.OK}Cache nettoyé avec succès.{Colors.RESET}")

# --- Données aléatoires ---
def generate_random_details():
    first_names = ["Alex", "Jean", "Marie", "Thomas"]
    last_names = ["Dupont", "Martin", "Bernard", "Dubois"]
    return {
        'first_name': random.choice(first_names),
        'last_name': random.choice(last_names),
        'day': random.randint(1, 28),
        'month': random.randint(1, 12),
        'year': random.randint(1980, 2000)
    }

# --- Simulation pause ---
def simulate_pause(duration=500):
    time.sleep(duration / 1000)

# --- Création de compte ---
def create_account(email, password):
    try:
        details = generate_random_details()

        print(f"{Colors.INFO}Veuillez ouvrir les paramètres : Paramètres > Comptes > Ajouter un compte Google{Colors.RESET}")
        input("Appuyez sur Entrée quand vous êtes prêt...")

        champs = [
            ("Prénom", details['first_name']),
            ("Nom", details['last_name']),
            ("Jour", str(details['day'])),
            ("Mois", str(details['month'])),
            ("Année", str(details['year'])),
            ("Email", email),
            ("Mot de passe", password),
            ("Confirmer mot de passe", password)
        ]

        for titre, valeur in champs:
            run_cmd(f"termux-dialog text -t '{titre}' -i '{valeur}'", delay=0.8)
            simulate_pause()

        run_cmd("termux-toast 'Complétez manuellement les dernières étapes'")
        print(f"{Colors.OK}Compte préparé : {email}{Colors.RESET}")
        return True

    except Exception as e:
        print(f"{Colors.ERR}Erreur : {str(e)}{Colors.RESET}")
        return False

# --- Programme principal ---
if __name__ == "__main__":
    check_termux_api()

    email = input("Entrez l'adresse email : ").strip()
    password = input("Entrez le mot de passe (min. 6 caractères) : ").strip()

    if not is_valid_email(email):
        print(f"{Colors.ERR}Email invalide.{Colors.RESET}")
        exit()

    if not is_strong_password(password):
        print(f"{Colors.ERR}Mot de passe trop court.{Colors.RESET}")
        exit()

    clear_cache()

    if create_account(email, password):
        with open("accounts.txt", "a") as f:
            f.write(f"{datetime.now()} - {email}:{password}\n")
        print(f"{Colors.OK}✅ Compte enregistré dans accounts.txt{Colors.RESET}")
    else:
        print(f"{Colors.ERR}❌ La création a échoué.{Colors.RESET}")
