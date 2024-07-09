package design_pattern_java.factory_pattern_exercise.concrete_client;

import design_pattern_java.factory_pattern_exercise.factory.ZoneFactory;
import java.util.*;


public class PacificCalendar extends Calendar {
	public PacificCalendar(ZoneFactory zoneFactory) {
		zoneFactory.createZone("US/Pacific");
		// make a calendar for the pacific zone
		// ...
	}
	public void createCalendar(List<String> appointments) {
		// make calendar from appointments
		System.out.println("Making the calendar");
	}
}