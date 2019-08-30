from urllib.robotparser import RobotFileParser
from urllib.request import urlopen,Request

#urllib.robotparser.RobotFileParser(url='')

# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp = RobotFileParser('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))




headers = {'User-Agent':'Chrome/75.0.3770.142'}
req = Request(url='http://www.jianshu.com/robots.txt',headers=headers)
rp = RobotFileParser()
rp.parse(urlopen(req).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))
