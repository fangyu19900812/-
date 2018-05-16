
版本：zookeeper-3.4.5

persistent node:永久有效的节点 除非client删除
ephemeral node: 临时节点，仅在client保持连接期间有效。
sequence node: 顺序节点。client申请该节点是，zk会在节点末尾添加递增序号。
4种节点 p、e、ps、es

1、解压zookeeper-3.4.5.tar.gz

2、在解压文件夹下创建myid, 内容填写0，每个节点都要不一样。

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
		

5、进入bin目录，执行客户端，数据都是同步的
	./zkCli.sh
	create /test "123"  创建节点"123"是数据
	get /test  获取节点数据及信息
	set /test "456" 修改节点数据
	ls /  当前目录节点
	create -s /test "123" 创建顺序节点 会在test后面加上序号:test001 序号会一直往上加，即使删除了某个节点
	create -e /test "123" 创建临时节点
	rmr /test 删除节点,可以删路径
	delete /test 删除节点,？？只能删一个节点？？

	https://blog.csdn.net/catoop/article/details/50848555
	java - ZooKeeper中一共由三种方法可以实现Watch，分别为getData、exists和getChildren







