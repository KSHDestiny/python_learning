package design_pattern_java.decorator_pattern.concrete_decorator;

import design_pattern_java.decorator_pattern.component.Beverage;
import design_pattern_java.decorator_pattern.decorator.CondimentDecorator;

public class Mocha extends CondimentDecorator {
	Beverage beverage;
 
	public Mocha(Beverage beverage) {
		this.beverage = beverage;
	}
 
	public String getDescription() {
		return beverage.getDescription() + ", Mocha";
	}
 
	public double cost() {
		return .20 + beverage.cost();
	}
}
