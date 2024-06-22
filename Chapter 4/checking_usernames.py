current_users= ['alex', 'john', 'luffy', 'gintoki', 'GOKU']

new_current_users =[user.lower() for user in current_users]
print(new_current_users)
new_users= ['gintoki', 'goku', 'naruto', 'sukuna']

for users in new_users:
    if users in new_current_users:
        print(f'Username {users} exists')
    else:
        print(f'Welcome {users}')