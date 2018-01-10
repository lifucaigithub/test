package g7.cucumber.utils;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.android.AndroidKeyCode;

public class ClearEditAndBackUtil {
	// clear the edit text
	public static void clearText(AndroidDriver<AndroidElement> driver,
			String text, AndroidElement ele) {
		ele.click();
		driver.pressKeyCode(AndroidKeyCode.KEYCODE_MOVE_END);
		for (int i = 0; i < text.length(); i++) {
			driver.pressKeyCode(AndroidKeyCode.BACKSPACE);
		}
	}

	// move to end
	public static void moveToEnd(AndroidDriver<AndroidElement> driver) {
		driver.pressKeyCode(AndroidKeyCode.KEYCODE_MOVE_END);
	}

	// click BACKSPACE
	public static void clickBackSpace(AndroidDriver<AndroidElement> driver) {
		driver.pressKeyCode(AndroidKeyCode.BACKSPACE);
	}

	// click back
	public static void clickAndroidBack(AndroidDriver<AndroidElement> driver) {
		driver.pressKeyCode(AndroidKeyCode.BACK);
	}

	// double click back
	public static void doubleClickAndroidBack(AndroidDriver<AndroidElement> driver) {
		driver.pressKeyCode(AndroidKeyCode.BACK);
		driver.pressKeyCode(AndroidKeyCode.BACK);

	}
}
