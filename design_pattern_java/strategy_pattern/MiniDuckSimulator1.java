package design_pattern_java.strategy_pattern;

import design_pattern_java.strategy_pattern.Duck.Duck;
import design_pattern_java.strategy_pattern.Duck.MallardDuck;
import design_pattern_java.strategy_pattern.Duck.ModelDuck;
import design_pattern_java.strategy_pattern.Fly.FlyRocketPowered;

public class MiniDuckSimulator1 {
 
	public static void main(String[] args) {
 
		Duck mallard = new MallardDuck();
		mallard.performQuack();
		mallard.performFly();
   
		Duck model = new ModelDuck();
		model.performFly();
		model.setFlyBehavior(new FlyRocketPowered());
		model.performFly();

	}
}
