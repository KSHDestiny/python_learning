package design_pattern_java.iterator_pattern.aggregate;

import design_pattern_java.iterator_pattern.iterator.MenuItem;
import java.util.Iterator;

public interface Menu {
	public Iterator<MenuItem> createIterator();
}
