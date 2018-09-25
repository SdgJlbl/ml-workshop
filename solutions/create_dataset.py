battles['label'] = (battles['First_pokemon'] == battles['Winner']).astype(int)
df = battles.join(pokemons, on='First_pokemon').join(pokemons, on='Second_pokemon', rsuffix='_opponent')