pokemon_0= {'type':'water', 'hp':10}
pokemon_1= {'type':'fire', 'hp':12}
pokemon_0['x_position']=10
pokemon_0['y_position']=50

print(pokemon_0)

print(f"The pokemon is {pokemon_0['type']} type")

for key, value in pokemon_0.items():
    print(key, value)
for key in pokemon_0.keys():
    print(key)
for value in set(pokemon_0.values()):
    print(value)
    #set doesn't lets you repeat, that's why 10 is shown 1 time

pokemons = []
for i in range(30):
    new_pokemon= {'type':'water', 'hp':10}
    pokemons.append(new_pokemon)

for pokemon in pokemons[:4]:
    if pokemon['type']=='water':
        pokemon['hp']=15

################################
#A List in the dictionary#######
pokemon_0['moves']= 'tackle', 'water gun'

print(pokemon_0)

pokemon_2={
    'type':'water', 
    'hp':10,
    'moves': ['water gun', 'tackle', 'bubble']

}

for move in pokemon_2['moves']:
    print(f"You can use the following move {move}")