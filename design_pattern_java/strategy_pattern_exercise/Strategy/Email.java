package design_pattern_java.strategy_pattern_exercise.Strategy;

public class Email implements ShareStrategy {
	public void share() {
		System.out.println("I'm emailing the photo");
	}
}
