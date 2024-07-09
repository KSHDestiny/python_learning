package design_pattern_java.observer_pattern_exercise.subject_observer;

public interface Subject {
	public void registerObserver(Observer o);
	public void removeObserver(Observer o);
	public void notifyObservers();
}
