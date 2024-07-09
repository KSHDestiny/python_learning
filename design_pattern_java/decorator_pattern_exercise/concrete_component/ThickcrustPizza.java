package design_pattern_java.decorator_pattern_exercise.concrete_component;

import design_pattern_java.decorator_pattern_exercise.component.Pizza;

public class ThickcrustPizza extends Pizza {
  
	public ThickcrustPizza() {
		description = "Thick crust pizza, with tomato sauce";
	}
  
	public double cost() {
		return 7.99;
	}
}

