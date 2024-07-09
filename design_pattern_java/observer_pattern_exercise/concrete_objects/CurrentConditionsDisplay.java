package design_pattern_java.observer_pattern_exercise.concrete_objects;

import design_pattern_java.observer_pattern_exercise.subject_observer.DisplayElement;
import design_pattern_java.observer_pattern_exercise.subject_observer.Observer;
import design_pattern_java.observer_pattern_exercise.subject_observer.Subject;

public class CurrentConditionsDisplay implements Observer, DisplayElement {
	private float temperature;
	private float humidity;
	private Subject weatherData;
	
	public CurrentConditionsDisplay(Subject weatherData) {
		this.weatherData = weatherData;
		weatherData.registerObserver(this);
	}
	
	public void update(float temperature, float humidity, float pressure) {
		this.temperature = temperature;
		this.humidity = humidity;
		display();
	}
	
	public void display() {
		System.out.println("Current conditions: " + temperature 
			+ "F degrees and " + humidity + "% humidity");
	}
}
