import sys
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
POSTMAN_API_KEY = os.environ.get('POSTMAN_API_KEY')
COLLECTION_UID = "28024806-64d66bc3-a56b-44f9-a9bd-625425ca533d"
GIT_REPO_PATH = os.getcwd()
COLLECTION_FILE = os.path.join(GIT_REPO_PATH, "collection.json")

# Fetch the collection from Postman
def fetch_collection():
    url = f"https://api.getpostman.com/collections/{COLLECTION_UID}"
    headers = {"X-API-Key": POSTMAN_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(COLLECTION_FILE, "w") as file:
            json.dump(response.json(), file, indent=2)
        print("Collection fetched and saved to Git repo.")
    else:
        print(f"Failed to fetch collection: {response.status_code} {response.text}")

# Update the collection in Postman
def update_collection():
    url = f"https://api.getpostman.com/collections/{COLLECTION_UID}"
    headers = {
        "X-API-Key": POSTMAN_API_KEY,
        "Content-Type": "application/json"
    }
    with open(COLLECTION_FILE, "r") as file:
        collection_data = json.load(file)
    response = requests.put(url, headers=headers, json=collection_data)
    if response.status_code == 200:
        print("Collection updated in Postman.")
    else:
        print(f"Failed to update collection: {response.status_code} {response.text}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [fetch|update]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "fetch":
        fetch_collection()
    elif command == "update":
        update_collection()
    else:
        print("Invalid command. Use 'fetch' to fetch the collection or 'update' to update it.")