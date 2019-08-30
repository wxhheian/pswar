from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""
# html = etree.HTML(text)
# result = etree.tostring(html)   #输出结果为bytes类型
# print(result.decode('utf-8'))    #利用decode()将bytes转成str类型



#直接读取文本文件进行解析,test.html内容为text
# html = etree.parse('./test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))


#// 从当前节点选取子孙节点      / 从当前节点选取直接子节点

# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//*')    # *代表匹配所有节点
# print(result)


# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li')    #匹配所有li节点
# print(result)
# print(result[0])


# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a')     #所有li节点下的a节点
# print(result)


# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//ul//a')             #结果与38-40行代码相同
# print(result)
#
#
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//ul/a')             ##结果为空
# print(result)


# . 选取当前节点   .. 选取当前节点的父节点  @ 选取属性

# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)
#
#
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)          # 结果与55-57行代码结果一样


# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)


# 获取文本
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)         #获得结果为['\n']  思考为什么


# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)
#
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)                   #思考与77行代码的区别



#属性获取
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)


#属性多值匹配
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')            #这里class属性有两个，一个是li,一个是li-first
# print(result)            #结果为空


#属性多值匹配
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li")]/a/text()')            #这里class属性有两个，一个是li,一个是li-first
# print(result)


#多属性匹配
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)


#按序选择
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)



#节点轴选择
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

html = etree.HTML(text)
result =html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')      #following 包含自身
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
