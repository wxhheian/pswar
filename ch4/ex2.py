from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>','lxml')
# print(soup.p.string)        #打印内容


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their name were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())    #自动更正格式在17行已经做好，18行代码只是让字符串以标准缩进形式输出
# print(soup.title)
# print(soup.title.string)


# soup = BeautifulSoup(html,'lxml')
# print(soup.title)
# print(soup.title.name)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)           #只打印第一个


#提取信息
# soup = BeautifulSoup(html,'lxml')
# print(soup.title.name)
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print(soup.p['name'])
# print(soup.p['class'])


#嵌套选择
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)



#关联选择
# html = """
# <html>
# <head>
# <title>The Dormouse's story</title>
# </head>
# <body>
# <p class="story">
#     Once upon a time there were three little sisters; and their name were
#     <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
# and they lived at the bottom of a well.
# </p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.p.contents)           #p的直接子节点的列表
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):           #结果与73行代码结果一样
#     print(i,child)
# print(soup.p.descendants)   #p的所有子孙节点
# for i,child in enumerate(soup.p.descendants):    #递归查询所有子节点
#     print(i,child)


#父节点和祖先节点
# html = """
# <html>
# <head>
# <title>The Dormouse's story</title>
# </head>
# <body>
# <p class="story">
#             Once upon a time there were three little sisters; and their name were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.a.parent)           #a的直接父节点

# html = """
# <html>
# <body>
# <p class="story">
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# """
# soup = BeautifulSoup(html,'lxml')
# print(type(soup.a.parents))          #class 'generator'
# print(list(enumerate(soup.a.parents)))            #生成器转list   注意有4个，而不是3个


#兄弟节点
# html = """
# <html>
# <body>
# <p class="story">
#             Once upon a time there were three little sisters; and their name were
# <a href="http://example.com/elsie" class="sister" id="link1">
# <span>Elsie</span>
# </a>
#             Hello
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
# </p>
# """
# soup = BeautifulSoup(html,'lxml')
# print('Next Sibling',soup.a.next_sibling)
# print('Prev Sibling',soup.a.previous_sibling)
# print('Next Siblins',list(enumerate(soup.a.next_siblings)))
# print('Prev Siblins',list(enumerate(soup.a.previous_siblings)))



# html = """
# <html>
# <body>
# <p class="story">
#             Once upon a time there were three little sisters; and their name were
# <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
# class="sister" id="link2">Lacie</a>
# </p>
# """
# soup = BeautifulSoup(html,'lxml')
# print('Next Sibling:')
# print(type(soup.a.next_sibling))       #class 'bs4.element.Tag'
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))             #class 'generator'
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])



#find_all(name,attrs,recursive,text,**kwargs)
# html="""
# <div class ="panel">
# <div class ="panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body">
# <ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class ="element">Foo</li>
# <li class ="element">Bar</li>
# </ul>
# </div>
# </div>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# # for ul in soup.find_all(name='ul'):
# #     print(ul.find_all(name='li'))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)



# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))
#对于一些常见的属性，比如id,class的查询
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))



# import re
# html = '''
# <div class="panel">
# <div class= "panel-body">
# <a>Hello,this is a link</a>
# <a>Hello,this is a link,too</a>
# </div>
# </div>
# '''
# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(text=re.compile('link')))




# html="""
# <div class ="panel">
# <div class ="panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body">
# <ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class ="element">Foo</li>
# <li class ="element">Bar</li>
# </ul>
# </div>
# </div>
# """
# soup = BeautifulSoup(html,'lxml')
# print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='list'))




#CSS选择器
html="""
<div class ="panel">
<div class ="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
</ul>
</div>
</div>
"""
###CSS语法说明     #head_wrapper.s-ps-islite .s-p-top  选中id为head_wrapper且class为s-ps-islite的节点，然后再选中其中内部的s-p-top的节点
###      .class   #id     * 所有节点     element,element
# soup = BeautifulSoup(html,'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))        # class bs4.element.Tag

# soup = BeautifulSoup(html,'lxml')
# for ul in soup.select('ul'):
#     print(ul.select('li'))


# soup = BeautifulSoup(html,'lxml')
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])



soup = BeautifulSoup(html,'lxml')
for li in soup.select('li'):
    print('Get Text:',li.get_text())
    print("String:",li.string)            #get_text()与string效果一样
