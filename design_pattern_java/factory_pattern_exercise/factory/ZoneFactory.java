package design_pattern_java.factory_pattern_exercise.factory;

import design_pattern_java.factory_pattern_exercise.concrete_product.*;
import design_pattern_java.factory_pattern_exercise.product.Zone;

public class ZoneFactory {
	public Zone createZone(String zoneId) {
		Zone zone = null;
		if (zoneId == "US/Pacific") {
			zone = new ZonePacific();
		}
		else if (zoneId == "US/Mountain") {
			zone = new ZoneMountain();
		}
		else if (zoneId == "US/Central") {
			zone = new ZoneCentral();
		}
		else if (zoneId == "US/Eastern") {
			zone = new ZoneEastern();
		}
		return zone;
	}
}