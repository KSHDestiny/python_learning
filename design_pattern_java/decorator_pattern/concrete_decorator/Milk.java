package design_pattern_java.decorator_pattern.concrete_decorator;

import design_pattern_java.decorator_pattern.component.Beverage;
import design_pattern_java.decorator_pattern.decorator.CondimentDecorator;

public class Milk extends CondimentDecorator {
	Beverage beverage;

	public Milk(Beverage beverage) {
		this.beverage = beverage;
	}

	public String getDescription() {
		return beverage.getDescription() + ", Milk";
	}

	public double cost() {
		return .10 + beverage.cost();
	}
}
