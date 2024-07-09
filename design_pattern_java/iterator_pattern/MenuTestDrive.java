package design_pattern_java.iterator_pattern;

import design_pattern_java.iterator_pattern.concrete_aggregate.DinerMenu;
import design_pattern_java.iterator_pattern.concrete_aggregate.PancakeHouseMenu;

public class MenuTestDrive {
	public static void main(String args[]) {
		PancakeHouseMenu pancakeHouseMenu = new PancakeHouseMenu();
		DinerMenu dinerMenu = new DinerMenu();
		Waitress waitress = new Waitress(pancakeHouseMenu, dinerMenu);
		// Use implicit iteration
		waitress.printMenu();
	}
}
