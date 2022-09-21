USERS_FILE = 'configs/users.dat'
LAST_SEEN = 'configs/last_seen.dat'

# Writes last seen tweet to dat file
def write_last_seen(info = 0):
    if info != 0:
        try:
            with open(LAST_SEEN, "w") as file:
                file.write(str(info));
                print('Wrote {} to last_seen!'.format(str(info)))
        except Exception as e:
            print(e)
    else:
        print('PROBLEM IN file_handling.py, write_last_seen: info variable came in as 0')

# Returns last seen tweet from dat file
def get_last_seen():
    with open(LAST_SEEN, "r") as file:
        line = file.read()
    return line

# Gets users
def get_users():
    with open(USERS_FILE, "r") as file:
        contents = file.read()
    lines = contents.split('\n')
    users = []
    for line in lines:
        data = line.split(' ')
        if len(data) == 3:
            user_info = data[0], data[1], data[2]
            users.append(user_info)
        else:
            print("ERROR IN LINE: {}\nLine does not have 3 elements".format(line))
    return users

# Debugging
if __name__ == '__main__':
    print('USERS: {}'.format(get_users()))
    print('LAST_SEEN: {}'.format(get_last_seen()))
    userchoice = input("Do you want to reset last seen? (y/n)\n")
    if userchoice == 'y':
        write_last_seen(1)
    print('Done debugging.')
