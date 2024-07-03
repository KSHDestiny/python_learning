package design_pattern_java.strategy_pattern.Duck;

import design_pattern_java.strategy_pattern.Fly.FlyWithWings;
import design_pattern_java.strategy_pattern.Quack.Quack;

public class RedHeadDuck extends Duck {
 
	public RedHeadDuck() {
		flyBehavior = new FlyWithWings();
		quackBehavior = new Quack();
	}
 
	public void display() {
		System.out.println("I'm a real Red Headed duck");
	}
}