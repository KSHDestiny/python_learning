package design_pattern_java.factory_pattern_exercise.client;

import design_pattern_java.factory_pattern_exercise.product.Zone;
import java.util.*;

public abstract class Calendar {
	private Zone zone;
	public void print() {
		System.out.println("--- " + zone.getDisplayName() + " Calendar ---");
		// print all appointments in correct time zone
		System.out.println("Offset from GMT: " + zone.getOffset());
	}
	public abstract void createCalendar(List<String> appointments);
}