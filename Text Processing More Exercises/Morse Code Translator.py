morse_code_input = str(input()).split(" | ")

morse_code_dictionary = {"..": "I", "--": "M", ".-": "A", "-..": "D", ".": "E", "-.--": "Y", "---": "O", "..-": "U", ".--": "W", ".-.": "R", "-": "T", ".-..": "L", "-.": "N", "--.": "G", "-.-.": "C", "....": "H", ".--.": "P", "-...": "B", "..-.": "F", ".---": "J", "-.-": "K", "--.-": "Q", "...": "S", "...-": "V", "-..-": "X", "--..": "Z"}

normal_text = ""

for morse_code_word in morse_code_input:
    morse_code_word = morse_code_word.split(" ")
    current_word = ""
    for code in morse_code_word:
        if code == "":
            continue
        current_word += morse_code_dictionary[code]
    normal_text += current_word + " "

print(normal_text)
