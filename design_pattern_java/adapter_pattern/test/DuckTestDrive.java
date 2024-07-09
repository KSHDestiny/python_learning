package design_pattern_java.adapter_pattern.test;
import design_pattern_java.adapter_pattern.MallardDuck;
import design_pattern_java.adapter_pattern.WildTurkey;
import design_pattern_java.adapter_pattern.adapter.TurkeyAdapter;
import design_pattern_java.adapter_pattern.original_interface.Duck;
import design_pattern_java.adapter_pattern_exercise.*;

public class DuckTestDrive {
	public static void main(String[] args) {
		MallardDuck duck = new MallardDuck();

		WildTurkey turkey = new WildTurkey();
		Duck turkeyAdapter = new TurkeyAdapter(turkey);

		System.out.println("The Turkey says...");
		turkey.gobble();
		turkey.fly();

		System.out.println("\nThe Duck says...");
		testDuck(duck);

		System.out.println("\nThe TurkeyAdapter says...");
		testDuck(turkeyAdapter);
		
		// Challenge
		Drone drone = new SuperDrone();
		Duck droneAdapter = new DroneAdapter(drone);
		testDuck(droneAdapter);
	}

	static void testDuck(Duck duck) {
		duck.quack();
		duck.fly();
	}
}
