import wiki

content="The moon is an austronomical body"
title="Moon"

wiki.save_page(title,content)

output=wiki.load_page('Moon')
print(output)

pages=wiki.list_topics()
print(pages)