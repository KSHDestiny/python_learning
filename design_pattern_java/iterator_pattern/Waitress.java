package design_pattern_java.iterator_pattern;

import design_pattern_java.iterator_pattern.aggregate.Menu;
import design_pattern_java.iterator_pattern.concrete_aggregate.DinerMenu;
import design_pattern_java.iterator_pattern.concrete_aggregate.PancakeHouseMenu;
import design_pattern_java.iterator_pattern.iterator.MenuItem;
import java.util.List;
 
public class Waitress {
	Menu pancakeHouseMenu;
	Menu dinerMenu;
 
	public Waitress(Menu pancakeHouseMenu, Menu dinerMenu) {
		this.pancakeHouseMenu = pancakeHouseMenu;
		this.dinerMenu = dinerMenu;
	}
	
	// implicit iteration
	public void printMenu() {
		List<MenuItem> breakfastItems = ((PancakeHouseMenu) pancakeHouseMenu).getMenuItems();
		for (MenuItem m : breakfastItems) {
			printMenuItem(m);
		}
		
		MenuItem[] lunchItems = ((DinerMenu) dinerMenu).getMenuItems();
		for (MenuItem m : lunchItems) {
			printMenuItem(m);
		}
	}
	
	public void printMenuItem(MenuItem menuItem) {
		System.out.print(menuItem.getName() + ", ");
		System.out.print(menuItem.getPrice() + " -- ");
		System.out.println(menuItem.getDescription());
	}
}
