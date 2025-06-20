# from db import pokemon


# --- Show drawing options to the user---
def print_menu():
    print("\nHow would you like to draw your Pokémon? ")
    print("1. Random")
    print("2. By ID")
    print("3. By Name")
    print("4. Exit")


# --- Printing Pokémon info (ui) ---
def print_pokemon(pokemon):
    name = pokemon["name"]
    id = pokemon["id"]
    height = pokemon["height"]
    weight = pokemon["weight"]
    types = pokemon["types"]
    print("\n🎯 Pokémon Drawn:")
    print(f"Name   : {name.title()}")
    print(f"ID     : {id}")
    print(f"Height : {height}")
    print(f"Weight : {weight}")
    print(f"Types  : {', '.join(types)}\n")
