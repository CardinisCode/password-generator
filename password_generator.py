#This will be my password generator project. 
#User can choose how many words they want in their password, 
#Which characters and numbers to add in. 
#Then the password generator will: 
# Mix the words around (shuffle)
# Capitalize the first letter of the first words
# Add the special characters and numbers (min of 1 each) 
# Give an error message if these special requirements arent met
#It will then save the passwords into our password generator dictionary 
#where the key = site for the password 
# and the value = password itself 
#Remember: Baby steps!!!! 

import random 
def password_maker(user_chosen_words, user_chosen_characters, howManyNumbers):
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_password = ""
    list_of_words = user_chosen_words.split()
    list_of_characters = user_chosen_characters.split()

    for word in range(0, len(list_of_words)):
        randomWord = random.choice(list_of_words)
        random_password += randomWord
        list_of_words.remove(randomWord)
    random_password = random_password[0].upper() + random_password[1:].lower()

    print("After the first loop, my random password looks like this:", random_password)

    for character in range(0, len(list_of_characters)):
        randomChar = random.choice(list_of_characters)
        random_password += randomChar
        list_of_characters.remove(randomChar)
    
    print("After adding characters to my password, it now looks like this:", random_password)
    
    for number in range(0, int(howManyNumbers) + 1):
        randomNumber = random.choice(list_of_numbers)
        random_password += str(randomNumber)
        list_of_numbers.remove(randomNumber)
    
    print("After adding numbers, my random password looks like:", random_password)
    shuffle_my_password = list(random_password)
    print("Broken down as a list, my password now looks like this:", shuffle_my_password)
    random.shuffle(shuffle_my_password)
    print(shuffle_my_password)

    my_new_password = ""
    for i in shuffle_my_password: 
        my_new_password += ''.join(i)

    return my_new_password


print("Please think of a few words of your choosing for your password")
chosenWords = input("Please provide your chosen words, seperated by spaces: ")
print("To confirm, your chosen words are:", chosenWords)
print()
print("Now think of the random characters you'd like to add to your password. ")
chosenCharacters = input("Please provide 2 special characters of your choice, seperated by spaces: ")
print("To confirm your special Characters are:", chosenCharacters)
print()
howManyNumbers = input("How many numbers would you like to add to your password? ")
print("To confirm you would like", howManyNumbers, "In your password.")

print(password_maker(chosenWords,chosenCharacters, howManyNumbers))

