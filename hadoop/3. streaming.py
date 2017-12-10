Hadoop Streaming：
	是Hadoop提供的一个编程工具，它允许用户使用任何可执行文件或者脚本文件作为Mapper和Reducer是Hadoop提供的一个编程工具，它允许用户使用任何可执行文件或者脚本文件作为Mapper和Reducer
	cat input.txt | python Mapper.py | sort | python Reducer.py > output

原理：
	mapper和reducer会从标准输入中读取用户数据，一行一行处理后发送给标准输出。Streaming工具会创建MapReduce作业，发送给各个tasktracker，同时监控整个作业的执行过程。
	如果一个文件（可执行或者脚本）作为mapper，mapper初始化时，每一个mapper任务会把该文件作为一个单独进程启动，mapper任务运行时，它把输入切分成行并把每一行提供给可执行文件进程的标准输入。 同时，mapper收集可执行文件进程标准输出的内容，并把收到的每一行内容转化成key/value对，作为mapper的输出。 默认情况下，一行中第一个tab之前的部分作为key，之后的（不包括tab）作为value。如果没有tab，整行作为key值，value值为null。
	对于reducer，类似。
	以上是Map/Reduce框架和streaming mapper/reducer之间的基本通信协议。
局限：
	1、streaming默认只能处理文本数据，如果想对二进制数据进行处理，可以对二进制的key和value进行base64编码转成文本。
	2、两次数据拷贝和解析（分割），影响时效性。
	
简单案例：
	run.sh:
		# stream地址
		STREAM_PATH ="/usr/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"
		
		#需要处理的文件，/表示在hdfs根目录下
		INPUT_FILE_PATH = "/file1.txt"
		#处理后的文件保存目录
		OUTPUT_PATH ="/output"
		#如果保存的目录已经存在就删除，否则会报错
		/usr/hadoop-1.2.1/bin/hadoop fs -rmr $SOUTPUT_PATH
		
		#开始执行
		/usr/hadoop-1.2.1/bin/hadoop jar $STREAM_PATH
			-input $INPUT_FILE_PATH \
			-output $OUTPUT_PATH \
			-mapper "python map.py" \
			-reduce "python red.py" \
			-jobconf "mapred.reduce.tasks=2" \
			-file ./map.py \
			-file ./red.py
		
		
		
		
		
		
		
		
		
		
		
		
		