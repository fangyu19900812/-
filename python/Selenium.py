
#其他包
import time

# 导入 webdriver
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# webdriver.Chrome()
# webdriver.Firefox()
# webdriver.Ie()
driver = webdriver.PhantomJS()  

# 如果没有在环境变量指定PhantomJS位置
driver = webdriver.PhantomJS(executable_path="./phantomjs")

####################### 模拟登陆 无验证码 ###########################
driver.get("http://www.douban.com")
# 输入账号密码
driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
driver.find_element_by_name("form_password").send_keys("xxxxxxxx")
# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()
# 等待3秒 太快页面会没有加载
time.sleep(3)
# 生成登陆后快照 保存在当前运行目录下
driver.save_screenshot("douban.png")
####################### 模拟登陆 无验证码 ###########################


# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

# 打印数据内容
print data

# 打印页面标题 "百度一下，你就知道"
print driver.title

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("kw").send_keys(u"长城")

# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()

# 获取新的页面快照
time.sleep(3)
driver.save_screenshot("长城.png")

# 打印网页渲染后的源代码
print driver.page_source

# 获取当前页面Cookie
print driver.get_cookies()

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("itcast")

# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
driver.find_element_by_id("kw").clear()

# 获取当前url
print driver.current_url


###################################################### 
################## 页面操作
###################################################### 
	#<input type="text" name="user-name" id="passwd-id" />
	# 获取id标签值
	element = driver.find_element_by_id("passwd-id")
	# 获取name标签值
	element = driver.find_element_by_name("user-name")
	# 获取标签名值
	element = driver.find_elements_by_tag_name("input")
	# 也可以通过XPath来匹配
	element = driver.find_element_by_xpath("//input[@id='passwd-id']")
	
	
	
######################################################  
################## 定位UI元素 (WebElements)
###################################################### 
	#find_element_by_id 
	#<div id="coolestWidgetEvah">...</div>
	id = driver.find_element_by_id("coolestWidgetEvah") 
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	id = driver.find_element(by=By.ID, value="coolestWidgetEvah")

	#find_elements_by_name
	#<input name="cheese" type="text"/>
	name = driver.find_element_by_name("cheese")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	name = driver.find_element(By.NAME, "cheese")

	#find_elements_by_xpath
	#<input type="text" name="example" />
	#<INPUT type="text" name="other" />
	xpath = driver.find_elements_by_xpath("//input")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	xpath = driver.find_elements(By.XPATH, "//input")
	
	#find_elements_by_link_text
	#<a href="http://www.google.com/search?q=cheese">cheese</a>
	link_text = driver.find_element_by_link_text("cheese")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	link_text = driver.find_element(By.LINK_TEXT, "cheese")
	
	#find_elements_by_partial_link_text
	#<a href="http://www.google.com/search?q=cheese">search for cheese</a>
	partial_link_text = driver.find_element_by_partial_link_text("cheese")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")
	
	#find_elements_by_tag_name
	#<iframe src="..."></iframe>
	tag_name = driver.find_element_by_tag_name("iframe")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	tag_name = driver.find_element(By.TAG_NAME, "iframe")
	
	#find_elements_by_class_name
	#<div class="cheese"><span>Cheddar</span></div><div class="cheese"><span>Gouda</span></div>
	class_name = driver.find_elements_by_class_name("cheese")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	class_name = driver.find_elements(By.CLASS_NAME, "cheese")
	
	#find_elements_by_css_selector
	#<div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>
	css_selector = driver.find_element_by_css_selector("#food span.dairy.aged")
	#------------------------ or -------------------------
	from selenium.webdriver.common.by import By
	css_selector = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

	
######################################################  
################## 模拟键盘输入
###################################################### 
	from selenium.webdriver.common.keys import Keys
	# Keys.BACK_SPACE：回退键（BackSpace） 
	# Keys.TAB：制表键（Tab） 
	# Keys.ENTER：回车键（Enter） 
	# Keys.SHIFT：大小写转换键（Shift） 
	# Keys.CONTROL：Control键（Ctrl） 
	# Keys.ALT：ALT键（Alt） 
	# Keys.ESCAPE：返回键（Esc） 
	# Keys.SPACE：空格键（Space） 
	# Keys.PAGE_UP：翻页键上（Page Up） 
	# Keys.PAGE_DOWN：翻页键下（Page Down） 
	# Keys.END：行尾键（End） 
	# Keys.HOME：行首键（Home） 
	# Keys.LEFT：方向键左（Left） 
	# Keys.UP：方向键上（Up） 
	# Keys.RIGHT：方向键右（Right） 
	# Keys.DOWN：方向键下（Down） 
	# Keys.INSERT：插入键（Insert） 
	# DELETE：删除键（Delete） 
	# NUMPAD0 ~ NUMPAD9：数字键1-9  
	# F1 ~ F12：F1 - F12键 
	send_keys(xxxx)
	# 全选（Ctrl+A）
	send_keys(Keys.CONTROL,'a')
	# 复制（Ctrl+C）
	send_keys(Keys.CONTROL,'c')
	# 剪切（Ctrl+X）
	send_keys(Keys.CONTROL,'x')
	# 粘贴（Ctrl+V）
	send_keys(Keys.CONTROL,'v')
	# 在搜索框中输入"中国"
	send_keys(u"中国")
	
######################################################  
################## 鼠标动作链
###################################################### 	
	#导入 ActionChains 类
	from selenium.webdriver import ActionChains

	# 鼠标移动到 ac 位置 鼠标悬停
	ac = driver.find_element_by_xpath('element')
	ActionChains(driver).move_to_element(ac).perform()
	
	# 在 ac 位置单击
	ac = driver.find_element_by_xpath("elementA")
	ActionChains(driver).move_to_element(ac).click(ac).perform()

	# 在 ac 位置双击
	ac = driver.find_element_by_xpath("elementB")
	ActionChains(driver).move_to_element(ac).double_click(ac).perform()

	# 在 ac 位置右击
	ac = driver.find_element_by_xpath("elementC")
	ActionChains(driver).move_to_element(ac).context_click(ac).perform()

	# 在 ac 位置左键单击hold住
	ac = driver.find_element_by_xpath('elementF')
	ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

	# 将 ac1 拖拽到 ac2 位置
	ac1 = driver.find_element_by_xpath('elementD')
	ac2 = driver.find_element_by_xpath('elementE')
	ActionChains(driver).drag_and_drop(ac1, ac2).perform()
	
	
	
######################################################  
################## 填充表单
###################################################### 	
	''' 我们已经知道了怎样向文本框中输入文字，但是有时候我们会碰到<select> </select>标签的下拉框。直接点击下拉框中的选项不一定可行。
		<select id="status" class="form-control valid" onchange="" name="status">
			<option value=""></option>
			<option value="0">未审核</option>
			<option value="1">初审通过</option>
			<option value="2">复审通过</option>
			<option value="3">审核不通过</option>
		</select>
	'''
	# 导入 Select 类
	from selenium.webdriver.support.ui import Select

	# 找到 name 的选项卡
	select = Select(driver.find_element_by_name('status'))

	# index 选择索引为1的项，索引从 0 开始
	select.select_by_index(1)
	
	# 选择value为0的项，value是option标签的一个属性值，并不是显示在下拉框中的值
	select.select_by_value("0")
	
	# 选择文本的值为"未审核"的项，visible_text是在option标签文本的值，是显示在下拉框的值
	select.select_by_visible_text(u"未审核")
	
	#全部取消选择怎么办呢？很简单:
	select.deselect_all()

	
	
######################################################  
################## 弹窗处理
###################################################### 	
	#当你触发了某个事件之后，页面出现了弹窗提示，处理这个提示或者获取提示信息方法如下：
	alert = driver.switch_to_alert()

	
######################################################  
################## 页面切换
###################################################### 	
	#一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换。切换窗口的方法如下：
	driver.switch_to.window("this is window name")

	#也可以使用 window_handles 方法来获取每个窗口的操作对象。例如：
	for handle in driver.window_handles:
		driver.switch_to_window(handle)
		

		
######################################################  
################## 页面前进和后退
###################################################### 	
	#操作页面的前进和后退功能：
	driver.forward()     #前进
	driver.back()        # 后退

	
	
######################################################  
################## Cookies
###################################################### 
	#获取页面每个Cookies值，用法如下
	for cookie in driver.get_cookies():
		print "%s -> %s" % (cookie['name'], cookie['value'])
		
	#删除Cookies，用法如下
	# By name
	driver.delete_cookie("CookieName")

	# all
	driver.delete_all_cookies()



######################################################  
################## 页面等待
###################################################### 
	'''
	注意：这是非常重要的一部分！！

	现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。

	为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。所以 Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待。

	隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。
	'''
	#显式等待
	#显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常了。
		from selenium import webdriver
		from selenium.webdriver.common.by import By
		# WebDriverWait 库，负责循环等待
		from selenium.webdriver.support.ui import WebDriverWait
		# expected_conditions 类，负责条件出发
		from selenium.webdriver.support import expected_conditions as EC

		driver = webdriver.Chrome()
		driver.get("http://www.xxxxx.com/loading")
		try:
			# 页面一直循环，直到 id="myDynamicElement" 出现
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.ID, "myDynamicElement"))
			)
		finally:
			driver.quit()
		#下面是一些内置的等待条件，你可以直接调用这些条件，而不用自己写某些等待条件了。
			title_is
			title_contains
			presence_of_element_located
			visibility_of_element_located
			visibility_of
			presence_of_all_elements_located
			text_to_be_present_in_element
			text_to_be_present_in_element_value
			frame_to_be_available_and_switch_to_it
			invisibility_of_element_located
			element_to_be_clickable – it is Displayed and Enabled.
			staleness_of
			element_to_be_selected
			element_located_to_be_selected
			element_selection_state_to_be
			element_located_selection_state_to_be
			alert_is_present
			
	#隐式等待
	#隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。
		from selenium import webdriver

		driver = webdriver.Chrome()
		driver.implicitly_wait(10) # seconds
		driver.get("http://www.xxxxx.com/loading")
		myDynamicElement = driver.find_element_by_id("myDynamicElement")
		#当然如果不设置，默认等待时间为0。
	
	
	
######################################################  
################## 执行 JavaScript 语句
###################################################### 
	#隐藏百度图片
		from selenium import webdriver
		driver = webdriver.PhantomJS()
		driver.get("https://www.baidu.com/")
		# 给搜索输入框标红的javascript脚本
		js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
		# 调用给搜索输入框标红js脚本
		driver.execute_script(js)
		#查看页面快照
		driver.save_screenshot("redbaidu.png")
		#js隐藏元素，将获取的图片元素隐藏
		img = driver.find_element_by_xpath("//*[@id='lg']/img")
		driver.execute_script('$(arguments[0]).fadeOut()',img)
		# 向下滚动到页面底部
		driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")
		#查看页面快照
		driver.save_screenshot("nullbaidu.png")
		driver.quit()
		
	#模拟滚动条滚动到底部
		from selenium import webdriver
		import time
		driver = webdriver.PhantomJS()
		driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")
		# 向下滚动10000像素
		js = "document.body.scrollTop=10000"
		#js="var q=document.documentElement.scrollTop=10000"
		time.sleep(3)
		#查看页面快照
		driver.save_screenshot("douban.png")
		# 执行JS语句
		driver.execute_script(js)
		time.sleep(10)
		#查看页面快照
		driver.save_screenshot("newdouban.png")
		driver.quit()
		
######################################################  
################## 退出
######################################################
	driver.quit()


