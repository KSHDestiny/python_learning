package design_pattern_java.observer_pattern;

import design_pattern_java.observer_pattern.concrete.SimpleObserver;
import design_pattern_java.observer_pattern.concrete.SimpleSubject;

public class Example {

	public static void main(String[] args) {
		SimpleSubject simpleSubject = new SimpleSubject();
	
		SimpleObserver simpleObserver = new SimpleObserver(simpleSubject);

		simpleSubject.setValue(80);
	}
}
