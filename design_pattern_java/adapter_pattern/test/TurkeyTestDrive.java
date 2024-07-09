package design_pattern_java.adapter_pattern.test;

import design_pattern_java.adapter_pattern.MallardDuck;
import design_pattern_java.adapter_pattern.adapter.DuckAdapter;
import design_pattern_java.adapter_pattern.adapter.Turkey;

public class TurkeyTestDrive {
	public static void main(String[] args) {
		MallardDuck duck = new MallardDuck();
		Turkey duckAdapter = new DuckAdapter(duck);
 
		for(int i=0;i<10;i++) {
			System.out.println("The DuckAdapter says...");
			duckAdapter.gobble();
			duckAdapter.fly();
		}
	}
}
