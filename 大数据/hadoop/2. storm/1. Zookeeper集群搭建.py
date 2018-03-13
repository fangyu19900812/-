
版本：zookeeper-3.4.5

1、解压zookeeper-3.4.5.tar.gz

2、在解压文件夹下创建myid, 内容填写0，每个节点都要不一样。

3、进入conf文件夹，若没有zoo.cfg则创建zoo.cfg
	vim zoo.cfg
		tickTime=2000
		iniLimit=10
		syncLimit=5
		dataDir=/usr/local/src/zookeeper-3.4.5  数据存放目录,必须创建 
		clientPort=2181
		
		server.0=master:8880:7770
		server.1=slave1:8881:7771
		server.2=slave2:8882:7772
		
4、进入bin目录
	./zkServer.sh start  启动，jps会看到QuorumPeerMain进程 
	./zkServer.sh status  查看主从，leader主，follow从，如果没有显示就是启动不成功 
		

persistent node:永久有效的节点 除非client删除

ephemeral node: 临时节点，仅在client保持连接期间有效。

sequence node: 顺序节点。client申请该节点是，zk会在节点末尾添加递增序号。

4种节点 p、e、ps、es








