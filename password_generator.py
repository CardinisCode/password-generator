#This will be my password generator project. 
#User can choose which words they would like in their password 
#Plus 2 special characters
#Then the password generator will: 
# Mix the words around (shuffle)
# Capitalize the first letter of the first words
# Add the special characters / numbers in between the words
# Give an error message if these special requirements arent met
#It will then save the passwords into our password generator dictionary 

import random 

def password_maker(user_chosen_words, user_chosen_characters, user_chosen_numbers):
    random_password = ""
    list_of_words = user_chosen_words.split()
    random.shuffle(list_of_words)
    print(list_of_words) 
    list_of_characters = user_chosen_characters.split()

    for i in range(0, len(list_of_words)):
        randomWord = random.choice(list_of_words)
        randomChar = random.choice(list_of_characters)
        if i == len(list_of_words) -1:
            random_password += randomWord + user_chosen_numbers
        else:
            random_password += randomWord + randomChar

        list_of_words.remove(randomWord)
        list_of_characters.remove(randomChar)
    new_password = random_password[0].upper() + random_password[1:].lower()

    print("My random password looks like this:", random_password)
    
    return new_password


print("Please think of a few words of your choosing for your password")
chosenWords = input("Your chosen words, seperated by spaces: ")
print("To confirm, your chosen words are:", chosenWords)
print()
print("Now think of the random characters you'd like to add to your password. ")
chosenCharacters = input("Please provide 2 special characters of your choice, seperated by spaces: ")
print("To confirm your special Characters are:", chosenCharacters)
print()
chosen_numbers = input("Which number/s would you like to add to your password? ")
print("To confirm you would like", chosen_numbers, "to be added to your password.")

print(password_maker(chosenWords,chosenCharacters, chosen_numbers))

