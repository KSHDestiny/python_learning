package design_pattern_java.decorator_pattern_exercise;

import design_pattern_java.decorator_pattern_exercise.component.Pizza;
import design_pattern_java.decorator_pattern_exercise.concrete_component.ThincrustPizza;
import design_pattern_java.decorator_pattern_exercise.concrete_decorator.Cheese;
import design_pattern_java.decorator_pattern_exercise.concrete_decorator.Olives;

public class PizzaStore {
 
	public static void main(String args[]) {
		Pizza pizza = new ThincrustPizza();
		Pizza cheesePizza = new Cheese(pizza);
		Pizza greekPizza = new Olives(cheesePizza);

		System.out.println(greekPizza.getDescription() 
				+ " $" + greekPizza.cost());

	}
}
