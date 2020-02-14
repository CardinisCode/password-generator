#Now lets store these passwords & usernames in a dictionary 
#But lets start with storing the password against the place we needed that password. 

my_dictionary_of_passwords = {}
userName = input("What username did you choose (if applicable):")
siteRequestingPassword = input("Whats the name of the website/application you needed this password for:")
password = input("What is your password for this website/application?:")

my_dictionary_of_passwords[siteRequestingPassword] = password

print(my_dictionary_of_passwords)

#Need to write each new entry to a file so it stores this info to be accessed as needed. 


