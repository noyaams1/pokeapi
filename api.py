from constant_vars import POKEMON_LIST_ENDPOINT, API_BASE_URL
import requests


# --- Get all Pokémons (name + URL) ---
def get_all_pokemon_data():
    response = requests.get(POKEMON_LIST_ENDPOINT)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Failed to fetch Pokémon list")
        return []


# --- Get full details of a Pokémon by name or ID ---
def get_pokemon_details_from_api(identifier):
    url = f"{API_BASE_URL}/pokemon/{identifier}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
        }
        return pokemon_info
    else:
        print(f"Failed to fetch details for {identifier}")
        return None
