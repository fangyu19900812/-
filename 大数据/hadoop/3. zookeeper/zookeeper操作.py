

java端：
https://blog.csdn.net/catoop/article/details/50848555

persistent node:永久有效的节点 除非client删除
ephemeral node: 临时节点，仅在client保持连接期间有效。
sequence node: 顺序节点。client申请该节点是，zk会在节点末尾添加递增序号。
4种节点 p、e、ps、es

应用：配置分发、集群管理、选主(临时+顺序节点)、锁服务、同步队列、FIFO
 

5、进入bin目录，执行客户端，数据都是同步的
	./zkCli.sh
	create /test "123"  创建节点"123"是数据
	create -s /test "123" 创建顺序节点 会在test后面加上序号:test001 序号会一直往上加，即使删除了某个节点
	create -e /test "123" 创建临时节点
	get /test  获取节点数据及信息
	set /test "456" 修改节点数据
	ls /  当前目录节点
	rmr /test 删除节点,可以删路径
	delete /test 删除节点,？？只能删一个节点？？

	
	
监控：watch机制
	java - ZooKeeper中一共由三种方法可以实现监控机制(Watch)，分别为getData()、getChildren()和exists()
	getData()：监控数据是否更新。
	getChildren():监控子节点新增、删除，父节点会发出信息。子节点数据发生变化，父节点不发出信息
	exists()：节点是否存在。注意监控一个不存在的节点，然后创建，会发出信息。
	
	1、监控为一次性的，触发后，需要重新设置
	2、保证先收到事件，在收到数据修改的信息
	3、传递性
		1、create会触发节点数据监控点，同时也会触发父节点的监控点
		2、delete会触发节点数据监控点，同时也会触发父节点的监控点
	
权限：ACL机制 访问控制链
	create 	有创建子节点的权限
	read	有读取节点数据和子节点列表的权限
	write	有修改节点数据的权限，无创建和删除子节点的权限
	delete	有删除子节点的权限
	admin	有设置节点权限的权限
	 
	
	机制：
		world	它下面只有一个id,叫anyone,
				world:anyone表示任何人，zk中对所有人权限的节点就是属于world:anyone的
		auth	已经被认证的用户
		digest	通过username:password字符串的md5编码认证用户
		host	匹配主机后缀，host:xxx.com
				比如能匹配1.xxx.com、2.xxx.com,不能匹配1.yyy.com
		ip		通过ip识别用户，表达格式为 addr/bits
	
	例子：
		ip:192.168.0.0/16,READ 表示ip地址192.168开头的主机有该节点读的权限
	