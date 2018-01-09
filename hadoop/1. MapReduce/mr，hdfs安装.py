
创建linux用户mster centos6.5

[master@master ~] [用户@主机名 当前目录]
移动文件到/usr/local/src提示没有权限，输入root密码提示不在名单
1、切换到root
	[master@master ~]$ su root
	输入密码
2、查看/etc/sudoers文件权限，如果只读权限，修改为可写权限
	[root@master master]# ls -l /etc/sudoers
	-r--r-----. 1 root root 4002 3月   2 2012 /etc/sudoers
	[root@master master]# chmod 777 /etc/sudoers
	[root@master master]# ls -l /etc/sudoers
	-rwxrwxrwx. 1 root root 4002 3月   2 2012 /etc/sudoers
3、执行vi命令，编辑/etc/sudoers文件，添加要提升权限的用户；在文件中找到root  ALL=(ALL) ALL，要往下拉才能找到，在该行下添加提升权限的用户信息，如：
	root      ALL=(ALL)       ALL
	master    ALL=(ALL)       ALL
	说明：格式为（用户名    网络中的主机=（执行命令的目标用户）    执行的命令范围）
4、保存退出，并恢复/etc/sudoers的访问权限为440
	[root@master master]# chmod 440 /etc/sudoers
	[root@master master]# ls -l /etc/sudoers
	-r--r-----. 1 root root 4030 9月  25 00:57 /etc/sudoers
5、切换到普通用户，测试用户权限提升功能	
	[root@master master]$ su master
	[root@master master]$ sudo mv hadoop/ /usr/local/src/
	
master:
		1、路径 usr/local/src/
		2、解压 hadoop （多用户格式 用户名@主机名 如masters@local)
		3、进入 hadoop解压后的文件夹 创建tmp文件夹，存放临时文件
		4、进入 usr/local/src/hadoop-1.2.1/conf目录
		
			修改masters （多用户格式 用户名@主机名 如masters@local 当前用户的就不用加@主机名，比如用户是master就不用。 slave1就写master@主机名)
				[master@master conf]$ vim master
				把localhost去掉加上master
				
			修改slaves （多用户格式 用户名@主机名 如slave1@local 当前用户的就不用加@主机名，比如用户是slave1 就不用写slave@主机名。 slave2就写slave1@主机名)
				[master@master conf]$ vim slaves
				把localhost去掉加上slave1换行slave2……有多少个slave就加多少个
				
			修改core-site.xml
				<configuration>
				//临时文件
					<property>
						<name>hadoop.tmp.dir</name>
						<value>/usr/local/src/hadoop-1.2.1/tmp</value> //在此目录slave会被创建dfs和marped两个文件夹,master只有dfs
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
		5、进入 /etc目录 需要root权限
			cd /etc
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
			关闭防火墙（也可以只打开要试用的端口） 需要root权限
				方法1、[root@djt002 ~]# /etc/init.d/iptables stop  //临时关闭防火墙
				方法2、[root@djt002 ~]# service iptables stop     //临时关闭防火墙
				[root@djt002 ~]# service iptables status //查看防火墙状态 
				iptables: Firewall is not running.
				

					
			永久关闭防火墙
				chkconfig查看系统自动启动的进程服务
				[root@djt002 ~]# chkconfig
				[root@djt002 ~]# chkconfig iptables off //永久关闭防火墙，下次登录生效 （设置自动启动为关闭）
				[root@djt002 ~]# chkconfig iptables on //永久打开防火墙，下次登录生效
				[root@djt002 ~]# chkconfig --del iptables （移除开机自动启动），下次登录生效
				[root@djt002 ~]#chkconfig --add iptables（增加开启自启动），下次登录生效
				
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
			//注意当前的用户是谁不要弄错了。Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
											lost connection

			# ssh-keygen  //一直回车
			# cd ~/.ssh/
			# cp id_rsa.pub authorized_keys
			复制slave公钥 id_rsa.pub里面的内容到master的autorized_keys
			所有的slave公钥复制完成后把master的autorized_keys复制到各个slave
			# scp -rp authorized_keys slave1:~/.ssh/   //scp -rp authorized_keys 192.168.183.11:~/.ssh/
			多用户  # scp -rp authorized_keys 用户@主机:~/.ssh/    //scp -rp authorized_keys slave@192.168.183.11:~/.ssh/
			//不需要密码就是设置成功
			# ssh slave1   多用户 #ssh 用户@主机 还有就是注意用户名是否规范
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
			//master启动后 slave自动启动
			# jps
			111 TaskTracker
			112 Jps
			113 DataNode
			如果有问题，把master和slaver的tmp文件夹内容删除，执行master第七步
	
	