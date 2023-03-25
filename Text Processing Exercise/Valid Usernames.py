usernames = str(input()).split(", ")

for username in usernames:
    if 2 < len(username) < 17:
        flag = True
        for i in username:
            if 47 < ord(i) < 58 or 64 < ord(i) < 91 or 96 < ord(i) < 123 or i == "-" or i == "_":
                flag = True
            else:
                flag = False
                break
        if flag:
            print(username)
