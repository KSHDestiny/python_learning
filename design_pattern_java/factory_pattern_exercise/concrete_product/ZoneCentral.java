package design_pattern_java.factory_pattern_exercise.concrete_product;

import design_pattern_java.factory_pattern_exercise.product.Zone;

public class ZoneCentral extends Zone {
	public ZoneCentral() {
		displayName = "US/Central";
		offset = -6;
	}
}