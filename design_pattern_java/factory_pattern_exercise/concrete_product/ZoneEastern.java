package design_pattern_java.factory_pattern_exercise.concrete_product;

import design_pattern_java.factory_pattern_exercise.product.Zone;

public class ZoneEastern extends Zone {
	public ZoneEastern() {
		displayName = "US/Eastern";
		offset = -5;
	}
}