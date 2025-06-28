import random
import json
from datetime import datetime

def generate_fingerprint():
    return {
        "user_agent": random.choice([
            "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL)...",
            "Mozilla/5.0 (Linux; Android 11; Redmi Note 9)...",
            "Mozilla/5.0 (Linux; Android 12; SM-A515F)..."
        ]),
        "timezone": random.choice(["Europe/Paris", "America/New_York", "Asia/Kolkata"]),
        "screen_resolution": random.choice(["1080x1920", "720x1280"]),
        "language": random.choice(["fr-FR", "en-US", "es-ES"]),
        "platform": "Android",
        "device_memory": random.choice(["4", "6", "8"]),
        "hardware_concurrency": random.choice(["4", "6", "8"]),
        "webgl_vendor": random.choice(["Qualcomm", "ARM", "Imagination Technologies"]),
        "renderer": random.choice(["Adreno (TM) 640", "Mali-G76", "PowerVR Rogue"])
    }

def generate_identity():
    first_names = ["Alex", "Jean", "Marie", "Thomas", "Lucie"]
    last_names = ["Dupont", "Martin", "Bernard", "Dubois"]
    first = random.choice(first_names)
    last = random.choice(last_names)
    year = random.randint(1985, 2004)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    email = f"{first.lower()}.{last.lower()}{random.randint(1000,9999)}@gmail.com"
    password = f"{first.lower()}_{random.randint(1000,9999)}"

    return {
        "first_name": first,
        "last_name": last,
        "birthdate": f"{day:02}/{month:02}/{year}",
        "email": email,
        "password": password,
        "fingerprint": generate_fingerprint()
    }