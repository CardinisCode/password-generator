#Now lets store these passwords & usernames in a dictionary 
#But lets start with storing the password against the place we needed that password. 








def capture_user_entry_from_user_entry():
    userName = input("What username did you choose (if applicable):")
    account = input("Whats the name of the account/application you needed this password for:")
    password = input("What is your password for this account/application?  :")
    email_address = input("Which email address did you use for this account? *Note if no answer is provided, it will be assumed the email is Gmail. :")

    if password == "" or account == "":
        return "No Password provided! Please retry with correct details."

    if userName == "":
        userName = "Not provided"

    if email_address == "":
        email_address = "Gmail"

    return (account, password, userName, email_address)


def update_password_keeper_from_file(file_name):
    incoming_file = open(file_name, "r")
    if len(incoming_file) == 0:
        return "Empty file!"
    
    file_contents = incoming_file.readlines()
    incoming_file.close()

    for line in file_contents:
        current_line = line.rstrip()
        line_split = current_line.split()
        print(line_split)
        

    return password_keeper




def add_new_account_details_into_password_keeper(new_entry, password_keeper):
    account, password, user_name, email_address = new_entry

    if not account in password_keeper.keys():
        password_keeper[account] = {
            "Password": password,
            "Username": user_name, 
            "Email Address": email_address
        }

    password_keeper[account]["Password"] = password

    if user_name != "Not provided" and user_name != "":
        password_keeper[account]["Username"] = user_name

    if email_address != "Gmail" and email_address != "":
        password_keeper[account]["Email Address"] = email_address

    return password_keeper


def write_passwords_to_file(password_keeper, file_name, wipe=False):
    if wipe == False:
        incoming_file = open(file_name, "a")
    else:
        incoming_file = open(file_name, "w")

    for password_name in password_keeper.keys():
        password = password_keeper[password_name]["Password"]
        username = password_keeper[password_name]["Username"]
        email_address = password_keeper[password_name]["Email Address"]
        first_line = "account name: " + password_name + "\n"
        second_line = "Password: " + password + " \n"
        incoming_file.write(first_line)
        incoming_file.write(second_line)

        third_line = "Email Address: " + email_address + " \n"
        incoming_file.write(third_line)

        third_line = "Username: " + username + " \n"
        print(third_line, file=incoming_file)

    print("The details for this account have been successfully written to the file.")
        
    return "Done!"


def print_passwords_for_confirmation(new_password_entry):
    account, password, userName, email_address = new_password_entry

    try:
        print_message = "For " + account + ": \n Password: " + password + "\n User name: " + userName + "\n Email Address:" + email_address
        return print_message

    except TypeError:
        print("Note: Your email address and your username have not yet been provided for this password.")
        print_message = "For " + account + " your password is " + password
        return print_message

    except Exception as e:
        print(e)



def print_user_password_from_dictionary(account_name, password_keeper):
    if password_keeper == {}:
        return "Sorry your dictionary is empty."

    try:
        password = password_keeper[account_name]
        print_message = "Your password for account " + account_name + " is: " + password
        return print_message
    except KeyError: 
        return "Sorry you do not have a password stored for this account! Please consider adding it."


def capture_users_new_password_and_store_it(file_name, wipe):
    new_password_entry = capture_user_entry_from_user_entry()
    add_new_account_details_into_password_keeper(new_password_entry, password_keeper)
    print_password = input("Would you like to have this password printed for confirmation? Yes or No: ")

    if print_password == "Yes":
        print(print_passwords_for_confirmation(new_password_entry))

    save_password_to_password_keeper = input("Would you like to store this password in your Password Keeper? Yes or No : ")
    if save_password_to_password_keeper == "Yes":
        add_new_account_details_into_password_keeper(new_password_entry, password_keeper)

    save_password_to_file = input("Would you like to save this new password to file? Yes or No: ")
    save_password_to_file = save_password_to_file.lstrip()

    if save_password_to_file == "Yes":
        if wipe == True:
            write_passwords_to_file(password_keeper, file_name, wipe=True)
        else:
            write_passwords_to_file(password_keeper, file_name)

    return "Done"


def wipe_password_keeper(password_keeper):
    password_keeper = {}

    return password_keeper


def print_updated_account_details(account_name, password_keeper):
    password = password_keeper[account_name]["Password"]
    username = password_keeper[account_name]["Username"]
    email_address = password_keeper[account_name]["Email Address"]

    try:
        printed_message = "For " + account_name + " : \n Password: " + password + "\n Username: " + username + "\n Email Address: " + email_address
        return printed_message
    
    except KeyError:
        return "Sadly you have not yet successfully added this account to your password keeper."

    except:
        return "You have done something wrong. Please retry adding this account to the password keeper"


def update_specific_account_details(account_name, detail, password_keeper, file_name):
    detail_type, updated_detail = detail.split()
    if detail_type == "Email address":
        password_keeper[account_name]["Email Address"] = updated_detail
    elif detail_type == "Username":
        password_keeper[account_name]["Username"]
    elif detail_type == "Password":
        password_keeper[account_name]["Password"]

    print_updated_details = input("Would you like to print details for this account to confirm it has been updated? Yes or No")
    print_updated_details = print_updated_details.lstrip()
    if print_updated_details == "Yes":
        print_updated_account_details(account_name, password_keeper)
    
    save_password_to_file = input("Would you like to save this new password to file? Yes or No: ")
    save_password_to_file = save_password_to_file.lstrip()

    if save_password_to_file == "Yes" or save_password_to_file == "YES":
        write_passwords_to_file(password_keeper, file_name)

    return password_keeper


password_keeper = {}
file_name = "password_diary.txt"
#new_password_entry = capture_user_entry()
# update_password_keeper = update_my_password(new_password_entry, password_keeper)
# write_passwords_to_file(password_keeper, file_name)

print("Please note: the following questions are case sensitive. Take care not to use Caps. Thank you!")
print()

empty_password_keeper = input("Before we begin, would you like to start with an empty password keeper? Yes or No :")
empty_password_keeper = empty_password_keeper.lstrip()

print("Note: if you choose to empty your password keeper, it will wipe both the dictionary and the file containing your account details.")
print("After the information has been deleted, all your stored passwords will be deleted.")
confirm_empty_password_keeper = input("To confirm, you would like to reset your password keeper? Yes or No: ")
confirm_empty_password_keeper = confirm_empty_password_keeper.lstrip()
if confirm_empty_password_keeper == "Yes":
    wipe = True
elif confirm_empty_password_keeper == "No":
    wipe = False 

password_keeper = wipe_password_keeper(password_keeper)
# Going forward make sure to edit the below functions so they either write to a clean file or add to it, based on how the user answered the above questions. 


new_entry_request = input("Would you like to save a new password? Yes or No : ")
new_entry_request = new_entry_request.lstrip()

if new_entry_request == "Yes":
    capture_users_new_password_and_store_it(file_name, wipe)

elif new_entry_request == "No":
    ask_if_user_wants_a_password = input("Would you like to access a password already saved? Yes or No : ")
    ask_if_user_wants_a_password = ask_if_user_wants_a_password.lstrip()

    if ask_if_user_wants_a_password == "Yes":
        print("For this next question, please answer in lower-case only. ")
        account_name = input("Please provide the account or app for the password you'd like to access: ")
        account_name = account_name.lstrip()
        password = print_user_password_from_dictionary(account_name, password_keeper)
        
        if password == "Sorry you do not have a password stored for this account": 
            add_password_to_dict = input("Would you like to add this password to your keeper? Yes or No : ")
            add_password_to_dict = add_password_to_dict.lstrip()
            if add_password_to_dict == "Yes":
                capture_users_new_password_and_store_it(file_name, wipe)

    if ask_if_user_wants_a_password == "No":
        request_password_keeper_wipe = input("Would you like to reset / empty your password keeper? Yes or No: ")
        request_password_keeper_wipe = request_password_keeper_wipe.lstrip()
        if request_password_keeper_wipe == "Yes":
            password_keeper = wipe_password_keeper(password_keeper)
        update_password_request = input("Would you like to update the details for one of your accounts? Yes or No :")
        update_password_request = update_password_request.lstrip()

        if update_password_request == "Yes":
            account_name = input("Which account would you like to update: ")
            account_name = account_name.lstrip()

            detail_type = input("Which detail would you like to update: password, username, or email address")
            detail_type = detail_type.lstrip()

            updated_detail = input("Please provide the updated information you'd like to provide for this detail: ")
            updated_detail = updated_detail.lstrip()

            detail = (detail_type, updated_detail)
            password_keeper = update_specific_account_details(account_name, detail, password_keeper, file_name)


            multiple_value_update = input("Would you like to update more than 1 account detail? Yes or No")
            multiple_value_update = multiple_value_update.lstrip()

            if multiple_value_update == "Yes":
                print("To only update specific fields, (in the following question) only fill in the relevant fields you would like to update.")
                capture_users_new_password_and_store_it(file_name, wipe)
            

else:
    print("Please retry, responding only with either Yes or No. Note this answer is caps-sensitive.")

# Note: Test your code and see if it behaves the way you'd like. If not, fix it. 










