title = str(input())
content_of_the_article = str(input())

print("<h1>")
print(f'    {title}')
print("</h1>")
print(f'<article>')
print(f'    {content_of_the_article}')
print(f'</article>')

while True:
    current_input = str(input())
    if current_input == "end of comments":
        break
    print("<div>")
    print(f'    {current_input}')
    print("</div>")
