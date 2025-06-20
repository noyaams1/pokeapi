from api import get_all_pokemon_data, get_pokemon_details_from_api
from boto3.dynamodb.conditions import Key
import boto3
import random

table_name = "pokemons_collection"
db_resource = boto3.resource("dynamodb", region_name="us-west-2")
table = db_resource.Table(table_name)


# --- checking if pokemon is already in DB, if not: adding it.
# def update_db_if_needed(db, details):
#     name = details["name"]
#     if name in db:
#         print(f"✅ Pokémon {name} is already in your collection!")
#         print_pokemon(db[name])
#         return True
#     else:
#         print(f"🎲 Adding new Pokémon: {name}")
#         db[name] = details
#         save_json(db, DB_PATH)
#         print_pokemon(details)
#         return False


# --- Random drawing---
def get_random_pokemon():
    all_pokemon = get_all_pokemon_data()
    if not all_pokemon:
        print("Error loading Pokémon list")
        return

    chosen = random.choice(all_pokemon)["name"]
    details = get_pokemon_details_from_api(chosen)
    if details:
        print(f"🎲 Adding new Pokémon: {details['name']}")
        table.put_item(Item=details)
    return details


# --- Drawing pokemon by ID ---
def get_pokemon_by_id_from_db():
    id = input("Enter Pokémon ID (e.g., 25): ").strip()
    if not id.isdigit():
        print("Please enter a valid number.")
        return
    id = int(id)
    pokemon = table.query(IndexName="id-index", KeyConditionExpression=Key("id").eq(id))
    items = pokemon.get("Items", [])
    details = items[0] if items else None
    if details:
        print(f"✅ Pokémon's id: {id} is already in your collection!")
    else:
        print(f"🎲 Adding new Pokémon with id: {id}")
        details = get_pokemon_details_from_api(id)
        table.put_item(Item=details)
    return details


# --- Drawing pokemon by name ---
def get_pokemon_by_name_from_db():
    name = input("Enter Pokémon name (e.g., pikachu): ").strip().lower()
    pokemon = table.get_item(Key={"name": name})
    details = pokemon.get("Item")
    if details:
        print(f"✅ Pokémon {name} is already in your collection!")
    else:
        print(f"🎲 Adding new Pokémon: {name}")
        details = get_pokemon_details_from_api(name)
        table.put_item(Item=details)
    return details


# random_pokemon = get_random_pokemon()
# pokemon_by_id = get_pokemon_by_id_from_db()
# pokemon_by_name = get_pokemon_by_name_from_db()

# random_pokemon = get_random_pokemon()
# pokemon_by_id = _get_pokemon_by_id_from_db()
# pokemon_by_name = get_pokemon_by_name_from_db()
