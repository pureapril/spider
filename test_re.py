import re
html = '''
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7"><a href="/2.mp3" singer="任贤齐">沧海一声笑</a></li>
        <li data-view="4"><a href="/3.mp3" singer="齐秦">往事随风</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(type(results))
for result in results:
    print(result)

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
for result in results:
    print(result[1])

content = "Hello 080603 April  "
# content = re.sub('\d+','',content) #~ 将数字替换为为空
content = re.sub('(\d+)',r'\1 0228',content) # ~Hello 080603 0228 April
print(content)