package design_pattern_java.decorator_pattern;

import design_pattern_java.decorator_pattern.component.Beverage;
import design_pattern_java.decorator_pattern.concrete_component.DarkRoast;
import design_pattern_java.decorator_pattern.concrete_component.Espresso;
import design_pattern_java.decorator_pattern.concrete_component.HouseBlend;
import design_pattern_java.decorator_pattern.concrete_decorator.Mocha;
import design_pattern_java.decorator_pattern.concrete_decorator.Soy;
import design_pattern_java.decorator_pattern.concrete_decorator.Whip;

public class StarbuzzCoffee {
 
	public static void main(String args[]) {
		Beverage beverage = new Espresso();
		System.out.println(beverage.getDescription() 
				+ " $" + beverage.cost());
 
		Beverage beverage2 = new DarkRoast();
		beverage2 = new Mocha(beverage2);
		beverage2 = new Mocha(beverage2);
		beverage2 = new Whip(beverage2);
		System.out.println(beverage2.getDescription() 
				+ " $" + beverage2.cost());
 
		Beverage beverage3 = new HouseBlend();
		beverage3 = new Soy(beverage3);
		beverage3 = new Mocha(beverage3);
		beverage3 = new Whip(beverage3);
		System.out.println(beverage3.getDescription() 
				+ " $" + beverage3.cost());
	}
}
