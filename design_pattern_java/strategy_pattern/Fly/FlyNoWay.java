package design_pattern_java.strategy_pattern.Fly;

public class FlyNoWay implements FlyBehavior {
	public void fly() {
		System.out.println("I can't fly");
	}
}
