from utilities import (
    get_random_pokemon,
    get_pokemon_by_id_from_db,
    get_pokemon_by_name_from_db,
)
from ui_messages import print_menu, print_pokemon


# --- Running the program---
def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            random_pokemon = get_random_pokemon()
            pokemon = random_pokemon
            print_pokemon(pokemon)

        elif choice == "2":
            pokemon_by_id = get_pokemon_by_id_from_db()
            pokemon = pokemon_by_id
            print_pokemon(pokemon)

        elif choice == "3":
            pokemon_by_name = get_pokemon_by_name_from_db()
            pokemon = pokemon_by_name
            print_pokemon(pokemon)

        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()
