import requests

def get_character_info(name):
    url = f"https://swapi.dev/api/people/?search={name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters = data.get("results", [])

        if not characters:
            return "No characters found."

        characters = sorted(characters, key=lambda x: x["name"])

        character_info = []
        for character in characters:
            info = {
                "Name": character["name"],
                "Starship1": get_starship_info(character["starships"][0]),
                "Starship2": get_starship_info(character["starships"][1]),
                "Home Planet": get_planet_info(character["homeworld"]),
                "Species": get_species_info(character["species"][0])
            }
            character_info.append(info)

        return character_info
    else:
        return "Error: Failed to retrieve character information."


def get_starship_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        starship = response.json()
        return {
            "Name": starship["name"],
            "Cargo Capacity": starship["cargo_capacity"],
            "Class": starship["starship_class"]
        }
    else:
        return "N/A"


def get_planet_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        planet = response.json()
        return {
            "Name": planet["name"],
            "Population": planet["population"],
            "Climate": planet["climate"]
        }
    else:
        return "N/A"


def get_species_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        species = response.json()
        return {
            "Name": species["name"],
            "Language": species["language"],
            "Lifespan": species["average_lifespan"]
        }
    else:
        return "N/A"

character_name = input("Enter a Star Wars character name: ")
result = get_character_info(character_name)
print(result)
