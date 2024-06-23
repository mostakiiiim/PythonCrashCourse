prompt = "Tell me something"
prompt+= "\nPress enter to 'quit'"

message =""
while message !='quit':
    message = input(prompt)
    print(message)