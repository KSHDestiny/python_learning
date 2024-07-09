package design_pattern_java.iterator_pattern_exercise.iterator;

import design_pattern_java.iterator_pattern_exercise.MenuItem;

public interface Iterator {
	boolean hasNext();
	MenuItem next();
}
