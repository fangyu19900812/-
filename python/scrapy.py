################################
#### 新建项目：
################################
	# 进入自定义的项目目录中，运行下列命令：
	scrapy startproject mySpider

	scrapy.cfg ：项目的配置文件
	mySpider/ ：项目的Python模块，将会从这里引用代码
	mySpider/items.py ：项目的目标文件
	mySpider/pipelines.py ：项目的管道文件
	mySpider/settings.py ：项目的设置文件
	mySpider/spiders/ ：存储爬虫代码目录
	
	
################################	
#### 案例：腾讯招聘网自动翻页采集
################################
	# 编写items.py 获取职位名称、详细信息
	# Item 定义结构化数据字段，用来保存爬取到的数据，有点像Python中的dict，但是提供了一些额外的保护减少错误。
	# 可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field的类属性来定义一个Item（可以理解成类似于ORM的映射关系）。
	# 创建一个ItcastItem 类，和构建item模型（model）
		class TencentItem(scrapy.Item):
			name = scrapy.Field()
			detailLink = scrapy.Field()
			positionInfo = scrapy.Field()
			peopleNumber = scrapy.Field()
			workLocation = scrapy.Field()
			publishTime = scrapy.Field()
	
	# 创建一个新的爬虫 会在mySpider/spiders/目录下看到tencent.py：
		scrapy genspider tencent "tencent.com"
		# class scrapy.Spider是最基本的类，所有编写的爬虫必须继承这个类。
		# 主要用到的函数及调用顺序为：
		# __init__() : 初始化爬虫名字和start_urls列表
		# start_requests() 调用make_requests_from url():生成Requests对象交给Scrapy下载并返回response
		# parse() : 解析response，并返回Item或Requests（需指定回调函数）。Item传给Item pipline持久化 ， 而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。
		
		# 主要属性和方法
			name 
				# 定义spider名字的字符串。
				# 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite
			allowed_domains
				# 包含了spider允许爬取的域名(domain)的列表，可选。
			start_urls
				# 初始URL元祖/列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。
			start_requests(self)
				# 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取（默认实现是使用 start_urls 的url）的第一个Request。
				# 当spider启动爬取并且未指定start_urls时，该方法被调用。
			parse(self, response)
				# 当请求url返回网页没有指定回调函数时，默认的Request对象回调函数。用来处理网页返回的response，以及生成Item或者Request对象。
			log(self, message[, level, component])
				# 使用 scrapy.log.msg() 方法记录(log)message。 更多数据请参见 logging
				
		# 源码
		from mySpider.items import TencentItem
		import scrapy
		import re
		class TencentSpider(scrapy.Spider):
			name = "tencent"
			allowed_domains = ["hr.tencent.com"]
			start_urls = [
				"http://hr.tencent.com/position.php?&start=0#a"
			]
			def parse(self, response):
				for each in response.xpath('//*[@class="even"]'):
					item = TencentItem()
					name = each.xpath('./td[1]/a/text()').extract()[0]
					detailLink = each.xpath('./td[1]/a/@href').extract()[0]
					positionInfo = each.xpath('./td[2]/text()').extract()[0]
					peopleNumber = each.xpath('./td[3]/text()').extract()[0]
					workLocation = each.xpath('./td[4]/text()').extract()[0]
					publishTime = each.xpath('./td[5]/text()').extract()[0]
					#print name, detailLink, catalog, peopleNumber, workLocation,publishTime
					item['name'] = name.encode('utf-8')
					item['detailLink'] = detailLink.encode('utf-8')
					item['positionInfo'] = positionInfo.encode('utf-8')
					item['peopleNumber'] = peopleNumber.encode('utf-8')
					item['workLocation'] = workLocation.encode('utf-8')
					item['publishTime'] = publishTime.encode('utf-8')
					curpage = re.search('(\d+)',response.url).group(1)
					page = int(curpage) + 10
					url = re.sub('\d+', str(page), response.url)
					# 发送新的url请求加入待爬队列，并调用回调函数 self.parse
					yield scrapy.Request(url, callback = self.parse)
					# 将获取的数据交给pipeline
					yield item			
		
	# 编写Item Pipeline 编写pipeline.py文件 其中process_item()方法必须实现:
		import something
		class SomethingPipeline(object):
			def __init__(self):    
				# 可选实现，做参数初始化等
				# doing something
			def process_item(self, item, spider):
				# item (Item 对象) – 被爬取的item
				# spider (Spider 对象) – 爬取该item的spider
				# 这个方法必须实现，每个item pipeline组件都需要调用该方法，
				# 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
				return item
			def open_spider(self, spider):
				# spider (Spider 对象) – 被开启的spider
				# 可选实现，当spider被开启时，这个方法被调用。
			def close_spider(self, spider):
				# spider (Spider 对象) – 被关闭的spider
				# 可选实现，当spider被关闭时，这个方法被调用
		
		# 源码
		import json
		class TencentJsonPipeline(object):
			def __init__(self):
				self.file = open('tencent.json', 'wb')
			def process_item(self, item, spider):
				content = json.dumps(dict(item), ensure_ascii=False) + "\n"
				self.file.write(content)
				return item
			def close_spider(self, spider):
				self.file.close()
	
	# setting.py 分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内（0-1000随意设置，数值越低，组件的优先级越高）
		ITEM_PIPELINES = {
			#'mySpider.pipelines.SomePipeline': 300,
			"mySpider.pipelines.TencentJsonPipeline":300
		}
	
	# 执行爬虫
		scrapy crawl tencent
		# 运行之后，如果打印的日志出现 [scrapy] INFO: Spider closed (finished)，代表执行完成。 之后当前文件夹中就出现了一个 tencent.html 文件，里面就是我们刚刚要爬取的网页的全部源代码信息。
		# scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，，命令如下：
		# json格式，默认为Unicode编码
		scrapy crawl tencent -o tencent.json
		# json lines格式，默认为Unicode编码
		scrapy crawl tencent -o tencent.jsonl
		# csv 逗号表达式，可用Excel打开
		scrapy crawl tencent -o tencent.csv
		# xml格式
		scrapy crawl tencent -o tencent.xml

	# 注意，Python2.x默认编码环境是ASCII，当和取回的数据编码格式不一致时，可能会造成乱码；
	# 我们可以指定保存内容的编码格式，一般情况下，我们可以在代码最上方添加：
		import sys
		reload(sys)
		sys.setdefaultencoding("utf-8")
	# 这三行代码是Python2.x里解决中文编码的万能钥匙，经过这么多年的吐槽后Python3学乖了，默认编码是Unicode了


















