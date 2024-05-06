# TryItYourself

name = "Eric"

message = f"Hello {name}, would you like to learn some Python today? "

print(message)

print(name.upper())
print(name.lower())
print(name.title())

author = ' Charles Bukowski  '

quote = "If you're going to try, \tgo all the way. Otherwise, \ndon't even start."


print(f'{author.lstrip()} once said, "{quote}"')
print(f'{author.rstrip()} once said, "{quote}"')
print(f'{author.strip()} once said, "{quote}"')

filename = ('python_notes.txt')

print(filename.removesuffix('.txt'))
