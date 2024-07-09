package design_pattern_java.decorator_pattern_exercise.concrete_decorator;

import design_pattern_java.decorator_pattern_exercise.component.Pizza;
import design_pattern_java.decorator_pattern_exercise.decorator.ToppingDecorator;

public class Olives extends ToppingDecorator {
	
 
	public Olives(Pizza pizza) {
		this.pizza = pizza;
	}
 
	public String getDescription() {
		return pizza.getDescription() + ", Olives";
	}
 
	public double cost() {
		return pizza.cost() + .30; 
	}
}
