person_0={
    'name':'mostakim reza',
    'first_name':'Mostakim',
    'last_name': 'Reza',
    'age': 22,
    'city':'ingolstadt'
}

"""for key, personal_info in person_0.items():
    print(f"This person's {key} is {personal_info}")"""

person_1={
    'name':'sajid shahadat',
    'first_name':'Sajid',
    'last_name': 'Shahadat',
    'age': 23,
    'city':'dhaka'
}
person_2={
    'name':'hasan mahmud sunny',
    'first_name':'hasan',
    'last_name': 'sunny',
    'age': 24,
    'city':'dhaka'
}

people= [person_0, person_1, person_2]

for persons in people:
    for person in persons.values():
        print({person})