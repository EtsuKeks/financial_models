"""
This script bridges the gap between local OAuth and headless environments.
It extracts GDrive API secrets from a local DVC config, performs a browser-based authentication locally, 
and uploads the resulting credential artifact (pydrive_cred.json) directly to Google Drive.
"""
import os
from pathlib import Path
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# This script assumes DVC is already configured locally with gdrive_client_id and gdrive_client_secret
conf = {l.split('=')[0].strip(): l.split('=')[1].strip() for l in Path(".dvc/config.local").read_text().splitlines() if '=' in l}

gauth = GoogleAuth()
gauth.settings.update({
    'client_config_backend': 'settings',
    'client_config': {
        'client_id': conf['gdrive_client_id'],
        'client_secret': conf['gdrive_client_secret'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://oauth2.googleapis.com/token',
        'revoke_uri': 'https://oauth2.googleapis.com/revoke',
        'redirect_uris': ['http://localhost:8080'],
        'redirect_uri': 'http://localhost:8080'  # Added singular redirect_uri
    }
})

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Find folder and existing creds
folder_id = drive.ListFile({'q': "title = 'financial_models_secrets' and mimeType = 'application/vnd.google-apps.folder'"}).GetList()[0]['id']
existing = drive.ListFile({'q': f"title = 'pydrive_cred.json' and '{folder_id}' in parents"}).GetList()

# Upload/Update
f = existing[0] if existing else drive.CreateFile({'title': 'pydrive_cred.json', 'parents': [{'id': folder_id}]})
gauth.SaveCredentialsFile("tmp.json")
f.SetContentFile("tmp.json")
f.Upload()

os.remove("tmp.json")
print("Done: pydrive_cred.json uploaded.")