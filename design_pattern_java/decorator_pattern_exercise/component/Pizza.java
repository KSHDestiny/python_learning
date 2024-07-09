package design_pattern_java.decorator_pattern_exercise.component;

public abstract class Pizza {
	protected String description = "Basic Pizza";
  
	public String getDescription() {
		return description;
	}
 
	public abstract double cost();
}
