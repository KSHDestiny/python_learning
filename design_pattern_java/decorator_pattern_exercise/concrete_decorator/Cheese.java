package design_pattern_java.decorator_pattern_exercise.concrete_decorator;

import design_pattern_java.decorator_pattern_exercise.component.Pizza;
import design_pattern_java.decorator_pattern_exercise.decorator.ToppingDecorator;

public class Cheese extends ToppingDecorator {
	public Cheese(Pizza pizza) {
		this.pizza = pizza;
	}
 
	public String getDescription() {
		return pizza.getDescription() + ", Cheese";
	}
 
	public double cost() {
		return pizza.cost(); // cheese is free
	}
}
