package design_pattern_java.strategy_pattern.Duck;

import design_pattern_java.strategy_pattern.Fly.FlyNoWay;
import design_pattern_java.strategy_pattern.Quack.Quack;

public class ModelDuck extends Duck {
	public ModelDuck() {
		flyBehavior = new FlyNoWay();
		quackBehavior = new Quack();
	}

	public void display() {
		System.out.println("I'm a model duck");
	}
}
