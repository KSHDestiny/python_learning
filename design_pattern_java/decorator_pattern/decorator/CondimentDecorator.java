package design_pattern_java.decorator_pattern.decorator;

import design_pattern_java.decorator_pattern.component.Beverage;

public abstract class CondimentDecorator extends Beverage {
	public abstract String getDescription();
}
