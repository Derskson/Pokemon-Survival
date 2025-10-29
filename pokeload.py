from requests_html import HTMLSession

pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0
}

URL_BASE = "https://pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

def get_pokemon(index, pokemon_base=None):
    if pokemon_base is None:
        pokemon_base = {
            "name": "",
            "current_health": 100,
            "base_health": 100,
            "level": 1,
            "type": None,
            "current_exp": 0
        }
    url = f"{URL_BASE}{index}"
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_base = session.get(url)
    
    new_pokemon["name"] = pokemon_base.html.find(".mini", first=True).text
    return new_pokemon
    

print(get_pokemon(4))
