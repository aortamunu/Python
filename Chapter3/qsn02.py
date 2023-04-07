letter = ''' Dear <|NAME|>,
Greetings from eSewa, Nepal. I am happy to tell you about your selection.
You are selected!

Have a great day ahead.
Thanks and regards,
Rishi

Date: <|DATE|>
'''

name = input("Enter the name")
date = input("Enter the date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)