package design_pattern_java.factory_pattern.factory;

import design_pattern_java.factory_pattern.client.PizzaStore;
import design_pattern_java.factory_pattern.concrete_product.*;
import design_pattern_java.factory_pattern.product.Pizza;

public class NYPizzaStore extends PizzaStore {

	Pizza createPizza(String item) {
		if (item.equals("cheese")) {
			return new NYStyleCheesePizza();
		} else if (item.equals("veggie")) {
			return new NYStyleVeggiePizza();
		} else if (item.equals("clam")) {
			return new NYStyleClamPizza();
		} else if (item.equals("pepperoni")) {
			return new NYStylePepperoniPizza();
		} else return null;
	}
}
