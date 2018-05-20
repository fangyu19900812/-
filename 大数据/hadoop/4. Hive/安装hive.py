
hive1.2版本只支持hbase 0.94及更低版本，hbase1.2.6需要hive 2.x才支持。


1、下载hive压缩包

2、在conf目录下，创建hive-site.xml配置文件或者hive-default.xml.template拷贝重命名：
<configuration>
	<property>
　　	<name>javax.jdo.option.ConnectionURL</name>
　　	<value>jdbc:mysql://master:3306/hive?createDatabaseIfNotExist=true</value>
	</property>
	<property>
	　　<name>javax.jdo.option.ConnectionDriverName</name>
	　　<value>com.mysql.jdbc.Driver</value>
	</property>
	<property>
	　　<name>javax.jdo.option.ConnectionUserName</name>
	　　<value>root</value>
	</property>
	<property>
	　　<name>javax.jdo.option.ConnectionPassword</name>
	　　<value>123456</value>
	</property>
</configuration>
	
3、下载mysql-connector-java压缩包
	https://downloads.mysql.com/archives/c-j/
	把解压的jar包放到hive的lib目录下
	
4、配置环境变量
	修改bashrc 
		vim ~/.bashrc 或者 vim /etc/profile 
			HIVE_HOME=XXXX
			PATH=$HIVE_HOME/bin
		source /etc/profile
5、运行
	hive
	会有RunJar进程连接hadoop
	hive在hadoop中的路径 /user/hive/warehouse（固定写法）
	然后mysql就会出现hive数据库
		
mysql要启动

Cannot find hadoop installation: $HADOOP_HOME or $HADOOP_PREFIX must be set or hadoop must be in the path
hadoop_home没有配置

Unable to instantiate org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClient
版本太高

FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.DDLTask. java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.metastore.HiveMetaStoreClient
查看日志，数据库连不上，把无密码修改为有密码就ok了



	