## What do you do if you get back multiple characters?

modify the show_character_info() method
```python

@app.route('/', methods=['GET', 'POST'])
def show_character_info():
    if request.method == 'POST':
        character_name = request.form['character_name']
        characters = get_character_info(character_name)

        if not characters:
            error_message = "No characters found."
            return render_template('error.html', error_message=error_message)

        # Sort characters by name in alphabetical order
        sorted_characters = sorted(characters, key=lambda x: x["name"])

        character_info_list = []
        for character in sorted_characters:
            # Get information for each character and append to the list
            info = {
                "Starships": get_starship_info(character.get("starships", [])),
                "Home Planet": get_planet_info(character.get("homeworld", "")),
                "Species": get_species_info(character.get("species", []))
            }
            character_info_list.append(info)

        return render_template('result.html', character_name=character_name, information=character_info_list)

    return render_template('index.html')
```

## What do you do if you get no characters back?

When no characters are found, we can update the get_character_info() function to return an empty list instead of None.

## How to handle multiple starships?

modify the get_character_info() method

```python
def get_character_info(name):
    url = f"https://swapi.dev/api/people/?search={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        characters = data.get("results", [])

        if not characters:
            return None  

        characters = sorted(characters, key=lambda x: x["name"])

        character_info = []
        for character in characters:
            starships_info = []
            for starship_url in character["starships"]:
                starship_info = get_starship_info(starship_url)
                starships_info.append(starship_info)

            info = {
                "Starships": starships_info if starships_info else "N/A",
                "Home Planet": get_planet_info(character["homeworld"]) if character.get("homeworld") else "N/A",
                "Species": get_species_info(character["species"][0]) if character["species"] else "Unknown"
            }
            character_info.append(info)

        return character_info
    else:
        return None 

```

## How to handle if a section (starship, home planet, species) is empty?

modify the get_character_info() method

```python
def get_character_info(name):
    url = f"https://swapi.dev/api/people/?search={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        characters = data.get("results", [])

        if not characters:
            return None 

        characters = sorted(characters, key=lambda x: x["name"])

        character_info = []
        for character in characters:
            info = {
                "Starship1": get_starship_info(character["starships"][0]) if character["starships"] else "N/A",
                "Starship2": get_starship_info(character["starships"][1]) if len(character["starships"]) > 1 else "N/A",
                "Home Planet": get_planet_info(character["homeworld"]) if character.get("homeworld") else "N/A",
                "Species": get_species_info(character["species"][0]) if character["species"] else "Unknown"
            }
            character_info.append(info)

        return character_info
    else:
        return None 

```