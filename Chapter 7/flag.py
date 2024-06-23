prompt = "Tell me something"
prompt+= "\nPress enter to 'quit'"

message =""
active = True
while active:
    message = input(prompt)
    if message =='quit':
        active = False
    else:
        print(message)

##Exit a loop

prompt = "Tell me something"
prompt+= "\nPress enter to 'quit'"

message =""

while True:
    message = input(prompt)
    if message =='quit':
        break
    else:
        print(message)
