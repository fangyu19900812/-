# 开源分布式实时计算系统
	 
# 没有持久化层
# 保证消息得到处理
# 支持多种编程语言
# 高效，用zeroMQ(老版本)作为底层消息队列
# 支持本地模拟测试，壳模拟集群所有功能

storm vs hadoop
# storm任务不会结束，持续，来一个执行一个。 hadoop任务会结束，执行完成停止。
# storm延时低，网络直传、内存计算，节省批处理的收集数据的时间
# hadoop使用磁盘作为交换介质，storm是内存运行。
# storm吞吐不及hadoop,不适合批处理计算模型。

主：nimbus
从：supervisor
spout相当于mr的jobTracker
bolt相当于mr的taskTracker 是线程不是进程

stream groupomg
	shuffle groupong:随机分组 （常用）
	fields groupong:按指定的field分组 按key分割分桶 （常用）
	all groupong:广播分组
	global groupong:全局分组

 










