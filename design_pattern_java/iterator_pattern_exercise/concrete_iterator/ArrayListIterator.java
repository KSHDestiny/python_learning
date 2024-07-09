package design_pattern_java.iterator_pattern_exercise.concrete_iterator;

import design_pattern_java.iterator_pattern_exercise.MenuItem;
import design_pattern_java.iterator_pattern_exercise.iterator.Iterator;
import java.util.ArrayList;


public class ArrayListIterator implements Iterator {
	ArrayList<MenuItem> items;
	int position = 0;
 
	public ArrayListIterator(ArrayList<MenuItem> items) {
		this.items = items;
	}
 
	public MenuItem next() {
		MenuItem item = items.get(position);
		position = position + 1;
		return item;
	}
 
	public boolean hasNext() {
		if (position >= items.size()) {
			return false;
		} else {
			return true;
		}
	}
}
