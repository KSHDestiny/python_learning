package design_pattern_java.strategy_pattern_exercise;

import design_pattern_java.strategy_pattern_exercise.PhoneCamera.BasicCameraApp;
import design_pattern_java.strategy_pattern_exercise.PhoneCamera.PhoneCameraApp;
import design_pattern_java.strategy_pattern_exercise.Strategy.Email;
import design_pattern_java.strategy_pattern_exercise.Strategy.Social;
import design_pattern_java.strategy_pattern_exercise.Strategy.Txt;
import java.util.Scanner;

public class PhotoWithPhone {
 
	public static void main(String[] args) {
 
		PhoneCameraApp cameraApp = new BasicCameraApp();
		String share = getSharing();
		switch (share) {
			case("t"): cameraApp.setShareStrategy(new Txt()); break;
			case("e"): cameraApp.setShareStrategy(new Email()); break;
			case("s"): cameraApp.setShareStrategy(new Social()); break;
			default: cameraApp.setShareStrategy(new Txt());
		}
		cameraApp.take();
		cameraApp.edit();
		cameraApp.save();
		cameraApp.share();
	}
	public static String getSharing() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Share with txt (t), email (e), or social media (s)?");
		String appName = scanner.next();
		scanner.close();
		return appName;
	}
}
