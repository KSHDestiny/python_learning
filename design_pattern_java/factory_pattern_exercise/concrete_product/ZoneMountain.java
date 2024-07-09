package design_pattern_java.factory_pattern_exercise.concrete_product;

import design_pattern_java.factory_pattern_exercise.product.Zone;

public class ZoneMountain extends Zone {
	public ZoneMountain() {
		displayName = "US/Mountain";
		offset = -7;
	}
}