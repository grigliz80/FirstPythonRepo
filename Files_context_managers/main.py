with open('db/days_of_week.txt') as week_file:
    weekdays = [day.rstrip() for day in week_file.readlines()]

print(weekdays)

username = input('Please enter your name: ')

with open('db/u_info.txt', 'w') as file_obj:
    file_obj.write(username)