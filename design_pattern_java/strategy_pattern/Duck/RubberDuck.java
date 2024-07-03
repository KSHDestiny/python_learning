package design_pattern_java.strategy_pattern.Duck;

import design_pattern_java.strategy_pattern.Fly.FlyBehavior;
import design_pattern_java.strategy_pattern.Fly.FlyNoWay;
import design_pattern_java.strategy_pattern.Quack.QuackBehavior;

public class RubberDuck extends Duck {
 
	public RubberDuck() {
		flyBehavior = new FlyNoWay();
		//quackBehavior = new Squeak();
		quackBehavior = () -> System.out.println("Squeak");
	}
	
	public RubberDuck(FlyBehavior flyBehavior, QuackBehavior quackBehavior) {
		this.flyBehavior = flyBehavior;
		this.quackBehavior = quackBehavior; 
	}
 
	public void display() {
		System.out.println("I'm a rubber duckie");
	}
}
