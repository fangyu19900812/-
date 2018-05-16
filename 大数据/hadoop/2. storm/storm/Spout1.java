package com.hadoop.storm;

import java.util.Map;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;

import java.util.Random;


public class Spout1 extends BaseRichSpout{
	
	SpoutOutputCollector _collector;

	public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
		// TODO Auto-generated method stub
		 _collector = collector;
		
	}

	public void nextTuple() {
		// TODO Auto-generated method stub
		final String[] words = new String[] {"how do you do", "you do what", "do you kown"};
		Random rand = new Random();
		String word = words[rand.nextInt(words.length)];
		
		Object msgid = "1"; 
		_collector.emit("ss",new Values(word), msgid);
		try {
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		// TODO Auto-generated method stub
		declarer.declareStream("ss",new Fields("word"));
		//declarer.declare(new Fields("word"));
	}

	@Override
	public void close() {
		// TODO Auto-generated method stub
		super.close();
	}

	@Override
	public void activate() {
		// TODO Auto-generated method stub
		super.activate();
	}

	@Override
	public void deactivate() {
		// TODO Auto-generated method stub
		super.deactivate();
	}

	@Override
	public void ack(Object msgId) {
		// TODO Auto-generated method stub
		//super.ack(msgId);
		System.out.println("Recive ACK!!!");
	}

	@Override
	public void fail(Object msgId) {
		// TODO Auto-generated method stub
		super.fail(msgId);
	}
}
