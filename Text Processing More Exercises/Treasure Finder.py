decrypt_key = str(input()).split(" ")
decrypt_key_list = [int(num) for num in decrypt_key]
while True:
    current_string = str(input())
    result = ""
    if current_string == "find":
        break
    index = -1
    for i in range(0, len(current_string)):
        current_letter = ord(current_string[i])
        index += 1
        if index == len(decrypt_key_list):
            index = 0
        current_decrypt = decrypt_key_list[index]
        result += chr(current_letter - current_decrypt)

    type = ""
    coordinates = ""
    flag = True
    for xedni, char in enumerate(result):
        if char == "&" and flag:
            flag = False
            xedni += 1
            while True:
                char = result[xedni]
                if char == "&":
                    break
                type += char
                xedni += 1

        if char == "<":
            xedni += 1
            while True:
                char = result[xedni]
                if char == ">":
                    break
                coordinates += char
                xedni += 1

    print(f'Found {type} at {coordinates}')
    
