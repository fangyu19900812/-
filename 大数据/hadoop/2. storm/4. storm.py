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
spout相当于mr的jobTracker 但spout是线程不是进程
bolt相当于mr的taskTracker 但bolt是线程不是进程
storm进程叫worker MR进程叫child   不会结束，除非主动kill
storm任务叫Topology MR任务叫job
基本单位
	storm:tuple
	hdfs:block
任务不需要nimbus来运行，需要supervisor

nimbus和supervisor 协调都通过zookeeper完成

storm 并行度
http://blog.csdn.net/qq_37095882/article/details/77624340
 

stream grouping
		a1   b1
		a2   b2
	shuffle grouping:随机分组 （常用）
		a1 -> b1
		a2 -> b2
	fields grouping:按指定的field分组 按key分割分桶 （常用）
		a1 -> b2
		a2 -> b1
	all grouping:广播分组
		a1 -> b1,b2
		a2 -> b1,b2
	global grouping:全局分组
		a1 -> b1
		a2 -> b1


LocalCluster cluster = new LocalCluster();
cluster.submitTopology(TOPOLOGY_NAME, config, builder.createTopology());

就不需要运行zookeeper，nimbus，supervisor，在storm ui也不会显示topology，因为是本地模拟。

如果用下面方式：
[Actionscript3] 纯文本查看 复制代码
StormSubmitter.submitTopology(TOPOLOGY_NAME, config, builder.createTopology());

则需要启动zookeeper，nimbus，supervisor，会在storm ui显示

wordcount在eclipse打印不了system.out.print信息用这个
https://blog.csdn.net/the_conquer_zzy/article/details/78771367








