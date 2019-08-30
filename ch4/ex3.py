from pyquery import PyQuery as pq

# html ='''
# <div>
# <ul>
# <li class ="item-O">first item</li>
# <li class="item-1">a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class ="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('li'))

#初始化URL
# doc = pq(url="https://cuiqingcai.com")    #不仅可以传入字符串,如14行代码,也可以传入网页URL
# print(doc('title'))
#
# import requests
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))         #结果与18-19行代码一样



#文件初始化
# doc = pq(filename='demo.html')    #要求本地存在一个demo.html
# print(doc('li'))


html ='''
<div id="container">
<ul class="list">
<li class ="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class ="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))    #class 'pyquery.pyquery.PyQuery'


# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')         #find()查找所有子孙节点
# print(type(lis))
# print(lis)
# lis = items.children()        #只查找子节点
# print(type(lis))
# print(lis)
# lis = items.children('.active')
# print(lis)



# html ='''
# <div class="wrap">
# <div id="container">
# <ul class="list">
# <li class="item-O">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# </div>
# '''
# doc = pq(html)
# items = doc('.list')
# container = items.parent()   #直接父节点
# print(type(container))
# print(container)
# parents = items.parents()
# print(type(parents))
# print(parents)          #输出结果有两个
# parent = items.parents('.wrap')
# print(parent)


# doc = pq(html)
# li = doc('.list .item-0.active')    #注意这里两个属性的写法
# print(li.siblings())
# print(li.siblings('.active'))


# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(str(li))


# doc = pq(html)
# lis = doc('li').items()
# print(type(lis))           #class generator
# for li in lis:
#     print(li,type(li))


html ='''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a,type(a))
# print(a.attr('href'))
# print(a.attr.href)
# a = doc('a')
# print(a,type(a))
# print(a.attr('href'))      #只能获取第一个属性
# print(a.attr.href)              #只能获取第一个属性


# doc = pq(html)
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))       #通过遍历获得所有属性

# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())


# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())      #获取li节点内的html文本


# doc = pq(html)
# li = doc('li')
# print(li.html())    #只返回一个第一个结果，想获得所有结果，必须遍历
# print(li.text())    #返回了所有结果
# print(type(li.text()))




# html ='''
# <div class="wrap">
# <div id="container">
# <ul class="list">
# <li class="item-O">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# </div>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)



# html = '''
# <ul class="list">
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# </ul>
# '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name','link')  #增加属性
# print(li)
# li.text('changed item')     #li节点内部全部改变成了传入的文本
# print(li)
# li.html('<span>changed item</span>')   #li节点内部全部改变成了传入的HTML文本
# print(li)



# html = '''
# <div class="wrap">
#     Hello, World
# <p>This is a paragraph.</p>
# </div>
# '''
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
#
# doc = pq(html)
# wrap = doc('.wrap')
# wrap.find('p').remove()
# print(wrap.text())



html ='''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')   #第二个节点
print(li)
li = doc('li:gt(2)')       #第三个li之后的li节点
print(li)
li = doc('li:nth-child(2n)')     #偶数位置的li节点
print(li)
li = doc('li:contains(second)')       #包含second文本的li节点
print(li)
