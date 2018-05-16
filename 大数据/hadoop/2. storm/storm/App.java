package com.hadoop.storm;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.AlreadyAliveException;
import org.apache.storm.generated.AuthorizationException;
import org.apache.storm.generated.InvalidTopologyException;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.tuple.Fields;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) 
    {
    	TopologyBuilder builder = new TopologyBuilder();
    	builder.setSpout("builder_Spout1", new Spout1(), 3);
    	builder.setBolt("builder_setBolt1", new Bolt1(), 5).shuffleGrouping("builder_Spout1","ss");
    	builder.setBolt("builder_setBolt2", new Bolt2(), 5).fieldsGrouping("builder_setBolt1", new Fields("word"));
    	
    	Config conf = new Config();
    	conf.setDebug(false);
       
    	if(args != null && args.length > 0){
    		 //集群模式
    		conf.setNumWorkers(3);
    		try {
				StormSubmitter.submitTopology("wordcount-online", conf, builder.createTopology());
			} catch (AlreadyAliveException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InvalidTopologyException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (AuthorizationException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	} else {
    		System.out.println("====================================================");
    		//本地模式
            LocalCluster localCluster = new LocalCluster();
            localCluster.submitTopology("wordcount-demo-123", conf, builder.createTopology());
            
    	}
    }
}
