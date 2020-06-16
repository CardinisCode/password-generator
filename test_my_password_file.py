def update_password_keeper_from_file(file_name, password_keeper):
    incoming_file = open(file_name, "r")

    
    file_contents = incoming_file.readlines()
    incoming_file.close()

    if len(file_contents) == 0:
        return "Empty file!"

    for line in file_contents:
        current_line = line.rstrip()
        #print(current_line)
        line_split = current_line.split()
        password_keeper.setdefault(line_split[0], line_split[1])

    return password_keeper

file_name = "password_diary.txt"
password_keeper = {}
print(update_password_keeper_from_file(file_name, password_keeper))