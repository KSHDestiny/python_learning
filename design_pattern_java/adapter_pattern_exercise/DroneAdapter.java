package design_pattern_java.adapter_pattern_exercise;
import design_pattern_java.adapter_pattern.original_interface.Duck;

public class DroneAdapter implements Duck {
	Drone drone;
 
	public DroneAdapter(Drone drone) {
		this.drone = drone;
	}
    
	public void quack() {
		drone.beep();
	}
  
	public void fly() {
		drone.spin_rotors();
		drone.take_off();
	}
}
