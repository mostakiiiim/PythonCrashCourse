def city_country(city_name, country_name):
    return f"{city_name}, {country_name}"


while True:
    print("Enter City name and Country name \n Press q to quit")

    city = str(input("Enter City :"))
    if city == 'q':
        break

    country= str(input("Enter Country :"))
    if country =='q':
        break
    
    city_country_name= city_country(city, country)
    print(f'"{city_country_name.title()}"')

