file_location = str(input()).split("\\")

last_part = file_location.pop()
last_part = last_part.split(".")

file_extension = last_part.pop()

print(f'File name: {".".join(last_part)}')
print(f'File extension: {file_extension}')
