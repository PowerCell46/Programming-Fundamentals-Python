import re

html = input()
html_title = html.replace("</title>", "<title>")
html_title = html_title.split("<title>")
title = html_title[1]
title = title.replace("\\n", "")
print(f'Title: {title}')

html_content = html.replace("</body>", "<body>")
html_content = html_content.split("<body>")
content = html_content[1]
content = content.replace("\\n", "")
content = re.sub(r"<.*?>", "", content)
print(f'Content: {content}')
