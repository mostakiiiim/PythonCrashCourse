friends_names = ['sajid', 'sunny', 'iftekhar', 'zuhayer']

print(friends_names[0])
print(friends_names[1])
print(friends_names[2])
print(friends_names[3])

greetings = f'Meet my good friend {friends_names[0]}'

print(greetings)

# ----------------------------------------------------------------

# 3.4

invited_guest = ['sajid', 'sunny', 'iftekhar']

invitation_message1 = f"Dear, {invited_guest[0]}. You're invited for dinner"
invitation_message2 = f"Dear, {invited_guest[1]}. You're invited for dinner"
invitation_message3 = f"Dear, {invited_guest[2]}. You're invited for dinner"

print(invitation_message1)
print(invitation_message2)
print(invitation_message3)

cannot_come = 'sunny'


print(f"{cannot_come.title()} is not going to make it to the party")


invited_guest.remove(cannot_come)
invited_guest.insert(1, 'Zuhayer')

invitation_message1 = f"Dear, {invited_guest[0].title()}. You're invited for dinner"
invitation_message2 = f"Dear, {invited_guest[1].title()}. You're invited for dinner"
invitation_message3 = f"Dear, {invited_guest[2].title()}. You're invited for dinner"

print(invitation_message1)
print(invitation_message2)
print(invitation_message3)

print("We've found a new table")

invited_guest.insert(0, 'Nihal')
invited_guest.insert(2, 'Nibir')
invited_guest.append('Jayed')



invitation_message1 = f"Dear, {invited_guest[0].title()}. You're invited for dinner"
invitation_message2 = f"Dear, {invited_guest[1].title()}. You're invited for dinner"
invitation_message3 = f"Dear, {invited_guest[2].title()}. You're invited for dinner"

invitation_message4 = f"Dear, {invited_guest[3].title()}. You're invited for dinner"
invitation_message5 = f"Dear, {invited_guest[4].title()}. You're invited for dinner"
invitation_message6 = f"Dear, {invited_guest[5].title()}. You're invited for dinner"

print(invitation_message1)
print(invitation_message2)
print(invitation_message3)
print(invitation_message4)
print(invitation_message5)
print(invitation_message6)

print('Unfortunately, I can only invite 2 people on the dinner')

popped_friend1 = invited_guest.pop() 
print(f"{popped_friend1}, sorry for inconvenience")

popped_friend2 = invited_guest.pop()
print(f"{popped_friend2}, sorry for inconvenience")

popped_friend3 = invited_guest.pop()
print(f"{popped_friend3}, sorry for inconvenience")

popped_friend4 = invited_guest.pop()
print(f"{popped_friend4}, sorry for inconvenience")

invitation_message1 = f"{invited_guest[0]}, you're still invited"
invitation_message2 = f"\n{invited_guest[1]}, you're still invited"

print(invitation_message1)
print(invitation_message2)

del invited_guest[1]
del invited_guest[0]

print(invited_guest)
