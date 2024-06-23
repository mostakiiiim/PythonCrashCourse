def greet_user(username):
    print(f"Welcome {username.title()}!\n")

greet_user('Omey')
#Positional Argument
#Keyword argument

def pokemon_info(pokemon_type, pokemon_name, region='kanto'):
    print(f"This is a {pokemon_type} type pokemon")
    print(f"It's name is {pokemon_name}")
    print(f"It is found in {region} region ")

pokemon_info('fire', 'charizard', 'Sinnoh')

pokemon_info(pokemon_name='charizard', pokemon_type='fire')