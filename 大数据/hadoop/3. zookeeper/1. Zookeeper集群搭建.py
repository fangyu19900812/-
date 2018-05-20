
版本：zookeeper-3.4.5

https://blog.csdn.net/beitiandijun/article/details/41802835
1、解压zookeeper-3.4.5.tar.gz

2、在解压文件夹下创建data目录、创建myid文件, 内容填写0，每个节点都要不一样。

3、进入conf文件夹，若没有zoo.cfg则创建zoo.cfg 或者把zoo_simple.cfg改个名
	vim zoo.cfg
		tickTime=2000 zookeeper中使用的基本时间单位, 毫秒值。 
		iniLimit=10 这个配置项是用来配置 Zookeeper 接受客户端（这里所说的客户端不是用户连接 Zookeeper 服务器的客户端，而是 Zookeeper 服务器集群中连接到 Leader 的 Follower 服务器）初始化连接时最长能忍受多少个 tickTime 时间间隔数。这里设置为5表名最长容忍时间为 5 * 2000 = 10 秒
		syncLimit=5 这个配置标识 Leader 与 Follower 之间发送消息，请求和应答时间长度，最长不能超过多少个 tickTime 的时间长度，总的时间长度就是 2 * 2000 = 4 秒。 
		dataDir=/usr/local/src/zookeeper-3.4.5  数据存放目录,必须创建 
		dataLogDir = xxx 日志存放目录
		clientPort=2181 监听client连接的端口号，这里说的client就是连接到Zookeeper的代码程序。 
		
		server.0=master:8880:7770  server.{myid}={ip}:{leader服务器交换信息的端口}:{当leader服务器挂了后, 选举leader的端口} 
		server.1=slave1:8881:7771
		server.2=slave2:8882:7772
		
		maxClientCnxns：对于一个客户端的连接数限制，默认是60，这在大部分时候是足够了。但是在我们实际使用中发现，在测试环境经常超过这个数，经过调查发现有的团队将几十个应用全部部署到一台机器上，以方便测试，于是这个数字就超过了。
		
		
4、进入bin目录
		每个节点都要启动！！！
	./zkServer.sh start  启动，jps会看到QuorumPeerMain进程 如果是HQuorumPeer就是HBase启动的zk
	./zkServer.sh status  查看主从，leader主，follow从，如果没有显示就是启动不成功 
	./zkServer.sh stop 停止








