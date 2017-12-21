
hadoop1.0
################################################
################ hadoop1.0��Ⱥ�
################################################
	master:
		1��·�� usr/local/src/
		2����ѹ hadoop
		3������ hadoop��ѹ����ļ��� ����tmp�ļ��У������ʱ�ļ�
		4������ usr/local/src/hadoop-1.2.1/confĿ¼
			�޸�masters 
				��localhostȥ������master
			�޸�slaves
				��localhostȥ������slave1����slave2�����ж��ٸ�slave�ͼӶ��ٸ�
			�޸�core-site.xml
				<configuration>
				//��ʱ�ļ�
					<property>
						<name>hadoop.tmp.dir</name>
						<value>/usr/local/src/hadoop-1.2.1/tmp</value>
					</property>
				//namenode ip��ַmaster ip��ַ
					<property>
						<name>fs.default.name</name>
						<value>hdfs://192.168.183.10:9000</value> 
					</property>
				</configuration>
			�޸�mapred-site.xml
				<configuration>
				//jobTracker Ҫhttp��ͷ
					<property>
						<name>mapred.job.tracker</name>
						<value>http://192.168.183.10:9001</value>
					</property>
				</configuration>
			�޸�hdfs-site.xml
				<configuration>
				//����hdfs������ Ĭ��3
					<property>
						<name>dfs.replication</name>
						<value>3</value>
					</property>
				</configuration>
			�޸�hadoop-env.sh
				//jdkĿ¼ http://www.cnblogs.com/kerrycode/archive/2015/08/27/4762921.html
				// http://blog.csdn.net/cx118118/article/details/54955620
				export JAVA_HOME= /usr/local/src/jdkxxx
		ǰ4����slaveһ��������������slave��Ȼ����ִ�����沽�衣
		5������ /etcĿ¼		
			�޸�hosts //����hostname�����ʿ�����hostname����ip
				192.168.183.10 master
				192.168.183.11 slave1
				192.168.183.12 slave2
			�޸�/etc/sysconfig/network(������Ч)
				HOSTNAME=localhost�ĳ�HOSTNAME=master
			�ն�ִ��(ֻ����ʱ��Ч��������Ч,����ʧЧ)
				# hostname	master
				# hostname
				master
				
		ע�⣺ÿ����������Ҫ�رգ�Ҳ�����������ùرա���
			�رշ���ǽ
				# /etc/init.d/iptables stop ��Ҳ����ֻ��Ҫ���õĶ˿ڣ�
				[root@djt002 ~]# service iptables stop     //��ʱ�رշ���ǽ
				[root@djt002 ~]# service iptables status //�鿴����ǽ״̬
				iptables: Firewall is not running.
					
			���ùرշ���ǽ
				[root@djt002 ~]# chkconfig iptables off //���ùرշ���ǽ 
				[root@djt002 ~]# chkconfig iptables on //���ô򿪷���ǽ
				
			�ر�selinux
				# setenforce 0
				# getenforce
				Permissive //��ʾ�ɹ��ر�
				
			���ùر�selinux
				# vim /etc/selinux/config
					  #SELINUX=enforcing //ע��
					  #SELINUXTYPE=targeted //ע��
					  SELINUX=disable //����
		6������������Զ�̵�¼ssh û�е���Ҫ��װ
			# ssh-keygen  //һֱ�س�
			# cd ~/.ssh/
			# cp id_rsa.pub authorized_keys
			����slave��Կ id_rsa.pub��������ݵ�master��autorized_keys
			���е�slave��Կ������ɺ��master��autorized_keys���Ƶ�����slave
			# scp -rp authorized_keys slave1:~/.ssh/   //scp -rp authorized_keys 192.168.183.11:~/.ssh/
			//����Ҫ����������óɹ�
			# ssh slave1 
			# exit //�˳�
			//����masters: ssh: Could not resolve hostname masters: Name or service not known
			��/usr/local/src/hadoop-1.2.1/conf�����mastersɾ�����´���һ�� �����slave�����ɾ���ؽ�slaves
		7��������Ⱥ
			���� usr/local/src/hadoop-1.2.1/binĿ¼
			//��һ��������Ҫ��ʽ��
			# ./hadoop namenode -format
			# ./start-all.sh
			# jps
			111 NameNode
			112 SecondaryNameNode
			113 Jps
			114 JobTracker
			//�����Ƿ���ִ�гɹ�
			# ./hadoop fs -ls /
	slave:
		1-4 ��masterһ�� ��master��hadoop���Ƶ�slave �Ͳ����ظ�ִ�� 
		�ն�ִ�� scp -rp hadoop-1.2.1 192.168.183.11:/usr/local/src/
		//slaveû������hostnameֻ����ip �������scp -rp hadoop-1.2.1 slave1:/usr/local/src/

		5������ /etcĿ¼		
			�޸�hosts //����hostname�����ʿ�����hostname����ip
				192.168.183.10 master
				192.168.183.11 slave1
				192.168.183.12 slave2
			�޸�/etc/sysconfig/network(������Ч��������Ч��)
				HOSTNAME=localhost�ĳ�HOSTNAME=slave1
			�ն�ִ��(ֻ����ʱ��Ч��������Ч,����ʧЧ)
				# hostname	slave1
				# hostname
				slave1
			�޸ķ���ǽ
				# /etc/init.d/iptables stop
			�޸�selinux
				# setenforce 0
				# getenforce
				Permissive //��ʾ�ɹ��ر�
		6������Զ�̵�¼����Ҫ����
			# ssh-keygen //һֱ�س�
			# cd ~/.ssh/
			# cp id_rsa.pub authorized_keys
			����slave��Կ id_rsa.pub��������ݵ�master��autorized_keys
			���е�slave��Կ������ɺ��master��autorized_keys���Ƶ�����slave
			//����Ҫ����������óɹ�
			# ssh master 
			# exit //�˳�

		7��������Ⱥ
			//master������
			# jps
			111 TaskTracker
			112 Jps
			113 DataNode
			��������⣬��master��slaver��tmp�ļ�������ɾ����ִ��master���߲�

			
			
################################################
################ HDFS
################################################
	 










################################################
################ Streaming
################################################
	Hadoop Streaming��
		��Hadoop�ṩ��һ����̹��ߣ��������û�ʹ���κο�ִ���ļ����߽ű��ļ���ΪMapper��Reducer��Hadoop�ṩ��һ����̹��ߣ��������û�ʹ���κο�ִ���ļ����߽ű��ļ���ΪMapper��Reducer
		cat input.txt | python Mapper.py | sort | python Reducer.py > output

	ԭ��
		mapper��reducer��ӱ�׼�����ж�ȡ�û����ݣ�һ��һ�д�����͸���׼�����Streaming���߻ᴴ��MapReduce��ҵ�����͸�����tasktracker��ͬʱ���������ҵ��ִ�й��̡�
		���һ���ļ�����ִ�л��߽ű�����Ϊmapper��mapper��ʼ��ʱ��ÿһ��mapper�����Ѹ��ļ���Ϊһ����������������mapper��������ʱ�����������зֳ��в���ÿһ���ṩ����ִ���ļ����̵ı�׼���롣 ͬʱ��mapper�ռ���ִ���ļ����̱�׼��������ݣ������յ���ÿһ������ת����key/value�ԣ���Ϊmapper������� Ĭ������£�һ���е�һ��tab֮ǰ�Ĳ�����Ϊkey��֮��ģ�������tab����Ϊvalue�����û��tab��������Ϊkeyֵ��valueֵΪnull��
		����reducer�����ơ�
		������Map/Reduce��ܺ�streaming mapper/reducer֮��Ļ���ͨ��Э�顣
	���ޣ�
		1��streamingĬ��ֻ�ܴ����ı����ݣ������Զ��������ݽ��д������ԶԶ����Ƶ�key��value����base64����ת���ı���
		2���������ݿ����ͽ������ָ��Ӱ��ʱЧ�ԡ�
	
	�򵥰�����
		����ģʽ:���ڱ��ز���
			[root@djt002 ~]# cat input.txt | python Mapper.py | sort | python Reducer.py > output
		��Ⱥģʽ��
			run.sh:
				# stream��ַ
				STREAM_PATH ="/usr/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar"
				
				#��Ҫ������ļ���/��ʾ��hdfs��Ŀ¼��
				INPUT_FILE_PATH = "/file1.txt"
				#�������ļ�����Ŀ¼
				OUTPUT_PATH ="/output"
				#��������Ŀ¼�Ѿ����ھ�ɾ��������ᱨ��
				/usr/hadoop-1.2.1/bin/hadoop fs -rmr $SOUTPUT_PATH
				
				#��ʼִ��
				/usr/hadoop-1.2.1/bin/hadoop jar $STREAM_PATH
					-input $INPUT_FILE_PATH \
					-output $OUTPUT_PATH \
					-mapper "python map.py" \
					-reduce "python red.py" \
					-jobconf "mapred.reduce.tasks=2" \
					-file ./map.py \
					-file ./red.py










	