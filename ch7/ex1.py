# selenium实例示范
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     wait = WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


#selenium支持很对类型的浏览器，如chrome,firefox,edge等，还有手机端的浏览器
#声明浏览器对象
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()


#使用get来访问页面，传入参数url即可
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()


#查找节点
#selenium可以驱动浏览器完成各种操作，比如填充表单，模拟点击等
#比如我们要完成某个输入框文字的操作，总需要知道这个输入框在哪里吧，
#selenium提供了一系列查找节点的方法

#单个节点
#find_element_by_name()是根据name值获取;find_element_by_id()根据id获取
#也可以用xpath,css选择器获取
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_name('q')
# input_third = browser.find_element_by_css_selector('#q')
# input_fourth = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_second,input_third,input_fourth)
# #返回结果类型都是WebElement类型
# browser.close()


#其他获取单个节点的方法
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_tag_name()
# find_element_by_class_name()


#selenium提供了通用方法find_element(),需要传入两个参数：查找方式By和值
#find_element实际上是find_element_by_id()方法的通用版本
#find_element_by_id(id) 等价于 find_element(By.ID,id)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID,'q')
# print(input_first)
# browser.close()

#查找多个节点find_elements(),在上面的查找单个节点中加上s
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')   #lis是一个列表
# for li in lis:
#     print(li)  #返回的每个结果是webelement类型
# browser.close()


#其他获取多个节点的方法
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_xpath()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_tag_name()
# find_elements_by_class_name()
# find_elements_by_css_selector()

#也可以用find_elements()方法来选择
# lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')



#selenium可以模型浏览器的一些动作
#比较常见的动作有输入文字send_keys();清空文字时用clear()方法；点击按钮时用click()方法

# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iphone')  #注意这里只是输入了'iphone',但是并没有按下搜索按钮
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()


#在上面的动作都是针对某个节点执行的，但有些动作没有节点而言
#比如，鼠标拖拽，键盘按键，这些动作称为动作链

#实现一个节点的拖拽操作，将某个节点从一处拖拽到另一处
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()



#对于某些操作，Selenium api没有提供，比如下拉进度条
#像下拉进度条可以直接模拟运行javascript，此时使用execute_script()方法即可
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

#selenium已经提供了选择节点的方法，返回的是webelement类型，可以直接通过方法和属性提取节点信息
#获取属性
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_class_name("Icon")   #如果class_name有多个，只能选一个
# print(logo)
# print(logo.get_attribute('class'))


#获取文本
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# zhuanti = browser.find_element_by_class_name('ExploreHomePage-ContentSection-header')
# print(zhuanti.text)


#获取id,位置，标签名和大小
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# #知乎网页已经更新，不能用了
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag.name)
# print(input.size)

#网页中有一种节点叫iframe,也就是子Frame,相当于页面的子页面，它的结构和外部网页的结构完全一致
#selenium打开页面后，它是默认在父级frame里面操作，如果此时页面中还有子frame,它是不能获取到子frame里面的节点
#这时需要使用switch_to.frame()方法来切换frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')https://blog.csdn.net/huilan_same/article/details/52200586
# #switch_to.frame(referenct) 参考 https://blog.csdn.net/huilan_same/article/details/52200586
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)



#selenium的get()方法会在网页框架加载结束后结束执行，此时如果获取page_source()，
#可能不是浏览器完全加载的页面，比如某些Ajax请求，我们在网页的源代码中不一定能成功获取
#所以需要一定的延时等待，确保节点已经加载出来

#隐式等待:如果selenuim没有找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('Button')
# print(input)



#显示等待：指定要查找的节点，然后指定一个最长的等待时间，如果在规定时间
#内加载出了这个节点，就返回这个节点，如果在规定时间没有加载出来，则抛出异常
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# #对于按钮来说，出现的等待条件是element_to_be_clickable()
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input)
# print(button)



#平常使用浏览器都有前进和后退的功能，selenium也可以完成这个操作，使用back(),forward()
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()



#使用 selenium可以方便地对cookies进行操作
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


#选项卡管理
#开启新的浏览器窗口
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://www.python.org/')


#selenium的异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('time out')
try:
    browser.find_element_by_id('Hello')
except NoSuchElementException:
    print('no element')
finally:
    browser.close()
