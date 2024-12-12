import requests
import json
import os

POSTMAN_API_KEY = "PMAK-675a60ce6a064600016a49eb-e62c6acd2e2ad80dc12e7beff126555800"
COLLECTION_UID = "28024806-9b30e18b-0b21-48fd-a72f-b372bbd34626"
GIT_REPO_PATH = "https://github.com/ardo-rw/automation-test.git"
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
    # Uncomment the action you want to perform
    # fetch_collection()
    update_collection()
