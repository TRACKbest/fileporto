import os
import time
import json
import random
import requests
from generate_identity import generate_identity

class GoogleAccountCreator:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        }

    def clear_cache(self):
        """Nettoyer le cache des applications Google"""
        try:
            os.system("pm clear com.google.android.gms > /dev/null 2>&1")
            os.system("pm clear com.google.android.gsf > /dev/null 2>&1")
            time.sleep(3)
        except:
            pass

    def get_initial_params(self):
        """Récupérer les paramètres initiaux de création de compte"""
        url = "https://accounts.google.com/signup/v1/createaccount"
        response = self.session.get(url, headers=self.headers)
        # Extraire les tokens nécessaires de la réponse
        return {
            "flow_token": self.extract_value(response.text, "flowToken"),
            "fid": self.extract_value(response.text, "fid")
        }

    def extract_value(self, text, key):
        """Extraire une valeur du texte HTML"""
        try:
            return text.split(f'"{key}":"')[1].split('"')[0]
        except:
            return ""

    def submit_step(self, url, data):
        """Soumettre une étape du formulaire"""
        response = self.session.post(url, data=data, headers=self.headers)
        return response.json()

    def create_account(self, identity):
        """Créer un compte automatiquement"""
        try:
            # Initialisation
            params = self.get_initial_params()
            if not params["flow_token"]:
                raise Exception("Impossible d'obtenir le token initial")

            # Étape 1: Informations de base
            step1_url = "https://accounts.google.com/signup/v1/createaccount"
            step1_data = {
                "flowToken": params["flow_token"],
                "fid": params["fid"],
                "firstName": identity["first_name"],
                "lastName": identity["last_name"],
                "day": identity["birthdate"].split('/')[0],
                "month": identity["birthdate"].split('/')[1],
                "year": identity["birthdate"].split('/')[2],
                "gender": "1",  # 1=Homme, 2=Femme, 3=Autre
                "skipPhone": "true"
            }
            step1_result = self.submit_step(step1_url, step1_data)

            # Étape 2: Création email/mot de passe
            step2_url = "https://accounts.google.com/signup/v1/createaccount/email"
            step2_data = {
                "flowToken": step1_result.get("flowToken", params["flow_token"]),
                "email": identity["email"],
                "password": identity["password"],
                "passwordConfirmation": identity["password"]
            }
            step2_result = self.submit_step(step2_url, step2_data)

            # Étape 3: Vérification (simulée)
            if step2_result.get("status") == "success":
                return True
            else:
                raise Exception("Échec à l'étape de création")

        except Exception as e:
            print(f"Erreur lors de la création: {str(e)}")
            return False

    def run(self):
        """Exécuter le processus complet"""
        print("=== Création Automatique de Compte Google ===")
        
        # Générer une identité
        identity = generate_identity()
        print("\nIdentité générée:")
        print(json.dumps(identity, indent=2))

        # Nettoyer le cache
        self.clear_cache()

        # Créer le compte
        print("\nDébut de la création automatique...")
        if self.create_account(identity):
            # Sauvegarder les informations
            with open("accounts.txt", "a") as f:
                f.write(f"{identity['email']}:{identity['password']}\n")
            
            print("\nCompte créé avec succès!")
            print(f"Email: {identity['email']}")
            print(f"Mot de passe: {identity['password']}")
            print("Informations sauvegardées dans accounts.txt")
        else:
            print("\nÉchec de la création du compte")

if __name__ == "__main__":
    creator = GoogleAccountCreator()
    creator.run()
