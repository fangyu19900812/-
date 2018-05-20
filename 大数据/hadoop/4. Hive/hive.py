
https://blog.csdn.net/haohaixingyun/article/details/52819588

Hive的基础也是MR
Hive基于一个统一的查询分析层，通过SQL语句的方式对HDFS上的数据进行查询、统计和分析
Hive本身不存储数据，完全依赖HDFS(存储)和MapReaduce(计算)
Hive的内容是读多写少，不支持对数据的改写和删除

Hive需要指定三个属性：
	列分隔符
	行分隔符
	读取文件数据的方法
	
元数据一般存储在Derby,也支持存储在Mysql

优化：
	partition
	bucket: sort by
	
	set hive.enforce.bucketing = true 控制上一轮reduce的数量从而配置bucket个数也可以设置mapred.reduce.tasks配置bucket个数
	
	抽样：
		select * from t tablesample(bucket 1 out of 2 on id);
		tablesample(bucket x out of y)
		如 tablesample(bucket 3 out of 16)，总数32，表示抽取32/16个样例，从第3 bucket开始和第3+16 bucket
		
		
		
创建表：
	create table	创建内部表，删除时数据会删除
	create external table	创建外部表，删除时数据不会删除(常用)
	
linux:	
	创建表：
		#hive -f file.sql 会在hadoop创建/user/hive/warehouse目录
		
	从本地文件导入数据：
		hive> load data local inpath '文件地址' overwrite into table 表名;
	或	# hive -e load data local inpath '文件地址' overwrite into table 表名;
		overwrite会覆盖原来的内容
	从HDFS导入数据：（不要local）
		hive> load data inpath '文件地址' overwrite into table 表名;
	join:
		hive> select a.*, b.* from w_a a join w_b b on a.userid=b.userid; 会启动MR
		hive> select usrid from w_a; 会启动MR
		
	UDF(用户自定义函数)：
		hive> add jar xxx.jar; (java写的udf,继承org.apachehadoop.hive.ql.exec.UDF)
		hive> create temporary function uppercase666 as 'jar里的类'; 定义函数
		hive> select id, age, uppercase666(addr) from w_a; 使用函数
		
	利用insert导入数据：
		insert into table 表名1 select col1,col2 from 表名2;
	
	通过查询插入(表1不存在时)：
		create table 表名1 as select * from 表名2;
	
	导出数据(导为本地文件,默认分隔符ctrl+A不是\t，不加local是导入hdfs)
		insert overwrite local directory 'xxx/xxxx/xx.txt' select id,age from 表名;
	
	partition:
		导入sql的时候partition 用于节省时间，不会调用MR
		
	transform:
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		