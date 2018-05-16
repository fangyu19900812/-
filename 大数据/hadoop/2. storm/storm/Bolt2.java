package com.hadoop.storm;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

public class Bolt2 extends BaseRichBolt{
	
	OutputCollector _collector;
	public Map<String , Integer> countMap = new HashMap<String ,Integer>();

	public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
		// TODO Auto-generated method stub
		_collector = collector;
		
	}

	public void execute(Tuple input) {
		// TODO Auto-generated method stub
		String word = input.getString(0);
		Integer count = this.countMap.get(word);
		if (null == count)
		{
			count = 0;
		}
		count++;
		this.countMap.put(word, count);
 
		Iterator<String> iter = this.countMap.keySet().iterator();
		while(iter.hasNext())
		{
			String next = iter.next();
			System.out.println(next + ":" + this.countMap.get(next));
		} 
		_collector.ack(input);
		
	}

	@Override
	public void cleanup() {
		// TODO Auto-generated method stub
		super.cleanup();
	}

	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		// TODO Auto-generated method stub
	}
}
