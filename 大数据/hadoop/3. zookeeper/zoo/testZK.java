package com.hadoop.zookeeper; 

import java.io.IOException;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.ZooKeeper;

public class testZK implements Watcher {
	public ZooKeeper zk = null;
	boolean bk = true;

	public void CreateConnection(String connectString, int timeout) {
		try {
			zk = new ZooKeeper(connectString, timeout, null);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void releaseConnection() {
		try {
			this.zk.close();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void createPath(String path, String data) {
		try {
//			this.zk.create(path, data.getBytes(), Ids.OPEN_ACL_UNSAFE,
//					CreateMode.EPHEMERAL);
			this.zk.create(path, data.getBytes(), Ids.OPEN_ACL_UNSAFE,
					CreateMode.PERSISTENT);
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public String readData(String path) {
		String ret = null;
		try {
			ret = new String(this.zk.getData(path, false, null));
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return ret;
	}

	public void writeData(String path, String data) {
		try {
			this.zk.setData(path, data.getBytes(), -1);
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void deleteNode(String path) {
		try {
			this.zk.delete(path, -1);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void isExist(String path) {
		try {
			this.zk.exists(path, this);
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void getChildren(String path) {
		try {
			this.zk.getChildren(path, this);
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void getData(String path) {
		try {
			this.zk.getData(path, this, null);
		} catch (KeeperException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String zkpath = "/testzk";
		testZK test = new testZK();
		test.CreateConnection("192.168.146.136:2181", 100000);
//		test.createPath(zkpath, "123");
//
//		String ret = test.readData(zkpath);
//		System.out.println("get data :" + ret);
//				
//		test.writeData(zkpath, "321");
//
//		ret = test.readData(zkpath);
//		System.out.println("get data :" + ret);

//		test.createPath("/test2", "123");
		test.getData("/test2");
		test.getChildren("/test2");
		test.isExist("/test2/node1");
		
//		test.createPath("/test2/test3", "123");

		while (test.bk) {
			System.out.print(".");
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		try {
			Thread.sleep(10);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		test.releaseConnection();
	}

	public void process(WatchedEvent arg0) {
		// TODO Auto-generated method stub
		System.out.println("get event" + arg0.getState() + " # "+ arg0.getType() + "\n");
		this.bk = false;
	}

}
