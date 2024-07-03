package design_pattern_java.strategy_pattern.Duck;

import design_pattern_java.strategy_pattern.Fly.FlyNoWay;
import design_pattern_java.strategy_pattern.Quack.MuteQuack;

public class DecoyDuck extends Duck {
	public DecoyDuck() {
		setFlyBehavior(new FlyNoWay());
		setQuackBehavior(new MuteQuack());
	}
	public void display() {
		System.out.println("I'm a duck Decoy");
	}
}
