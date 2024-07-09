package design_pattern_java.factory_pattern_exercise;

import java.util.*;

import design_pattern_java.factory_pattern_exercise.concrete_client.PacificCalendar;
import design_pattern_java.factory_pattern_exercise.factory.ZoneFactory;

public class CalendarTestDrive {
 
	public static void main(String[] args) {
		ZoneFactory zoneFactory = new ZoneFactory();
		Calendar calendar = new PacificCalendar(zoneFactory);
		List<String> appts = Arrays.asList("appt 1", "appt 2");
		calendar.createCalendar(appts);
		calendar.print();
	}
}
