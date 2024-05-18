# Chapter1
# pylint: disable=pointless-string-statement

# TIY

simple_message = "don't make the right the decision. Make the decision right"

print(simple_message)

new_message = "Quote of the day: " + simple_message

print(new_message)


# DataTypes

# Strings

# ChangingCases
"""
A method is an action that can be applied on a data.

The(.) dot after the name string indicates python to take the action
"""
name = "md. mostakim reza"

print(name.title())
print(name.upper())
print(name.lower())

initials = "Mr."

# f-Strings
fullname = f"{initials} {name}"

print(fullname. title())
'''f is for format because python formats the strings'''

# White spaces
'''
To add tab "\t"
To add newline "\n"
'''

'''To Strip whitespaces from strings use .rstrip() method'''

'''
.removeprefix( ) Method is used to remove certain prefixes from strings

'''

first_url = "https://www.google.com"
short_url = first_url.removeprefix("https://")

print(short_url)
