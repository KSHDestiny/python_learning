package design_pattern_java.decorator_pattern.concrete_component;

import design_pattern_java.decorator_pattern.component.Beverage;

public class Espresso extends Beverage {
  
	public Espresso() {
		description = "Espresso";
	}
  
	public double cost() {
		return 1.99;
	}
}

