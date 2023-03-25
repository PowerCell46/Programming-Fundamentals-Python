banned_words = str(input()).split(", ")
text = str(input())

for ban in banned_words:
    while ban in text:
        text = text.replace(ban, ("*" * len(ban)))

print(text)
