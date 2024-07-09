package design_pattern_java.decorator_pattern_exercise.decorator;

import design_pattern_java.decorator_pattern_exercise.component.Pizza;

public abstract class ToppingDecorator extends Pizza {
	protected Pizza pizza;
	public abstract String getDescription();
}
