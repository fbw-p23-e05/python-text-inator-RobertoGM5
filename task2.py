userInput = input("Enter a single word: ")

consonants = "bcdfghjklmnpqrstvwxyz"
endsConsonant = userInput[-1] in consonants

if endsConsonant:
    result = userInput + "inator"
else:
    result = userInput + "-inator"

length = str(len(userInput))
result += " "+length+"000"

print("Transformed word:", result)