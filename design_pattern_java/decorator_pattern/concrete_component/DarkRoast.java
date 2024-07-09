package design_pattern_java.decorator_pattern.concrete_component;

import design_pattern_java.decorator_pattern.component.Beverage;

public class DarkRoast extends Beverage {
	public DarkRoast() {
		description = "Dark Roast Coffee";
	}
 
	public double cost() {
		return .99;
	}
}

