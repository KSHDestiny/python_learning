package design_pattern_java.observer_pattern_exercise;

import design_pattern_java.observer_pattern_exercise.concrete_objects.CurrentConditionsDisplay;
import design_pattern_java.observer_pattern_exercise.concrete_objects.ForecastDisplay;
import design_pattern_java.observer_pattern_exercise.concrete_objects.StatisticsDisplay;
import design_pattern_java.observer_pattern_exercise.concrete_subject.WeatherData;

public class WeatherStation {

	public static void main(String[] args) {
		WeatherData weatherData = new WeatherData();
	
		CurrentConditionsDisplay currentDisplay = 
		new CurrentConditionsDisplay(weatherData);
		StatisticsDisplay statisticsDisplay = new StatisticsDisplay(weatherData);
		ForecastDisplay forecastDisplay = new ForecastDisplay(weatherData);

		weatherData.setMeasurements(80, 65, 30.4f);
		weatherData.setMeasurements(82, 70, 29.2f);
		weatherData.setMeasurements(78, 90, 29.2f);
	}
}
