input_text = str(input())
input_text_list = [letter for letter in input_text]
decrypted_str = ""

for letter in input_text_list:
    decrypted_str += chr(ord(letter) + 3)

print(decrypted_str)
