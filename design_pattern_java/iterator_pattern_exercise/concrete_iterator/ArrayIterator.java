package design_pattern_java.iterator_pattern_exercise.concrete_iterator;

import design_pattern_java.iterator_pattern_exercise.MenuItem;
import design_pattern_java.iterator_pattern_exercise.iterator.Iterator;


public class ArrayIterator implements Iterator {
	MenuItem[] items;
	int position = 0;
 
	public ArrayIterator(MenuItem[] items) {
		this.items = items;
	}
 
	public MenuItem next() {
		MenuItem menuItem = items[position];
		position = position + 1;
		return menuItem;
	}
 
	public boolean hasNext() {
		if (position >= items.length || items[position] == null) {
			return false;
		} else {
			return true;
		}
	}
}
