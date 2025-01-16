with open('db/u_info.txt', 'r') as file_obj:
    username = file_obj.read()


print('Hey', username + '!')