package design_pattern_java.decorator_pattern.concrete_component;

import design_pattern_java.decorator_pattern.component.Beverage;

public class Decaf extends Beverage {
	public Decaf() {
		description = "Decaf Coffee";
	}
 
	public double cost() {
		return 1.05;
	}
}

