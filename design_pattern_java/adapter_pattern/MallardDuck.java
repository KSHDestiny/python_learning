package design_pattern_java.adapter_pattern;

import design_pattern_java.adapter_pattern.original_interface.Duck;

public class MallardDuck implements Duck {
	public void quack() {
		System.out.println("Quack");
	}
 
	public void fly() {
		System.out.println("I'm flying");
	}
}
