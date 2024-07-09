package design_pattern_java.factory_pattern_exercise.concrete_product;

import design_pattern_java.factory_pattern_exercise.product.Zone;

public class ZonePacific extends Zone {
	public ZonePacific() {
		displayName = "US/Pacific";
		offset = -8;
	}
}