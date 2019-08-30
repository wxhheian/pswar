import re

#match()
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())     #输出匹配的结果
# print(result.span())        #输出匹配的位置


#group()
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())     #输出完整的匹配结果
# print(result.group(1))    #索引从1开始
# print(result.span())        #输出匹配的位置


# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$',content)         #.* 贪婪模式
# print(result)
# print(result.group(1))


# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))


# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)',content)
# result2 = re.match('http.*?comment/(.*)',content)
# print(result1.group(1))    #输出为空  因为*是匹配0到多个字符，?又是非贪婪模式，所以匹配0个字符就结束了
# print(result2.group(1))    #匹配到结果


# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$',content)    # . 匹配不包括换行符的所有字符
# print(result.group(1))                   #匹配错误
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)   #re.S 表示修饰符，作用在于使.匹配包括换行符在内的所有字符
# print(result.group(1))                   #匹配错误


# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com',content)
# print(result)


#match()是从字符串的开头开始匹配，一旦开头不匹配，整个匹配都会失败
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.match('Hello.*?(\d+).*?Demo',content)
# print(result)               #输出结果为None
# result = re.search('Hello.*?(\d+).*?Demo',content)          #区别match()与search()
# print(result)


html = '''<div id="songs-list">
<h2 class='title'>经典老歌</h2>
<p class='introduction'>
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view='7'>
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
# if result:
#     print(result.group(1),result.group(2))


# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(results)
# print(type(results))              #results是个列表
# for result in results:
#     print(result)
#     print(result[0],result[1],result[2])



# content = '54aK54YR5oiR54ix5L2g'
# content = re.sub('\d+','',content)
# print(content)

#提取所有li节点的歌名,用正则表达式
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
# print(results)
# for result in results:
#     print(result[1])
#
# #提取所有li节点的歌名,用sub()。将所有的a节点都替换成空
# html = re.sub('<a.*?>|</a>','',html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# for result in results:
#     print(result.strip())


content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')          #得到正则表达式对象，以便以后反复使用
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)
