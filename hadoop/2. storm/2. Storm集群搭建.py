
版本：apache-storm-0.9.3
前置：java、python、zookeeper
1、解压apache-storm-0.9.3.tar.gz

2、进入apache-storm-0.9.3/conf目录
	修改storm.yaml
		zookeeper服务host也可以写ip
		storm.zookeeper.servers:
			- "master"
			- "slave1"
			- "slave2"
			如果Zookeeper集群使用的不是默认端口，那么还需要storm.zookeeper.port选项。	
		nimbus.host:"master"   
		supervisor.slots.ports:  最多5个端口
			- 6700
			- 6701
			- 6702
			- 6703
			- 6704
			注意一点是：配置条目的冒号后面要有一个空格，下面的对应值横杠两侧都要有空格，前面可以多输入几个，注意这些细节可以避免很多错误
		storm.local.dir: "/home/admin/storm/workdir" 需要提前创建
		
3、启动（是用python启动的，框架是java开发）
	#bash run.sh
	master节点
		run.sh
			python bin/storm nimbus &
			python bin/storm ui &   是master:8080/index.html页面
			python bin/storm logviewer &
		kill.sh
			kill `ps aux | fgrep storm | fgrep -v 'fgrep' | awk '{print $2}'`
			
	slave节点
		run.sh
			python bin/storm supervisor &
			python bin/storm logviewer &
			
	启动会比较慢，会有消息打印出来。
	#jps
	主：nimbus
		core
		logviewer
	从：supervisor
		logviewer
	

4、运行项目
	把java程序打成jar包：比如一个名称为chengxu工程打包成名称为dabaochengxu.jar
	python apache-storm-0.9.3/bin/storm jar ./dabaochengxu.jar chengxu.start remote
	python storm目录 jar ./打的jar包 项目的启动方法main 传参参数
	
	

