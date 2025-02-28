import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Die Scopes definieren, welche API-Berechtigungen wir benötigen
SCOPES = ["https://www.googleapis.com/auth/business.manage"]

def get_business_accounts():
    """Google Business Profile API aufrufen, um alle Accounts anzuzeigen."""
    print("Starte die Authentifizierung...")
    
    # OAuth2 Konfiguration aus der client_secrets.json Datei laden
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES)
    
    # Authentifizierung durchführen (öffnet Browser-Fenster)
    creds = flow.run_local_server(port=0)
    print("Authentifizierung abgeschlossen.")
    
    # Service für die Business Profile API erstellen
    service = build("mybusinessaccountmanagement", "v1", credentials=creds)
    
    # Accounts abrufen
    accounts = service.accounts().list().execute()
    
    print("Gefundene Accounts:")
    # Vollständige API-Antwort ausgeben
    print(accounts)
    
    # Einzelne Account-IDs extrahieren
    if "accounts" in accounts:
        for account in accounts["accounts"]:
            print("--------------------")
            print("Account Name:", account.get("accountName"))
            print("Account ID:", account.get("name"))
    else:
        print("Keine Accounts gefunden.")

if __name__ == "__main__":
    get_business_accounts()
