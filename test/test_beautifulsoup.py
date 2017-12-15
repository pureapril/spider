from bs4 import BeautifulSoup  # pip install lxml
html = '''<html><head><title>陌上西厢 - April</title></head><body>
    <ul id="list" class="list-group"><li data-code="code111">一路上有你</li>
    <li data-code="code222" class="april"><a href="/2.mp3" singer="任贤齐">沧海一声笑</a></li>
    <li data-code="code333"><a href="/3.mp3" singer="齐秦">往事随风</a></li>
    <li data-code="code444"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
    </ul></div>'''
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title)           # <title>陌上西厢 - April</title>
print(soup.title.name)       # title
print(soup.title.string)    # 陌上西厢 - April
print(soup.title.parent.name) # head
print(soup.li)                  # <li data-code="code111">一路上有你</li>
print(soup.li["data-code"]) # code111
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='list'))

for link in soup.find_all('a'):
   print(link.get('href'))
   print(soup.get_text())   # 获取soup对象中所有文字内容
