package design_pattern_java.decorator_pattern.concrete_decorator;

import design_pattern_java.decorator_pattern.component.Beverage;
import design_pattern_java.decorator_pattern.decorator.CondimentDecorator;

public class Soy extends CondimentDecorator {
	Beverage beverage;

	public Soy(Beverage beverage) {
		this.beverage = beverage;
	}

	public String getDescription() {
		return beverage.getDescription() + ", Soy";
	}

	public double cost() {
		return .15 + beverage.cost();
	}
}
