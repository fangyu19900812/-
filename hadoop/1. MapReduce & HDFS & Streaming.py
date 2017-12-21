
hadoop1.0
################################################
################ hadoop1.0集群搭建
################################################
	master:
		1、路径 usr/local/src/
		2、解压 hadoop
		3、进入 hadoop解压后的文件夹 创建tmp文件夹，存放临时文件
		4、进入 usr/local/src/hadoop-1.2.1/conf目录
			修改masters 
				把localhost去掉加上master
			修改slaves
				把localhost去掉加上slave1换行slave2……有多少个slave就加多少个
			修改core-site.xml
				<configuration>
				//临时文件
					<property>
						<name>hadoop.tmp.dir</name>
						<value>/usr/local/src/hadoop-1.2.1/tmp</value>
					</property>
				//namenode ip地址master ip地址
					<property>
						<name>fs.default.name</name>
						<value>hdfs://192.168.183.10:9000</value> 
					</property>
				</configuration>
			修改mapred-site.xml
				<configuration>
				//jobTracker 要http开头
					<property>
						<name>mapred.job.tracker</name>
						<value>http://192.168.183.10:9001</value>
					</property>
				</configuration>
			修改hdfs-site.xml
				<configuration>
				//配置hdfs副本数 默认3
					<property>
						<name>dfs.replication</name>
						<value>3</value>
					</property>
				</configuration>
			修改hadoop-env.sh
				//jdk目录 http://www.cnblogs.com/kerrycode/archive/2015/08/27/4762921.html
				// http://blog.csdn.net/cx118118/article/details/54955620
				export JAVA_HOME= /usr/local/src/jdkxxx
		前4步和slave一样，可以先配置slave。然后再执行下面步骤。
		5、进入 /etc目录		
			修改hosts //配置hostname。访问可以用hostname不用ip
				192.168.183.10 master
				192.168.183.11 slave1
				192.168.183.12 slave2
			修改/etc/sysconfig/network(永久生效)
				HOSTNAME=localhost改成HOSTNAME=master
			终端执行(只是临时生效、立即生效,重启失效)
				# hostname	master
				# hostname
				master
				
		注意：每次重启后都需要关闭（也可以设置永久关闭。）
			关闭防火墙
				# /etc/init.d/iptables stop （也可以只打开要试用的端口）
				[root@djt002 ~]# service iptables stop     //临时关闭防火墙
				[root@djt002 ~]# service iptables status //查看防火墙状态
				iptables: Firewall is not running.
					
			永久关闭防火墙
				[root@djt002 ~]# chkconfig iptables off //永久关闭防火墙 
				[root@djt002 ~]# chkconfig iptables on //永久打开防火墙
				
			关闭selinux
				# setenforce 0
				# getenforce
				Permissive //表示成功关闭
				
			永久关闭selinux
				# vim /etc/selinux/config
					  #SELINUX=enforcing //注释
					  #SELINUXTYPE=targeted //注释
					  SELINUX=disable //新增
		6、设置免密码远程登录ssh 没有的需要安装
			# ssh-keygen  //一直回车
			# cd ~/.ssh/
			# cp id_rsa.pub authorized_keys
			复制slave公钥 id_rsa.pub里面的内容到master的autorized_keys
			所有的slave公钥复制完成后把master的autorized_keys复制到各个slave
			# scp -rp authorized_keys slave1:~/.ssh/   //scp -rp authorized_keys 192.168.183.11:~/.ssh/
			//不需要密码就是设置成功
			# ssh slave1 
			# exit //退出
			//报错masters: ssh: Could not resolve hostname masters: Name or service not known
			把/usr/local/src/hadoop-1.2.1/conf里面的masters删除重新创建一个 如果是slave报错就删除重建slaves
		7、启动集群
			进入 usr/local/src/hadoop-1.2.1/bin目录
			//第一次启动需要格式化
			# ./hadoop namenode -format
			# ./start-all.sh
			# jps
			111 NameNode
			112 SecondaryNameNode
			113 Jps
			114 JobTracker
			//测试是否能执行成功
			# ./hadoop fs -ls /
	slave:
		1-4 与master一样 把master的hadoop复制到slave 就不用重复执行 
		终端执行 scp -rp hadoop-1.2.1 192.168.183.11:/usr/local/src/
		//slave没有设置hostname只能用ip 否则可以scp -rp hadoop-1.2.1 slave1:/usr/local/src/

		5、进入 /etc目录		
			修改hosts //配置hostname。访问可以用hostname不用ip
				192.168.183.10 master
				192.168.183.11 slave1
				192.168.183.12 slave2
			修改/etc/sysconfig/network(永久生效，重启生效、)
				HOSTNAME=localhost改成HOSTNAME=slave1
			终端执行(只是临时生效、立即生效,重启失效)
				# hostname	slave1
				# hostname
				slave1
			修改防火墙
				# /etc/init.d/iptables stop
			修改selinux
				# setenforce 0
				# getenforce
				Permissive //表示成功关闭
		6、设置远程登录不需要密码
			# ssh-keygen //一直回车
			# cd ~/.ssh/
			# cp id_rsa.pub authorized_keys
			复制slave公钥 id_rsa.pub里面的内容到master的autorized_keys
			所有的slave公钥复制完成后把master的autorized_keys复制到各个slave
			//不需要密码就是设置成功
			# ssh master 
			# exit //退出

		7、启动集群
			//master启动后
			# jps
			111 TaskTracker
			112 Jps
			113 DataNode
			如果有问题，把master和slaver的tmp文件夹内容删除，执行master第七步

			
			
################################################
################ HDFS
################################################
	 










################################################
################ Streaming
################################################
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
		本地模式:用于本地测试
			[root@djt002 ~]# cat input.txt | python Mapper.py | sort | python Reducer.py > output
		集群模式：
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










	