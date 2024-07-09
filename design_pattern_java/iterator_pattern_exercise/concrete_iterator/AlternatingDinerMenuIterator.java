package design_pattern_java.iterator_pattern_exercise.concrete_iterator;

import design_pattern_java.iterator_pattern_exercise.MenuItem;
import design_pattern_java.iterator_pattern_exercise.iterator.Iterator;
import java.util.Calendar;


public class AlternatingDinerMenuIterator implements Iterator {
	MenuItem[] list;
	int position;

	public AlternatingDinerMenuIterator(MenuItem[] list) {
		this.list = list;
		position = Calendar.DAY_OF_WEEK % 2;
	}
	public MenuItem next() {
		MenuItem menuItem = list[position];
		position = position + 2;
		return menuItem;
	}
	public boolean hasNext() {
		if (position >= list.length || list[position] == null) {
			return false;
		} else {
			return true;
		}
	}
	public String toString() {
		return "Alternating Diner Menu Iterator";
	}
}
