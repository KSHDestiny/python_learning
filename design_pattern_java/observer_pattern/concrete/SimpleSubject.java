package design_pattern_java.observer_pattern.concrete;

import java.util.*;

import design_pattern_java.observer_pattern.subject_observer.Subject;
import design_pattern_java.observer_pattern.subject_observer.Observer;

public class SimpleSubject implements Subject {
	private ArrayList<Observer> observers;
	private int value = 0;
	
	public SimpleSubject() {
		observers = new ArrayList<Observer>();
	}
	
	public void registerObserver(Observer o) {
		observers.add(o);
	}
	
	public void removeObserver(Observer o) {
		int i = observers.indexOf(o);
		if (i >= 0) {
			observers.remove(i);
		}
	}
	
	public void notifyObservers() {
		for (Observer observer : observers) {
			observer.update(value);
		}
	}
	
	public void setValue(int value) {
		this.value = value;
		notifyObservers();
	}
}