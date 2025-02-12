import json
import os
import requests
import base64
from tqdm import tqdm
import zipfile
import webbrowser

API_BASE_URL = "https://api.humanscanrepository.com/"
CREDENTIALS_FILE = "src/credentials.json" #path to your credentials file, please contact us at support@humanscanrepository.com to prvoide you credentials 
DOWNLOAD_FOLDER = "downloads"

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return None

def save_credentials(username, email, password, access_token, refresh_token):
    credentials = {
        "username": username,
        "email": email,
        "password": password,
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)

def login(username, password, apiKey):
    headers = {
        "X-Api-Key": apiKey,
        "Authorization": "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()
    }
    response = requests.post(f"{API_BASE_URL}/login", headers=headers)
    if response.status_code == 200:
        return response.json().get("AccessToken"), response.json().get("RefreshToken")
    else:
        print("Login failed:", response.json())
        return None, None

def register(username, email, password,apiKey):
    response = requests.post(f"{API_BASE_URL}/register", json={"username": username, "email": email, "password": password}, headers={"X-Api-Key": apiKey})
    return response.status_code == 200

def get_all_models(token,apiKey):
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Key": apiKey
    }
    response = requests.get(f"{API_BASE_URL}/models", headers=headers)
    if response.status_code == 200:
        models = response.json()
        print("Available Models:")
        for model in models:
            print(f"ID: {model['id']}")
    else:
        print("Failed to retrieve models:", response.json())

def get_download_files(token,apiKey):
    model_id = input("Enter the model ID: ")
    file_type = input("Enter the file type: ")
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Key": apiKey
    }
    response = requests.get(f"{API_BASE_URL}/models/{model_id}?files={file_type}", headers=headers)
    if response.status_code == 200:
        files = response.json().get('files', [])
        print("Download Files:")
        for file in files:
            if file == file_type:
                file_url = files[file]["URL"]
                file_type = files[file]["type"]
                print(f"File: {file}, URL: {file_url}")
                
                # Ask if the user wants to download the file
                download_choice = input("Do you want to download this file? (yes/no): ").strip().lower()
                if download_choice == 'yes':
                    download_file(file_url, model_id,file_type )
                break
    else:
        print("Failed to retrieve download files:", response.json())

def download_file(file_url, file_name,file_type):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    
    file_path = os.path.join(DOWNLOAD_FOLDER, (file_name+"."+file_type))

    # Check if the file already exists
    if os.path.exists(file_path):
        override_choice = input(f"{file_name} already exists. Do you want to override it? (yes/no): ").strip().lower()
        if override_choice != 'yes':
            print("Download canceled.")
            return

    # Download the file with progress
    try:
        with requests.get(file_url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(file_path, 'wb') as f, tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name) as bar:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    bar.update(len(chunk))
        print(f"Downloaded: {file_name} to {DOWNLOAD_FOLDER}")
    except Exception as e:
        print(f"Failed to download the file: {e}")

def get_model_by_id(token,apiKey):
    model_id = input("Enter the model ID: ")
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Api-Key": apiKey
    }
    response = requests.get(f"{API_BASE_URL}/models/{model_id}", headers=headers)
    if response.status_code == 200:
        model = response.json()
        print("Model Details:")
        print(json.dumps(model, indent=4))
    else:
        print("Failed to retrieve model:", response.json())