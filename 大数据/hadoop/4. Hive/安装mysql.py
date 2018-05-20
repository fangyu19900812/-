

yum install mysql
yum install mysql-server

启动：
	/etc/init.d/mysqld start
	
	
设置用户名 密码
	mysqladmin -u root password '111111'
	#ERROR 1045 (28000):Access denied for user 'root'@'localhost' (using password:YES
		接下来就是用sql来修改root的密码
		mysql> use mysql;
		mysql> update user set password=password("你的新密码") where user="root";
		mysql> flush privileges;
		mysql> quit
		
	#/etc/my.cnf is ignored
		权限太大，改为644
	
	#ERROR 1045 (28000):Access denied for user 'root'@'localhost' (using password:NO
		查看密码 sudo cat /root/.mysql_secret (root就不用sodu)
		mysql -uroot -p 输入密码
	
	#如果控制台输入mysql不能进入就把密码置空
	
	
	
测试登录：
	mysql -uroot -p111111  注意密码要和p连着 root要和u连着
	
操作：
	从文件导入数据：
		load data local infile '文件地址' into table 表名;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	