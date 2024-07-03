package design_pattern_java.strategy_pattern;

import design_pattern_java.strategy_pattern.Duck.DecoyDuck;
import design_pattern_java.strategy_pattern.Duck.Duck;
import design_pattern_java.strategy_pattern.Duck.MallardDuck;
import design_pattern_java.strategy_pattern.Duck.ModelDuck;
import design_pattern_java.strategy_pattern.Duck.RubberDuck;
import design_pattern_java.strategy_pattern.Fly.FlyBehavior;
import design_pattern_java.strategy_pattern.Fly.FlyRocketPowered;
import design_pattern_java.strategy_pattern.Quack.QuackBehavior;

public class MiniDuckSimulator {
 
	public static void main(String[] args) {
 
		MallardDuck	mallard = new MallardDuck();
		FlyBehavior cantFly = () -> System.out.println("I can't fly");
		QuackBehavior squeak = () -> System.out.println("Squeak");
		RubberDuck	rubberDuckie = new RubberDuck(cantFly, squeak);
		DecoyDuck	decoy = new DecoyDuck();
 
		Duck	 model = new ModelDuck();

		mallard.performQuack();
		rubberDuckie.performQuack();
		decoy.performQuack();
   
		model.performFly();	
		model.setFlyBehavior(new FlyRocketPowered());
		model.performFly();
	}
}
