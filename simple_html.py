from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    return h1_tag.string


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_concerns = [e.string for e in list_items]
    return list_concerns


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    return paragraph.string


def find_other_paragraphs():
    paragraphs = simple_soup.find_all('p')
    other_paragrpahs = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    return other_paragrpahs[0].string


print(find_title())
print(find_list_items())
print(find_subtitle())
print(find_other_paragraphs())