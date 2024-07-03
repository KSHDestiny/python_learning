package design_pattern_java.strategy_pattern.Quack;

public class Squeak implements QuackBehavior {
	public void quack() {
		System.out.println("Squeak");
	}
}
