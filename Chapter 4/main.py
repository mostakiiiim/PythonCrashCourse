my_foods=["vat", "goru", "murgi"]
my_food2=my_foods[:]

print(my_foods)
print(my_food2)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

user_names=['admin', 'user1', 'bobcat', 'alfredo']
if user_names:

    for users in user_names:
        if 'admin' in users:
            print(f"Hello {users}, would you like to see a status report?")
        else:
            print(f"Welcome to the system {users}")
else:
    print("We need more users")

