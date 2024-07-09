package design_pattern_java.decorator_pattern.concrete_component;

import design_pattern_java.decorator_pattern.component.Beverage;

public class HouseBlend extends Beverage {
	public HouseBlend() {
		description = "House Blend Coffee";
	}
 
	public double cost() {
		return .89;
	}
}

