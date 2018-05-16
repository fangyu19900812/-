package com.hadoop.storm;

import java.util.Map;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

public class Bolt1 extends BaseRichBolt{
	 
	OutputCollector _collector;


	public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
		// TODO Auto-generated method stub
		_collector = collector;
		
	}

	public void execute(Tuple input) {
		// TODO Auto-generated method stub
		String sentence = input.getString(0);
		for (String word : sentence.split(" ")){
			//_collector.emit(new Values(word));
			_collector.emit(input, new Values(word));
			// TODO
//			outputCollector.ack(input);
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
		declarer.declare(new Fields("word"));
		
	}
}
