package design_pattern_java.strategy_pattern.Duck;

import design_pattern_java.strategy_pattern.Fly.FlyWithWings;
import design_pattern_java.strategy_pattern.Quack.Quack;

public class MallardDuck extends Duck {

	public MallardDuck() {

		quackBehavior = new Quack();
		flyBehavior = new FlyWithWings();

	}

	public void display() {
		System.out.println("I'm a real Mallard duck");
	}
}
